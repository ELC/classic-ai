---
title: Juegos de dos jugadores
---

# Juegos de dos jugadores

2.3.:1.. J111egos de dos jugadores

**Visión de conjunto**

Para mucha gente los juegos provocan una inexplicable fascinación, y la idea de
que las computadoras pudieran jugar ha existido al menos desde que existen las
computadoras. Charles Babbage, el famoso arquitecto de computadoras del siglo
XIX, pensó en programar su máquina analítica para que jugara al ajedrez, y más
tarde pensó en construir una máquina para jugar a las tres en raya (Bowden,
1953). Dos de los pioneros en las ciencias de la información y de la computación
contribuyeron a la incipiente literatura sobre juegos por computadora. Claude
Shannon (1950) escribió un articulo en el que se describían los mecanismos que
podían usarse en un programa que jugara al ajedrez. Pocos años después, Alan
Turing describió un programa para jugar al ajedrez, a pesar de que nuca lo
construyó. Al principio de los sesenta, Arthur Samuel tuvo éxito al construir el
primer programa de juegos importante y operativo. Su programa jugaba a las damas
y además de jugar, podía aprender de sus errores para mejorar su comportamiento
(Samuel, 1963).

Existian dos razones para que los juegos pareciesen un buen dominio de
exploración de la inteligencia de una máquina:

- Proporcionan una tarea estructurada en la que es muy fácil medir el éxito o el
  fracaso.

- Obviamente no necesitan grandes cantidades de conocimiento. Se pensó que se
  podrían resolver por búsqueda directa a partir del estado inicial hasta la
  posición ganadora.

La primera de estas razones aun sigue siendo valida y explica el continuado
interés en el área de los, juegos por computadora. Desafortunadamente, la
segunda no es cierta para aquellos juegos que no sean muy simples. Por ejemplo,
considere el juego del ajedrez.

- El factor de ramificación en una partida media es más o menos 35.

- En una partida media, cada jugador realiza 50 movimientos.

- Por tanto, para examinar el árbol del juego completamente, se tendrían que
  examinar 35100 posiciones.

Asi resulta evidente que un programa que realice una simple búsqueda exhaustiva
en el árbol del juego, no podrá seleccionar ni siquiera su primer movimiento
durante el tiempo de vida de su oponente. Es necesario algún tipo de
procedimiento de búsqueda heurística.

Una forma de contemplar todos los procedimientos de búsqueda que se han
explicado es que esencialmente se trata de ***procedimientos de generación y
prueba,*** en donde la comprobación se realiza después de cantidades distintas
de trabajo realizadas por el generador. En un extremo, *el generador proporciona
propuestas de soluciones completas,* que el comprobador evalúa. En el otro
extremo, *el generador genera movimientos individuates en el espacio de
búsqueda, cada uno de los cuales se evalúa a continuación mediante el
comprobador para pasar a elegir el más prometedor de ellos.* Mirandolo así,
resulta claro que para mejorar la efectividad de un programa resolutor de
problemas es necesario hacer dos cosas:

- ***Mejorar el procedimiento de generación*** de forma que solo se generen
  movimientos (o caminos) buenos.

- ***Mejorar el procedimiento de 'prueba*** para que solo se reconozcan y
  exploren en primer lugar los mejores movimientos (o caminos).

En los programas para jugar es particularmente importante que se hagan las dos
cosas. Si se usa un simple *generador de movimientos legales,* el procedimiento
de prueba (que probablemente,utiliza una combinación de búsqueda y una función
de evaluación heurística) deberá procesar cada uno de ellos. Como el
procedimiento de búsqueda debe tener en cuenta muchas posibilidades, debe ser
rápido. Por lo tanto, *probablemente no pueda realizar su trabajo con
precisión.* Suponga, por otra parte que en lugar de un generador de movimientos
legales, se usa un *generador de movimientos p/ausibles* en el que solo se
genera un *pequeño número de movimientos prometedores.* Conforme se incrementa
el número de movimientos legales posibles, la aplicación de técnicas heurísticas
para seleccionar solo aquellos que sean algo prometedores, se vuelve más
importante. Con un generador de movimientos más selective, *el procedimiento de
prueba puede permitirse el lujo de emplear más tiempo en la evaluación de cada
uno de los movimientos que* se *le proporcionan, por lo que puede producir un
resultado más fiable.* De este modo, con la incorporación de conocimiento
heurístico tanto en el generador como en el comprobador, se mejora el
rendimiento del sistema total.

Por supuesto, en los juegos, al igual que en otros dominios de problemas, la
búsqueda no es la única técnica disponible. En algunos juegos existen al menos
algunas ocasión)es.en.las que son apropiadas otras técnicas más directas. Por
ejemplo, en el ajedrez, tanto las aperturas como los finales están ampliamente
estudiados, por lo que es mejor jugar *consultando con una tabla de una base de
datos que almacene patrones.* ***Entonces para jugar una partida completa, deben
combinarse las técnicas orientadas a la búsqueda con las que no lo son.*** La
forma ideal de usar un procedimiento de búsqueda para encontrar una solución a
un problema, es generar mo/cimientos a través del espacio del problema hasta que
se encuentra un estado objetivo. En el contexto de programas de juegos, un
estado objetivo es aquel en el cuál ganamos. Desafortunadamente, para juegos
interesantes como el ajedrez, normalmente no es posible buscar hasta encontrar
un estado objetivo, ni siquiera disponiendo de un buen generador de movimientos
plausibles. La profundidad del árbol (o grafo) resultante y su factor de
ramificación son demasiado grandes.

Con la cantidad de tiempo disponible, solo es posible buscar menos de diez
movimientos en el árbol (llamados capas en la literatura de juegos). As\[ pues,
para elegir el mejor movimiento, deben compararse las posiciones del tablero
resultantes para determinar cuál es la más ventajosa. Esto se lleva a cabo con
una función de evaluación estática, que usa toda la información disponible para
evaluar posiciones individuales del tablero estimando la probabilidad de que
conduzcan eventualmente a la victoria. Su función es similar a la función
heurística h' en el algoritmo A\*: en ausencia de una información completa,
elige la posición más prometedora. Naturalmente, la función de evaluación
estática puede aplicarse simplemente a las posiciones generadas por los
movimientos propuestos. Pero, puesto que es difícil producir una función como
esta que sea realmente muy precisa, es mejor aplicarla tantos l niveles hacia
abajo en el árbol de juego como lo permita el tiempo disponible.
