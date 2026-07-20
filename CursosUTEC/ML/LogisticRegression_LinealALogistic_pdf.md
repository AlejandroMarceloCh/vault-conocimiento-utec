---
curso: ML
titulo: LogisticRegression_LinealALogistic
slides: 10
fuente: LogisticRegression_LinealALogistic.pdf
---

## Slide 1

De Regresión Lineal a Logistic Regression

¿Por qué necesitamos el Sigmoid y cómo interpretarlo?

## Slide 2

El Problema: Regresión Lineal para Clasificar

Queremos predecir si un estudiante APRUEBA (1) o REPRUEBA (0) según las horas de estudio.

**Figura:** Dos gráficos de dispersión lado a lado, eje X "Horas de estudio" (0 a 7), eje Y "¿Aprobó?" (−0.4 a 1.4). Puntos rojos = Reprobó (t=0), puntos azules = Aprobó (t=1). Izquierda: "Regresión Lineal para clasificar" — muestra una recta de regresión lineal naranja ajustada a los puntos, que sube desde valores negativos (<0, zona sombreada roja "< 0 ⚠") pasando por los puntos hasta superar 1 (zona sombreada roja "> 1 ⚠") en horas altas. Derecha: "Lo que necesitamos: valores en [0,1]" — los mismos puntos con una banda verde sombreada entre 0 y 1 marcada "Necesitamos predicciones entre 0 y 1".

Conclusión: Regresión Lineal puede predecir valores fuera de [0,1] — no válidos como probabilidades.

## Slide 3

La Solución: Función Sigmoid

$\sigma(z) = \dfrac{1}{1+\exp(-z)}$ con $z = w^Tx + w_0$

**Figura:** Dos gráficos lado a lado. Izquierda: "Función Sigmoid σ(z) = 1/(1+e⁻ᶻ)", eje X "z = w·x + w₀" (−8 a 8), eje Y "σ(z)" (0 a 1). Curva sigmoide en azul, con línea punteada horizontal en y=0.5 marcada "y = 0.5 (Decision Boundary)", líneas guía en z=0/σ=0.5, anotaciones "z → -∞, σ → 0" y "z → +∞, σ → 1", área bajo la curva sombreada en azul claro. Derecha: "Sigmoid vs sign(·)", eje X "z" (−6 a 6), eje Y (−1 a 1). Curva sigmoide azul continua etiquetada "Suave y diferenciable ✅" y función escalón sign(z) en rojo punteado (salta de −1 a 1 en z=0) etiquetada "No diferenciable en z=0 ❌".

El Sigmoid comprime cualquier valor z en (−∞, +∞) al intervalo [0, 1] — interpretable como probabilidad.

## Slide 4

Modelo de Logistic Regression

$y(x) = \sigma(w^Tx + w_0) \Rightarrow p(C=0 \mid x) \in [0,1]$

**Figura:** Gráfico "Logistic Regression: P(aprobar)" a la izquierda, eje X "Horas de estudio" (0 a 6), eje Y "P(aprobar | horas)" (0 a 1.0). Curva sigmoide azul ajustada a los puntos (rojos = Reprobó t=0, azules = Aprobó t=1), línea horizontal punteada gris en 0.5, línea vertical naranja punteada marcando "Decision Boundary ≈ 2.7h". A la derecha, tabla "Predicciones del modelo" con columnas Horas | P(aprobar) | Clasificación: 1 horas → 0.08 → ❌ Reprueba; 2 horas → 0.27 → ❌ Reprueba; 3 horas → 0.62 → ✅ Aprueba; 4 horas → 0.88 → ✅ Aprueba; 5 horas → 0.97 → ✅ Aprueba.

El Decision Boundary ocurre cuando p = 0.5, es decir cuando $z = w^Tx + w_0 = 0$.

## Slide 5

Decision Boundary: ¿Qué significa $z = w^T\cdot x + w_0 = 0$?

Tres bloques de encabezado:
- z > 0 | σ(z) > 0.5 | p > 0.5 | Clase 0
- z = 0 | σ(z) = 0.5 | Máxima incertidumbre | Decision Boundary
- z < 0 | σ(z) < 0.5 | p < 0.5 | Clase 1

