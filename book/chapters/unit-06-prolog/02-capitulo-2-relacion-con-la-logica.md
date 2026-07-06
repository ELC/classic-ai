---
title: Relación con la lógica
---

# Relación con la lógica

Como su nombre lo indica, el Prolog se basa en manipulaciones lógicas;
posibilita al programador especificar sus problemas en forma lógica, en lugar de
en términos de construcciones convencionales de programación sobre lo que debe
hacer la computadora y en qué momento. Si queremos analizar cómo se relaciona
Prolog con la lógica debemos establecer primero que es lo que significa lógica:
la lógica se desarrolló, originalmente, como una forma de representar argumentos
de manera que fuera posible comprobar si estos eran válidos o no. Se puede
utilizarla lógica para expresar objetos, relaciones entre objetos y cómo pueden
inferirse en forma válida algunos objetos a partir de otros. Por ejemplo, cuando
decimos “Eduardo tiene una PC” estamos expresando una relación entre el objeto
“Eduardo” y otro “una PC”; además la relación tiene un orden específico: ¡es
Eduardo quien tiene una PC y no una PC quien tiene a Eduardo! Cuando realizamos
la pregunta ¿Tiene Eduardo una PC? lo que estamos haciendo es indagar sobre una
relación. Prolog trabaja con lógica proposicional, también conocida como lógica
de predicados o cálculo proposicional. Prolog hace que la computadora maneje la
parte de inferir. Tiene un motor de inferencia incorporado que automáticamente
busca los hechos y construye conclusiones lógicas. La programación de
computadoras en Prolog consiste en:

- Declarar algunos hechos sobre los objetos y sus relaciones,
- Definir algunas reglas sobre los objetos y sus relaciones, y
- Hacer preguntas sobre los objetos y sus relaciones.

Podemos considerar a Prolog como un almacén de hechos y reglas, que utiliza a
éstos para responder las preguntas, proporciona los medios para realizar
inferencias de un hecho a otro. Se puede considerar a Prolog como un lenguaje
coloquial, lo cual significa que el programador y la computadora sostienen una
especie de conversación.

## Hechos

La primera forma de combinar un objeto y una relación es usarlas para definir un
hecho, la sintaxis de Prolog es:

Relación (objeto).

Supongamos que queremos decir a Prolog el hecho de que “a Eduardo le gusta la
PC”, en Prolog debemos escribir:

le_gusta_a(Eduardo,pc).

Observe que el objeto está entre paréntesis y la relación le precede, lo que
quiere decir que este objeto tiene esa relación. La relación se conoce como el
predicado y el objeto como el argumento.

Los siguientes puntos son importantes:

- Los nombres de todos los objetos y relaciones deben comenzar con letra
  minúscula.
- Primero se escribe la relación y luego los objetos separándolos mediante comas
  y encerrados entre paréntesis.
- Al final del hecho debe ir un punto (el carácter “.”).
- El carácter “\_” en el nombre del predicado indica que todo es una única
  palabra para una relación.
- Dos hechos coinciden si sus predicados son lo mismo (se escriben de igual
  forma) y si cada uno de los correspondientes argumentos son iguales entre sí.

## Variables

En Prolog no sólo se pueden nombrar determinados objetos, sino que también se
pueden utilizar nombres como X que representen objetos a los que el mismo Prolog
les dará ese valor, este tipo de nombres es o que se llama variables. Cuando el
lenguaje Prolog utilicé una determinada variable esta puede estar Instanciada o
no instanciada. El primer caso se da cuando existe un objeto determinado,
representando por la variable, en caso contrario, una variable no está
instanciada cuando, todavía no se conoce lo que representa.

Las variables deben comenzar con letra mayúscula.

Cuando se intenta establecer una relación que contenga una variable, Prolog
efectuará una búsqueda recorriendo todos los hechos que él tiene almacenados
para encontrar un objeto que pueda ser representado por la variable. Por
ejemplo, cuando preguntamos ¿le gusta X a Eduardo?, Prolog buscará entre todos
sus hechos para encontrar cosas que le gusten a Eduardo.

