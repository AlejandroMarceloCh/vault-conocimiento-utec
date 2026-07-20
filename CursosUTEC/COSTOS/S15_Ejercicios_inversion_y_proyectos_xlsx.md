---
curso: COSTOS
titulo: S15 Ejercicios inversión y proyectos
slides: 0
fuente: S15 Ejercicios inversión y proyectos.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: S15 Ejercicios inversión y proyectos.xlsx. -->

<!-- INTERPRETAR: datos tabulares de S15 Ejercicios inversión y proyectos.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: 1.FOX
Filas: 92 · Columnas: 7
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (float64)

Muestra (primeras 40 de 92 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
,,,,,,
DATOS,,,,,,
,100 POLOS,1 POLO,1500 POLOS,,,
POLOS,100,1,1500,,,
COSTO,1000,10,15000,,,
VENTA,1030,10.3,15450.000000000002,,,
UTILIDAD,30,0.3000000000000007,450.0000000000018,,,
,,,,,,
a) Hallar el rendimiento que obtendría el señor Fox al invertir en el negocio del señor Morillas.,,,,,,
(se asume que en total se producen y venden 3000 polos pero el objetivo es solo evaluar el 50% del total de la inversión del señor Fox),,,,,,
,,,,15450.000000000002,,
,,,,,,
,0,1,2,3,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
Inversión:,15000,,,,,
,,,,,,
,,,,,,
CALCULO DE LA TIR,,,,,,
INVERSION,-15000,,,,,
Nper,3,,0,1,2,3.0
VF,15450.000000000002,,-15000,0,0,15450.0
TIR del proyecto,0.009901634049972694,,0.009901634049978236,,,
,,,,,,
b) Determinar si le conviene al señor Fox invertir en el negocio de su primo Valentino.,,,,,,
,,,,,,
Alternativa 2 de inversión:,,,,,,
,,,,,,
,0,1,2,3,,
Inversión :,15000,,,,,
Beneficios :,,4000,6000,9000,,
,,,,,,
,,,,,,
,,4000,6000,9000,,
,0,1,2,3,,
,,,,,,
,,,,,,
,,,,,,

Resumen numérico:
         Unnamed: 6
count      2.000000
mean    7726.500000
std    10922.678449
min        3.000000
25%     3864.750000
50%     7726.500000
75%    11588.250000
max    15450.000000

## Hoja: 2.WILSON
Filas: 52 · Columnas: 8
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64)

