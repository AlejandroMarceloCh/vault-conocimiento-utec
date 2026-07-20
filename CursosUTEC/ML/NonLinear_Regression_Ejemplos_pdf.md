---
curso: ML
titulo: NonLinear_Regression_Ejemplos
slides: 10
fuente: NonLinear_Regression_Ejemplos.pdf
---

## Slide 1

CS3061 · Machine Learning · UTEC

# Regresión No Lineal

*Dos ejemplos explicados paso a paso*

Prof. Dr. Manuel Eduardo Loaiza Fernández

**EJEMPLO 1 — REGRESIÓN POLINOMIAL**

Temperatura vs Consumo de Energía

Modelo cuadrático: $\hat{y} = w_0 + w_1 x + w_2 x^2$

*¿A qué temperatura se consume menos energía?*

**EJEMPLO 2 — REGRESIÓN LOGARÍTMICA**

Días de Riego vs Altura de Planta

Modelo logarítmico: $\hat{y} = w_0 + w_1 \cdot \ln(x)$

*¿Cuánto crecerá la planta en el futuro?*

## Slide 2

# Ejemplo 1: Temperatura vs Consumo de Energía

**CONTEXTO DEL PROBLEMA**

En invierno se necesita calefacción y en verano aire acondicionado. La relación entre temperatura y consumo tiene forma de U — existe una temperatura óptima donde el consumo es mínimo.

**¿POR QUÉ GRADO 2?**

La forma en U es exactamente una parábola → polinomio de grado 2. Una línea recta no puede capturar que el consumo sube en ambos extremos de temperatura.

**DATASET — 10 OBSERVACIONES**

| 5°C | 10°C | 15°C | 18°C | 20°C |
|---|---|---|---|---|
| 310 kWh | 250 kWh | 200 kWh | 180 kWh | 170 kWh |

| 22°C | 25°C | 28°C | 32°C | 36°C |
|---|---|---|---|---|
| 175 kWh | 185 kWh | 210 kWh | 260 kWh | 320 kWh |

## Slide 3

# Distribución 2D — ¿Por qué cada modelo? ¿Qué es R²?

**Figura:** tres paneles de dispersión/curvas, eje X "Temperatura (°C)" (rango 5–36), eje Y "Consumo de energía (kWh)" (rango ~170–350).
- Panel 1 "① Distribución de los datos (puntos de muestra)": los 10 puntos del dataset, anotados con flechas "¿Forma en U? Polinomio grado 2", "← máx frío" (punto en 5°C, 310 kWh), "máx calor →" (punto en 36°C, 320 kWh), y "mínimo →≈20°C" señalando la zona baja de la curva.
- Panel 2 "② Lineal vs Cuadrático (¿cuál se ajusta mejor?)": los mismos puntos con dos curvas ajustadas — línea recta roja punteada "Lineal R²=0.002 ✗" (casi plana, no captura la forma) y curva verde "Cuadrático R²=0.9908 ✓" (forma de U que sigue los puntos).
- Panel 3 "③ ¿Qué es R²? R²=0.9908 — fracción explicada": los puntos reales (naranja), el modelo cuadrático (verde) y una línea punteada horizontal "Promedio ȳ=226"; una flecha vertical morada marca "SS_tot" (distancia entre un punto y el promedio).

Barra inferior: $R^2 = 1 - SS\_res/SS\_tot$ | R²=1: ajuste perfecto | R²=0: predice siempre ȳ | R²<0: peor que el promedio | Objetivo: R² > 0.90

## Slide 4

# Ejemplo 1: Proceso paso a paso

**1 — Elegir el modelo (Feature Engineering)**

$x \to [1, x, x^2]$
Agregar potencias como nuevas features

Vector de features:
$x=[1, 20, 400]$ para T=20°C

**2 — Construir la matriz X (N×3)**

$X = \begin{bmatrix} 1 & 5 & 25 \\ 1 & 10 & 100 \\ 1 & 20 & 400 \\ ... & ... & ... \end{bmatrix}$ (10 filas)

**3 — Solución analítica (Normal Equation)**

$W^* = (X^T X)^{-1} \cdot X^T \cdot y$

$w_0 = 423.04$
$w_1 = -24.17$
$w_2 = 0.59$

**4 — Evaluar el modelo (R² y predicciones)**

MSE = 25.98
R² = 0.9908 ← excelente

$\hat{y}(T=20°C) = 176.4$ kWh

## Slide 5

# Ejemplo 1: Resultado — Temperatura vs Consumo

**Figura:** gráfico de dispersión + curva, título "Regresión Polinomial — R² = 0.9908". Eje X "Temperatura (°C)" (5 a 35), eje Y "Consumo (kWh)" (175 a 350). Puntos azules "Datos reales" siguen una curva verde en forma de U, ecuación en el gráfico $\hat{y} = 423.04 - 24.17x + 0.59x^2$, etiqueta "R² = 0.9908". Una línea vertical punteada naranja marca "T óptima 20.5°C, 175 kWh" en el mínimo de la curva, con una flecha señalando ese punto.

**RESULTADO**

Modelo final:

$\hat{y} = 423.04 - 24.17 \cdot x + 0.59 \cdot x^2$

Métricas:

| R² | 0.9908 |
|---|---|
| MSE | 25.98 |
| MAE | 4.08 |

T. óptima: 20.4°C
Consumo mín: 176.3 kWh

Interpretación: x² captura la forma en U — cuando la temperatura se aleja de 20.4°C en cualquier dirección, el consumo sube. Imposible con regresión lineal simple.

## Slide 6

