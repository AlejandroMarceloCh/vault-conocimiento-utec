---
curso: ML
titulo: caso1_combustible
slides: 0
fuente: caso1_combustible.csv
---

# caso1_combustible.csv — Interpretación

El archivo es una tabla de 200 vehículos con cinco columnas numéricas: `peso_kg`, `cilindrada_L`, `potencia_hp` y `anio` como características, y `consumo_km_litro` como variable objetivo. Cada fila describe un vehículo por su peso, el volumen de su motor, sus caballos de fuerza, su año de fabricación (1990–2023) y cuántos kilómetros recorre por litro. La estructura —varias variables predictoras continuas frente a un objetivo continuo— es el molde clásico de un problema de regresión supervisada, y ese es el concepto que el caso ejercita: estimar el consumo en función de las propiedades físicas del vehículo.

El caso también enseña a mirar los datos antes de modelar. El resumen numérico revela una señal fuerte: el objetivo está fuertemente sesgado y apelmazado en su piso, con media 3.53 pero mediana, mínimo y hasta el percentil 75 todos clavados en 3.0, mientras el máximo llega a 19.75. Esa acumulación en un valor obliga a discutir censura, valores atípicos y la calidad del target antes de entrenar cualquier modelo.

En un proyecto real sirve para practicar el flujo completo: exploración descriptiva, tratamiento de outliers y escalado, y regresión lineal o modelos más flexibles. Conecta con los temas del curso sobre análisis exploratorio, preprocesamiento de features, métricas de error (MAE, RMSE) y validación, así como con la interpretación de coeficientes para explicar qué variable pesa más en el consumo.

```
## Hoja: csv
Filas: 200 · Columnas: 5
Columnas y tipos: peso_kg (float64), cilindrada_L (float64), potencia_hp (int64), anio (int64), consumo_km_litro (float64)

peso_kg,cilindrada_L,potencia_hp,anio,consumo_km_litro
1599.2,3.91,163,2016,3.0
1706.4,3.54,309,2012,3.0
1507.0,3.91,387,2009,3.0
926.9,4.1,354,2019,9.29
2371.9,4.33,281,2003,3.0
...

Resumen numérico:
           peso_kg  cilindrada_L  potencia_hp         anio  consumo_km_litro
count   200.000000    200.000000   200.000000   200.000000        200.000000
mean   1643.744000      3.089400   228.655000  2006.670000          3.533500
std     504.620224      1.169239    95.490724     9.709401          2.063539
min     817.300000      1.000000    60.000000  1990.000000          3.000000
25%    1173.325000      2.015000   153.000000  1998.000000          3.000000
50%    1645.400000      3.090000   228.000000  2007.000000          3.000000
75%    2079.550000      4.202500   316.000000  2015.250000          3.000000
max     2497.200000      4.940000   399.000000  2023.000000         19.750000
```
