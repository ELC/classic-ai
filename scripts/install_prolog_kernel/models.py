from collections.abc import Sequence
from enum import StrEnum, auto
from pathlib import Path
from typing import Self

from pydantic import BaseModel, ConfigDict, Field

from .config import WINDOWS_SWIPL_BIN, WINDOWS_SWIPL_HOME
from .errors import PrologPatchApplicationError


class FrozenModel(BaseModel):
    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)


class PrologPatch(FrozenModel):
    old: str = Field(min_length=1)
    new: str = Field(min_length=1)


class PatchFile(FrozenModel):
    path: Path
    patches: Sequence[PrologPatch]


class FileOutput(FrozenModel):
    path: Path
    text: str

    def write(self) -> None:
        self.path.write_text(self.text, encoding="utf-8")


class PatchPlan(FileOutput):
    @classmethod
    def from_file(cls, patch_file: PatchFile) -> Self:
        text = patch_file.path.read_text(encoding="utf-8")
        for patch in patch_file.patches:
            if patch.old in text:
                text = text.replace(patch.old, patch.new)
            elif patch.new not in text:
                raise PrologPatchApplicationError(path=patch_file.path)
        return cls(path=patch_file.path, text=text)


class PrologKernelPackage(FrozenModel):
    path: Path


class SwiplBinKind(StrEnum):
    FOUND = auto()
    DEFAULT_WIN = auto()


class SwiplBinFound(FrozenModel):
    kind: SwiplBinKind = SwiplBinKind.FOUND
    path: Path

    @property
    def env_overwrites(self) -> dict[str, str]:
        return {"PATH": str(self.path)}


class SwiplBinDefaultWin(FrozenModel):
    kind: SwiplBinKind = SwiplBinKind.DEFAULT_WIN
    path: Path = WINDOWS_SWIPL_BIN

    @property
    def env_overwrites(self) -> dict[str, str]:
        return {
            "PATH": str(self.path),
            "SWI_HOME_DIR": str(WINDOWS_SWIPL_HOME),
        }


SwiplBin = SwiplBinFound | SwiplBinDefaultWin
