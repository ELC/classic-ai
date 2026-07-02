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

```{code-cell} prolog
:tags: [skip-execution]

primer_caracter(hola, Caracter)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

primer_caracter(Cadena, Caracter) :- sub_atom(Cadena, 0, 1, _, Caracter).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

primer_caracter(hola, Caracter)?
```

### Resultado esperado

```{code-cell} prolog
primer_caracter(Cadena, Caracter) :- sub_atom(Cadena, 0, 1, _, Caracter).

primer_caracter(hola, Caracter)?
```

## Ejercicio 2

2. Ingresar una cadena de texto y obtener el último carácter de la misma.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

ultimo_caracter(hola, Caracter)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

ultimo_caracter(Cadena, Caracter) :-
    atom_length(Cadena, Longitud),
    Inicio is Longitud - 1,
    sub_atom(Cadena, Inicio, 1, 0, Caracter).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

ultimo_caracter(hola, Caracter)?
```

### Resultado esperado

```{code-cell} prolog
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

```{code-cell} prolog
:tags: [skip-execution]

largo_atom(hola, Longitud)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

largo_atom(Cadena, Longitud) :- atom_length(Cadena, Longitud).
largo_recursivo(Cadena, Longitud) :-
    sub_atom(Cadena, 0, 1, Resto, _),
    sub_atom(Cadena, 1, Resto, 0, Cola),
    largo_recursivo(Cola, Parcial),
    Longitud is Parcial + 1.
largo_recursivo('', 0).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

largo_atom(hola, Longitud)?
```

### Resultado esperado

```{code-cell} prolog
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

```{code-cell} prolog
:tags: [skip-execution]

cadena_a_caracteres(hola, Caracteres)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

cadena_a_caracteres(Cadena, Caracteres) :- atom_chars(Cadena, Caracteres).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

cadena_a_caracteres(hola, Caracteres)?
```

### Resultado esperado

```{code-cell} prolog
cadena_a_caracteres(Cadena, Caracteres) :- atom_chars(Cadena, Caracteres).

cadena_a_caracteres(hola, Caracteres)?
```

## Ejercicio 5

5. Transformar una cadena de texto en una lista de palabras, tomando como

   divisor el espacio.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

cadena_a_palabras('hola mundo', Palabras)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

cadena_a_palabras(Cadena, Palabras) :- atomic_list_concat(Palabras, ' ', Cadena).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

cadena_a_palabras('hola mundo', Palabras)?
```

### Resultado esperado

```{code-cell} prolog
cadena_a_palabras(Cadena, Palabras) :- atomic_list_concat(Palabras, ' ', Cadena).

cadena_a_palabras('hola mundo', Palabras)?
```

## Ejercicio 6

6. Hacer un programa que transforme un número entero a binario.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

a_binario(5, Binario)?
```

### Solución

```{code-cell} prolog
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

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

a_binario(5, Binario)?
```

### Resultado esperado

```{code-cell} prolog
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

```{code-cell} prolog
:tags: [skip-execution]

anbn(aabb)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

anbn(Palabra) :- atom_chars(Palabra, Caracteres), anbn_lista(Caracteres).
anbn_lista([]).
anbn_lista([a|Resto]) :- append(Medio, [b], Resto), anbn_lista(Medio).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

anbn(aabb)?
```

### Resultado esperado

```{code-cell} prolog
anbn(Palabra) :- atom_chars(Palabra, Caracteres), anbn_lista(Caracteres).
anbn_lista([]).
anbn_lista([a|Resto]) :- append(Medio, [b], Resto), anbn_lista(Medio).

anbn(aabb)?
```

## Ejercicio 8

8. Ingresar una cadena y un carácter, luego informar la cantidad de veces que

   aparece dicho carácter en la cadena.

### Consultas de prueba

```{code-cell} prolog
:tags: [skip-execution]

cantidad_caracter(banana, a, Cantidad)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

cantidad_caracter(Cadena, Caracter, Cantidad) :-
    atom_chars(Cadena, Caracteres),
    apariciones(Caracter, Caracteres, Cantidad).
```

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell} prolog
:tags: [skip-execution]

cantidad_caracter(banana, a, Cantidad)?
```

### Resultado esperado

```{code-cell} prolog
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

```{code-cell} prolog
:tags: [skip-execution]

contar_vocales(casa, A, E, I, O, U, Consonantes)?
```

### Solución

```{code-cell} prolog
:tags: [skip-execution]

vocal(a).
vocal(e).
vocal(i).
vocal(o).
vocal(u).
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

### Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

### Resultado esperado

```{code-cell} prolog
:tags: [skip-execution]

contar_vocales(casa, A, E, I, O, U, Consonantes)?
```
