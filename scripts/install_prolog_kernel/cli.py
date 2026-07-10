import sys

import typer
from pydantic import ValidationError

from .errors import PrologKernelInstallError
from .kernel_spec import KernelSpecPatcher
from .models import FileOutput
from .patches import PrologPatchPlanner


app = typer.Typer(
    help="Install and patch the Prolog Jupyter kernel.",
    invoke_without_command=True,
)


@app.callback()
def install() -> None:
    """Install the Prolog kernelspec and apply compatibility patches."""
    kernel_spec_patcher = KernelSpecPatcher()
    source_patcher = PrologPatchPlanner()
    try:
        typer.echo("Installing Prolog kernel spec")
        kernel_spec_patcher.install_kernel_spec()
        outputs: list[FileOutput] = [
            *source_patcher.outputs,
            *kernel_spec_patcher.outputs,
        ]
        for output in outputs:
            output.write()
    except (PrologKernelInstallError, ValidationError) as error:
        typer.echo(str(error), err=True)
        raise typer.Exit(1) from error


def main() -> int:
    try:
        app()
    except SystemExit as error:
        return int(error.code or 0)
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        return 130
    return 0
