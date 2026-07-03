---
title: Práctica 2
kernelspec:
  name: calysto_prolog
  display_name: Calysto Prolog
  language: prolog
---

# Práctica 2

PROLOG - Listas

## Operaciones básicas

## Ejercicio 1

1. Ingresar una lista de elementos y mostrarla por pantalla.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

mostrar([a,b,c])?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

mostrar(Lista) :- write(Lista).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

mostrar([a,b,c])?
```

### Resultado esperado

```{code-cell} prolog
mostrar(Lista) :- write(Lista).
```

```{code-cell} prolog
mostrar([a,b,c])?
```

## Ejercicio 2

2. Ingresar una lista de elementos y mostrar su cabeza y su cola.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

cabeza_cola([a,b,c],Cabeza,Cola)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

cabeza_cola([Cabeza|Cola], Cabeza, Cola).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

cabeza_cola([a,b,c],Cabeza,Cola)?
```

### Resultado esperado

```{code-cell} prolog
cabeza_cola([Cabeza|Cola], Cabeza, Cola).
```

```{code-cell} prolog
cabeza_cola([a,b,c],Cabeza,Cola)?
```

## Ejercicio 3

3. Ingresar una lista de elementos y mostrar su primer elemento.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

primer_elemento([a,b,c],Primero)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

primer_elemento([Primero|_], Primero).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

primer_elemento([a,b,c],Primero)?
```

### Resultado esperado

```{code-cell} prolog
primer_elemento([Primero|_], Primero).
```

```{code-cell} prolog
primer_elemento([a,b,c],Primero)?
```

## Ejercicio 4

4. Ingresar una lista de elementos y mostrar sus dos primeros elementos.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

dos_primeros([a,b,c],Primero,Segundo)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

dos_primeros([Primero, Segundo|_], Primero, Segundo).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

dos_primeros([a,b,c],Primero,Segundo)?
```

### Resultado esperado

```{code-cell} prolog
dos_primeros([Primero, Segundo|_], Primero, Segundo).
```

```{code-cell} prolog
dos_primeros([a,b,c],Primero,Segundo)?
```

## Ejercicio 5

5. Ingresar una lista de elementos y mostrar su último elemento.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

ultimo([a,b,c],Ultimo)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

ultimo([Ultimo], Ultimo).
ultimo([_|Cola], Ultimo) :- ultimo(Cola, Ultimo).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

ultimo([a,b,c],Ultimo)?
```

### Resultado esperado

```{code-cell} prolog
ultimo([Ultimo], Ultimo).
ultimo([_|Cola], Ultimo) :- ultimo(Cola, Ultimo).
```

```{code-cell} prolog
ultimo([a,b,c],Ultimo)?
```

## Ejercicio 6

6. Ingresar una lista de números enteros y calcular la diferencia entre el

   primero y el último de ellos.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

diferencia_primero_ultimo([10,2,4],Diferencia)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

diferencia_primero_ultimo([Primero|Cola], Diferencia) :-
    ultimo(Cola, Ultimo), Diferencia is Primero - Ultimo.
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

diferencia_primero_ultimo([10,2,4],Diferencia)?
```

### Resultado esperado

```{code-cell} prolog
diferencia_primero_ultimo([Primero|Cola], Diferencia) :-
    ultimo(Cola, Ultimo), Diferencia is Primero - Ultimo.
```

```{code-cell} prolog
diferencia_primero_ultimo([10,2,4],Diferencia)?
```

## Ejercicio 7

7. Ingresar una lista de elementos e informar cuántos elementos tiene.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

cantidad([a,b,c],Cantidad)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

cantidad([], 0).
cantidad([_|Cola], N) :- cantidad(Cola, N1), N is N1 + 1.
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

