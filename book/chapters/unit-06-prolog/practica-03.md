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

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

primer_caracter(hola, Caracter)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

primer_caracter(Cadena, Caracter) :- sub_atom(Cadena, 0, 1, _, Caracter).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

primer_caracter(hola, Caracter)?
```

::::

```{code-cell}
primer_caracter(Cadena, Caracter) :- sub_atom(Cadena, 0, 1, _, Caracter).

primer_caracter(hola, Caracter)?
```

## Ejercicio 2

2. Ingresar una cadena de texto y obtener el último carácter de la misma.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

ultimo_caracter(hola, Caracter)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

ultimo_caracter(hola, Caracter)?
```

::::

```{code-cell}
ultimo_caracter(Cadena, Caracter) :-
    atom_length(Cadena, Longitud),
    Inicio is Longitud - 1,
    sub_atom(Cadena, Inicio, 1, 0, Caracter).

ultimo_caracter(hola, Caracter)?
```

## Ejercicio 3

3. Ingresar una cadena de texto e informar cuántos caracteres tiene. En primer
   lugar haciendo uso del predicado atom_length/2 y en una segunda instancia
   utilizando sub_atom/5 de forma recursiva.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

largo_atom(hola, Longitud)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

largo_atom(hola, Longitud)?
```

::::

```{code-cell}
largo_atom(Cadena, Longitud) :- atom_length(Cadena, Longitud).
largo_recursivo(Cadena, Longitud) :-
    sub_atom(Cadena, 0, 1, Resto, _),
    sub_atom(Cadena, 1, Resto, 0, Cola),
    largo_recursivo(Cola, Parcial),
    Longitud is Parcial + 1.
largo_recursivo('', 0).

largo_atom(hola, Longitud)?
```

## Ejercicio 4

4. Transformar una cadena en una lista de caracteres.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

cadena_a_caracteres(hola, Caracteres)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

cadena_a_caracteres(Cadena, Caracteres) :- atom_chars(Cadena, Caracteres).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

cadena_a_caracteres(hola, Caracteres)?
```

::::

```{code-cell}
cadena_a_caracteres(Cadena, Caracteres) :- atom_chars(Cadena, Caracteres).

cadena_a_caracteres(hola, Caracteres)?
```

## Ejercicio 5

5. Transformar una cadena de texto en una lista de palabras, tomando como
   divisor el espacio.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

cadena_a_palabras('hola mundo', Palabras)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

cadena_a_palabras(Cadena, Palabras) :- atomic_list_concat(Palabras, ' ', Cadena).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

cadena_a_palabras('hola mundo', Palabras)?
```

::::

```{code-cell}
cadena_a_palabras(Cadena, Palabras) :- atomic_list_concat(Palabras, ' ', Cadena).

cadena_a_palabras('hola mundo', Palabras)?
```

## Ejercicio 6

6. Hacer un programa que transforme un número entero a binario.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

a_binario(5, Binario)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

a_binario(5, Binario)?
```

::::

```{code-cell}
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

a_binario(5, Binario)?
```

## Ejercicio 7

7. Hacer un reconocedor de palabras de la forma anbn.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

anbn(aabb)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

anbn(Palabra) :- atom_chars(Palabra, Caracteres), anbn_lista(Caracteres).
anbn_lista([]).
anbn_lista([a|Resto]) :- append(Medio, [b], Resto), anbn_lista(Medio).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

anbn(aabb)?
```

::::

```{code-cell}
anbn(Palabra) :- atom_chars(Palabra, Caracteres), anbn_lista(Caracteres).
anbn_lista([]).
anbn_lista([a|Resto]) :- append(Medio, [b], Resto), anbn_lista(Medio).

anbn(aabb)?
```

## Ejercicio 8

8. Ingresar una cadena y un carácter, luego informar la cantidad de veces que
   aparece dicho carácter en la cadena.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

cantidad_caracter(banana, a, Cantidad)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

cantidad_caracter(Cadena, Caracter, Cantidad) :-
    atom_chars(Cadena, Caracteres),
    apariciones(Caracter, Caracteres, Cantidad).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

cantidad_caracter(banana, a, Cantidad)?
```

::::

```{code-cell}
cantidad_caracter(Cadena, Caracter, Cantidad) :-
    atom_chars(Cadena, Caracteres),
    apariciones(Caracter, Caracteres, Cantidad).

cantidad_caracter(banana, a, Cantidad)?
```

## Ejercicio 9

9. Ingresar una cadena, contar e informar el número de veces que aparece cada
   una de las vocales (a, e, i, o, u) y la cantidad de veces que aparece
   cualquier consonante.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

contar_vocales(casa, A, E, I, O, U, Consonantes)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

```{code-cell}
:tags: [skip-execution]

contar_vocales(casa, A, E, I, O, U, Consonantes)?
```

::::
