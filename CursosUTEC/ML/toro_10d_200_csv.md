---
curso: ML
titulo: toro_10d_200
slides: 0
fuente: toro_10d_200.csv
---

# toro_10d_200.csv

Este archivo es un dataset tabular de clasificación con 200 observaciones y 11 columnas: diez atributos continuos `x1`–`x10` (todos `float64`) y una variable objetivo `clase` de tipo entero. La etiqueta toma cuatro valores discretos (0, 1, 2 y 3), por lo que se trata de un problema de clasificación multiclase con cuatro categorías. El nombre "toro_10d" sugiere datos sintéticos generados sobre una estructura geométrica (un toro embebido en un espacio de diez dimensiones): las variables no son medidas independientes de un fenómeno real, sino coordenadas construidas para practicar. Esto se nota en el resumen numérico: varias columnas están centradas cerca de cero con escalas dispares (`x4` con desviación 4.16 frente a `x3` acotada entre −1 y 1, típico de un seno o coseno), lo que anticipa la necesidad de estandarizar antes de entrenar.

El concepto que ejercita es la clasificación supervisada multiclase en un espacio de features de dimensión media, donde la frontera de decisión no es trivialmente lineal. Es un banco de pruebas ideal para comparar modelos (k-NN, SVM con kernel, árboles, redes) y para discutir el efecto de la geometría de los datos y la maldición de la dimensionalidad.

En un proyecto real sirve como referencia controlada: al conocer la estructura generadora se puede validar si un modelo captura relaciones no lineales. Conecta con escalamiento de variables, validación cruzada, matrices de confusión y reducción de dimensionalidad.

## Estructura del dataset

| Columna | Tipo | Rol |
|---------|------|-----|
| x1–x10 | float64 | Atributos predictores |
| clase | int64 | Etiqueta objetivo (0, 1, 2, 3) |

Filas: 200 · Columnas: 11

Muestra (primeras filas, formato CSV):

```
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,clase
-1.672731,1.682425,-0.778587,-4.146419,2.903648,0.589373,-1.54185,0.73492,1.595629,-1.3545,1
3.679709,-1.177378,0.504383,6.680132,-3.121093,0.277877,1.587209,-2.353625,-0.796297,1.107534,3
-0.398196,-3.504609,0.849767,4.372176,-3.535615,-1.320116,1.483593,0.937817,-2.624402,2.098993,2
-3.095948,-2.209709,-0.59511,-1.006274,-0.159471,-1.487205,0.140548,1.985631,-0.377162,-0.260734,2
1.233476,1.84023,-0.619977,-0.733459,1.632447,0.523609,-0.522048,-1.529193,1.151194,-1.383971,0
```

Resumen numérico:

```
               x1          x2          x3          x4          x5          x6          x7          x8          x9         x10       clase
count  200.000000  200.000000  200.000000  200.000000  200.000000  200.000000  200.000000  200.000000  200.000000  200.000000  200.000000
mean     0.143233    0.164314   -0.073162   -0.000992    0.203357    0.058172   -0.038948   -0.101482    0.148000   -0.119413    1.465000
std      2.143675    2.229577    0.695003    4.155757    2.072022    1.156326    1.305680    1.447602    1.243932    1.064747    1.151261
min     -3.959198   -3.867127   -0.999993   -7.978129   -4.497488   -2.207006   -2.697753   -2.647869   -2.961688   -2.336896    0.000000
25%     -1.711485   -1.815819   -0.778968   -3.694130   -1.324900   -0.954176   -1.167873   -1.325877   -0.747834   -0.906401    0.000000
50%      0.271123    0.085558   -0.145224    0.240258    0.220990    0.122418   -0.094240   -0.203511    0.144351   -0.249107    1.000000
75%      1.964631    2.088485    0.592610    3.843653    1.644856    0.981820    1.111568    1.083169    1.072117    0.765351    3.000000
max      3.971783    3.989210    0.999999    7.508825    4.264384    2.351944    2.224543    3.152253    2.853798    2.098993    3.000000
```
