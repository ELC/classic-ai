inicio:- write('Ingrese Cadena: '), read(A) , sumaletra( A, N ),
write('La suma ascii de los caracteres de la cadena es: '), write(N).

sumaletra(A,0):- atom_length(A,0).
sumaletra(A,N):- sub_atom(A,0,1,Cant,C), atom_char(C,N1),
sub_atom(A,1,Cant,_,A1), sumaletra(A1,N2),
N is N1 + N2.
