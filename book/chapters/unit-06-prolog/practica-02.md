---
title: Práctica 2
kernelspec:
  name: prolog_kernel
  display_name: Prolog
  language: prolog
---

# Práctica 2
PROLOG - Listas

## Operaciones básicas
## Ejercicio 1
Ingresar una lista de elementos y mostrarla por pantalla.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

mostrar(Lista) :- write(Lista).
```

### Verificación
```{code-cell} prolog
?- with_output_to(atom(Salida), mostrar([a, b, c])), assertion(Salida == '[a,b,c]').
```

## Ejercicio 2
Ingresar una lista de elementos y mostrar su cabeza y su cola.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

cabeza_cola(Lista, Cabeza, Cola) :- Lista = [Cabeza|Cola].
```

### Verificación
```{code-cell} prolog
?- cabeza_cola([a, b, c], Cabeza, Cola), assertion(Cabeza == a), assertion(Cola == [b, c]).
```

## Ejercicio 3
Ingresar una lista de elementos y mostrar su primer elemento.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

primer_elemento(Lista, Primero) :- Lista = [Primero|_].
```

### Verificación
```{code-cell} prolog
?- primer_elemento([a, b, c], Primero), assertion(Primero == a).
```

## Ejercicio 4
Ingresar una lista de elementos y mostrar sus dos primeros elementos.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

dos_primeros(Lista, Primero, Segundo) :- Lista = [Primero, Segundo|_].
```

### Verificación
```{code-cell} prolog
?- dos_primeros([a, b, c], Primero, Segundo), assertion(Primero == a), assertion(Segundo == b).
```

## Ejercicio 5
Ingresar una lista de elementos y mostrar su último elemento.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

ultimo([Ultimo], Ultimo).
ultimo([_|Cola], Ultimo) :- ultimo(Cola, Ultimo).
```

### Verificación
```{code-cell} prolog
?- ultimo([a, b, c], Ultimo), assertion(Ultimo == c).
```

## Ejercicio 6
Ingresar una lista de números enteros y calcular la diferencia entre el primero
y el último de ellos.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

diferencia_primero_ultimo([Primero|Cola], Diferencia) :-
    ultimo(Cola, Ultimo), Diferencia is Primero - Ultimo.
```

### Verificación
```{code-cell} prolog
?- diferencia_primero_ultimo([10, 2, 4], Diferencia), assertion(Diferencia =:= 6).
```

## Ejercicio 7
Ingresar una lista de elementos e informar cuántos elementos tiene.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

cantidad([], 0).
cantidad([_|Cola], N) :- cantidad(Cola, N1), N is N1 + 1.
```

### Verificación
```{code-cell} prolog
?- cantidad([a, b, c], Cantidad), assertion(Cantidad =:= 3).
```

## Ejercicio 8
Ingresar una lista de números enteros e informar cuánto da la sumatoria de
ellos.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

sumatoria([], 0).
sumatoria([Cabeza|Cola], Suma) :-
    sumatoria(Cola, Parcial), Suma is Cabeza + Parcial.
```

### Verificación
```{code-cell} prolog
?- sumatoria([1, 2, 3], Suma), assertion(Suma =:= 6).
```

## Ejercicio 9
Ingresar una lista de números enteros y calcular su promedio. Respetar el
formato del predicado donde L es la lista ingresada, S la sumatoria y C el
contador de los elementos de la lista.

```{code-cell} prolog

% promedio(L, S, C).
```

### Solución
```{code-cell} prolog
:tags: [hide-cell]

promedio(Lista, Suma, Cantidad) :-
    sumatoria(Lista, Suma), cantidad(Lista, Cantidad), Cantidad > 0.
```

### Verificación
```{code-cell} prolog
?- promedio([1, 2, 3], Suma, Cantidad), assertion(Suma =:= 6), assertion(Cantidad =:= 3).
```

## Ejercicio 10
Ingresar una lista y un elemento e informar si ese elemento está en la lista.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

