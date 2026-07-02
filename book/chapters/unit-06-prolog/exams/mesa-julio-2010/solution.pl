julio2010:- dynamic(codigo/1), dynamic(empleado/3), dynamic(trabajo/3), consult('empleados.txt'), menu.
menu:- write('Ingrese una Opcion'),nl,
write(' 1 - Nuevo Empleado'),nl,
write(' 2 - Agregar Trabajo'),nl,
write(' 3 - lista importes por empleado'),nl,
write(' 4 - Lista Todo'),nl,
write(' 5 - Salir'),nl,
read(X),opcion(X).

opcion(1):- write('Nombre:' ),read(N),
write('Apellido: '),read(A),
codigo(Nro), Cod is Nro+1, retract(codigo(Nro)),assert(codigo(Cod)),
assert(empleado(Cod,N,A)),
menu.
opcion(2):- write('cod Empleado: '), read(N),
write('Trabajo: '), read(T),
write('Precio: '), read(P),
assert(trabajo(N,T,P)),
menu.
opcion(3):- guardar, write('Listado de Sueldo Total'), nl, listaSueldo.
opcion(4):- nl, write('Listado de empleados'), nl,listaEmpleado.
opcion(5):- guardar.

listaSueldo:- nl, empleado(X,N,A),
write('codigo: '), write(X),
write('Nombre: '), write(N),
write(' Apellido: '), write(A),
write(' Sueldo: '), totalsueldo(X,T),
write(T), nl, fail.
listaSueldo:- retractall(trabajo), consult('empleados.txt'), nl, menu.

totalsueldo(X,T):-sueldo(X,T).
sueldo(X,T):- trabajo(X,D,P), retract(trabajo(X,D,P)), sueldo(X,T1), T is T1 + P.
sueldo(_,0).

listaEmpleado:- empleado(X,N,A), write('codigo: '), write(X),
write(' Nombre: '), write(N),
write(' Apellido: '),write(A), nl, fail.
listaEmpleado:- nl, menu.

guardar:- tell('empleados.txt'),
listing(codigo),
listing(empleado),
listing(trabajo),
told.
