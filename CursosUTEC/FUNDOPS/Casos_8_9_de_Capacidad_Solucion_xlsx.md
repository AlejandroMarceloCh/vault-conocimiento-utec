---
curso: FUNDOPS
titulo: Casos 8 - 9 de Capacidad - Solución
slides: 0
fuente: Casos 8 - 9 de Capacidad - Solución.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Casos 8 - 9 de Capacidad - Solución.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Casos 8 - 9 de Capacidad - Solución.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Caso 8
Filas: 36 · Columnas: 15
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (float64), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object)

Muestra (primeras 36 de 36 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,Proceso,Capacidad de Diseño por máquina,Unidades,Cantidad de máquinas,% Defectuosos,% Eficiencia,Capacidad Efectiva Diaria,Capacidad Real Diaria,Cantidad que Ingresa,Cantidad Producida,,Materia Prima S,Total,
,A,50,kg/hr,15,0.1,1,6000,5400,2133.333333,1920,,,,
,B,100,kg/hr,3,0.2,0.8,1920,1536,1920,1536,,460.8,1996.8,40% de lo que ingresa a C
,C,80,pz/hr,10,0.1,1,6400,5760,4992,13478.4,,,,
,D,5000,pz/día,1,0,1,5000,5000,40434.4,13478,,,,
,W,300,kg/hr,10,0.2,0.9,21600,17280,3744,2995.2,,,,
,Z,800,pz/hr,5,0,1,32000,32000,26956,26956,,,,
,Y,1000,pz/hr,4,0,1,32000,32000,26956,26956,,,,
,,,,,,,kg/dia,,,,,,,
,no tenemos la demanda,,,,,,Capacidad Efectiva  = (Capacidad de Diseño) (Eficiencia),,,,,,,
,lo procesado es igual al PT cuando no hay produtos defectuosos,,,,,,100 kg/hr x 3 maq x 80 % x 8hr/dia,,,1920,,,,
,,,,,,,,,,,,1kg de C---> 3pza en D,,
,"no sabemos cuanto se produce, 
",,,,,,Capacidad Real       = (Capacidad Efectiva) (1-%Defectuosos) ,,,,,,,
,pero el dato es que B trabaja al 100% de capacidad efectiva,,,,,,1920*(1-20%),1536,,,,2pza Y + 1 pza C --> 1pza en D,,
,,,,,,,,,,,,1pza C,13478.4,
,,,,,,,Qtotales=Qbuenos /(1-%defec),,,2133.333333,,2pza Y,26956.8,
,,,,,,,Qbuenos=Qtotales*(1-%defect),,,,,,,
,,,,,,,5k producido en B --->agregan1.5kg MP S,,,,,,40434.4,
,,,,,,,1536 KG B---> X MP S,,460.8,MP S,,,,
,,,,,,,,,,,,,,
,,,,,,,sale de B---40% de lo que ingresa a C,,,,,,,
,,,,,,,sale de W--60% de lo qie ingresa a C,,,,,,,
,,,,,,,1996.8 k de B---> 40% de lo que ingresa a C,,,,,,,
,,,,,,,X kg de W --->60% de lo que ingresa a C,,,,,,,
,,,,,,,,2995.2,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 11
count         0.0          0.0
mean          NaN          NaN
std           NaN          NaN
min           NaN          NaN
25%           NaN          NaN
50%           NaN          NaN
75%           NaN          NaN
max           NaN          NaN

## Hoja: Caso 9
Filas: 65 · Columnas: 12
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (float64), Unnamed: 10 (object), Unnamed: 11 (float64)

Muestra (primeras 40 de 65 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11
,,,,,,,,,,,
,,,,,,,,,,,
,50000,2 A,50000,3 B,50000,2 C,50000,3 D,50000.0,2 E,40000.0
,,,,,1 pieza,,,,,,
,,,,,,,,,,0.2,
,Pzas /mes,64800,,90000,,80000,,57000,,60000,
,,,,,,,,,,,
,,,,,,,,,,,
,,,,,150000,,,,,,
,150000,2 Z,,,3 piezas,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,Pzas /mes,150000,,,,,,,,,
,,,,,,,,,,,
,Proceso,A,B,C,D,E,Z,,,,
,Capacidad de diseño por máquina (piezas / hora),180,150,200,100,150,375,,,,
,% Eficiencia,90,100,100,95,100,100,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,Demanda mensual ,,39166.66667,,,,,,,,
,,,,,,,,,,,
,,,,,,,62666.66667,,,,
,62667,2 A,62667,3 b,62667, 1 w,62667,,,,
,,,,,1 pieza,,,,,,
,,,,,,,,,,,
,Pzas /mes,64800,,90000,,70000,,,,,
,,,,,,,,,,,
,,,,,188001,,,,,,
,188001,,,,,,,,,,
,,3 Z,,,3 piezas,,,,2.50668,3 maquinas Z,
,,,,,,,,,,,
,,,,,,,,,,,
,Pzas /mes,150000,,,,,,,,,
,,75000,,,,,,,,,
,Proceso,A,B,C,D,E,Z,,,,

Resumen numérico:
       Unnamed: 0    Unnamed: 9  Unnamed: 11
count         0.0      2.000000          1.0
mean          NaN  25001.253340      40000.0
std           NaN  35353.566569          NaN
min           NaN      2.506680      40000.0
25%           NaN  12501.880010      40000.0
50%           NaN  25001.253340      40000.0
75%           NaN  37500.626670      40000.0
max           NaN  50000.000000      40000.0
