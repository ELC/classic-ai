# Canciones favoritas por invitados y género vals

- Fecha: 2015-12-17

La base de hechos estaba formada por:

Tenía un atributo mas que no me acuerdo pero no se usaba

```prolog
cancion(IdCancion,Nombre,Artista,Duración,Genero)
invitados(Nombre, [IdCanciones que gusta])
```

1. Listar las canciones que le gusta a más del 80% de los invitados.

1. Listar las canciones de género "vals" que duren más de 15 minutos. Nota:
   fijense esto del punto 1, lo que pueden hacer es crear 2 bases de hechos, una
   con los hechos de canciones y otro con la de los invitados, y cuando busco
   por canción todos los invitados y los elimino con un retract, luego los
   vuelvo a cargar (a los invitados) ya que son bases diferentes.
