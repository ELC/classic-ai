---
title: Práctica 1
kernelspec:
  name: calysto_prolog
  display_name: Calysto Prolog
---

# Práctica 1

PROLOG - Conceptos básicos

## Ejercicio 1

1. Teniendo la siguiente base de hechos... observa(maria,omar).
   observa(laura,omar). observa(maria,flavio). observa(gabriela,flavio).
   observa(maria,carlos).

Ejecutar las siguientes preguntas al Prolog y analizar la respuesta dada en cada
caso. a. observa(maria,flavio). b. observa(maria,Quien). c. observa(maria,_). d.
observa(Quien,flavio). e. observa(Quien1,Quien2). f. observa(_,\_).

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

observa(maria, flavio)?
observa(maria, Quien)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

observa(maria, omar).
observa(laura, omar).
observa(maria, flavio).
observa(gabriela, flavio).
observa(maria, carlos).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

observa(maria, flavio)?
observa(maria, Quien)?
```

::::

```{code-cell}
observa(maria, omar).
observa(laura, omar).
observa(maria, flavio).
observa(gabriela, flavio).
observa(maria, carlos).

observa(maria, flavio)?
observa(maria, Quien)?
```

## Ejercicio 2

2. Teniendo la siguiente base de hechos, definir una regla que permita
   determinar quienes hablan el idioma inglés y francés. conoce(franco,ingles).
   conoce(renzo,ingles). conoce(franco,frances). conoce(renzo,frances).
   conoce(franco,italiano). conoce(marco,ingles). conoce(omar,ingles).
   conoce(maria,frances).

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

habla_ingles_y_frances(Quien)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

conoce(franco, ingles).
conoce(renzo, ingles).
conoce(franco, frances).
conoce(renzo, frances).
conoce(franco, italiano).
conoce(marco, ingles).
conoce(omar, ingles).
conoce(maria, frances).

habla_ingles_y_frances(Persona) :-
    conoce(Persona, ingles),
    conoce(Persona, frances).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

habla_ingles_y_frances(Quien)?
```

::::

```{code-cell}
conoce(franco, ingles).
conoce(renzo, ingles).
conoce(franco, frances).
conoce(renzo, frances).
conoce(franco, italiano).
conoce(marco, ingles).
conoce(omar, ingles).
conoce(maria, frances).

habla_ingles_y_frances(Persona) :-
    conoce(Persona, ingles),
    conoce(Persona, frances).

habla_ingles_y_frances(Quien)?
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

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

rivales(argentina, brasil)?
rivales(holanda, Rival)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

grupo(1, brasil).
grupo(1, espania).
grupo(1, jamaica).
grupo(1, italia).
grupo(2, argentina).
grupo(2, nigeria).
grupo(2, holanda).
grupo(2, escocia).

rivales(Equipo, Rival) :-
    grupo(Grupo, Equipo),
    grupo(Grupo, Rival),
    Equipo \= Rival.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

rivales(argentina, brasil)?
rivales(holanda, Rival)?
```

::::

```{code-cell}
grupo(1, brasil).
grupo(1, espania).
grupo(1, jamaica).
grupo(1, italia).
grupo(2, argentina).
grupo(2, nigeria).
grupo(2, holanda).
grupo(2, escocia).

rivales(Equipo, Rival) :-
    grupo(Grupo, Equipo),
    grupo(Grupo, Rival),
    Equipo \= Rival.

rivales(argentina, brasil)?
rivales(holanda, Rival)?
```

## Ejercicio 4

4. Dados los siguientes predicados: hombre(unHombre). mujer(unaMujer).
   padres(persona, madre, padre).

a. Construya una base de hechos con los miembros de su familia. b. Defina las
siguientes reglas:

