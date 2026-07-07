---
title: Banco de exámenes Prolog
---

(banco-de-examenes-prolog)=

# Banco de exámenes Prolog

Este apéndice conserva los enunciados y soluciones existentes como material
estático. La conversión completa a ejercicios ejecutables queda diferida para un
pase posterior.

(palabras-y-caracteres)=

## Palabras y caracteres

- Fecha: 2012-12-20

Final Inteligencia Artificial 20/12/2012 Practica:

1. Ingresar una lista de cadenas y un carácter. Por cada cadena de la lista y el
   carácter, verificar si ya están en la BD, sino esta registrarlo
   palabra(cadena,carácter,cantidad).

1. Ingresar un carácter y calcular el promedio de veces que aparece en la BD.

::::{dropdown} solution.pl

```prolog
%MENU PRINCIPAL
:-dynamic palabras/3.

inicio:-cargar,menu(0).

cargar:-consult('palabras.txt').
grabar:-tell('palabras.txt'),listing(palabras),told.

%OPCIONES
menu(0):-write('INGRESE OPCION:'),nl,
write('1- PUNTO 1'),nl,
write('2- PUNTo 2'),nl,
write('3- SALIR'),nl,
read(OP),menu(OP).

menu(1):-punto1,menu(0).
menu(2):-punto2,menu(0).
menu(3).

% PUNTO 1
punto1:-write('INGRESE UNA LISTA DE PALABRAS:'),leer(L),nl,
write('INGRESE CARACTER:'),read(C),nl,
contar(L,C,Cantidad),
buscarBC(L,C,Cantidad).

leer([H|T]):-read(H),atom(H),H\=[],leer(T).
leer([]).

contar([],_,0).
contar([H|T],C,Cantidad):-contar(T,C,Cant),aparece(H,C,Cont), Cantidad is Cant+Cont.
contar([_|T],C,Cantidad):-contar(T,C,Cantidad).

aparece('',_,0).
aparece(H,C,Cont):-sub_atom(H,0,1,RH,SubCad1),SubCad1=C,
sub_atom(H,1,RH,_,SubCad2),aparece(SubCad2,C,C1),Cont is C1+1.
aparece(H,C,Cont):-sub_atom(H,0,1,RH,SubCad1),SubCad1\=C,
sub_atom(H,1,RH,_,SubCad2),aparece(SubCad2,C,Cont).

buscarBC(L,C,Cantidad):-palabras(L,C,Cantidad),write('YA EXISTE'),nl,nl.
buscarBC(L,C,Cantidad):-assert(palabras(L,C,Cantidad)),grabar,write('GRABACION EXITOSA'),nl,nl.

% PUNTO 2
punto2:- cargar, write('INGRESE CARACTER:'),read(C),nl,
calcular(C,Suma,Cantidad),Promedio is Suma/Cantidad,
write('EL PROMEDIO ES:'),write(Promedio),nl,nl.

calcular(C,Suma,Cantidad):-palabras(_,C,Cant),retract(palabras(_,C,Cant)),
calcular(C,S1,C1),Suma is S1+Cant,Cantidad is C1+1.
calcular(_,0,0).
```

::::

(medicamentos-composicion-y-sintomas)=

## Medicamentos, composición y síntomas

- Fecha: 2013-08-29

1. Ingresar una lista [] de síntomas que presenta un paciente e informar a
   través de una nueva lista [] los nombres de los medicamentos que
   contrarrestan al menos el 80% de los síntomas del paciente.

1. Ingresar dos componentes y sus respectivas cantidades e informar a través de
   una lista [] los nombres de los medicamentos que contienen dichos componentes
   y en la cantidad indicada.

Nota Personal: para resolver el punto 2 hay que tener en cuenta que el
medicamento debe contener los 2 componentes en las 2 cantidades indicadas.

```prolog
medicamentos(nombre,droga,presentación,laboratorio,[síntomas que contrarresta]).
composición(nombre,componente,cantidad).
```

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2013-08-29-medicamentos.
```

::::

(ordenes-productos-y-stock)=

## Órdenes, productos y stock

- Fecha: 2013-11-22

Dada una BBDD compuesta por hechos con la siguiente estructura:

```prolog
orden(nro_orden, fecha_orden, cliente).
producto(codigo_producto, descripcion, cantidad_en_stock).
orden_producto(nro_orden, codigo_producto, cantidad_solicitada).
```

Hacer un programa que permita:

1. Ingresar una lista [] de productos y que a partir de esta determine a través
   de una nueva lista [] aquellos productos para los cuales no hay suficiente
   stock para cubrir todas las órdenes que haya con pedidos de dicho producto.

1. Informar a través de una lista aquellos productos que aparecen en al menos 5
   órdenes de compra.

1. Dado un cliente (dato de entrada) informar si tiene al menos 2 órdenes de
   compra emitidas en el mismo mes y año.

Nota:

- Para los ítems 1 y 2 trabajar sólo con los códigos de los productos.
- El formato de la fecha es dd/mm/aaaa.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2013-11-22-ordenes.
```

::::

(cantantes-albumes-y-temas)=

## Cantantes, álbumes y temas

- Fecha: 2013-12-05

Dada una BD con:

,fecha_edicion,copias_vendidas) (El formato del campo fecha es dd/mm/aaaa)

1)Ingrese un album y una lista [] de temas y a partir de esto devolver una lista
con aquellos temas de la lista original que correspondan al album ingresado.

2)Informar cuantos albumes fueron lanzados en un determinado año (dato de
entrada) por cantantes de origen sueco.

3)Ingresar un cantante y devolver una lista con todos los albumes que haya
lanzado a lo largo de su carrera y cuya cantidad de copias supere el millon.

