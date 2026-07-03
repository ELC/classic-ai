---
title: Práctica 1
kernelspec:
  name: prolog_kernel
  display_name: Prolog
  language: prolog
---

# Práctica 1

PROLOG - Conceptos básicos

## Ejercicio 1

1. Teniendo la siguiente base de hechos...

```{code-cell} prolog

observa(maria, omar).
observa(laura, omar).
observa(maria, flavio).
observa(gabriela, flavio).
observa(maria, carlos).
```

Ejecutar las siguientes preguntas al Prolog y analizar la respuesta dada en cada

caso.







### Solución

```{code-cell} prolog
:tags: [hide-cell]

observa(maria, omar).
observa(laura, omar).
observa(maria, flavio).
observa(gabriela, flavio).
observa(maria, carlos).
```

### Verificación

```{code-cell} prolog
?- observa(maria, flavio).
```

```{code-cell} prolog
?- observa(maria, Quien).
```

## Ejercicio 2

2. Teniendo la siguiente base de hechos, definir una regla que permita

determinar quienes hablan el idioma inglés y francés.

```{code-cell} prolog

conoce(franco, ingles).
conoce(renzo, ingles).
conoce(franco, frances).
conoce(renzo, frances).
conoce(franco, italiano).
conoce(marco, ingles).
conoce(omar, ingles).
conoce(maria, frances).
```

### Solución

```{code-cell} prolog
:tags: [hide-cell]

conoce(franco, ingles).
conoce(renzo, ingles).
conoce(franco, frances).
conoce(renzo, frances).
conoce(franco, italiano).
conoce(marco, ingles).
conoce(omar, ingles).
conoce(maria, frances).

habla_ingles_y_frances(Persona) :-
    conoce(Persona, ingles), conoce(Persona, frances).
```

### Verificación

```{code-cell} prolog
?- habla_ingles_y_frances(Quien).
```

## Ejercicio 3

3. Escribir un programa Prolog que responda consultas acerca de cuáles son los

   rivales de una determinada selección en un campeonato mundial.

Una selección tiene como rivales todos los otros equipos de su mismo grupo.

Incluir en el programa la siguiente información:

- El grupo 1 está formado por Brasil, España, Jamaica e Italia.

- El grupo 2 está formado por Argentina, Nigeria, Holanda y Escocia.

El programa debe ser capaz de responder a las siguientes consultas: a) ¿Son

rivales Argentina y Brasil? b) ¿Cuáles son los rivales de un determinado equipo

(por ejemplo Holanda)?

### Solución

```{code-cell} prolog
:tags: [hide-cell]

grupo(1, brasil).
grupo(1, espania).
grupo(1, jamaica).
grupo(1, italia).
grupo(2, argentina).
grupo(2, nigeria).
grupo(2, holanda).
grupo(2, escocia).

rivales(Equipo, Rival) :-
    grupo(Grupo, Equipo), grupo(Grupo, Rival), Equipo \= Rival.
```

### Verificación

```{code-cell} prolog
?- rivales(argentina, holanda).
```

```{code-cell} prolog
?- rivales(holanda, Rival).
```

## Ejercicio 4

4. Dados los siguientes predicados:

```{code-cell} prolog

hombre(unHombre).
mujer(unaMujer).
```

```{code-cell} prolog

% padres(Persona, Madre, Padre).
```

a. Construya una base de hechos con los miembros de su familia. b. Defina las

siguientes reglas:

- hermana/2, donde significa que A es hermana de B.

```{code-cell} prolog

% hermana(A, B).
```

- nieto/2, donde significa que A es el nieto de B.

```{code-cell} prolog

% nieto(A, B).
```

- abuelo/2, donde significa que A es el abuelo de B.

```{code-cell} prolog

% abuelo(A, B).
```

- tia/2, donde significa que A es la tía de B. Esta regla definirla, en

```{code-cell} prolog

% tia(A, B).
```

una primera instancia, valiéndose sólo de los hechos disponibles. En una

segunda instancia, valiéndose de alguna otra regla que pudieron haber definido

previamente.

### Solución

```{code-cell} prolog
:tags: [hide-cell]

hombre(juan).
hombre(pedro).
hombre(carlos).
mujer(maria).
mujer(ana).
mujer(lucia).
padres(ana, maria, juan).
padres(lucia, ana, pedro).

hermana(A, B) :-
    mujer(A), padres(A, Madre, Padre), padres(B, Madre, Padre), A \= B.

nieto(A, B) :-
    padres(A, Madre, Padre), (padres(Madre, B, _) ; padres(Madre, _, B) ;
     padres(Padre, B, _) ; padres(Padre, _, B)).

abuelo(A, B) :-
    hombre(A), nieto(B, A).

tia(A, B) :-
    hermana(A, Madre), padres(B, Madre, _).
```

### Verificación

```{code-cell} prolog
?- nieto(lucia, maria).
```

## Ejercicio 5

5. Dada la siguiente base de hechos: %

