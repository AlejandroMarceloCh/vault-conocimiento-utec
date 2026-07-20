---
curso: COSTOS
titulo: S15_EJERCICIOS_INDICADORES RENTABILIDAD SOLUCION
slides: 0
fuente: S15_EJERCICIOS_INDICADORES RENTABILIDAD SOLUCION.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: S15_EJERCICIOS_INDICADORES RENTABILIDAD SOLUCION.xlsx. -->

<!-- INTERPRETAR: datos tabulares de S15_EJERCICIOS_INDICADORES RENTABILIDAD SOLUCION.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: ppt
Filas: 20 · Columnas: 16
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (float64), Unnamed: 9 (float64), Unnamed: 10 (object), Unnamed: 11 (float64), Unnamed: 12 (object), Unnamed: 13 (float64), Unnamed: 14 (float64), Unnamed: 15 (object)

Muestra (primeras 20 de 20 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15
,,,,,,,,,,Cok,0.1,,,,
,,,,,,,,,,Proyecto A,,,,,Payback
,,,,,,,,,,,0.0,1,2.0,3.0,Años
,,,,,,,,,,A,-2000.0,2000,,,1
,,,,,,,,,,A descontado,-2000.0,1818.181818181818,,,no se recupera
,,,,,,,,,,,,,,,
,,,,,,,,,,B,-2000.0,1000,1000.0,5000.0,2
,,,,,,,,,,b descontado,-2000.0,909.090909090909,826.4462809917354,3756.574004507888,2.0704000000000002
,,,,,,,,,,,,Flujo Acum,1735.5371900826444,,
,,,,,,,,,,,,Me falta,264.46280991735557,,
,,,,,,,,,,,,,,,
,,,,,,,,,,C,-2000.0,,2000.0,5000.0,2
,,,,,,,,,,c descontado,-2000.0,,1652.8925619834708,3756.574004507888,2.0924
,,,,,,,,,,,,Flujo Acum,1652.8925619834708,,
,,,,,,,,,,,,Me falta,347.10743801652916,,
,,,,,,,,,,,,,,,
,,,,,,,,,,D,-2000.0,1000,1000.0,100000.0,2
,,,,,,,,,,D descontado,-2000.0,909.090909090909,826.4462809917354,75131.48009015775,2.00352
,,,,,,,,,,,,Flujo Acum,1735.5371900826444,,
,,,,,,,,,,,,Me falta,264.46280991735557,,

Resumen numérico:
       Unnamed: 0  Unnamed: 1  Unnamed: 2  Unnamed: 3  Unnamed: 4  Unnamed: 5  Unnamed: 6  Unnamed: 7  Unnamed: 8  Unnamed: 9  Unnamed: 11  Unnamed: 13    Unnamed: 14
count         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0    10.000000    13.000000       7.000000
mean          NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN -1599.990000  1023.675779   27521.089728
std           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN   843.295125   676.499856   41675.513089
min           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN -2000.000000     2.000000       3.000000
25%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN -2000.000000   347.107438    3756.574005
50%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN -2000.000000  1000.000000    5000.000000
75%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN -2000.000000  1652.892562   40065.740045
max           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN     0.100000  2000.000000  100000.000000

## Hoja: Ejemplo 1
Filas: 15 · Columnas: 11
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (float64), Unnamed: 10 (object)

Muestra (primeras 15 de 15 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,Cok,0.15,,,,,,,,
,,0.0,1.0,2.0,3.0,4.0,,VPN,,TIR
,Proyecto A,-110000.0,55000.0,82000.0,90000.0,112000.0,,123042.69210015694,,0.5699318843674301
,Proyecto B,-110000.0,82000.0,54000.0,121000.0,62000.0,,117144.27121115208,,0.6098941723207603
,Proyecto C,-110000.0,100000.0,30000.0,74000.0,82000.0,,95180.7990966299,,0.5582155634315902
,Proyecto D,-110000.0,77000.0,82000.0,94000.0,140000.0,,160812.2826890985,,0.6967313065226346

Resumen numérico:
       Unnamed: 0     Unnamed: 2     Unnamed: 3    Unnamed: 4     Unnamed: 5     Unnamed: 6  Unnamed: 7  Unnamed: 9
count         0.0       6.000000       5.000000      5.000000       5.000000       5.000000         0.0         0.0
mean          NaN  -73333.308333   62800.200000  49600.400000   75800.600000   79200.800000         NaN         NaN
std           NaN   56803.794474   38596.225207  35224.287087   45618.924821   53263.886482         NaN         NaN
min           NaN -110000.000000       1.000000      2.000000       3.000000       4.000000         NaN         NaN
25%           NaN -110000.000000   55000.000000  30000.000000   74000.000000   62000.000000         NaN         NaN
50%           NaN -110000.000000   77000.000000  54000.000000   90000.000000   82000.000000         NaN         NaN
75%           NaN  -27500.000000   82000.000000  82000.000000   94000.000000  112000.000000         NaN         NaN
max           NaN       0.150000  100000.000000  82000.000000  121000.000000  140000.000000         NaN         NaN

## Hoja: Ejemplo 2
Filas: 13 · Columnas: 9
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (object), Unnamed: 8 (float64)

Muestra (primeras 13 de 13 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,0.0,1.0,2.0,3.0,4.0,,,
,-32000.0,-17000.0,19000.0,25000.0,36000.0,,TIR,0.18925203492566833
,,,,,,,,
,-32000.0,-19000.0,9000.0,44000.0,75000.0,,TIR,0.3435808112270573

Resumen numérico:
       Unnamed: 0    Unnamed: 1    Unnamed: 2    Unnamed: 3    Unnamed: 4    Unnamed: 5  Unnamed: 6  Unnamed: 8
count         0.0      3.000000      3.000000      3.000000      3.000000      3.000000         0.0    2.000000
mean          NaN -21333.333333 -11999.666667   9334.000000  23001.000000  37001.333333         NaN    0.266416
std           NaN  18475.208614  10440.881205   9503.402969  22066.513159  37508.025879         NaN    0.109127
min           NaN -32000.000000 -19000.000000      2.000000      3.000000      4.000000         NaN    0.189252
25%           NaN -32000.000000 -18000.000000   4501.000000  12501.500000  18002.000000         NaN    0.227834
50%           NaN -32000.000000 -17000.000000   9000.000000  25000.000000  36000.000000         NaN    0.266416
75%           NaN -16000.000000  -8499.500000  14000.000000  34500.000000  55500.000000         NaN    0.304999
max           NaN      0.000000      1.000000  19000.000000  44000.000000  75000.000000         NaN    0.343581

## Hoja: Ejemplo 3
Filas: 29 · Columnas: 11
Columnas y tipos: Dato: (object), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object)

Muestra (primeras 29 de 29 filas, formato CSV):
Dato:,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
CoK,0.12,,,,,,,,,
,0,1.0,2.0,3.0,4.0,TIR,CoK,,P. R,
Proyecto A,-100000,50000.0,80000.0,96000.0,110000.0,0.6192647107123257,0.12,0.4992647107123257,1.625,
,F.acum,50000.0,,,,,,,,
,Falta,50000.0,,,,,,,,
Proyecto B,-100000,80000.0,50000.0,116000.0,60000.0,0.6565434146834757,0.12,0.5365434146834757,1.4,
,F.acum,80000.0,,,,,,,,
,Falta,20000.0,,,,,,,,
Proyecto C,-100000,100000.0,30000.0,76000.0,80000.0,0.6438455072445408,0.12,0.5238455072445408,1,Se elige el menor P.R
Proyecto D,-100000,70000.0,80000.0,96000.0,100000.0,0.7031176161521293,0.12,0.5831176161521293,1.375,
,F.acum,70000.0,,,,,,,,
,Falta,30000.0,,,,,,,,
,,,,,,,,,,
,,,,,,,,,,
,0,1.0,2.0,3.0,4.0,VAN,P.R.D,VAN,,
Proyecto A,-100000,44642.85714285714,63775.51020408162,68330.90379008744,69906.98862453143,146656.25976155762,,146656.2597615576,,
Proyecto B,-100000,71428.57142857142,39859.69387755101,82566.50874635566,38131.08470428987,131985.85875676794,,131985.85875676796,,
Proyecto C,-100000,89285.71428571428,23915.81632653061,54095.29883381923,50841.44627238649,118138.2757184506,,118138.2757184506,,
Proyecto D,-100000,62499.99999999999,63775.51020408162,68330.90379008744,63551.80784048312,158158.22183465218,,158158.22183465215,,
,,,,,,,,,,
,,,,,,,,,,
PAYBACK DESCONTADO,,,,,,,,,,
,0,1.0,2.0,3.0,4.0,,,,,
Proyecto A,,1.8679977600000002,,,,,,,,
Proyecto B,,1.716789248,,,,,,,,
Proyecto C,,1.4479880533333334,,,,,,,,
Proyecto D,,1.16799552,,,,,,,,
,,,,,,,,,,
Con payback descontado la mejor opcion seria el proyecto D,,,,,,,,,,

Resumen numérico:
          Unnamed: 2    Unnamed: 3     Unnamed: 4     Unnamed: 5
count      21.000000     11.000000      11.000000      11.000000
mean    41326.968744  39212.048237   59757.510469   52040.302495
std     35004.948965  30954.742586   41791.379426   39082.640322
min         1.000000      2.000000       3.000000       4.000000
25%         1.716789  11958.908163   27049.149417   19067.542352
50%     50000.000000  39859.693878   68330.903790   60000.000000
75%     70000.000000  63775.510204   89283.254373   74953.494312
max    100000.000000  80000.000000  116000.000000  110000.000000

## Hoja: Ejemplo 4
Filas: 64 · Columnas: 6
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object)

Muestra (primeras 40 de 64 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
Ejemplo 4,,,,,
EJERCICIO TABLA,,,,,
"Considera los proyectos de inversión de la siguiente TABLA (valores en miles de
euros)",,,,,
,,Flujo de fondos anuales,,,
,Desembolso inicial,Año 1,Año 2,Año 3,Año 4
Proyecto A,200,70,70,60,60
Proyecto B,120,50,50,50,0
,,,,,
Se pide:,,,,,
a) Calcular el valor actual neto de ambos proyectos para una tasa de descuento del 10%.,,,,,
b) Calcular el plazo de recuperación de cada uno de los proyectos.,,,,,
"c) Atendiendo a los resultados de los apartados anteriores, explicar cuál de los dos
proyectos sería preferible.",,,,,
,,,,,
a) Calcular el valor actual neto de ambos proyectos para una tasa de descuento del 10%.,,,,,
,,,,,
,Desembolso inicial,Año 1,Año 2,Año 3,Año 4
Proyecto A,-200,70,70,60,60
,,,,,
Tasa =,0.1,,,,
,,,,,
,VAN(A),7.547298681783985,,,
,,,,,
,,,,,
,Desembolso inicial,Año 1,Año 2,Año 3,Año 4
Proyecto B,-120,50,50,50,0
,,,,,
Tasa =,0.1,,,,
,,,,,
,VAN(B),4.342599549211116,,,
,,,,,
b) Calcular el plazo de recuperación de cada uno de los proyectos.,,,,,
,,,,,
,,,,,
,,,,,
,,,,,
,,,,,
,,,,,
,Desembolso inicial,Año 1,Año 2,Año 3,Año 4
Proyecto A,-200,70,70,60,60
Acumulado ,-200,-130,-60,0,60