- hermana/2, donde hermana(A,B) significa que A es hermana de B.
- nieto/2, donde nieto(A,B) significa que A es el nieto de B.
- abuelo/2, donde abuelo(A,B) significa que A es el abuelo de B.
- tia/2, donde tia(A,B) significa que A es la tía de B. Esta regla definirla, en
  una primera instancia, valiéndose sólo de los hechos disponibles. En una
  segunda instancia, valiéndose de alguna otra regla que pudieron haber definido
  previamente.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

nieto(lucia, maria)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

hombre(juan).
hombre(pedro).
hombre(carlos).
mujer(maria).
mujer(ana).
mujer(lucia).
padres(ana, maria, juan).
padres(lucia, ana, pedro).

hermana(A, B) :-
    mujer(A),
    padres(A, Madre, Padre),
    padres(B, Madre, Padre),
    A \= B.

nieto(A, B) :-
    padres(A, Madre, Padre),
    (padres(Madre, B, _) ; padres(Madre, _, B) ;
     padres(Padre, B, _) ; padres(Padre, _, B)).

abuelo(A, B) :-
    hombre(A),
    nieto(B, A).

tia(A, B) :-
    hermana(A, Madre),
    padres(B, Madre, _).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

nieto(lucia, maria)?
```

::::

```{code-cell}
hombre(juan).
hombre(pedro).
hombre(carlos).
mujer(maria).
mujer(ana).
mujer(lucia).
padres(ana, maria, juan).
padres(lucia, ana, pedro).

hermana(A, B) :-
    mujer(A),
    padres(A, Madre, Padre),
    padres(B, Madre, Padre),
    A \= B.

nieto(A, B) :-
    padres(A, Madre, Padre),
    (padres(Madre, B, _) ; padres(Madre, _, B) ;
     padres(Padre, B, _) ; padres(Padre, _, B)).

abuelo(A, B) :-
    hombre(A),
    nieto(B, A).

tia(A, B) :-
    hermana(A, Madre),
    padres(B, Madre, _).

nieto(lucia, maria)?
```

## Ejercicio 5

5. Dada la siguiente base de hechos: % auto(patente,propietario)
   auto(hti687,pedro). auto(jug144,juan). auto(gqm758,pedro).
   auto(lod445,carlos). auto(lfz569,miguel). auto(axk798,maria).

% deuda(patente, monto adeudado) deuda(lfz569,2000). deuda(gqm758,15000).
deuda(axk798,1000).

Escriba una regla que permita determinar si una persona (dato entrada) tiene
algún auto con deuda.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

tiene_auto_con_deuda(pedro)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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
    auto(Patente, Persona),
    deuda(Patente, _).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

tiene_auto_con_deuda(pedro)?
```

::::

```{code-cell}
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
    auto(Patente, Persona),
    deuda(Patente, _).

tiene_auto_con_deuda(pedro)?
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

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

puede_formar_banda(rosario)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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
    guitarrista(_, Ciudad),
    cantante(_, Ciudad),
    baterista(_, Ciudad).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

puede_formar_banda(rosario)?
```

::::

```{code-cell}
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
    guitarrista(_, Ciudad),
    cantante(_, Ciudad),
    baterista(_, Ciudad).

puede_formar_banda(rosario)?
```

## Ejercicio 7

7. Escribir un programa que simule una calculadora para las operaciones
   matemáticas básicas (suma, resta, multiplicación y división) entre dos
   valores numéricos, informando el resultado.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

calcular(suma, 2, 3, Resultado)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

calcular(suma, A, B, Resultado) :- Resultado is A + B.
calcular(resta, A, B, Resultado) :- Resultado is A - B.
calcular(multiplicacion, A, B, Resultado) :- Resultado is A * B.
calcular(division, A, B, Resultado) :-
    B =\= 0,
    Resultado is A / B.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

calcular(suma, 2, 3, Resultado)?
```

::::

```{code-cell}
calcular(suma, A, B, Resultado) :- Resultado is A + B.
calcular(resta, A, B, Resultado) :- Resultado is A - B.
calcular(multiplicacion, A, B, Resultado) :- Resultado is A * B.
calcular(division, A, B, Resultado) :-
    B =\= 0,
    Resultado is A / B.

