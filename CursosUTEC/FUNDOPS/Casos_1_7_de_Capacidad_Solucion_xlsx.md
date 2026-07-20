---
curso: FUNDOPS
titulo: Casos 1 - 7 de Capacidad - Solución
slides: 0
fuente: Casos 1 - 7 de Capacidad - Solución.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Casos 1 - 7 de Capacidad - Solución.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Casos 1 - 7 de Capacidad - Solución.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Caso 1
Filas: 12 · Columnas: 7
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object)

Muestra (primeras 12 de 12 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
,Laboratorio Farmaceútico S.A.A.,,,,,
,,,,,,
,ARTÍCULO,DEMANDA (KG/SEM),CAPAC. MÁXIMA (KG/HORA),CAPAC. EFECTIVA(KG/HORA),CAPAC. REAL (KG/HORA),HORAS
,A,2280,15,12,11.399999999999999,200.00000000000003
,B,1620,20,16,15.2,106.57894736842105
,C,380,25,20,19,20
,D,280,19,15.200000000000001,14.44,19.390581717451525
,E,100,25,20,19,5.2631578947368425
,,,,,TOTAL DE HORAS =,351.23268698060946
,Eficiencia =,0.8,,,TOTAL DE MÁQUINAS =,9
,% Productos Aceptables =,0.95,,,,
,Núm. Horas Sem. =,40,,,,

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

## Hoja: Caso 2
Filas: 18 · Columnas: 10
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (float64), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object)

