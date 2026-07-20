---
curso: ML
titulo: caso3_energia
slides: 0
fuente: caso3_energia.csv
---

# caso3_energia.csv — Interpretación

Este archivo es un dataset tabular de 200 filas y 6 columnas que modela el consumo eléctrico de hogares. Cinco columnas son predictoras: `temperatura_C` (temperatura ambiente, entre 5.1 y 40 °C), `habitantes` (número entero de residentes, de 1 a 7), `superficie_m2` (área de la vivienda, 31 a 249.5 m²), `eficiencia_1a5` (una calificación ordinal de eficiencia energética de 1 a 5) y `horas_en_hogar` (horas diarias de ocupación, 4.1 a 17.9). La sexta columna, `consumo_kwh`, es la variable objetivo continua: el consumo eléctrico medido en kilovatios-hora, con media 415.5 y rango de 100.1 a 735.8.

El concepto que ejercita es la **regresión lineal múltiple**: predecir una variable numérica continua a partir de varias predictoras de naturaleza mixta (continuas, de conteo y ordinales). Es un caso didáctico casi ideal, porque las relaciones son intuitivas —más habitantes, más superficie o mayor temperatura empujan el consumo hacia arriba— y permite interpretar el signo y la magnitud de cada coeficiente.

En un proyecto real sirve para estimación de demanda energética, detección de hogares con consumo anómalo y análisis de qué factores pesan más en la factura. Conecta con temas del curso como preprocesamiento y escalado de features, evaluación con MAE/RMSE/R², validación cruzada y análisis de residuos e importancia de variables.

## Datos originales del volcado

**Columnas y tipos:** `temperatura_C` (float64), `habitantes` (int64), `superficie_m2` (float64), `eficiencia_1a5` (int64), `horas_en_hogar` (float64), `consumo_kwh` (float64)

```
temperatura_C,habitantes,superficie_m2,eficiencia_1a5,horas_en_hogar,consumo_kwh
32.9,7,123.9,4,15.2,579.9
17.6,1,106.4,1,15.5,326.4
7.5,1,237.5,2,13.3,289.3
14.8,7,237.2,5,5.6,437.9
35.6,2,234.1,4,15.4,481.0
22.5,3,219.2,2,16.5,501.9
13.1,3,98.4,2,5.9,312.4
13.0,1,237.9,2,17.3,353.6
13.2,1,62.1,2,16.4,250.4
6.7,5,125.1,4,10.8,312.3
15.8,2,144.4,3,9.0,276.1
12.6,1,182.6,1,12.9,322.8
22.6,3,76.0,1,12.2,396.6
16.4,6,151.1,2,5.8,464.3
21.9,2,171.9,1,8.8,413.5
16.4,3,214.1,1,8.3,400.4
34.0,2,138.6,1,4.4,471.1
38.0,2,147.6,2,6.4,490.8
19.1,4,204.4,4,4.8,388.9
31.0,5,93.4,1,5.8,552.6
...
```

**Resumen numérico:**

| Estadístico | temperatura_C | habitantes | superficie_m2 | eficiencia_1a5 | horas_en_hogar | consumo_kwh |
|---|---|---|---|---|---|---|
| count | 200.00 | 200.00 | 200.00 | 200.00 | 200.00 | 200.00 |
| mean | 22.53 | 3.81 | 139.33 | 2.98 | 10.68 | 415.51 |
| std | 10.42 | 2.05 | 62.62 | 1.46 | 3.97 | 116.03 |
| min | 5.10 | 1.00 | 31.00 | 1.00 | 4.10 | 100.10 |
| 25% | 13.18 | 2.00 | 82.73 | 2.00 | 6.98 | 343.55 |
| 50% | 21.85 | 4.00 | 136.90 | 3.00 | 10.70 | 406.70 |
| 75% | 31.85 | 6.00 | 191.08 | 4.00 | 13.78 | 491.00 |
| max | 40.00 | 7.00 | 249.50 | 5.00 | 17.90 | 735.80 |
