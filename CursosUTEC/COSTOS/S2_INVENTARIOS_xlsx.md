---
curso: COSTOS
titulo: S2 INVENTARIOS
slides: 0
fuente: S2 INVENTARIOS.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: S2 INVENTARIOS.xlsx. -->

<!-- INTERPRETAR: datos tabulares de S2 INVENTARIOS.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: PEPS
Filas: 77 · Columnas: 11
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object)

Muestra (primeras 40 de 77 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,,,,,,,,,,
,METODO PEPS,,,,,,,,,
,,,,,,,,,,
,FECHA,COMPRAS,,,COSTO BIENES VENDIDOS,,,INVENTARIO DISPONIBLE,,
,,CANTIDAD,COSTO UNITARIO,COSTO TOTAL,CANTIDAD,COSTO UNITARIO,COSTO TOTAL,CANTIDAD,COSTO UNITARIO,COSTO TOTAL
,2017-01-01 00:00:00,,,,,,,70,200,14000
,2017-02-20 00:00:00,420,225,94500,,,0,70,200,14000
,,,,,,,,420,225,94500
,2017-04-10 00:00:00,,,0,70,200,14000,210,225,47250
,,,,,210,225,47250,,,
,2017-06-08 00:00:00,490,250,122500,,,0,210,225,47250
,,,,,,,,490,250,122500
,,,,,,,,,,
,2017-11-06 00:00:00,,,0,210,225,47250,130,250,32500
,,,,,360,250,90000,,,
,2017-12-31 00:00:00,910,,217000,850,,198500,130,,32500
,,,,,,,,,,
,INVENTARIO INICIAL,,,14000,,,,,,
,(+) COMPRAS,,,217000,,,,,,
,(-) INVENTARIO FINAL,,,-32500,,,,,,
,COSTO DE VENTAS,,,198500,0,,,,,
,,,,,,,,,,
,,,,,,,,,,
,ASIENTOS,,,,,,,,,
,,,,,,,,,,
,,_____ x_____,,,,,,,,
,2017-02-20 00:00:00,Compras,,,94500,,,,,
,,Cuentas por pagar,,,,94500,,,,
,,Por la compra de 420 unid,,,,,,,,
,,_____ x_____,,,,,,,,
,,Existencias,,,94500,,,,,
,,Variación de existencias,,,,94500,,,,
,,Por el ingreso al almacén,,,,,,,,
,,_____ x_____,,,,,,,,
,,,,,,,,,,
,,_____ x_____,,,,,,,,
,2017-04-10 00:00:00,Cuentas por cobrar,,,84000,,,,,
,,Ventas,,,,84000,,,,
,,Por la venta de 280 unid a S/ 300.00 c/u,,,,,,,,
,,_____ x_____,,,,,,,,

Resumen numérico:
       Unnamed: 0
count         0.0
mean          NaN
std           NaN
min           NaN
25%           NaN
50%           NaN
75%           NaN
max           NaN

## Hoja: UEPS
Filas: 77 · Columnas: 11
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object)

Muestra (primeras 40 de 77 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,,,,,,,,,,
,METODO UEPS,,,,,,,,,
,,,,,,,,,,
,FECHA,COMPRAS,,,COSTO BIENES VENDIDOS,,,INVENTARIO DISPONIBLE,,
,,CANTIDAD,COSTO UNITARIO,COSTO TOTAL,CANTIDAD,COSTO UNITARIO,COSTO TOTAL,CANTIDAD,COSTO UNITARIO,COSTO TOTAL
,2017-01-01 00:00:00,,,,,,,70,200,14000
,2017-02-20 00:00:00,420,225,94500,,,0,70,200,14000
,,,,,,,,420,225,94500
,2017-04-10 00:00:00,,,0,280,225,63000,70,200,14000
,,,,,,,,140,225,31500
,2017-06-08 00:00:00,490,250,122500,,,0,70,200,14000
,,,,,,,,140,225,31500
,,,,,,,,490,250,122500
,2017-11-06 00:00:00,,,0,490,250,122500,70,200,14000
,,,,,80,225,18000,60,225,13500
,2017-12-31 00:00:00,910,,217000,850,,203500,130,,27500
,,,,,,,,,,
,INVENTARIO INICIAL,,,14000,,,,,,
,(+) COMPRAS,,,217000,,,,,,
,(-) INVENTARIO FINAL,,,-27500,,,,,,
,COSTO DE VENTAS,,,203500,0,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,_____ x_____,,,,,,,,
,2017-02-20 00:00:00,Compras,,,94500,,,,,
,,Cuentas por pagar,,,,94500,,,,
,,Por la compra de 420 unid a S/. 225 c/u,,,,,,,,
,,_____ x_____,,,,,,,,
,,Existencias,,,94500,,,,,
,,Variación de existencias,,,,94500,,,,
,,Por el ingreso al almacén,,,,,,,,
,,_____ x_____,,,,,,,,
,,,,,,,,,,
,,_____ x_____,,,,,,,,
,2017-04-10 00:00:00,Cuentas por cobrar,,,84000,,,,,
,,Ventas,,,,84000,,,,
,,Por la venta de 280 unid a S/ 300.00 c/u,,,,,,,,
,,_____ x_____,,,,,,,,

Resumen numérico:
       Unnamed: 0
count         0.0
mean          NaN
std           NaN
min           NaN
25%           NaN
50%           NaN
75%           NaN
max           NaN

## Hoja: PROMEDIO
Filas: 77 · Columnas: 11
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object)

