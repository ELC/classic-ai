inicio:- write('Ingrese un Número:'), read(A),suma_hasta(A,S), write(S).

suma_hasta(0,0).
suma_hasta(A,S):-A1 is A - 1, suma_hasta( A1,S1 ), S is S1 + A.