```{code-cell} prolog

% auto(Patente, Propietario).
auto(hti687, pedro).
auto(jug144, juan).
auto(gqm758, pedro).
```

```{code-cell} prolog

% deuda(Patente, MontoAdeudado).
auto(lod445, carlos).
auto(lfz569, miguel).
auto(axk798, maria).
deuda(lfz569, 2000).
deuda(gqm758, 15000).
deuda(axk798, 1000).
```

Escriba una regla que permita determinar si una persona (dato entrada) tiene

algún auto con deuda.

### Solución

```{code-cell} prolog
:tags: [hide-cell]

auto(hti687, pedro).
auto(jug144, juan).
auto(gqm758, pedro).
auto(lod445, carlos).
auto(lfz569, miguel).
auto(axk798, maria).

deuda(lfz569, 2000).
deuda(gqm758, 15000).
deuda(axk798, 1000).

tiene_auto_con_deuda(Persona) :-
    auto(Patente, Persona), deuda(Patente, _).
```

### Verificación

```{code-cell} prolog
?- tiene_auto_con_deuda(pedro).
```

## Ejercicio 6

6. Escribir un programa Prolog que ayude a un organizador a armar un festival,

   considerando las diferentes bandas de música que se pueden formar en cada

   ciudad.

Para formar una banda son necesarios un guitarrista, un cantante y un baterista.

Se dispone de la siguiente información:

- Carolina y José son guitarristas y viven en Rosario.

- Miguel es guitarrista y vive en Funes.

- Mariano es un cantante que vive en Rosario.

- Silvia es una cantante que vive en Funes.

- Eduardo es un baterista que vive en Roldán.

- Diego es un baterista que vive en Casilda.

- Laura es una baterista que vive en Rosario.

- Mauro es cantante y vive en Funes.

El programa debe responder si en una ciudad (dato de entrada), se puede o no

formar una banda.

### Solución

```{code-cell} prolog
:tags: [hide-cell]

guitarrista(carolina, rosario).
guitarrista(jose, rosario).
guitarrista(miguel, funes).
cantante(mariano, rosario).
cantante(silvia, funes).
cantante(mauro, funes).
baterista(eduardo, roldan).
baterista(diego, casilda).
baterista(laura, rosario).

puede_formar_banda(Ciudad) :-
    guitarrista(_, Ciudad), cantante(_, Ciudad), baterista(_, Ciudad).
```

### Verificación

```{code-cell} prolog
?- puede_formar_banda(rosario).
```

## Ejercicio 7

7. Escribir un programa que simule una calculadora para las operaciones

   matemáticas básicas (suma, resta, multiplicación y división) entre dos

   valores numéricos, informando el resultado.

### Solución

```{code-cell} prolog
:tags: [hide-cell]

calcular(suma, A, B, Resultado) :- Resultado is A + B.
calcular(resta, A, B, Resultado) :- Resultado is A - B.
calcular(multiplicacion, A, B, Resultado) :- Resultado is A * B.
calcular(division, A, B, Resultado) :-
    B =\= 0, Resultado is A / B.
```

### Verificación

```{code-cell} prolog
?- calcular(suma, 2, 3, Resultado).
```

## Ejercicio 8

8. Dada la siguiente estructura de hechos:

```{code-cell} prolog

% horoscopo(Signo, DiaInicio, MesIni, DiaFin, MesFin).
```

Por ejemplo:

```{code-cell} prolog

horoscopo(aries, 21, 3, 20, 4).
horoscopo(tauro, 21, 4, 21, 5).
horoscopo(geminis, 22, 5, 21, 6).
```

Definir una regla del estilo que permita:

```{code-cell} prolog

% signo(Dia, Mes, Signo).
```

a. Ingresar un signo, día y mes y me informe si es correcto ese signo para esa

fecha. Ejemplo:



b. Ingresar una fecha (día y mes) y me informe de qué signo soy. Ejemplo:



## Recursividad

### Solución

```{code-cell} prolog
:tags: [hide-cell]

horoscopo(aries, 21, 3, 20, 4).
horoscopo(tauro, 21, 4, 21, 5).
horoscopo(geminis, 22, 5, 21, 6).
horoscopo(cancer, 22, 6, 22, 7).
horoscopo(leo, 23, 7, 22, 8).
horoscopo(virgo, 23, 8, 22, 9).
horoscopo(libra, 23, 9, 22, 10).
horoscopo(escorpio, 23, 10, 21, 11).
horoscopo(sagitario, 22, 11, 21, 12).
horoscopo(capricornio, 22, 12, 20, 1).
horoscopo(acuario, 21, 1, 19, 2).
horoscopo(piscis, 20, 2, 20, 3).
```