Decision Boundary: $z = w^T\cdot x + w_0 = 0$

**Figura:** Tres paneles. Izquierda: "1D: z=0 es un PUNTO", eje X "Horas de estudio (x)" (0 a 6), eje Y "p(C=0|x)" (0 a 1). Curva sigmoide azul con línea vertical naranja punteada en z=0 → x=2.67h, zona sombreada roja a la izquierda ("z<0 Reprueba") y azul a la derecha ("z>0 Aprueba"), punto marcado z=0/p=0.5. Centro: "z determina la clasificación", tabla con columnas Horas x | z=1.5x−4 | p=σ(z) | Clase: 1.00h → −2.50 → 0.08 → Reprueba; 2.00h → −1.00 → 0.27 → Reprueba; 2.67h → 0.00 → 0.50 → Boundary; 3.00h → 0.50 → 0.62 → Aprueba; 4.00h → 2.00 → 0.88 → Aprueba; 5.00h → 3.50 → 0.97 → Aprueba. Derecha: "2D: z=0 es una LINEA RECTA", eje X "x₁" (−3 a 3), eje Y "x₂" (−3 a 3). Puntos rojos (Clase 0, z<0) agrupados abajo-izquierda, puntos azules (Clase 1, z>0) agrupados arriba-derecha, línea diagonal naranja "z=0 (boundary)" separando ambas nubes, anotaciones "z>0, p>0.5, Clase 1" y "z<0, p<0.5, Clase 0".

z resume TODA la información de las features en un solo número. El sigmoid convierte ese número en probabilidad.

## Slide 6

Cómo los Pesos Controlan el Sigmoid

w1 controla la PENDIENTE (qué tan abrupta es la transición) | w0 controla la POSICIÓN (dónde está el decision boundary)

Efecto de w0 (posición) y w1 (pendiente) en el Sigmoid

**Figura:** Tres gráficos de la curva sigmoide σ(z), eje X "z" (−7.5 a 7.5), eje Y (0 a 1.0), cada uno con línea horizontal punteada gris en 0.5 y línea vertical naranja punteada marcando el Decision Boundary (DB). Panel 1: "w0=0, w1=1 (estándar)", curva azul estándar, DB=0.0. Panel 2: "w0=0, w1=0.3 (transición suave)", curva roja mucho más gradual, DB=0.0. Panel 3: "w0=-3, w1=1 (boundary desplazado)", curva verde estándar de pendiente pero desplazada, DB=3.0.

Parámetro | w1 grande => transición abrupta | w0 negativo => boundary se desplaza a la derecha

Gradient Descent aprende automáticamente los mejores valores de w0 y w1 desde los datos.

## Slide 7

Analogía: z como "Altitud" y el Sigmoid como "Conversor"

Analogía: z es como la ALTITUD de un terreno. z = 0 es el NIVEL DEL MAR = Decision Boundary. Sobre el mar → Clase 0. Bajo el mar → Clase 1.

z=0 es el punto exacto donde el modelo está indeciso (p=0.5)

**Figura:** Dos gráficos lado a lado. Izquierda: "Analogía: z como 'altitud'", eje X "Features x" (−5 a 5), eje Y "z = w^T·x + w0" (−4 a 4 aprox.). Línea diagonal azul ascendente representando z, línea horizontal naranja en z=0 marcada "nivel del mar", zona sombreada azul arriba ("z > 0, altitud positiva", "Clase 0, z>0, p>0.5") y zona sombreada roja abajo ("z < 0, altitud negativa", "Clase 1, z<0, p<0.5"), línea vertical punteada naranja marcando "Decision Boundary z=0". Derecha: "Sigmoid convierte z en probabilidad", eje X "z = w^T·x + w0" (−6 a 6), eje Y "p = σ(z)" (0 a 1.0). Curva sigmoide azul con línea punteada naranja horizontal en p=0.5 (boundary) y vertical en z=0, zona sombreada azul (z>0 → p>0.5 Clase 0) con flecha "z>0, Clase 0" y zona sombreada roja (z<0 → p<0.5 Clase 1) con flecha "z<0, Clase 1".

