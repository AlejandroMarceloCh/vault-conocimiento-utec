---
curso: CONTAFIN
titulo: KARDEX METODO PEPS UTEC
slides: 0
fuente: KARDEX METODO PEPS UTEC.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: KARDEX METODO PEPS UTEC.xlsx. -->

<!-- INTERPRETAR: datos tabulares de KARDEX METODO PEPS UTEC.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: CLASE
Filas: 20 · Columnas: 14
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), EL CUADRO KARDEX PERMITE CONOCER EL COSTO DE LOS PRODUCTOS (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object)

Muestra (primeras 20 de 20 filas, formato CSV):
Unnamed: 0,Unnamed: 1,EL CUADRO KARDEX PERMITE CONOCER EL COSTO DE LOS PRODUCTOS,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13
,,EL CUADRO KARDEX SE ELABORA SIN IGV OJO ,,,,,,,,,,,
,,,,,FISICAS,,Costo unitario= valor unitario,,,,costo=valor,,
,EMPRESA,CIBERMUNDO S.A.C,,,,,,,,,esta sin igv,,
,PRODUCTO,LAPTOP LENOVO ICORE 7 RAM 500,,,,,,MÉTODO,PEPS,,,,
,Fecha,DETALLE,ENTRADA,,,SALIDA,,,SALDO,,,,
,,,UNID,C/U,TOTAL S/.,UNID,C/U,TOTAL S/.,UNID,C/U,TOTAL S/.,LOTE,
,01.08.2022,Stock inicial,,,,,,,110,800,88000,1,
,02.08.22,Compra,46,1004.3478260869565,46200,,,,46,1004.3478260869565,46200,2,
,06.08.2022,Dev.a proveed,-10,1004.3478260869565,-10043.478260869564,,,,36,1004.3478260869565,36156.52173913043,2,
,15.08.22,Venta,,,,110,800,88000,0,800,0,1,
,,,,,,25,1004.3478260869565,25108.695652173912,11,1004.3478260869564,11047.82608695652,2,
,16.08.22,Compra,280,1000,280000,,,,280,1180,330400,3,
,22.08.22,Venta,,,,11,1004.3478260869564,11047.82608695652,0,1004.3478260869564,0,2,
,,,,,,239,1180,282020,41,1180,48380,3,
,28.08.2022,Dev de cliente,,,,-20,800,-16000,20,800,16000,1,
,,,,,,,,,41,1180,48380,3,No se mezclan los inventarios
,,,316,,316156.52173913043,365,,390176.52173913043,600,1056.497175141243,633898.3050847457,4,
,,,,,,COSTO DE VENTAS,,,SALDO FINAL O STOCK FINAL,,,,
,,,,,,,,,,,,,
,,*LAS 365 LAPTOPS QUE VENDI ME COSTARON S/390176.52 SOLES,,,,,,,,,,,

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

## Hoja: PEPS
Filas: 19 · Columnas: 17
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), EL CUADRO KARDEX PERMITE CONOCER EL COSTO DE LOS PRODUCTOS (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), Unnamed: 15 (float64), Unnamed: 16 (float64)

