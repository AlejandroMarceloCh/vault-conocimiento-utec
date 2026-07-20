---
curso: FUNDOPS
titulo: Ejemplo de Capacidad - Solución en clase
slides: 0
fuente: Ejemplo de Capacidad - Solución en clase.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Ejemplo de Capacidad - Solución en clase.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Ejemplo de Capacidad - Solución en clase.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Data
Filas: 66 · Columnas: 8
Columnas y tipos: Unnamed: 0 (float64), Ejemplo de Capacidad (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object)

Muestra (primeras 40 de 66 filas, formato CSV):
Unnamed: 0,Ejemplo de Capacidad,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7
,,,,,,,
,Productos,Demanda anual, Tamaño de Lotes,Lotes /año,,,
,X105,300000,8000,,,,
,X106,95000,5000,,,,
,X107,145000,6000,,,,
,Suma,,,,,,
,Lote promedio:,,,,,,
,,,,,,,
,Número de semanas anuales,52,,,,,
,,,,,,,
,Tiempos de ejecución ,,,,,,
,,,,,,,
,,Habilitado,Armado,Soldado,Pintado,Accesorios,Línea
,Planta A,,,,,,
,T Ejecución (horas),0.002,0.002,0.003,0.005,0.004,
,Set-up (horas),4,3,6,8,4,
,T Ejecución (horas),,,,,,
,Set-up (horas),,,,,,
,Planta B,,,,,,
,T Ejecución (horas),0.002,0.002,0.0025,0.0043,0.004,
,Set-up (horas),4,3,7,10,4,
,T Ejecución (horas),,,,,,
,Set-up (horas),,,,,,
,Planta C,,,,,,
,T Ejecución (horas),0.002,0.002,0.0025,0.0033,0.004,
,Set-up (horas),4,3,7,12,4,
,,,,,,,
,,,,,,,
,Cuadro de Datos,,,,,,
,,,,,,,
,Eficiencias,,,,,,
,Planta A,,,,,,
,Eficiencia 1 1er turno,0.93,,,,,
,Horas Extras,0.86,,,,,
,Eficiencia 2 2do turno,0.7,,,,,
,Planta B,,,,,,
,Eficiencia 1 1er turno,0.94,,,,,
,Horas Extras,0.9,,,,,
,Eficiencia 2 2do turno,0.89,,,,,
,Planta C,,,,,,

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

## Hoja: Solución
Filas: 65 · Columnas: 13
Columnas y tipos: Unnamed: 0 (float64), Ejemplo de Capacidad (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (float64), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object)

Muestra (primeras 40 de 65 filas, formato CSV):
Unnamed: 0,Ejemplo de Capacidad,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12
,,unid/año,unid/lote,,,,,,,,,
,Productos,Demanda anual, Tamaño de Lotes,Lotes /año,,,,,,,,
,X105,300000,8000,37.5,,,,,,,,
,X106,95000,5000,19,,,,,,,,
,X107,145000,6000,24.166666666666668,,,,,,,,
,Demanda Total =,540000,,80.66666666666667,,,,,,,,
,Q = Tamaño de lote promedio =,6694.214876033057,,,,,,,,,,
,,,,unid/año,,,,,,,,
,Número de semanas anuales,52,,unid/lote,,,,,,,,
,,,,,,,,,,,,
,Tiempos de ejecución ,,,,,,,,,,,
,,,,,,,,,,,,"48 hr  --> 1semana ---> 
x hr --> 52 semanas"
,,,,,,,,,Semanas disponibles,52,,
,Planta A,Habilitado,Armado,Soldado,Pintado,Accesorios,Línea,,,asumimos,,
,T Ejecución (horas/unidad),0.002,0.002,0.003,0.005,0.004,0.005,,Horas disponibles,Semanales (hr),Horas Anuales,Acumulado
,Set-up (horas),4,3,6,8,4,8,,Turno 1,48,2496,2496
,Flow Rate (unidades/hora),384.98098859315587,408.4720121028744,256.6539923954373,161.41889198884016,217.50805585392052,161.41889198884016,,Horas Extras,12,624,3120
,Planta B,Habilitado,Armado,Soldado,Pintado,Accesorios,Línea,,Turno 2,48,2496,5616
,T Ejecución (horas),0.002,0.002,0.0025,0.0043,0.004,0.0043,,,,,
,Set-up (horas),4,3,7,10,4,10,,,374698.4455958549,,
,Flow Rate (unidades/hora),384.98098859315587,408.4720121028744,282.03342618384397,172.59748561687618,217.50805585392052,172.59748561687618,,Máxima producción,86623.83419689118,,
,Planta C,Habilitado,Armado,Soldado,Pintado,Accesorios,Línea,,Tiempos,Producción Máxima,Tiempo Unitario (horas/unid),Prod Acumulada
,T Ejecución (horas),0.002,0.002,0.0025,0.0033,0.004,0.0033,,Planta A - T. Regular,374698.4455958549,0.0066613566971989915,374698.4455958549
,Set-up (horas),4,3,7,12,4,12,,Planta A - H. Extra,86623.83419689118,0.007203560149296584,461322.27979274606
,Flow Rate (unidades/hora),384.98098859315587,408.4720121028744,282.03342618384397,196.36363636363635,217.50805585392052,196.36363636363635,,Planta A - 2do Turno,282031.0880829015,0.008850088183421518,743353.3678756475
,,,,,,,,,,,,
,,,,,,,,,Planta B- T. Regular,404955.12465373956,0.006163645915418966,404955.12465373956
,Cuadro de Datos,,,,,,,,Planta B- H. Extra,96930.74792243767,0.00643758573388203,501885.87257617724
,,,,,,,,,Planta B - 2do Turno,383414.95844875346,0.0065099181578582325,885300.8310249307
,Eficiencias,,,,,,,,,,,
,Planta A,,,,,,,,Planta C - T. Regular,470518.6909090908,0.005304783950617285,470518.6909090908
,Eficiencia 1 1er turno,0.93,,,,,,,Planta C - H. Extra,112728.43636363636,0.005535426731078905,583247.1272727272
,Horas Extras,0.86,,,,,,,Planta C - 2do Turno,446012.50909090904,0.005596255596255597,1029259.6363636362
,Eficiencia 2 2do turno,0.7,,,,,,,,,,
,Planta B,,,,,,,,,,,
,Eficiencia 1 1er turno,0.94,,,,,,,,Planta A,Planta B,Planta C
,Horas Extras,0.9,,,,,,,Costo de MO Directa,496204.8,496204.8,496204.8
,Eficiencia 2 2do turno,0.89,,,,,,,Costo de Horas Extra,93038.4,93038.4,93038.4
,Planta C,,,,,,,,Costo de Materiales,636595.1714254216,734708.4216237827,845463.2727272725
,Eficiencia 1 1er turno,0.96,,,,,,,Costo de Servicios y Adm.,80000,100000,160000

Resumen numérico:
       Unnamed: 0  Unnamed: 8
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN
