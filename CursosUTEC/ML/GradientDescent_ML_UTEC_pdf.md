---
curso: ML
titulo: GradientDescent_ML_UTEC
slides: 17
fuente: GradientDescent_ML_UTEC.pdf
---

## Slide 1

CS3061 · Machine Learning

# Gradient Descent

Regresión Lineal Uni y Multivariable

Algoritmo completo · GD · SGD · Mini-Batch · Forma matricial

## Slide 2

# Contenido de la clase

01 Framework Mitchell (T, P, E)

02 Modelo lineal y función de costo MSE

03 Gradiente: derivadas parciales

04 Gradient Descent — algoritmo paso a paso

05 GD · SGD · Mini-Batch: diferencias

06 Regresión multivariable: notación vectorial

07 Gradiente matricial ∇wJ y solución analítica

08 Normalización Z-score: por qué es obligatoria

## Slide 3

# 01 · Framework Mitchell

Antes de entrenar cualquier modelo, debes definir tres elementos

**T**
Tarea
Predecir ŷ dado x
Clasificación o regresión
Ejemplo: predecir precio de casa

**P**
Medida de desempeño
MSE, MAE, R², Accuracy
Mide qué tan bien predice el modelo en datos nuevos

**E**
Experiencia (datos)
Dataset: pares (x, y)
Features de entrada
Etiqueta / valor esperado

Mitchell (1997): "A computer program learns from experience E with respect to task T and performance measure P"

## Slide 4

# 02 · Modelo lineal e inicialización

$\hat{y} = w_1 \cdot x + w_0$

$w_1$ = pendiente (slope)     $w_0$ = intercepto (bias)

**Inicialización**
$w_1 = 0$
$w_0 = 0$

**PROPIEDADES**
$w_1 > 0$ — Relación positiva
$w_1 < 0$ — Relación negativa
$w_0$ — Valor cuando x=0
$\hat{y}$ — Predicción del modelo

**Figura:** gráfico cartesiano con eje vertical $\hat{y}$ y eje horizontal $x$. Puntos de datos dispersos (azules) siguiendo una tendencia ascendente. Una línea roja horizontal en la parte inferior etiquetada "$w_1=0, w_0=0$ (inicio)" representa el modelo antes de entrenar. Una línea discontinua amarilla ajustada a los puntos, etiquetada "$\hat{y} = w_1x + w_0$ (final)", representa el modelo ya entrenado que se ajusta a la nube de puntos.

## Slide 5

# 02 · Función de costo: MSE y MAE

**MSE — MEAN SQUARED ERROR**

$J(w) = (1/N) \cdot \Sigma_i (y_i - \hat{y}_i)^2$

Penaliza errores grandes desproporcionadamente (cuadrado)

**MAE — MEAN ABSOLUTE ERROR**

$J(w) = (1/N) \cdot \Sigma_i |y_i - \hat{y}_i|$

Todos los errores pesan proporcionalmente a su tamaño

**COMPARACIÓN CON EJEMPLO: ERRORES = [1, 1, 1, 1, 10]**

**Figura:** tabla comparativa con columnas MSE, MAE y Observación. Fila "Sin outlier [1,1,1,1,1]": MSE=1.00, MAE=1.00, Observación="Idénticos sin outliers". Fila "Con outlier [1,1,1,1,10]": MSE=20.80, MAE=2.80, Observación="MSE domina por outlier". Fila "Diferencia": MSE=19.8×, MAE=1.4×, Observación="MSE más sensible".

Usar MSE cuando errores grandes son inaceptables · Usar MAE para robustez ante outliers

## Slide 6

# 03 · El gradiente: intuición geométrica

**ANALOGÍA: BAJAR UNA MONTAÑA CON OJOS VENDADOS**

- Estás parado en un punto de la superficie J(w)
- Solo sientes si el suelo sube o baja en cada dirección
- El gradiente ∇J indica la dirección de mayor subida
- Para bajar: muévete en dirección contraria al gradiente
- Cada paso te acerca al mínimo (valle)

