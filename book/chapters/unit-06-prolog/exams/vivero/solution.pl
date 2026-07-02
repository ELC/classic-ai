:-dynamic(vivero/3).
:-dynamic(plantas/4).

inicio:-retractall(vivero(_,_,_)),retractall(plantas(_,_,_,_)),menu.

abrir_base:-consult('bdvivero.txt').

menu:- writeln('Ingrese opcion deseada'),
        writeln('0 - Salir'),
        writeln('1 - Ingresar plantas y dividirlas por estacion'),
        writeln('2 - Ingresar vivero y obtener sucursales con precio promedio inferior a 10mil'),
        read(Op),
        Op \= 0,
        Op<3,
        opcion(Op),
        menu.
menu:-writeln('Gracias por usar el sistema experto!').

opcion(1):- writeln('Ingrese una serie de plantas'),
            leer(ListaPlantas),
            dividir_por_estacion(ListaPlantas,ListaOI,ListaPV),
            listar_por_estacion(ListaOI,ListaPV).

opcion(2):- writeln('Ingrese vivero'),
            read(Vivero),
            abrir_base,
            vivero(_,Vivero,SucLista),
            obtener_plantas_economicas(SucLista, ListaEconomicas, _, _),
            listar_economicas(ListaEconomicas).

leer([H|T]):- read(H),H\=[],leer(T).
leer([]).

dividir_por_estacion([],[],[]).
dividir_por_estacion([H|T],[H|ListaOI],ListaPV):- abrir_base,
                                                plantas(H,Estado,_,_),
                                                retract(plantas(H,Estado,_,_)),
                                                Estado = 'otonio',
                                                dividir_por_estacion(T,ListaOI,ListaPV).
dividir_por_estacion([H|T],[H|ListaOI],ListaPV):- abrir_base,
                                                plantas(H,Estado,_,_),
                                                retract(plantas(H,Estado,_,_)),
                                                Estado = 'invierno',
                                                dividir_por_estacion(T,ListaOI,ListaPV).
dividir_por_estacion([H|T],ListaOI,[H|ListaPV]):- abrir_base,
                                                plantas(H,Estado,_,_),
                                                retract(plantas(H,Estado,_,_)),
                                                Estado = 'primavera',
                                                dividir_por_estacion(T,ListaOI,ListaPV).
dividir_por_estacion([H|T],ListaOI,[H|ListaPV]):- abrir_base,
                                                plantas(H,Estado,_,_),
                                                retract(plantas(H,Estado,_,_)),
                                                Estado = 'verano',
                                                dividir_por_estacion(T,ListaOI,ListaPV).
dividir_por_estacion([_|T],ListaOI,ListaPV):-dividir_por_estacion(T,ListaOI,ListaPV).

listar_por_estacion(ListaOI,ListaPV):- writeln('Las plantas ingresadas de estado otonio/invierno son:'),writeln(ListaOI),
                                        writeln('Las plantas ingresadas de estado primavera/verano son:'),writeln(ListaPV).

obtener_plantas_economicas(TodasSucurVivero, [Cod|ListaEc],S,C):- plantas(_,_,Precio,Cod),
                                                                retract(plantas(_,_,Precio,Cod)),
                                                                pertenece(TodasSucurVivero,Cod),
                                                                obtener_plantas_economicas(TodasSucurVivero,ListaEc,SumNuevo,ContNuevo),
                                                                S is SumNuevo + Precio,
                                                                C is ContNuevo + 1,
                                                                C > 0,
                                                                P is S/C,
                                                                P < 10000.
obtener_plantas_economicas(_,[],0,0).

pertenece([H|_],H).
pertenece([_|T],Cod):-pertenece(T,Cod).

listar_economicas(ListaEco):- writeln('La lista de sucursales con precio promedio inferior a 10000 es '),writeln(ListaEco).