# Ejemplo 2: Días de Riego vs Altura de Planta

**CONTEXTO DEL PROBLEMA**

Las plantas crecen rápido al inicio y luego se desaceleran. No importa cuánto riegues después de cierto punto — la altura satura. Esta forma de saturación es exactamente logarítmica.

**¿POR QUÉ FUNCIÓN LOGARÍTMICA?**

ln(x) crece rápido al inicio y luego cada vez más lento. Feature engineering: transformar x → ln(x) convierte el problema en regresión lineal estándar.

**DATASET — 10 OBSERVACIONES**

| 1 día | 3 días | 7 días | 14 días | 21 días |
|---|---|---|---|---|
| 2.1 cm | 5.8 cm | 9.3 cm | 13.2 cm | 15.8 cm |

| 30 días | 45 días | 60 días | 90 días | 120 días |
|---|---|---|---|---|
| 18.1 cm | 20.9 cm | 22.5 cm | 24.8 cm | 26.1 cm |

## Slide 7

# Distribución 2D — ¿Por qué cada modelo? ¿Qué es R²?

**Figura:** tres paneles, eje X "Días de riego" (0 a 120), eje Y "Altura de planta (cm)" (0 a ~30).
- Panel 1 "① Distribución de los datos (puntos de muestra)": los 10 puntos del dataset, anotados "¿Crece y satura → Función ln(x)?", "Crece rápido al inicio" (señalando puntos iniciales bajos), "Satura → cada vez más lento" (señalando puntos finales que se aplanan).
- Panel 2 "② Lineal vs Logarítmico (¿cuál se ajusta mejor?)": puntos reales con línea recta roja punteada "Lineal R²=0.779 ✗" y curva azul "Logarítmico R²=0.9871 ✓" que sigue la saturación.
- Panel 3 "③ Truco: x→ln(x) lo lineariza. ¡Ahora es regresión lineal!": eje X transformado a "ln(días de riego)" (0 a 5), puntos "Datos (x→ln(x))" alineados sobre una recta azul "Línea recta R²=0.9871 ✓", con anotación "Feature Engineering: x → ln(x)".

Barra inferior: $R^2 = 1 - SS\_res/SS\_tot$ | R²=1: ajuste perfecto | R²=0: predice siempre ȳ | R²<0: peor que el promedio | Objetivo: R² > 0.90

## Slide 8

# Ejemplo 2: Proceso paso a paso

**1 — Feature Engineering: $x \to \ln(x)$**

Transformar cada dato:

Día 1 → ln(1) = 0.000
Día 7 → ln(7) = 1.946
Día 30 → ln(30) = 3.401
Día 90 → ln(90) = 4.500

**2 — Construir la matriz X (N×2)**

$X = \begin{bmatrix} 1 & 0.000 \\ 1 & 1.099 \\ 1 & 1.946 \\ 1 & 2.639 \\ ... & ... \end{bmatrix}$ (10 filas)

**3 — Solución analítica (Normal Equation)**

$W^* = (X^T X)^{-1} \cdot X^T \cdot y$

$w_0 = 0.3887$
$w_1 = 5.2771$

$\hat{y} = 0.39 + 5.28 \cdot \ln(x)$

**4 — Predicciones futuras (extrapolación)**

Día 150: ln(150)=5.01
$\hat{y} = 0.39+5.28\cdot5.01 = 26.8$ cm

Día 365: ln(365)=5.90
$\hat{y} = 0.39+5.28\cdot5.90 = 31.5$ cm

## Slide 9

# Ejemplo 2: Resultado — Días de Riego vs Altura

**Figura:** gráfico de dispersión + curva, título "Regresión Logarítmica — R² = 0.9871". Eje X "Días de riego" (0 a 350), eje Y "Altura de planta (cm)" (-5 a 30). Puntos azules "Datos reales" siguen una curva verde ascendente que satura, ecuación $\hat{y} = 0.39 + 5.28 \cdot \ln(x)$, etiqueta "R² = 0.9871". Tres puntos de predicción extrapolados marcados como rombos: rojo "150d→26.8cm", amarillo "180d→27.8cm", morado "365d→31.5cm".

**RESULTADO**

Modelo final:

$\hat{y} = 0.39 + 5.28 \cdot \ln(x)$

Métricas:

| R² | 0.9871 |
|---|---|
| MSE | 0.773 |
| MAE | 0.718 |

Predicciones:
150 días: 26.8 cm
180 días: 27.8 cm
365 días: 31.5 cm

Clave: transformar x → ln(x) convierte la curva en línea recta (panel derecho). El mismo algoritmo de regresión lineal funciona — solo cambia la feature.

## Slide 10

# Comparación final de los dos ejemplos

| | Ejemplo 1 — Energía | Ejemplo 2 — Planta | Diferencia |
|---|---|---|---|
| Fenómeno | Calor/frío → más consumo | Saturación del crecimiento | Formas distintas |
| Modelo | $\hat{y} = w_0+w_1x+w_2x^2$ | $\hat{y} = w_0+w_1\cdot\ln(x)$ | Polin. vs Logar. |
| Feature Eng. | $x \to [1, x, x^2]$ | $x \to [1, \ln(x)]$ | Potencias vs ln |
| Parámetros | 3 pesos: $w_0,w_1,w_2$ | 2 pesos: $w_0,w_1$ | Más grado=más pesos |
| R² | 0.9908 | 0.9871 | Ambos excelentes |
| Optimización | Normal Equation | Normal Equation | ¡Mismo algoritmo! |

Feature Engineering transforma el problema → mismo algoritmo GD/Normal Equation resuelve → R²>0.98