**Figura:** curva en forma de U (parábola) titulada "SUPERFICIE J(w) — CURVA DE COSTO (FORMA U)", eje vertical J, eje horizontal w. Un punto verde en el fondo del valle marcado "w*" (mínimo). Un punto naranja sobre la curva a la derecha del mínimo marcado "w actual", del cual sale una flecha naranja ascendente etiquetada "∇J (sube)" y una flecha roja descendente etiquetada "$-\alpha\nabla J$ (baja)" apuntando hacia el mínimo.

## Slide 7

# 03 · Derivadas parciales de J(w)

Calculadas usando la regla de la cadena sobre $MSE = (1/N)\cdot\Sigma(y_i - w_1x_i - w_0)^2$

$\partial J/\partial w_1 = (-2/N) \cdot \Sigma_i x_i \cdot (y_i - \hat{y}_i)$

$\partial J/\partial w_0 = (-2/N) \cdot \Sigma_i (y_i - \hat{y}_i)$

**OBSERVACIÓN CLAVE**
∂J/∂w₁ incluye xᵢ como factor
∂J/∂w₀ solo usa el error directo (equivale a xᵢ = 1 por el bias trick)

**SIGNO NEGATIVO: POR QUÉ IMPORTA**
El −2/N viene de la derivada de (y−ŷ)²
El signo indica: si el error es positivo, el gradiente empuja a w hacia arriba

## Slide 8

# 04 · Gradient Descent — algoritmo completo

**1 — Inicializar**
$w_1 \leftarrow 0, \quad w_0 \leftarrow 0$

**2 — Forward pass**
$\hat{y}_i \leftarrow w_1 \cdot x_i + w_0$ para todo $i = 1..N$

**3 — Calcular costo**
$J \leftarrow (1/N)\cdot\Sigma(y_i - \hat{y}_i)^2$

**4 — Calcular grad.**
$\partial J/\partial w_1 \leftarrow -2/N\cdot\Sigma\, x_i(y_i-\hat{y}_i)$
$\partial J/\partial w_0 \leftarrow -2/N\cdot\Sigma\, (y_i-\hat{y}_i)$

**5 — Actualizar**
$w_1 \leftarrow w_1 - \alpha\cdot\partial J/\partial w_1$
$w_0 \leftarrow w_0 - \alpha\cdot\partial J/\partial w_0$

**6 — Criterio parada**
Si $|J_t - J_{t-1}| < \varepsilon \rightarrow$ terminar
Si no → volver al paso 2

α = learning rate · ε = tolerancia de convergencia · N = número de muestras

## Slide 9

# 05 · GD · SGD · Mini-Batch: diferencias

**BATCH — Gradient Descent (GD)**
```
por cada iteración:
  grad ← gradiente(TODOS los datos)
  w ← w − α·grad
```
VENTAJAS
• Gradiente exacto
• Trayectoria suave
• Convergencia garantizada

CUÁNDO USAR
Datasets pequeños
Regresión simple

**STOCHASTIC — Stochastic GD (SGD)**
```
por cada época:
  shuffle(datos)
  por cada muestra i:
    grad ← gradiente(muestra i)
    w ← w − α·grad
```
VENTAJAS
• N actualizaciones/época
• Muy rápido para N grande
• Puede salir de mínimos locales

CUÁNDO USAR
Datasets grandes
Aprendizaje online

**MINI-BATCH — Mini-Batch GD**
```
por cada época:
  shuffle(datos)
  por lotes de k muestras:
    grad ← gradiente(lote)
    w ← w − α·grad
```
VENTAJAS
• Balance ruido/velocidad
• Eficiente en GPU/CPU
• Estándar en deep learning

CUÁNDO USAR
Deep learning
Batch típico: 32, 64, 128