## Hoja: Ejemplo 5
Filas: 61 · Columnas: 6
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object)

Muestra (primeras 40 de 61 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
Ejemplo 5,,,,,
EJERCICIO DECIDIR,,,,,
Una empresa debe DECIDIR entre dos proyectos de inversión de cuatro año de duración. Ambos proyectos requieren un desembolso inicial de 5.000 euros y generan los siguientes flujos de caja anuales (en euros):,,,,,
,,,,,
,,,,,
proyecto,Año 1,Año 2,Año 3,Año 4,
A,2000,1000,2000,8000,
B,3000,0,2600,5500,
,,,,,
Se pide:,,,,,
"a) Determinar qué proyecto es preferible de acuerdo con el criterio del plazo de
recuperación o pay-back.",,,,,
"b) Sabiendo que el coste de capital es del 7%, determinar qué proyecto es preferible Según el criterio del Valor Actual Neto.",,,,,
"c) ¿Cuál de los dos criterios anteriores consideras más adecuado? Justifica la
respuesta. ",,,,,
,,,,,
,,,,,
,,,,,
"a) Determinar qué proyecto es preferible de acuerdo con el criterio del plazo de
recuperación o pay-back.",,,,,
,,,,,
,,,,,
,,,,,
,,,,,
,,,,,
,,,,,
,,,,,
,,,,,
proyecto,Año 0,Año 1,Año 2,Año 3,Año 4
A,-5000,2000,1000,2000,8000
acumulado,-5000,-3000,-2000,0,8000
,,,,,
periodo último con flujo acumulado negativo,,,,2,
Valor absoluto del último flujo acumulado negativo,,,,2000,
valor flujo de caja en el siguiente periodo,,,,2000,
,,,,,
,Periodo de recuperación =,,,3,
,Periodo de recuperación =,,,3 años,
,,,,,
,,,,,
proyecto,Año 0,Año 1,Año 2,Año 3,Año 4
B,-5000,3000,0,2600,5500
acumulado,-5000,-2000,-2000,600,6100

## Hoja: Ejemplo 6
Filas: 61 · Columnas: 8
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object)

