---
title: Práctica 2
kernelspec:
  name: calysto_prolog
  display_name: Calysto Prolog
---

# Práctica 2

PROLOG - Listas

## Operaciones básicas

## Ejercicio 1

1. Ingresar una lista de elementos y mostrarla por pantalla.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 1 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
mostrar(Lista) :- write(Lista).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

mostrar(Lista) :- write(Lista).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 2

2. Ingresar una lista de elementos y mostrar su cabeza y su cola.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 2 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
cabeza_cola([Cabeza|Cola], Cabeza, Cola).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

cabeza_cola([Cabeza|Cola], Cabeza, Cola).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 3

3. Ingresar una lista de elementos y mostrar su primer elemento.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 3 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
primer_elemento([Primero|_], Primero).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

primer_elemento([Primero|_], Primero).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 4

4. Ingresar una lista de elementos y mostrar sus dos primeros elementos.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 4 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
dos_primeros([Primero, Segundo|_], Primero, Segundo).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

dos_primeros([Primero, Segundo|_], Primero, Segundo).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 5

5. Ingresar una lista de elementos y mostrar su último elemento.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 5 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
ultimo([Ultimo], Ultimo).
ultimo([_|Cola], Ultimo) :- ultimo(Cola, Ultimo).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

ultimo([Ultimo], Ultimo).
ultimo([_|Cola], Ultimo) :- ultimo(Cola, Ultimo).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 6

6. Ingresar una lista de números enteros y calcular la diferencia entre el
   primero y el último de ellos.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 6 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
diferencia_primero_ultimo([Primero|Cola], Diferencia) :-
    ultimo(Cola, Ultimo),
    Diferencia is Primero - Ultimo.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

diferencia_primero_ultimo([Primero|Cola], Diferencia) :-
    ultimo(Cola, Ultimo),
    Diferencia is Primero - Ultimo.

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 7

7. Ingresar una lista de elementos e informar cuántos elementos tiene.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 7 acá.
```

### Consultas de prueba

```prolog
cantidad([a, b, c], Cantidad)?
```

::::{dropdown} Solución

```prolog
cantidad([], 0).
cantidad([_|Cola], N) :- cantidad(Cola, N1), N is N1 + 1.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
cantidad([a, b, c], Cantidad)?
```

::::

```{code-cell}
:tags: [remove-cell]

cantidad([], 0).
cantidad([_|Cola], N) :- cantidad(Cola, N1), N is N1 + 1.

cantidad([a, b, c], Cantidad)?
```

## Ejercicio 8

8. Ingresar una lista de números enteros e informar cuánto da la sumatoria de
   ellos.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 8 acá.
```

### Consultas de prueba

```prolog
sumatoria([1, 2, 3], Suma)?
```

::::{dropdown} Solución

```prolog
sumatoria([], 0).
sumatoria([Cabeza|Cola], Suma) :-
    sumatoria(Cola, Parcial),
    Suma is Cabeza + Parcial.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
sumatoria([1, 2, 3], Suma)?
```

::::

```{code-cell}
:tags: [remove-cell]

sumatoria([], 0).
sumatoria([Cabeza|Cola], Suma) :-
    sumatoria(Cola, Parcial),
    Suma is Cabeza + Parcial.

sumatoria([1, 2, 3], Suma)?
```

## Ejercicio 9

9. Ingresar una lista de números enteros y calcular su promedio. Respetar el
   formato del predicado promedio(L,S,C) donde L es la lista ingresada, S la
   sumatoria y C el contador de los elementos de la lista.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 9 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
promedio(Lista, Suma, Cantidad) :-
    sumatoria(Lista, Suma),
    cantidad(Lista, Cantidad),
    Cantidad > 0.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

promedio(Lista, Suma, Cantidad) :-
    sumatoria(Lista, Suma),
    cantidad(Lista, Cantidad),
    Cantidad > 0.

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 10

10. Ingresar una lista y un elemento e informar si ese elemento está en la
    lista.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 10 acá.
```

### Consultas de prueba

```prolog
pertenece(b, [a, b, c])?
```

::::{dropdown} Solución

```prolog
pertenece(Elemento, [Elemento|_]).
pertenece(Elemento, [_|Cola]) :- pertenece(Elemento, Cola).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
pertenece(b, [a, b, c])?
```

::::

```{code-cell}
:tags: [remove-cell]

pertenece(Elemento, [Elemento|_]).
pertenece(Elemento, [_|Cola]) :- pertenece(Elemento, Cola).

