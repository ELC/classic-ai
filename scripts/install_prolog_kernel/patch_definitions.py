from .models import PrologPatch


TERM_BINDINGS_IMPORT_PATCH = PrologPatch(
    old=""":- if(sicstus).
:- use_module(library(aggregate), [forall/2]).
:- use_module(library(file_systems), [delete_file/1]).
:- use_module(jupyter_variable_bindings, [term_with_stored_var_bindings/4, store_var_bindings/1]).
:- endif.""",
    new=""":- use_module(jupyter_variable_bindings, [term_with_stored_var_bindings/4, store_var_bindings/1]).

:- if(sicstus).
:- use_module(library(aggregate), [forall/2]).
:- use_module(library(file_systems), [delete_file/1]).
:- endif.""",
)
TERM_REPLACE_BINDINGS_PATCH = PrologPatch(
    old=""":- if(swi).
replace_previous_variable_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings, Exception) :-
  catch(toplevel_variables:expand_query(Term, UpdatedTerm, Bindings, UpdatedBindings), Exception, true).
:- else.
replace_previous_variable_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings, Exception) :-
  catch(jupyter_variable_bindings:term_with_stored_var_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings), Exception, true).
:- endif.""",
    new="""replace_previous_variable_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings, Exception) :-
  catch(jupyter_variable_bindings:term_with_stored_var_bindings(Term, Bindings, UpdatedTerm, UpdatedBindings), Exception, true).""",
)
TERM_UPDATE_BINDINGS_PATCH = PrologPatch(
    old=""":- if(swi).
update_variable_bindings(BindingsWithoutSingletons) :-
  toplevel_variables:expand_answer(BindingsWithoutSingletons, _NewBindings).
:- else.
update_variable_bindings(BindingsWithoutSingletons) :-
  jupyter_variable_bindings:store_var_bindings(BindingsWithoutSingletons).
:- endif.""",
    new="""update_variable_bindings(BindingsWithoutSingletons) :-
  jupyter_variable_bindings:store_var_bindings(BindingsWithoutSingletons).""",
)
QUERY_PROCESS_FILE_NAME_PATCH = PrologPatch(
    old="""file_name(stdout, '.server_stdout').
file_name(message_output, '.message_output').
file_name(output, '.server_output').
file_name(test, 'test_definition.pl').""",
    new="""file_name(stdout, FileName) :- process_file_name('.server_stdout', FileName).
file_name(message_output, FileName) :- process_file_name('.message_output', FileName).
file_name(output, FileName) :- process_file_name('.server_output', FileName).
file_name(test, FileName) :- process_file_name('test_definition.pl', FileName).

process_file_name(BaseName, FileName) :-
  current_prolog_flag(pid, Pid),
  atomic_list_concat([BaseName, '.', Pid], FileName).""",
)

TERM_HANDLING_PATCHES = (
    TERM_BINDINGS_IMPORT_PATCH,
    TERM_REPLACE_BINDINGS_PATCH,
    TERM_UPDATE_BINDINGS_PATCH,
)
QUERY_HANDLING_PATCHES = (
    QUERY_PROCESS_FILE_NAME_PATCH,
)