Muestra (primeras 40 de 52 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
2. DECISIÓN DE EXPANSIÓN,,,,,,,
William Wilson Cerámicas Perú Sac,,,,,,,
,,,,,,,
solución,,,,,,,
Cálcular el costo de la inversión,,,,,,,
,,,,,,,
Costo de adquisición del nuevo equipo,,,500000,,,,
Costo de instalación del equipo,,,20000,,,,
Costo total de la inversión,,,520000,,,,
,,,,,,,
,,,,,,,
Determinar el flujo de efectivo en los años de vida de la inversión.,,,,,,,
"El gasto por alquiler es un costo suprimido, que se presentará ya sea que se lleve a cabo o no la inversión y que por lo tanto deberá ignorarse por ser irrelevante para la decisión. ",,,,,,,
"Los gastos de producción anuales que se considerarán son servicios públicos, personal y materia prma, que dan un total de 600,000 dólares por año. ",,,,,,,
"El ingreso anual por ventas es $ 10 x 100,000 unidades de producto, o 1 000,000. El ingreso anual antes de depreciación e impuestos es entonces 1 000,000 de dólares bruto, menos 600,000 dólares de gastos, o $ 400,000 dólares. ",,,,,,,
"Luego hay que determinar los cargos por depreciación que se deducirán de los 400,000 dólares de ingresos anuales con el método de suma de dígitos de los años.",,,,,,,
(1+2+3+4+5 = 15),,,,,,,
,,,,,,,
AÑO,"PROPORCIÓN DE 500,000 QUE SE DEPRECIARÁ ",,,CARGO POR DEPRECIACIÓN,,,
1,,"5/15 x 500,000",,,166666.66666666666,,
2,,"4/15 x 500,000",,,133333.33333333334,,
3,,"3/15 x 500,000",,,100000.0,,
4,,"2/15 x 500,000",,,66666.66666666667,,
5,,"1/15 x 500,000",,,33333.333333333336,,
Depreciación acumulada,,,,,500000.0,,
,,,,,,,
Encotrar el flujo de efectivo anual cuando los impuestos son 40%. Se muestra el flujo de efectivo sólo para el primer año.,,,,,,,
,,,,,,,
,,,,,,,
Ganancias antes de depreciación e impuestos,,,,,400000.0,400000.0,400000.0
Deducir: impuestos a,,,0.4,-160000,,-160000.0,-160000.0
Sumar: Beneficio fiscal del gasto de depreciación (0.4 x 166.666.67),,,,66666.66666666667,-93333.33333333333,53333.33333333334,40000.0
Flujo de efectivo (primer año),,,,,306666.6666666667,293333.3333333334,280000.0
,,,,,,,
"Determinar el valor actual del flujo de efectivo. Como Wilson exige por lo menos una tasa de rentabilidad de 20% sobre las inversiones, se multiplican los flujos de efectivo por el factor de valor actual de 20% para cada año. Hay que usar el factor de cada uno de los años porque los flujos de efectivo  no son anualidades. (Revisar teoría factor de actualización o Valor actual (VA) en Finanzas)",,,,,,,
,,,,,,,
AÑO,Factor  de Valor actual,,Flujo de efectivo,VALOR ACTUAL,,,
1,0.8333333333333334,,306666.6666666667,,255555.5555555556,,
2,0.6944444444444444,,293333.3333333333,,203703.70370370368,,
3,0.5787037037037037,,280000,,162037.03703703705,,

Resumen numérico:
          Unnamed: 5    Unnamed: 6     Unnamed: 7
count      15.000000  4.000000e+00       4.000000
mean   221116.369456  1.466667e+05  140000.000000
std    227697.528911  2.506288e+05  249799.919936
min    -93333.333333 -1.600000e+05 -160000.000000
25%    100904.492455  7.275958e-12  -10000.000000
50%    162037.037037  1.733333e+05  160000.000000
75%    281111.111111  3.200000e+05  310000.000000
max    851706.104252  4.000000e+05  400000.000000

## Hoja: 3.BACKUS
Filas: 74 · Columnas: 7
Columnas y tipos: 3. DECISIÓN DE REEMPLAZO (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (float64), Unnamed: 6 (float64)

Muestra (primeras 40 de 74 filas, formato CSV):
3. DECISIÓN DE REEMPLAZO,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
Cervecería Backus,,,,,,
,,,,,,
solución,,,,,,
,,,,,,
Determinar el costo de la inversión,,,,,,
,,,,,,
Precio de la máquina nueva,,,,6000,,
Menos: Venta de la máquina anterior ,,,-2000,,,
 Costos de reparación evitables,,,-300,-2300,,
Costo efectivo de la inversión,,,,3700,,
,,,,,,
,,,,,,
Determinar el aumento en flujo de efectivo que se obtiene de la inversión en la máquina nueva.,,,,,,
,,,,,,
Ahorros anuales en costos,,,1200,,,
Diferencia en depreciación,,,,,,
Depreciación anual de la máquina vieja,,,,,,
,,,,,,
Costo - Desecho ,,=,4000  - 0,=,400.0,
Vida esperada,,,10,,,
,,,,,,
Depreciación anual de la máquina nueva,,,,,,
,,,,,,
Costo - Desecho ,,=,6000  - 500,=,1100.0,
Vida esperada,,,5,,,
,,,,,,
Diferencia en la depreciación :,,,(1100 -400),,700.0,
,,,,,,
Incremento neto anual de flujo de efectivo hacia la empresa:,,,,,,
,,,,,,
Ahorro en costo,,,,,,1200.0
Deducir: Impuestos a,,,,0.4,-480.0,
Sumar : Ventaja del aumento en depreciación (0.4 x 700),,,,,280.0,-200.0
Aumento anual en flujo de efectivo,,,,,,1000.0
,,,,,,
Determinar el valor neto actual de la inversión,,,,,,
El flujo de efectivo de cinco años de 1000 dólares por año es una anualidad. ,,,,,,
"con descuento de 12%, el valor actual del costo de capital es:",,,,,,
,,,,,,
Factor  de Valor actual,,Flujo anual,Flujo neto actual,,,

Resumen numérico:
        Unnamed: 5   Unnamed: 6
count     5.000000     3.000000
mean    400.000000   666.666667
std     584.978632   757.187779
min    -480.000000  -200.000000
25%     280.000000   400.000000
50%     400.000000  1000.000000
75%     700.000000  1100.000000
max    1100.000000  1200.000000

## Hoja: 4.TAYLOR
Filas: 37 · Columnas: 13
Columnas y tipos: Unnamed: 0 (float64), 5. Taylor Mountain Uranium Company (object), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (object), Unnamed: 5 (float64), Unnamed: 6 (object), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (float64), Unnamed: 11 (float64), Unnamed: 12 (float64)

Muestra (primeras 37 de 37 filas, formato CSV):
Unnamed: 0,5. Taylor Mountain Uranium Company,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12
,,,,,,,,,,,,
,Taylor Mountain Uranium Company actualmente registra ingresos anuales en efectivo por USD 1.2 millones y,,,,,,,,,,,
,egresos anuales en efectivo por 700 mil. Su depreciación asciende a USD 200 mil al año. Se espera que estas,,,,,,,,,,,
,cifras permanezcan constantes en el futuro inmediato (al menos 15 años). La tasa fiscal marginal aplicable a la,,,,,,,,,,,
,compañía es de 40%.,,,,,,,,,,,
,"Se considera la posibilidad de invertir en una nueva unidad de procesamiento de alta velocidad que cuesta USD 1.2 millones como posible inversión para elevar la capacidad de producción de la compañía. Esta nueva pieza de equipo tendrá una vida útil estimada en 10 años y un valor de rescate estimado de 0 dólares. En caso de adquirirla, se espera que los ingresos anuales de Taylor aumenten a USD 1.6 millones y que sus gastos anuales (sin contar la depreciación) se eleven a 900 mil y a su vez la depreciación anual se incremente a 320 mil. Suponga que no será necesario elevar el capital de trabajo neto como resultado de este proyecto. Calcule los flujos de efectivo netos anuales del proyecto para los próximos 10 años, dando por supuesta la compra de la nueva unidad de procesamiento. Calcule también la inversión neta de este proyecto.",,,,,,,,,,,
,,,,,,,,,,,,
,,,,,,,,,,,,
,,,,,,NUEVA UNIDAD,,,,,,
,,,,,,Inversión,,1200000,millones,,,
,,,,,,Vida util,,10,años,,,
,,,,,,Valor rescate ,,0,,,,
,,,,,,,,,,,,
,Cifras x 15 años,,,,,,,,,,,
,Ingresos actuales,,1200000.0,,,Ingresos ,,1600000,millones,,,
,Egresos actuales,,700000.0,mil,,Egresos,,900000,mil (sin depreciación),,,
,Depreciación,,200000.0,mil,,Depreciación,,320000,mil,,,
,,,,,,Analisis,,10 años,,,,
,Tasa,,0.4,,,,,,,,,
,,,,,,,,,,,,
,,,,,,,,,,,,
2.0,Flujo incremental,0.0,1.0,2,3.0,4,5.0,6,7,8.0,9.0,10.0
,Inversión adicional,-1200000.0,,,,,,,,,,
,Venta instalaciones,0.0,,,,,,,,,,
,Efecto tributario,0.0,,,,,,,,,,
,,,,,,,,,,,,
,Ingresos adicionales,,400000.0,400000,400000.0,400000,400000.0,400000,400000,400000.0,400000.0,400000.0
,Ahorro en costos operativos,,200000.0,200000,200000.0,200000,200000.0,200000,200000,200000.0,200000.0,200000.0
,Depreciación adicional,,120000.0,120000,120000.0,120000,120000.0,120000,120000,120000.0,120000.0,120000.0
,U.a.impuestos,,80000.0,80000,80000.0,80000,80000.0,80000,80000,80000.0,80000.0,80000.0
,Impuestos adicionales,,32000.0,32000,32000.0,32000,32000.0,32000,32000,32000.0,32000.0,32000.0
,,,,,,,,,,,,
,Flujo incremental,-1200000.0,48000.0,48000,48000.0,48000,48000.0,48000,48000,48000.0,48000.0,48000.0
,más depreciación,,120000.0,120000,120000.0,120000,120000.0,120000,120000,120000.0,120000.0,120000.0
,flujo Incremental financ,-1200000.0,168000.0,168000,168000.0,168000,168000.0,168000,168000,168000.0,168000.0,168000.0
,,,,,,,,,,,,
,tir,0.06637325948915973,,,,,,,,,,

Resumen numérico:
       Unnamed: 0    Unnamed: 2    Unnamed: 3     Unnamed: 5     Unnamed: 7    Unnamed: 10    Unnamed: 11    Unnamed: 12
count         1.0  7.000000e+00  1.300000e+01       9.000000       9.000000       9.000000       9.000000       9.000000
mean          2.0 -5.142857e+05  2.513847e+05  129778.111111  129778.333333  129778.666667  129778.777778  129778.888889
std           NaN  6.414270e+05  3.434174e+05  119984.778668  119984.508271  119984.102680  119983.967485  119983.832290
min           2.0 -1.200000e+06  4.000000e-01       3.000000       5.000000       8.000000       9.000000      10.000000
25%           2.0 -1.200000e+06  4.800000e+04   48000.000000   48000.000000   48000.000000   48000.000000   48000.000000
50%           2.0  0.000000e+00  1.200000e+05  120000.000000  120000.000000  120000.000000  120000.000000  120000.000000
75%           2.0  0.000000e+00  2.000000e+05  168000.000000  168000.000000  168000.000000  168000.000000  168000.000000
max           2.0  6.637326e-02  1.200000e+06  400000.000000  400000.000000  400000.000000  400000.000000  400000.000000

## Hoja: 5.THOMAS
Filas: 83 · Columnas: 7
Columnas y tipos: 7. Thoma Pharmaceutical (object), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (float64)

Muestra (primeras 40 de 83 filas, formato CSV):
7. Thoma Pharmaceutical,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
,,,,,,
"Es posible que la empresa Thoma Pharmaceutical adquiera equipo de análisis de ADN, el cual tiene un costo de $",,,,,,
"60,000. Se espera que ayudará a reducir $ 20,000 al año los costos de mano de obra del personal clínico. Este",,,,,,
"equipo tiene una vida útil de cinco años, pero para fines de recuperación del costo (depreciación), entra en la",,,,,,
categoría de propiedad de tres años. Al final no se espera ningún valor de recuperación. La tasa fiscal corporativa,,,,,,
de la empresa (estatal y federal) es de 38% y su tasa de rendimiento requerida es de 15%. (Si las utilidades,,,,,,
"después de impuestos de este proyecto son negativas en cualquier año, la compañía compensará la pérdida",,,,,,
contra el ingreso de ese año.) Con base en esta información:,,,,,,
 ¿Cuál es el valor presente neto del proyecto? ¿Es aceptable?,,,,,,
 Suponga que en el período de cuatro años se espera una inflación de 6% en el ahorro de los costos de mano,,,,,,
"de obra, de tal forma que dichos ahorros serán de $ 20,000 el primer año, de $ 21,200 el segundo y así",,,,,,
sucesivamente.,,,,,,
"- Si la tasa de rendimiento requerida sigue siendo de 15%, ¿Cuál es el valor presente neto del",,,,,,
proyecto? ¿Es aceptable?,,,,,,
"- Si hubiera un requerimiento de capital de trabajo de $ 10,000, además del costo del equipo, y se",,,,,,
"necesitara esta inversión adicional durante la vida del proyecto, ¿qué efecto tendría en el valor",,,,,,
presente?,,,,,,
,,,,,,
Inversión en equipo,60000.0,,,,,
Reducción anual de costos,20000.0,mano de obra,,,,
Vida util,5.0,AÑOS,,,,
Depreciación,3.0,AÑOS,,,,
Valor rescate ,0.0,,,,,
IR,0.38,,,,,
TASA DESCUENTO,0.15,,,,,
INFLACION,0.06,mano de obra,,,,
Horizonte,4.0,años,,,,
,,,,,,
 ¿Cuál es el valor presente neto del proyecto? ¿Es aceptable?,,,,,,
1er análisis,,1,2.0,3.0,4.0,5.0
INVERSION,-60000.0,,,,,
Ahorro incremental mano de obra,,20000,20000.0,20000.0,20000.0,20000.0
Depreciacion,,20000,20000.0,20000.0,0.0,0.0
,,,,,,
UAI,-60000.0,0,0.0,0.0,20000.0,20000.0
IMPUESTOS,,0,0.0,0.0,-7600.0,-7600.0
UTILIDAD D.IMPUESTOS,-60000.0,0,0.0,0.0,12400.0,12400.0
UTILIDAD + DEPRECIACION,-60000.0,20000,20000.0,20000.0,12400.0,12400.0
,,,,,,
VAN,-1080.765894545999,No es aceptable,,,,

Resumen numérico:
         Unnamed: 1    Unnamed: 3    Unnamed: 4    Unnamed: 5    Unnamed: 6
count     29.000000     25.000000     25.000000     25.000000     26.000000
mean  -21679.858458   6704.560000   7027.259200   6729.313152  13778.301108
std    34274.972374  11283.404931  11464.469728  12352.246917  18687.230077
min   -70000.000000 -10000.000000 -10000.000000 -10000.000000  -9051.721600
25%   -60000.000000      0.000000      0.000000      0.000000      0.000000
50%    -1080.765895    744.000000   1532.640000   4768.598400  13584.299200
75%        0.172378  20000.000000  20000.000000  14768.598400  22865.240000
max    60000.000000  21200.000000  22472.000000  23820.320000  64768.598400
