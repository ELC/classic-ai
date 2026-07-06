---
title: Base de datos y functores
---

# Base de datos y functores

## Base de datos

Una base de datos es un conjunto de cláusulas (hechos y reglas) que hemos
definido antes de iniciar la ejecución del programa. Prolog tiene un motor
incorporado para buscar en dicha base.

La identificación y vuelta atrás que se realiza automáticamente cuando se
propone un objetivo, es una forma eficiente de buscar en una base de datos. Sin
embargo, es útil añadir o quitar hechos mientras se proponen objetivos.

Modificando la base de cláusulas Para poder modificar la base de datos, el
predicado a modificar debe ser etiquetado como dynamic/1. Esto se hace al
principio en el código del programa y de la siguiente forma:
:-dynamic(hecho/aridad).

Un predicado que no es dinámico es estático por defecto. Los predicados
estáticos no pueden ser alterados en tiempo de ejecución. Prolog internamente
compila las cláusulas estáticas para mejorar la eficiencia. Es por esta razón
que debe hacerse la diferencia. Una vez que tenemos etiquetado a nuestro
predicado como dinámico, entonces podemos añadir y eliminar cláusulas usando la
familia de predicados assert/1 y retract/1.

asserta(hecho). Añade un hecho a la base de datos que esta almacenada en
memoria. El hecho se coloca por encima de cualquier otra cláusula con el mismo
predicado. Es decir, que la nueva clausula queda definida como primera cláusula
del predicado.

assertz(hecho). assert(hecho). Son equivalentes, ambos añaden un hecho a la base
de datos que esta almacenada en memoria. El hecho se coloca por debajo de las
cláusulas existentes con el mismo predicado. Es decir, la nueva clausula queda
definida como última cláusula del predicado.

El predicado assert/1 y cualquiera de sus aserciones, como otros predicados de
E/S, siempre falla en el backtracking y no deshace sus propios cambios.

retract(hecho). Elimina una cláusula en particular. Es decir, suprime el primer
hecho de la base de datos que coincide con el hecho objetivo. Como en el caso
del assert/1, no es posible deshacer los cambios debidos a este predicado en el
backtraking.

retractall(hecho). Elimina todas las cláusulas de un predicado definidas en la
base de datos.

Grabar la base de datos en disco Es posible guardar una base de datos en un
archivo (.txt o .pl) en disco. Para hacerlo se utilizan los siguientes
predicados: tell/1: cambia el dispositivo de escritura por defecto al archivo.
listing/1: lista en el archivo en este caso, los hechos de la base de datos.
told: devuelve el dispositivo de escritura a pantalla.
grabar::-tell(‘C:/…/nombre_archivo.txt’),listing(hecho),told. Este archivo de
texto tendrá una clausula en cada línea y puede ser editado directamente.

Levantar la base de datos a memoria consult/1 trae un archivo de predicados de
una base de datos a memoria. Si cualquiera de las líneas del archivo no
coinciden con los estándares de sintaxis de Prolog, el predicado consult/1
fallará. Frecuentemente, el archivo consultado será un archivo que se puso en el
disco a través de los predicados tell/1, listing/1 y told. consult/1 puede ser
invocado de varias formas. La más simple consiste en llamar a consult/1 con el
nombre del archivo sin la extensión. Es indiferente el uso de mayúsculas o
minúsculas excepto para la primera letra que debe ser minúscula para que Prolog
no piense que es una variable. consult(practica3). En este caso buscará en el
directorio actual y en una serie de directorios que tiene para buscar un archivo
con ese nombre. Otra forma consiste en escribir la ruta del archivo completa
entre comillas simples. La barra que separa los directorios en Windows debe
estar inclinada hacia la derecha (y no como en Windows que está escrita hacia la
izquierda). consult(’c:/documentos/practica3.txt’).

