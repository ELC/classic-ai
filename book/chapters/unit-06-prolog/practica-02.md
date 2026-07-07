---
title: Práctica 2
kernelspec:
  name: prolog_kernel
  display_name: Prolog
  language: prolog
---

(practica-2)=

# Práctica 2

PROLOG - Listas

(operaciones-basicas)=

## Operaciones básicas

(ejercicio-1-2)=

## Ejercicio 1

Ingresar una lista de elementos y mostrarla por pantalla.

(solucion-13)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

mostrar(Lista) :- write(Lista).
```

(verificacion-14)=

### Verificación

```{code-cell} prolog
?- with_output_to(atom(Salida), mostrar([a, b, c])), assertion(Salida == '[a,b,c]').
```

(ejercicio-2-2)=

## Ejercicio 2

Ingresar una lista de elementos y mostrar su cabeza y su cola.

(solucion-14)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

cabeza_cola(Lista, Cabeza, Cola) :- Lista = [Cabeza|Cola].
```

(verificacion-15)=

### Verificación

```{code-cell} prolog
?- cabeza_cola([a, b, c], Cabeza, Cola), assertion(Cabeza == a), assertion(Cola == [b, c]).
```

(ejercicio-3-2)=

## Ejercicio 3

Ingresar una lista de elementos y mostrar su primer elemento.

(solucion-15)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

primer_elemento(Lista, Primero) :- Lista = [Primero|_].
```

(verificacion-16)=

### Verificación

```{code-cell} prolog
?- primer_elemento([a, b, c], Primero), assertion(Primero == a).
```

(ejercicio-4-2)=

## Ejercicio 4

Ingresar una lista de elementos y mostrar sus dos primeros elementos.

(solucion-16)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

dos_primeros(Lista, Primero, Segundo) :- Lista = [Primero, Segundo|_].
```

(verificacion-17)=

### Verificación

```{code-cell} prolog
?- dos_primeros([a, b, c], Primero, Segundo), assertion(Primero == a), assertion(Segundo == b).
```

(ejercicio-5-2)=

## Ejercicio 5

Ingresar una lista de elementos y mostrar su último elemento.

(solucion-17)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

ultimo([Ultimo], Ultimo).
ultimo([_|Cola], Ultimo) :- ultimo(Cola, Ultimo).
```

(verificacion-18)=

### Verificación

```{code-cell} prolog
?- ultimo([a, b, c], Ultimo), assertion(Ultimo == c).
```

(ejercicio-6-2)=

## Ejercicio 6

Ingresar una lista de números enteros y calcular la diferencia entre el primero
y el último de ellos.

(solucion-18)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

diferencia_primero_ultimo([Primero|Cola], Diferencia) :-
    ultimo(Cola, Ultimo), Diferencia is Primero - Ultimo.
```

(verificacion-19)=

### Verificación

```{code-cell} prolog
?- diferencia_primero_ultimo([10, 2, 4], Diferencia), assertion(Diferencia =:= 6).
```

(ejercicio-7-2)=

## Ejercicio 7

Ingresar una lista de elementos e informar cuántos elementos tiene.

(solucion-19)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

cantidad([], 0).
cantidad([_|Cola], N) :- cantidad(Cola, N1), N is N1 + 1.
```

(verificacion-20)=

### Verificación

```{code-cell} prolog
?- cantidad([a, b, c], Cantidad), assertion(Cantidad =:= 3).
```

(ejercicio-8-2)=

## Ejercicio 8

Ingresar una lista de números enteros e informar cuánto da la sumatoria de
ellos.

(solucion-20)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

sumatoria([], 0).
sumatoria([Cabeza|Cola], Suma) :-
    sumatoria(Cola, Parcial), Suma is Cabeza + Parcial.
```

(verificacion-21)=

### Verificación

```{code-cell} prolog
?- sumatoria([1, 2, 3], Suma), assertion(Suma =:= 6).
```

(ejercicio-9-2)=

## Ejercicio 9

Ingresar una lista de números enteros y calcular su promedio. Respetar el
formato del predicado donde L es la lista ingresada, S la sumatoria y C el
contador de los elementos de la lista.

```{code-cell} prolog

% promedio(L, S, C).
```

(solucion-21)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

promedio(Lista, Suma, Cantidad) :-
    sumatoria(Lista, Suma), cantidad(Lista, Cantidad), Cantidad > 0.