pertenece(b, [a, b, c])?
```

## Ejercicio 11

11. Ingresar una lista de enteros e informar cuál es el mayor de todos los
    números.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 11 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
mayor([X], X).
mayor([Cabeza|Cola], Mayor) :-
    mayor(Cola, MayorCola),
    (Cabeza > MayorCola -> Mayor = Cabeza ; Mayor = MayorCola).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

mayor([X], X).
mayor([Cabeza|Cola], Mayor) :-
    mayor(Cola, MayorCola),
    (Cabeza > MayorCola -> Mayor = Cabeza ; Mayor = MayorCola).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 12

12. Ingresar una lista de enteros e informar cuál es el menor de todos los
    números.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 12 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
menor([X], X).
menor([Cabeza|Cola], Menor) :-
    menor(Cola, MenorCola),
    (Cabeza < MenorCola -> Menor = Cabeza ; Menor = MenorCola).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

menor([X], X).
menor([Cabeza|Cola], Menor) :-
    menor(Cola, MenorCola),
    (Cabeza < MenorCola -> Menor = Cabeza ; Menor = MenorCola).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 13

13. Ingresar dos listas de elementos, concatenarlas (los elementos deben ser
    asignados de a uno en la lista de salida) y mostrarlas en una tercera.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 13 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
concatenar([], Lista, Lista).
concatenar([Cabeza|Cola], Lista, [Cabeza|Resultado]) :-
    concatenar(Cola, Lista, Resultado).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

concatenar([], Lista, Lista).
concatenar([Cabeza|Cola], Lista, [Cabeza|Resultado]) :-
    concatenar(Cola, Lista, Resultado).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 14

14. Ingresar una lista y determinar el primer elemento que se repite.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 14 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
primer_repetido([Cabeza|Cola], Cabeza) :- pertenece(Cabeza, Cola).
primer_repetido([_|Cola], Repetido) :- primer_repetido(Cola, Repetido).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

primer_repetido([Cabeza|Cola], Cabeza) :- pertenece(Cabeza, Cola).
primer_repetido([_|Cola], Repetido) :- primer_repetido(Cola, Repetido).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 15

15. Ingresar una lista y determinar a través de una segunda lista todos los
    elementos que se repiten.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 15 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
repetidos([], []).
repetidos([Cabeza|Cola], [Cabeza|Resultado]) :-
    pertenece(Cabeza, Cola),
    repetidos(Cola, Resultado).
repetidos([Cabeza|Cola], Resultado) :-
    \+ pertenece(Cabeza, Cola),
    repetidos(Cola, Resultado).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

repetidos([], []).
repetidos([Cabeza|Cola], [Cabeza|Resultado]) :-
    pertenece(Cabeza, Cola),
    repetidos(Cola, Resultado).
repetidos([Cabeza|Cola], Resultado) :-
    \+ pertenece(Cabeza, Cola),
    repetidos(Cola, Resultado).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 16

16. Ingresar una lista y un elemento e informar cuántas veces está ese elemento
    en la lista.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 16 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
apariciones(_, [], 0).
apariciones(Elemento, [Elemento|Cola], Cantidad) :-
    apariciones(Elemento, Cola, Parcial),
    Cantidad is Parcial + 1.
apariciones(Elemento, [Otro|Cola], Cantidad) :-
    Elemento \= Otro,
    apariciones(Elemento, Cola, Cantidad).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

apariciones(_, [], 0).
apariciones(Elemento, [Elemento|Cola], Cantidad) :-
    apariciones(Elemento, Cola, Parcial),
    Cantidad is Parcial + 1.
apariciones(Elemento, [Otro|Cola], Cantidad) :-
    Elemento \= Otro,
    apariciones(Elemento, Cola, Cantidad).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 17

17. En una base de hechos hay un registro de personas y viajes realizados:
    persona(nombre, [lista ciudades visitó]) Construir una regla que permita
    verificar si una persona visitó una determinada ciudad (datos de entrada:
    nombre persona y ciudad).

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 17 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
persona(ana, [rosario, cordoba, mendoza]).
persona(luis, [salta, rosario]).
visito(Persona, Ciudad) :-
    persona(Persona, Ciudades),
    pertenece(Ciudad, Ciudades).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::

```{code-cell}
:tags: [remove-cell]

persona(ana, [rosario, cordoba, mendoza]).
persona(luis, [salta, rosario]).
visito(Persona, Ciudad) :-
    persona(Persona, Ciudades),
    pertenece(Ciudad, Ciudades).

% Ejecutá consultas propias sobre la solución.
```
