---
curso: COSTOS
titulo: 1. COSTO ESTANDAR calculos
slides: 0
fuente: 1. COSTO ESTANDAR calculos.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 1. COSTO ESTANDAR calculos.xlsx. -->

<!-- INTERPRETAR: datos tabulares de 1. COSTO ESTANDAR calculos.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: EJERCICIO
Filas: 28 · Columnas: 8
Columnas y tipos: Unnamed: 0 (object), Estandar (object), Real (object), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (float64)

Muestra (primeras 28 de 28 filas, formato CSV):
Unnamed: 0,Estandar,Real,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
PRECIO MP A,2.5,2.26,,,,,
PRECIO MP B,0.75,0.77,,,,,
CANTIDAD MP A,2500,2650,,,,,
CANTIDAD MP B,10000,10100,,,,,
TARIFA dpto I,15,16.25,,,,,
TARIFA dpto II,18,18,,,,,
HORAS Dpto I,250,300,,,,,
HORAS Dpto II,650,600,,,,,
BASE CIF,900,900,,,,,
TASA CIF,12,12,,,,,
,,,,,,,
"Variación de Precio A = 2,650 (2.50 - 2.26) =+636 (F)",,,,,636.0000000000006,favorable,
"Variación de Precio B = 10,100 (0.75 - 0.77) =-202 (D)",,,,,-202.00000000000017,desfavorable,
"Variación de Cantidad de A = 2.50 (2,500 - 2,650) = -375 (D)",,,,,-375,desfavorable,
"Variación de Cantidad de B = 0.75 (10,000 - 10,100) = -75 (D)",,,,,-75,desfavorable,
Variación de Tarifa Dpto I = 300 (15.00 - 16.25) = -375 (D),,,,,-375,desfavorable,
Variación de Tarifa Dpto II = 600 (18.00 - 18.00) = 0 (N),,,,,0,neutro,
Variación de Eficiencia I =15.00 (250 - 300) = -750 (D),,,,,-750,desfavorable,
Variación de Eficiencia II =18.00 (650 - 600) = +900 (F),,,,,900,favorable,
Variación de CIF = 900 x 12 - 900 x 12 = 0,,,,,0,neutro,
,,,,,,,
"El primer mes se trabajaron 5 lotes de producción, obteniendo los siguientes costos:",,,,,,,
Materia Prima,,Cantidad,,,Total,,
   Material A  ,  ,2650,,,5989,,2.26
   Material B ,,10100,,,7777,,
Mano de Obra,,Horas,,,Total,,
   Departamento 1    ,,300,,,4875,,
   Departamento 2 ,  ,600,,,10800,,

Resumen numérico:
       Unnamed: 3  Unnamed: 4  Unnamed: 7
count         0.0         0.0        1.00
mean          NaN         NaN        2.26
std           NaN         NaN         NaN
min           NaN         NaN        2.26
25%           NaN         NaN        2.26
50%           NaN         NaN        2.26
75%           NaN         NaN        2.26
max           NaN         NaN        2.26

## Hoja: FORMULAS
Filas: 9 · Columnas: 8
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (float64), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (object), Unnamed: 7 (object)

Muestra (primeras 9 de 9 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
"Variación de Precio A = 2,650 (2.50 - 2.26) =+636 (F)",,,,,,VAR Precio MPD A,Q Real * (Costo STD - Costo REAL)
"Variación de Precio B = 10,100 (0.75 - 0.77) =-202 (D)",,,,,,VAR Precio MPD B,Q Real * (Costo STD - Costo REAL)
"Variación de Cantidad de A = 2.50 (2,500 - 2,650) = -375 (D)",,,,,,VAR Q MPD A,COSTO UNT. STD * (Q STD - Q REAL)
"Variación de Cantidad de B = 0.75 (10,000 - 10,100) = -75 (D)",,,,,,VAR Q MPD B,COSTO UNIT. STD * (Q STD - Q REAL)
Variación de Tarifa Dpto I = 300 (15.00 - 16.25) = -375 (D),,,,,,VAR TASA MOD D1,Q Real hrs * (TASA STD - TASA REAL)
Variación de Tarifa Dpto II = 600 (18.00 - 18.00) = 0 (N),,,,,,VAR TASA MOD D2,Q Real hrs * (TASA STD - TASA REAL)
Variación de Eficiencia I =15.00 (250 - 300) = -750 (D),,,,,,VAR EFICIENCIA MOD D1,Tasa STD * (Q hrs STD -  Q hrs REAL)
Variación de Eficiencia II =18.00 (650 - 600) = +900 (F),,,,,,VAR EFICIENCIA MOD D2,Tasa STD  * (Q hrs STD -  Q hrs REAL)
Variación de CIF = 900 x 12 - 900 x 12 = 0,,,,,,,

Resumen numérico:
       Unnamed: 1  Unnamed: 2  Unnamed: 3  Unnamed: 4  Unnamed: 5
count         0.0         0.0         0.0         0.0         0.0
mean          NaN         NaN         NaN         NaN         NaN
std           NaN         NaN         NaN         NaN         NaN
min           NaN         NaN         NaN         NaN         NaN
25%           NaN         NaN         NaN         NaN         NaN
50%           NaN         NaN         NaN         NaN         NaN
75%           NaN         NaN         NaN         NaN         NaN
max           NaN         NaN         NaN         NaN         NaN
