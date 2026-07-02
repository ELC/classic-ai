---
title: "Capitulo 3. Manipulación de datos"
---

## Capitulo 3. Manipulación de datos

### 3.1 Tipos de dominios estándares

La jerarquía de los términos en Prolog es:

![Jerarquía de los términos en Prolog](images/jerarquia-terminos-prolog.png)

Átomos

Los términos átomos son aquellos que se corresponden con las constantes del
vocabulario. Se comprueban que están bien definidos mediando el predicado
atom/1. Existen dos formas de definir constantes. La primera es escribiendo el
nombre de la constante con la primera letra en minúsculas. Ejemplo: ?- atom(a).
Yes ?- atom(fEdErIcO). Yes La segunda forma es más flexible. Si buscamos que
nuestra constante contenga espacios, caracteres raros o la primera letra en
mayúsculas lo escribimos entre comillas simples. Ejemplo:

?- atom(’a’). Yes ?- atom(’a a’). Yes ?- atom(’A’). Yes ?- atom(’2’). Yes

Números (number)

Enteros Cualquier número comprendido entre (-231 y 231). El limite esta
determinado porque los enteros se almacenan como valores de 32 bits, treinta y
uno de esos bits representan el número y el otro bit el signo. Ejemplo:
4,-300,3004

Reales Cualquier número real en el rango +/- 1E-307 a +/-1E+308. El formato
incluye estas opciones: signo, numero, punto decimal, fracción, E(exponente),
signo para el exponente, exponente. Ejemplo: 3, -3.1415

Existen distintos predicados para comprobar los tipos de términos: variables
(var), átomos (atom), cadenas (string), números (number) y términos compuestos
(compound). El predicado atomic sirve para reconocer los términos atómicos (es
decir, a las variables, átomos, cadenas y números). Por ejemplo, ?- var(X1). =>
Yes ?- var(\_). => Yes ?- var(\_X1). => Yes ?- X1=a, var(X1). => No ?-
atom(átomo). => Yes ?- atom('átomo'). => Yes ?- atom([]). => Yes ?- atom(3). =>
No ?- atom(1+2). => No ?- number(123). => Yes ?- number(-25.14). => Yes ?-
number(1+3). => No ?- X is 1+3, number(X). => X=4 Yes ?- compound(1+2). => Yes
?- compound(f(X, a)). => Yes ?- compound([1,2]). => Yes ?- compound([]). => No
?- atomic(átomo). => Yes ?- atomic(123). => Yes ?- atomic(X). => No ?-
atomic(f(1,2)). => No

### 3.2 Entrada y salida de datos

A continuación se describirán los principales predicados del lenguaje Prolog
utilizados para la entrada y salida de datos. Estos nos permitirán leer
caracteres y términos. A continuación resumiremos brevemente cada uno de ellos.

read(X)

Permite leer un cierto dato en la variable X. Este podrá ser un entero, real,
carácter o cadena de texto. La variable debe estar libre y el valor vinculado
debe estar dentro del dominio estándar.

write(X)

Es el predicado de escritura más utilizado, escribirá el valor de X en el
dispositivo de escritura activo.

Ejemplo: write(‘Hola a todos’). X=3, write(X).

display(X)

Este predicado funciona exactamente igual que write.

Ejemplo: display(‘el sol es brillante’)

nl

Este predicado indica nueva línea. Hace que el cursor se mueva a la siguiente
línea. No tiene argumentos.

### 3.3 Predicados predefinidos

Existen algunos predicados predefinidos en el sistema y que están disponibles en
todo momento. El más importante es la igualdad: =/2 . Este predicado tiene éxito
si sus dos argumentos unifican entre sí, falla en caso contrario. Por ejemplo,
el objetivo X=3 provoca la ligadura de X al valor 3 puesto que unifican.