En la práctica: Mini-Batch GD con batch=32 es el estándar en redes neuronales y modelos grandes

## Slide 10

# 06

Regresión Multivariable

Del modelo escalar al modelo vectorial y matricial

## Slide 11

# 06 · De 1D a múltiples variables

**MODELO UNIVARIABLE (1 FEATURE)**

$\hat{y} = w_0 + w_1 \cdot x_1$

2 parámetros: w₀ (bias), w₁

Ejemplo: precio = w₀ + w₁·(m²)

**MODELO MULTIVARIABLE (D FEATURES)**

$\hat{y} = w_0 + w_1x_1 + w_2x_2 + ... + w_dx_d$

d+1 parámetros: w₀,w₁,...,wd

Ejemplo: precio = w₀ + w₁·m² + w₂·hab + w₃·dist

**BIAS TRICK — UNIFICAR W₀ EN EL VECTOR**

Agregar $x_0 = 1$ → $\hat{y} = w^Tx$ donde:

$w = [w_0, w_1, w_2, ..., w_d]^T$ (vector de pesos, dimensión d+1)

$x = [1, x_1, x_2, ..., x_d]^T$ (vector de features con bias)

$w^Tx = \Sigma_j w_jx_j$

El bias trick permite que todos los parámetros se actualicen con la misma regla de GD

## Slide 12

# 06 · Representación matricial del dataset

**MATRIZ X (N×(D+1)) — DATOS DE ENTRADA**

$X =$
```
[ 1   x1(1)   x2(1)   ···   xd(1) ]
[ 1   x1(2)   x2(2)   ···   xd(2) ]
[              ···                ]
[ 1   x1(N)   x2(N)   ···   xd(N) ]
```

↑ columna de unos = bias trick
N filas = N muestras
d+1 columnas = d features + bias

**VECTOR W (D+1) — PARÁMETROS**

$w = [w_0, w_1, w_2, ..., w_d]^T$

**VECTOR Y (N) — VALORES REALES**

$y = [y^{(1)}, y^{(2)}, ..., y^{(N)}]^T$

Ejemplo casa 3: $y^{(3)}$ = 220,000 USD

Predicción vectorizada: $\hat{y} = X \cdot w$
(N predicciones en una sola operación matricial)

## Slide 13

# 07 · Gradiente matricial ∇wJ

Generalizando las derivadas parciales al vector completo de pesos

**MSE EN FORMA MATRICIAL**

$J(w) = (1/N) \cdot (y - Xw)^T (y - Xw) = (1/N) \cdot ||y - Xw||^2$

**GRADIENTE VECTORIAL — DERIVADA DE J RESPECTO AL VECTOR W COMPLETO**

$\nabla_wJ(w) = (-2/N) \cdot X^T (y - Xw) = (-2/N) \cdot X^Te$

**Xᵀ (D+1 × N)**
Transpuesta de la matriz de datos. Actúa como "colector de errores"

**e = y − Xw (N × 1)**
Vector de errores: diferencia entre valores reales y predichos

**ACTUALIZACIÓN VECTORIAL**
$w \leftarrow w - \alpha \cdot \nabla_wJ$
Una línea para todos los pesos

∇wJ es un vector de dimensión (d+1) — una derivada parcial por cada peso simultáneamente

## Slide 14

# 07 · GD multivariable — algoritmo vectorizado

**PSEUDOCÓDIGO GD MULTIVARIABLE**
```
Entrada: X (N×d+1), y (N), α, ε

inicializar w ← [0, 0, ..., 0]ᵀ

mientras no converja:

    e ← y − X·w            # errores (N×1)

    ∇w ← (−2/N)·Xᵀ·e       # gradiente (d+1)

    w ← w − α·∇w           # actualizar pesos

    si ||∇w|| < ε → parar

retornar w
```

**ESCALAR (1 FEATURE)**
$\partial J/\partial w_1 = -2/N\cdot\Sigma\, x_i\cdot e_i$
$\partial J/\partial w_0 = -2/N\cdot\Sigma\, e_i$