```

(verificacion-22)=

### Verificación

```{code-cell} prolog
?- promedio([1, 2, 3], Suma, Cantidad), assertion(Suma =:= 6), assertion(Cantidad =:= 3).
```

(ejercicio-10-2)=

## Ejercicio 10

Ingresar una lista y un elemento e informar si ese elemento está en la lista.

(solucion-22)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

pertenece(Elemento, [Elemento|_]).
pertenece(Elemento, [_|Cola]) :- pertenece(Elemento, Cola).
```

(verificacion-23)=

### Verificación

```{code-cell} prolog
?- assertion(pertenece(b, [a, b, c])).
```

(ejercicio-11-2)=

## Ejercicio 11

Ingresar una lista de enteros e informar cuál es el mayor de todos los números.

(solucion-23)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

mayor([X], X).
mayor([Cabeza|Cola], Mayor) :-
    mayor(Cola, MayorCola), (Cabeza > MayorCola -> Mayor = Cabeza ; Mayor = MayorCola).
```

(verificacion-24)=

### Verificación

```{code-cell} prolog
?- mayor([3, 8, 2], Mayor), assertion(Mayor =:= 8).
```

(ejercicio-12-2)=

## Ejercicio 12

Ingresar una lista de enteros e informar cuál es el menor de todos los números.

(solucion-24)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

menor([X], X).
menor([Cabeza|Cola], Menor) :-
    menor(Cola, MenorCola), (Cabeza < MenorCola -> Menor = Cabeza ; Menor = MenorCola).
```

(verificacion-25)=

### Verificación

```{code-cell} prolog
?- menor([3, 8, 2], Menor), assertion(Menor =:= 2).
```

(ejercicio-13-2)=

## Ejercicio 13

Ingresar dos listas de elementos, concatenarlas (los elementos deben ser
asignados de a uno en la lista de salida) y mostrarlas en una tercera.

(solucion-25)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

concatenar([], Lista, Lista).
concatenar([Cabeza|Cola], Lista, [Cabeza|Resultado]) :-
    concatenar(Cola, Lista, Resultado).
```

(verificacion-26)=

### Verificación

```{code-cell} prolog
?- concatenar([a, b], [c, d], Resultado), assertion(Resultado == [a, b, c, d]).
```

(ejercicio-14)=

## Ejercicio 14

Ingresar una lista y determinar el primer elemento que se repite.

(solucion-26)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

primer_repetido([Cabeza|Cola], Cabeza) :- pertenece(Cabeza, Cola).
primer_repetido([_|Cola], Repetido) :- primer_repetido(Cola, Repetido).
```

(verificacion-27)=

### Verificación

```{code-cell} prolog
?- primer_repetido([a, b, c, b], Repetido), assertion(Repetido == b).
```

(ejercicio-15)=

## Ejercicio 15

Ingresar una lista y determinar a través de una segunda lista todos los
elementos que se repiten.

(solucion-27)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

repetidos([], []).
repetidos([Cabeza|Cola], [Cabeza|Resultado]) :-
    pertenece(Cabeza, Cola), repetidos(Cola, Resultado).
repetidos([Cabeza|Cola], Resultado) :-
    \+ pertenece(Cabeza, Cola), repetidos(Cola, Resultado).
```

(verificacion-28)=

### Verificación

```{code-cell} prolog
?- repetidos([a, b, c, b, a], Resultado), assertion(Resultado == [a, b]).
```

(ejercicio-16)=

## Ejercicio 16

Ingresar una lista y un elemento e informar cuántas veces está ese elemento en
la lista.

(solucion-28)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

apariciones(_, [], 0).
apariciones(Elemento, [Elemento|Cola], Cantidad) :-
    apariciones(Elemento, Cola, Parcial), Cantidad is Parcial + 1.
apariciones(Elemento, [Otro|Cola], Cantidad) :-
    Elemento \= Otro, apariciones(Elemento, Cola, Cantidad).
```

(verificacion-29)=

### Verificación

```{code-cell} prolog
?- apariciones(a, [a, b, a, c], Cantidad), assertion(Cantidad =:= 2).
```

(ejercicio-17)=

## Ejercicio 17

En una base de hechos hay un registro de personas y viajes realizados. Construir
una regla que permita verificar si una persona visitó una determinada ciudad
(datos de entrada: nombre persona y ciudad).

```{code-cell} prolog

% persona(Nombre, [ListaCiudadesVisito]).
```

(solucion-29)=

### Solución

```{code-cell} prolog
:tags: [hide-cell]

persona(ana, [rosario, cordoba, mendoza]).
persona(luis, [salta, rosario]).
visito(Persona, Ciudad) :-
    persona(Persona, Ciudades), pertenece(Ciudad, Ciudades).
```

(verificacion-30)=

### Verificación

```{code-cell} prolog
?- assertion(visito(ana, rosario)).
```