```prolog
cantante(nombre_cantante,pais_origen)
album(nombre_album,nombre_cantante,[lista_temas])
```

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2013-12-05-albumes.
```

::::

(vacunas-por-edad-y-enfermedades)=

## Vacunas por edad y enfermedades

- Fecha: 2014-02-13

Dada una BD con los siguientes hechos:

1. Ingresar un niño y en base a su edad indicar en una lista las vacunas que le
   faltan aplicar. 2)Ingresar un niño y una enfermedad. Para esa enfermedad,
   indicar una lista de las vacunas que la contrarrestan. Además, informar si el
   niño tiene puesta alguna de esas vacunas o le falta la aplicación de alguna
   dosis. 3)Ingresar una vacuna e indicar la cantidad de niños que la tienen
   puesta.

```prolog
niño(nombre,edad,[vacunas_aplicadas]).
vacuna(vacuna,[enfermedades_que_combate]).
vacuna_aplicacion(edadDesde,edadHasta,[vacunas_a_aplicar]).
```

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2014-02-13-vacunas.
```

::::

(empleados-empresas-y-sueldos)=

## Empleados, empresas y sueldos

- Fecha: 2014-02-27

```prolog
empleado(nombre_empleado, profesion, ciudad)
trabaja(nombre_empleado, nombre_empresa, sueldo)
empresa(nombre_empresa, ciudad)
```

1. Devolver una lista [] con los nombres de todos los empleados que trabajan en
   la misma ciudad que la que viven.

1. Mostrar los nombres de los empleados que no trabajan en Microsoft.

1. Mostrar la tupla "Nombre Empleado - Nombre Empresa", para aquellos empleados
   que ganan más que cualquier empleado de Microsoft.

1. Calcular el sueldo promedio de los empleados de una determinada empresa
   (ingresarla), que ganan más que el que más gana en Microsoft.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2014-02-27-empleados.
```

::::

(peliculas-directores-actores-y-estrenos)=

## Películas, directores, actores y estrenos

- Fecha: 2014-04-21

Se tienen hechos definidos como película (nombre, genero, [directores],
[actores], fecha_estreno, pais_estreno). Formato de fecha: dd/mm/aaaa

1. Ingresar el nombre de un actor. Mostrar la lista [] de películas en las que
   actuó.
1. Mostrar una lista [] de las películas que tienen 2 directores o más.
1. Ingresar un año y un país, y decir cuantas películas se estrenaron en ese
   país y en ese año.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2014-04-21-peliculas.
```

::::

(verbos-raices-y-transformacion-de-listas)=

## Verbos, raíces y transformación de listas

- Fecha: 2014-07-31

A. Ingrese una lista de verbos, sacar las raíces y almacenarlos en la base de
datos de la siguiente forma (partir - part). B. Ingresar dos verbos y decir si
pertenecen a alguna conjunción de los que están en la base de datos. Si
pertenecen mostrar "Los verbos ingresados son conjugación de alguno de la base
de datos", sino mostrar "Los verbos ingresados no son conjugación de uno de la
base de datos o no existe el verbo en la BD". 2) Ingresar una lista de números
enteros: Si el último número es par, cambiar las posiciones de pares de esa
lista por cero. Si el último numero es impar, cambiar las posiciones de impares
de esa lista por uno. Mostrar la lista.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2014-07-31-verbos-listas.
```

::::

(lotes-y-lineas-de-credito)=

## Lotes y líneas de crédito

- Fecha: 2015-04-27

Una persona puede tener mas de un lote. Cada linea de crédito puede pagarse en u
numero distinto de cuotas 12, 24, 36 (Forma de financiación)

```prolog
lote(codLote, superficie, [dni], zona).
persona(dni, apellido, nombre).
lineaCredito(codLinea, descripcion, superficieDesde, SuperficieHasta, monto,[cuotas])
```

1. Ingresando un dni, devolver para cada lote la linea de crédito y el monto.

1. Ingresando un código de lote, devolver la linea de crédito y la máxima
   cantidad de cuotas de financiación.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2015-04-27-lotes.
```

::::

(gimnasio-socios-ejercicios-asistencias-y-niveles)=

## Gimnasio: socios, ejercicios, asistencias y niveles

- Fecha: 2015-08-06

Socio(dni, apellido, sexo, edad) Ejercicio(cod, descripcion, cod.nivel,
sexorecomendado, edaddesde, edadhasta) Asistencia(fecha, dni, minentreno,
[codejercicios realizados]) Nivel(cod nivel, descrip, canthoradesde,
canthorahasta) A tener en cuenta: Nivel: inicial (de 0 hs a 72 hs) medio (de
tanto a tanto) avanzado ( de tanto a tanto) y

```prolog
extremo(de tanto a tanto)
```

1. Ingresar un dni de un socio e informar: a. El nivel en el que se encuentra
   (teniendo en cuenta la asistencia) b. Los ejercicios que recomienda realizar
   de acuerdo a su nivel, sexo y edad.
1. Ingresar una fecha y un cod ejercicio e informar los socios que lo realizaron
   en esa fecha.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2015-08-06-gimnasio.
```

::::

(canciones-favoritas-por-invitados-y-genero-vals)=

## Canciones favoritas por invitados y género vals

- Fecha: 2015-12-17

La base de hechos estaba formada por:

Tenía un atributo mas que no me acuerdo pero no se usaba

```prolog
cancion(IdCancion,Nombre,Artista,Duración,Genero)
invitados(Nombre, [IdCanciones que gusta])
```

1. Listar las canciones que le gusta a más del 80% de los invitados.

1. Listar las canciones de género "vals" que duren más de 15 minutos. Nota:
   fijense esto del punto 1, lo que pueden hacer es crear 2 bases de hechos, una
   con los hechos de canciones y otro con la de los invitados, y cuando busco
   por canción todos los invitados y los elimino con un retract, luego los
   vuelvo a cargar (a los invitados) ya que son bases diferentes.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2015-12-17-canciones.
```

::::

(hotel-habitaciones-disponibles-y-habitaciones-premium-ocupadas)=

## Hotel: habitaciones disponibles y habitaciones premium ocupadas

- Fecha: 2016-02-11

Un Hotel cuenta con la siguiente base de hechos:

Una habitación puede contener una cierta cantidad de características como por
ejemplo “WIFI, Heladera, Aire Acondicionado, etc”. Una habitación pueda pasar
por dos estados, “disponible” y “ocupada”. Una habitación cuyo precio por día es
mayor a $1000 se considera una habitación Premium.

```prolog
habitación(numero,descripción,[Lista de Cod. Caract.],precio x dia, estado)
característica(código,descripción)
```