Muestra (primeras 40 de 61 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
Ejemplo 6,,,,,,,
ANALIZA,,,,,,,
"Una empresa ANALIZA dos proyectos de inversión de los que dispone de la siguiente
información (valores en euros):",,,,,,,
,,,,,,,
Proyecto ,Desembolso inicial,Pagos año 1 ,Cobros año 1,Pagos año 2 ,Cobros año 2,Pagos año 3 ,Cobros año 3
A,20000,3000,13000,10000,25000,2000,0
B,80000,5000,30500,10000,14500,0,90000
,,,,,,,
Se pide:,,,,,,,
a) Calcular el pay-back o plazo de recuperación de ambos proyectos explicando cuál sería preferible según este criterio.,,,,,,,
"b) Calcular el Valor Actual Neto (VAN) de los dos proyectos suponiendo una tasa de
actualización del 10%.",,,,,,,
"c) ¿Cuál de los dos proyectos sería preferible según el criterio del VAN? ¿Qué criterio
sería preferible?",,,,,,,
,,,,,,,
,,,,,,,
a) Calcular el pay-back o plazo de recuperación de ambos proyectos explicando cuál sería preferible según este criterio.,,,,,,,
,,,,,,,
Proyecto A,Desembolso inicial,año 1,año 2,año 3,,,
salidas,-20000,-3000,-10000,-2000,,,
entradas,0,13000,25000,0,,,
flujo,-20000,10000,15000,-2000,,,
acumulado,-20000,-10000,5000,3000,,,
,,,,,,,
periodo último con flujo acumulado negativo,,,,1,,,
Valor absoluto del último flujo acumulado negativo,,,,10000,,,
valor flujo de caja en el siguiente periodo,,,,15000,,,
,,,,,,,
,Periodo de recuperación =,,,1.6666666666666665,,,
,Periodo de recuperación =,,,"1 años, 8 meses y 1 día",,,
,,,,,,,
,,,,,,,
Proyecto B ,Desembolso inicial,año 1,año 2,año 3,,,
salidas,-80000,-5000,-10000,0,,,
entradas,0,30500,14500,90000,,,
flujo,-80000,25500,4500,90000,,,
acumulado,-80000,-54500,-50000,40000,,,
,,,,,,,
periodo último con flujo acumulado negativo,,,,2,,,
Valor absoluto del último flujo acumulado negativo,,,,50000,,,
valor flujo de caja en el siguiente periodo,,,,90000,,,
,,,,,,,

