---
curso: FUNDOPS
titulo: Casos resueltos
slides: 0
fuente: Casos resueltos.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Casos resueltos.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Casos resueltos.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Caso 1 - Data
Filas: 10 · Columnas: 3
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object)

Muestra (primeras 10 de 10 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2
,Factor,Porcentaje
,Necesidades personales,
,Fatiga básica ,
,Carga de 10 lb,
,Parado ,
,Posición ligeramente extraña,
,Nivel de luz ligeramente por debajo de los estándares recomendados,
,Ruidos intermitentes,
,Monotonía alta,
,Total,0

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

## Hoja: Caso 1 - Solution
Filas: 10 · Columnas: 3
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object)

Muestra (primeras 10 de 10 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2
,Factor,Porcentaje
,Necesidades personales,0.05
,Fatiga básica ,0.04
,Carga de 10 lb,0.01
,Parado ,0.02
,Posición ligeramente extraña,0
,Nivel de luz ligeramente por debajo de los estándares recomendados,0
,Ruidos intermitentes,0.02
,Monotonía alta,0.04
,Total,0.18

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

## Hoja: Caso 2 - Data
Filas: 9 · Columnas: 3
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (float64), Unnamed: 2 (object)

Muestra (primeras 9 de 9 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2
,,
TO =,8.0,min
Calificación = ,0.95,
Porcentaje de holgura = ,0.07,
Porcentaje de holgura adicional = ,0.08,
,,
TN = ,,min
TE = ,,min
TE (Recalculado) = ,,min

Resumen numérico:
       Unnamed: 1
count    4.000000
mean     2.275000
std      3.838893
min      0.070000
25%      0.077500
50%      0.515000
75%      2.712500
max      8.000000

## Hoja: Caso 2 - Solution
Filas: 11 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object)

Muestra (primeras 11 de 11 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,,,
,TO =,8.0,min
,Calificación = ,0.95,
,Porcentaje de holgura = ,0.07,
,Porcentaje de holgura adicional = ,0.08,
,,,
,TN = ,7.6,min
,FH trabajo =,1.07,
,TE = ,8.132,min
,FH trabajo (recalculado) =,1.1500000000000001,
,TE (Recalculado) = ,8.74,min

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0    9.000000
mean          NaN    3.976889
std           NaN    3.957863
min           NaN    0.070000
25%           NaN    0.950000
50%           NaN    1.150000
75%           NaN    8.000000
max           NaN    8.740000

## Hoja: Caso 3 - Data
Filas: 24 · Columnas: 12
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object)

Muestra (primeras 24 de 24 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11
,,,Observaciones (minutos por ciclo),,,,,,,,
,Element,Calificación,1,2,3.0,4.0,5.0,TO,TN,TE,
,A,0.9,1.4,1.42,1.39,1.38,1.41,,,,
,B,1.2,2.1,2.05,2.0,1.85,1.8,,,,
,C,1.1,1.6,1.4,1.5,1.45,1.55,,,,
,,,,,,,,,a.,0,minutos
,,,,,,,,,,,
,,Factor de holgura,0.1,,,,,,,,
,,,,,,,,,,,
,b. ,,,,,,,,,,
,,z =,2.33,,,,,,,,
,,h = ,0.04,,,,,,,,
,,s =,0.01581138830084191,minutes,,,,,,,
,,x =,0,minutes,,,,,,,
,,,,,,,,,,,
,,n = ,,observación,,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,c.,,,,,,,,,,
,,e =,0.1,minute,,,,,,,
,,z =,1.65,,,,,,,,
,,s = ,0.07905694150420955,,,,,,,,
,,,,,,,,,,,
,,n =,2,observaciones,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 5  Unnamed: 6  Unnamed: 7
count         0.0    4.000000    4.000000    4.000000
mean          NaN    1.972500    2.170000    2.440000
std           NaN    0.734637    1.237444    1.714273
min           NaN    1.390000    1.380000    1.410000
25%           NaN    1.472500    1.432500    1.515000
50%           NaN    1.750000    1.650000    1.675000
75%           NaN    2.250000    2.387500    2.600000
max           NaN    3.000000    4.000000    5.000000

## Hoja: Caso 3 - Solution
Filas: 26 · Columnas: 12
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object)

Muestra (primeras 26 de 26 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11
,,,Observaciones (minutos por ciclo),,,,,,,,
,Element,Calificación,1,2,3.0,4.0,5.0,TO,TN,TE,
,A,0.9,1.4,1.42,1.39,1.38,1.41,1.4,1.26,1.3860000000000001,
,B,1.2,2.1,2.05,2.0,1.85,1.8,1.9600000000000002,2.3520000000000003,2.5872000000000006,
,C,1.1,1.6,1.4,1.5,1.45,1.55,1.5,1.6500000000000001,1.8150000000000004,
,,,,,,,,,a.,5.788200000000002,minutos
,,,,,,,,,,,
,,Factor de holgura,0.1,,,,,,,,
,,,,,,,,,,,
,b. ,,,,,,,,,,
,,Nivel de Confianza =,0.98,,,,,,,,
,,z =,2.33,2.3263478740408408,,,,,,,
,,h = ,0.04,,,,,,,,
,,s =,0.01581138830084191,minutes,,,,,,,
,,x =,1.4,minutes,,,,,,,
,,,,,,,,,,,
,,n = ,1,observación,,,,,,,
,,,,,,,,,,,
,,,,,,,,,,,
,c.,,,,,,,,,,
,,Nivel de Confianza =,0.9,,,,,,,,
,,e =,0.1,minute,,,,,,,
,,z =,1.65,1.6448536269514715,,,,,,,
,,s = ,0.07905694150420955,,,,,,,,
,,,,,,,,,,,
,,n =,2,observaciones,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 5  Unnamed: 6  Unnamed: 7
count         0.0    4.000000    4.000000    4.000000
mean          NaN    1.972500    2.170000    2.440000
std           NaN    0.734637    1.237444    1.714273
min           NaN    1.390000    1.380000    1.410000
25%           NaN    1.472500    1.432500    1.515000
50%           NaN    1.750000    1.650000    1.675000
75%           NaN    2.250000    2.387500    2.600000
max           NaN    3.000000    4.000000    5.000000

## Hoja: Caso 4
Filas: 17 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object)

Muestra (primeras 17 de 17 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,Máquina,,
,n=,40.0,observaciones
,TO (máquina) =,3.3,min
,Calificación =,1.0,
,Holgura = ,0.0,
,TN (máquina),3.3,min
,TE (máquina),3.3,min
,,,
,Trabajador,,
,n=,40.0,observaciones
,TO (trabajador) = ,1.9,min
,Calificación =,1.2,
,Holgura =,0.12,del tiempo de trabajo
,TN (trabajador) = ,2.28,min
,TE (trabajador) = ,2.590909090909091,min
,,,
,TE (de la tarea) = ,5.890909090909091,min

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0   13.000000
mean          NaN    8.067832
std           NaN   14.257102
min           NaN    0.000000
25%           NaN    1.200000
50%           NaN    2.590909
75%           NaN    3.300000
max           NaN   40.000000

## Hoja: Caso 5
Filas: 13 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object)

Muestra (primeras 13 de 13 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,,,
,Holgura por descanso = ,24.0,min
,Holgura por tiempo personal =,10.0,min
,Holgura por retrasos =,14.0,min
,Holgura basada en el tiempo de trabajo =,48.0,min
,Tiempo de trabajo (horas) =,4.0,horas
,Tiempo de trabajo (min) =,240.0,min
,% Holgura en base al tiempo de trabajo =,0.2,
,,,
,TO = ,6.0,min/ciclo
,Calificación = ,0.95,
,TN =,5.699999999999999,min/ciclo
,TE = ,7.124999999999999,min/ciclo

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0   11.000000
mean          NaN   32.725000
std           NaN   70.094234
min           NaN    0.200000
25%           NaN    4.850000
50%           NaN    7.125000
75%           NaN   19.000000
max           NaN  240.000000

## Hoja: Caso 6
Filas: 22 · Columnas: 15
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (float64), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (float64), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object)

Muestra (primeras 22 de 22 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14
a.,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,Elemento de la tarea,Observaciones (minutos),,,,,,,Calificación,Holgura,TO,TN,TE,
,,1,2.0,3,4,5.0,6,7,,,,,,
,1. Seleccionar los amortiguadores correctos,4,5.0,4,6,4.0,15*,4,1.1,0.2,4.5,4.95,6.1875,
,2. Retirar el amortiguador antiguo.,6,8.0,7,6,7.0,6,7,0.9,,6.714285714285714,6.042857142857143,7.553571428571428,
,3. Soldar/instalar el nuevo amortiguador,15,14.0,14,12,15.0,16,13,1.05,,14.142857142857142,14.85,18.5625,
,4. Inspeccionar el trabajo,3,4.0,24*,5,4.0,3,18*,1,,3.8,3.8,4.749999999999999,
,5. Completar la documentación,5,6.0,8,-,7.0,6,7,1.3,,6.5,8.450000000000001,10.5625,
,,,,,,,,,,,,,47.61607142857143,min
,* El trabajador tiene conversaciones largas con el supervisor (no relacionadas con la tarea específica),,,,,,,,,,,,,
,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
b.,,,,,,,,,,,,,,
,,,,,,,,,,,,,,
,Elemento de la tarea,Observaciones (minutos),,,,,,,TO,s,z,h,n,
,,1,2.0,3,4,5.0,6,7,,,,,,
,1. Seleccionar los amortiguadores correctos,4,5.0,4,6,4.0,15*,4,4.5,0.8366600265340756,1.96,0.05,54,
,2. Retirar el amortiguador antiguo.,6,8.0,7,6,7.0,6,7,6.714285714285714,0.7559289460184563,,,20,
,3. Soldar/instalar el nuevo amortiguador,15,14.0,14,12,15.0,16,13,14.142857142857142,1.3451854182690985,,,14,
,4. Inspeccionar el trabajo,3,4.0,24*,5,4.0,3,18*,3.8,0.8366600265340751,,,75,
,5. Completar la documentación,5,6.0,8,-,7.0,6,7,6.5,1.0488088481701516,,,41,

Resumen numérico:
       Unnamed: 3  Unnamed: 6
count    12.00000   12.000000
mean      6.50000    7.000000
std       3.98862    3.954284
min       2.00000    4.000000
25%       4.00000    4.000000
50%       5.50000    6.000000
75%       8.00000    7.000000
max      14.00000   15.000000

## Hoja: Caso 7
Filas: 14 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object)

Muestra (primeras 14 de 14 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,Tiempo observado por unidad = ,280.0,segundos/unidad
,Calificación =,1.05,
,Holgura =,0.13,
,,,
,Tiempo normal por unidad = ,294.0,segundos/unidad
,Tiempo estándar por unidad = ,337.9310344827586,segundos/unidad
,Tiempo disponible por turno =,28800.0,segundos/turno
,Producción estándar por turno = ,85.0,unidades/turno
,,,
,Producción por turno de operador = ,100.0,unidades/turno
,Unidades por encima de producción estándar,15.0,unidades/turno
,Incentivo por unidad encima de producción estándar,1.0,$/unidad
,,,
,Incentivos a recibir por el operador ($),15.0,

Resumen numérico:
       Unnamed: 0    Unnamed: 2
count         0.0     11.000000
mean          NaN   2720.828276
std           NaN   8650.460906
min           NaN      0.130000
25%           NaN      8.025000
50%           NaN     85.000000
75%           NaN    287.000000
max           NaN  28800.000000

## Hoja: Caso 8
Filas: 5 · Columnas: 3
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64)

Muestra (primeras 5 de 5 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2
,,
,p = ,0.2
,z = ,2.33
,e = ,0.05
,n =,348.0

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0    4.000000
mean          NaN   87.645000
std           NaN  173.573123
min           NaN    0.050000
25%           NaN    0.162500
50%           NaN    1.265000
75%           NaN   88.747500
max           NaN  348.000000

## Hoja: Caso 9
Filas: 5 · Columnas: 16
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (float64), Unnamed: 13 (object), Unnamed: 14 (float64), Unnamed: 15 (object)

Muestra (primeras 5 de 5 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15
,,,,,,,,,,,,,,,
,Observación,1,2,3,4,5,6,7,8,9,10,,z =,1.65,
,O o D,O,O,D,O,D,O,O,O,D,O,,e = ,0.06,
,Observación,11,12,13,14,15,16,17,18,19,20,,p =,0.25,
,O o D,O,O,O,D,O,O,O,O,O,D,,n = ,142.0,observaciones

Resumen numérico:
       Unnamed: 0  Unnamed: 12  Unnamed: 14
count         0.0          0.0      4.00000
mean          NaN          NaN     35.99000
std           NaN          NaN     70.67689
min           NaN          NaN      0.06000
25%           NaN          NaN      0.20250
50%           NaN          NaN      0.95000
75%           NaN          NaN     36.73750
max           NaN          NaN    142.00000

## Hoja: Caso 10
Filas: 27 · Columnas: 4
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object)

Muestra (primeras 27 de 27 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,Número de habitaciones = ,400.0,
,Limpieza en caso de check out = ,0.5,horas
,Limpieza si no hay checkout =,0.25,horas
,Turno de trabajo = ,6.0,horas/día
,Habitaciones con check out =,200.0,
,Habitaciones sin check out =,200.0,
,Llegada al trabajo y abastecer carro = ,0.1,horas
,Empujar carro al piso =,0.1,horas
,Descanso mañana =,0.33,horas
,Almuerzo =,0.5,horas
,Reabastecer carro =,0.3,horas
,Descanso tarde =,0.33,horas
,Empujar carro de vuelta a lavandería y guardar items =,0.33,horas
,,,
,,,
a. ,Tiempo efectivo (horas) =,4.010000000000001,horas
,Tiempo efectivo (min) =,240.60000000000005,min
,,,
,,,
b.,Tiempo requerido de limpieza (horas) =,150.0,horas
,Tiempo requerido de limpieza (min) =,9000.0,min
,,,
c.,Número de empleados de limpieza requeridos =,38.0,
,,,
d. ,,,
,Tiempo requerido de limpieza si todos check out =,200.0,horas
,Número de empleados de limpieza requeridos =,50.0,

Resumen numérico:
        Unnamed: 2
count    20.000000
mean    524.567500
std    1998.169744
min       0.100000
25%       0.330000
50%       5.005000
75%     200.000000
max    9000.000000
