:-dynamic(vivero/3).
:-dynamic(plantas/4).

inicio:-retractall(vivero(_,_,_)),retractall(plantas(_,_,_,_)),menu.

menu:-writeln('INGRESE OPCION'),
        writeln('OPCION 0: SALIR'),
        writeln('OPCION 1: INGRESAR PLANTAS Y MOSTRAR EN 2 LISTAS LAS DE O/I Y P/V'),
        writeln('OPCION 2: INGRESAR UN VIVERO Y OBTENER LISTA DE SUCURSALES DE PLANTAS PRECIO PROMEDIO MENOS A 10MIL'),
        read(Op),
        Op\=0,
        Op<3,
        opcion(Op),
        menu.

menu:-writeln('Gracias por usar el sistema experto').

opcion(1):- 
            writeln('ingrese plantas a clasificar'),
            leer(Plantas),
            dividir_por_estacion(Plantas,ListaOI,ListaPV),
            writeln('Las plantas de otonio invierno son:'),
            writeln(ListaOI),
            writeln('Las plantas de primavera verano son'),
            writeln(ListaPV).

opcion(2):- abrir_base,
            writeln('Ingrese un vivero'),
            read(Cod),
            vivero(Cod,_,ListaSuc),
            buscar_sucursales(ListaSuc,NuevaSuc),writeln(NuevaSuc).
opcion(_).

abrir_base:- consult('bdvivero.txt').

leer([H|T]):- read(H),H\=[],leer(T).
leer([]).

dividir_por_estacion([],[],[]).
dividir_por_estacion([H|Plantas],[H|ListaOI],ListaPV):- abrir_base,
                                                    retract(plantas(H,Est,_,_)),
                                                    Est = 'otonio',
                                                    dividir_por_estacion(Plantas,ListaOI,ListaPV).
dividir_por_estacion([H|Plantas],[H|ListaOI],ListaPV):- abrir_base,
                                                    retract(plantas(H,Est,_,_)),
                                                    Est = 'invierno',
                                                    dividir_por_estacion(Plantas,ListaOI,ListaPV).
dividir_por_estacion([H|Plantas],ListaOI,[H|ListaPV]):- abrir_base,
                                                    retract(plantas(H,Est,_,_)),
                                                    Est = 'primavera',
                                                    dividir_por_estacion(Plantas,ListaOI,ListaPV).
dividir_por_estacion([H|Plantas],ListaOI,[H|ListaPV]):- abrir_base,
                                                    retract(plantas(H,Est,_,_)),
                                                    Est = 'verano',
                                                    dividir_por_estacion(Plantas,ListaOI,ListaPV).
dividir_por_estacion([_|Plantas],ListaOI,ListaPV):-dividir_por_estacion(Plantas,ListaOI,ListaPV).

buscar_sucursales([],[]).
buscar_sucursales([H|T],[H|Nueva]):- H\=[],
                            promedio_suc(H,S,C),
                            C>0,
                            P is S/C,
                            P < 10000,
                            buscar_sucursales(T,Nueva).
buscar_sucursales([_|T],Nueva):-buscar_sucursales(T,Nueva).

promedio_suc(H,S,C):- retract(plantas(_,_,Precio,H)),
                        promedio_suc(H,Snuevo,Cnuevo),
                        S is Snuevo + Precio,
                        C is Cnuevo + 1.
promedio_suc(_,0,0).