1. Un usuario quiere saber las habitaciones disponibles según una lista de
   características que ingresa (Códigos), donde se debe mostrar de cada
   habitación disponible, Descripción y Precio por día. Una habitación puede
   tener más características que las ingresadas por el usuario.

1. El gerente del hotel quiere regalarles un champan a cada habitación Premium
   que se encuentre ocupada en ese momento. Genere dicho informe.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2016-02-11-hotel.
```

::::

(gimnasio-socios-ejercicios-asistencias-y-niveles-2)=

## Gimnasio: socios, ejercicios, asistencias y niveles

- Fecha: 2016-02-25

Socio(dni, apellido, sexo, edad) Ejercicio(cod, descripcion, cod.nivel,
sexorecomendado, edaddesde, edadhasta) Asistencia(fecha, dni, minentreno,
[codejercicios realizados]) Nivel(cod nivel, descripcion, canthoradesde,
canthorahasta) A tener en cuenta: Nivel: inicial (de 0 hs a 72 hs) medio (de
tanto a tanto) avanzado (de tanto a tanto) y

```prolog
extremo(de tanto a tanto)
```

1. Ingresar un dni de un socio e informar: a. El nivel en el que se encuentra
   (teniendo en cuenta la asistencia) b. Los ejercicios que recomienda realizar
   de acuerdo a su nivel, sexo y edad.
1. Ingresar una fecha y un cod ejercicio e informar los socios que lo realizaron
   en esa fecha.

::::{dropdown} solution.pl

```prolog
% TODO: resolver el final practico 2016-02-25-gimnasio.
```

::::

(enunciado)=

## Enunciado

Final A 1 ingreser dos cadenas y mostrar la unión en una lista.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% , COMENTADA
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% inicio A 2 Recetas de Cocinas.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

```prolog
sub_atom(B,0,1,NB1,_)
```

::::{dropdown} solution.pl

```prolog
inicio:-write('ingrese cadena 1:'),read(A),
write('ingrese Cadena 2:'),read(B),
intercepcion(A,B,L),
write('Lista Comun:'), write(L).
intercepcion(A,B,[H|T]):-
atom_length(A,NA),
atom_length(B,NB),
NA > 0, NB > 0,
sub_atom(A,0,1,NA1,H),
sub_atom(A,1,NA1,_,A1),
esta(H,B), intercepcion(A1,B,T).
intercepcion(A,B,T):-
atom_length(A,NA),
atom_length(B,NB),
NA > 0, NB > 0,
sub_atom(A,0,1,NA1,_),
sub_atom(A,1,NA1,_,A1),
intercepcion(A1,B,T).

intercepcion(_,_,[]).

esta(H,B):-atom_length(B,NB), NB > 0,
sub_atom(B,0,1,_,H).
esta(H,B):-atom_length(B,NB), NB > 0,
NB1 is NB-1,
sub_atom(B,1,NB1,_,B1),
esta(H,B1).

inicio:- dynamic(cod/1), dynamic(receta/2), dynamic(ingrediente/3),consult('recetas1.txt'), menu.

menu:- nl, write('1 Alta de Receta'),
nl, write('2 Baja de Receta'),
nl, write('3 Alta de Ingrediente'),
nl, write('4 Baja de Ingrediente'),
nl, write('5 Consulta todo'),
nl, write('6 Consuta Dos Ingrediente'),
nl, write('7 Salir'),
nl, nl, write('Ingrese una opcion: '), read(A), opcion(A).

opcion(1):- nl, write('Ingrese Nuevo Nombre Receta: '), read(N),
cod(Nro), Cod is Nro + 1, retract(cod(Nro)),assert(cod(Cod)),
assert(receta(Cod,N)), menu.
opcion(2):- nl, write('Ingrese Codigo de Receta a eliminar: '), read(C),
retract(receta(C,_)),menu.
opcion(3):- nl, write('Ingrese Codigo de Receta: '), read(C),
write('Ingrese Nuevo Ingrediente: '), read(I),
write('Cantidad Ingrediente: '), read(N),
assert(ingrediente(C,I,N)),menu.
opcion(4):- nl, write('Codigo de Receta:'), read(C),
write('Nombre Ingrediente a Eliminar: '), read(I),
retract(ingrediente(C, I,_)),menu.
opcion(5):- nl, write(' Lista de Recetas '), listarecetas.
opcion(6):- nl, write(' ingrediente 1: '), read(I1),
write(' Ingrediente 2: '), read(I2),
nl, write('Lista de ingredientes ' ),
listaingr(I1, I2).
opcion(_):- tell('recetas1.txt'),
listing(cod),
listing(receta),
listing(ingrediente),
told.

listarecetas:- receta(C, N), nl, write('Cod: '), write(C),
write(' - '), write(N),fail.
listarecetas:- nl, menu.

listaingr(I1,I2):- ingrediente(C, I1,_), ingrediente(C, I2,_),
receta(C, N), write(C), write(' - '), write(N), fail.
listaingr(_,_):- nl, menu.
```

::::

(enunciado-2)=

## Enunciado

Final Agosto 2010

1. Agregar lista de palabras agudas y graves.
1. Agregar a una BD las palabras de la lista, separando las en agudas termina en
   n, s o vocal y graves, todas las demas.
1. Mostras cantidas de Agudas terminadas en n, cant en s y cant en o.
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
ago2010:- dynamic(aguda/2), dynamic(grave/2),consult('palabras.txt'), nl,
write('lista de palabras: '), leer(T),
agregarpalabras(T),terminacion('n',C1),
terminacion('s',C2), terminacion('o',C3),
nl, write('terminadas en N: '), write( C1 ),
nl, write('terminadas en S: '), write( C2 ),
nl, write('terminadas en o: '), write( C3 ).

leer([H|T]):- read(H), H\=[], leer(T).
leer([]).

agregarpalabras([]).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'n'),
assert(aguda(H,'n')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 's'),
assert(aguda(H,'s')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'a'),
assert(aguda(H,'a')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'e'),
assert(aguda(H,'e')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'i'),
assert(aguda(H,'i')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'o'),
assert(aguda(H,'o')), agregarpalabras(T).
agregarpalabras([H|T]):- atom_length(H,C), C1 is C-1, sub_atom(H, C1, 1, _, 'u'),
assert(aguda(H,'u')), agregarpalabras(T).

terminacion(X,Cant):- aguda(P,X), retract(aguda(P,X)), terminacion(X,Cant1), Cant is Cant1 + 1.
terminacion(_,0).

litarAgudas:- aguda(P,V), nl, write(P), write(V), fail.
```