## Hoja: Ejemplo 7
Filas: 56 · Columnas: 6
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object)

Muestra (primeras 40 de 56 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
Ejemplo 7,,,,,
HIPOTÉTICA,,,,,
"Una empresa ANALIZA dos proyectos de inversión de los que dispone de la siguiente
información (valores en euros):",,,,,
,,,,,
,Desembolso inicial,Año 1,Año 2,Año 3,Año 4
Proyecto A,790000,400000,380000,120000,0
Proyecto B,1000000,300000,350000,250000,300000
,,,,,
Se pide:,,,,,
a) Calcular el pay-back o plazo de recuperación de ambos proyectos e indicar cuál de los dos escogería un inversor que utilizara este criterio de selección de inversiones.,,,,,
Razona la respuesta,,,,,
"b) Calcular el Valor Actual Neto (VAN) de los proyectos A y B suponiendo que la tasa
de actualización aplicable es del 8%.",,,,,
"c) Basándote en el criterio del VAN indica cuál de los dos proyectos sería preferible.
Justifica tu respuesta.",,,,,
,,,,,
,,,,,
a) Calcular el pay-back o plazo de recuperación de ambos proyectos e indicar cuál de los dos escogería un inversor que utilizara este criterio de selección de inversiones.,,,,,
,,,,,
,Desembolso inicial,Año 1,Año 2,Año 3,Año 4
Proyecto A,-790000,400000,380000,120000,0
acumulado,-790000,-390000,-10000,110000,110000
,,,,,
periodo último con flujo acumulado negativo,,,,2,
Valor absoluto del último flujo acumulado negativo,,,,10000,
valor flujo de caja en el siguiente periodo,,,,120000,
,,,,,
,Periodo de recuperación =,,,2.0833333333333335,
,Periodo de recuperación =,,,2 años y 1 mes,
,,,,,
,Desembolso inicial,Año 1,Año 2,Año 3,Año 4
Proyecto B,-1000000,300000,350000,250000,300000
acumulado,-1000000,-700000,-350000,-100000,200000
,,,,,
periodo último con flujo acumulado negativo,,,,3,
Valor absoluto del último flujo acumulado negativo,,,,100000,
valor flujo de caja en el siguiente periodo,,,,300000,
,,,,,
,Periodo de recuperación =,,,3.3333333333333335,
,Periodo de recuperación =,,,3 años y 4 meses.,
,,,,,
Según el criterio del pay-back sería preferible el proyecto A porque recupera antes el,,,,,

