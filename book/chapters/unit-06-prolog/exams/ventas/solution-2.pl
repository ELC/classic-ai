:-dynamic(venta/4).

inicio:- retractall(venta(_,_,_,_)),menu.

menu:-writeln('INGRESE OPCION DESEADA: '),
        writeln('OPCION 0: SALIR'),
        writeln('OPCION 1: Por un DNI y un ANIO, informar CONSUMO PROMEDIO'),
        writeln('OPCION 2: Dado un producto, mostrar quienes lo compraron el anio pasado'),
        writeln('OPCION 3: Ingresar DNI e informar MAXIMO CONSUMO'),
        read(Op),
        Op\=0,
        Op<4,
        opcion(Op),
        menu.

menu:-writeln('Gracias por usar el sistema experto').

opcion(1):- abrir_base,
            writeln('Ingresar DNI'),
            read(Dni),
            validar(Dni),
            writeln('Ingresar Anio'),
            read(Anio),
            calcular_consumo_prom(Dni,Anio,Sum,Cont),
            validar_contador(Cont),
            Cont>0,
            P is Sum/Cont,
            writeln('EL PROMEDIO DE CONSUMO EN ESE AÑO ES '),writeln(P).

opcion(2):- abrir_base,
            writeln('INGRESE PRODUCTO'),
            read(Prod),
            listar_compradores(Prod,[]).

opcion(3):- abrir_base,
            writeln('INGRESE DNI'),
            read(Dni),
            maximo_consumo(Dni,M,0),
            writeln('SU CONSUMO MAXIMO FUE DE '),writeln(M).

opcion(_).

abrir_base:-consult('bdventas.txt').

validar(Dni):-venta(Dni,_,_,_).
validar(_):- writeln('NO EXISTE ESE DNI'),menu.

calcular_consumo_prom(Dni,Anio,Sum,Cont):- retract(venta(Dni,_,Fecha,Monto)),
                                    sub_atom(Fecha,_,4,0,Anio),
                                    calcular_consumo_prom(Dni,Anio,SNuevo,CNuevo),
                                    Sum is SNuevo + Monto,
                                    Cont is CNuevo + 1.
calcular_consumo_prom(_,_,0,0).

validar_contador(C):- C>0.
validar_contador(0):- writeln('NO TIENE CONSUMO PARA EL AÑO QUE INGRESO '),menu.

listar_compradores(Prod,Lista):- retract(venta(Dni,Prod,Fecha,_)),
                            sub_atom(Fecha,_,4,0,'2022'),
                            not(pertenece(Dni,Lista)),
                            writeln(Dni),
                            listar_compradores(Prod,[Dni|Lista]).
listar_compradores(_,_).


pertenece(H,[H|_]).
pertenece(H,[_|T]):-pertenece(H,T).

maximo_consumo(Dni,M,Max):- retract(venta(Dni,_,_,Monto)),
                            Max < Monto,
                            maximo_consumo(Dni,M,Monto).
maximo_consumo(_,Max,Max).