---
curso: CONTAFIN
titulo: S7 KARDEX UTEC SOLUCIONARIO
slides: 0
fuente: S7 KARDEX UTEC SOLUCIONARIO.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: S7 KARDEX UTEC SOLUCIONARIO.xlsx. -->

<!-- INTERPRETAR: datos tabulares de S7 KARDEX UTEC SOLUCIONARIO.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Caso 2
Filas: 35 · Columnas: 16
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), EL CUADRO KARDEX PERMITE CONOCER EL COSTO DE LOS PRODUCTOS (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (float64), Unnamed: 13 (object), Unnamed: 14 (float64), Unnamed: 15 (float64)

Muestra (primeras 35 de 35 filas, formato CSV):
Unnamed: 0,Unnamed: 1,EL CUADRO KARDEX PERMITE CONOCER EL COSTO DE LOS PRODUCTOS,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15
,,EL CUADRO KARDEX SE ELABORA SIN IGV OJO ,,,,,,,,,,,,,
,,,,,FISICAS,,Costo unitario= valor unitario,,,,costo=valor,,,,
,EMPRESA,FAST RUNNERS S.A.C,,,,,,,,,esta sin igv,,,,
,PRODUCTO,zapatilla nike air max (azul con blanco)talla 38,,,,,,MÉTODO,PROMEDIO,,,,INVENTARIO INICIAL,,5000.0
,Fecha,DETALLE,ENTRADA,,,SALIDA,,,SALDO,,,,COMPRAS,,8675.0
,,,UNID,C/U,TOTAL S/.,UNID,C/U,TOTAL S/.,UNID,C/U,TOTAL S/.,,DISPONIBLE,,13675.0
,2022-07-01 00:00:00,Stock inicial,,,,,,,100,50,5000,,INVENTARIO FINAL,,1106.1538461538462
,2022-07-08 00:00:00,Compra,100,62,6200,,,,200,56,11200,,COSTO DE VENTAS ,,12568.846153846154
,2022-07-10 00:00:00,Venta,,,,130,56,7280,70,56,3920,,,,
,2022-07-13 00:00:00,Venta,,,,50,56,2800,20,56,1120,,,,
,2022-07-18 00:00:00,Compra,60,55,3300,,,,80,55.25,4420,,,,
,2022-07-20 00:00:00,Dev  a provee,-15,55,-825,,,,65,55.30769230769231,3595,,,,
,2022-07-21 00:00:00,Venta,,,,50,55.30769230769231,2765.3846153846152,15,55.307692307692314,829.6153846153848,,,,
,2022-07-24 00:00:00,Dev de cliente,,,,-5,55.30769230769231,-276.53846153846155,20,55.30769230769231,1106.1538461538462,,,,
,,,,,,,,,,,,,,,
,,,145,,8675,225,,12568.846153846154,20,,1106.1538461538462,,,,
,,,,,,COSTO DE VENTAS,,,SALDO FINAL O STOCK FINAL,,,,,,
,Tip: Recuerden que Ustedes son COMPRADOR.,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,LOS PRODUCTOS SE VENDEN AL CLIENTE SEGUN:,,,,FECHA,UNIDADES VENDIDAS,VALOR DE VENTA UNITARIO,VALOR TOTAL,,,,,,
,,2022-07-10 00:00:00,200 SOLES CADA UNO,,,,,,,,,,,,
,,2022-07-13 00:00:00,180 SOLES CADA UNO,,,2022-07-10 00:00:00,130,200,26000,,,,,,
,,2022-07-21 00:00:00,200 SOLES CADA UNO,,,2022-07-13 00:00:00,50,180,9000,,,,,,
,,,,,,2022-07-21 00:00:00,50,200,10000,,,,,,
,,,,,,2022-07-24 00:00:00,-5,200,-1000,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,VENTA NETA,44000,,,,,,
,,,,,,,,VENTAS,45000,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,VENTA NETA,,44000,,VENTAS,,45000,,,,,,,
,,COSTO DE VENTAS,,12568.846153846154,,DEV.DE CLIENTES,,1000,,,,,,,
,,RESULTADO BRUTO,,31431.153846153844,,VENTA NETA,,44000,,,,,,,
,,,,,,COSTO DE VENTAS,,12568.846153846154,,,,,,,
,,,,,,RESULTADO BRUTO,,31431.153846153844,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 12  Unnamed: 14   Unnamed: 15
count         0.0          0.0          0.0      5.000000
mean          NaN          NaN          NaN   8205.000000
std           NaN          NaN          NaN   5240.481728
min           NaN          NaN          NaN   1106.153846
25%           NaN          NaN          NaN   5000.000000
50%           NaN          NaN          NaN   8675.000000
75%           NaN          NaN          NaN  12568.846154
max           NaN          NaN          NaN  13675.000000

## Hoja: Caso 1
Filas: 26 · Columnas: 12
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), EL CUADRO KARDEX PERMITE CONOCER EL COSTO DE LOS PRODUCTOS (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object)