Una variable X no nombra un objeto en particular sino que se puede utilizar para
representar objetos que no podamos nombrar. Por ejemplo, no podemos nombrar un
objeto como algo que le gusta a Eduardo, de forma que Prolog adopta una forma de
expresar esto.

En vez de preguntar le_gusta_a(eduardo, Algo que le gusta a eduardo).

podemos utilizar le_gusta_a(eduardo, X).

Observación: Las variables pueden tener nombres más largos. Por ejemplo: Algo
que le gusta a eduardo.

A veces es necesario utilizar una variable aunque su nombre no se utilice nunca,
supongamos que queremos averiguar si a alguien le gusta Eduardo, pero no estamos
interesados en saber quien, entonces utilizamos la variable anónima. Esta
variable es un único carácter de subrayado.

le_gusta_a(\_,eduardo).

Se utiliza para evitar el tener que imaginar continuamente diferentes nombres de
variables cuando no se van a utilizar en ningún otro sitio de la cláusula.

## Reglas

En Prolog se usa una regla cuando se quiere significar que un hecho depende de
otros hechos. Por ejemplo, si queremos afirmar que a Eduardo le gustan todas las
pc’s del mercado, habría que escribir hechos por separado, así:

le_gusta_a(eduardo, ibm). le_gusta_a(eduardo, compaq). le_gusta_a(eduardo,
hacer). le_gusta_a(eduardo, falcon). ....

Así sucesivamente para cada una de las pc’s que tengamos.

En Prolog una regla consiste una cabeza y un cuerpo. Estas partes se encuentran
separadas mediante el símbolo “:-”; que está compuesto de un signo de dos puntos
y de un guión. Este símbolo es equivalente a “si”.

La cabeza describe qué hecho es el que la regla intenta definir, mientras que el
cuerpo describe la conjunción de objetivos que deben satisfacerse, uno tras
otro, para que la cabeza sea cierta.

es(compaq, pc). es(falcon, pc).

.... le_gusta_a(eduardo, objeto):-es(objeto, pc).

Una forma más simple de decir que a Eduardo le gustan todas las pc es decir que
a Eduardo le gusta cualquier objeto siempre que sea una pc. Este hecho se da en
forma de una regla sobre lo que le gusta a Eduardo, en vez de dar la relación de
todas las pc que le gustan a Eduardo.

La regla es mucho más compacta que una lista de hechos. Las reglas hacen que el
Prolog pase de ser sólo un diccionario o una base de datos, en el que se pueda
buscar, a ser una máquina lógica, pensante.

Ejemplo de reglas:

- Marco compra vino si es más barato que la cerveza.
- X es un pájaro si: X es un animal y X tiene plumas.

Una regla es una afirmación general sobre objetos y sus relaciones. Así podemos
permitir que una variable represente un objeto diferente en casa uso distinto de
la regla. Por ejemplo:

a Marco le gusta cualquiera a la que le guste el vino, o en otras palabras, a
Marco le gusta algo si a esto le gusta el vino, con variable, a Marco le gusta X
si a X le gusta el vino.

El ejemplo anterior se escribe en Prolog de la siguiente forma:

le_gusta_a(marco, X):- le_gusta_a(X, vino).

## Cláusulas

Utilizaremos la palabra cláusula siempre que nos refiramos a un hecho o a una
regla. Existen dos formas de dar información a Prolog sobre un predicado dado,
como le_gusta_a. Podemos darle tanto hechos como reglas. En general, un
predicado está definido por una mezcla de hechos y reglas. A uno y otras se las
denomina como cláusulas de un predicado. Por ejemplo consideremos la regla:

Una persona puede robar una cosa si la persona es un ladrón y le gusta la cosa y
la cosa es valiosa.

En Prolog sería: puede_robar(X,Y):- ladrón(X), le_gusta_a(X,Y), valiosa(Y).

El predicado puede_robar significa que alguna persona X puede robar alguna cosa
Y. Esta cláusula depende de las cláusulas le_gusta_a y valiosa.

## Preguntas

Una vez que tengamos algunos hechos podemos hacer alguna pregunta acerca de
ellos. En Prolog una pregunta se representa igual que un hecho Cuando se hace
una pregunta Prolog efectúa una búsqueda por toda la base de datos, localizando
hechos que coincidan con el hecho en cuestión. Si se encuentra uno que coincida
se responderá sí (Yes/True), por el contrario si no se encuentra, la respuesta
será no (No/False).

