---
title: Práctica 3
kernelspec:
  name: prolog_kernel
  display_name: Prolog
  language: prolog
---

# Práctica 3
PROLOG - Cadenas

## Ejercicio 1
Ingresar una cadena de texto y obtener el primer carácter de la misma.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

primer_caracter(Cadena, Caracter) :- sub_atom(Cadena, 0, 1, _, Caracter).
```

### Verificación
```{code-cell} prolog
?- primer_caracter(hola, Caracter), assertion(Caracter == h).
```

## Ejercicio 2
Ingresar una cadena de texto y obtener el último carácter de la misma.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

ultimo_caracter(Cadena, Caracter) :-
    atom_length(Cadena, Longitud), Inicio is Longitud - 1, sub_atom(Cadena, Inicio, 1, 0, Caracter).
```

### Verificación
```{code-cell} prolog
?- ultimo_caracter(hola, Caracter), assertion(Caracter == a).
```

## Ejercicio 3
Ingresar una cadena de texto e informar cuántos caracteres tiene. En primer
lugar haciendo uso del predicado atom_length/2 y en una segunda instancia
utilizando sub_atom/5 de forma recursiva.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

largo_atom(Cadena, Longitud) :- atom_length(Cadena, Longitud).
largo_recursivo(Cadena, Longitud) :-
    sub_atom(Cadena, 0, 1, Resto, _), sub_atom(Cadena, 1, Resto, 0, Cola), largo_recursivo(Cola, Parcial), Longitud is Parcial + 1.
largo_recursivo('', 0).
```

### Verificación
```{code-cell} prolog
?- largo_atom(hola, LongitudAtom), largo_recursivo(hola, LongitudRecursiva), assertion(LongitudAtom =:= 4), assertion(LongitudRecursiva =:= 4).
```

## Ejercicio 4
Transformar una cadena en una lista de caracteres.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

cadena_a_caracteres(Cadena, Caracteres) :- atom_chars(Cadena, Caracteres).
```

### Verificación
```{code-cell} prolog
?- cadena_a_caracteres(hola, Caracteres), assertion(Caracteres == [h, o, l, a]).
```

## Ejercicio 5
Transformar una cadena de texto en una lista de palabras, tomando como divisor
el espacio.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

cadena_a_palabras(Cadena, Palabras) :- atomic_list_concat(Palabras, ' ', Cadena).
```

### Verificación
```{code-cell} prolog
?- cadena_a_palabras('hola mundo', Palabras), assertion(Palabras == [hola, mundo]).
```

## Ejercicio 6
Hacer un programa que transforme un número entero a binario.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

a_binario(0, '0').
a_binario(N, Binario) :-
    N > 0, a_binario_lista(N, Lista), atomic_list_concat(Lista, Binario).
a_binario_lista(0, []).
a_binario_lista(N, Lista) :-
    N > 0, Bit is N mod 2, Cociente is N // 2, a_binario_lista(Cociente, Parcial), append(Parcial, [Bit], Lista).
```

### Verificación
```{code-cell} prolog
?- a_binario(5, Binario), assertion(Binario == '101').
```

## Ejercicio 7
Hacer un reconocedor de palabras de la forma anbn.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

anbn(Palabra) :- atom_chars(Palabra, Caracteres), anbn_lista(Caracteres).
anbn_lista([]).
anbn_lista([a|Resto]) :- append(Medio, [b], Resto), anbn_lista(Medio).
```

### Verificación
```{code-cell} prolog
?- assertion(anbn(aabb)).
```

```{code-cell} prolog
?- assertion(\+ anbn(aaab)).
```

## Ejercicio 8
Ingresar una cadena y un carácter, luego informar la cantidad de veces que
aparece dicho carácter en la cadena.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

cantidad_caracter(Cadena, Caracter, Cantidad) :-
    atom_chars(Cadena, Caracteres), apariciones_caracter(Caracter, Caracteres, Cantidad).
apariciones_caracter(_, [], 0).
apariciones_caracter(Elemento, [Elemento|Resto], Cantidad) :-
    apariciones_caracter(Elemento, Resto, Parcial), Cantidad is Parcial + 1.
apariciones_caracter(Elemento, [_|Resto], Cantidad) :- apariciones_caracter(Elemento, Resto, Cantidad).
```

### Verificación
```{code-cell} prolog
?- cantidad_caracter(banana, a, Cantidad), assertion(Cantidad =:= 3).
```

## Ejercicio 9
Ingresar una cadena, contar e informar el número de veces que aparece cada una
de las vocales (a, e, i, o, u) y la cantidad de veces que aparece cualquier
consonante.

### Solución
```{code-cell} prolog
:tags: [hide-cell]

vocal(a).
vocal(e).
vocal(i).
vocal(o).
vocal(u).
contar_vocales(Cadena, A, E, I, O, U, Consonantes) :-
    atom_chars(Cadena, Caracteres), apariciones_vocal(a, Caracteres, A), apariciones_vocal(e, Caracteres, E), apariciones_vocal(i, Caracteres, I), apariciones_vocal(o, Caracteres, O), apariciones_vocal(u, Caracteres, U), contar_consonantes(Caracteres, Consonantes).
apariciones_vocal(_, [], 0).
apariciones_vocal(Elemento, [Elemento|Resto], Cantidad) :-
    apariciones_vocal(Elemento, Resto, Parcial), Cantidad is Parcial + 1.
apariciones_vocal(Elemento, [_|Resto], Cantidad) :- apariciones_vocal(Elemento, Resto, Cantidad).
contar_consonantes([], 0).
contar_consonantes([C|Resto], Total) :-
    contar_consonantes(Resto, Parcial), (vocal(C) -> Total = Parcial ; Total is Parcial + 1).
```

### Verificación
```{code-cell} prolog
?- contar_vocales(casa, A, E, I, O, U, Consonantes), assertion(A =:= 2), assertion(E =:= 0), assertion(I =:= 0), assertion(O =:= 0), assertion(U =:= 0), assertion(Consonantes =:= 2).
```
