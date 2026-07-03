from __future__ import annotations

import json
import shutil
import subprocess
import sys
from importlib.util import find_spec
from pathlib import Path

from jupyter_client.kernelspec import KernelSpecManager


STALE_KERNELS = ("calysto_prolog", "logtalk_kernel")
WINDOWS_SWIPL_BIN = Path("C:/Program Files/swipl/bin")
WINDOWS_SWIPL_HOME = Path("C:/Program Files/swipl")
TERM_HANDLING_PATCHES = (
    (
        """:- if(sicstus).
:- use_module(library(aggregate), [forall/2]).
:- use_module(library(file_systems), [delete_file/1]).
:- use_module(jupyter_variable_bindings, [term_with_stored_var_bindings/4, store_var_bindings/1]).
:- endif.""",
        """:- use_module(jupyter_variable_bindings, [term_with_stored_var_bindings/4, store_var_bindings/1]).

:- if(sicstus).
:- use_module(library(aggregate), [forall/2]).
:- use_module(library(file_systems), [delete_file/1]).
:- endif.""",
    ),
    (
        """:- if(swi).
replace_previous_variable_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings, Exception) :-
  catch(toplevel_variables:expand_query(Term, UpdatedTerm, Bindings, UpdatedBindings), Exception, true).
:- else.
replace_previous_variable_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings, Exception) :-
  catch(jupyter_variable_bindings:term_with_stored_var_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings), Exception, true).
:- endif.""",
        """replace_previous_variable_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings, Exception) :-
  catch(jupyter_variable_bindings:term_with_stored_var_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings), Exception, true).""",
    ),
    (
        """:- if(swi).
update_variable_bindings(BindingsWithoutSingletons) :-
  toplevel_variables:expand_answer(BindingsWithoutSingletons, _NewBindings).
:- else.
update_variable_bindings(BindingsWithoutSingletons) :-
  jupyter_variable_bindings:store_var_bindings(BindingsWithoutSingletons).
:- endif.""",
        """update_variable_bindings(BindingsWithoutSingletons) :-
  jupyter_variable_bindings:store_var_bindings(BindingsWithoutSingletons).""",
    ),
)
QUERY_HANDLING_PATCHES = (
    (
        """file_name(stdout, '.server_stdout').
file_name(message_output, '.message_output').
file_name(output, '.server_output').
file_name(test, 'test_definition.pl').""",
        """file_name(stdout, FileName) :- process_file_name('.server_stdout', FileName).
file_name(message_output, FileName) :- process_file_name('.message_output', FileName).
file_name(output, FileName) :- process_file_name('.server_output', FileName).
file_name(test, FileName) :- process_file_name('test_definition.pl', FileName).

process_file_name(BaseName, FileName) :-
  current_prolog_flag(pid, Pid),
  atomic_list_concat([BaseName, '.', Pid], FileName).""",
    ),
)


def remove_stale_kernels(manager: KernelSpecManager) -> None:
    for kernel_name in STALE_KERNELS:
        try:
            manager.remove_kernel_spec(kernel_name)
        except Exception:  # noqa: BLE001 - kernels may be absent or user-owned.
            continue


def swipl_bin_directory() -> str | None:
    swipl = shutil.which("swipl")
    if swipl is not None:
        return str(Path(swipl).resolve().parent)
    if WINDOWS_SWIPL_BIN.exists():
        return str(WINDOWS_SWIPL_BIN)
    return None


def patch_kernel_json(manager: KernelSpecManager) -> None:
    spec = manager.get_kernel_spec("prolog_kernel")
    kernel_json_path = Path(spec.resource_dir) / "kernel.json"
    data = json.loads(kernel_json_path.read_text(encoding="utf-8"))

    data["argv"] = [
        sys.executable,
        "-m",
        "prolog_kernel",
        "-f",
        "{connection_file}",
    ]

    env = dict(data.get("env", {}))
    swipl_bin = swipl_bin_directory()
    if swipl_bin is not None:
        env["PATH"] = swipl_bin
    if WINDOWS_SWIPL_HOME.exists():
        env["SWI_HOME_DIR"] = str(WINDOWS_SWIPL_HOME)
    data["env"] = env

    kernel_json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def prolog_kernel_package_directory() -> Path:
    spec = find_spec("prolog_kernel")
    if spec is None or spec.origin is None:
        raise RuntimeError("prolog_kernel is not installed")
    return Path(spec.origin).resolve().parent


def apply_patches(path: Path, patches: tuple[tuple[str, str], ...]) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in patches:
        if old in text:
            text = text.replace(old, new)
        elif new not in text:
            raise RuntimeError(f"Could not apply prolog-kernel compatibility patch to {path}")
    path.write_text(text, encoding="utf-8")


def patch_prolog_server_sources() -> None:
    prolog_server_path = prolog_kernel_package_directory() / "prolog_server"
    apply_patches(prolog_server_path / "jupyter_term_handling.pl", TERM_HANDLING_PATCHES)
    apply_patches(prolog_server_path / "jupyter_query_handling.pl", QUERY_HANDLING_PATCHES)


def main() -> None:
    subprocess.run(
        [sys.executable, "-m", "prolog_kernel.install", "--user"],
        check=True,
    )
    patch_prolog_server_sources()
    manager = KernelSpecManager()
    remove_stale_kernels(manager)
    patch_kernel_json(manager)


if __name__ == "__main__":
    main()
