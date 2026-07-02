:-dynamic(heladeria/3).
:-dynamic(locales/3).


inicio:-retractall(heladeria(_,_,_)),retractall(locales(_,_,_)),abrir_base,menu.


abrir_base:-consult('bdheladerias.txt').


menu:-writeln('INGRESE OPCION'),
        writeln('OPCION 0 - SALIR'),
        writeln('OPCION 1 - Ingresar lista de códigos de heladería y decir cuáles de ellos tienen al menos una sucursal en el centro'),
        writeln('OPCION 2 - Ingresar una calle y devolver nombre de heladerías SIN REPETIR que tengan al menos 1 vez esa calle en sus direcciones'),
        read(Op),
        Op\=0,
        Op<3,
        opcion(Op),
        menu.


menu:-writeln('Gracias por usar el sistema experto!').


opcion(1):- writeln('Ingrese lista e codigos de heladerias'),
            leer(ListaHela),
            sucursal_centro(ListaHela,ListaCentro),
            writeln('Las heladerias con AL MENOS una sucursal en el centro son '),
            writeln(ListaCentro).


opcion(2):-writeln('Ingresar calle'),
            read(Calle),
            buscar_heladerias2(Calle).


leer([H|T]):-read(H),H\=[],leer(T).
leer([]).


sucursal_centro([],[]).
sucursal_centro([H|Heladerias],[H|Centro]):- locales(H,Zona,_),
                                                retract(locales(H,Zona,_)),
                                                Zona = 'centro',
                                                sucursal_centro(Heladerias,Centro).
sucursal_centro([_|Hel],Centro):-sucursal_centro(Hel,Centro).


buscar_heladerias2(Calle):- retract(heladeria(Cod,Nom,_)),
                            locales_calle(Calle,Cod),
                            writeln(Nom),
                            buscar_heladerias2(Calle).
buscar_heladerias2(_).

perteneceCalle(Calle,[H|_]):- sub_atom(H,0,_,_,Calle).
perteneceCalle(Calle,[_|T]):- perteneceCalle(Calle,T).


pertenece(H,[H|_]).
pertenece(H,[_|T]):-pertenece(H,T).


locales_calle(Calle,Cod):- retract(locales(Cod,_,ListaSucu)),
                            perteneceCalle(Calle,ListaSucu).
