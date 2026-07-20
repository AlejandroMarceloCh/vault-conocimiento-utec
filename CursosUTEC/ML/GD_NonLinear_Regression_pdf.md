---
curso: ML
titulo: GD_NonLinear_Regression
slides: 8
fuente: GD_NonLinear_Regression.pdf
---

## Slide 1

Regresion No Lineal

Gradient Descent — Dos ejemplos paso a paso

EJEMPLO 3 — POLINOMIAL + GD

Temperatura vs Consumo de Energia

Modelo: y = w0 + w1*x + w2*x2

Mismo problema que Ej.1 — pesos con GD

EJEMPLO 4 — LOGARITMICA + GD

Dias de Riego vs Altura de Planta

Modelo: y = w0 + w1*ln(x)

Mismo problema que Ej.2 — pesos con GD

Mismos modelos que Ej.1 y Ej.2 — diferencia: los pesos wi se obtienen con Gradient Descent en lugar de la Ecuacion Normal $W^* = (X^\top X)^{-1} X^\top y$

## Slide 2

Ejemplo 3: Temperatura vs Consumo — GD vs Ecuacion Normal

MISMO PROBLEMA QUE EJ.1

Dataset identico al Ejemplo 1. La diferencia es el metodo de optimizacion: en Ej.1 usamos la Ecuacion Normal (solucion cerrada), aqui usamos Gradient Descent iterativo.

IDEA CENTRAL DE GD

Partir de w=[0,0,0], calcular el gradiente de la Loss, dar un paso en la direccion contraria. Repetir hasta converger. El resultado debe ser identico a la Ecuacion Normal.

DATASET — 10 OBSERVACIONES (identico Ej.1)

**Figura:** Grilla de 10 tarjetas con pares Temperatura (°C) → Consumo (kWh): 5°C→310 kWh, 10°C→250 kWh, 15°C→200 kWh, 18°C→180 kWh, 20°C→170 kWh, 22°C→175 kWh, 25°C→185 kWh, 28°C→210 kWh, 32°C→260 kWh, 36°C→320 kWh.

## Slide 3

Ejemplo 3: Gradient Descent sobre Regresion Polinomial

1 Feature Engineering (igual que Ej.1)

phi(x) = [1, x, x^2] -> vector de features
Matriz X: N x 3 (10 filas, 3 columnas)
Normalizar x: xn = (x - mean(x)) / std(x)
Normalizar y: yn = (y - mean(y)) / std(y)
Necesario: x^2 llega a 1296 -> GD diverge sin norm.

2 Gradiente del MSE (Loss = mean((yhat-y)^2))

yhat = X @ w (producto matricial)
Loss = (1/N) * sum((yhat - yn)^2)
grad = (2/N) * X^T @ (yhat - yn)
grad[0]: respecto a w0 (bias)
grad[1]: respecto a w1 (term. lineal)
grad[2]: respecto a w2 (term. cuadratico)

3 GD loop — 8000 epocas (lr = 0.05, espacio norm.)

Epoch 1: w0= 0.000 w1= 0.004 w2= 0.106 L=1.000
Epoch 100: w0=-0.917 w1= 0.138 w2= 0.923 L=0.009
Epoch 500: w0=-0.933 w1= 0.140 w2= 0.933 L=0.009
Epoch 1000: w0=-0.933 w1= 0.140 w2= 0.933 L=0.009
Epoch 8000: w0=-0.933 w1= 0.140 w2= 0.933 L=0.009

4 Resultado y comparacion (escala original)

GD: w0=423.0 w1=-24.2 w2=0.592
Ec.Normal: w0=423.0 w1=-24.2 w2=0.592
R2 = 0.9908 (identico al Ej.1)
MSE = 25.98 kWh^2
T optima: 20.4 C | Consumo min: 176.3 kWh

Clave: GD requiere normalizar features cuando hay terminos cuadraticos (x^2 hasta 1296 vs x hasta 36). Sin normalizacion el gradiente explota y los pesos divergen a NaN.

## Slide 4

Ejemplo 3: Resultado — Temperatura vs Consumo con GD

**Figura:** Grafico de dispersion + curva. Titulo "Polinomial Grado 2 — GD | R² = 0.9908". Eje X: Temperatura (°C), de 5 a 36. Eje Y: Consumo (kWh), de 175 a 350. Puntos celestes "Datos reales" siguiendo forma de parabola con minimo cerca de 20°C. Curva verde "GD: $\hat{y} = w_0 + w_1 x + w_2 x^2$" ajustando los puntos. Linea vertical punteada naranja marcando T óptima = 20.4°C, con flecha señalando el punto minimo "T óptima 20.4°C, 176.3 kWh". Recuadro verde "R² = 0.9908".

RESULTADO
Modelo final (GD): y = 423.04 - 24.17*x + 0.59*x^2

Metricas:
R2 0.9908
MSE 25.98
MAE 4.08

T. optima:
20.4°C
176.3 kWh min

GD convergio exactamente a la misma solucion que la Ecuacion Normal. R2=0.9908 identico. Conclusion: GD es un metodo alternativo valido cuando la matriz no es invertible o N es enorme.

## Slide 5

Ejemplo 4: Dias de Riego vs Altura — GD vs Ecuacion Normal

MISMO PROBLEMA QUE EJ.2