$w_1 \leftarrow w_1 - \alpha\cdot\partial J/\partial w_1$
$w_0 \leftarrow w_0 - \alpha\cdot\partial J/\partial w_0$

**VECTORIAL (D FEATURES)**
$\nabla w = (-2/N)\cdot X^T\cdot e$

$w \leftarrow w - \alpha\cdot\nabla w$

¡Una línea por regla!
Escala a d=10,000

## Slide 15

# 07 · Solución analítica: Normal Equation

Igualando ∇wJ = 0 y despejando w directamente — sin iteraciones

$w^* = (X^TX)^{-1} \cdot X^T \cdot y$

**DERIVACIÓN EN 3 PASOS**

$\nabla_wJ = (-2/N)\cdot X^T(y-Xw) = 0$

$X^Ty = X^TXw$

$w^* = (X^TX)^{-1}\cdot X^Ty$ ← multiplicar por $(X^TX)^{-1}$

**GD VS SOLUCIÓN ANALÍTICA**

**Figura:** tabla comparativa con columnas "GD / SGD" y "Normal Equation". Fila "Resultado": GD/SGD="Aproximado (itera)", Normal Equation="Exacto (una operación)". Fila "Escala a d grande": GD/SGD="✓ Sí (O(d) por iter)", Normal Equation="✗ No (O(d³) inversión)". Fila "Uso en ML real": GD/SGD="Redes neuronales, big data", Normal Equation="Regresión lineal, d < 1000".

## Slide 16

# 08 · Normalización Z-score — por qué es obligatoria

**EL PROBLEMA SIN NORMALIZAR**

Feature x₁ = m² → escala 50–250
Feature x₂ = hab → escala 1–6

$\partial J/\partial w_1 \approx 120 \cdot error$
$\partial J/\partial w_2 \approx 3 \cdot error$

¡w₁ da pasos 40× más grandes!
Con mismo α: GD diverge

**Z-SCORE: LA SOLUCIÓN**

$x'_j = (x_j - \mu_j) / \sigma_j$

Resultado:
• Media = 0
• Desv. estándar = 1
• Todas en misma escala
• GD usa α=0.05 sin problemas

**PROCEDIMIENTO CORRECTO**

Calcular μⱼ y σⱼ SOLO del training set

Normalizar: x'ⱼ = (xⱼ−μⱼ)/σⱼ al train y test

Entrenar el modelo con datos normalizados

Para datos nuevos: usar los MISMOS μⱼ y σⱼ del training

⚠ Data leakage: NUNCA recalcules μ y σ con datos de test — contamina la evaluación del modelo

## Slide 17

# Resumen: proceso completo de Gradient Descent

**ALGORITMO COMPLETO (ESCALAR Y VECTORIAL)**
```
# Inicializar
w ← 0 ( w ← vector ceros)

# Normalizar
X_norm ← (X − μ) / σ

# Loop principal
mientras no converja:

  # Forward: predicciones
  ŷ ← X·w   ( ŷ = w1x + w0)

  # Costo
  J ← (1/N)||y − ŷ||²

  # Gradiente
  ∇w ← (−2/N)·Xᵀ·(y−ŷ)

  # Actualizar
  w ← w − α·∇w

  si |ΔJ| < ε → parar

retornar w
```

**T, P, E**
Definir tarea, métrica y experiencia primero

**α**
Learning rate
Tamaño del paso en GD

**MSE**
$J = (1/N)\cdot\Sigma(y_i-\hat{y}_i)^2$
Función de costo a minimizar

**Z-score**
$x'=(x-\mu)/\sigma$
Obligatorio para GD iterativo

**∇wJ**
$(-2/N)\cdot X^T\cdot e$
Dirección de mayor subida

**(XᵀX)⁻¹Xᵀy**
Solución analítica exacta
Solo si d es pequeño
