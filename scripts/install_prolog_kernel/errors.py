from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PrologKernelInstallError(Exception):
    """Base class for expected Prolog kernel installation failures."""


@dataclass(frozen=True)
class PrologKernelPackageNotFoundError(PrologKernelInstallError):
    def __str__(self) -> str:
        return "prolog_kernel is not installed"


@dataclass(frozen=True)
class PrologPatchApplicationError(PrologKernelInstallError):
    path: Path

    def __str__(self) -> str:
        return f"Could not apply prolog-kernel compatibility patch to {self.path}"