Dataset identico al Ejemplo 2. Feature engineering: transformar x a ln(x). Luego regresion lineal en el espacio transformado. Los pesos w0 y w1 se obtienen ahora con GD.

POR QUE GD AQUI TAMBIEN?

Una vez aplicada la transformacion z=ln(x), el modelo es lineal en los parametros. GD sobre este espacio transformado funciona perfectamente y converge al mismo resultado que $W^* = (X^\top X)^{-1} X^\top y$.

DATASET — 10 OBSERVACIONES (identico Ej.2)

**Figura:** Grilla de 10 tarjetas con pares Dias de riego → Altura de planta: 1 dia→2.1 cm, 3 dias→5.8 cm, 7 dias→9.3 cm, 14 dias→13.2 cm, 21 dias→15.8 cm, 30 dias→18.1 cm, 45 dias→20.9 cm, 60 dias→22.5 cm, 90 dias→24.8 cm, 120 dias→26.1 cm.

## Slide 6

Ejemplo 4: Gradient Descent sobre Regresion Logaritmica

1 Feature Engineering (igual que Ej.2)

Transformar: z = ln(x)
Dia 1 -> ln(1) = 0.000
Dia 7 -> ln(7) = 1.946
Dia 30 -> ln(30) = 3.401
Matriz X: N x 2 [1, ln(x)]
Sin normalizacion extra (ln es suave)

2 Gradiente del MSE (modelo lineal en z)

yhat = w0 + w1*ln(x) = X @ w
Loss = (1/N) * sum((yhat - y)^2)
grad = (2/N) * X^T @ (yhat - y)
grad[0] = (2/N) * sum(yhat - y)
grad[1] = (2/N) * sum((yhat-y)*ln(x))
Gradientes exactos — no hay aprox.

3 GD loop — 5000 epocas (lr = 0.01)

Epoch 1: w0= 0.0000 w1= 0.0000 L=311.53
Epoch 100: w0= 0.5468 w1= 5.2332 L=0.7776
Epoch 500: w0= 0.3926 w1= 5.2760 L=0.7726
Epoch 1000: w0= 0.3893 w1= 5.2770 L=0.7726
Epoch 3000: w0= 0.3887 w1= 5.2771 L=0.7726

4 Resultado y comparacion (convergencia perfecta)

GD: w0=0.3887 w1=5.2771
Ec.Normal: w0=0.3887 w1=5.2771
R2 = 0.9871 (identico al Ej.2)
MSE = 0.773 cm^2
Pred 150d: 26.83 cm | 365d: 31.52 cm

Feature engineering z=ln(x) hace el modelo lineal en los parametros. Por eso GD con gradiente (2/N)*X^T*(yhat-y) converge exactamente igual que la Ecuacion Normal. No se necesita normalizacion adicional.

## Slide 7

Ejemplo 4: Resultado — Dias de Riego vs Altura con GD

**Figura:** Grafico de dispersion + curva. Titulo "Logarítmica — GD | R² = 0.9871". Eje X: Dias de riego, de 0 a 350. Eje Y: Altura de planta (cm), de -5 a 30. Puntos celestes "Datos reales" con crecimiento rapido inicial y luego aplanamiento (forma logaritmica). Curva verde "GD: $\hat{y} = w_0 + w_1 \ln(x)$" ajustando los puntos. Tres puntos diamante de prediccion extrapolada: naranja "150d→26.8cm", amarillo "180d→27.8cm", morado "365d→31.5cm". Recuadro verde "R² = 0.9871".

RESULTADO
Modelo final (GD): y = 0.39 + 5.28*ln(x)

Metricas:
R2 0.9871
MSE 0.773
MAE 0.750

Predicciones:
150 dias: 26.8 cm
180 dias: 27.8 cm
365 dias: 31.5 cm

GD convergio a la misma solucion que la Ecuacion Normal. La clave: feature engineering z=ln(x) hace el problema lineal, y GD sobre features lineales siempre converge al optimo global.

## Slide 8

Comparacion final — GD vs Ecuacion Normal (mismos modelos)

**Figura:** Tabla comparativa con columnas [vacio / Ej.1/Ej.3 — Polinomial / Ej.2/Ej.4 — Logaritmica / Diferencia] y filas:
- Modelo: $y = w_0 + w_1 x + w_2 x^2$ | $y = w_0 + w_1 \ln(x)$ | Feature eng.
- Pesos (Ec.N): $w = (X^\top X)^{-1} X^\top y$ | $w = (X^\top X)^{-1} X^\top y$ | Formula cerrada
- Pesos (GD): $w \mathrel{-}= lr \cdot X^\top (Xw-y)$ | $w \mathrel{-}= lr \cdot X^\top (Xw-y)$ | Mismo loop GD
- Normalizar?: SI — x^2 hasta 1296 | NO — ln es suave | Depende del modelo
- lr optimo: 0.05 (espacio norm.) | 0.01 | Diferente escala
- Epocas: ~500 para converger | ~1000 para converger | Log es mas lento
- R2 final: 0.9908 | 0.9871 | Identico Ej.1/Ej.2
- Conclusion: GD == Ec.Normal | GD == Ec.Normal | Mismo resultado!

GD converge al mismo minimo que la Ecuacion Normal cuando la Loss es convexa — pero escala a millones de datos y modelos donde $(X^\top X)^{-1}$ no existe