## Predicados y Objetivos

Los predicados son las relaciones, los elementos ejecutables en Prolog. Una
llamada concreta a un predicado, con unos argumentos concretos, se denomina
objetivo (en inglés, goal). Todos los objetivos tienen un resultado de éxito o
fallo tras su ejecución, indicando si el predicado es cierto para los argumentos
dados, o por el contrario, es falso. Cuando un objetivo tiene éxito las
variables libres que aparecen en los argumentos pueden quedar instanciadas.
Estos son los valores que hacen cierto el predicado. Si el predicado falla, no
ocurren ligaduras en las variables libres.

Ejemplo El caso básico es aquél que no contiene variables:
son_hermanos('Juan','Maria'). Este objetivo solamente puede tener una solución
(verdadero o falso). Si utilizamos una variable libre: son_hermanos('Juan',X),
es posible que existan varios valores para dicha variable que hacen cierto el
objetivo. Por ejemplo para X ='Maria', y para X ='Luis'. También es posible
tener varias variables libres: son_hermanos(Y,Z). En este caso obtenemos todas
las combinaciones para las variables que hacen cierto el objetivo. Por ejemplo,
Y ='Juan' y Z ='Maria' es una solución. Y ='Juan' y Z ='Luis' es otra solución.

## Secuencia de objetivos

Hasta ahora hemos visto como ejecutar objetivos simples, pero esto no resulta
demasiado útil. En Prolog los objetivos se pueden combinar mediante conectivas
propias de la lógica de primer orden: la conjunción, la disyunción y la
negación. La conjunción es la manera habitual de ejecutar secuencias de
objetivos que Prolog deberá satisfacer uno después del otro. El operador de
conjunción es la coma (and). Por ejemplo: edad(luis,Y),edad(juan,Z),Y>Z.
Analicemos qué ocurre con la instanciación de las variables:

- En primer lugar, los objetivos se ejecutan secuencialmente por orden de
  escritura (es decir, de izquierda a derecha).
- Si un objetivo falla, los siguientes objetivos ya no se ejecutan. Además, la
  conjunción en total falla.
- Si un objetivo tiene éxito, algunas o todas sus variables quedan ligadas, y
  por ende, dejan de ser variables libres para el resto de objetivos en la
  secuencia.
- Si todos los objetivos tienen éxito, la conjunción tiene éxito y mantiene las
  ligaduras de los objetivos que la componen.

Supongamos que la edad de Luis es 32 años, y la edad de Juan es 25:

- La ejecución del primer objetivo tiene éxito e instancia la variable "Y", que
  antes estaba libre, al valor 32.
- Llega el momento de ejecutar el segundo objetivo. Su variable "Z" también
  estaba libre, pero el objetivo tiene éxito e instancia dicha variable al valor
  25\.
- Se ejecuta el tercer objetivo, pero sus variables ya no están libres porque
  fueron instanciadas en los objetivos anteriores. Como el valor de "Y" es mayor
  que el de "Z" la comparación tiene éxito.
- Como todos los objetivos han tenido éxito, la conjunción tiene éxito, y deja
  las variables "Y" y "Z" instanciadas a los valores 32 y 25 respectivamente.

El operador de disyunción (or) es el punto y coma. Tendrá éxito si se cumple
alguno de los objetivos que la componen. La disyunción lógica también se puede
representar mediante un conjunto de sentencias alternativas, es decir, poniendo
cada miembro de la disyunción en una cláusula aparte. Esta última será la forma
en la que trabajaremos en el desarrollo de nuestros programas en Prolog.

El operador de negación es not. El predicado not/1 antes de la llamada a un
predicado P, cambia su valor de verdad, es decir, si el predicado P tiene éxito
, not(P) fallará y si el predicado P falla, not(P) tendrá éxito. Ejemplo:
observa(juan,brenda). observa(marco,felicia). observa(federico,felicia).

feliz(X):- not(observa(X,felicia)).

- La regla feliz(X):- not(observa(X, felicia)) indica que alguien puede ser
  feliz sólo si no está observando a felicia.
