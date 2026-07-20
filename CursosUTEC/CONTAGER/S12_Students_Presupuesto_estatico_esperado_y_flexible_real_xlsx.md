---
curso: CONTAGER
titulo: S12 Students  Presupuesto estatico(esperado) y flexible (real)
slides: 0
fuente: S12 Students  Presupuesto estatico(esperado) y flexible (real).xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: S12 Students  Presupuesto estatico(esperado) y flexible (real).xlsx. -->

<!-- INTERPRETAR: datos tabulares de S12 Students  Presupuesto estatico(esperado) y flexible (real).xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: S9 Presup estatico
Filas: 56 · Columnas: 8
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (object)

Muestra (primeras 40 de 56 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
,ESTRUCTURA DE COSTOS:,,,,,,
,ESTANDAR UNITARIO,CANTIDAD ESTANDAR,PRECIO ESTANDAR S/.,COSTO TOTAL ESTANDAR S/.,,,
,MATERIALES DIRECTOS,5 KILOS,S/.8 POR KILO,40,,,
,MANO DE OBRA DIRECTA,2 HORAS MOD,S/.10 POR HORA MOD,20,,,
,COSTOS INDIRECTOS VARIABLES,1.5 HORAS/MAQUINA,S/.4.50 POR HORA MAQUINA,6.75,,,
,,,,,,,
,DATOS:,,,,,,
,LOS COSTOS VARIABLES PRESUPUESTADOS ASCIENDEN A S/40500 ANUALES ,,,,,,EMPRESA: TORTA LUX S.A.C
,LOS COSTOS FIJOS PRESUPUESTADOS ASCIENDEN A S/55800,,,,,,OBJETO DEL COSTO:
,EL VALOR DE VENTA DE CADA TORTA ES DE S/120,,,,,,LA TORTA
,SE HA PRESUPUESTADO UNA PRODUCCION PARA EL AÑO 2023 DE 6000 TORTAS,,,,,,
,LA BASE DE ASIGNACION QUE UTILIZA SON LAS HORAS MAQUINA ,,,,,,
,CADA TORTA REQUIERE 1.5 HORAS MAQUINA.,,,,,,
,EL RANGO RELEVANTE VA ENTRE 5800 Y 6800 TORTAS ANUALES.,,,,,,
,,,,,,,
,DESARROLLO:,,,,,,
,PASO 1 ) DETERMINAR LA TASA DE APLICACIÓN CIF VARIABLE Y CIF FIJO,,,,,,
,,,,,,,
,TASA DE APLICACIÓN = PRESUPUESTO CIF VARIABLE / PRESUPUESTO DE LA BASE DE ASIGNACION CIF VARIABLE,,,,,,
,,,,,,,
,TASA DE APLICACIÓN= 40500/ 1.5 HORA MAQUINA X 6000 TORTAS ,,,,,,
,4.5,,,,,,
,SE LEE S/4.5 SOLES POR HORA MAQUINA CIF VARIABLE,,,,,,
,,,,,,,
,TASA DE APLICACIÓN= PRESUPUESTO CIF FIJO / PRESUPUESTO DE LA BASE DE ASIGNACION CIF FIJO,,,,,,
,,,,,,,
,TASA DE APLICACIÓN= 55800/(1.5 HORA MAQUINA X 6000 TORTAS),,,,,,
,6.2,,,,,,
,SE LEE : S/6.20 SOLES POR HORA MAQUINA CIF FIJO,,,,,,
,,,,,,,
,PASO 2) DETERMINAR LA ESTRUCTURA DEL COSTO UNITARIO :,,,,,,
,,,,,,,
,ESTANDAR UNITARIO,CANTIDAD ESTANDAR,PRECIO ESTANDAR S/.,COSTO TOTAL ESTANDAR S/.,,,
,MATERIALES DIRECTOS,5 KILOS,S/.8 POR KILO,40,,,
,MANO DE OBRA DIRECTA,2 HORAS MOD,S/.10 POR HORA MOD,20,,,
,COSTOS INDIRECTOS VARIABLES,1.5 HORAS/MAQUINA,S/.4.50 POR HORA MAQUINA,6.75,,,
,COSTOS INDIRECTOS FIJOS,1.5 HORAS/MAQUINA,S/.6.20 POR HORA MAQUINA,9.3,,,
,,,,,,,
,PASO 3) ELABORAR EL PRESUPUESTO ESTATICO(esperado),,,,,,
,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 5  Unnamed: 6
count         0.0         0.0         0.0
mean          NaN         NaN         NaN
std           NaN         NaN         NaN
min           NaN         NaN         NaN
25%           NaN         NaN         NaN
50%           NaN         NaN         NaN
75%           NaN         NaN         NaN
max           NaN         NaN         NaN

