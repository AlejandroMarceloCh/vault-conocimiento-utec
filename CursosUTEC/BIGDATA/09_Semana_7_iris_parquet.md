---
curso: BIGDATA
titulo: 09 - Semana 7/iris
slides: 0
fuente: 09 - Semana 7/iris.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 09 - Semana 7/iris.parquet. -->

<!-- INTERPRETAR: datos tabulares de iris.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 150 · Columnas: 5
Columnas y tipos: sepal.length (float64), sepal.width (float64), petal.length (float64), petal.width (float64), variety (object)

Muestra (primeras 40 de 150 filas, formato CSV):
sepal.length,sepal.width,petal.length,petal.width,variety
5.1,3.5,1.4,0.2,Setosa
4.9,3.0,1.4,0.2,Setosa
4.7,3.2,1.3,0.2,Setosa
4.6,3.1,1.5,0.2,Setosa
5.0,3.6,1.4,0.2,Setosa
5.4,3.9,1.7,0.4,Setosa
4.6,3.4,1.4,0.3,Setosa
5.0,3.4,1.5,0.2,Setosa
4.4,2.9,1.4,0.2,Setosa
4.9,3.1,1.5,0.1,Setosa
5.4,3.7,1.5,0.2,Setosa
4.8,3.4,1.6,0.2,Setosa
4.8,3.0,1.4,0.1,Setosa
4.3,3.0,1.1,0.1,Setosa
5.8,4.0,1.2,0.2,Setosa
5.7,4.4,1.5,0.4,Setosa
5.4,3.9,1.3,0.4,Setosa
5.1,3.5,1.4,0.3,Setosa
5.7,3.8,1.7,0.3,Setosa
5.1,3.8,1.5,0.3,Setosa
5.4,3.4,1.7,0.2,Setosa
5.1,3.7,1.5,0.4,Setosa
4.6,3.6,1.0,0.2,Setosa
5.1,3.3,1.7,0.5,Setosa
4.8,3.4,1.9,0.2,Setosa
5.0,3.0,1.6,0.2,Setosa
5.0,3.4,1.6,0.4,Setosa
5.2,3.5,1.5,0.2,Setosa
5.2,3.4,1.4,0.2,Setosa
4.7,3.2,1.6,0.2,Setosa
4.8,3.1,1.6,0.2,Setosa
5.4,3.4,1.5,0.4,Setosa
5.2,4.1,1.5,0.1,Setosa
5.5,4.2,1.4,0.2,Setosa
4.9,3.1,1.5,0.2,Setosa
5.0,3.2,1.2,0.2,Setosa
5.5,3.5,1.3,0.2,Setosa
4.9,3.6,1.4,0.1,Setosa
4.4,3.0,1.3,0.2,Setosa
5.1,3.4,1.5,0.2,Setosa

Resumen numérico:
       sepal.length  sepal.width  petal.length  petal.width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.057333      3.758000     1.199333
std        0.828066     0.435866      1.765298     0.762238
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