calcular(suma, 2, 3, Resultado)?
```

## Ejercicio 8

8. Dada la siguiente estructura de hechos:

horoscopo(Signo,DiaInicio,MesIni,DiaFin,MesFin).

Por ejemplo: horoscopo(aries,21,3,20,4). horoscopo(tauro,21,4,21,5).
horoscopo(geminis,22,5,21,6).

Definir una regla del estilo signo(Dia, Mes, Signo) que permita:

a. Ingresar un signo, día y mes y me informe si es correcto ese signo para esa
fecha. Ejemplo: ?-signo(3,5,tauro). ?-signo(23,4,aries).

b. Ingresar una fecha (día y mes) y me informe de qué signo soy. Ejemplo:
?-signo(16,12,Signo). ?-signo(7,4,Signo).

## Recursividad

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

signo(3, 5, tauro)?
signo(16, 12, Signo)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

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

fecha_en_rango(Dia, Mes, DiaInicio, MesInicio, DiaFin, MesFin) :-
    (MesInicio = MesFin, Mes = MesInicio, Dia >= DiaInicio, Dia =< DiaFin);
    (MesInicio < MesFin,
        ((Mes = MesInicio, Dia >= DiaInicio);
         (Mes = MesFin, Dia =< DiaFin);
         (Mes > MesInicio, Mes < MesFin)));
    (MesInicio > MesFin,
        ((Mes = MesInicio, Dia >= DiaInicio);
         (Mes = MesFin, Dia =< DiaFin);
         (Mes > MesInicio; Mes < MesFin))).

signo(Dia, Mes, Signo) :-
    horoscopo(Signo, DiaInicio, MesInicio, DiaFin, MesFin),
    fecha_en_rango(Dia, Mes, DiaInicio, MesInicio, DiaFin, MesFin).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

signo(3, 5, tauro)?
signo(16, 12, Signo)?
```

::::

```{code-cell}
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

fecha_en_rango(Dia, Mes, DiaInicio, MesInicio, DiaFin, MesFin) :-
    (MesInicio = MesFin, Mes = MesInicio, Dia >= DiaInicio, Dia =< DiaFin);
    (MesInicio < MesFin,
        ((Mes = MesInicio, Dia >= DiaInicio);
         (Mes = MesFin, Dia =< DiaFin);
         (Mes > MesInicio, Mes < MesFin)));
    (MesInicio > MesFin,
        ((Mes = MesInicio, Dia >= DiaInicio);
         (Mes = MesFin, Dia =< DiaFin);
         (Mes > MesInicio; Mes < MesFin))).

signo(Dia, Mes, Signo) :-
    horoscopo(Signo, DiaInicio, MesInicio, DiaFin, MesFin),
    fecha_en_rango(Dia, Mes, DiaInicio, MesInicio, DiaFin, MesFin).

signo(3, 5, tauro)?
signo(16, 12, Signo)?
```

## Ejercicio 9

9. Se tiene la siguiente base de hechos: hijo(juan,miguel). hijo(jose,miguel).
   hijo(miguel,roberto). hijo(julio,roberto). hijo(roberto,carlos).

Donde hijo(X,Y) indica que X es hijo de Y. Definir la regla descendiente(A,B),
la cual permite determinar si A es descendiente de B.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

descendiente(juan, carlos)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

hijo(juan, miguel).
hijo(jose, miguel).
hijo(miguel, roberto).
hijo(julio, roberto).
hijo(roberto, carlos).

descendiente(A, B) :- hijo(A, B).
descendiente(A, B) :-
    hijo(A, C),
    descendiente(C, B).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

descendiente(juan, carlos)?
```

::::

```{code-cell}
hijo(juan, miguel).
hijo(jose, miguel).
hijo(miguel, roberto).
hijo(julio, roberto).
hijo(roberto, carlos).

descendiente(A, B) :- hijo(A, B).
descendiente(A, B) :-
    hijo(A, C),
    descendiente(C, B).

