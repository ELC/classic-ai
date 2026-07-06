# Lotes y líneas de crédito
- Fecha: 2015-04-27

Una persona puede tener mas de un lote. Cada linea de crédito puede pagarse en u
numero distinto de cuotas 12, 24, 36 (Forma de financiación)

```prolog
lote(codLote, superficie, [dni], zona).
persona(dni, apellido, nombre).
lineaCredito(codLinea, descripcion, superficieDesde, SuperficieHasta, monto,[cuotas])
```

1. Ingresando un dni, devolver para cada lote la linea de crédito y el monto.

1. Ingresando un código de lote, devolver la linea de crédito y la máxima
   cantidad de cuotas de financiación.
