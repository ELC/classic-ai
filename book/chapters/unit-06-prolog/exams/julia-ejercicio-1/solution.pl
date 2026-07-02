inicio :- write('lista 1:'), leer(L1), write('lista 2:'), leer(L2),
comparaLis(L1,L2).

comparaLis(L1,L2) :- cant(L1,C), cant(L2,C), similitud(L1,L2,N),
Valor is N/C, clasifica(Valor).
comparaLis(_,_) :- write('Listas de distintas Longitudes').

cant([],0).
cant([_|T],N):- cant(T,N1), N is N1 + 1.

similitud([],[],0).
similitud([H|T1],[H|T2],N):- similitud(T1,T2,N1), N is N1 + 1.
similitud([_|T1],[_|T2],N):- similitud(T1,T2,N).


clasifica(N):- N = 1, write('Identicas') .
clasifica(N):- N>=(0.75), write('Muy Parecidas') .
clasifica(N):- N>=(0.25), write('Parecidas') .
clasifica(N):- N>= 0, write('Poco Parecidas') .
clasifica(N):- N = 0, write('Nada Parecidas') .

leer([H|T]):-read(H), H\=[], leer(T).
leer([]).
