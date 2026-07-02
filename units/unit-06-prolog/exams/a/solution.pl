inicio:-write('ingrese cadena 1:'),read(A),
write('ingrese Cadena 2:'),read(B),
intercepcion(A,B,L),
write('Lista Comun:'), write(L).
intercepcion(A,B,[H|T]):-
atom_length(A,NA),
atom_length(B,NB),
NA > 0, NB > 0,
sub_atom(A,0,1,NA1,H),
sub_atom(A,1,NA1,_,A1),
esta(H,B), intercepcion(A1,B,T).
intercepcion(A,B,T):-
atom_length(A,NA),
atom_length(B,NB),
NA > 0, NB > 0,
sub_atom(A,0,1,NA1,_),
sub_atom(A,1,NA1,_,A1),
intercepcion(A1,B,T).

intercepcion(_,_,[]).

esta(H,B):-atom_length(B,NB), NB > 0,
sub_atom(B,0,1,_,H).
esta(H,B):-atom_length(B,NB), NB > 0,
NB1 is NB-1,
sub_atom(B,1,NB1,_,B1),
esta(H,B1).



inicio:- dynamic(cod/1), dynamic(receta/2), dynamic(ingrediente/3),consult('recetas1.txt'), menu.

menu:- nl, write('1 Alta de Receta'),
nl, write('2 Baja de Receta'),
nl, write('3 Alta de Ingrediente'),
nl, write('4 Baja de Ingrediente'),
nl, write('5 Consulta todo'),
nl, write('6 Consuta Dos Ingrediente'),
nl, write('7 Salir'),
nl, nl, write('Ingrese una opcion: '), read(A), opcion(A).

opcion(1):- nl, write('Ingrese Nuevo Nombre Receta: '), read(N),
cod(Nro), Cod is Nro + 1, retract(cod(Nro)),assert(cod(Cod)),
assert(receta(Cod,N)), menu.
opcion(2):- nl, write('Ingrese Codigo de Receta a eliminar: '), read(C),
retract(receta(C,_)),menu.
opcion(3):- nl, write('Ingrese Codigo de Receta: '), read(C),
write('Ingrese Nuevo Ingrediente: '), read(I),
write('Cantidad Ingrediente: '), read(N),
assert(ingrediente(C,I,N)),menu.
opcion(4):- nl, write('Codigo de Receta:'), read(C),
write('Nombre Ingrediente a Eliminar: '), read(I),
retract(ingrediente(C, I,_)),menu.
opcion(5):- nl, write(' Lista de Recetas '), listarecetas.
opcion(6):- nl, write(' ingrediente 1: '), read(I1),
write(' Ingrediente 2: '), read(I2),
nl, write('Lista de ingredientes ' ),
listaingr(I1, I2).
opcion(_):- tell('recetas1.txt'),
listing(cod),
listing(receta),
listing(ingrediente),
told.

listarecetas:- receta(C, N), nl, write('Cod: '), write(C),
write(' - '), write(N),fail.
listarecetas:- nl, menu.

listaingr(I1,I2):- ingrediente(C, I1,_), ingrediente(C, I2,_),
receta(C, N), write(C), write(' - '), write(N), fail.
listaingr(_,_):- nl, menu.
