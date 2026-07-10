from importlib.util import find_spec
from pathlib import Path

from .errors import PrologKernelPackageNotFoundError
from .models import FrozenModel, PatchFile, PatchPlan, PrologKernelPackage
from .patch_definitions import QUERY_HANDLING_PATCHES, TERM_HANDLING_PATCHES


class PrologPatchPlanner(FrozenModel):
    @property
    def outputs(self) -> list[PatchPlan]:
        prolog_server_path = self._package.path / "prolog_server"
        patch_files = [
            PatchFile(
                path=prolog_server_path / "jupyter_term_handling.pl",
                patches=TERM_HANDLING_PATCHES,
            ),
            PatchFile(
                path=prolog_server_path / "jupyter_query_handling.pl",
                patches=QUERY_HANDLING_PATCHES,
            ),
        ]
        return [PatchPlan.from_file(patch_file) for patch_file in patch_files]

    @property
    def _package(self) -> PrologKernelPackage:
        spec = find_spec("prolog_kernel")
        if spec is None or spec.origin is None:
            raise PrologKernelPackageNotFoundError
        package_path = Path(spec.origin).resolve().parent
        return PrologKernelPackage(path=package_path)