cantidad([a,b,c],Cantidad)?
```

### Resultado esperado

```{code-cell} prolog
cantidad([], 0).
cantidad([_|Cola], N) :- cantidad(Cola, N1), N is N1 + 1.
```

```{code-cell} prolog
cantidad([a,b,c],Cantidad)?
```

## Ejercicio 8

8. Ingresar una lista de números enteros e informar cuánto da la sumatoria de

   ellos.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

sumatoria([1,2,3],Suma)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

sumatoria([], 0).
sumatoria([Cabeza|Cola], Suma) :-
    sumatoria(Cola, Parcial), Suma is Cabeza + Parcial.
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

sumatoria([1,2,3],Suma)?
```

### Resultado esperado

```{code-cell} prolog
sumatoria([], 0).
sumatoria([Cabeza|Cola], Suma) :-
    sumatoria(Cola, Parcial), Suma is Cabeza + Parcial.
```

```{code-cell} prolog
sumatoria([1,2,3],Suma)?
```

## Ejercicio 9

9. Ingresar una lista de números enteros y calcular su promedio. Respetar el

formato del predicado donde L es la lista ingresada, S la

```{code-cell} prolog
:tags: [skip-execution]

promedio(L, S, C).
```

sumatoria y C el contador de los elementos de la lista.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

promedio([1,2,3],Suma,Cantidad)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

promedio(Lista, Suma, Cantidad) :-
    sumatoria(Lista, Suma), cantidad(Lista, Cantidad), Cantidad > 0.
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

promedio([1,2,3],Suma,Cantidad)?
```

### Resultado esperado

```{code-cell} prolog
promedio(Lista, Suma, Cantidad) :-
    sumatoria(Lista, Suma), cantidad(Lista, Cantidad), Cantidad > 0.
```

```{code-cell} prolog
promedio([1,2,3],Suma,Cantidad)?
```

## Ejercicio 10

10. Ingresar una lista y un elemento e informar si ese elemento está en la

    lista.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

pertenece(b,[a,b,c])?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

pertenece(Elemento, [Elemento|_]).
pertenece(Elemento, [_|Cola]) :- pertenece(Elemento, Cola).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

pertenece(b,[a,b,c])?
```

### Resultado esperado

```{code-cell} prolog
pertenece(Elemento, [Elemento|_]).
pertenece(Elemento, [_|Cola]) :- pertenece(Elemento, Cola).
```

```{code-cell} prolog
pertenece(b,[a,b,c])?
```

## Ejercicio 11

11. Ingresar una lista de enteros e informar cuál es el mayor de todos los

    números.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

mayor([3,8,2],Mayor)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

mayor([X], X).
mayor([Cabeza|Cola], Mayor) :-
    mayor(Cola, MayorCola), (Cabeza > MayorCola -> Mayor = Cabeza ; Mayor = MayorCola).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

mayor([3,8,2],Mayor)?
```

### Resultado esperado

```{code-cell} prolog
mayor([X], X).
mayor([Cabeza|Cola], Mayor) :-
    mayor(Cola, MayorCola), (Cabeza > MayorCola -> Mayor = Cabeza ; Mayor = MayorCola).
```

```{code-cell} prolog
mayor([3,8,2],Mayor)?
```

## Ejercicio 12

12. Ingresar una lista de enteros e informar cuál es el menor de todos los

    números.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

menor([3,8,2],Menor)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

menor([X], X).
menor([Cabeza|Cola], Menor) :-
    menor(Cola, MenorCola), (Cabeza < MenorCola -> Menor = Cabeza ; Menor = MenorCola).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

menor([3,8,2],Menor)?
```

### Resultado esperado

```{code-cell} prolog
menor([X], X).
menor([Cabeza|Cola], Menor) :-
    menor(Cola, MenorCola), (Cabeza < MenorCola -> Menor = Cabeza ; Menor = MenorCola).
```

```{code-cell} prolog
menor([3,8,2],Menor)?
```

## Ejercicio 13

13. Ingresar dos listas de elementos, concatenarlas (los elementos deben ser

    asignados de a uno en la lista de salida) y mostrarlas en una tercera.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

concatenar([a,b],[c,d],Resultado)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

concatenar([], Lista, Lista).
concatenar([Cabeza|Cola], Lista, [Cabeza|Resultado]) :-
    concatenar(Cola, Lista, Resultado).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

