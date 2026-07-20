---
curso: COSTOS
titulo: 2. COSTO ESTANDAR EJEMPLO
slides: 0
fuente: 2. COSTO ESTANDAR EJEMPLO.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 2. COSTO ESTANDAR EJEMPLO.xlsx. -->

<!-- INTERPRETAR: datos tabulares de 2. COSTO ESTANDAR EJEMPLO.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: solución
Filas: 180 · Columnas: 10
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object)

Muestra (primeras 40 de 180 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9
,UTEC,,,,,,,,
,CURSO,COSTOS Y PRESUPUESTOS,,,,,,,
,,,,,,,,,
,GUIA 4,,,,,,,,
,EJERCICIO 1,,VARIACIONES ESTANDAR,,,,,,
,,,,,,,,,
,"Determine las variaciones de Precio, Cantidad, Eficiencia, Tasa Laboral y CIF de:",,,,,,,,
,,,,,,,,,
,,,ESTANDAR,,,,,,
,,Producto:,,,Casaca de cuero,,,,
,,Cantidad:,,,10,unidades,,,
,,MATERIALES,Cantidad,,Precio ($),,Total,398.99999999999994,
,, Cuero Guante,250,pies,1.3, / pie,325,,
,, Napa,150,pies,0.34, / pie,51.00000000000001,,
,, Forro,18,metros,0.9, / mt,16.2,,
,, Botones,80,botones,0.08,unidad,6.4,,
,, Etiqueta,20,unidades,0.02,unidad,0.4,,
,,MANO DE OBRA,Horas,,Tarifa ($ / hora),,Total,24.5,
,, Corte,0.4,,10,,4,,
,, Costura,1.2,,15,,18,,
,, Acabado,0.5,,5,,2.5,,
,,CIF,Base,,Tasa,,Total,103.57999999999998,
,, Corte,  Horas MOD,,15,,6,,
,, Costura,  Costo MP,,0.22,,87.77999999999999,,
,, Acabado,  Costo MO,,0.4,,9.8,,
,,,,TOTAL $,,,527.0799999999999,,
,,,COSTO POR UNIDAD $,,,,52.70799999999999,,
,,,,,,,,,
,Se trabajo un pedido de ,,500,unidades y se incurrió en los siguientes gastos y costos:,,,,,
,,,Comprado,,Usado,,  Precio,,
,Cuero guante,,5000,pies,5000,pies,1.2,pies,
,,,10000,pies,8000,pies,1.35,pies,
,Cuero napa,,5000,pies,5000,pies,0.31,pies,
,,,2820,pies,2820,pies,0.35,pies,
,Forro,,1000,mts,840,mts,0.9,mts,
,Botones,,5,millares,4,millares,80,millares,
,Etiquetas,,10,millares,1.01,millares,20,millares,
,,,,,,,,,
,Al departamento de Corte se les dio una bonificación de $ ,,,,1.1," / hora,  al departamento de costura se les aumento ",,,
,el ahorro por eficiencia que obtuvieron y al departamento de acabados un aumento de $ ,,,,,,0.2, / unidad.,

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

## Hoja: caso
Filas: 56 · Columnas: 9
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object)

Muestra (primeras 40 de 56 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8
,UTEC,,,,,,,
,CURSO,COSTOS Y PRESUPUESTOS,,,,,,
,,,,,,,,
,GUIA 4,,,,,,,
,EJERCICIO 1,,VARIACIONES ESTANDAR,,,,,
,,,,,,,,
,"Determine las variaciones de Precio, Cantidad, Eficiencia, Tasa Laboral y CIF de:",,,,,,,
,,,,,,,,
,,,ESTANDAR,,,,,
,,Producto:,,,Casaca de cuero,,,
,,Cantidad:,,,10,unidades,,
,,MATERIALES,Cantidad,,Precio ($),,Total,398.99999999999994
,, Cuero Guante,250,pies,1.3, / pie,325,
,, Napa,150,pies,0.34, / pie,51.00000000000001,
,, Forro,18,metros,0.9, / mt,16.2,
,, Botones,80,botones,0.08,unidad,6.4,
,, Etiqueta,20,unidades,0.02,unidad,0.4,
,,MANO DE OBRA,Horas,,Tarifa ($ / hora),,Total,24.5
,, Corte,0.4,,10,,4,
,, Costura,1.2,,15,,18,
,, Acabado,0.5,,5,,2.5,
,,CIF,Base,,Tasa,,Total,103.57999999999998
,, Corte,  Horas MOD,,15,,6,
,, Costura,  Costo MP,,0.22,,87.77999999999999,
,, Acabado,  Costo MO,,0.4,,9.8,
,,,,TOTAL $,,,527.0799999999999,
,,,COSTO POR UNIDAD $,,,,52.70799999999999,
,,,,,,,,
,Se trabajo un pedido de ,,500,unidades y se incurrió en los siguientes gastos y costos:,,,,
,,,Comprado,,Usado,,  Precio,
,Cuero guante,,5000,pies,5000,pies,1.2,pies
,,,10000,pies,8000,pies,1.35,pies
,Cuero napa,,5000,pies,5000,pies,0.31,pies
,,,2820,pies,2820,pies,0.35,pies
,Forro,,1000,mts,840,mts,0.9,mts
,Botones,,5,millares,4,millares,80,millares
,Etiquetas,,10,millares,1.01,millares,20,millares
,,,,,,,,
,Al departamento de Corte se les dio una bonificación de $ ,,,,1.1," / hora,  al departamento de costura se les aumento ",,
,el ahorro por eficiencia que obtuvieron y al departamento de acabados un aumento de $ ,,,,,,0.2, / unidad.

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
