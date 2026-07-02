---
title: Práctica 4
kernelspec:
  name: calysto_prolog
  display_name: Calysto Prolog
---

# Práctica 4

PROLOG - Base de datos y Functores

## Ejercicio 1

1. Hacer un programa que permita definir las cuentas a pagar del mes (luz, agua,
   alquiler, teléfono, cable, supermercado, etc.) de un grupo de personas. A su
   vez, deberá permitir ingresar el nombre de una de ellas e informar de todos
   sus gastos.

### Tu solución

```{code-cell}
:tags: [skip-execution]

% Escribí y ejecutá tu solución para el ejercicio 1 acá.
```

### Consultas de prueba

```prolog
gastos_de(maria, Concepto, Monto)?
```

::::{dropdown} Solución

```prolog
gasto(maria, luz, 1000).
gasto(maria, alquiler, 50000).
gasto(juan, agua, 2500).
gastos_de(Persona, Concepto, Monto) :- gasto(Persona, Concepto, Monto).
```

::::

::::{dropdown} Verificación

Si el kernel soporta PlUnit, podés transformar estas consultas en pruebas
unitarias. En Calysto Prolog usá las consultas ejecutables como verificación de
respaldo.

```prolog
gastos_de(maria, Concepto, Monto)?
```

::::

```{code-cell}
:tags: [remove-cell]

gasto(maria, luz, 1000).
gasto(maria, alquiler, 50000).
gasto(juan, agua, 2500).
gastos_de(Persona, Concepto, Monto) :- gasto(Persona, Concepto, Monto).

gastos_de(maria, Concepto, Monto)?
```

## Ejercicio 2

2. Hacer un programa que defina una Base de datos de personas de la siguiente
   forma: personas(codigo,nombre). El programa debe permitir ingresar un código
   y verificar si el mismo está definido en la BBDD. De estarlo deberá informar
   a quién corresponde, de lo contrario deberá solicitar ingresar un nombre y
   registrar entonces la persona en la BBDD.

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
:- dynamic personas/2.
personas(1, ana).
personas(2, luis).
consultar_o_registrar(Codigo, Nombre) :- personas(Codigo, Nombre).
consultar_o_registrar(Codigo, Nombre) :-
    \+ personas(Codigo, _),
    assertz(personas(Codigo, Nombre)).
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

:- dynamic personas/2.
personas(1, ana).
personas(2, luis).
consultar_o_registrar(Codigo, Nombre) :- personas(Codigo, Nombre).
consultar_o_registrar(Codigo, Nombre) :-
    \+ personas(Codigo, _),
    assertz(personas(Codigo, Nombre)).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 3

3. Desarrollar un programa que permita definir los hábitos de:

- alimentación (comida, cantidad)
- bebida (bebida, cantidad)
- reproducción (época de reproducción, período de gestación)
- horas de sueño

de un conjunto de animales de un Zoo. Dicha información se guardará en una base
de datos. El programa, deberá permitir: a. Ingresar el nombre de un animal e
informar de todos sus hábitos. b. Ingresar un hábito e informar todos los
animales que lo tienen.

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
habito(leon, alimentacion(carne, mucha)).
habito(leon, suenio(18)).
habito(jirafa, alimentacion(hojas, mucha)).
habitos_de(Animal, Habito) :- habito(Animal, Habito).
animal_con_habito(Animal, Habito) :- habito(Animal, Habito).
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

habito(leon, alimentacion(carne, mucha)).
habito(leon, suenio(18)).
habito(jirafa, alimentacion(hojas, mucha)).
habitos_de(Animal, Habito) :- habito(Animal, Habito).
animal_con_habito(Animal, Habito) :- habito(Animal, Habito).

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 4

4. Ampliar el ejercicio 1 a través del uso de functores. Por ejemplo:
   gasto(maria, super(coto,500)). gasto(omar, tel(fijo,telecom,150)).
   gasto(maria,tel(movil,personal,100)).

a. Ingresar un gasto (por ej. super) e informar todas las personas que tienen
dicho gasto. b. Informar las personas que tienen un consumo superior a los $150
en un cierto gasto (dato de entrada). c. Calcular gasto promedio para una
determinada persona (dato de entrada).

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
gasto(maria, super(coto, 500)).
gasto(omar, tel(fijo, telecom, 150)).
gasto(maria, tel(movil, personal, 100)).
persona_con_gasto(Persona, Tipo) :-
    gasto(Persona, Gasto),
    functor(Gasto, Tipo, _).
consumo_superior(Persona, Tipo, Minimo) :-
    gasto(Persona, Gasto),
    functor(Gasto, Tipo, _),
    arg(_, Gasto, Monto), number(Monto), Monto > Minimo.