Mostrar la base de cláusulas Para ver el contenido de la base usamos el
predicado listing/0. Este predicado muestra todas las cláusulas que tenemos
actualmente. Para ver sólo aquellas cláusulas que pertenecen a un predicado
usamos listing(Pred) donde Pred es el predicado que buscamos mirar.

Ejemplos: :-dynamic(estudiantes/3). % Indica que estudiantes es un predicado
dinámico de aridad tres, es decir, que toma tres argumentos. % Esto tiene que
ser declarado para poder utilizar los predicados y assert/1 y retract/1.

carga_estudiantes:-consult('C:/Facultad/Inteligencia Artificial/Prolog/
Ejemplos/estudiantes.txt'). % carga en memoria la base de hechos del tipo
estudiantes/3 definida en el archivo estudiantes.txt

lista_estudiantes:-listing(estudiantes). % lista todo el conocimiento del
predicado estudiantes.

agregar(Código, Nombre, Apellido):-assert(estudiantes(Código, Nombre,
Apellido)), write(' Agregado! '). % agrega un estudiante

eliminar(Código):-retract(estudiantes(Código, _,_)), write(' Eliminado!'). %
elimina un estudiante identificado por Código.

El predicado Fail Se trata de un predicado que siempre falla. Se utiliza para
obligar al Prolog a dar un fallo. El predicado fail/0 se utiliza para realizar
búsquedas en la base de datos y no quedarnos únicamente con la primera solución
que satisface la búsqueda, por tanto, implica la realización del proceso de
retroceso para que se generen nuevas soluciones. Una aplicación de este
predicado es entonces la generación de todas las posibles soluciones para un
problema. Recordemos que cuando la máquina Prolog encuentra una solución para y
devuelve el resultado de la ejecución. Con fail podemos forzar a que no pare y
siga construyendo el árbol de búsqueda hasta que no queden más soluciones que
mostrar.

Ejemplo: Supongamos que contamos con la siguiente Base de conocimiento:
gastos(mario,super). gastos(mario,teléfono). gastos(mario,alquiler).
gastos(ariel,teléfono). gastos(ariel,alquiler). gastos(juan,alquiler).

Inicio:-write(‘Ingrese nombre de la persona’),read(Nom),gastos(Nom,Gasto),
write(Gasto). De esta manera, si ingresamos por ejemplo el nombre ‘mario’, nos
informaría únicamente del gasto ‘super’.

Inicio:-write(‘Ingrese nombre de la persona’),read(Nom),gastos(Nom,Gasto),
write(Gasto),fail. De esta otra manera, e ingresando el mismo nombre de persona,
nos informaría de todos los gastos correspondientes a ‘mario’, es decir,
‘super’, ‘teléfono’ y ‘alquiler’.

Ejemplo: Contamos con esta otra Base de conocimientos: padre(juan, jose).
padre(omar, laura). padre(juan, luis). padre(juan, alberto). padre(pedro,
mario).

listado:-padre(juan,X), write(X), nl, fail.

Objetivo ?.- listado.

Respuesta jose luis alberto

## Functores

En muchas aplicaciones se necesita emplear tipos de datos más complejos que los
que se han usado hasta este momento. Cuando un argumento es a s vez un
predicado, se llama functor y los argumentos de un functor se llaman
componentes. Los objetos compuestos le permiten añadir mas detalles a las
cláusulas. Por ejemplo, una lista de facturas a pagar podría escribirse como la
siguiente serie de hechos.

paga(marco, super). paga(marco,teléfono).

Con la utilización de objetos compuestos, las mismas presentarían mayor
información.

paga(marco, super(coto,1000). paga(marco,teléfono(personal,móvil,500)).

La estructura de la cláusula mostrada con objetos compuestos tiene la siguiente
forma:

predicado(argumento,functor(componente, componente, componente)).

Los componentes de un objeto compuesto pueden a su vez ser objetos compuestos.
No se debe hacer esto indefinidamente, porque demasiados niveles de paréntesis
harían al programa demasiado difícil de leer.
