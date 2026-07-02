---
title: "Capitulo 1. Introducción"
---

# Unidad Didáctica 6 - Eje Conceptual

Programación practica en Prolog

Universidad Tecnológica Nacional

Facultad Regional Rosario

Ingeniería en Sistemas de Información

Docentes: Ing. Laura Aquili Ing. Pablo Pistilli

(sec-unit-06-prolog-indice)=

## Indice

- CAPITULO 1 - (p. 3)
- Introducción - (p. 3)
- CAPITULO 2 - (p. 5)
- Relación con la Lógica - (p. 5)
- 2.1 Hechos - (p. 5)
- 2.2 Variables - (p. 6)
- 2.3 Reglas - (p. 6)
- 2.4 Cláusulas - (p. 7)
- 2.5 Preguntas - (p. 7)
- 2.6 Predicados y Objetivos - (p. 7)
- 2.7 Secuencia de objetivos - (p. 8)
- 2.8 Backtracking - (p. 9)
- 2.9 Ejemplos - (p. 10)
- CAPITULO 3 - (p. 12)
- Manipulación de datos - (p. 12)
- 3.1 Tipos de dominios estándares - (p. 12)
- 3.2 Entrada y salida de datos - (p. 13)
- 3.3 Predicados predefinidos - (p. 13)
- 3.4 Evaluación de expresiones aritméticas - (p. 14)
- 3.5 Recursividad - (p. 15)
- CAPITULO 4 - (p. 16)
- Estructuras de datos - (p. 16)
- 4.1 Listas - (p. 16)
- 4.1.1 Identificación de la cabeza y la cola - (p. 16)
- 4.1.2 Recursividad en listas - (p. 17)
- 4.2 Cadenas - (p. 18)
- CAPITULO 5 - (p. 19)
- Base de datos y Functores - (p. 19)
- 4.1 Base de datos - (p. 19)
- 4.2 Functores - (p. 22)

(sec-unit-06-prolog-capitulo-1-introduccion)=

## Capitulo 1. Introducción

Prolog es un lenguaje de programación que se utiliza para resolver problemas en
los que entran en juego objetos y relaciones entre objetos. Actualmente se ha
convertido en el principal entorno de programación para Inteligencia Artificial
(IA), una de las principales áreas de aplicación de las computadoras que está
emergiendo. También se puede hacer virtualmente cualquier cosa en Prolog como
podría hacerlo con cualquier otro lenguaje de programación, incluyendo juegos,
contabilidad, gráficos y simulación. PROLOG no es siempre el lenguaje más
práctico o eficiente para algunas aplicaciones, pero pueden igualmente
realizarse con él. Para los programadores que investigan IA, el Prolog ofrece un
método diferente de trabajo al empleado por los lenguajes más familiares, tales
como Basic, Cobol, Pascal y C.

### 1.1 Una breve historia del Prolog

Prolog significa “PRProgramming LOGic”, es decir programación basada en la
lógica y es un lenguaje de programación de computadoras que fue inventado
alrededor de 1970 por Alain Colmenauer y sus colegas de la Universidad de
Marsella, Francia. Rápidamente el Prolog se convirtió en el lenguaje principal
para IA en Europa, mientras que Lisp (otro lenguaje de programación para IA) se
usaba principalmente por los programadores de los Estados Unidos. A finales de
los años ’70 comenzaron a aparecer versiones de Prolog para microcomputadoras.
Uno de los compiladores de Prolog más populares fue el MicroProlog, pero éste no
ofrece la misma riqueza de predicados. No existió mucho interés por el Prolog
hasta que los científicos japoneses lanzaron su famoso proyecto de la quinta
generación con el objetivo de diseñar nuevas computadoras y software. De
repente, la gente comenzó a mirar de otra forma el Prolog y sus posibilidades.

### 1.2 ¿Para qué sirve Prolog?

Los lenguajes de computadoras son raramente buenos para todos los tipos de
problemas. Fortran fue usado principalmente por los científicos y matemáticos,
mientras que Cobol fue usado principalmente en el mundo comercial. A las
implementaciones del Prolog les falta la habilidad para manejar problemas sobre
“números” o “procesamiento de texto”; en su lugar, Prolog está diseñado para
manejar “problemas lógicos” ( es decir, problemas en los que se necesitan tomar
decisiones en forma ordenada). Intenta hacer que la computadora “razone” la
forma de encontrar una solución. Es particularmente adecuado para diferentes
tipos de problemas de inteligencia artificial.

### 1.3 Lenguaje Procedural vs. Lenguaje Declarativo

