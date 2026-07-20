---
curso: FUNDOPS
titulo: 1-3 - Solución de Casos de Productividad
slides: 0
fuente: 1-3 - Solución de Casos de Productividad.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 1-3 - Solución de Casos de Productividad.xlsx. -->

<!-- INTERPRETAR: datos tabulares de 1-3 - Solución de Casos de Productividad.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: caso 1-2
Filas: 41 · Columnas: 8
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (float64), Unnamed: 5 (object), Unnamed: 6 (float64), Unnamed: 7 (object)

Muestra (primeras 40 de 41 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
,,,,,EJERCICIO 2,,
,EJERCICIO 1,,,,EMPRESA,,IMPRENTA
,TRAZADO Y CORTE,,,,PRODUCCION DE ,,BOLSAS DE PAPEL
,PROD.  ACTUAL,50.0,PIEZAS/HORA,,M.P.,0.5,PLIEGO X BOLSA
,PROD. MEJORADA,64.0,PIEZAS/HORA,,OPERACIÓN,,CORTAR EL PLIEGO DE PAPEL EN 2
,,,,,,,UNIR LOS BORDES CON COLA SINTETICA
,PAGO DIARIO (JORNAL),25.0,SOLES/8HORAS,,,,
,PAGO POR HORA,3.125,SOLES/HORA,,PROD. DEFECTUOSOS INICIAL,0.1,X ROTURAS
,,,,,PROD. DEFECTUOSOS MEJORADO,0.02,X ROTURAS
,PRODUCTVIDAD INICIAL,16.0,,,,,
,PRODUCTVIDAD MEJORADA,20.48,,,COSTO M.P INICIAL,1.5,SOLES/PLIEGO
,,,,,COSTO M.P FINAL,1.65,SOLES/PLIEGO
,VARIACION DE LA PRODUCTIVIDAD,0.28,,,,,
,,,,,PEDIDO,36.0,
,,,,,,,
,,,,,*******************,,
,,,,,PRODUCCION INICIAL,,
,,,,,Q BUENOS,36.0,unidades
,,,,,Q DEFECTUOSOS,,0.1
,,,,,,,
,,,,,Q TOTAL,40.0,unidades
,,,,,,,
,,,,,M.P.,0.5,PLIEGO X BOLSA
,,,,,M.P. TOTAL,20.0,PLIEGOS/BOLSAS
,,,,,COSTO DE M.P. TOTAL,30.0,SOLES x M.P. TOTAL
,,,,,,,
,,,,,PRODUCTVIDAD INICIAL,1.2,unidades/soles
,,,,,,,
,,,,,PRODUCCION MEJORADA,,
,,,,,Q BUENOS,36.0,unidades
,,,,,Q DEFECTUOSOS,,0.02
,,,,,,,
,,,,,Q TOTAL,36.734693877551024,unidades
,,,,,,,
,,,,,M.P.,0.5,PLIEGO X BOLSA
,,,,,M.P. TOTAL,18.367346938775512,PLIEGOS/BOLSAS
,,,,,COSTO DE M.P. TOTAL,30.306122448979593,SOLES x M.P. TOTAL
,,,,,,,
,,,,,PRODUCTVIDAD MEJORADA,1.1878787878787878,unidades/soles
,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 2  Unnamed: 4  Unnamed: 6
count         0.0    7.000000         0.0   19.000000
mean          NaN   25.555000         NaN   15.292418
std           NaN   23.575652         NaN   16.597422
min           NaN    0.280000         NaN   -0.010101
25%           NaN    9.562500         NaN    0.500000
50%           NaN   20.480000         NaN    1.650000
75%           NaN   37.500000         NaN   33.153061
max           NaN   64.000000         NaN   40.000000

## Hoja: Caso 3-Producción
Filas: 5 · Columnas: 17
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (object)

Muestra (primeras 5 de 5 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16
,Caso 3,,,,,,,,,,,,,,,
,,,,,,,,,,,x mes,,,,,
,Situación,Producción,Unidades,Recursos,Unidades,Costo M.O,Unidades,Minutos diarios,# Días/mes,Precio venta (S./pieza),Q a Producir (piezas) x mes,Q (soles),R (soles),Productividad (soles venta/soles M.O.),Incremento (soles venta/soles M.O.),Incremento (%)
,Actual,1,pieza,8,minutos,750,S./mes,465,20,10,1162.5,11625,750,15.5,,
,Futura,1,pieza,5,minutos,1250,S./mes,465,20,10,1860,18600,1250,14.88,-0.6199999999999992,-0.03999999999999995

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
