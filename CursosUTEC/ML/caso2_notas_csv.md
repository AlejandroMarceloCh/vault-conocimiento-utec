---
curso: ML
titulo: caso2_notas
slides: 0
fuente: caso2_notas.csv
---

## caso2_notas.csv — Regresión para predecir la nota final

El archivo `caso2_notas.csv` es un dataset tabular de 200 filas y 5 columnas que describe el desempeño académico de 200 estudiantes. Cuatro columnas son variables predictoras (features): `horas_estudio` (float, de 0.1 a 11.9), `horas_suenio` (float, de 4.0 a 10.0), `asistencia_pct` (float, de 40.3 a 99.9) y `ejercicios_resueltos` (entero, de 0 a 200). La quinta columna, `nota_final ( Y )`, es la variable objetivo: un valor continuo entre 8.64 y 20.0, con media 15.09 y desviación 3.10. El propio nombre "( Y )" marca que esa columna es la que se busca predecir.

El concepto de ML que ejercita es la regresión supervisada: aprender una función que estime un valor numérico continuo a partir de varias variables de entrada. A diferencia de una clasificación, aquí no se predicen categorías sino una cantidad, y por eso se evalúa con métricas como MAE, RMSE o R². El dataset invita además a explorar correlaciones (más horas de estudio y más asistencia tienden a subir la nota) y el efecto conjunto de varios predictores, es decir, regresión lineal múltiple.

En un proyecto real este caso sirve de base limpia para practicar el flujo completo: análisis exploratorio con el resumen numérico (count, media, std, cuartiles), separación train/test, ajuste de un modelo (regresión lineal, árboles o gradient boosting) e interpretación de la importancia de cada variable. Conecta con estadística descriptiva, correlación, evaluación de modelos y feature engineering, temas centrales del curso.

```
## Hoja: csv
Filas: 200 · Columnas: 5
Columnas y tipos: horas_estudio (float64), horas_suenio (float64), asistencia_pct (float64), ejercicios_resueltos (int64), nota_final ( Y ) (float64)

Muestra (primeras 40 de 200 filas, formato CSV):
horas_estudio,horas_suenio,asistencia_pct,ejercicios_resueltos,nota_final ( Y )
4.4,6.0,90.2,191,15.16
3.6,6.6,66.2,10,11.6
1.7,7.7,75.9,150,12.88
6.7,8.0,52.9,170,15.75
10.2,4.6,65.6,135,17.27
3.7,9.4,46.4,20,11.45
2.9,7.9,81.0,177,14.95
0.9,4.2,75.0,178,11.48
8.1,5.8,45.5,14,12.22
2.3,4.6,61.6,2,8.84
2.9,4.9,44.0,76,9.73
10.9,6.3,82.0,64,20.0
1.0,4.1,92.1,52,10.16
10.1,4.6,44.4,120,15.63
9.0,8.7,80.2,36,17.23
4.7,6.8,55.8,103,13.07
11.9,7.4,60.9,154,20.0
6.2,5.8,77.3,4,11.86
7.9,9.2,69.8,176,18.28
7.4,6.8,73.5,200,16.73
1.8,4.7,93.0,10,10.68
9.4,6.5,62.3,101,17.55
8.6,4.0,82.7,100,17.26
11.2,4.9,94.3,143,20.0
9.2,8.6,51.6,198,18.86
7.6,9.4,76.9,175,19.08
2.8,8.6,70.5,47,12.0
7.6,4.6,68.4,70,15.39
0.8,6.0,92.5,120,13.33
2.4,7.9,93.9,167,14.99
3.2,7.4,43.6,23,8.97
5.5,9.5,90.2,142,17.08
3.1,5.0,96.1,102,12.98
1.2,4.9,64.8,73,8.64
2.8,5.9,91.9,83,12.6
5.7,4.8,80.3,97,14.56
8.1,9.8,53.9,65,17.35
6.0,5.4,43.0,140,14.05
5.4,7.9,45.9,41,13.34
1.9,9.9,46.0,44,10.32

Resumen numérico:
       horas_estudio  horas_suenio  asistencia_pct  ejercicios_resueltos  nota_final ( Y )
count     200.000000    200.000000      200.000000            200.000000        200.000000
mean        6.248500      6.958000       69.119000             99.545000         15.087400
std         3.412981      1.781715       17.877465             59.337532          3.099968
min         0.100000      4.000000       40.300000              0.000000          8.640000
25%         3.175000      5.375000       52.200000             45.750000         12.752500
50%         6.300000      7.000000       69.400000            101.000000         14.940000
75%         9.225000      8.525000       84.350000            150.250000         17.717500
max        11.900000     10.000000       99.900000            200.000000         20.000000
```