Muestra (primeras 18 de 18 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9
,JOHAN S.A.A.,,,,,,,,
,,,,,,,,,
,Artículo,Secuencia de,Requerimiento,,OPERACIONES,A,B,C,D
,,Operaciones,Anual (und.),,Capacidad de diseño (unid/hr),100,150,120,200
,M,A-B-C-D,500000,,Eficiencia (%),0.9,0.8,0.85,0.88
,N,A-C-B-C-D,400000,,Defectuosos (%),0.05,0.06,0.06,0.04
,P,A-C-D-B,250000,,Capacidad Real (unid/hora),85.5,112.8,95.88,168.95999999999998
,,,,,Capacidad Anual (unid/año),492480,649728,552268.7999999999,973209.5999999999
,,,,,# Unidades Necesarias,1150000,1150000,1550000,1150000
,Semanas =,52,sem/año,,# Máquinas,3,2,3,2
,Días =,5,días/sem,,,2.3351202079272255,,,
,Turnos =,3,turnos/día,,,,,,
,Duración x turno =,8,horas/turno,,,,,,
,Vacaciones =,4,sem/año,,,,,,
,# Horas DisponIbles x año =,5760,horas/año,,,,,,
,,,,,,,,,
,,48,,,,,,,
,,5760,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 4
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: Caso 3
Filas: 19 · Columnas: 18
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (object), Unnamed: 17 (object)

Muestra (primeras 19 de 19 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17
,,,,,,,,,,,,,,,,,
,,,,Antes de la Mejora,,,,,,,Después de la Mejora,,,,,,
,ESTACION,Costo HM ($/h),Costo HH ($/h),% DEF.,HH/ kg,HM/kg,Cant. Ingresada-Totales (kg),HH,HM,Costo ($),% DEF.,HH/kg,HM/kg,Cant. Ingresada-Totales (kg),HH,HM,Costo ($)
,A,0.05,0.025,0.1,15,20,71042.90991759022,1065643.6487638534,1420858.1983518044,97684.00113668657,0.07,16.5,21,62881.217380368485,1037540.08677608,1320505.5649877382,91963.78041878891
,B,0.06,0.03,0.08,18,15,63938.6189258312,1150895.1406649617,959079.283887468,92071.61125319693,0.05,19.8,15.75,58479.53216374269,1157894.7368421054,921052.6315789474,90000
,C,0.04,0.02,0.15,10,20,58823.529411764706,588235.2941176471,1176470.5882352942,58823.52941176471,0.1,11,21,55555.555555555555,611111.1111111111,1166666.6666666667,58888.88888888889
,,,,,,,,2804774.0835464625,3556408.070474567,248579.1418016482,,,,,2806545.9347292962,3408224.863233352,240852.66930767777
,Cantidad Producida =,50000,kg,,,,,,,,,,,,,,
,Productividad Inicial =,0.20114318376679052,kg/$,,,,,26641.091219096335,71042.90991759022,97684.00113668657,,,,,,,
,Productividad Final =,0.2075957893417714,kg/$,,,,,34526.85421994885,57544.75703324808,92071.61125319693,,,,,,,
,Variación Product. =,0.0320796631242655,,,,,,11764.705882352942,47058.82352941177,58823.52941176471,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,71042.90991759022,,,63938.6189258312,,58823.529411764706,,,50000,PT - C,,,,
,,,,,62881.217380368485,,58479.53216374269,,55555.555555555555,,,,,,,,
,,,,,,,,,Qtotales = Qbuenos/(-%P.Def),,,0.20114318376679052,,,,,
,,,,,,15 hh/kg,,18 hh/kg,,10 hh/kg,,,,,,,
,,,,,,20 hm/kg,,15 hm/kg,,20 hm/kg,,,,,,,

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

## Hoja: Caso 4
Filas: 19 · Columnas: 11
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (float64)

Muestra (primeras 19 de 19 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,,,,,,,,,,
,,MÁQUINAS,,,,,,,,
,PARÁMETROS,A,B,C,,,,,,
,Capacidad de diseño (piezas/día),100,100,80,,,,,,
,Eficiencia (%),0.9,0.85,1,,,,,,
,Capacidad Efectiva (piezas/día),90,85,80,,,,,,
,Defectuosos (%),0,0,0.05,,,,,,
,Capacidad Real (piezas/día),90,85,76,,,,,,
,Capacidad Real (piezas/semana),450,425,380,,,,,,
a,Producción que Ingresa al Proceso,422,422,422,Qtotales,,,,,
,Producción que Sale del Proceso,422,422,400,Qbuenos,,,,,
,# Máquinas,2,1,2,,,,,,
,% Utilización,0.4688888888888889,0.9929411764705882,0.5263157894736842,,,,,,
,,,,,,,,,,
,Producción PT (Qtotales)=,400,piezas/semana,,,,,,,
,# días/semana =,5,días/semana,,,,,,,
,,,,,,,,,,
,,,,,QtotalesA,QbuenosA,QtotalesB,QbuenosB,QT=,400.0
,,,,,422,422,422,422,422,

Resumen numérico:
       Unnamed: 10
count          1.0
mean         400.0
std            NaN
min          400.0
25%          400.0
50%          400.0
75%          400.0
max          400.0

## Hoja: Caso 5
Filas: 17 · Columnas: 7
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object)

Muestra (primeras 17 de 17 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
,,,,,,
,,MÁQUINAS,,,,
,Parámetros,A,B,C,D,
,Capacidad de diseño (kg / mes),400,1500,700,400,
,Eficiencia ( % ),0.95,0.98,0.98,0.99,
,Capacidad Efectiva (kg/mes),380,1470,686,396,Cap. Diseño x eficiencia
,Defectuosos ( % ),0.02,0.03,0.02,0.02,
,Capacidad Real (kg/mes),372.4,1425.8999999999999,672.28,388.08,Cap. Efectiva x (1-%P. Defec)
,Producción que Ingresa al Proceso (kg/mes),1000,980,950.6,931.588,Q buenos/(1-%P.Defe)
a,Producción que Sale del Proceso (kg/mes),980,950.6,931.588,912.95624,Qtotales x (1-%P.Defec)
,# Máquinas,4,1,2,4,
b,% Utilización (respecto a lo ingresa al proceso),0.6578947368421053,0.6666666666666666,0.6928571428571428,0.5881237373737374,
b,% Utilización (respecto a lo que sale del proceso),0.6578947368421053,0.6666666666666667,0.6928571428571428,0.5881237373737374,
,Producción que Ingresa al Proceso (kg/mes),2000,1960,1901.2,1863.176,
,Producción que Sale del Proceso (kg/mes),1960,1901.2,1863.176,1825.91248,Qtotales x (1-%P.Defec)
c,# Máquinas,6,2,3,5,
,% Utilización (respecto a lo que sale del proceso),0.8771929824561405,0.6666666666666667,0.9238095238095239,0.9409979797979798,

## Hoja: Caso 6
Filas: 27 · Columnas: 6
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object)

Muestra (primeras 27 de 27 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
,ALIMENTO PARA AVES,,,,
,,,,,
,PROCESO,A,B,C,D
,Capacidad de diseño x máquina (kg/hora),800,2000,600,1000
,Capacidad de diseño x máquina (kg/día),19200,48000,14400,24000
,Eficiencia (%),1,0.9,0.9,1
,Capacidad Efectiva x máquina (kg/día),19200,43200,12960,24000
,Defectuosos (%),0,0.1,0.1,0.05
,Capacidad Real x máquina (kg/día),19200,38880,11664,22800
,# Máquinas,3,1,4,2
,Capacidad Efectiva Total (kg/día),57600,43200,51840,48000
,Capacidad Real Total (kg/día),57600,38880,46656,45600
,Producción que Ingresa al Proceso (= Capacidad Efectiva) (kg/día),57600,43200,38880,34992
,Producción que Sale del Proceso (kg/día),57600,38880,34992,33242.4
,,,,,
,% Utilización,1,1,0.75,0.729
,% Capacidad Ociosa,0,0,0.25,0.271
,,,,,
,# Turnos =,3,turnos,,
,Horas de Trabajo = ,8,horas/turno,,
,Capacidad por Bolsa =,50,kg,,
,# Bolsas Producidas =,664,bolsas/día,,
,Material que no se procesa en B =,14400,kg,,
,Material que no se Embolsa =,42.400000000001455,kg,,
,Material que se Desecha =,14442.400000000001,kg,,
,Costo de Materia en Proceso que se Desecha =,10,$/kg,,
,Costo Total de Desperdicio =,144424,$,,

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

## Hoja: Caso 7
Filas: 34 · Columnas: 11
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object)

Muestra (primeras 34 de 34 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,PLAYS S.A.,,,,,,,,,
,,,,,,,,,,
,,Capacidad de diseño (pz/hr),Eficiencia (%),Defectuosos (%),Capacidad Efectiva,Capacidad Real,Cantidad Ingresada,Cantidad Entregada,Nro. De Máquinas,
,MAQ. A,50,1,0.15,50,42.5,470.5882352941177,400,10,
,MAQ.B,444.44444444444446,0.9,0,400,400,400,400,2,
,MAQ.C,420,0.8,0.15,336,285.59999999999997,400,340,2,
,MAQ.D,500,1,0.15,500,425,340,289,1,
,,,,,,,,,,
,Mat. Prima por Pieza Terminada =,3,kg/pieza,,,,,,,
,M.Prima Requerida =,867,kg,,Mat. Prima Final =,532.4463749999999,kg,,1.8423749999999997,kg/unidad
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,Capacidad de Diseño (pz/hr),Eficiencia (%),Defectuosos (%),Capacidad Efectiva,Capacidad Real,Nro. De Máquinas,Cantidad Ingresada,Cantidad Entregada,
,MAQ. A,50,1,0.15,50,42.5,10,500,425,
,MAQ.W,800,1,0,800,800,1,425,425,
,MAQ.D,500,1,0.15,500,425,1,425,361,
,,,,,,,,,,
,M.Prima Requerida =,920.5499999999998,kg,,M. Prima Final =,665.0973749999998,kg,,,
,,,,,,,,,,
,,,,,,,,,,
,Kg. M. Prima Por Pieza Terminada =,2.5499999999999994,kg,,,,,,,
,,,,,,,,,,
,Ahorro de MP =,0.4500000000000006,kg,,,,,,,

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