::::

(enunciado-3)=

## Enunciado

% % fecha es aaaa-mm-dd ingresar un año y mes ("2023-10") y mostrar el monto
total recaudado ese mes (una venta puede tener varias veces la misma pc, hay que
hacer dos sumadores) ingresar una lista de características y devolver otra lista
que contenga *sin repetir* los id de pc que contengan esas características
(evaluar cada característica de la lista ingresada para cada característica de
la pc)

```prolog
computadora(id, tipo, precio, stock, [características])
ventas(id, fecha, [idCompusVendidas])
```

::::{dropdown} solution-2.pl

```prolog
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
```

::::

::::{dropdown} solution.pl

```prolog
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
```

::::

::::{dropdown} bdcompus.txt

```text
computadora(1,'dell',10000,210,['4gb ram','gris','nueva']).
computadora(2,'samsung',9000,300,['4gb ram','gris','nueva']).
computadora(3,'apple',15000,10,['8gb ram','blanca','nueva']).
computadora(4,'apple',16000,100,['8gb ram','gris','nueva']).
computadora(5,'lenovo',6000,160,['4gb ram','gris','usada']).
computadora(6,'lenovo',7000,160,['6gb ram','gris','usada']).
computadora(7,'hp',8000,160,['4gb ram','blanca','usada']).

ventas(1,'2023-10-30', [1,1,3,4]).
ventas(2,'2023-10-31', [2,5,7,5]).
ventas(3,'2023-11-01', [6,5,7,1]).
ventas(4,'2023-11-02', [5,1,3]).
```

::::

(enunciado-4)=

## Enunciado

Revisar enunciado: no habia enunciado confiable en el archivo original. Inferido
a partir de la solucion del dominio `heladerias` y sus predicados principales:
opcion, leer, sucursal_centro, buscar_heladerias2, perteneceCalle, pertenece,
locales_calle.

::::{dropdown} solution-2.pl

```prolog
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
```

::::

::::{dropdown} solution.pl

```prolog
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
```

::::

::::{dropdown} bdheladerias.txt

```text
heladeria(1,yomo,4444444).
heladeria(2,smart,555555).
heladeria(3,rio,666666).
heladeria(4,tento,777777).

locales(1,centro,['pellegrini 1200','pellegrini 1400','san juan 1800']).
locales(1,sur,['pellegrini 5000','27 de febrero 4000']).
locales(2,centro,['san luis 223','pellegrini 5000','27 de febrero 4000']).
locales(3,centro,['san lorenzo 113']).
locales(4,sur,['san martin 5000','27 de febrero 4000']).
```

::::

(enunciado-5)=

## Enunciado

Final Julia Ejercicio

1.

Ingresar dos listas. Si son del mismo tamaño comparar similitud = 100%
'Identicas'

> = 75% 'Muy Parecidas' = 25% 'Parecidas' = 0% 'Poco Parecidas' = 0% 'Nada
> Parecidas' %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
> %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
inicio :- write('lista 1:'), leer(L1), write('lista 2:'), leer(L2),
comparaLis(L1,L2).

comparaLis(L1,L2) :- cant(L1,C), cant(L2,C), similitud(L1,L2,N),
Valor is N/C, clasifica(Valor).
comparaLis(_,_) :- write('Listas de distintas Longitudes').

cant([],0).
cant([_|T],N):- cant(T,N1), N is N1 + 1.

similitud([],[],0).
similitud([H|T1],[H|T2],N):- similitud(T1,T2,N1), N is N1 + 1.
similitud([_|T1],[_|T2],N):- similitud(T1,T2,N).

clasifica(N):- N = 1, write('Identicas') .
clasifica(N):- N>=(0.75), write('Muy Parecidas') .
clasifica(N):- N>=(0.25), write('Parecidas') .
clasifica(N):- N>= 0, write('Poco Parecidas') .
clasifica(N):- N = 0, write('Nada Parecidas') .

leer([H|T]):-read(H), H\=[], leer(T).
leer([]).
```

::::

(enunciado-6)=

## Enunciado

Final Julia Ejercicio

2.

Ingresar 1 lista y un elemento. Borrar de la lista posiciones donde aparesca
elemento Y decir cuantas veces esta repetido.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
inicio :- write('lista 1:'), leer(L1), write('elemento:'), read(A),
limpiezaLista(L1,L2,A,N), write('Lista Limpia:'), write(L2),
nl, write('Esta Repetido: '), write(N), write('veces').

leer([H|T]):-read(H), H\=[], leer(T).
leer([]).

limpiezaLista([H|T1],T2,H,N):-limpiezaLista(T1,T2,H,N1), N is N1 + 1.
limpiezaLista([H|T1],[H|T2],C,N):-limpiezaLista(T1,T2,C,N).
limpiezaLista([],[],_,0).
```

::::

(enunciado-7)=

## Enunciado

Final Mesa 09/10/2008. Ingresar una cadena e Identificar Digtongos/Hiatos.
Ejemplo Digtongo: puerto, Hiato: aeroplano.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
inicio :- write('ingrese una palabra:'),read(A),tipo(A).

tipo(A) :- atom_length(A,N), N>0, sub_atom(A,0,1,N1,C),
sub_atom(A,1,N1,_,A1), digtongo(C,A1).
tipo(A) :- atom_length(A,N), N>0, sub_atom(A,0,1,N1,C),
sub_atom(A,1,N1,_,A1), hiato(C,A1).
tipo(_) :- write('No es Digtongo/Hiato').

