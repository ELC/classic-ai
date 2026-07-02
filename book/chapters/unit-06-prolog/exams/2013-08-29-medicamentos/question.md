# Medicamentos, composicion y sintomas

- Fecha: 2013-08-29

1. Ingresar una lista [] de síntomas que presenta un paciente e informar a
   través de una nueva lista [] los nombres de los medicamentos que
   contrarrestan al menos el 80% de los síntomas del paciente.

1. Ingresar dos componentes y sus respectivas cantidades e informar a través de
   una lista [] los nombres de los medicamentos que contienen dichos componentes
   y en la cantidad indicada.

Nota Personal: para resolver el punto 2 hay que tener en cuenta que el
medicamento debe contener los 2 componentes en las 2 cantidades indicadas.

```prolog
medicamentos(nombre,droga,presentación,laboratorio,[síntomas que contrarresta]).
composición(nombre,componente,cantidad).
```
