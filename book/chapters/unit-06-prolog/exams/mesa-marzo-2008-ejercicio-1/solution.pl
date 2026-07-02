inicio :- write( 'ingrese una lista:' ), leer(L1), ultimo(L1,U),
modiParImpar(L1,U,L2), write( 'Lista modificada: ' ),
write(L2).

modiParImpar([],_,[]).
modiParImpar(L1,U,L2) :- R is U mod 2, R = 0, agregaCont(L1,L2).% Si es Par
modiParImpar(L1,_,L2) :- agregaCero(L1,L2).% Si es Impar

agregaCero([],[]).
agregaCero([_|L1],[0|L2]):-agregaCont(L1,L2).

agregaCont([],[]).
agregaCont([H|L1],[H|L2]):-agregaCero(L1,L2).

leer([H|T]):-read(H), H \= [], leer(T).
leer([]).

ultimo([_|T],U):- ultimo(T,U).
ultimo([U|[]],U).
