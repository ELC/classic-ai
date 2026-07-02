:-dynamic(vehiculos/5).
:-dynamic(caracteristicas/2).

inicio:-retractall(vehiculos(_,_,_,_,_)),retractall(caracteristicas(_,_)),abrir_base,menu.

abrir_base:- consult('bdvehiculos-2.txt').

menu:- writeln('Ingresar opcion deseada'),
        writeln('OPCION 0: SALIR'),
        writeln('OPCION 1: INGRESAR RANGO PRECIO Y LISTA CARACTERISTICAS DESEADAS Y DEVOLVER VEHICULOS'),
        writeln('OPCION 2: INGRESAR UNA CARACTERISTICA Y ESTADO Y DEVOLVER CANTIDAD DE AUTOS QUE CUMPLEN'),
        read(Op),
        Op \= 0,
        Op<3,
        opcion(Op),
        menu.
menu:-writeln('Gracias por usar el sistema experto!').

opcion(1):- writeln('Ingrese el precio minimo'),
            read(Min),
            writeln('Ingrese el precio maximo'),
            read(Max),
            writeln('Ingrese caracteristicas deseadas'),
            leer(ListaCarDesc),
            convertir_a_codigo(ListaCarDesc,ListaCar),
            writeln('Los autos que cumplen con los precios y caracteristicas ingresados son: '),
            obtener_vehiculos(Min,Max,ListaCar).

opcion(2):- writeln('Ingresar caracteristica'),
            read(Car),
            caracteristicas(Codi,Car),
            writeln('Ingresar estado'),
            read(Est),
            contar_vehiculos(Codi,Est,Cont),
            writeln('La cantidad de autos con esa caracteristica y ese estado son '), write(Cont).

opcion(_).

leer([H|T]):-read(H), H\=[], leer(T).
leer([]).

convertir_a_codigo([],[]).
convertir_a_codigo([HDesc|ListaDesc],[HCod|ListaCod]):- caracteristicas(HCod,HDesc),
                                                    convertir_a_codigo(ListaDesc,ListaCod).

obtener_vehiculos(Min,Max,ListaCar):- vehiculos(Marca,Precio,Tipo,Est,CarAuto),
                                        retract(vehiculos(Marca,Precio,Tipo,Est,CarAuto)),
                                        Precio < Max,
                                        Precio > Min,
                                        ListaCar \=[],
                                        validar_car(ListaCar,CarAuto),
                                        writeln(" "),
                                        write(Marca),write(" "),write(Precio),write(" "),write(Tipo),write(" "),writeln(Est),
                                        obtener_vehiculos(Min,Max,ListaCar).
obtener_vehiculos(_,_,_).

validar_car([],_).
validar_car([H|ListaIngresada],ListaAuto):- H\=[],
                                            pertenece(H,ListaAuto),
                                            validar_car(ListaIngresada,ListaAuto).
pertenece(H,[H|_]).
pertenece(H,[_|T]):-pertenece(H,T).

contar_vehiculos(C,Estado,Con):- vehiculos(_,_,_,Estado,ListaCarac),
                            retract(vehiculos(_,_,_,Estado,ListaCarac)),
                            pertenece(C,ListaCarac),
                            contar_vehiculos(C,Estado,CNuevo),
                            Con is CNuevo + 1.
contar_vehiculos(_,_,0).

