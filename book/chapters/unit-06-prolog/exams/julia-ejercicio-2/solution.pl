inicio :- write('lista 1:'), leer(L1), write('elemento:'), read(A),
limpiezaLista(L1,L2,A,N), write('Lista Limpia:'), write(L2),
nl, write('Esta Repetido: '), write(N), write('veces').

leer([H|T]):-read(H), H\=[], leer(T).
leer([]).

limpiezaLista([H|T1],T2,H,N):-limpiezaLista(T1,T2,H,N1), N is N1 + 1.
limpiezaLista([H|T1],[H|T2],C,N):-limpiezaLista(T1,T2,C,N).
limpiezaLista([],[],_,0).