Muestra (primeras 40 de 77 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,,,,,,,,,,
,METODO PROMEDIO,,,,,,,,,
,,,,,,,,,,
,FECHA,COMPRAS,,,COSTO BIENES VENDIDOS,,,INVENTARIO DISPONIBLE,,
,,CANTIDAD,COSTO UNITARIO,COSTO TOTAL,CANTIDAD,COSTO UNITARIO,COSTO TOTAL,CANTIDAD,COSTO UNITARIO,COSTO TOTAL
,2017-01-01 00:00:00,,,,,,,70,200,14000
,2017-02-20 00:00:00,420,225,94500,,,0,490,221.42857142857142,108500
,,,,,,,,,,
,2017-04-10 00:00:00,,,0,280,221.42857142857142,62000,210,221.42857142857142,46500
,,,,,,,,,,
,2017-06-08 00:00:00,490,250,122500,,,0,700,241.42857142857142,169000
,,,,,,,,,,
,,,,,,,,,,
,2017-11-06 00:00:00,,,0,570,241.42857142857142,137614.2857142857,130,241.42857142857142,31385.714285714283
,,,,,,,,,,
,2017-12-31 00:00:00,910,,217000,850,,199614.2857142857,130,,31385.714285714283
,,,,,,,,,,
,INVENTARIO INICIAL,,,14000,,,,,,
,(+) COMPRAS,,,217000,,,,,,
,(-) INVENTARIO FINAL,,,-31385.714285714283,,,,,,
,COSTO DE VENTAS,,,199614.2857142857,0,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,_____ x_____,,,,,,,,
,2017-02-20 00:00:00,Compras,,,94500,,,,,
,,Cuentas por pagar,,,,94500,,,,
,,Por la compra de 420 unid a S/. 225 c/u,,,,,,,,
,,_____ x_____,,,,,,,,
,,Existencias,,,94500,,,,,
,,Variación de existencias,,,,94500,,,,
,,Por el ingreso al almacén,,,,,,,,
,,_____ x_____,,,,,,,,
,,,,,,,,,,
,,_____ x_____,,,,,,,,
,2017-04-10 00:00:00,Cuentas por cobrar,,,84000,,,,,
,,Ventas,,,,84000,,,,
,,Por la venta de 280 unid a S/ 300.00 c/u,,,,,,,,
,,_____ x_____,,,,,,,,

Resumen numérico:
       Unnamed: 0
count         0.0
mean          NaN
std           NaN
min           NaN
25%           NaN
50%           NaN
75%           NaN
max           NaN

## Hoja: COMPARACION
Filas: 7 · Columnas: 5
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 7 de 7 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,,,,
,,PEPS,UEPS,PROMEDIO
Ingresos por ventas,,255000,255000,255000
(-) Costo de los bienes vendidos,,198500,203500,199614.2857142857
Utilidad Bruta,,56500,51500,55385.71428571429
,,,,
,,0,0,0

Resumen numérico:
       Unnamed: 1
count         0.0
mean          NaN
std           NaN
min           NaN
25%           NaN
50%           NaN
75%           NaN
max           NaN

## Hoja: Caso
Filas: 0 · Columnas: 0
Columnas y tipos: 

Muestra (primeras 0 de 0 filas, formato CSV):