concatenar([a,b],[c,d],Resultado)?
```

### Resultado esperado

```{code-cell} prolog
concatenar([], Lista, Lista).
concatenar([Cabeza|Cola], Lista, [Cabeza|Resultado]) :-
    concatenar(Cola, Lista, Resultado).
```

```{code-cell} prolog
concatenar([a,b],[c,d],Resultado)?
```

## Ejercicio 14

14. Ingresar una lista y determinar el primer elemento que se repite.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

primer_repetido([a,b,c,b],Repetido)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

primer_repetido([Cabeza|Cola], Cabeza) :- pertenece(Cabeza, Cola).
primer_repetido([_|Cola], Repetido) :- primer_repetido(Cola, Repetido).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

primer_repetido([a,b,c,b],Repetido)?
```

### Resultado esperado

```{code-cell} prolog
primer_repetido([Cabeza|Cola], Cabeza) :- pertenece(Cabeza, Cola).
primer_repetido([_|Cola], Repetido) :- primer_repetido(Cola, Repetido).
```

```{code-cell} prolog
primer_repetido([a,b,c,b],Repetido)?
```

## Ejercicio 15

15. Ingresar una lista y determinar a través de una segunda lista todos los

    elementos que se repiten.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

repetidos([a,b,c,b,a],Resultado)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

repetidos([], []).
repetidos([Cabeza|Cola], [Cabeza|Resultado]) :-
    pertenece(Cabeza, Cola), repetidos(Cola, Resultado).
repetidos([Cabeza|Cola], Resultado) :-
    \+ pertenece(Cabeza, Cola), repetidos(Cola, Resultado).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

repetidos([a,b,c,b,a],Resultado)?
```

### Resultado esperado

```{code-cell} prolog
repetidos([], []).
repetidos([Cabeza|Cola], [Cabeza|Resultado]) :-
    pertenece(Cabeza, Cola), repetidos(Cola, Resultado).
repetidos([Cabeza|Cola], Resultado) :-
    \+ pertenece(Cabeza, Cola), repetidos(Cola, Resultado).
```

```{code-cell} prolog
repetidos([a,b,c,b,a],Resultado)?
```

## Ejercicio 16

16. Ingresar una lista y un elemento e informar cuántas veces está ese elemento

    en la lista.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

apariciones(a,[a,b,a,c],Cantidad)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

apariciones(_, [], 0).
apariciones(Elemento, [Elemento|Cola], Cantidad) :-
    apariciones(Elemento, Cola, Parcial), Cantidad is Parcial + 1.
apariciones(Elemento, [Otro|Cola], Cantidad) :-
    Elemento \= Otro, apariciones(Elemento, Cola, Cantidad).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

apariciones(a,[a,b,a,c],Cantidad)?
```

### Resultado esperado

```{code-cell} prolog
apariciones(_, [], 0).
apariciones(Elemento, [Elemento|Cola], Cantidad) :-
    apariciones(Elemento, Cola, Parcial), Cantidad is Parcial + 1.
apariciones(Elemento, [Otro|Cola], Cantidad) :-
    Elemento \= Otro, apariciones(Elemento, Cola, Cantidad).
```

```{code-cell} prolog
apariciones(a,[a,b,a,c],Cantidad)?
```

## Ejercicio 17

17. En una base de hechos hay un registro de personas y viajes realizados:

Construir una regla que permita

```{code-cell} prolog
:tags: [skip-execution]

persona(nombre, [lista ciudades visitó]).
```

```
verificar si una persona visitó una determinada ciudad (datos de entrada:

nombre persona y ciudad).
```

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

visito(ana,rosario)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

persona(ana, [rosario, cordoba, mendoza]).
persona(luis, [salta, rosario]).
visito(Persona, Ciudad) :-
    persona(Persona, Ciudades), pertenece(Ciudad, Ciudades).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

### Resultado esperado

```{code-cell} prolog
:tags: [skip-execution]

visito(ana,rosario)?
```