Otro ejemplo es f(3)=f(X), que también liga X al valor 3. Es muy importante no
confundir la igualdad lógica con la igualdad aritmética. Por ejemplo, X =3+2
tiene éxito pero no resulta en X instanciado a 5. De hecho, la variable X queda
ligada al término 3+2. El signo igual (=) se utiliza para indicar que el
predicado se cumple si los objetos de ambas partes de la igualdad pueden hacerse
coincidir, es decir, el operador hace una comprobación lógica. Otros predicados
predefinidos muy útiles son los de comparación aritmética. Naturalmente, estos
no funcionan con cualquier término como argumento. Solamente sirven para números
(enteros y decimales).

![Operadores de comparación aritmética en Prolog](images/operadores-comparacion-aritmetica-prolog.png)

Operadores Significado relacionales < Menor que

> Mayor que = Igual que =< Menor o igual que = Mayor o igual que = Distinto de

### 3.4 Evaluación de expresiones aritméticas

En Prolog es fácil construir expresiones aritméticas y se hace med mediante el
predicado is/2. Por ejemplo, vamos a sumar dos números cualquiera: 1 ?- X is 2 +
5\. X = 7 yes

El predicado is/2 funciona como sentencia de asignación, dando un valor a una
variable, pero siempre y cuando la variable sea libre. Una variable no
instanciada puede usarse con sentencias de asignación. El valor de las
constantes o de otras variables instanciadas se vinculará a la variable libre.
Esto se llama haber compartido el valor. Sin embargo en una cláusula que no
tenga una variable libre, el Prolog evaluará matemáticamente la expresión y
luego comprobará si es verdadera o falsa.

Expresiones válidas Las expresiones que podemos utilizar en el segundo argumento
pueden variar de un entorno de desarrollo a otro, pero vamos a citar las más
comunes:

![Expresiones aritméticas validas en Prolog](images/expresiones-aritmeticas-validas-prolog.png)

Operadores aritméticos Significado Ejemplo +/2 Suma X is A + B. */2 Producto X
is 2 * 7. -/2 Resta X is 5 - 2. '/'/2 División X is 7 / 5. -/1 Cambio de signo X
is -Z. '//'/2 División entera X is 7 // 2. mod/2 Resto de la división entera X
is 7 mod 2. '^'/2 Potencia X is 2^3. abs/1 Valor absoluto X is abs(-3). pi/0 La
constante PI X is 2*pi. sin/1 seno en radianes X is sin(0). cos/1 coseno en
radianes X is cos(pi). tan/1 tangente en radianes X is tan(pi/2).

### 3.5 Recursividad

La recursividad es un concepto importante en Prolog. Se utiliza para describir
operaciones que se llaman a sí mismas como parte de un proceso. La recursividad
por sí misma manda el control de la búsqueda hacia atrás. En Prolog, no existen
estructuras de control para bucles. Estos se implementan mediante predicados
recursivos. La operación factorial es el primer tipo de recursividad que
normalmente la gente aprende en la escuela. A continuación, examinaremos
brevemente cómo funciona la recursividad en Prolog y cómo se puede obtener el
factorial de un número con él. Una expresión recursiva puede escaparse de las
manos sin un sólido punto final. La operación factorial para cuando se alcanza
el 1. Otras expresiones recursivas necesitan tener impuesto un límite similar.
El Prolog utiliza una pila – una creación lógica de la memoria – para guardar
los valores y variables mencionados en la búsqueda del punto final recursivo.
Finalmente, la expresión recursiva alcanza el límite. Puede encontrar un valor
en el punto final con el que trabajará hacia atrás a través de muchos niveles
hasta el resultado final. Prolog no ofrece una facilidad para el factorial como
operador incorporado. El siguiente código muestra cómo construir una definición
recursiva del factorial.

inicio:-write('Ingrese un número: '),read(N),factorial(N,Z),write(Z).
factorial(0,1). factorial(N,Z):-X is N-1,factorial(X,R),Z is R\*N.

(sec-unit-06-prolog-capitulo-4-estructuras-de-datos)=