## Hoja: S9 Presup flexible
Filas: 23 · Columnas: 8
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object)

Muestra (primeras 23 de 23 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
,,SUPONGA QUE AL TERMINO DEL AÑO NO SE LOGRAN VENDER LAS 6000 TORTAS,,,,,
,,SE VENDIERON SOLO 5920 TORTAS,,,,,
,,POR TANTO DEBEMOS AJUSTAR EL PRESUPUESTO A ESTE NUEVO NIVEL DE VENTAS(REAL),,,,,
,,ESTE PRESUPUESTO AJUSTADO RECIBE EL NOMBRE DE PRESUPUESTO FLEXIBLE (REAL),,,,,
,,,,,,,
,,PASO 1) ELABORAR LA ESTRUCTURA DE COSTOS (real),,,,5920,tortas vendidas en el 2023
,,,,,,,
,,,CANTIDAD ESTANDAR,PRECIO ESTANDAR S/.,COSTO TOTAL ESTANDAR S/.,,
,,MATERIALES DIRECTOS,29600,S/.8 POR KILO,236800,,
,,MANO DE OBRA DIRECTO,11840,S/.10 POR HORA MOD,118400,,
,,CIF VARIABLES,8880,S/.4.50 POR HORA MAQUINA,39960,,
,,CIF FIJOS,8880,S/.6.20 POR HORA MAQUINA,55800,*Se utiliza el CIF fijo inicial S/55800,
,,,,,,porque la cantidad de tortas realmente vendidas,
,,PASO 2 ) ELABORAR EL ESTADO DE RESULTADOS (REAL):AÑO 2023,,,,esta dentro del rango relevante,
,,,,S/.,,(5800 y 6800 unidades),
,,INGRESOS(VENTAS) ,,710400,,,
,,COSTOS VARIABLES,,395160,,,
,,MD,236800,,,,
,,MOD,118400,,,,
,,CIF VARIABLES,39960,,,,
,,MARGEN DE CONTRIBUCION TOTAL,,315240,,,
,,CIF FIJOS PRESUPUESTADOS,,55800,,,
,,UTILIDAD OPERATIVA,,259440,,,

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

## Hoja: S9 Comparacion
Filas: 20 · Columnas: 8
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), S/. (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), S/..1 (float64)