digtongo(C,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,_,C1),
esAbierta(C), esCerrada(C1), write('Es Digtongo').
digtongo(C,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,_,C1),
esCerrada(C), esCerrada(C1), C \= C1, write('Es Digtongo').
digtongo(C,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,_,C1),
esCerrada(C), esAbierta(C1), write('Es Digtongo').
digtongo(_,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,N1,C1),
sub_atom(A,1,N1,_,A1), digtongo(C1,A1).

hiato(C,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,_,C1),
esAbierta(C), esAbierta(C1), write( 'Es Hiato' ).
hiato(_,A) :- atom_length(A,N), N>0, sub_atom(A,0,1,N1,C1),
sub_atom(A,1,N1,_,A1), hiato(C1,A1).

esAbierta('a').
esAbierta('e').
esAbierta('o').
esCerrada('i').
esCerrada('u').
```

::::

(enunciado-8)=

## Enunciado

Final Mesa julio 2010 Empleado( Cod, Nom, Ape ) Trabajo( Cod, Descripcion,
Precio ) ABM empleados y trabajos de los empleados Determinar para cada empleado
el total trabajado %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
julio2010:- dynamic(codigo/1), dynamic(empleado/3), dynamic(trabajo/3), consult('empleados.txt'), menu.
menu:- write('Ingrese una Opcion'),nl,
write(' 1 - Nuevo Empleado'),nl,
write(' 2 - Agregar Trabajo'),nl,
write(' 3 - lista importes por empleado'),nl,
write(' 4 - Lista Todo'),nl,
write(' 5 - Salir'),nl,
read(X),opcion(X).

opcion(1):- write('Nombre:' ),read(N),
write('Apellido: '),read(A),
codigo(Nro), Cod is Nro+1, retract(codigo(Nro)),assert(codigo(Cod)),
assert(empleado(Cod,N,A)),
menu.
opcion(2):- write('cod Empleado: '), read(N),
write('Trabajo: '), read(T),
write('Precio: '), read(P),
assert(trabajo(N,T,P)),
menu.
opcion(3):- guardar, write('Listado de Sueldo Total'), nl, listaSueldo.
opcion(4):- nl, write('Listado de empleados'), nl,listaEmpleado.
opcion(5):- guardar.

listaSueldo:- nl, empleado(X,N,A),
write('codigo: '), write(X),
write('Nombre: '), write(N),
write(' Apellido: '), write(A),
write(' Sueldo: '), totalsueldo(X,T),
write(T), nl, fail.
listaSueldo:- retractall(trabajo), consult('empleados.txt'), nl, menu.

totalsueldo(X,T):-sueldo(X,T).
sueldo(X,T):- trabajo(X,D,P), retract(trabajo(X,D,P)), sueldo(X,T1), T is T1 + P.
sueldo(_,0).

listaEmpleado:- empleado(X,N,A), write('codigo: '), write(X),
write(' Nombre: '), write(N),
write(' Apellido: '),write(A), nl, fail.
listaEmpleado:- nl, menu.

guardar:- tell('empleados.txt'),
listing(codigo),
listing(empleado),
listing(trabajo),
told.
```

::::

(enunciado-9)=

## Enunciado

Final Mesa Marzo 2008 ejercicio

1.

Ingresar lista y si ultimo caracter es par poner todos los lugares pares de la
lista en Cero. Si es impar poner lugeres impares en cero. Devolver lista
resultante %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
inicio :- write( 'ingrese una lista:' ), leer(L1), ultimo(L1,U),
modiParImpar(L1,U,L2), write( 'Lista modificada: ' ),
write(L2).

modiParImpar([],_,[]).
modiParImpar(L1,U,L2) :- R is U mod 2, R = 0, agregaCont(L1,L2).% Si es Par
modiParImpar(L1,_,L2) :- agregaCero(L1,L2).% Si es Impar

agregaCero([],[]).
agregaCero([_|L1],[0|L2]):-agregaCont(L1,L2).

agregaCont([],[]).
agregaCont([H|L1],[H|L2]):-agregaCero(L1,L2).

leer([H|T]):-read(H), H \= [], leer(T).
leer([]).

ultimo([_|T],U):- ultimo(T,U).
ultimo([U|[]],U).
```

::::

(enunciado-10)=

## Enunciado

Final Mesa Marzo 2008 ejercicio

2.

Ingresar número N y devolver la suma hasta 0. Eje. N= 4 devolver 4+3+2+1+0 = 10.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
inicio:- write('Ingrese un Número:'), read(A),suma_hasta(A,S), write(S).

suma_hasta(0,0).
suma_hasta(A,S):-A1 is A - 1, suma_hasta( A1,S1 ), S is S1 + A.
```

::::

(enunciado-11)=

## Enunciado

Final Mesa Mayo 2008 ejercicio

1.

Ingresar una cadena y devolver las suma de sus carasteres en ascii. funcion
atom_char(C,N) me da el ascii de la variable C.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
inicio:- write('Ingrese Cadena: '), read(A) , sumaletra( A, N ),
write('La suma ascii de los caracteres de la cadena es: '), write(N).

sumaletra(A,0):- atom_length(A,0).
sumaletra(A,N):- sub_atom(A,0,1,Cant,C), atom_char(C,N1),
sub_atom(A,1,Cant,_,A1), sumaletra(A1,N2),
N is N1 + N2.
```

::::

(enunciado-12)=

## Enunciado

Final Mesa Mayo 2008 ejercicio

2.

Ingresar una Lista de enteros y luego devolver otra lista donde: el 1º es 2º-1º,
el 2º es 3º-2º y asi sucesivamente. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

::::{dropdown} solution.pl

```prolog
inicio:-write('Ingrese lista de numeros: '), leer( L ) , listaDif( L, LR ),
write('lista Diferencias:'), write(LR).

listaDif( [],[]).
listaDif( [H1|L],LR ):- dif(H1, L, LR), ascii('a').

dif(_,[],[]).
dif( H1, [H2|L], [H|LR] ):- H is H2-H1, dif(H2, L, LR).

leer([H|T]):-read(H), H \= [], leer(T).
leer([]).
```

::::

(enunciado-13)=

## Enunciado

Revisar enunciado: no habia enunciado confiable en el archivo original. Inferido
a partir de la solucion del dominio `pacientes` y sus predicados principales:
opcion, buscar_especialidades, pertenece, listar_especialidades,
contar_pacientes.

::::{dropdown} solution-2.pl

```prolog
:-dynamic(paciente/3).
:-dynamic(profesional/4).
:-dynamic(turno/6).

