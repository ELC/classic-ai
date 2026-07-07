---
title: Técnicas de búsqueda heurística
---

(tecnicas-de-busqueda-heuristica)=

# Técnicas de búsqueda heurística

Con el fin de resolver problemas complicados con eficiencia, con frecuencia es
necesario comprometer los requisitos de movilidad y sistematicidad, y construir
una estructura de control *que no garantice encontrar la mejor respuesta pero
que casi siempre encuentre una buena* *so/solución.* De esta forma, surge la
idea de **heurística.** *Una heurística* es *una técnica que* *aumenta la
eficiencia de un proceso de búsqueda, posiblemente sacrificando demandas de*
*completitud.* Las heurísticas son coma los guías de turismo: resultan adecuados
en el sentido de que generalmente suelen indicar las rutas interesantes; son
malos en el sentido de que pueden olvidar puntos de interés para ciertas
personas. Algunas heurísticas ayudan a guiar el proceso de búsqueda sin
sacrificar ninguna demanda de completitud que el proceso haya podido tener
previamente. Otras (en realidad, muchas de las mejores) pueden ocasionalmente
causar que una buena ruta sea pasada por alto. Pero, en promedio, mejoran la
calidad de las C rutas que exploran. Al usar buenas heurísticas se pueden
esperar buenas (aunque posiblemente no óptimas) soluciones para problemas
difíciles, tales como el del viajante de comercio, en un tiempo menor al
exponencial. Existen algunas heurísticas de propósito general que son adecuadas
para una amplia variedad de dominios de problemas. Ademas, es posible construir
heurísticas de propósito especial que exploten el conocimiento especifico del
dominio para resolver problemas particulares.

La heurística del vecino más próximo es un ejemplo de una buena heurística de
propósito general valida para varios problemas combinatorios. Consiste en
seleccionar en cada paso la alternativa localmente superior. Al aplicarla al
problema del viajante de comercio, surge el siguiente proceso:

1. Seleccionar arbitrariamente una ciudad de comienzo.

1. Para seleccionar la siguiente ciudad, fijarse en las ciudades que todavía no
   se han

visitado y seleccionar aquella que sea más cercana. Ir a esa ciudad.

1. Repetir el paso 2 hasta que todas las ciudades hayan sido visitadas. Cuando
   se aplican a problemas específicos, la eficacia de las técnicas de búsqueda
   heurísticas depende en gran medida de la forma en que exploten el
   conocimiento del dominio particular, ya que, por sí solas, no son capaces de
   salvar la explosión combinatoria a la que son tan

vulnerables los procesos de búsqueda. Por esta razón, a estas técnicas se las
denomina con frecuencia métodos débiles (weak methods). A pesar de que
comprender la limitada efectividad de estos métodos débiles para resolver
problemas difíciles ha sido un importante resultado surgido en las últimas tres
décadas de investigación en IA, estas técnicas proporcionan un marco donde
situar el conocimiento del dominio específico, ya sea manualmente o como
resultado de un aprendizaje automático. Es por ello que siguen formando el
núcleo de la mayoría de los sistemas de IA.

**Problema de la Mochila**

Consiste en elegir, de entre un conjunto **den** *elementos* de un negocio,
(cada uno con un valor ***V;,*** y un peso ***p;*** ), aquellos que puedan ser
cargados en la mochila de un individuo, que decide hacer una visita nocturna al
negocio. La mochila resiste un *peso máxima* ***Py*** se debe tener en cuenta
que el visitante pretende acumular *el mayor valor posible,* entre todos los
objetos que recoge.

Este es un claro ejemplo de la presentación de un problema, en el que hay
dificultad para hallar una solución óptima exacta, principalmente por el tiempo
que llevaría recorrer y combinar todas las posibilidades en forma exhaustiva.

- l • Para 20 elementos + se definen 220=1.048.580 subconjuntos o soluciones

* Para 60 elementos + se necesitan 365 siglos para resolver el problema, a 1
  millón de soluciones por segundo

Existen entonces, ***métodos heurísticos*** que proporcionan soluciones
factibles (que satisfacen las restricciones del problema), que aunque no
optimicen la función objetivo, se acercan al valor óptimo en un tiempo de
cálculo razonable.

Una clase de algoritmos heurísticos son los ***métodos constructivos,*** que
consisten en ir agregando componentes individuales a la solución hasta que se
obtiene una solución factible.

Un representante de estos son los ***algoritmos greedy*** (golosos o
devoradores). Estos algoritmos van construyendo paso a paso la solución,
buscando el máximo beneficio en cada paso.

En el problema de la mochila, debemos ir escogiendo los elementos que aporten el
mayor valor en proporción a su peso ***v;* / *p;*** *).* l:ejercicio«is

1. Desarrollar un algoritmo goloso que brinde una solución para el siguiente
   conjunto de datos:

| --- | --- | --- |

| 1 | 150 | 20 |

| 2 | 325 | 40 |

| 3 | 600 | 50 |

| 4 | 805 | 36 |

| 5 | 430 | 25 |

| 6 | 1200 | 64 |

| 7 | 770 | 54 |

| 8 | 60 | 18 |

| 9 | 930 | 46 |

| 10 | 353 | 28 |

Peso máxima soportado por la mochila:

![Ejercicio: mochila con algoritmo goloso](images/ejercicio-mochila-algoritmo-goloso.png)

42Q0 grs.

1. Dados 3 elementos, cuyos pesos son: 1800 grs., 600 grs. Y 1200 grs. y cuyos
   valores

son: $72, $36 y $60 respectivamente, y dado que la mochila puede soportar hasta
3000 grs. se pide:

- 1. Hallar una solución utilizando un algoritmo goloso.

2. Analizar dicha solución respecto a su grado de optimización y elaborar las

conclusiones que considere adecuadas.