Muestra (primeras 20 de 20 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,S/.,Unnamed: 4,Unnamed: 5,Unnamed: 6,S/..1
,ESTADO DE RESULTADOS PROYECTADO 2023,,,,ESTADO DE RESULTADOS FLEXIBLE(real),,
,INGRESOS(VENTAS),,720000,,INGRESOS(VENTAS),,710400.0
,COSTOS VARIABLES,,400500,,COSTOS VARIABLES,,395160.0
,MD,240000,,,MD,236800,
,MOD,120000,,,MOD,118400,
,CIF VARIABLES,40500,,,CIF VARIABLES,39960,
,MARGEN DE CONTRIBUCION TOTAL,,319500,,MARGEN DE CONTRIBUCION TOTAL,,315240.0
,CIF FIJOS PRESUPUESTADOS,,55800,,CIF FIJOS PRESUPUESTADOS,,55800.0
,UTILIDAD OPERATIVA,,263700,,UTILIDAD OPERATIVA,,259440.0
,,,,,,,
,,S/,S/,S/,,,
,,PROYECTADO,REAL,VARIACION,ANALISIS,ACCIONES,
,INGRESOS(VENTAS),720000,710400,9600,MENOS VENTAS,PARA MEJORAR,
,COSTOS VARIABLES,400500,395160,5340,MENOS COSTOS VARIABLES,,
,MD,,,,,,
,MOD,,,,,,
,CIF VARIABLES,,,,,,
,MARGEN DE CONTRIBUCION TOTAL,319500,315240,4260,MENOR MARGEN DE CONTRIBUCION,,
,CIF FIJOS PRESUPUESTADOS,55800,55800,0,CIF IGUAL PORQUE LA CANTIDAD DE TORTAS ESTA DENTRO DEL RANGO RELEVANTE,,
,UTILIDAD OPERATIVA,263700,259440,4260,MENOR GANANCIA OPERATIVA,,

Resumen numérico:
       Unnamed: 0          S/..1
count         0.0       5.000000
mean          NaN  347208.000000
std           NaN  238669.028405
min           NaN   55800.000000
25%           NaN  259440.000000
50%           NaN  315240.000000
75%           NaN  395160.000000
max           NaN  710400.000000

## Hoja: Presup estatico
Filas: 56 · Columnas: 7
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (float64), Unnamed: 6 (object)

Muestra (primeras 40 de 56 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
,ESTRUCTURA DE COSTOS:,,,,,EMPRESA: PASTELERIA LO MAS RICO S.A.C
,ESTANDAR UNITARIO,CANTIDAD ESTANDAR,PRECIO ESTANDAR S/.,COSTO TOTAL ESTANDAR S/.,,OBJETO DEL COSTO:
,MATERIALES DIRECTOS,5 KILOS,S/.4 POR KILO,,,PIE DE MANZANA 24 PORCIONES
,MANO DE OBRA DIRECTA,1.5 HORAS MOD,S/.9 POR HORA MOD,,,
,COSTOS INDIRECTOS VARIABLES,1.5 HORAS/MAQUINA,S/.3 POR HORA MAQUINA,,,
,,,,,,
,DATOS:,,,,,
,LOS COSTOS VARIABLES PRESUPUESTADOS ASCIENDEN A S/30500 ANUALES ,,,,,
,LOS COSTOS FIJOS PRESUPUESTADOS ASCIENDEN A S/45800,,,,,
,EL VALOR DE VENTA DE CADA PIE DE MANZANA ES DE S/95,,,,,
,SE HA PRESUPUESTADO UNA PRODUCCION PARA EL AÑO 2023 DE 7000 PIE DE MANZANAS,,,,,
,LA BASE DE ASIGNACION QUE UTILIZA SON LAS HORAS MAQUINA ,,,,,
,CADA PIE DE MANZANA REQUIERE 1.5 HORAS MAQUINA.,,,,,
,EL RANGO RELEVANTE VA ENTRE 6500 Y 7200 TORTAS ANUALES.,,,,,
,,,,,,
,DESARROLLO:,,,,,
,PASO 1 ) DETERMINAR LA TASA DE APLICACIÓN CIF VARIABLE Y CIF FIJO,,,,,
,,,,,,
,TASA DE APLICACIÓN = PRESUPUESTO CIF VARIABLE / PRESUPUESTO DE LA BASE DE ASIGNACION CIF VARIABLE,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,TASA DE APLICACIÓN= PRESUPUESTO CIF FIJO / PRESUPUESTO DE LA BASE DE ASIGNACION CIF FIJO,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,PASO 2) DETERMINAR LA ESTRUCTURA DEL COSTO UNITARIO :,,,,,
,,,,,,
,ESTANDAR UNITARIO,CANTIDAD ESTANDAR,PRECIO ESTANDAR S/.,COSTO TOTAL ESTANDAR S/.,,
,MATERIALES DIRECTOS,,,,,
,MANO DE OBRA DIRECTA,,,,,
,COSTOS INDIRECTOS VARIABLES,,,,,
,COSTOS INDIRECTOS FIJOS,,,,,
,,,,,,
,PASO 3) ELABORAR EL PRESUPUESTO ESTATICO(esperado),,,,,
,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 5
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: Presup flexible
Filas: 23 · Columnas: 8
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object)