inicio:-retractall(paciente(_,_,_)),retractall(profesional(_,_,_,_)),retractall(turno(_,_,_,_,_,_)),menu.

menu:- writeln('Ingrese opcion:'),
        writeln('OPCION 0: Salir'),
        writeln('OPCION 1: Para un paciente y un año, determinar las especialidades atendidas'),
        writeln('OPCION 2: Mostrar profesionales con turnos con montos mayores de 1500'),
        read(Op),
        Op\=0,
        Op<3,
        opcion(Op),
        menu.

menu:- writeln('Gracias por usar el sistema experto!').

opcion(1):- abrir_base,
            writeln('Ingrese nombre paciente'),
            read(Nom),
            paciente(Dni,Nom,_),
            writeln('Ingrese anio'),
            read(Anio),
            writeln('Las especialidades encontradas son:'),
            buscar_especialidades(Dni,Anio,[]).

opcion(2):- abrir_base,
            buscar_profesionales.

opcion(_).

abrir_base:-consult('bdpacientes-2.txt').

buscar_especialidades(Dni,Anio,ListaSinRep):- turno(Dni,_,Esp,Fecha,_,_),
                                    retract(turno(Dni,_,Esp,Fecha,_,_)),
                                    sub_atom(Fecha,_,4,0,Anio),
                                    not(pertenece(Esp,ListaSinRep)),
                                    writeln(Esp),
                                    buscar_especialidades(Dni,Anio,[Esp|ListaSinRep]).
buscar_especialidades(_,_,_).

pertenece(H,[H|_]).
pertenece(H,[_|T]):-pertenece(H,T).

buscar_profesionales:- retract(profesional(Dni,Nom,_,_)),
                        contar(Dni,Cont),
                        Cont>0,
                        write('Profesional: '),write(Nom),write(' con '),write(Cont),writeln(' turnos de montos mayores a 1500'),
                        buscar_profesionales.
buscar_profesionales.

contar(Dni,C):- retract(turno(_,Dni,_,_,_,Monto)),
                Monto>1500,
                contar(Dni,CNuevo),
                C is CNuevo + 1.
contar(_,0).
```

::::

::::{dropdown} solution.pl

```prolog
:-dynamic(paciente/3).
:-dynamic(profesional/4).
:-dynamic(turno/6).

inicio:-retractall(paciente(_,_,_)),retractall(profesional(_,_,_,_)),retractall(turno(_,_,_,_,_,_)),abrir_base,menu.

abrir_base:-consult('bdpacientes.txt').

menu:- writeln('ingresar opcion deseada'),
        writeln('OPCION 1: Listar para un paciente y un año las especialidades atendidas'),
        writeln('OPCION 2: Mostrar el nombre y la cantidad de turnos de profesionales donde el monto fue mayor a 10000'),
        writeln('OPCION 3: Salir'),
        read(Op),
        Op < 3,
        opcion(Op),
        menu.

menu:- writeln('Gracias por usar el sistema experto!').

opcion(1):- writeln('Ingrese nombre del paciente'),
            read(NomP),
            paciente(DniP,NomP,_),
            writeln('Ingrese el anio'),
            read(Anio),
            writeln('Las especialidades atendidas fueron:'),
            buscar_especialidades(DniP,Anio,[],ListaEspecialidades),
            listar_especialidades(ListaEspecialidades).

opcion(2):- listar_profesionales.

opcion(_).

buscar_especialidades(Dni,Anio,ListaSinRepetir,[Espe|T]):- turno(Dni,_,Espe,Fecha,_,_),
                                                    retract(turno(Dni,_,Espe,Fecha,_,_)),
                                                    sub_atom(Fecha,_,4,0,Anio),
                                                    not(pertenece(ListaSinRepetir,Espe)),
                                                    buscar_especialidades(Dni,Anio,[Espe|ListaSinRepetir], T).
buscar_especialidades(_,_,_,[]).

pertenece([E|_],E).
pertenece([_|T],E):-pertenece(T,E).

listar_especialidades(L):- writeln(L).
listar_especialidades([]):- writeln('No se encontraron especialidades').

listar_profesionales:- profesional(DniPro,Nom,_,_),
                        retract(profesional(DniPro,Nom,_,_)),
                        contar_pacientes(DniPro,Contador),
                        Contador>0,
                        writeln('Profesional: '),write(Nom),write(' cantidad pacientes:'),write(Contador),writeln(' '),
                        listar_profesionales.
listar_profesionales.

contar_pacientes(Dni,Cont):- turno(_,Dni,_,_,_,Monto),
                                        retract(turno(_,Dni,_,_,_,Monto)),
                                        Monto>15000,
                                        contar_pacientes(Dni,CNuevo),
                                        Cont is CNuevo + 1.

contar_pacientes(_,0).
```

::::

::::{dropdown} bdpacientes-2.txt

```text
paciente(123, 'franco', 'uom').
paciente(1234, 'nicolas', 'uom').
paciente(12345, 'raquel', 'pami').
paciente(123456, 'jorge', 'pami').
paciente(654322, 'antonela', 'osde').
paciente(656565, 'rosa', 'osde').
paciente(646464, 'ana', 'osde').
paciente(636363, 'simon', 'avalian').
paciente(626262, 'mateo', 'avalian').
paciente(616161, 'jimena', 'avalian').

profesional(321, 'juan', 'odontologia', 'uom').
profesional(4321, 'pedro', 'pediatria', 'uom').
profesional(54321, 'esteban', 'traumatologia', 'pami').
profesional(654321, 'joaquin', 'cardiologia', 'pami').
profesional(111, 'lujan', 'oculista', 'osde').
profesional(222, 'andres', 'neurologia', 'osde').
profesional(333, 'lorena', 'kinesiolia', 'avalian').
profesional(444, 'helena', 'psicologia', 'avalian').

