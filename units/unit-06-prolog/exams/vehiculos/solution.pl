:-dynamic(vehiculos/5).
:-dynamic(caracteristicas/2).

inicio:- retractall(vehiculos(_,_,_,_,_)), retractall(caracteristicas(_,_)),abrir_base,menu.

abrir_base:-consult('bdvehiculos.txt').

menu:- writeln('Por favor ingrese opcion deseada'),
        writeln('OPCION 1: Listar vehiculos por precio y caracteristicas'),
        writeln('OPCION 2: Contar vehiculos con cierto estado y caracteristicas'),
        writeln('OPCION 3: Salir'),
        read(Op),
        Op<3,
        operaciones(Op),
        menu.

menu:- writeln('Gracias por usar el sistema experto!').

operaciones(1):- writeln('Ingrese PRECIO MINIMO'),
                read(Min),
                writeln('Ingrese PRECIO MAXIMO'),
                read(Max),
                writeln('Ingrese CARACTERISTICAS DESEADAS'),
                leer(ListaCarDeseadasDescrip),
                convertir_desc_a_id(ListaCarDeseadasDescrip,ListaCarDeseadasCodigo),
                writeln('Autos con precio y caracteristicas adecuadas:'),
                buscar_autos(Min,Max,ListaCarDeseadasCodigo).

operaciones(2):- writeln('Ingrese una sola caracteristica'),
                read(Car),
                caracteristicas(Id,Car),
                writeln('Ingrese estado: nuevo/usado:'),
                read(Estado),
                contar(Cont,Estado,Id),
                writeln('La cantidad de vehiculos son  '),
                write(Cont).

operaciones(_).

leer([H|T]):-read(H), H\=[], leer(T).
leer([]).

convertir_desc_a_id([],[]).
convertir_desc_a_id([HDes|TDes],[H|T]):-caracteristicas(H,HDes),
                                        retract(caracteristicas(H,HDes)),
                                        convertir_desc_a_id(TDes,T).

buscar_autos(Minimo,Maximo,CarDeseadas):- vehiculos(M,Precio,T,E,Carac),
                                    retract(vehiculos(M,Precio,T,E,Carac)),
                                    Precio > Minimo,
                                    Precio < Maximo,
                                    CarDeseadas \= [],
                                    pertenece(CarDeseadas,Carac),
                                    write(M),write('  '),write(Precio),write('  '),write(T),write('  '),write(E),
                                    buscar_autos(Minimo,Maximo,CarDeseadas).
buscar_autos(_,_,_).

pertenece([],_).
pertenece([H|T],ListaCaracteristicas):- H\=[],
                                        existe(H,ListaCaracteristicas),
                                        pertenece(T,ListaCaracteristicas).

existe(C,[C|_]).
existe(C,[_|T]):-existe(C,T).

contar(C,E,Car):- vehiculos(_,_,_,E,[HCar|TCar]),
                    retract(vehiculos(_,_,_,E,[HCar|TCar])),
                    existe(Car,[HCar|TCar]),
                    contar(Con,E,Car),
                    C is Con + 1.
                    
contar(0,_,_).

