---
title: Escalada o remonte de colinas
---

(sec-unit-02-busqueda-y-planificacion-escalada-o-remonte-de-colinas)=

## Escalada o remonte de colinas

1. Escalada o Remonte de colinas

**Escalada**

El método de la escalada es una variante del de generación y prueba; en· el
existe realimentación a partir del procedimiento de prueba que se usa para
ayudar al generador a decidirse por cuál dirección debe moverse en el espacio de
búsqueda. En un procedimiento de generación y prueba puro, la función de prueba
responde solo un sí o un no. Pero si la función de prueba se amplía mediante una
función heurística que proporcione una estimación de. lo cercano que se
encuentra un estado.al estado objetivo, el procedimiento de generación puede
usar esta información tal y como se muestra en un ejemplo posterior. Ademas esto
es particularmente apropiado porque normalmente el cálculo de la función
heurística puede hacerse, casi sin coste alguno, al mismo tiempo en que se esta
llevando a cabo la verificación de una solución. La escalada se utiliza
frecuentemente cuando se dispone de una buena función heurística para evaluar
los estados, pero cuando no se dispone de otro tipo de conocimiento provechoso.

Ejercicio

Suponga que se encuentra en una ciudad desconocida sin ningún mapa, y que quiere
llegar al centro. Usted simplemente iría hacia los rascacielos. La función
heurística sería en este caso la distancia existente entre su posición y los
rascacielos y los estados deseables son aquellos en que esa distancia se
minimiza.

| | | | | | | |

| --- | --- | --- | --- | --- | --- | --- |

| | | | | | | |

| | | | |. | (:\_:; | |

| | | | | | | |

| | | | | | | |

| | | | | | | |

| | | | | | | |

| | | | | | | |

Desde una posición al objetivo, avanzar de a un paso y valorar. Si no es mejor,

![Ejemplo: escalada en grilla hacia el objetivo](images/ejemplo-escalada-grilla-objetivo.png)
volver atrás y buscar otro.

**Escalada simple**

La forma más sencilla de implementar el método de la escalada es la siguiente:

**Algoritmo: Escalada simple**

- 1. Evaluar el estado inicial. Si también es el estado objetivo, devolverlo y
     terminar. En

caso contrario, continuar con el estado inicial como estado actual.

- 1. Repetir hasta que se encuentre una solución o hasta que no queden nuevos
     operadores

que aplicar al estado actual:

- - 1. Seleccionar un operador que no haya sido aplicado con anterioridad al
       estado

actual y aplicarlo para generar un nuevo estado.

- - 1. Evaluar el nuevo estado.

Si es un estado objetivo, devolverlo y terminar.

Si no es un estado objetivo, pero es mejor que el estado actual,

convertirlo en el estado actual.

Si no es mejor que el estado actual, continuar con el bucle.

La principal diferencia que existe entre este algoritmo y el que se ha dado para
la técnica de generación y prueba, consiste en *el uso de una función de
evaluación coma una forma de* *introducir conocimiento especifico de la tarea
realizada en el proceso de control.* La utilización de este conocimiento es lo
que hace a este y a otros métodos que se explican a lo largo de este capítulo,
métodos de búsqueda heurística, y es este mismo conocimiento lo que da a estos
métodos la capacidad de resolver algunos problemas que de otra forma serían
inabordables.

Nótese que en este algoritmo se ha formulado la relativamente vaga pregunta,
*"i.Es un estado* *mejor que otro?".* Para que el algoritmo pueda funcionar, es
necesario proporcionar una definición precisa del término mejor. En algunos
casos, significa un valor más alto de una función heurística; en otros,
significa un valor más bajo. No importa lo que signifique siempre que a lo largo
de una escalada específica se sea consistente con su interpretación.

**Escala.da por la máxima pendiente**

Una variación útil del método de escalada simple consiste en considerar todos
las posibles movimientos a partir del estado actual y elegir el mejor de el.las
coma nuevo estado. Este método se denomina *método de escalada por la máxima
pendiente (steepest-ascent hill* *climbing) o búsqueda def gradiente (gradient
search).* Nótese el contraste con el método básico, en el que el primer estado
que parezca que sea mejor que el actual se selecciona coma el estado actual. El
algoritmo funciona así.

**Algoritmo: Escalada por la máxima pendiente**

1. Evaluar el estado inicial. Si también es el estado objetivo, devolverlo y
   terminar. En

caso contrario, continuar con el estado inicial coma estado actual.

1. Repetir hasta que se encuentre una solución o hasta que una iteración
   completa no

produzca un cambio en el estado actual:

- 1. Sea SUCC un estado tal que algún posible sucesor del estado actual sea
     mejor

que este SUCC.

- 1. Para cada operador aplicado al estado actual hacer lo siguiente:

1. Aplicar el operador y generar un nuevo estado.

1. Evaluar el nuevo estado. Si es un estado objetivo, devolverlo y terminar.

Si no, compararlo con SUCC. Si es mejor, asignar a SUCC este nuevo

estado. Si no es mejor, dejar succ coma esta.

- 1. Si SUCC es mejor que el estado actual, hacer que el estado actual sea SUCC.

Ejercicio

Resolver el ejercicio anterior utilizando una estrategia de Escalada por la
máxima pendiente, o sea, considerando todos los posibles movimientos a partir
del estado actual y elegir el mejor de ellos como nuevo estado.