turno(1234, 321, 'odontologia', '01-01-2023', 'uom', 30000).
turno(1234, 321, 'odontologia', '01-02-2023', 'uom', 20000).
turno(1234, 321, 'odontologia', '01-03-2023', 'pami', 30000).
turno(1234, 654321, 'cardiologia', '01-03-2023', 'pami', 30000).
turno(1234, 654321, 'cardiologia', '01-04-2023', 'pami', 30000).
turno(1234, 654321, 'cardiologia', '01-04-2022', 'pami', 30000).
turno(1234, 54321, 'traumatologia', '01-05-2023', 'pami', 30000).
turno(1234, 54321, 'traumatologia', '01-05-2022', 'pami', 30000).
turno(654322, 222, 'neurologia', '02-04-2023', 'osde', 10000).
turno(654322, 222, 'neurologia', '01-09-2023', 'osde', 15000).
turno(654322, 111, 'oculista', '09-10-2023', 'osde', 13000).
turno(636363, 333, 'kinesiologia', '10-03-2023', 'avalian', 16000).
turno(636363, 333, 'kinesiologia', '25-03-2023', 'avalian', 16800).
turno(636363, 444, 'psicologia', '16-04-2023', 'avalian', 12000).
turno(616161, 444, 'psicologia', '17-08-2023', 'avalian', 12000).
turno(616161, 444, 'psicologia', '27-08-2023', 'avalian', 12500).
turno(616161, 444, 'psicologia', '05-09-2023', 'avalian', 12700).
```

::::

::::{dropdown} bdpacientes.txt

```text
paciente(123, 'franco', 'uom').
paciente(1234, 'nicolas', 'uom').
paciente(12345, 'raquel', 'pami').
paciente(123456, 'jorge', 'pami').
paciente(654322, 'antonela', 'osde').
paciente(656565, 'rosa', 'osde').
paciente(646464, 'ana', 'osde').
paciente(636363, 'simon', 'avalian').
paciente(626262, 'mateo', 'avalian').
paciente(616161, 'jimena', 'avalian').

profesional(321, 'juan', 'odontologia', 'uom').
profesional(4321, 'pedro', 'pediatria', 'uom').
profesional(54321, 'esteban', 'traumatologia', 'pami').
profesional(654321, 'joaquin', 'cardiologia', 'pami').
profesional(111, 'lujan', 'oculista', 'osde').
profesional(222, 'andres', 'neurologia', 'osde').
profesional(333, 'lorena', 'kinesiolia', 'avalian').
profesional(444, 'helena', 'psicologia', 'avalian').

turno(1234, 321, 'odontologia', '01-01-2023', 'uom', 30000).
turno(1234, 321, 'odontologia', '01-02-2023', 'uom', 20000).
turno(1234, 321, 'odontologia', '01-03-2023', 'pami', 30000).
turno(1234, 654321, 'cardiologia', '01-03-2023', 'pami', 30000).
turno(1234, 654321, 'cardiologia', '01-04-2023', 'pami', 30000).
turno(1234, 654321, 'cardiologia', '01-04-2022', 'pami', 30000).
turno(1234, 54321, 'traumatologia', '01-05-2023', 'pami', 30000).
turno(1234, 54321, 'traumatologia', '01-05-2022', 'pami', 30000).
turno(654322, 222, 'neurologia', '02-04-2023', 'osde', 10000).
turno(654322, 222, 'neurologia', '01-09-2023', 'osde', 15000).
turno(654322, 111, 'oculista', '09-10-2023', 'osde', 13000).
turno(636363, 333, 'kinesiologia', '10-03-2023', 'avalian', 16000).
turno(636363, 333, 'kinesiologia', '25-03-2023', 'avalian', 16800).
turno(636363, 444, 'psicologia', '16-04-2023', 'avalian', 12000).
turno(616161, 444, 'psicologia', '17-08-2023', 'avalian', 12000).
turno(616161, 444, 'psicologia', '27-08-2023', 'avalian', 12500).
turno(616161, 444, 'psicologia', '05-09-2023', 'avalian', 12700).
```

::::

(enunciado-14)=

## Enunciado

Revisar enunciado: no habia enunciado confiable en el archivo original. Inferido
a partir de la solucion del dominio `vehiculos` y sus predicados principales:
operaciones, leer, convertir_desc_a_id, buscar_autos, pertenece, existe, contar.

::::{dropdown} solution-2.pl

```prolog
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
```

::::

::::{dropdown} solution.pl

```prolog
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
```

::::

::::{dropdown} bdvehiculos-2.txt

```text
:-dynamic vehiculos/5.
:-dynamic caracteristicas/2.

vehiculos('Ford', 10000, 'auto', 'nuevo', [1,2,3,4]).
vehiculos('Ford', 15000, 'auto', 'nuevo', [1,2]).
vehiculos('Ford', 25000, 'auto', 'nuevo', [1,2,4]).
vehiculos('Ford', 13000, 'auto', 'usado', [1,4]).
vehiculos('Ford', 8000, 'auto', 'usado', [1,3]).
vehiculos('Ford', 9500, 'auto', 'usado', [1,4]).

vehiculos('Toyota', 20000, 'auto', 'nuevo', [2,3,4]).
vehiculos('Toyota', 28000, 'auto', 'nuevo', [1,2,3,4]).
vehiculos('Toyota', 16000, 'auto', 'usado', [1,2]).

vehiculos('Chevrolet', 40000, 'auto', 'nuevo', [2,3,4]).
vehiculos('Chevrolet', 50000, 'auto', 'nuevo', [1,3]).
vehiculos('Chevrolet', 10000, 'auto', 'nuevo', [2,3]).
vehiculos('Chevrolet', 9100, 'auto', 'usado', [1,3]).

caracteristicas(1, 'rojo').
caracteristicas(2, 'aire acondicionado').
caracteristicas(3, 'largo').
caracteristicas(4, 'al piso').
```

::::

::::{dropdown} bdvehiculos.txt

```text
:-dynamic vehiculos/5.
:-dynamic caracteristicas/2.