## Hoja: Ejemplo 8
Filas: 25 · Columnas: 4
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 25 de 25 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
Ejemplo 8,,,
EJERCICIO INVERSIÓN,,,
"Un proyecto de inversión requiere un desembolso inicial de 20.000 euros y dura dos
años. En el primer año genera unos cobros de 20.000 euros y en el segundo de
40.000 euros. Además, es necesario realizar unos pagos de 10.000 euros el primer
año y 20.000 el segundo. La tasa de descuento aplicable a esta inversión es del 12%.
Se pide:",,,
a) Calcular el Valor Actual Neto de esta inversión,,,
b) Determinar la Tasa de Rentabilidad Interna de la inversión,,,
"c) Atendiendo a los resultados de los apartados anteriores, ¿realizarías esta inversión? Razona tu respuesta",,,
,,,
a) Calcular el Valor Actual Neto de esta inversión,,,
,,,
,Inicial,año 1,año 2
inversión,-20000,,
ingresos,,20000,40000
pagos,,-10000,-20000
flujo,-20000,10000,20000
,,,
tasa=,0.12,,
,,,
,VAN =,4872.448979591831,
,,,
b) Determinar la Tasa de Rentabilidad Interna de la inversión,,,
,,,
,TIR=,0.2807764064042064,
,,,
"c) Atendiendo a los resultados de los apartados anteriores, ¿realizarías esta inversión? Razona tu respuesta",,,
"Sí realizaría esta inversión ya que supera la rentabilidad exigida (tasa de descuento
aplicable). Según el enunciado, la tasa de descuento es de un 12% y la rentabilidad
real de la inversión es de un 28,08%, criterio necesario para que, según el criterio de
la TIR, sea un proyecto viable. Según el criterio del VAN, al ser éste mayor que cero,
es viable.",,,

