:-dynamic(heladeria/3).
:-dynamic(locales/3).

inicio:-retractall(heladeria(_,_,_)),retractall(locales(_,_,_)),menu.

menu:-writeln('INGRESE OPCION'),
        writeln('OPCION 0 - SALIR'),
        writeln('OPCION 1 - INGRESAR COD HELADERIA Y LISTAR LAS QUE TIENEN SUC EN EL CENTRO'),
        writeln('OPCION 2 - INGRESAR UNA CALLE Y DEVOLVER NOMBRES D HELADERIAS SIN REPETIR QUE TIENEN EN ESA CALLE'),
        read(Op),
        Op\=0,
        Op<3,
        opcion(Op),
        menu.

menu:- writeln('GRACIAS POR USAR SISTEMA EXPERTO').

opcion(1):- abrir_base,
            writeln('Ingrese codigos de heladerias'),
            leer(ListaHela),
            mostrar_hela_centro(ListaHela).

opcion(2):- abrir_base,
            writeln('Ingresar Calle'),
            read(Calle),
            mostrar_calle_hela(Calle,[]).

opcion(_).
abrir_base:-consult('bdheladerias.txt').

leer([H|T]):-read(H),H\=[],leer(T).
leer([]).

mostrar_hela_centro([]).
mostrar_hela_centro([H|T]):- retract(locales(H,Zona,_)),
                            Zona = 'centro',
                            writeln(H),
                            mostrar_hela_centro(T).
mostrar_hela_centro([_|T]):-mostrar_hela_centro(T).


mostrar_calle_hela(Calle,SinRep):-retract(locales(Id,_,ListaSucursales)),
                                    validar_lista(Calle,ListaSucursales),
                                    not(pertenece(Id,SinRep)),
                                    retract(heladeria(Id,Nombre,_)),
                                    writeln(Nombre),
                                    mostrar_calle_hela(Calle,[Id|SinRep]).
mostrar_calle_hela(_,[]).

validar_lista(Calle,[H|_]):- sub_atom(H,0,_,_,Calle).
validar_lista(Calle,[_|T]):- validar_lista(Calle,T).

pertenece(H,[H|_]).
pertenece(H,[_|T]):-pertenece(H,T).