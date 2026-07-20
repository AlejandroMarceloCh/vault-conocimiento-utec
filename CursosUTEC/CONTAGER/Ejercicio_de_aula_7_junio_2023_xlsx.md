---
curso: CONTAGER
titulo: Ejercicio de aula 7 junio 2023
slides: 0
fuente: Ejercicio de aula 7 junio 2023.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Ejercicio de aula 7 junio 2023.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Ejercicio de aula 7 junio 2023.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Hoja1
Filas: 26 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 26 de 26 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,,,2022-01-01 00:00:00,2022-02-01 00:00:00
,,SALDO INICIAL,3500,14995
,,INGRESOS S/.,,
,,prestamo del banco,7000,
,,COBRANZA F/CLIENTE Frankz B.,10620,
,,COBRANZA AL CLIENTE Burgstein,,9440
,,Cobranzas proyectadas,,4814.400000000001
,,TOTAL INGRESOS S/,17620,14254.400000000001
,,EGRESOS:,,
,,PAGO FACTURA F/001-7622,1500,
,,PAGO RECIBO AGUA+LUZ+TELEFONO,1160,1500
,,PAGO CUOTA 1 AL BCP,,1000
,,PAGO ADELANTO DE IMP A LA RENTA,850,255
,,PAGO PLANILLA,2615,10615
,,PAGO A SODIMAC,,118
,,PAGO DE IGV,,2636.237288135593
,,TOTAL EGRESOS S/,6125,16124.237288135593
,,FLUJO DEL MES S/,11495,-1869.8372881355917
,,SALDO FINAL S/,14995,13125.162711864408
,,,,
,,Borrador:,,
,,PAGO DE SERVICIOS,,
,,,,
,,*Historico,,
,,Ventas al contado 20%,,
,,Ventas al credito 80%,,

Resumen numérico:
       Unnamed: 0  Unnamed: 1
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: igv
Filas: 26 · Columnas: 5
Columnas y tipos: Unnamed: 0 (datetime64[ns]), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 26 de 26 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,REGISTRO DE COMPRAS,,0.18,PRECIO
,2022-01-01 00:00:00,VALOR DE VENTA,IGV,IMPORTE TOTAL
, compra F/001-7622,1271.1864406779662,228.8135593220339,1500
,Serv.basicos,983.0508474576271,176.94915254237287,1160
,Compra a Sodimac,100,18,118
,,,,
,,,423.7627118644068,
,,,Credito fiscal,
,REGISTRO DE VENTAS,,,
,,VALOR DE VENTA,IGV,IMPORTE TOTAL
2023-01-18,Venta a cliente,9000,1620,10620
2023-01-28,Venta a cliente,8000,1440,9440
,,17000,3060,20060
,,,,
,,,,
,REGISTRO DE COMPRAS,,0.18,PRECIO
,2022-02-01 00:00:00,VALOR DE VENTA,IGV,IMPORTE TOTAL
,proyeccion recibo agua,1271.1864406779662,228.8135593220339,1500
,,,,
,,,,
,,,,
,,,,
,REGISTRO DE VENTAS(proyeccion),,,
,,VALOR DE VENTA,IGV,IMPORTE TOTAL
,Proyeccion,20400,3672,24072
,,,3672,
