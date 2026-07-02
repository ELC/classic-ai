---
title: Problemas con consecuencia cierta e incierta
---

(sec-unit-01-introduccion-problemas-con-consecuencia-cierta-e-incierta)=

## Problemas con consecuencia cierta e incierta

,Es predecible el universo?

Suponga nuevamente que estamos jugando al 8-puzzle. Cada vez que se hace un
movimiento, se sabe exactamente que ocurrirá. Esto significa que es posible
planificar una secuencia entera de movimientos y estar seguros de que se conoce
cuál sera el resultado. Es posible utilizar una planificación para evitar tener
que deshacer movimientos, si bien todavía se deben hacer comprobaciones de
movimientos en tiempo de planificación. De esta forma, es necesaria una
estructura de control que permita la comprobación.

Sin embargo, en otros juegos diferentes al 8-puzzle, no es posible un proceso de
planificación. Suponga que queremos jugar al bridge. Una de las decisiones que
hay que tomar es que carta jugar en la primera baza. Sería deseable planificar
la mano completa antes de realizar esta primera jugada. Pero ahora no es posible
hacer tal planificación con certeza debido a que no se sabe con exactitud donde
están las cartas y que harán los otros jugadores en sus turnos. Lo mejor que se
puede hacer es investigar distintos planes y utilizar las probabilidades de las
consecuencias que se derivan de su elección para resaltar el que tenga la más
alta probabilidad estimada de llegar a una buena puntuación en el juego.

Las dos últimas características explicadas, ignorable versus recuperable y
consecuencia-cierta versus consecuencia-incierta, interactúan de una forma
interesante. Tai y como se ha mencionado siempre, una forma de resolver los
problemas irrecuperables es planificando una solución completa antes de
embarcarse. en la implementación del plan. Sin embargo, este proceso de
planificación solo es útil en los problemas de consecuencia-cierta. Asf, uno de
los tipos de problemas más difíciles de resolver son los irrecuperables de
consecuencia-incierta. Ejemplos de tales problemas son los siguientes:

Bridge. Sin embargo, puede mejorarse un poco ya que existen estimaciones exactas
de las probabilidades de cada una de las posibles consecuencias.

Control de un brazo de robot. La consecuencia es incierta debido a varias
razones. Alguien podría poner algo en la ruta del brazo; los mecanismos del
brazo podrían atascarse; un *leve C* error podría causar que el brazo choque con
una pila de objetos.

Ayudar a un abogado a decidir cómo defender a su cliente contra un cargo de
asesinato. En este caso no se puede dar probablemente una lista de posibles
consecuencias, y mucho menos dar sus probabilidades.
