from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

from jupyter_client import KernelManager


PRACTICE_GLOB = "book/chapters/unit-06-prolog/practica-0*.md"
KERNEL_TIMEOUT_SECONDS = 60
VERIFICATION_HEADINGS = {"### Verificación", "### Verificacion"}
ASSERTION_PATTERN = re.compile(r"\bassertion\s*\(")
FALSE_RESULT_PATTERN = re.compile(r"^\s*(false|no)\.?\s*$", re.IGNORECASE | re.MULTILINE)


@dataclass(frozen=True)
class PrologCell:
    line_number: int
    code: str
    is_verification: bool


def prolog_cells(path: Path) -> list[PrologCell]:
    lines = path.read_text(encoding="utf-8").splitlines()
    cells: list[PrologCell] = []
    in_cell = False
    in_verification_section = False
    start = 0
    body: list[str] = []

    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not in_cell and stripped.startswith("#"):
            in_verification_section = stripped in VERIFICATION_HEADINGS

        if not in_cell and line.strip() == "```{code-cell} prolog":
            in_cell = True
            start = line_number
            body = []
            continue

        if in_cell and line.strip() == "```":
            code = "\n".join(body).strip()
            if code and has_executable_prolog(code):
                cells.append(PrologCell(start, code, in_verification_section))
            in_cell = False
            continue

        if in_cell and not line.strip().startswith(":tags:"):
            body.append(line)

    return cells


def has_executable_prolog(code: str) -> bool:
    return any(line.strip() and not line.strip().startswith("%") for line in code.splitlines())


def has_assertion(code: str) -> bool:
    return ASSERTION_PATTERN.search(code) is not None


def has_false_result(output: str) -> bool:
    return FALSE_RESULT_PATTERN.search(output) is not None


def execute(client, code: str) -> tuple[str, str]:
    message_id = client.execute(code)
    outputs: list[str] = []

    while True:
        message = client.get_iopub_msg(timeout=KERNEL_TIMEOUT_SECONDS)
        if message["parent_header"].get("msg_id") != message_id:
            continue

        message_type = message["msg_type"]
        content = message["content"]
        if message_type == "stream":
            outputs.append(content["text"])
        elif message_type == "error":
            outputs.append("\n".join(content["traceback"]))
        elif message_type in {"execute_result", "display_data"}:
            outputs.append(str(content["data"].get("text/plain", "")))
        elif message_type == "status" and content["execution_state"] == "idle":
            break

    reply = client.get_shell_msg(timeout=KERNEL_TIMEOUT_SECONDS)
    while reply["parent_header"].get("msg_id") != message_id:
        reply = client.get_shell_msg(timeout=KERNEL_TIMEOUT_SECONDS)

    return reply["content"].get("status", "error"), "".join(outputs)


def format_error(path: Path, line_number: int, message: str, code: str, output: str = "") -> str:
    parts = [
        f"{path}:{line_number} {message}",
        "Code:",
        code,
    ]
    if output:
        parts.extend(["Output:", output.strip()])
    return "\n".join(parts)


def check_page(client, path: Path) -> list[str]:
    errors: list[str] = []
    for cell in prolog_cells(path):
        if cell.is_verification and not has_assertion(cell.code):
            errors.append(
                format_error(
                    path,
                    cell.line_number,
                    "verification cell must contain assertion/1",
                    cell.code,
                )
            )

        status, output = execute(client, cell.code)
        if status != "ok":
            errors.append(
                format_error(
                    path,
                    cell.line_number,
                    f"failed with status {status}",
                    cell.code,
                    output,
                )
            )
        elif has_false_result(output):
            errors.append(
                format_error(
                    path,
                    cell.line_number,
                    "failed with false result",
                    cell.code,
                    output,
                )
            )

    return errors


def main() -> int:
    paths = sorted(Path().glob(PRACTICE_GLOB))
    errors: list[str] = []

    for path in paths:
        kernel_manager = KernelManager(kernel_name="prolog_kernel")
        kernel_manager.start_kernel()
        client = kernel_manager.client()
        client.start_channels()

        try:
            client.wait_for_ready(timeout=KERNEL_TIMEOUT_SECONDS)
            errors.extend(check_page(client, path))
        finally:
            client.stop_channels()
            kernel_manager.shutdown_kernel(now=True)

    if errors:
        print("\n\n".join(errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