Muestra (primeras 26 de 26 filas, formato CSV):
Unnamed: 0,Unnamed: 1,EL CUADRO KARDEX PERMITE CONOCER EL COSTO DE LOS PRODUCTOS,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11
,,EL CUADRO KARDEX SE ELABORA SIN IGV OJO ,,,,,,,,,
,,,,,FISICAS,,Costo unitario= valor unitario,,,,costo=valor
,EMPRESA,COMPUTER PERU S.A.C,,,,,,,,,esta sin igv
,PRODUCTO,LAPTOP LENOVO CORE i7,,,,,,MÉTODO,PROMEDIO,,
,Fecha,DETALLE,ENTRADA,,,SALIDA,,,SALDO,,
,,,UNID,C/U, COSTO TOTAL S/.,UNID,C/U,TOTAL S/.,UNID,C/U,COSTO TOTAL S/.
,01.08.2022,Stock inicial,,,,,,,110,800,88000
,03.08.22,Compra,46,1004.3478260869565,46200,,,,156,860.2564102564103,134200
,06.08.2022,Dev.a proveed,-10,1004.3478260869565,-10043.478260869564,,,,146,850.3871351995235,124156.52173913043
,15.08.22,Venta,,,,135,850.3871351995235,114802.26325193567,11,850.3871351995239,9354.258487194762
,16.08.22,Compra,280,1050,294000,,,,291,1042.4544965195696,303354.2584871948
,22.08.22,Venta,,,,250,1042.4544965195696,260613.6241298924,41,1042.4544965195698,42740.63435730236
,26.08.2022,Compra,600,1056.497175141243,633898.3050847457,,,,641,1055.5989694883745,676638.9394420481
,28.08.2022,Dev de cliente,,,,-20,850.3871351995235,-17007.742703990472,661,1049.3898368321309,693646.6821460385
,,,,,,,,,,,
,,,916,,964054.8268238762,365,,358408.1446778376,661,,693646.6821460385
,,,,,,COSTO DE VENTAS,,,SALDO FINAL O STOCK FINAL,,
,Tip: Recuerden que Ustedes son COMPRADOR.,,,,,,,,,,
,,,,,,,,,COSTO TOTAL,=,COSTO UNITARIO
,,,,,Aquí es S/46000 de las computadoras +,,,,UNIDADES,,
,,,,,S/200 del valor del flete.TODO es lo que,,,,,,
,,,,,invertiste en comprar las 46 laptops,,,,PRECIO/1.18= VALOR,,
,,,,,,,,,,,
,,,,,EL KARDEX SOLO DEBE TENER DATOS AL COSTO O VALOR (ES DECIR SIN IGV),,,,PRECIO= DATO QUE INCLUYE IGV,,
,,,,,,,,,,,
,,,,,,,,,VALOR O COSTO = DATO QUE NO INCLUYE IGV,,

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

## Hoja: FORMULAS
Filas: 11 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 11 de 11 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,,COSTO TOTAL,=,COSTO UNITARIO
,,UNIDADES,,
,,,,
,,PRECIO/1.18= VALOR,,
,,,,
,,PRECIO= DATO QUE INCLUYE IGV,,
,,,,
,,VALOR O COSTO = DATO QUE NO INCLUYE IGV,,
,,,,
,,,,
,,EL KARDEX SOLO DEBE TENER DATOS AL COSTO O VALOR (ES DECIR SIN IGV),,

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

## Hoja: FORMATOS
Filas: 50 · Columnas: 18
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (float64), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (object), Unnamed: 17 (object)

Muestra (primeras 40 de 50 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,EMPRESA,,,,,,,,,,,,,,,,
,PRODUCTO,,,,,,,MÉTODO,PROMEDIO,,,,,,,,
,F,DETALLE,ENTRADA,,,SALIDA,,,SALDO,,,,,,,,
,,,UNID,C/U,TOTAL,UNID,C/U,TOTAL,UNID,C/U,TOTAL,,,,,,
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
,,,UNID,C/U,TOTAL,UNID,C/U,TOTAL,UNID,C/U,TOTAL,,,,,,
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