- Si invocamos el objetivo feliz(marco), obtendremos la respuesta “No”.
- En otras palabras, la parte izquierda de la regla, “feliz(marco)”, es solo
  verdad si la parte derecha, “observa(marco, felicia)”, no es verdad. Pero la
  parte derecha es verdad. Un hecho muestra que es verdad.
- Por lo tanto, la parte derecha de la regla fallará como objetivo temporal;
  luego la parte izquierda fallará como posible cumplimiento del objetivo
  original y finalmente el Prolog nos informará que el objetivo original falla o
  no se cumple.

## Backtracking

El mecanismo empleado por PROLOG para satisfacer las cuestiones que se le
plantean, es el de razonamiento hacia atrás (backward) complementado con la
búsqueda en profundidad (depth first) y la vuelta atrás o reevaluación
(backtracking). Razonamiento hacia atrás significa que partiendo de un objetivo
a probar, busca las aserciones que pueden probar el objetivo. Si en un punto
caben varios caminos, se recorren en el orden que aparecen en el programa, esto
es, de arriba a abajo y de izquierda a derecha. Backtracking: Si en un momento
dado una variable se instancia con determinado valor con el fin de alcanzar una
solución, y se llega a un camino no satisfactorio, el mecanismo de control
retrocede al punto en el cual se instanció la variable, la des-instancia y si es
posible, busca otra instanciación que supondrá un nuevo camino de búsqueda. Se
puede ver esta estrategia sobre un ejemplo: Supongamos la pregunta:
?-puede_casarse_con(maría, X). PROLOG recorre la base de datos en busca de un
hecho que coincida con la cuestión planteada y halla la regla:
puede_casarse_con(X, Y) :- quiere_a(X, Y), hombre(X), mujer(Y). produciéndose
una coincidencia con la cabeza de la misma, y una instanciación de la variable X
de la regla con el objeto 'maría'. Tendremos por lo tanto: (1)
puede_casarse_con(maría, Y) :- quiere_a(maría, Y), hombre(maría), mujer(Y).

A continuación, se busca una instanciación de la variable Y que haga cierta la
regla, es decir, que verifique los hechos del cuerpo de la misma. La nueva meta
será : (2) quiere_a(maría, Y).

De nuevo PROLOG recorre la base de datos. En este caso encuentra un hecho que
coincide con el objetivo: quiere_a(maría, enrique).

instanciando la variable Y con el objeto 'enrique'. Siguiendo el orden dado por
la regla (1), quedan por probar dos hechos una vez instanciada la variable Y:
hombre(maría), mujer(enrique). Se recorre de nuevo la base de datos, no hallando
en este caso ninguna coincidencia con el hecho hombre(maría). Por lo tanto,
PROLOG recurre a la vuelta atrás, des-instanciando el valor de la variable Y, y

retrocediendo con el fin de encontrar una nueva instanciación de la misma que
verifique el hecho (2). Un nuevo recorrido de la base de hechos da como
resultado la coincidencia con: quiere_a(maría, susana). Se repite el proceso
anterior. La variable Y se instancia con el objeto 'susana' y se intentan probar
los hechos restantes: hombre(maría), mujer(susana).

De nuevo se produce un fallo que provoca la des-instanciación de la variable Y,
así como una vuelta atrás en busca de nuevos hechos que coincidan con (2). Una
nueva reevaluación da como resultado la instanciación de Y con el objeto 'ana'
(la ultima posible), y un nuevo fallo en el hecho: hombre(maría).

Una vez comprobadas sin éxito todas las posibles instanciaciones del hecho (2),
PROLOG da por imposible la regla (1), se produce de nuevo la vuelta atrás y una
nueva búsqueda en la base de datos que tiene como resultado la coincidencia con
la regla: (3) puede_casarse_con(maría, Y) :- quiere_a(maría, Y), mujer(maría),
hombre(Y).

Se repite todo el proceso anterior, buscando nuevas instanciaciones de la
variable Y que verifiquen el cuerpo de la regla. La primera coincidencia
corresponde al hecho quiere_a(maría, enrique). que provoca la instanciación de
la variable Y con el objeto 'enrique'. PROLOG tratar de probar ahora el resto
del cuerpo de la regla con las instanciaciones actuales: mujer(maría),
hombre(enrique).