Muestra (primeras 19 de 19 filas, formato CSV):
Unnamed: 0,Unnamed: 1,EL CUADRO KARDEX PERMITE CONOCER EL COSTO DE LOS PRODUCTOS,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16
,,EL CUADRO KARDEX SE ELABORA SIN IGV OJO ,,,,,,,,,,,,,,
,,,,,FISICAS,,Costo unitario= valor unitario,,,,costo=valor,,,,,
,EMPRESA,ZAPATILLAS IMPORTADAS S.A.C,,,,,,,,,esta sin igv,,,,,
,PRODUCTO,zapatilla nike air max (azul con blanco)talla 37,,,,,,MÉTODO PEPS,,,,,+,INVENTARIO INICIAL,,5000.0
,Fecha,DETALLE,ENTRADA,,,SALIDA,,,SALDO,,,,+,COMPRAS,,8675.0
,,,UNID,C/U,TOTAL S/.,UNID,C/U,COSTO TOTAL S/.,UNID,C/U,COSTO TOTAL S/.,LOTE,=,DISPONIBLE,,13675.0
,2022-07-01 00:00:00,Stock inicial,,,,,,,100,50,5000,1,-,INVENTARIO FINAL,,1135.0
,2022-07-08 00:00:00,Compra,100,62,6200,,,,100,62,6200,2,=,COSTO DE VENTAS ,,12540.0
,2022-07-10 00:00:00,Venta,,,,100,50,5000,0,50,0,1,,,,
,,,,,,30,62,1860,70,62,4340,2,,,,
,2022-07-13 00:00:00,Venta,,,,50,62,3100,20,62,1240,2,,,,
,2022-07-18 00:00:00,Compra,60,55,3300,,,,60,55,3300,3,,,,
,2022-07-20 00:00:00,Dev  a provee,-15,55,-825,,,,45,55,2475,3,,,,
,2022-07-21 00:00:00,vENTA,,,,20,62,1240,0,62,0,2,,,,
,,,,,,30,55,1650,15,55,825,3,,,,
,2022-07-24 00:00:00,Dev de cliente,,,,-5,62,-310,5,62,310,2,,,,
,,,145,,8675,225,,12540,15,55,825,3,,,,
,,,,,,,,,5,62,310,2,,,,
,,,,,,COSTO DE VENTAS,,,SALDO FINAL O STOCK FINAL,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 15   Unnamed: 16
count         0.0          0.0      5.000000
mean          NaN          NaN   8205.000000
std           NaN          NaN   5224.723677
min           NaN          NaN   1135.000000
25%           NaN          NaN   5000.000000
50%           NaN          NaN   8675.000000
75%           NaN          NaN  12540.000000
max           NaN          NaN  13675.000000

## Hoja: FORMATOS
Filas: 43 · Columnas: 18
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (float64), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (object), Unnamed: 17 (object)

Muestra (primeras 40 de 43 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17
,EMPRESA,,,,,,,,,,,,,,,,
,PRODUCTO,,,,,,,MÉTODO,,,,,,,,,
,F,DETALLE,ENTRADA,,,SALIDA,,,SALDO,,,,,,,,
,,,UNID,C/U,TOTAL,UNID,C/U,TOTAL,UNID,C/U,TOTAL,LOTE,,,,,
1.0,,,,,,,,,,,,,,,,,
2.0,,,,,,,,,,,,,,Escriba y aplique la fórmula del costo de ventas,,,
3.0,,,,,,,,,,,,,,Método,Promedio,PEPS,
4.0,,,,,,,,,,,,,,,,,
5.0,,,,,,,,,,,,,,,,,
6.0,,,,,,,,,,,,,,,,,
7.0,,,,,,,,,,,,,,,,,
8.0,,,,,,,,,,,,,,,,,
9.0,,,,,,,,,,,,,,,,,
10.0,,,,,,,,,,,,,,,,,
11.0,,,,,,,,,,,,,,,,,
12.0,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,Resultado bruto,,,
,,,,,,,,,,,,,,Método,Promedio,PEPS,
,,,,,,,,,,,,,,,,,
,EMPRESA,,,,,,,,,,,,,,,,
,PRODUCTO,,,,,,,MÉTODO,PEPS,,,,,,,,
,F,DETALLE,ENTRADA,,,SALIDA,,,SALDO,,,LOTE,,,,,
,,,UNID,C/U,TOTAL,UNID,C/U,TOTAL,UNID,C/U,TOTAL,TOTAL,,,,,
1.0,,,,,,,,,,,,,,,,,
2.0,,,,,,,,,,,,,,,,,
3.0,,,,,,,,,,,,,,,,,
4.0,,,,,,,,,,,,,,,,,
5.0,,,,,,,,,,,,,,,Cálcule la venta total,,
6.0,,,,,,,,,,,,,,,Unidades,Valor de venta unitario,Valor de venta total
7.0,,,,,,,,,,,,,,,,,
8.0,,,,,,,,,,,,,,,,,
9.0,,,,,,,,,,,,,,,,,
10.0,,,,,,,,,,,,,,,,,
11.0,,,,,,,,,,,,,,,,,
12.0,,,,,,,,,,,,,,,,,
13.0,,,,,,,,,,,,,,,,,
14.0,,,,,,,,,,,,,,,,,
15.0,,,,,,,,,,,,,,,,,
16.0,,,,,,,,,,,,,,,,,
17.0,,,,,,,,,,,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 13
count   31.000000          0.0
mean     8.645161          NaN
std      5.173963          NaN
min      1.000000          NaN
25%      4.500000          NaN
50%      8.000000          NaN
75%     12.000000          NaN
max     19.000000          NaN
