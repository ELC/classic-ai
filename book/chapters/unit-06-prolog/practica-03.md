---
title: Práctica 3
kernelspec:
  name: calysto_prolog
  display_name: Calysto Prolog
---

# Práctica 3

PROLOG - Cadenas

## Ejercicio 1

1. Ingresar una cadena de texto y obtener el primer carácter de la misma.

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
primer_caracter(Cadena, Caracter) :- sub_atom(Cadena, 0, 1, _, Caracter).
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

primer_caracter(Cadena, Caracter) :- sub_atom(Cadena, 0, 1, _, Caracter).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 2

2. Ingresar una cadena de texto y obtener el último carácter de la misma.

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
ultimo_caracter(Cadena, Caracter) :-
    atom_length(Cadena, Longitud),
    Inicio is Longitud - 1,
    sub_atom(Cadena, Inicio, 1, 0, Caracter).
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

ultimo_caracter(Cadena, Caracter) :-
    atom_length(Cadena, Longitud),
    Inicio is Longitud - 1,
    sub_atom(Cadena, Inicio, 1, 0, Caracter).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 3

3. Ingresar una cadena de texto e informar cuántos caracteres tiene. En primer
   lugar haciendo uso del predicado atom_length/2 y en una segunda instancia
   utilizando sub_atom/5 de forma recursiva.

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
largo_atom(Cadena, Longitud) :- atom_length(Cadena, Longitud).
largo_recursivo(Cadena, Longitud) :-
    sub_atom(Cadena, 0, 1, Resto, _),
    sub_atom(Cadena, 1, Resto, 0, Cola),
    largo_recursivo(Cola, Parcial),
    Longitud is Parcial + 1.
largo_recursivo('', 0).
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

largo_atom(Cadena, Longitud) :- atom_length(Cadena, Longitud).
largo_recursivo(Cadena, Longitud) :-
    sub_atom(Cadena, 0, 1, Resto, _),
    sub_atom(Cadena, 1, Resto, 0, Cola),
    largo_recursivo(Cola, Parcial),
    Longitud is Parcial + 1.
largo_recursivo('', 0).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 4

4. Transformar una cadena en una lista de caracteres.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 4 acá.
```

### Consultas de prueba

```prolog
cadena_a_caracteres(hola, Caracteres)?
```

::::{dropdown} Solución

```prolog
cadena_a_caracteres(Cadena, Caracteres) :- atom_chars(Cadena, Caracteres).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
cadena_a_caracteres(hola, Caracteres)?
```

::::

```{code-cell}
:tags: [remove-cell]

cadena_a_caracteres(Cadena, Caracteres) :- atom_chars(Cadena, Caracteres).

cadena_a_caracteres(hola, Caracteres)?
```

## Ejercicio 5

5. Transformar una cadena de texto en una lista de palabras, tomando como
   divisor el espacio.

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
cadena_a_palabras(Cadena, Palabras) :- atomic_list_concat(Palabras, ' ', Cadena).
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

cadena_a_palabras(Cadena, Palabras) :- atomic_list_concat(Palabras, ' ', Cadena).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 6

6. Hacer un programa que transforme un número entero a binario.

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
a_binario(0, '0').
a_binario(N, Binario) :-
    N > 0,
    a_binario_lista(N, Lista),
    atomic_list_concat(Lista, Binario).
a_binario_lista(0, []).
a_binario_lista(N, Lista) :-
    N > 0,
    Bit is N mod 2,
    Cociente is N // 2,
    a_binario_lista(Cociente, Parcial),
    append(Parcial, [Bit], Lista).
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

a_binario(0, '0').
a_binario(N, Binario) :-
    N > 0,
    a_binario_lista(N, Lista),
    atomic_list_concat(Lista, Binario).
a_binario_lista(0, []).
a_binario_lista(N, Lista) :-
    N > 0,
    Bit is N mod 2,
    Cociente is N // 2,
    a_binario_lista(Cociente, Parcial),
    append(Parcial, [Bit], Lista).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 7

7. Hacer un reconocedor de palabras de la forma anbn.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 7 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
anbn(Palabra) :- atom_chars(Palabra, Caracteres), anbn_lista(Caracteres).
anbn_lista([]).
anbn_lista([a|Resto]) :- append(Medio, [b], Resto), anbn_lista(Medio).
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

anbn(Palabra) :- atom_chars(Palabra, Caracteres), anbn_lista(Caracteres).
anbn_lista([]).
anbn_lista([a|Resto]) :- append(Medio, [b], Resto), anbn_lista(Medio).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 8

8. Ingresar una cadena y un carácter, luego informar la cantidad de veces que
   aparece dicho carácter en la cadena.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 8 acá.
```

### Consultas de prueba

```prolog
% Ejecutá consultas propias sobre la solución.
```

::::{dropdown} Solución

```prolog
cantidad_caracter(Cadena, Caracter, Cantidad) :-
    atom_chars(Cadena, Caracteres),
    apariciones(Caracter, Caracteres, Cantidad).
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

cantidad_caracter(Cadena, Caracter, Cantidad) :-
    atom_chars(Cadena, Caracteres),
    apariciones(Caracter, Caracteres, Cantidad).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 9

9. Ingresar una cadena, contar e informar el número de veces que aparece cada
   una de las vocales (a, e, i, o, u) y la cantidad de veces que aparece
   cualquier consonante.

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
vocal(a). vocal(e). vocal(i). vocal(o). vocal(u).
contar_vocales(Cadena, A, E, I, O, U, Consonantes) :-
    atom_chars(Cadena, Caracteres),
    apariciones(a, Caracteres, A), apariciones(e, Caracteres, E),
    apariciones(i, Caracteres, I), apariciones(o, Caracteres, O),
    apariciones(u, Caracteres, U),
    contar_consonantes(Caracteres, Consonantes).
contar_consonantes([], 0).
contar_consonantes([C|Resto], Total) :-
    contar_consonantes(Resto, Parcial),
    (vocal(C) -> Total = Parcial ; Total is Parcial + 1).
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

vocal(a). vocal(e). vocal(i). vocal(o). vocal(u).
contar_vocales(Cadena, A, E, I, O, U, Consonantes) :-
    atom_chars(Cadena, Caracteres),
    apariciones(a, Caracteres, A), apariciones(e, Caracteres, E),
    apariciones(i, Caracteres, I), apariciones(o, Caracteres, O),
    apariciones(u, Caracteres, U),
    contar_consonantes(Caracteres, Consonantes).
contar_consonantes([], 0).
contar_consonantes([C|Resto], Total) :-
    contar_consonantes(Resto, Parcial),
    (vocal(C) -> Total = Parcial ; Total is Parcial + 1).

% Ejecutá consultas propias sobre la solución.
```
