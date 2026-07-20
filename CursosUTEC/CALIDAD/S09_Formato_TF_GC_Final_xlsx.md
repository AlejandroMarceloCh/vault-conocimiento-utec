---
curso: CALIDAD
titulo: S09_Formato_TF_GC_Final
slides: 0
fuente: S09_Formato_TF_GC_Final.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: S09_Formato_TF_GC_Final.xlsx. -->

<!-- INTERPRETAR: datos tabulares de S09_Formato_TF_GC_Final.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Características del Proyecto
Filas: 8 · Columnas: 3
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object)

Muestra (primeras 8 de 8 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2
,,
,,
,CASO : SERVICIOS LOGISTICOS,
,,
,,
,Alcance: ,Proceso de Despacho a canal moderno
,Objetivo: ,Reducir la cantidad de despachos rechazados en un 70%
,Impacto,320000

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

## Hoja: DPMO
Filas: 27 · Columnas: 27
Columnas y tipos: Pregunta (object), Especificación (object), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), VALORES REALES (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (float64), VALORES OBJETIVOS (object), Unnamed: 16 (object), Unnamed: 17 (object), Unnamed: 18 (object), Unnamed: 19 (object), Unnamed: 20 (object), Unnamed: 21 (object), Unnamed: 22 (object), Unnamed: 23 (float64), Unnamed: 24 (object), Unnamed: 25 (float64), Unnamed: 26 (object)

Muestra (primeras 27 de 27 filas, formato CSV):
Pregunta,Especificación,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,VALORES REALES,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,VALORES OBJETIVOS,Unnamed: 16,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20,Unnamed: 21,Unnamed: 22,Unnamed: 23,Unnamed: 24,Unnamed: 25,Unnamed: 26
PROCESO:,Despacho a clientes de Canal Moderno,,,,,Día,Servicios,Defectos,Oportunidades,DPMO,DPU,Prob_Falla,SIGMA,,Día,Servicios,Defectos,Oportunidades,DPMO,DPU,Prob_Falla,SIGMA,,IMPACTO,,OBJETIVO
QUE SE PRODUCE:,Servicio de despacho,,,,,2014-09-01 00:00:00,195,10,4,12820.51282051282,0.05128205128205128,0.01282051282051282,3.731605835260923,,2014-09-01 00:00:00,195,1.1699999999999982,4,1499.9999999999977,0.005999999999999991,0.0014999999999999976,4.467737925341783,,44150.00000000001,0.8830000000000002,38984.45000000002
REQUISITOS:,Producto solicitado,,,,,2014-09-02 00:00:00,495,39,4,19696.969696969696,0.07878787878787878,0.019696969696969695,3.5600481348732176,,2014-09-02 00:00:00,495,2.9700000000000006,4,1500.0000000000002,0.006000000000000001,0.0015000000000000002,4.467737925341783,,180150,0.9238461538461539,166430.88461538462
,Producto optimo,,,,,2014-09-03 00:00:00,495,40,4,20202.020202020205,0.08080808080808081,0.020202020202020204,3.5495942663939903,,2014-09-03 00:00:00,495,2.9699999999999918,4,1499.999999999996,0.005999999999999984,0.001499999999999996,4.467737925341783,,185150.00000000003,0.9257500000000002,171402.61250000005
,Cantidad solicitada,,,,,2014-09-04 00:00:00,607,38,4,15650.741350906095,0.06260296540362438,0.015650741350906095,3.6532188526531586,,2014-09-04 00:00:00,607,3.6420000000000012,4,1500.0000000000005,0.006000000000000002,0.0015000000000000005,4.467737925341783,,171789.99999999997,0.904157894736842,155325.28473684206
,Documentación,,,,,2014-09-05 00:00:00,599,30,4,12520.868113522538,0.05008347245409015,0.012520868113522538,3.7407582876133585,,2014-09-05 00:00:00,599,3.594000000000001,4,1500.0000000000005,0.006000000000000002,0.0015000000000000005,4.467737925341783,,132030,0.8802,116212.806
OPORTUNIDADES DE DEFECTO:,Producto cruzado,,,,,2014-09-07 00:00:00,471,40,4,21231.422505307855,0.08492569002123142,0.021231422505307854,3.5289552842642076,,2014-09-07 00:00:00,471,2.8260000000000023,4,1500.0000000000011,0.0060000000000000045,0.0015000000000000011,4.467737925341783,,185870,0.92935,172738.2845
,Producto dañado,,,,,2014-09-08 00:00:00,373,24,4,16085.790884718499,0.064343163538874,0.0160857908847185,3.642272234418901,,2014-09-08 00:00:00,373,2.2379999999999995,4,1499.9999999999995,0.005999999999999998,0.0014999999999999996,4.467737925341783,,108810,0.9067500000000001,98663.4675
,Incompleto,,,,,2014-09-09 00:00:00,542,42,4,19372.693726937272,0.07749077490774908,0.01937269372693727,3.566880798812089,,2014-09-09 00:00:00,542,3.251999999999999,4,1499.9999999999993,0.0059999999999999975,0.0014999999999999994,4.467737925341783,,193740.00000000003,0.9225714285714287,178738.98857142864
,Documentación incompleta y/o errónea,,,,,2014-09-10 00:00:00,629,42,4,16693.163751987282,0.06677265500794913,0.016693163751987282,3.6274064403077406,,2014-09-10 00:00:00,629,3.773999999999999,4,1499.9999999999995,0.005999999999999998,0.0014999999999999996,4.467737925341783,,191130,0.9101428571428571,173955.60428571427
,,,,,,2014-09-11 00:00:00,605,47,4,19421.487603305784,0.07768595041322314,0.019421487603305785,3.565846506639168,,2014-09-11 00:00:00,605,3.629999999999999,4,1499.9999999999995,0.005999999999999998,0.0014999999999999996,4.467737925341783,,216850.00000000003,0.9227659574468086,200101.79787234045
,,,,,,2014-09-12 00:00:00,564,42,4,18617.021276595744,0.07446808510638298,0.018617021276595744,3.5831885261436334,,2014-09-12 00:00:00,564,3.3839999999999986,4,1499.9999999999993,0.0059999999999999975,0.0014999999999999994,4.467737925341783,,193080,0.9194285714285714,177523.26857142855
,,,,,,2014-09-14 00:00:00,551,36,4,16333.938294010888,0.06533575317604355,0.016333938294010888,3.636141566536129,,2014-09-14 00:00:00,551,3.3060000000000045,4,1500.000000000002,0.006000000000000008,0.001500000000000002,4.467737925341783,,163469.99999999997,0.9081666666666666,148458.00499999995
,,,,,,2014-09-15 00:00:00,412,20,4,12135.922330097088,0.04854368932038835,0.012135922330097087,3.7527986928495674,,2014-09-15 00:00:00,412,2.4719999999999978,4,1499.9999999999986,0.005999999999999995,0.0014999999999999987,4.467737925341783,,87640.00000000001,0.8764000000000001,76807.69600000003
,,,,,,2014-09-16 00:00:00,555,51,4,22972.972972972973,0.0918918918918919,0.022972972972972974,3.495889554411394,,2014-09-16 00:00:00,555,3.3299999999999947,4,1499.9999999999977,0.005999999999999991,0.0014999999999999976,4.467737925341783,,238350,0.9347058823529412,222787.14705882352
,,,,,,2014-09-17 00:00:00,616,31,4,12581.168831168832,0.05032467532467533,0.012581168831168832,3.738901318860144,,2014-09-17 00:00:00,616,3.6959999999999997,4,1499.9999999999998,0.005999999999999999,0.0014999999999999998,4.467737925341783,,136520,0.8807741935483872,120243.29290322581
,,,,,,2014-09-18 00:00:00,628,44,4,17515.92356687898,0.07006369426751592,0.01751592356687898,3.607990084358506,,2014-09-18 00:00:00,628,3.767999999999999,4,1499.9999999999995,0.005999999999999998,0.0014999999999999996,4.467737925341783,,201160,0.9143636363636364,183933.3890909091
,,,,,,2014-09-19 00:00:00,577,32,4,13864.818024263432,0.05545927209705372,0.01386481802426343,3.7010902406283273,,2014-09-19 00:00:00,577,3.461999999999996,4,1499.9999999999984,0.005999999999999993,0.0014999999999999983,4.467737925341783,,142690.00000000003,0.8918125000000001,127252.72562500005
,,,,,,2014-09-21 00:00:00,564,104,4,46099.29078014184,0.18439716312056736,0.04609929078014184,3.183912493090681,,2014-09-21 00:00:00,564,3.3839999999999986,4,1499.9999999999993,0.0059999999999999975,0.0014999999999999994,4.467737925341783,,503080,0.9674615384615385,486710.55076923076
,,,,,,2014-09-22 00:00:00,396,21,4,13257.575757575758,0.05303030303030303,0.013257575757575758,3.718582348562772,,2014-09-22 00:00:00,396,2.3759999999999994,4,1499.9999999999995,0.005999999999999998,0.0014999999999999996,4.467737925341783,,93120.00000000001,0.886857142857143,82584.13714285717
,,,,,,2014-09-23 00:00:00,621,46,4,18518.51851851852,0.07407407407407407,0.018518518518518517,3.5853555660318284,,2014-09-23 00:00:00,621,3.726000000000001,4,1500.0000000000002,0.006000000000000001,0.0015000000000000002,4.467737925341783,,211370,0.919,194249.03
,,,,,,2014-09-24 00:00:00,620,52,4,20967.74193548387,0.08387096774193549,0.020967741935483872,3.5341598235266827,,2014-09-24 00:00:00,620,3.7199999999999953,4,1499.9999999999982,0.005999999999999992,0.001499999999999998,4.467737925341783,,241400,0.9284615384615384,224130.61538461538
,,,,,,2014-09-25 00:00:00,645,49,4,18992.248062015504,0.07596899224806201,0.018992248062015504,3.5750219971576223,,2014-09-25 00:00:00,645,3.870000000000001,4,1500.0000000000005,0.006000000000000002,0.0015000000000000005,4.467737925341783,,225649.99999999997,0.9210204081632652,207828.25510204077
,,,,,,2014-09-26 00:00:00,587,38,4,16183.986371379897,0.06473594548551959,0.016183986371379896,3.639836618544174,,2014-09-26 00:00:00,587,3.5220000000000002,4,1500,0.006,0.0015,4.467737925341783,,172390,0.9073157894736843,156412.16894736842
,,,,,,2014-09-28 00:00:00,489,38,4,19427.402862985688,0.07770961145194274,0.019427402862985686,3.565721269949271,,2014-09-28 00:00:00,489,2.934000000000001,4,1500.0000000000005,0.006000000000000002,0.0015000000000000005,4.467737925341783,,175330,0.9227894736842106,161792.67842105264
,,,,,,2014-09-29 00:00:00,398,23,4,14447.236180904523,0.05778894472361809,0.014447236180904523,3.684923278800996,,2014-09-29 00:00:00,398,2.3880000000000035,4,1500.0000000000023,0.006000000000000009,0.0015000000000000022,4.467737925341783,,103059.99999999997,0.896173913043478,92359.68347826082
,,,,,,2014-09-30 00:00:00,652,31,4,11886.503067484664,0.04754601226993865,0.011886503067484663,3.7607780233310804,,2014-09-30 00:00:00,652,3.912000000000001,4,1500.0000000000002,0.006000000000000001,0.0015000000000000002,4.467737925341783,,135440,0.8738064516129033,118348.34580645162

Resumen numérico:
       Unnamed: 2  Unnamed: 3  Unnamed: 4  Unnamed: 5  Unnamed: 14  Unnamed: 23  Unnamed: 25
count         0.0         0.0         0.0         0.0          0.0          0.0    26.000000
mean          NaN         NaN         NaN         NaN          NaN          NaN     0.909887
std           NaN         NaN         NaN         NaN          NaN          NaN     0.021804
min           NaN         NaN         NaN         NaN          NaN          NaN     0.873806
25%           NaN         NaN         NaN         NaN          NaN          NaN     0.892903
50%           NaN         NaN         NaN         NaN          NaN          NaN     0.912253
75%           NaN         NaN         NaN         NaN          NaN          NaN     0.922784
max           NaN         NaN         NaN         NaN          NaN          NaN     0.967462

## Hoja: SIPOC
Filas: 46 · Columnas: 18
Columnas y tipos: Unnamed: 0 (float64), CARACTERIZACIÓN DE LOS PROCESOS - SIPOC (object), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (float64), Unnamed: 12 (float64), Unnamed: 13 (object), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (float64), Unnamed: 17 (object)

Muestra (primeras 40 de 46 filas, formato CSV):
Unnamed: 0,CARACTERIZACIÓN DE LOS PROCESOS - SIPOC,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16,Unnamed: 17
,,,,,,,,,,,,,CÓDIGO,:,001,,
,,,,,Proceso:,PROCESO DE DESPACHO,,,,,,,,,,,
,,,,,Area:,JEFATURA OPERACIONES,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,
,Proveedores,,,Entradas,,,,Procesos,,,,,Salidas,,Clientes,,
,,,,,,,,,,GENERA VALOR,,,,,,,
,Comercial,,,Entradas controladas,,,,,ACTIVIDAD ,,,,Pedidos Despachados,,Autoservicios,,
,Plantas productivas,,,Pedidos de ventas,,,,1,Verificación stock fisico-sistema,NO,,,Guia de Remisión,,Cuentas Claves,,
,Almacén Pulmón,,,Mercadería de Planta,,,,2,Cuadrar stock,NO,,,Factura,,Insituciones,,
,,,,,,,,3,Migración stock SAP a BASIC,NO,,,Boletas de cambio,,Distribidones,,
,,,,,,,,4,Coordinar pedidos con Comercial,NO,,,Orden de Compra,,,,
,,,,Entradas no controladas,,,,5,Descargar pedidos Hen Help a Basic,SI,,,,,,,
,,,,Cantidad de Pedidos,,,,6,Informar a créditos,NO,,,,,,,
,,,,,,,,7,Analizar línea crédito,NO,,,,,,,
,,,,,,,,8,Depuración clientes morosos,NO,,,,,,,
,,,,,,,,9,Informar a programador,NO,,,,,,,
,,,,,,,,10,Descargar información a ROADNET,SI,,,,,,,
,,,,,,,,11,Análisis de Ruteo,SI,,,,,,,
,,,,,,,,12,Asignación de transporte,NO,,,,,,,
,,,,,,,,13,Coordinar con facturación y despacho,SI,,,,,,,
,,,,,,,,14,Impresión de factura ,NO,,,,,,,
,,,,,,,,15,Impresión de O/C,NO,,,,,,,
,,,,,,,,16,Entrega tickets,SI,,,,,,,
,,,,,,,,17,Picking,SI,,,,,,,
,,,,,,,,18,Traslado a despacho,NO,,,,,,,
,,,,,,,,19,Check List de carga,NO,,,,,,,
,,,,,,,,20,Confirmación de carga a montacarguista,NO,,,Parámetros de Control / Medición / Seguimiento,,Documentos del Proceso,,
,Responsables,,,,,,,21,Carga camión,SI,,,,,,,
,Jefe de operaciones,,,,,,,22,Recojo de factura,NO,,,Indicador de rechazos,,Pedido,,
,Supervisor de almacén,,,,,,,23,Generación G/R,NO,,,Nivel de servicio,,Guia de Remisión,,
,Asistente de almacén,,,,,,,24,Entrega de documento a transporte,NO,,,DPMO / CP,,Factura,,Minitab 17
,,,,,,,,25,Validar G/R par salida,NO,,,"Carta NP ,P, U, C (Atributos)",,,,
,Proceso de Soporte,,,,,,,26,Entrega de mercadería,SI,,,Lean: Valor / Total Act,,,,
,Inventario (Control de ingreso y salida de mercadería),,,,,,,27,Validación de documentos,NO,,,,,,,
,Sistema SAP,,,,,,,28,Verificación de devolución,NO,,,,,,,
,"Sistema basis, Comercial, Sipan",,,,,,,29,Validación de documentos,NO,,,,,,,
,,,,,,,,,,,,,,,,,
,Inicio / Fin,,,,,,,Recursos,,,,,Requisitos a cumplir,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 2  Unnamed: 3  Unnamed: 7  Unnamed: 11  Unnamed: 12  Unnamed: 16
count         0.0         0.0         0.0         0.0          0.0          0.0          0.0
mean          NaN         NaN         NaN         NaN          NaN          NaN          NaN
std           NaN         NaN         NaN         NaN          NaN          NaN          NaN
min           NaN         NaN         NaN         NaN          NaN          NaN          NaN
25%           NaN         NaN         NaN         NaN          NaN          NaN          NaN
50%           NaN         NaN         NaN         NaN          NaN          NaN          NaN
75%           NaN         NaN         NaN         NaN          NaN          NaN          NaN
max           NaN         NaN         NaN         NaN          NaN          NaN          NaN

## Hoja: DAP
Filas: 73 · Columnas: 16
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (float64), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), DOP: Diagrama de Operaciones del Proceso (object)