El Decision Boundary z=0 divide el espacio: PUNTO en 1D, LÍNEA en 2D, PLANO en 3D, HIPERPLANO en nD.

## Slide 8

Casos Lineales y No-Lineales

El Sigmoid SIEMPRE recibe $z = w^Tx + w_0$ (lineal en w). Las features x pueden ser transformadas.

Logistic Regression: Linear y No-Linear

**Figura:** Tres gráficos de dispersión, eje X y eje Y de −4 a 4 (tercer panel con ejes propios φ). Izquierda: "Caso Lineal ✅ Logistic Regression funciona" — puntos rojos (Clase 0) agrupados a la izquierda y azules (Clase 1) a la derecha, separados por una línea vertical azul "Decision Boundary (lineal)" en x=0. Centro: "Caso No Lineal ⚠️ Necesita feature engineering" — puntos rojos (Clase 0) agrupados en un círculo central rodeados por puntos azules (Clase 1) dispersos alrededor; un círculo naranja "Boundary curvo" delimita la región roja, una línea vertical azul punteada "Boundary lineal ❌" no logra separar las clases. Derecha: "Feature Engineering ✅ Boundary lineal en nuevo espacio", eje X "φ1 = x1" (−4 a 4 aprox.), eje Y "φ2 = x1² + x2²" (0 a 16). Tras la transformación, los puntos azules (Clase 1) quedan arriba y los rojos (Clase 0) abajo, separados por una línea horizontal verde "Boundary lineal en espacio φ".

Feature Engineering: agregar $\phi(x) = [x_1, x_2, x_1x_2, x_1^2, \ldots]$ permite boundaries no-lineales.

## Slide 9

Extensión a Múltiples Clases

Logistic Regression básica evalúa pertenencia a UNA sola clase. Para K clases se usa Softmax.

**Figura:** Dos gráficos de dispersión lado a lado, ejes X e Y aproximadamente de −4/−6 a 4/6. Izquierda: "Logistic Regression Binaria (Sigmoid) - 2 clases" — puntos rojos (Clase 0) a la izquierda y azules (Clase 1) a la derecha, separados por una línea vertical azul "Decision Boundary", zona sombreada rosa a la izquierda etiquetada "P(C=0|x), Sigmoid σ(z)". Derecha: "Multinomial Logistic Regression (Softmax) - K clases" — tres grupos de puntos: rojos "Grasshopper" (arriba-izquierda), azules "Katydid" (arriba-derecha), verdes "Cricket" (abajo-centro), con una línea vertical naranja punteada y una línea horizontal morada punteada cruzándose, y un recuadro con la fórmula "Softmax: P(Ck|x) = exp(zk)/Σexp(zj)".

Sigmoid es caso especial de Softmax con K=2. Softmax garantiza que todas las probabilidades sumen 1.

## Slide 10

Pipeline Completo: Resumen

Pipeline Completo: De Regresión Lineal → Logistic Regression

**Figura:** Diagrama de flujo horizontal con 5 cajas de colores conectadas por flechas: (1) azul oscuro "Datos (x, t)" con nota "Features: horas, notas antena..."; (2) celeste "Combinación Lineal z" con nota "$z = w\cdot x + w_0 \in (-\infty, +\infty)$"; (3) naranja "Sigmoid σ(z)" con nota "$\sigma(z) = 1/(1+e^{-z}) \in [0,1]$"; (4) verde "Probabilidad p(C|x)" con nota "P(aprobar) = 0.87, Interpretable"; (5) rojo "Clasificación ŷ" con nota "ŷ=1 si p≥0.5, ŷ=0 si p<0.5". Debajo, recuadro morado con ícono de advertencia: "⚠ Extensión No-Lineal: agregar features $\phi(x) = [x, x^2, x_1x_2, \ldots] \rightarrow z = w\cdot\phi(x) + w_0$".

Cuatro tarjetas de resumen al pie:
- Sigmoid: Comprime z a [0,1] interpretable como probabilidad
- Linealidad en w: $z = w^T\phi(x) + w_0$ siempre lineal en parámetros
- Feature Eng.: φ(x) permite boundaries no-lineales
- Softmax: Extensión natural para K > 2 clases
