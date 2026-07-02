:-dynamic(computadora/5).
:-dynamic(ventas/3).

inicio:-retractall(computadora(_,_,_,_,_)),retractall(ventas(_,_,_)),menu.

menu:-writeln('INGRESE OPCION DESEADA'),
        writeln('OPCION 0- SALIR'),
        writeln('OPCION 1 - INGRESAR ANIO Y MES Y MOSTRAR EL EL MONTO EN ESE MES '),
        writeln('OPCION 2 - INGRESAR LISTA DE CARACTERISTICAS Y DEVOLVER LISTA DE LOS ID DE PC Q TENGAN LAS MISMAS'),
        read(Op),
        Op\=0,
        Op<3,
        opcion(Op),
        menu.

menu:- writeln('GRACIAS POR USAR EL SISTEMA EXPERTO').

opcion(1):- abrir_base,
            writeln('Ingrese anio y mes: AAAA-MM'),
            read(Aniomes),
            calcular_monto(Aniomes,Total),
            writeln('EL TOTAL FUE DE '),
            writeln(Total).

opcion(2):- abrir_base,
            writeln('INGRESE LISTA CARACTERISTICAS'),
            leer(Carac),
            buscar_compus(Carac).

opcion(_).
abrir_base:-consult('bdcompus.txt').

calcular_monto(Aniomes, T):- retract(ventas(_,Fecha,ListaCompu)),
                            sub_atom(Fecha,0,7,_,Aniomes),
                            compus_tot(ListaCompu,SubT),
                            calcular_monto(Aniomes,Tot),
                            T is Tot + SubT.
calcular_monto(_,0).

compus_tot([Id|T],S):- computadora(Id,_,Precio,_,_),
                        compus_tot(T,Suma),
                        S is Suma + Precio.
compus_tot([],0).

leer([H|T]):-read(H),H\=[],leer(T).
leer([]).

buscar_compus(CaracDeseadas):- retract(computadora(Id,_,_,_,ListaCarCom)),
                        incluye(CaracDeseadas,ListaCarCom),
                        writeln(Id),
                        buscar_compus(CaracDeseadas).
buscar_compus(_).

incluye([],_).
incluye([H|ListaDeseadas],ListaCompu):- pertenece(H,ListaCompu),
                                        incluye(ListaDeseadas,ListaCompu).
pertenece(H,[H|_]).
pertenece(H,[_|T]):-pertenece(H,T).

