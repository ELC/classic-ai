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

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

mostrar([a, b, c])?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

mostrar(Lista) :- write(Lista).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

mostrar([a, b, c])?
```

::::

```{code-cell}
mostrar(Lista) :- write(Lista).

mostrar([a, b, c])?
```

## Ejercicio 2

2. Ingresar una lista de elementos y mostrar su cabeza y su cola.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

cabeza_cola([a, b, c], Cabeza, Cola)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

cabeza_cola([Cabeza|Cola], Cabeza, Cola).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

cabeza_cola([a, b, c], Cabeza, Cola)?
```

::::

```{code-cell}
cabeza_cola([Cabeza|Cola], Cabeza, Cola).

cabeza_cola([a, b, c], Cabeza, Cola)?
```

## Ejercicio 3

3. Ingresar una lista de elementos y mostrar su primer elemento.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

primer_elemento([a, b, c], Primero)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

primer_elemento([Primero|_], Primero).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

primer_elemento([a, b, c], Primero)?
```

::::

```{code-cell}
primer_elemento([Primero|_], Primero).

primer_elemento([a, b, c], Primero)?
```

## Ejercicio 4

4. Ingresar una lista de elementos y mostrar sus dos primeros elementos.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

dos_primeros([a, b, c], Primero, Segundo)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

dos_primeros([Primero, Segundo|_], Primero, Segundo).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

dos_primeros([a, b, c], Primero, Segundo)?
```

::::

```{code-cell}
dos_primeros([Primero, Segundo|_], Primero, Segundo).

dos_primeros([a, b, c], Primero, Segundo)?
```

## Ejercicio 5

5. Ingresar una lista de elementos y mostrar su último elemento.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

ultimo([a, b, c], Ultimo)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

ultimo([Ultimo], Ultimo).
ultimo([_|Cola], Ultimo) :- ultimo(Cola, Ultimo).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

ultimo([a, b, c], Ultimo)?
```

::::

```{code-cell}
ultimo([Ultimo], Ultimo).
ultimo([_|Cola], Ultimo) :- ultimo(Cola, Ultimo).

ultimo([a, b, c], Ultimo)?
```

## Ejercicio 6

6. Ingresar una lista de números enteros y calcular la diferencia entre el
   primero y el último de ellos.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

diferencia_primero_ultimo([10, 2, 4], Diferencia)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

diferencia_primero_ultimo([Primero|Cola], Diferencia) :-
    ultimo(Cola, Ultimo),
    Diferencia is Primero - Ultimo.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

diferencia_primero_ultimo([10, 2, 4], Diferencia)?
```

::::

```{code-cell}
diferencia_primero_ultimo([Primero|Cola], Diferencia) :-
    ultimo(Cola, Ultimo),
    Diferencia is Primero - Ultimo.

diferencia_primero_ultimo([10, 2, 4], Diferencia)?
```

## Ejercicio 7

7. Ingresar una lista de elementos e informar cuántos elementos tiene.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

cantidad([a, b, c], Cantidad)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

cantidad([], 0).
cantidad([_|Cola], N) :- cantidad(Cola, N1), N is N1 + 1.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

cantidad([a, b, c], Cantidad)?
```

::::

```{code-cell}
cantidad([], 0).
cantidad([_|Cola], N) :- cantidad(Cola, N1), N is N1 + 1.

cantidad([a, b, c], Cantidad)?
```

## Ejercicio 8

8. Ingresar una lista de números enteros e informar cuánto da la sumatoria de
   ellos.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

sumatoria([1, 2, 3], Suma)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

sumatoria([1, 2, 3], Suma)?
```

::::

```{code-cell}
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

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

promedio([1, 2, 3], Suma, Cantidad)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

promedio([1, 2, 3], Suma, Cantidad)?
```

::::

```{code-cell}
promedio(Lista, Suma, Cantidad) :-
    sumatoria(Lista, Suma),
    cantidad(Lista, Cantidad),
    Cantidad > 0.

promedio([1, 2, 3], Suma, Cantidad)?
```

## Ejercicio 10

10. Ingresar una lista y un elemento e informar si ese elemento está en la
    lista.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

pertenece(b, [a, b, c])?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

pertenece(Elemento, [Elemento|_]).
pertenece(Elemento, [_|Cola]) :- pertenece(Elemento, Cola).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