promedio_persona(Persona, Promedio) :-
    findall(Monto, (gasto(Persona, G), arg(_, G, Monto), number(Monto)), Montos),
    sum_list(Montos, Suma), length(Montos, Cantidad), Cantidad > 0,
    Promedio is Suma / Cantidad.
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

gasto(maria, super(coto, 500)).
gasto(omar, tel(fijo, telecom, 150)).
gasto(maria, tel(movil, personal, 100)).
persona_con_gasto(Persona, Tipo) :-
    gasto(Persona, Gasto),
    functor(Gasto, Tipo, _).
consumo_superior(Persona, Tipo, Minimo) :-
    gasto(Persona, Gasto),
    functor(Gasto, Tipo, _),
    arg(_, Gasto, Monto), number(Monto), Monto > Minimo.
promedio_persona(Persona, Promedio) :-
    findall(Monto, (gasto(Persona, G), arg(_, G, Monto), number(Monto)), Montos),
    sum_list(Montos, Suma), length(Montos, Cantidad), Cantidad > 0,
    Promedio is Suma / Cantidad.

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 5

5. Hacer un programa que permita realizar altas, bajas y consultas a la base de
   datos de una librería. De cada libro se registran los siguientes datos:

- Nro. de libro (auto numérico)
- Titulo
- Autor
- Editorial
- Precio

La base datos debe guardarse en disco. Calcular además el precio promedio de los
libros de un determinado autor.

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
:- dynamic libro/5.
alta_libro(Nro, Titulo, Autor, Editorial, Precio) :-
    assertz(libro(Nro, Titulo, Autor, Editorial, Precio)).
baja_libro(Nro) :- retractall(libro(Nro, _, _, _, _)).
consulta_libro(Nro, Titulo, Autor, Editorial, Precio) :-
    libro(Nro, Titulo, Autor, Editorial, Precio).
promedio_autor(Autor, Promedio) :-
    findall(Precio, libro(_, _, Autor, _, Precio), Precios),
    sum_list(Precios, Suma), length(Precios, Cantidad), Cantidad > 0,
    Promedio is Suma / Cantidad.
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

:- dynamic libro/5.
alta_libro(Nro, Titulo, Autor, Editorial, Precio) :-
    assertz(libro(Nro, Titulo, Autor, Editorial, Precio)).
baja_libro(Nro) :- retractall(libro(Nro, _, _, _, _)).
consulta_libro(Nro, Titulo, Autor, Editorial, Precio) :-
    libro(Nro, Titulo, Autor, Editorial, Precio).
promedio_autor(Autor, Promedio) :-
    findall(Precio, libro(_, _, Autor, _, Precio), Precios),
    sum_list(Precios, Suma), length(Precios, Cantidad), Cantidad > 0,
    Promedio is Suma / Cantidad.

% Ejecutá consultas propias sobre la solución.
```

## Ejercicio 6

6. Hacer un programa que permita registrar en una Base de Datos recetas de
   cocina. De cada receta se registran los siguientes datos:

- Código de receta
- Nombre de la receta Y por cada ingrediente que contenga la receta:
- Nombre del ingrediente
- Cantidad A su vez, permitir ingresar dos (2) ingredientes e informar de todas
  las recetas (Código y Nombre) que poseen ambos ingredientes. Por otro lado,
  para un ingrediente en particular y una cierta cantidad del mismo, determinar
  aquellas recetas que llevan ese ingrediente y superan dicha cantidad.

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
receta(1, ensalada, tomate, 2).
receta(1, ensalada, lechuga, 1).
receta(2, salsa, tomate, 5).
recetas_con_ingredientes(Codigo, Nombre, I1, I2) :-
    receta(Codigo, Nombre, I1, _),
    receta(Codigo, Nombre, I2, _),
    I1 \= I2.
recetas_con_cantidad(Codigo, Nombre, Ingrediente, Minimo) :-
    receta(Codigo, Nombre, Ingrediente, Cantidad),
    Cantidad > Minimo.
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

receta(1, ensalada, tomate, 2).
receta(1, ensalada, lechuga, 1).
receta(2, salsa, tomate, 5).
recetas_con_ingredientes(Codigo, Nombre, I1, I2) :-
    receta(Codigo, Nombre, I1, _),
    receta(Codigo, Nombre, I2, _),
    I1 \= I2.
recetas_con_cantidad(Codigo, Nombre, Ingrediente, Minimo) :-
    receta(Codigo, Nombre, Ingrediente, Cantidad),
    Cantidad > Minimo.

% Ejecutá consultas propias sobre la solución.
```
