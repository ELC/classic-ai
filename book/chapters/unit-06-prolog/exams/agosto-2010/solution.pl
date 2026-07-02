ago2010:- dynamic(aguda/2), dynamic(grave/2),consult('palabras.txt'), nl,
write('lista de palabras: '), leer(T),
agregarpalabras(T),terminacion('n',C1),
terminacion('s',C2), terminacion('o',C3),
nl, write('terminadas en N: '), write( C1 ),
nl, write('terminadas en S: '), write( C2 ),
nl, write('terminadas en o: '), write( C3 ).

leer([H|T]):- read(H), H\=[], leer(T).
leer([]).

agregarpalabras([]).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'n'),
assert(aguda(H,'n')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 's'),
assert(aguda(H,'s')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'a'),
assert(aguda(H,'a')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'e'),
assert(aguda(H,'e')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'i'),
assert(aguda(H,'i')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'o'),
assert(aguda(H,'o')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'u'),
assert(aguda(H,'u')), agregarpalabras(T).

terminacion(X,Cant):- aguda(P,X), retract(aguda(P,X)), terminacion(X,Cant1), Cant is Cant1 + 1.
terminacion(_,0).

litarAgudas:- aguda(P,V), nl, write(P), write(V), fail.