Un recorrido de la base de datos, da un resultado positivo en ambos hechos,
quedando probado en su totalidad el cuerpo de la regla (3) y por lo tanto su
cabeza, que no es más que una de las soluciones al objetivo inicial. X = enrique

PROLOG utiliza un mecanismo de búsqueda independiente de la base de datos.
Aunque pueda parecer algo ilógico, es una buena estrategia puesto que garantiza
el proceso de todas las posibilidades. Es útil para el programador conocer dicho
mecanismo a la hora de depurar y optimizar los programas.

## Ejemplos

Supongamos entonces la siguiente base de conocimientos:

edad(juan,25). edad(franco,10). edad(luis,32). edad(renzo,38). edad(marco,7).

1. Veamos un predicado compuesto por una simple cláusula:

es_menor(Individuo):- edad(Individuo,Valor),Valor < 18.

- Invocamos el objetivo: es_menor(luis).
- Según nuestra base de conocimiento, la edad de luis es 32 años, es decir, el
  objetivo edad(luis,32) tiene éxito.
- Primero se unifica la cabeza de la cláusula con el objetivo. Es decir,
  unificamos es_menor(luis) y es_menor(Individuo), produciéndose la ligadura de
  la variable Individuo al valor luis. Como el ámbito de visibilidad de la
  variable es su cláusula, la ligadura también afecta al cuerpo, luego estamos
  ejecutando realmente: es_menor(luis):- edad(luis,Valor),Valor < 18.
- Ahora ejecutamos el cuerpo, que instancia la variable Valor a 32. Pero el
  cuerpo falla porque el segundo objetivo falla (32 < 18 es falso). Entonces la
  cláusula falla y se produce backtracking.
- Como no hay más puntos de elección el objetivo falla. Es decir, luis no es
  menor de edad.

2. Ahora veamos como las instanciaciones que se producen en el cuerpo de la
   cláusula afectan también a la cabeza. Consideramos el siguiente predicado
   compuesto de una única cláusula:

mayor_que(A,B):- edad(A,EdadA),edad(B,EdadB),EdadA >EdadB.

- Ejecutamos el objetivo: mayor_que(luis,Quien)
- Unificamos el objetivo con la cabeza de la regla: la variable A se instancia a
  luis, la variable B permanece unificada con la variable Quien.
- Ejecutamos el cuerpo, que tiene éxito e instancia las variables EdadA a 32, B
  a juan y EdadB a 25.
- Como la variable B ha quedado instanciada y además unificaba con Quien, la
  variable Quien queda instanciada a ese mismo valor.
- El tercer objetivo también tiene éxito (32 > 25 es verdadero), por ende la
  cláusula entera tiene éxito.
- El objetivo tiene éxito unificando la variable Quien al valor juan. Es decir,
  luis es mayor que juan.

3. Programa que incluye una regla por la cual se define el concepto de
   “hermana”. hombre(omar). /*omar es un hombre*/ hombre(damian). mujer(maria).
   /*maria es una mujer*/ mujer(gabriela). padres(gabriela,maria,omar). /*los
   padres de gabriela son maria y omar*/ padres(damian,maria,omar).
   hermana(X,Y):-mujer(X),padres(X,M,P), padres(Y,M,P),X=Y.

- El objetivo hermana(gabriela, damian) determina si gabriela es hermana de
  damian.
- La primer conjunción mujer(X), buscará una mujer con el nombre gabriela.
- La segunda, padres(X,M,P), devolverá los padres de gabriela si la conjunción
  anterior fue verdadera. En este caso será M=maria y P=omar.
- La siguiente buscará si existe una cláusula padres(Y,M,P) con valores
  Y=damian, M=maria y P=omar. Esto evaluará si los padres de gabriela son los
  mismos que los de damian.
- Finalmente se evalúa si las personas X e Y no son la misma.

Recordar que cada vez que se evalúa una conjunción la/s anterior/es tuvieron que
ser verdadera/s, en caso contrario no se evaluarán la/s siguiente/s
conjunción/es.