## Hoja: Ejemplo 9
Filas: 27 · Columnas: 4
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 27 de 27 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
Ejemplo 9,,,
 EJERCICIO DIRECTOR,,,
"Supón que eres el director financiero de una empresa que está valorando la
posibilidad de desarrollar un proyecto de inversión de dos años de duración. El
proyecto requiere la realización de un desembolso inicial de 6.000 euros y se espera
que genere unos flujos de caja de 5.000 euros el primer año y 1.400 euros el
segundo año. Sabiendo que el tipo de interés es del 10%, se pide:",,,
,,,
a) Calcular el VAN del proyecto.,,,
b) Calcular la tasa de rentabilidad interna (TIR) del proyecto,,,
c) Interpretar los resultados y evaluar la viabilidad del proyecto,,,
,,,
solución,,,
a) Calcular el VAN del proyecto.,,,
,,,
,,,
,inicial,año 1,año 2
flujo,-6000,5000,1400
,,,
tasa =,0.1,,
,,,
,VAN =,-297.52066115702564,
,,,
,,,
b) Calcular la tasa de rentabilidad interna (TIR) del proyecto,,,
,,,
,TIR =,0.05458864030015431,
,,,
,,,
c) Interpretar los resultados y evaluar la viabilidad del proyecto,,,
"El VAN refleja la diferencia entre el desembolso inicial y el valor actualizado de los
flujos netos de caja que genera el proyecto de inversión. Como este valor es
negativo, el proyecto no es viable. Además, el valor de la TIR es inferior al coste del
dinero, por lo tanto, con arreglo a este criterio tampoco seria realizable el proyecto",,,

## Hoja: Ejemplo 10
Filas: 24 · Columnas: 4
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 24 de 24 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
Ejemplo 10,,,
EJERCICIO DETERMINADA,,,
"Una determinada empresa tiene que decidir sobre la oportunidad de llevar a cabo un
proyecto de inversión que supone realizar un desembolso inicial de 8 millones de
euros. El proyecto tiene una duración estimada de dos años y la empresa estima que
el proyecto le proporcionará unos flujos netos de caja de 4 millones el primer año y
de 5 millones el segundo año. Se pide:
",,,
a) Calcular la Tasa Interna de Rentabilidad (TIR) del proyecto.,,,
b) Calcular el Valor Actual Neto (VAN) del proyecto si el coste del dinero es del 12%.,,,
"c) Tomando como referencia los resultados de los apartados anteriores, valorar la
conveniencia o no de llevar a cabo dicho proyecto.",,,
SOLUCION,,,
,,,
a) Calcular la Tasa Interna de Rentabilidad (TIR) del proyecto.,,,
,,,
,INICIAL,AÑO 1,AÑO 2
FLUJO,-8000000,4000000,5000000
,,,
TIR =,0.07915619758884995,,
,,,
,,,
,,,
b) Calcular el Valor Actual Neto (VAN) del proyecto si el coste del dinero es del 12%.,,,
,,,
VAN =,-442602.0408163285,,
,,,
,,,
"c) Tomando como referencia los resultados de los apartados anteriores, valorar la
conveniencia o no de llevar a cabo dicho proyecto.",,,
"No es conveniente realizar el proyecto porque la TIR (8%) es inferior al coste del
dinero (12%) y el VAN es negativo.",,,

## Hoja: Hoja1
Filas: 0 · Columnas: 0
Columnas y tipos: 

Muestra (primeras 0 de 0 filas, formato CSV):
