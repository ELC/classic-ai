:-dynamic(venta/4).

inicio:-retractall(venta(_,_,_,_)),abrir_base,menu.

abrir_base:-consult('bdventas.txt').

menu:-writeln('ingrese opcion deseada'),
        writeln('OPCION 1: Dado un dni y un año, mostrar consumo promedio'),
        writeln('OPCION 2: Dado un producto, listar quienes lo compraron el año pasado'),
        writeln('OPCION 3: Calcular el maximo consumo de una persona'),
        writeln('OPCION 4: Salir'),
        read(Op),
        Op<4,
        opcion(Op),
        menu.

menu:-writeln('Gracias por usar el sistema experto').

opcion(1):- writeln('Ingrese dni'),
            read(Dni),
            validar(Dni),
            writeln('Ingrese año'),
            read(Year),
            calcular_consumo(Dni,Year,S,C),
            validar_suma_y_cont(S,C).

opcion(2):- writeln('ingrese el producto'),
            read(P),
            buscar_compradores(P).

opcion(3):- writeln('Ingrese persona'),
            read(Dni),
            venta(Dni,_,_,M),
            calcular_maximo(Dni,Max,M),
            writeln('Su maximo consumo fue: '), writeln(Max).

opcion(_).

validar(Dni):- venta(Dni,_,_,_).
validar(_):- writeln('No se encontraron ventas para dicha persona.'), menu.

calcular_consumo(Dni,Year,S,C):- venta(Dni,_,Fecha,Monto),
                                retract(venta(Dni,_,Fecha,Monto)),
                                sub_atom(Fecha,_,4,0,Year),
                                calcular_consumo(Dni,Year,SumaNuevo,ContNuevo),
                                S is SumaNuevo + Monto,
                                C is ContNuevo + 1.
calcular_consumo(_,_,0,0).

validar_suma_y_cont(_,0):- writeln('Para el año ingresado no se encontraron registros de consumo').
validar_suma_y_cont(S,C):- P is S/C, mostrar_promedio(P).


mostrar_promedio(P):-writeln('El consumo promedio para el dni y el año ingresado es '),writeln(P).

buscar_compradores(Prod):- venta(Dni,Prod,Fecha,_),
                            retract(venta(Dni,Prod,Fecha,_)),
                            sub_atom(Fecha,_,4,0,2022),
                            writeln(Dni),
                            buscar_compradores(Prod).
buscar_compradores(_).

calcular_maximo(Dni,Max,M):- venta(Dni,_,_,Monto),
                            retract(venta(Dni,_,_,Monto)),
                            M < Monto,
                            calcular_maximo(Dni, Max, Monto).
calcular_maximo(_,Max,Max).


                            


