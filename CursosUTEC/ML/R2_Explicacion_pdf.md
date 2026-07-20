---
curso: ML
titulo: R2_Explicacion
slides: 6
fuente: R2_Explicacion.pdf
---

## Slide 1

# R² Coeficiente de Determinación

¿De dónde sale? · ¿Qué mide? · ¿Cómo se interpreta?

**Pregunta**
¿Qué fracción de Y explica el modelo?

**Rango**
(−∞, 1] → meta: R² > 0.90

**Fórmula**
R² = 1 − SS_res / SS_tot

**R² Vs MSE**
Adimensional — comparable entre datasets

## Slide 2

# 1. De dónde sale R² — las dos sumas de cuadrados

**SS_TOT — VARIABILIDAD TOTAL DE Y**

Imagina que no tienes modelo — la mejor predicción sin saber X es predecir siempre ȳ. La variabilidad total mide qué tan dispersos están los datos alrededor de ese promedio.

ȳ (media de Y):
$\bar{y} = (1/N) \cdot \sum y_i$ = promedio de todos los valores reales de Y

$SS\_tot = \sum (y_i - \bar{y})^2$

Distancias de cada punto al promedio ȳ → variabilidad total de Y

**SS_RES — LO QUE EL MODELO NO EXPLICA**

Con el modelo entrenado, los residuos son las distancias entre los valores reales y las predicciones.

$SS\_res = \sum (y_i - \hat{y}_i)^2$

Nota: SS_res = N · MSE ← es el MSE escalado
→ lo que queda sin explicar después del modelo

**LA DERIVACIÓN DE R² EN 3 PASOS**

1. La fracción sin explicar:
SS_res / SS_tot

2. La fracción explicada:
1 − SS_res / SS_tot

3. Eso es R²:
R² = 1 − SS_res / SS_tot

$$R^2 = 1 - \frac{SS\_res}{SS\_tot}$$ = fracción de variabilidad de Y que el modelo SÍ explica

## Slide 3

# La pregunta que R² responde

¿Qué fracción de la variabilidad de Y explica mi modelo?

**CASO IDEAL — MODELO PERFECTO**

Si el modelo predice sin error:

$\hat{y}_i = y_i$ para todo i

Los residuos son cero:

SS_res = 0 ($y_i - \hat{y}_i = 0$)

R² = 1 − 0/SS_tot = 1.0

El modelo explica el 100% de la variabilidad

**VS**

**CASO INÚTIL — PREDICE SIEMPRE Ȳ**

Si el modelo predice siempre el promedio:

$\hat{y}_i = \bar{y}$ para todo i

Residuos = variabilidad total:

SS_res = SS_tot

R² = 1 − SS_tot/SS_tot = 0

El modelo no aporta nada nuevo sobre el promedio

R² mide qué tan mejor es el modelo comparado con "predecir siempre el promedio" — la estrategia más tonta posible

## Slide 4

# 2. Relación entre R² y MSE

**LA CONEXIÓN MATEMÁTICA**

Como SS_res = N · MSE y SS_tot = N · Var(y), se puede reescribir:

$$R^2 = 1 - MSE / Var(y)$$

**MSE — ERROR ABSOLUTO**

Mide el error en las unidades al cuadrado de Y.

$MSE = (1/N) \cdot \sum (y_i - \hat{y}_i)^2$

Problema: depende de la escala.
No puedes comparar MSE entre datasets con unidades distintas.

Ejemplo:
Modelo notas → MSE = 3.2 puntos²
Modelo precios → MSE = 15,000 soles²
¿Cuál es mejor? → IMPOSIBLE saberlo solo con MSE

**R² — COMPARACIÓN RELATIVA**

Normaliza el MSE por la varianza de Y. Resultado: adimensional.

$R^2 = 1 - MSE/Var(y)$

Ventaja: comparable entre cualquier dataset.
Siempre en el rango (−∞, 1].

Ejemplo:
Modelo notas → R² = 0.85
Modelo precios → R² = 0.92
¿Cuál es mejor? → Precios (92% variabilidad explicada)

Durante el entrenamiento se minimiza MSE (tiene gradiente). R² se calcula al final como métrica de evaluación — no se optimiza directamente.

## Slide 5

# 3. Interpretación de los valores de R²

**Figura:** Barra de escala horizontal en 7 segmentos de color (de rojo a verde) con los valores de referencia: < 0, 0, 0.3, 0.5, 0.7, 0.9, 1.0, usada como eje visual para ubicar cada caso de la tabla de abajo.

**R² < 0**
El modelo es PEOR que predecir siempre el promedio ȳ
horas_sueño → nota_final (R²=−0.134)
Usar horas de sueño empeora la predicción vs solo decir "todos sacan 15"

**R² ≈ 0**
El modelo no aporta nada — equivale a predecir siempre ȳ
Temperatura vs Consumo con modelo LINEAL (R²=0.002)
La línea recta es prácticamente inútil para esta relación

**R² ≈ 0.5**
El modelo explica la mitad de la variabilidad
horas_estudio → nota_final (R²=0.573)
Conocer las horas de estudio explica el 57% de por qué unos alumnos sacan más nota que otros

**R² > 0.9**
Excelente — el modelo captura casi toda la variabilidad
Temperatura vs Consumo con modelo CUADRÁTICO (R²=0.991)
Días de riego vs Altura con ln(x) (R²=0.987)

**R² = 1.0**
Perfecto — predicción sin error (raro en datos reales)
Solo ocurre cuando $\hat{y}_i = y_i$ para todo i
En la práctica indica sobreajuste (overfitting)

## Slide 6

# Resumen — todo lo que necesitas saber sobre R²

$$R^2 = 1 - \frac{SS\_res}{SS\_tot} = 1 - MSE/Var(y)$$

**SS_TOT**
Variabilidad total
$\sum (y_i - \bar{y})^2$
Qué tan dispersos están los datos de Y

**SS_RES**
Variabilidad NO explicada
$\sum (y_i - \hat{y}_i)^2$ = N·MSE
Lo que el modelo no captura

**R²=1**
Modelo perfecto
SS_res = 0
→ predice sin ningún error

**R²=0**
Modelo inútil
Equivale a predecir siempre ȳ
→ no aporta nada nuevo

**R²<0**
Modelo pésimo
Peor que predecir ȳ
→ feature perjudica la predicción

**META**
R² > 0.90 en la práctica
Se calcula en TEST, no en training
No se optimiza directamente

"R² = fracción de la variabilidad de Y que el modelo explica mejor que predecir siempre el promedio"