Muestra (primeras 40 de 73 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,DOP: Diagrama de Operaciones del Proceso
GRAFICA DE PROCESOS,,,,,,,,,,,,,,,
,,,,,,,,,,Resumen,,,,,
,,,,,,,,,,Actividad,,Número,Tiempo,Distancia,
Proceso:,,Despacho de mercadería,,,,,,,,,,,,,
Sujeto de la gráfica:,,Proceso de Despacho,,,,,,,,Operación,,24,1067.27,,
Principio:,,Verificación stock fisico-sistema,,,,,,,,Transporte,,1,30,,
Final:,,Asignación de transporte,,,,,,,,Inspección,,4,124,,
,,,,,,,,,,Retraso,,0,0,,
,,,,,,,,,,Almacenaje,,0,0,,
,,,,,,,,,,TOTAL,,29,1221.27,,
,,,,,,,,,,,,,20.354499999999998,horas,
Paso ,Tiempo,Distancia,,,,,,Genera,No Genera,Descripción del paso,,,,,Detalle del proceso
núm.,(min.),(mts),,,,,,Valor,Valor,,,,,,
1,100,,X,,,,,SI,,Verificación stock fisico-sistema,,,,,
2,40,,,,X,,,,NO,Cuadrar stock,,,,,
3,15,,X,,,,,,NO,Migración stock SAP a BASIC,,,,,
4,20,,X,,,,,,NO,Coordinar pedidos con Comercial,,,,,
5,25,,X,,,,,SI,,Descargar pedidos Hen Help a Basic,,,,,
6,2,,X,,,,,,NO,Informar a créditos,,,,,
7,60,,X,,,,,,NO,Analizar línea crédito,,,,,
8,15,,X,,,,,,NO,Depuración clientes morosos,,,,,
9,2,,X,,,,,,NO,Informar a programador,,,,,
10,5,,X,,,,,SI,,Descargar información a ROADNET,,,,,
11,60,,,,X,,,SI,,Análisis de Ruteo,,,,,
12,20,,X,,,,,,NO,Asignación de transporte,,,,,
13,2,,X,,,,,SI,,Coordinar con facturación y despacho,,,,,
14,30,,X,,,,,,NO,Impresión de factura ,,,,,
15,10,,X,,,,,,NO,Impresión de O/C,,,,,
16,2,,X,,,,,SI,,Entrega tickets,,,,,
17,360,,X,,,,,SI,,Picking,,,,,
18,30,30,,X,,,,,NO,Traslado a despacho,,,,,
19,20,,,,X,,,,NO,Check List de carga,,,,,
20,0.2,,X,,,,,,NO,Confirmación de carga a montacarguista,,,,,
21,20,,X,,,,,SI,,Carga camión,,,,,
22,0.03,,X,,,,,,NO,Recojo de factura,,,,,
23,0.04,,X,,,,,,NO,Generación G/R,,,,,
24,1,,X,,,,,,NO,Entrega de documento a transporte,,,,,
25,4,,,,X,,,,NO,Validar G/R par salida,,,,,
26,360,,X,,,,,SI,,Entrega de mercadería,,,,,
27,3,,X,,,,,,NO,Validación de documentos,,,,,

Resumen numérico:
        Unnamed: 7  Unnamed: 11
count     2.000000          0.0
mean    610.635000          NaN
std     863.568299          NaN
min       0.000000          NaN
25%     305.317500          NaN
50%     610.635000          NaN
75%     915.952500          NaN
max    1221.270000          NaN

## Hoja: AMEF
Filas: 22 · Columnas: 17
Columnas y tipos: Unnamed: 0 (float64), ANÁLISIS DE MODOS DE FALLO Y SUS EFECTOS (AMEF) (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (object)

Muestra (primeras 22 de 22 filas, formato CSV):
Unnamed: 0,ANÁLISIS DE MODOS DE FALLO Y SUS EFECTOS (AMEF),Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16
,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
,Nombre del Sistema (Título):,Despacho a Canal Moderno,,,,,,,,Fecha AMFE:,,,,,,
,Responsable (Dpto. / Área):,Operaciones ,,,,,,,,Fecha Revisión,,,,,,
,Responsable de AMEF (persona):,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
,Pasos del Proceso,Modo de Falla,Efecto de la Falla,Causa de la Falla,Situación Actual,,,,,Acciones Recomendadas,Responsable,Situación Actual,,,,
,,,,,Control,SEV,OCC,DET,NPR,,,Acciones Adoptadas,SEV,OCC,DET,NPR
,,,,,,,,,,,,,,,,
,Actualización Stock en Sistema Basis,Productos no aptos para determinado canal,Productos no cargados para despacho,Diseño de sistema informático,NO,8,8,8,512,Causa ó Mecanismo de Control,,Mecanismo de control,,,,
,Bajada de pedido al sistema Basis,Falta de coordinación con el área comercial,Pedidos no atendidos,Falta de capacitacion al personal,SI,9,2,2,36,,,,,,,
,Aprobación de créditos,Demora en aprobación,Demora en programación de carga,Falta de competencias del personal,SI,8,2,3,48,,,,,,,
,Programación de carga,Unidades excedidas en capacidad de carga,Productos no cargados para despacho,Falta de competencias del personal,NO,6,6,10,360,,,,,,,
,Emisión de Orden de carga y facturas,Traspapeleo de documentos,Mercadería no entregada a cliente- Reclamo de cliente,Falta de competencias del personal,SI,9,2,4,72,,,,,,,
,Preparación de carga,Cruce de carga,Reclamo del cliente,Falta de capacitacion al personal,SI,9,8,10,720,,,,,,,
,Verificación de carga,Faltante y/o sobrante de carga,Reclamo del cliente,Falta de capacitacion al personal,SI,9,8,6,432,,,,,,,
,Carga de productos a unidades,Cargar paletas no correspondiente a carga de unidad,Productos no cargados para despacho,Falta de capacitacion al personal,SI,9,3,5,135,,,,,,,
,Entrega de facturas a transportista,Entrega de documentos errados,Interrupcion del servicio y/o decomiso por la SUNAT,Falta de competencias del personal,NO,8,2,2,32,,,,,,,
,Generación y entrega de GR,Entrega de documentos errados,Interrupcion del servicio y/o decomiso por la SUNAT,Falta de competencias del personal,SI,8,1,2,16,,,,,,,
,Validación de documentos para salida de la unidad,Mala validación de asistente,Reclamo del cliente,Falta de capacitacion al personal,NO,9,6,2,108,,,,,,,
,Atención a cliente final,No llegar a tiempo,Rechazos totales y parciales,Mala programación de carga,SI,9,8,9,648,,,,,,,
,Liquidación de carga,Faltante de devoluciones,Diferencia de inventario,Falta de capacitacion al personal,SI,1,5,1,5,,,,,,,

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

## Hoja: ISHIKAWA
Filas: 0 · Columnas: 0
Columnas y tipos: 

Muestra (primeras 0 de 0 filas, formato CSV):


## Hoja: 5S
Filas: 10 · Columnas: 14
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (float64), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (float64), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object)

Muestra (primeras 10 de 10 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13
,,"Evaluación Semanal 5 S's 
",,,,,,,Conceptos,Total,Optimo,Porcentaje,Nº NA
,,,,,,,,,General,24.5,40,0.6621621621621622,3
LOGO DE,,,,,,,,,Selección,8,14,0.6153846153846154,1
EMPRESA,,,,,,,,,Orden,9.5,14,0.7307692307692307,1
,,,,,,,,,Limpieza,7,12,0.6363636363636364,1
,,,,,,,,,,,,,
,NIVEL:,REGULAR,,RANGOS DE MADUREZ,,,,,,,,,
,,,,,,,,,FECHA:,,,,
,,,,Crítico,Regular,Bien,Excelente,,,,,,
,PORCENTAJE:,0.6621621621621622,,> 0 %,> 50 %,> 70 %,> 90 %,,EVALUADOR: ,,,,

Resumen numérico:
       Unnamed: 3  Unnamed: 8
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: DAP-mejorado
Filas: 73 · Columnas: 16
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (float64), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), DOP: Diagrama de Operaciones del Proceso (object)

Muestra (primeras 40 de 73 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,DOP: Diagrama de Operaciones del Proceso
GRAFICA DE PROCESOS,,,,,,,,,,,,,,,
,,,,,,,,,,Resumen,,,,,
,,,,,,,,,,Actividad,,Número,Tiempo,Distancia,
Proceso:,,Despacho de mercadería,,,,,,,,,,,,,
Sujeto de la gráfica:,,Proceso de Despacho,,,,,,,,Operación,,24,1067.27,,
Principio:,,Verificación stock fisico-sistema,,,,,,,,Transporte,,1,30,,
Final:,,Asignación de transporte,,,,,,,,Inspección,,4,124,,
,,,,,,,,,,Retraso,,0,0,,
,,,,,,,,,,Almacenaje,,0,0,,
,,,,,,,,,,TOTAL,,29,1221.27,,
,,,,,,,,,,,,,20.354499999999998,horas,
Paso ,Tiempo,Distancia,,,,,,Genera,No Genera,Descripción del paso,,,,,Detalle del proceso
núm.,(min.),(mts),,,,,,Valor,Valor,,,,,,
1,100,,X,,,,,SI,,Verificación stock fisico-sistema,,,,,El personal analisa el stock fisico y el stock del sistema
2,40,,,,X,,,,NO,Cuadrar stock,,,,,En Caso no cuadre las cantidades realiza un ajuste
3,15,,X,,,,,,NO,Migración stock SAP a BASIC,,,,,Posterior a ello migra el stock real al sistema Basic
4,20,,X,,,,,,NO,Coordinar pedidos con Comercial,,,,,El area comercial genera sus pedidos previa coordinacion con almacen
5,25,,X,,,,,SI,,Descargar pedidos Hen Help a Basic,,,,,se realiza la descarga de los pedidos al sistema Basic
6,2,,X,,,,,,NO,Informar a créditos,,,,,posterior a ello se pasa la informacion de la cantidad a  facturar para que el area de creditos valide su atencion
7,60,,X,,,,,si,,Analizar línea crédito,,,,,el area de creditos analiza la transaccion y da el visto bueno de lo contrario pasa a observacion
8,15,,X,,,,,,NO,Depuración clientes morosos,,,,,se realiza la depuracion de los clientes en observacion
9,2,,X,,,,,,NO,Informar a programador,,,,,pasa la informacion al programador
10,5,,X,,,,,SI,,Descargar información a ROADNET,,,,,el programador realiza  la descarga de la informacion al sistema Roadnet
11,60,,,,X,,,SI,,Análisis de Ruteo,,,,,se analisa el sistema del ruteo
12,20,,X,,,,,si,,Asignación de transporte,,,,,posterior a ello se asigna el transporte
13,2,,X,,,,,SI,,Coordinar con facturación y despacho,,,,,se coordina con el area de facturacion y despacho
14,30,,X,,,,,,NO,Impresión de factura ,,,,,se imprime la factura para ejecutar el despacho
15,10,,X,,,,,,NO,Impresión de O/C,,,,,se imprime la O\C para ejecutar el despacho
16,2,,X,,,,,SI,,Entrega tickets,,,,,entrega de ticket de verificacion
17,360,,X,,,,,SI,,Picking,,,,,verificacion y picking
18,30,30,,X,,,,,NO,Traslado a despacho,,,,,traslado al area de despacho
19,20,,,,X,,,si,,Check List de carga,,,,,verificacion  de la carga por medio del check list de carga
20,0.2,,X,,,,,,NO,Confirmación de carga a montacarguista,,,,,una vez verificada la carga se pasa la informacion al montacarguista
21,20,,X,,,,,SI,,Carga camión,,,,,el montacarguista carga el pedido al camion
22,0.03,,X,,,,,,NO,Recojo de factura,,,,,emison de la factura por el area de facturacion
23,0.04,,X,,,,,,NO,Generación G/R,,,,,posterior a ello emision de la guia de remision
24,1,,X,,,,,,NO,Entrega de documento a transporte,,,,,entrega de documento al transportista
25,4,,,,X,,,,NO,Validar G/R par salida,,,,,validacion de la guia de remision para la salida del transporte hacia el destino
26,360,,X,,,,,SI,,Entrega de mercadería,,,,,entrega de la mercaderia al  punto de destino
27,3,,X,,,,,,NO,Validación de documentos,,,,,se valida los documen tos con la conformidad del cliente

Resumen numérico:
        Unnamed: 7  Unnamed: 11
count     2.000000          0.0
mean    610.635000          NaN
std     863.568299          NaN
min       0.000000          NaN
25%     305.317500          NaN
50%     610.635000          NaN
75%     915.952500          NaN
max    1221.270000          NaN

## Hoja: AMEFZOL mejorado
Filas: 22 · Columnas: 17
Columnas y tipos: Unnamed: 0 (float64), ANÁLISIS DE MODOS DE FALLO Y SUS EFECTOS (AMEF) (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (object)

Muestra (primeras 22 de 22 filas, formato CSV):
Unnamed: 0,ANÁLISIS DE MODOS DE FALLO Y SUS EFECTOS (AMEF),Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16
,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
,Nombre del Sistema (Título):,Despacho a Canal Moderno,,,,,,,,Fecha AMFE:,,,,,,
,Responsable (Dpto. / Área):,Operaciones ,,,,,,,,Fecha Revisión,,,,,,
,Responsable de AMEF (persona):,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
,Pasos del Proceso,Modo de Falla,Efecto de la Falla,Causa de la Falla,Situación Actual,,,,,Acciones Recomendadas,Responsable,Situación Actual,,,,
,,,,,Control,SEV,OCC,DET,NPR,,,Acciones Adoptadas,SEV,OCC,DET,NPR
,,,,,,,,,,,,,,,,
,Actualización Stock en Sistema Basis,Productos no aptos para determinado canal,Productos no cargados para despacho,Diseño de sistema informático,NO,8,8,8,512,Mejorar diseño de  sistema,Jefe de area,Adaptar el sisitema a la necesidad,8,6,8,384
,Bajada de pedido al sistema Basis,Falta de coordinación con el área comercial,Pedidos no atendidos,Falta de capacitacion al personal,SI,9,2,2,36,Capacitacion al personal de Pedidos,,,,,,
,Aprobación de créditos,Demora en aprobación,Demora en programación de carga,Falta de competencias del personal,SI,8,2,3,48,Mejoramiento en la programcion de carga,,,,,,
,Programación de carga,Unidades excedidas en capacidad de carga,Productos no cargados para despacho,Falta de competencias del personal,NO,6,6,10,360,Mejorar programacion de carga,Jefe de area,constantes captacitaciones al personal y grafica de control ,6,5,2,60
,Emisión de Orden de carga y facturas,Traspapeleo de documentos,Mercadería no entregada a cliente- Reclamo de cliente,Falta de competencias del personal,SI,9,2,4,72,Capacitacion en la organización documentaria,,,,,,
,Preparación de carga,Cruce de carga,Reclamo del cliente,Falta de capacitacion al personal,SI,9,8,10,720,Mejoramiento de sistema de carga,Jefe de area,constantes captacitaciones al personal,9,5,10,450
,Verificación de carga,Faltante y/o sobrante de carga,Reclamo del cliente,Falta de capacitacion al personal,SI,9,8,6,432,Mejoramiento del sistema de verificacion de carga,Jefe de area,Mejorar el Sistema de evalución,9,5,6,270
,Carga de productos a unidades,Cargar paletas no correspondiente a carga de unidad,Productos no cargados para despacho,Falta de capacitacion al personal,SI,9,3,5,135,Mejorar sistema de carga,,,,,,
,Entrega de facturas a transportista,Entrega de documentos errados,Interrupcion del servicio y/o decomiso por la SUNAT,Falta de competencias del personal,NO,8,2,2,32,Mejoramiento del sisitemas de facturacion,,,,,,
,Generación y entrega de GR,Entrega de documentos errados,Interrupcion del servicio y/o decomiso por la SUNAT,Falta de competencias del personal,SI,8,1,2,16,Mejoramineto de sisitemas documentario,,,,,,
,Validación de documentos para salida de la unidad,Mala validación de asistente,Reclamo del cliente,Falta de capacitacion al personal,NO,9,6,2,108,Capacitacion del personal para verificacion,,,,,,
,Atención a cliente final,No llegar a tiempo,Rechazos totales y parciales,Mala programación de carga,SI,9,8,9,648,Mejorar los sistemas de programacion,Jefe de area,Capacitacion al personal de carga,9,5,9,405
,Liquidación de carga,Faltante de devoluciones,Diferencia de inventario,Falta de capacitacion al personal,SI,1,5,1,5,Capacitacion a personal de carga,,,,,,

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

## Hoja: Pasos Evaluación_ANOVA
Filas: 154 · Columnas: 7
Columnas y tipos: Unnamed: 0 (object), Pasos: (object), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object)

Muestra (primeras 40 de 154 filas, formato CSV):
Unnamed: 0,Pasos:,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
1.-,Evaluar Normalidad DPU,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,"Obs: Se presenta que el P-value es < a 0.05, por lo que se elimina un dato que está fuera de distribución.",,,,,
,,,,,,
2.-,Reevaluar Normalidad depurando dato fuera de rango,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,
,,,,,,

Resumen numérico:
       Unnamed: 2  Unnamed: 3
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: Hoja1
Filas: 25 · Columnas: 8
Columnas y tipos: DPU (float64), Ausentismo (float64), Total CF (float64), Demora Inicio Picking (float64), Unnamed: 4 (float64), Servicios (int64), Defectos (int64), DPU.1 (float64)

Muestra (primeras 25 de 25 filas, formato CSV):
DPU,Ausentismo,Total CF,Demora Inicio Picking,Unnamed: 4,Servicios,Defectos,DPU.1
0.9487179487179487,0.0,17546.333333333332,0.03472222222222221,,195,10,0.9487179487179487
0.9212121212121213,0.13043478260869568,51672.666666666664,0.0625,,495,39,0.9212121212121213
0.9191919191919192,0.13043478260869568,47309.583333333336,0.08333333333333326,,495,40,0.9191919191919192
0.9373970345963756,0.08695652173913049,68773.70000000001,0.01388888888888884,,607,38,0.9373970345963756
0.9499165275459098,0.13043478260869568,49852.9,0.03819444444444453,,599,30,0.9499165275459098
0.9150743099787686,0.045454545454545414,61925.7,0.05555555555555547,,471,40,0.9150743099787686
0.935656836461126,0.0,29219.0,0.01388888888888895,,373,24,0.935656836461126
0.922509225092251,0.0,60570.583333333336,0.0347222222222221,,542,42,0.9225092250922509
0.9332273449920508,0.0,53005.54166666667,0.02777777777777779,,629,42,0.9332273449920508
0.9223140495867769,0.0,66701.63333333333,0.01041666666666674,,605,47,0.9223140495867769
0.925531914893617,0.09090909090909094,56882.341666666674,0.01388888888888895,,564,42,0.925531914893617
0.9346642468239564,0.19999999999999996,65591.08333333334,0.05208333333333337,,551,36,0.9346642468239564
0.9514563106796117,0.050000000000000044,31559.333333333332,0.02083333333333326,,412,20,0.9514563106796117
0.9081081081081082,0.050000000000000044,85080.86666666667,0.02083333333333337,,555,51,0.9081081081081082
0.9496753246753247,0.0,55323.5,0.01736111111111116,,616,31,0.9496753246753247
0.9299363057324841,0.0,83697.41666666667,0.010416666666666519,,628,44,0.9299363057324841
0.9445407279029463,0.0,52107.583333333336,0.01388888888888884,,577,32,0.9445407279029463
0.946969696969697,0.050000000000000044,29800.175,0.02777777777777779,,396,21,0.946969696969697
0.9259259259259259,0.050000000000000044,82337.0,0.03125,,621,46,0.9259259259259259
0.9161290322580645,0.0,76438.375,0.02430555555555547,,620,52,0.9161290322580645
0.924031007751938,0.0,87408.78333333333,0.02430555555555558,,645,49,0.924031007751938
0.9352640545144804,0.0,67949.83333333333,0.02430555555555547,,587,38,0.9352640545144804
0.9222903885480572,0.04347826086956519,79226.10833333334,0.04999999999999993,,489,38,0.9222903885480572
0.9422110552763819,0.08695652173913049,28640.833333333336,0.021527777777777812,,398,23,0.9422110552763819
0.9524539877300614,0.13043478260869568,95837.34999999999,0.02083333333333326,,652,31,0.9524539877300613

Resumen numérico:
             DPU  Ausentismo      Total CF  Demora Inicio Picking  Unnamed: 4   Servicios   Defectos      DPU.1
count  25.000000   25.000000     25.000000              25.000000         0.0   25.000000  25.000000  25.000000
mean    0.932576    0.051020  59378.329000               0.029944         NaN  532.880000  36.240000   0.932576
std     0.013012    0.057851  20922.416445               0.018201         NaN  109.736928  10.540715   0.013012
min     0.908108    0.000000  17546.333333               0.010417         NaN  195.000000  10.000000   0.908108
25%     0.922314    0.000000  49852.900000               0.017361         NaN  489.000000  31.000000   0.922314
50%     0.933227    0.045455  60570.583333               0.024306         NaN  564.000000  38.000000   0.933227
75%     0.944541    0.086957  76438.375000               0.034722         NaN  616.000000  42.000000   0.944541
max     0.952454    0.200000  95837.350000               0.083333         NaN  652.000000  52.000000   0.952454