pertenece(b, [a, b, c])?
```

::::

```{code-cell}
pertenece(Elemento, [Elemento|_]).
pertenece(Elemento, [_|Cola]) :- pertenece(Elemento, Cola).

pertenece(b, [a, b, c])?
```

## Ejercicio 11

11. Ingresar una lista de enteros e informar cuál es el mayor de todos los
    números.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

mayor([3, 8, 2], Mayor)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

mayor([3, 8, 2], Mayor)?
```

::::

```{code-cell}
mayor([X], X).
mayor([Cabeza|Cola], Mayor) :-
    mayor(Cola, MayorCola),
    (Cabeza > MayorCola -> Mayor = Cabeza ; Mayor = MayorCola).

mayor([3, 8, 2], Mayor)?
```

## Ejercicio 12

12. Ingresar una lista de enteros e informar cuál es el menor de todos los
    números.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

menor([3, 8, 2], Menor)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

menor([3, 8, 2], Menor)?
```

::::

```{code-cell}
menor([X], X).
menor([Cabeza|Cola], Menor) :-
    menor(Cola, MenorCola),
    (Cabeza < MenorCola -> Menor = Cabeza ; Menor = MenorCola).

menor([3, 8, 2], Menor)?
```

## Ejercicio 13

13. Ingresar dos listas de elementos, concatenarlas (los elementos deben ser
    asignados de a uno en la lista de salida) y mostrarlas en una tercera.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

concatenar([a, b], [c, d], Resultado)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

concatenar([], Lista, Lista).
concatenar([Cabeza|Cola], Lista, [Cabeza|Resultado]) :-
    concatenar(Cola, Lista, Resultado).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

concatenar([a, b], [c, d], Resultado)?
```

::::

```{code-cell}
concatenar([], Lista, Lista).
concatenar([Cabeza|Cola], Lista, [Cabeza|Resultado]) :-
    concatenar(Cola, Lista, Resultado).

concatenar([a, b], [c, d], Resultado)?
```

## Ejercicio 14

14. Ingresar una lista y determinar el primer elemento que se repite.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

primer_repetido([a, b, c, b], Repetido)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

primer_repetido([Cabeza|Cola], Cabeza) :- pertenece(Cabeza, Cola).
primer_repetido([_|Cola], Repetido) :- primer_repetido(Cola, Repetido).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

primer_repetido([a, b, c, b], Repetido)?
```

::::

```{code-cell}
primer_repetido([Cabeza|Cola], Cabeza) :- pertenece(Cabeza, Cola).
primer_repetido([_|Cola], Repetido) :- primer_repetido(Cola, Repetido).

primer_repetido([a, b, c, b], Repetido)?
```

## Ejercicio 15

15. Ingresar una lista y determinar a través de una segunda lista todos los
    elementos que se repiten.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

repetidos([a, b, c, b, a], Resultado)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

repetidos([a, b, c, b, a], Resultado)?
```

::::

```{code-cell}
repetidos([], []).
repetidos([Cabeza|Cola], [Cabeza|Resultado]) :-
    pertenece(Cabeza, Cola),
    repetidos(Cola, Resultado).
repetidos([Cabeza|Cola], Resultado) :-
    \+ pertenece(Cabeza, Cola),
    repetidos(Cola, Resultado).

repetidos([a, b, c, b, a], Resultado)?
```

## Ejercicio 16

16. Ingresar una lista y un elemento e informar cuántas veces está ese elemento
    en la lista.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

apariciones(a, [a, b, a, c], Cantidad)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

apariciones(a, [a, b, a, c], Cantidad)?
```

::::

```{code-cell}
apariciones(_, [], 0).
apariciones(Elemento, [Elemento|Cola], Cantidad) :-
    apariciones(Elemento, Cola, Parcial),
    Cantidad is Parcial + 1.
apariciones(Elemento, [Otro|Cola], Cantidad) :-
    Elemento \= Otro,
    apariciones(Elemento, Cola, Cantidad).

apariciones(a, [a, b, a, c], Cantidad)?
```

## Ejercicio 17

17. En una base de hechos hay un registro de personas y viajes realizados:
    persona(nombre, [lista ciudades visitó]) Construir una regla que permita
    verificar si una persona visitó una determinada ciudad (datos de entrada:
    nombre persona y ciudad).

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

visito(ana, rosario)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

visito(ana, rosario)?
```

::::
