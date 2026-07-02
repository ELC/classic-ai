:-dynamic(unidades/3).
:-dynamic(viajes/2).

inicio:-retractall(unidades(_,_,_)),retractall(viajes(_,_)),menu.

menu:- writeln('Ingrese opcion'),
        writeln('OPCION 0: Salir'),
        writeln('OPCION 1: Calcular total de viajes para cada unidad'),
        writeln('OPCION 2: Ingresar una lista de unidades, y listar las que tengan viajes mayores a 500'),
        read(Op),
        Op \=0,
        Op<3,
        opcion(Op),
        menu.

menu:- writeln('Gracias por usar el sistema experto!').

opcion(1):- abrir_base,
            calcular_viajes.

opcion(2):- abrir_base,
            writeln('Ingrese lista de unidades'),
            leer(ListaU),
            mayores(ListaU).
opcion(_).

abrir_base:- consult('bdviajes.txt').

calcular_viajes:- unidades(Nro,_,_),
                retract(unidades(Nro,_,_)),
                total_viajes_x_unidad(Nro, Cont),
                writeln('La cantidad de viajes para la unidad  '),writeln(Nro),write(' es '),write(Cont),
                calcular_viajes.
calcular_viajes.

total_viajes_x_unidad(Num,C):-viajes(Num,_),
                                retract(viajes(Num,_)),
                                total_viajes_x_unidad(Num,CNuevo),
                                C is CNuevo + 1.
total_viajes_x_unidad(_,0).

leer([H|T]):-read(H),H\=[],leer(T).
leer([]).

mayores([]).
mayores([H|Lista]):-
                retract(unidades(H,_,_)),
                ver_montos_viajes(C,H),
                C>0,
                writeln(H),
                mayores(Lista).
mayores([_|Lista]):-mayores(Lista).

ver_montos_viajes(C,Cod):-retract(viajes(Cod,Monto)),
                        Monto>500,
                        ver_montos_viajes(Conta,Cod),
                        C is Conta + 1.
ver_montos_viajes(0,_).
