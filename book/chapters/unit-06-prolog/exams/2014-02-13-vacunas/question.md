# Vacunas por edad y enfermedades
- Fecha: 2014-02-13

Dada una BD con los siguientes hechos:

1. Ingresar un niño y en base a su edad indicar en una lista las vacunas que le
   faltan aplicar. 2)Ingresar un niño y una enfermedad. Para esa enfermedad,
   indicar una lista de las vacunas que la contrarrestan. Además, informar si el
   niño tiene puesta alguna de esas vacunas o le falta la aplicación de alguna
   dosis. 3)Ingresar una vacuna e indicar la cantidad de niños que la tienen
   puesta.

```prolog
niño(nombre,edad,[vacunas_aplicadas]).
vacuna(vacuna,[enfermedades_que_combate]).
vacuna_aplicacion(edadDesde,edadHasta,[vacunas_a_aplicar]).
```
