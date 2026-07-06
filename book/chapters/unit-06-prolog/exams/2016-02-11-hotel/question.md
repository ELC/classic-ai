# Hotel: habitaciones disponibles y habitaciones premium ocupadas
- Fecha: 2016-02-11

Un Hotel cuenta con la siguiente base de hechos:

Una habitación puede contener una cierta cantidad de características como por
ejemplo “WIFI, Heladera, Aire Acondicionado, etc”. Una habitación pueda pasar
por dos estados, “disponible” y “ocupada”. Una habitación cuyo precio por día es
mayor a $1000 se considera una habitación Premium.

```prolog
habitación(numero,descripción,[Lista de Cod. Caract.],precio x dia, estado)
característica(código,descripción)
```

1. Un usuario quiere saber las habitaciones disponibles según una lista de
   características que ingresa (Códigos), donde se debe mostrar de cada
   habitación disponible, Descripción y Precio por día. Una habitación puede
   tener más características que las ingresadas por el usuario.

1. El gerente del hotel quiere regalarles un champan a cada habitación Premium
   que se encuentre ocupada en ese momento. Genere dicho informe.