Muestra (primeras 23 de 23 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
,,SUPONGA QUE AL TERMINO DEL AÑO NO SE LOGRAN VENDER LOS 7000 PIE DE MANZANA,,,,,
,,SE VENDIERON SOLO 6550 PIE DE MANZANA,,,,,
,,POR TANTO DEBEMOS AJUSTAR EL PRESUPUESTO A ESTE NUEVO NIVEL DE VENTAS(REAL),,,,,
,,ESTE PRESUPUESTO AJUSTADO RECIBE EL NOMBRE DE PRESUPUESTO FLEXIBLE (REAL),,,,,
,,,,,,,
,,PASO 1) ELABORAR LA ESTRUCTURA DE COSTOS (real),,,,6550,tortas vendidas en el 2023
,,,,,,,
,,,CANTIDAD ESTANDAR,PRECIO ESTANDAR S/.,COSTO TOTAL ESTANDAR S/.,,
,,MATERIALES DIRECTOS,,,,,
,,MANO DE OBRA DIRECTO,,,,,
,,CIF VARIABLES,,,,,
,,CIF FIJOS,,,,*Se utiliza el CIF fijo inicial S/,
,,,,,,porque la cantidad de tortas realmente vendidas,
,,PASO 2 ) ELABORAR EL ESTADO DE RESULTADOS (REAL):AÑO 2023,,,,esta dentro del rango relevante,
,,,,S/.,,(6500 Y 7200 unidades),
,,INGRESOS(VENTAS) ,,,,,
,,COSTOS VARIABLES,,,,,
,,MD,,,,,
,,MOD,,,,,
,,CIF VARIABLES,,,,,
,,MARGEN DE CONTRIBUCION TOTAL,,,,,
,,CIF FIJOS PRESUPUESTADOS,,,,,
,,UTILIDAD OPERATIVA,,,,,

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

## Hoja: Comparacion
Filas: 20 · Columnas: 9
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), S/. (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), S/..1 (float64), Unnamed: 8 (object)

Muestra (primeras 20 de 20 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,S/.,Unnamed: 4,Unnamed: 5,Unnamed: 6,S/..1,Unnamed: 8
,ESTADO DE RESULTADOS PROYECTADO 2023,,,,ESTADO DE RESULTADOS FLEXIBLE(real),,,
,INGRESOS(VENTAS),,,,INGRESOS(VENTAS),,,
,COSTOS VARIABLES,,,,COSTOS VARIABLES,,,
,MD,,,,MD,,,
,MOD,,,,MOD,,,
,CIF VARIABLES,,,,CIF VARIABLES,,,
,MARGEN DE CONTRIBUCION TOTAL,,,,MARGEN DE CONTRIBUCION TOTAL,,,
,CIF FIJOS PRESUPUESTADOS,,,,CIF FIJOS PRESUPUESTADOS,,,
,UTILIDAD OPERATIVA,,,,UTILIDAD OPERATIVA,,,
,,,,,,,,
,,S/,S/,S/,,,,
,,PROYECTADO,REAL,VARIACION,ANALISIS,ACCIONES,,
,INGRESOS(VENTAS),,,,,PARA MEJORAR,,Escriba almenos unas 3
,COSTOS VARIABLES,,,,,,,acciones de mejora
,MD,,,,,,,
,MOD,,,,,,,
,CIF VARIABLES,,,,,,,
,MARGEN DE CONTRIBUCION TOTAL,,,,,,,
,CIF FIJOS PRESUPUESTADOS,,,,,,,
,UTILIDAD OPERATIVA,,,,,,,

Resumen numérico:
       Unnamed: 0  S/..1
count         0.0    0.0
mean          NaN    NaN
std           NaN    NaN
min           NaN    NaN
25%           NaN    NaN
50%           NaN    NaN
75%           NaN    NaN
max           NaN    NaN
