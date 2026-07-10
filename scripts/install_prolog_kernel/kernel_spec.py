import shutil
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Self

from jupyter_client.kernelspec import KernelSpec, KernelSpecManager
from pydantic import Field

from .config import (
    KERNEL_NAME,
    KERNELSPEC_SOURCE_DIR,
)
from .models import (
    FileOutput,
    FrozenModel,
    SwiplBin,
    SwiplBinDefaultWin,
    SwiplBinFound,
)


class KernelJson(FrozenModel):
    path: Path = Field(exclude=True)
    argv: Sequence[str] = Field(default_factory=tuple)
    display_name: str = Field(min_length=1)
    env: Mapping[str, object] = Field(default_factory=dict)
    language: str = Field(min_length=1)

    @classmethod
    def from_spec(cls, spec: KernelSpec) -> Self:
        kernel_json_path = Path(spec.resource_dir) / "kernel.json"
        return cls(
            path=kernel_json_path,
            argv=tuple(spec.argv),
            display_name=spec.display_name,
            env=dict(spec.env),
            language=spec.language,
        )

    def update_from_kernel_name(self, kernel_name: str) -> Self:
        return self.model_copy(
            update={
                "argv": (
                    sys.executable,
                    "-m",
                    kernel_name,
                    "-f",
                    "{connection_file}",
                ),
            },
        )

    def update_from_swipl_bin(self, swipl_bin: SwiplBin) -> Self:
        env = dict(self.env)
        env.update(swipl_bin.env_overwrites)
        return self.model_copy(update={"env": env})

    def to_json(self) -> str:
        return self.model_dump_json(indent=2) + "\n"


class KernelSpecPatcher(FrozenModel):
    manager: KernelSpecManager = Field(default_factory=KernelSpecManager)

    def install_kernel_spec(self) -> None:
        self.manager.install_kernel_spec(
            KERNELSPEC_SOURCE_DIR,
            KERNEL_NAME,
            user=True,
        )

    @property
    def _swipl_bin(self) -> SwiplBin:
        swipl = shutil.which("swipl")
        if swipl is not None:
            swipl_path = Path(swipl).resolve().parent
            return SwiplBinFound(path=swipl_path)
        return SwiplBinDefaultWin()

    @property
    def outputs(self) -> list[FileOutput]:
        spec = self.manager.get_kernel_spec(KERNEL_NAME)
        update = (
            KernelJson.from_spec(spec)
            .update_from_kernel_name(KERNEL_NAME)
            .update_from_swipl_bin(self._swipl_bin)
        )
        return [FileOutput(path=update.path, text=update.to_json())]