pertenece(Elemento, [Elemento|_]).
pertenece(Elemento, [_|Cola]) :- pertenece(Elemento, Cola).
```

### Verificación
```{code-cell} prolog
?- assertion(pertenece(b, [a, b, c])).
```

## Ejercicio 11
Ingresar una lista de enteros e informar cuál es el mayor de todos los números.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

mayor([X], X).
mayor([Cabeza|Cola], Mayor) :-
    mayor(Cola, MayorCola), (Cabeza > MayorCola -> Mayor = Cabeza ; Mayor = MayorCola).
```

### Verificación
```{code-cell} prolog
?- mayor([3, 8, 2], Mayor), assertion(Mayor =:= 8).
```

## Ejercicio 12
Ingresar una lista de enteros e informar cuál es el menor de todos los números.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

menor([X], X).
menor([Cabeza|Cola], Menor) :-
    menor(Cola, MenorCola), (Cabeza < MenorCola -> Menor = Cabeza ; Menor = MenorCola).
```

### Verificación
```{code-cell} prolog
?- menor([3, 8, 2], Menor), assertion(Menor =:= 2).
```

## Ejercicio 13
Ingresar dos listas de elementos, concatenarlas (los elementos deben ser
asignados de a uno en la lista de salida) y mostrarlas en una tercera.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

concatenar([], Lista, Lista).
concatenar([Cabeza|Cola], Lista, [Cabeza|Resultado]) :-
    concatenar(Cola, Lista, Resultado).
```

### Verificación
```{code-cell} prolog
?- concatenar([a, b], [c, d], Resultado), assertion(Resultado == [a, b, c, d]).
```

## Ejercicio 14
Ingresar una lista y determinar el primer elemento que se repite.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

primer_repetido([Cabeza|Cola], Cabeza) :- pertenece(Cabeza, Cola).
primer_repetido([_|Cola], Repetido) :- primer_repetido(Cola, Repetido).
```

### Verificación
```{code-cell} prolog
?- primer_repetido([a, b, c, b], Repetido), assertion(Repetido == b).
```

## Ejercicio 15
Ingresar una lista y determinar a través de una segunda lista todos los
elementos que se repiten.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

repetidos([], []).
repetidos([Cabeza|Cola], [Cabeza|Resultado]) :-
    pertenece(Cabeza, Cola), repetidos(Cola, Resultado).
repetidos([Cabeza|Cola], Resultado) :-
    \+ pertenece(Cabeza, Cola), repetidos(Cola, Resultado).
```

### Verificación
```{code-cell} prolog
?- repetidos([a, b, c, b, a], Resultado), assertion(Resultado == [a, b]).
```

## Ejercicio 16
Ingresar una lista y un elemento e informar cuántas veces está ese elemento en
la lista.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

apariciones(_, [], 0).
apariciones(Elemento, [Elemento|Cola], Cantidad) :-
    apariciones(Elemento, Cola, Parcial), Cantidad is Parcial + 1.
apariciones(Elemento, [Otro|Cola], Cantidad) :-
    Elemento \= Otro, apariciones(Elemento, Cola, Cantidad).
```

### Verificación
```{code-cell} prolog
?- apariciones(a, [a, b, a, c], Cantidad), assertion(Cantidad =:= 2).
```

## Ejercicio 17
En una base de hechos hay un registro de personas y viajes realizados. Construir
una regla que permita verificar si una persona visitó una determinada ciudad
(datos de entrada: nombre persona y ciudad).

```{code-cell} prolog

% persona(Nombre, [ListaCiudadesVisito]).
```

### Solución
```{code-cell} prolog
:tags: [hide-cell]

persona(ana, [rosario, cordoba, mendoza]).
persona(luis, [salta, rosario]).
visito(Persona, Ciudad) :-
    persona(Persona, Ciudades), pertenece(Ciudad, Ciudades).
```

### Verificación
```{code-cell} prolog
?- assertion(visito(ana, rosario)).
```