vehiculos('Ford', 10000, 'auto', 'nuevo', [1,2,3,4]).
vehiculos('Ford', 15000, 'auto', 'nuevo', [1,2]).
vehiculos('Ford', 25000, 'auto', 'nuevo', [1,2,4]).
vehiculos('Ford', 13000, 'auto', 'usado', [1,4]).
vehiculos('Ford', 8000, 'auto', 'usado', [1,3]).
vehiculos('Ford', 9500, 'auto', 'usado', [1,4]).

vehiculos('Toyota', 20000, 'auto', 'nuevo', [2,3,4]).
vehiculos('Toyota', 28000, 'auto', 'nuevo', [1,2,3,4]).
vehiculos('Toyota', 16000, 'auto', 'usado', [1,2]).

vehiculos('Chevrolet', 40000, 'auto', 'nuevo', [2,3,4]).
vehiculos('Chevrolet', 50000, 'auto', 'nuevo', [1,3]).
vehiculos('Chevrolet', 10000, 'auto', 'nuevo', [2,3]).
vehiculos('Chevrolet', 9100, 'auto', 'usado', [1,3]).

caracteristicas(1, 'rojo').
caracteristicas(2, 'aire acondicionado').
caracteristicas(3, 'largo').
caracteristicas(4, 'al piso').
```

::::

(enunciado-15)=

## Enunciado

Revisar enunciado: no habia enunciado confiable en el archivo original. Inferido
a partir de la solucion del dominio `ventas` y sus predicados principales:
opcion, validar, calcular_consumo, validar_suma_y_cont, mostrar_promedio,
buscar_compradores, calcular_maximo.

::::{dropdown} solution-2.pl

```prolog
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
```

::::

::::{dropdown} solution.pl

```prolog
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
```

::::

::::{dropdown} bdventas.txt

```text
venta(123, 'auto', '10-08-2023', 100).
venta(123, 'tuerca', '10-07-2023', 200).
venta(123, 'zapatilla', '10-05-2022', 500).
venta(123, 'zapatilla', '10-04-2022', 500).
venta(123, 'zapatilla', '10-05-2023', 400).

venta(1234, 'casa', '10-05-2023', 700).
venta(1234, 'zapatilla', '10-05-2022', 400).
venta(1234, 'peluche', '10-05-2023', 200).
```

::::

(enunciado-16)=

## Enunciado

Revisar enunciado: no habia enunciado confiable en el archivo original. Inferido
a partir de la solucion del dominio `viajes` y sus predicados principales:
opcion, total_viajes_x_unidad, leer, mayores, ver_montos_viajes.

::::{dropdown} solution.pl

```prolog
:-dynamic(unidades/3).
:-dynamic(viajes/2).

inicio:-retractall(unidades(_,_,_)),retractall(viajes(_,_)),menu.

menu:- writeln('Ingrese opcion'),
        writeln('OPCION 0: Salir'),
        writeln('OPCION 1: Calcular total de viajes para cada unidad'),
        writeln('OPCION 2: Ingresar una lista de unidades, y listar las que tengan viajes mayores a 500'),
        read(Op),
        Op \=0,
        Op<3,
        opcion(Op),
        menu.

menu:- writeln('Gracias por usar el sistema experto!').

opcion(1):- abrir_base,
            calcular_viajes.

opcion(2):- abrir_base,
            writeln('Ingrese lista de unidades'),
            leer(ListaU),
            mayores(ListaU).
opcion(_).

abrir_base:- consult('bdviajes.txt').

calcular_viajes:- unidades(Nro,_,_),
                retract(unidades(Nro,_,_)),
                total_viajes_x_unidad(Nro, Cont),
                writeln('La cantidad de viajes para la unidad  '),writeln(Nro),write(' es '),write(Cont),
                calcular_viajes.
calcular_viajes.

total_viajes_x_unidad(Num,C):-viajes(Num,_),
                                retract(viajes(Num,_)),
                                total_viajes_x_unidad(Num,CNuevo),
                                C is CNuevo + 1.
total_viajes_x_unidad(_,0).

leer([H|T]):-read(H),H\=[],leer(T).
leer([]).

mayores([]).
mayores([H|Lista]):-
                retract(unidades(H,_,_)),
                ver_montos_viajes(C,H),
                C>0,
                writeln(H),
                mayores(Lista).
mayores([_|Lista]):-mayores(Lista).

ver_montos_viajes(C,Cod):-retract(viajes(Cod,Monto)),
                        Monto>500,
                        ver_montos_viajes(Conta,Cod),
                        C is Conta + 1.
ver_montos_viajes(0,_).
```

::::

::::{dropdown} bdviajes.txt

```text
:-dynamic unidades/3.
:-dynamic viajes/2.

unidades(1, 'Toyota', 'Camry'). 
unidades(2, 'Honda', 'Civic').
unidades(3, 'Ford', 'Focus').

viajes(1, 100).  
viajes(2, 100).
viajes(3, 6500).
viajes(1, 2500).
viajes(2, 300).
viajes(1, 100).
viajes(3, 6000).
viajes(1, 2000).
viajes(3, 6300).
```

::::

(enunciado-17)=

## Enunciado

Revisar enunciado: no habia enunciado confiable en el archivo original. Inferido
a partir de la solucion del dominio `vivero` y sus predicados principales:
opcion, leer, dividir_por_estacion, listar_por_estacion,
obtener_plantas_economicas, pertenece, listar_economicas.

::::{dropdown} solution-2.pl

```prolog
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
```

::::

::::{dropdown} solution.pl

```prolog
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
```

::::

::::{dropdown} bdvivero.txt

```text
vivero(1, 'Vivero A', [1, 2]).
vivero(2, 'Vivero B', [3, 4]).

plantas(1, 'otonio', 300, 1).
plantas(2, 'invierno', 500, 1).
plantas(3, 'primavera', 18000, 2).
plantas(4, 'verano', 12000, 2).
plantas(5, 'otonio', 3500, 3).
plantas(6, 'primavera', 5500, 3).
plantas(7, 'verano', 7500, 4).
plantas(8, 'otonio', 11000, 4).
plantas(9, 'otonio', 10000, 1).
plantas(10, 'invierno', 15000, 2).
plantas(11, 'primavera', 8, 3).
plantas(12, 'verano', 12, 4).
```

::::
