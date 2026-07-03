from __future__ import annotations

import sys
from pathlib import Path

from jupyter_client import KernelManager


PRACTICE_GLOB = "book/chapters/unit-06-prolog/practica-0*.md"
KERNEL_TIMEOUT_SECONDS = 60


def prolog_cells(path: Path) -> list[tuple[int, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    cells: list[tuple[int, str]] = []
    in_cell = False
    start = 0
    body: list[str] = []

    for line_number, line in enumerate(lines, start=1):
        if not in_cell and line.strip() == "```{code-cell} prolog":
            in_cell = True
            start = line_number
            body = []
            continue

        if in_cell and line.strip() == "```":
            code = "\n".join(body).strip()
            if code and has_executable_prolog(code):
                cells.append((start, code))
            in_cell = False
            continue

        if in_cell and not line.strip().startswith(":"):
            body.append(line)

    return cells


def has_executable_prolog(code: str) -> bool:
    return any(line.strip() and not line.strip().startswith("%") for line in code.splitlines())


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


def check_page(client, path: Path) -> list[str]:
    errors: list[str] = []
    for line_number, code in prolog_cells(path):
        status, output = execute(client, code)
        if status != "ok":
            errors.append(
                "\n".join(
                    [
                        f"{path}:{line_number} failed with status {status}",
                        "Code:",
                        code,
                        "Output:",
                        output.strip(),
                    ]
                )
            )

    return errors


def main() -> int:
    paths = sorted(Path().glob(PRACTICE_GLOB))
    kernel_manager = KernelManager(kernel_name="prolog_kernel")
    kernel_manager.start_kernel()
    client = kernel_manager.client()
    client.start_channels()

    try:
        client.wait_for_ready(timeout=KERNEL_TIMEOUT_SECONDS)
        errors = [error for path in paths for error in check_page(client, path)]
    finally:
        client.stop_channels()
        kernel_manager.shutdown_kernel(now=True)

    if errors:
        print("\n\n".join(errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
