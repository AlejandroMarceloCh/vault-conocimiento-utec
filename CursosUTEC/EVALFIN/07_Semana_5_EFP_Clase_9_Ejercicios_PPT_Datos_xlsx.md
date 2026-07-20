---
curso: EVALFIN
titulo: 07 - Semana 5/EFP - Clase 9 - Ejercicios PPT - Datos
slides: 0
fuente: 07 - Semana 5/EFP - Clase 9 - Ejercicios PPT - Datos.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 07 - Semana 5/EFP - Clase 9 - Ejercicios PPT - Datos.xlsx. -->

<!-- INTERPRETAR: datos tabulares de EFP - Clase 9 - Ejercicios PPT - Datos.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: 2. Apalancamiento
Filas: 8 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (object)

Muestra (primeras 8 de 8 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,Inversión,1000000.0,,
,ROI,0.15,,
,Kd,0.08,,
,Préstamo,,,Porcentaje de deuda/inversión
,Capital,,,
,ROE,,,
,,,,
,Mejora el ROE si ROI > Kd * (1 - t),,,

Resumen numérico:
       Unnamed: 0      Unnamed: 2  Unnamed: 3
count         0.0        3.000000         0.0
mean          NaN   333333.410000         NaN
std           NaN   577350.202794         NaN
min           NaN        0.080000         NaN
25%           NaN        0.115000         NaN
50%           NaN        0.150000         NaN
75%           NaN   500000.075000         NaN
max           NaN  1000000.000000         NaN

## Hoja: 3. Impacto
Filas: 18 · Columnas: 8
Columnas y tipos: Unnamed: 0 (float64), Datos (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object)

Muestra (primeras 18 de 18 filas, formato CSV):
Unnamed: 0,Datos,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
,Inversión total requerida,1000000,sin VR ni Kt,,,,
,Tiempo del proyecto,5,años,,,,
,FC operativo,300000,constante 5 años,,,,
,Costo de capital propio,0.12, (Ke),,,,
,Costo de la deuda,0.08, (Kd),,,,
,Tasa de impuestos,0.3, (t),,,,
,,,,,,,
,Escenario,,,,,,
,,Año 0,Año 1,Año 2,Año 3,Año 4,Año 5
,FC inversiones,-1000000,,,,,
,FC operativo,,300000,300000,300000,300000,300000
,FC ECONOMICO,-1000000,300000,300000,300000,300000,300000
,FC financiamiento,,,,,,
,Préstamo,,,,,,
,Amortización,,,,,,
,Interés,,,,,,
,Escudo fiscal,,,,,,
,FC FINANCIERO,,,,,,

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