```{code-cell} prolog
:tags: [hide-cell]

fecha_en_rango(Dia, Mes, DiaInicio, MesInicio, DiaFin, MesFin) :-
    (MesInicio = MesFin, Mes = MesInicio, Dia >= DiaInicio, Dia =< DiaFin);
    (MesInicio < MesFin, ((Mes = MesInicio, Dia >= DiaInicio);
         (Mes = MesFin, Dia =< DiaFin);
         (Mes > MesInicio, Mes < MesFin)));
    (MesInicio > MesFin, ((Mes = MesInicio, Dia >= DiaInicio);
         (Mes = MesFin, Dia =< DiaFin);
         (Mes > MesInicio; Mes < MesFin))).
```

```{code-cell} prolog
:tags: [hide-cell]

signo(Dia, Mes, Signo) :-
    horoscopo(Signo, DiaInicio, MesInicio, DiaFin, MesFin), fecha_en_rango(Dia, Mes, DiaInicio, MesInicio, DiaFin, MesFin).
```

### Verificación

```{code-cell} prolog
?- signo(3, 5, tauro).
```

```{code-cell} prolog
?- signo(16, 12, Signo).
```

## Ejercicio 9

9. Se tiene la siguiente base de hechos:

```{code-cell} prolog

hijo(juan, miguel).
hijo(jose, miguel).
```

```{code-cell} prolog

hijo(miguel, roberto).
hijo(julio, roberto).
hijo(roberto, carlos).
```

Donde indica que X es hijo de Y. Definir la regla,

```{code-cell} prolog

hijo(X, Y).
descendiente(A, B).
```

la cual permite determinar si A es descendiente de B.

### Solución

```{code-cell} prolog
:tags: [hide-cell]

hijo(juan, miguel).
hijo(jose, miguel).
hijo(miguel, roberto).
hijo(julio, roberto).
hijo(roberto, carlos).

descendiente(A, B) :- hijo(A, B).
descendiente(A, B) :-
    hijo(A, C), descendiente(C, B).
```

### Verificación

```{code-cell} prolog
?- descendiente(juan, carlos).
```

## Ejercicio 10

10. Dada la siguiente red de tareas de un proyecto:

![Red de tareas de un proyecto](images/practica-01-red-tareas.png)

Definir la regla, la cual permite saber si para la ejecución de

```{code-cell} prolog

% requiere_de(X, Y).
```

la tarea Y se requiere tener finalizada la tarea X.

### Solución

```{code-cell} prolog
:tags: [hide-cell]

requiere_de(a, b).
requiere_de(b, c).
requiere_de(c, d).
requiere_de(a, e).

requiere_de(X, Y) :- requiere_de_directa(X, Y).
requiere_de(X, Y) :-
    requiere_de_directa(X, Z), requiere_de(Z, Y).

requiere_de_directa(a, b).
requiere_de_directa(b, c).
requiere_de_directa(c, d).
requiere_de_directa(a, e).
```

### Verificación

```{code-cell} prolog
?- requiere_de(a, d).
```

## Ejercicio 11

11. Hacer un programa para calcular el factorial de un número.

```{code-cell} prolog

% factorial(N, Fact).
```

- N es el número ingresado (argumento de entrada).

- Fact es el resultado calculado (argumento de salida).

### Solución

```{code-cell} prolog
:tags: [hide-cell]

factorial(0, 1).
factorial(N, Fact) :-
    N > 0, N1 is N - 1, factorial(N1, Fact1), Fact is N * Fact1.
```

### Verificación

```{code-cell} prolog
?- factorial(5, Resultado).
```

## Ejercicio 12

12. Hacer un programa que permita ingresar un número y calcule su sumatoria, es

    decir, la suma de sus términos descontados en una unidad hasta llegar a

    cero. Por ejemplo, si el número ingresado fuera 5, se deberá calcular la

sumatoria 5+4+3+2+1 e informar como resultado 15.

```{code-cell} prolog

% suma(N, Sum).
```

- N es el número ingresado (argumento de entrada).

- Sum es el resultado calculado (argumento de salida).

### Solución

```{code-cell} prolog
:tags: [hide-cell]

suma(0, 0).
suma(N, Sum) :-
    N > 0, N1 is N - 1, suma(N1, Sum1), Sum is N + Sum1.
```

### Verificación

```{code-cell} prolog
?- suma(5, Resultado).
```

## Ejercicio 13

13. Hacer un programa que permita ingresar un número y calcule la sumatoria de

    sus términos descontados en una unidad (hasta llegar a cero) pares e

impares.

```{code-cell} prolog

% suma(N, SumPares, SumImpares).
```

- N es el número ingresado (argumento de entrada).

- SumPares es uno de los resultados calculados (argumento de salida).

- SumImpares es uno de los resultados calculados (argumento de salida).

### Solución

```{code-cell} prolog
:tags: [hide-cell]

suma(0, 0, 0).
suma(N, SumPares, SumImpares) :-
    N > 0, N1 is N - 1, suma(N1, Pares1, Impares1), (0 is N mod 2 ->
        SumPares is Pares1 + N, SumImpares is Impares1
    ;
        SumPares is Pares1, SumImpares is Impares1 + N
    ).
```

### Verificación

```{code-cell} prolog
?- suma(5, Pares, Impares).
```