La mayoría de los lenguajes de computadoras personales –Basic, Pascal, Cobol,
etc- han sido procedurales. Tales lenguajes permiten al programador decirle a la
computadora lo que tiene que hacer, paso a paso, procedimiento por
procedimiento, hasta alcanzar una conclusión. El Prolog no es procedural, es
declarativo, necesita que se declaren reglas y hechos sobre símbolos específicos
y luego se le pregunte sobre si un objetivo concreto se deduce lógicamente a
partir de los mismos. Mientras que un lenguaje procedural le exige que
introduzca el recipiente y los ingredientes, un lenguaje declarativo sólo le
pide les ingredientes y el objetivo. Se declara la situación con la que se
quiere trabajar y donde quiere ir, el propio lenguaje realiza el trabajo de
decidir cómo alcanzar dicho objetivo. La diferencia entre lenguaje declarativo y
procedural es una de las razones por la que la implementación de un lenguaje
como Prolog es una herramienta tan buena para desarrollar aplicaciones con IA,
especialmente cuando se lo compara con otros lenguajes. Al trabajar con un
lenguaje declarativo se da información sobre un determinado tema, se definen las
relaciones que existen entre estos datos y finalmente se construyen preguntas o
cuestionamientos sobre

todo el paquete, quedándole al lenguaje la tarea de elaborar las conclusiones
mediante un razonamiento lógico.

### 1.4 Inteligencia Artificial (IA): Visión General

Determinar qué es un programa inteligente implica que se conoce lo que significa
inteligencia: capacidad o habilidad para percibir hechos y proposiciones y sus
relaciones y razonar sobre ellos. Esencialmente significa pensar. Esta
definición implica solamente inteligencia humana, no admite la posibilidad de
que una máquina pueda pensar, ya que los programas no hacen la misma tarea de la
misma forma que una persona. Que un programa sea inteligente requiere que actúe
inteligentemente, como un ser humano. Un programa inteligente exhibe un
comportamiento similar al de un humano cuando se enfrenta a un problema similar.
No es necesario que el programa resuelva concretamente o intente resolver el
problema igual que un humano. Obsérvese que el programa no necesita pensar como
un humano, pero debe actuar como tal. Es difícil establecer una fecha de
comienzo para lo que es comúnmente llamado IA. El primer paso se le atribuye a
Alan M. Turing por su invención de la computadora de programas almacenados.
Determinó que un programa podía ser almacenado como dato en la memoria de la
computadora y ejecutarlo más tarde. Anteriormente las computadoras fueron
máquinas dedicadas que debían ser recableadas para diferentes problemas. El
almacenamiento de programas permitía entonces cambiar la función de la
computadora fácil y rápidamente. El término inteligencia artificial se imputa a
Marvin Minsky, investigador del MIT (Massachusetts Institute of Technology)
quien escribió un articulo titulado “Pasos de la Inteligencia Artificial” (enero
1961), que explicaba la posibilidad de hacer pensar a las computadoras. Al final
de los años ’70 se habían alcanzado varios éxitos, tales como el procesamiento
de lenguaje natural, representación del conocimiento y resolución de problemas
en áreas específicas de la IA. Los dos problemas más significativos de IA son
los sistemas expertos y el procesamiento de lenguaje natural. A saber:

#### 1.4.1 Sistema Experto

Es un programa de computadora que contiene conocimientos acerca de un
determinado campo y cuando es interrogado responde como un experto humano.
Contiene información (una base de conocimientos) y una herramienta para
comprender las preguntas y responder la respuesta correcta examinando la base
(esto es, motor de inferencia). El Prolog tiene incorporado estructuras para la
creación de bases de conocimientos y un motor de inferencia.

#### 1.4.2 Procesamiento de Lenguaje Natural

El Procesamiento de lenguaje natural es la técnica que fuerza a las computadoras
a entender el lenguaje humano. Los científicos que estudian el Procesamiento de
lenguaje natural esperan crear un hardware y software que permita escribir por
ejemplo: “llevar el archivo del swi-prolog al directorio del Prolog” y haga que
la computadora siga dichas directrices. El Prolog puede usar la idea de una base
de conocimientos y un motor de inferencias para dividir el lenguaje humano en
diferentes partes y relaciones y así intentar comprender su significado
detectando palabras claves.

#### 1.4.3 Áreas más importantes de la Inteligencia Artificial

El campo de la IA se compone de varias áreas de estudio:

- Búsqueda (de soluciones).
- Sistemas expertos.
- Procesamiento del lenguaje natural.
- Robótica
- Lógica.

(sec-unit-06-prolog-capitulo-2-relacion-con-la-logica)=
