:-dynamic(computadora/5).
:-dynamic(ventas/3).

inicio:-retractall(computadora(_,_,_,_,_)),retractall(ventas(_,_,_)),menu.

menu:- writeln('INGRESE OPCION DESEADA'),
        writeln('O - SALIR'),
        writeln('1 - INGRESAR MES Y ANIO, Y MOSTRAR MONTO RECAUDADO ESE MES'),
        writeln('2 - INGRESAR LISTA DE CARACTERISTICAS Y DEVOLVER EN UNA NUEVA LISTA SIN REPETIR LOS ID DE LAS PC Q TENGAN ESAS CARACTERISTICAS'),
        read(Op),
        Op\=0,
        Op<3,
        opcion(Op),
        menu.

menu:- writeln('Gracias por usar este sistema experto').

opcion(1):- abrir_base,
            writeln('INGRESE MES Y ANIO: AAAA-MM'),
            read(Mesanio),
            calcular_monto(Mesanio,Monto),
            writeln('El monto es de '),writeln(Monto).

opcion(2):- abrir_base,
            writeln('Ingresar lista carcteristicas'),
            leer(ListaCar),
            buscar_computadoras(ListaCar,NuevaLista,[]),
            writeln(NuevaLista).

opcion(_).

abrir_base:-consult('bdcompus.txt').

calcular_monto(Mesanio,M):- retract(ventas(_,Fecha,ListaCompus)),
                            sub_atom(Fecha,0,7,_,Mesanio),
                            precio_compus(ListaCompus,Precios),
                            calcular_monto(Mesanio, Monto),
                            M is Monto + Precios.
calcular_monto(_,0).

precio_compus([Id|ListaCompus],Cont):- computadora(Id,_,Precio,_,_),
                                        precio_compus(ListaCompus,P),
                                        Cont is P + Precio.
precio_compus([],0).

leer([H|T]):-read(H),H\=[],leer(T).
leer([]).

buscar_computadoras(Caracteristicas,[Id|ListaFinal],T):- retract(computadora(Id,_,_,_,Lista)),
                                                incluye(Caracteristicas,Lista),
                                                not(pertenece(Id,T)),
                                                buscar_computadoras(Caracteristicas,ListaFinal,[Id|T]).
buscar_computadoras(_,[],_).

incluye([],_).
incluye([H|CarDeseadas],ListaCar):- pertenece(H,ListaCar),
                                    incluye(CarDeseadas,ListaCar).

pertenece(H,[H|_]).
pertenece(H,[_|T]):-pertenece(H,T).