descendiente(juan, carlos)?
```

## Ejercicio 10

10. Dada la siguiente red de tareas de un proyecto:

![Red de tareas de un proyecto](images/practica-01-red-tareas.png)

Definir la regla requiere_de(X,Y), la cual permite saber si para la ejecución de
la tarea Y se requiere tener finalizada la tarea X.

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

requiere_de(a, d)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

requiere_de(a, b).
requiere_de(b, c).
requiere_de(c, d).
requiere_de(a, e).

requiere_de(X, Y) :- requiere_de_directa(X, Y).
requiere_de(X, Y) :-
    requiere_de_directa(X, Z),
    requiere_de(Z, Y).

requiere_de_directa(a, b).
requiere_de_directa(b, c).
requiere_de_directa(c, d).
requiere_de_directa(a, e).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

requiere_de(a, d)?
```

::::

```{code-cell}
requiere_de(a, b).
requiere_de(b, c).
requiere_de(c, d).
requiere_de(a, e).

requiere_de(X, Y) :- requiere_de_directa(X, Y).
requiere_de(X, Y) :-
    requiere_de_directa(X, Z),
    requiere_de(Z, Y).

requiere_de_directa(a, b).
requiere_de_directa(b, c).
requiere_de_directa(c, d).
requiere_de_directa(a, e).

requiere_de(a, d)?
```

## Ejercicio 11

11. Hacer un programa para calcular el factorial de un número.
    factorial(N,Fact).

- N es el número ingresado (argumento de entrada).
- Fact es el resultado calculado (argumento de salida).

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

factorial(5, Resultado)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

factorial(0, 1).
factorial(N, Fact) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, Fact1),
    Fact is N * Fact1.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

factorial(5, Resultado)?
```

::::

```{code-cell}
factorial(0, 1).
factorial(N, Fact) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, Fact1),
    Fact is N * Fact1.

factorial(5, Resultado)?
```

## Ejercicio 12

12. Hacer un programa que permita ingresar un número y calcule su sumatoria, es
    decir, la suma de sus términos descontados en una unidad hasta llegar a
    cero. Por ejemplo, si el número ingresado fuera 5, se deberá calcular la
    sumatoria 5+4+3+2+1 e informar como resultado 15. suma(N,Sum).

- N es el número ingresado (argumento de entrada).
- Sum es el resultado calculado (argumento de salida).

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

suma(5, Resultado)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

suma(0, 0).
suma(N, Sum) :-
    N > 0,
    N1 is N - 1,
    suma(N1, Sum1),
    Sum is N + Sum1.
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

suma(5, Resultado)?
```

::::

```{code-cell}
suma(0, 0).
suma(N, Sum) :-
    N > 0,
    N1 is N - 1,
    suma(N1, Sum1),
    Sum is N + Sum1.

suma(5, Resultado)?
```

## Ejercicio 13

13. Hacer un programa que permita ingresar un número y calcule la sumatoria de
    sus términos descontados en una unidad (hasta llegar a cero) pares e
    impares. suma(N,SumPares,SumImpares).

- N es el número ingresado (argumento de entrada).
- SumPares es uno de los resultados calculados (argumento de salida).
- SumImpares es uno de los resultados calculados (argumento de salida).

### Consultas de prueba

```{code-cell}
:tags: [skip-execution]

suma(5, Pares, Impares)?
```

::::{dropdown} Solución

```{code-cell}
:tags: [skip-execution]

suma(0, 0, 0).
suma(N, SumPares, SumImpares) :-
    N > 0,
    N1 is N - 1,
    suma(N1, Pares1, Impares1),
    (0 is N mod 2 ->
        SumPares is Pares1 + N,
        SumImpares is Impares1
    ;
        SumPares is Pares1,
        SumImpares is Impares1 + N
    ).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```{code-cell}
:tags: [skip-execution]

suma(5, Pares, Impares)?
```

::::
