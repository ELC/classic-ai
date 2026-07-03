---
title: Práctica 4
kernelspec:
  name: prolog_kernel
  display_name: Prolog
  language: prolog
---

# Práctica 4

PROLOG - Base de datos y Functores

## Ejercicio 1

1. Hacer un programa que permita definir las cuentas a pagar del mes (luz, agua,

   alquiler, teléfono, cable, supermercado, etc.) de un grupo de personas. A su

   vez, deberá permitir ingresar el nombre de una de ellas e informar de todos

   sus gastos.

### Solución

```{code-cell} prolog
:tags: [hide-cell]

gasto(maria, luz, 1000).
gasto(maria, alquiler, 50000).
gasto(juan, agua, 2500).
gastos_de(Persona, Concepto, Monto) :- gasto(Persona, Concepto, Monto).
```

### Verificación

```{code-cell} prolog
?- gastos_de(maria, Concepto, Monto).
```

## Ejercicio 2

2. Hacer un programa que defina una Base de datos de personas de la siguiente

forma: El programa debe permitir ingresar un código

```{code-cell} prolog

% personas(Codigo, Nombre).
```

y verificar si el mismo está definido en la BBDD. De estarlo deberá informar

a quién corresponde, de lo contrario deberá solicitar ingresar un nombre y

registrar entonces la persona en la BBDD.

### Solución

```{code-cell} prolog
:tags: [hide-cell]

personas(1, ana).
personas(2, luis).
consultar_o_registrar(Codigo, Nombre) :- personas(Codigo, Nombre).
consultar_o_registrar(Codigo, Nombre) :-
    \+ personas(Codigo, _), assertz(personas(Codigo, Nombre)).
```

### Verificación

```{code-cell} prolog
?- consultar_o_registrar(1, Nombre).
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

### Solución

```{code-cell} prolog
:tags: [hide-cell]

habito(leon, alimentacion(carne, mucha)).
habito(leon, suenio(18)).
habito(jirafa, alimentacion(hojas, mucha)).
habitos_de(Animal, Habito) :- habito(Animal, Habito).
animal_con_habito(Animal, Habito) :- habito(Animal, Habito).
```

### Verificación

```{code-cell} prolog
?- habitos_de(leon, Habito).
```

## Ejercicio 4

4. Ampliar el ejercicio 1 a través del uso de functores. Por ejemplo:

```{code-cell} prolog

gasto(maria, super(coto, 500)).
gasto(omar, tel(fijo, telecom, 150)).
gasto(maria, tel(movil, personal, 100)).
```

a. Ingresar un gasto (por ej. super) e informar todas las personas que tienen

dicho gasto. b. Informar las personas que tienen un consumo superior a los $150

en un cierto gasto (dato de entrada). c. Calcular gasto promedio para una

determinada persona (dato de entrada).

### Solución

```{code-cell} prolog
:tags: [hide-cell]

gasto(maria, super(coto, 500)).
gasto(omar, tel(fijo, telecom, 150)).
gasto(maria, tel(movil, personal, 100)).
persona_con_gasto(Persona, Tipo) :-
    gasto(Persona, Gasto), functor(Gasto, Tipo, _).
consumo_superior(Persona, Tipo, Minimo) :-
    gasto(Persona, Gasto), functor(Gasto, Tipo, _), arg(_, Gasto, Monto), number(Monto), Monto > Minimo.
promedio_persona(Persona, Promedio) :-
    findall(Monto, (gasto(Persona, G), arg(_, G, Monto), number(Monto)), Montos), sum_list(Montos, Suma), length(Montos, Cantidad), Cantidad > 0, Promedio is Suma / Cantidad.
```

### Verificación

```{code-cell} prolog
?- persona_con_gasto(maria, super).
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

### Solución

```{code-cell} prolog
:tags: [hide-cell]

alta_libro(Nro, Titulo, Autor, Editorial, Precio) :-
    assertz(libro(Nro, Titulo, Autor, Editorial, Precio)).
baja_libro(Nro) :- retractall(libro(Nro, _, _, _, _)).
consulta_libro(Nro, Titulo, Autor, Editorial, Precio) :-
    libro(Nro, Titulo, Autor, Editorial, Precio).
promedio_autor(Autor, Promedio) :-
    findall(Precio, libro(_, _, Autor, _, Precio), Precios), sum_list(Precios, Suma), length(Precios, Cantidad), Cantidad > 0, Promedio is Suma / Cantidad.
```

### Verificación

```{code-cell} prolog
?- alta_libro(1, prolog, aquili, utn, 100).
```

```{code-cell} prolog
?- consulta_libro(1, Titulo, Autor, Editorial, Precio).
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

### Solución

```{code-cell} prolog
:tags: [hide-cell]

receta(1, ensalada, tomate, 2).
receta(1, ensalada, lechuga, 1).
receta(2, salsa, tomate, 5).
recetas_con_ingredientes(Codigo, Nombre, I1, I2) :-
    receta(Codigo, Nombre, I1, _), receta(Codigo, Nombre, I2, _), I1 \= I2.
recetas_con_cantidad(Codigo, Nombre, Ingrediente, Minimo) :-
    receta(Codigo, Nombre, Ingrediente, Cantidad), Cantidad > Minimo.
```

### Verificación

```{code-cell} prolog
?- recetas_con_ingredientes(Codigo, Nombre, tomate, lechuga).
```
