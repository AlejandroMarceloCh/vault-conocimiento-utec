---
curso: ML
titulo: GD_Univariable_vs_Multivariable
slides: 8
fuente: GD_Univariable_vs_Multivariable.pdf
---

## Slide 1

CS3061 · Machine Learning · UTEC

# Gradient Descent

*Univariable → Multivariable*

Comparación función a función · Solo GD · Forma 1 (loop explícito)

**Figura:** Cuatro tarjetas horizontales con nombres de función, cada una en un color distinto: `predecir()` (azul), `calcular_mse()` (verde), `gradiente()` (naranja), `gradient_descent()` (rojo). Representan el índice de las 4 funciones que se compararán en el bloque.

## Slide 2

**0 — El Bias Trick — antes de comparar**

*La única decisión de diseño que lo cambia todo:*

**Figura:** Panel comparativo de dos columnas.

Columna izquierda (UNIVARIABLE):
- 2 parámetros separados
```
w = 0.0      # pendiente
b = 0.0      # intercepto
```
Predicción:
$\hat{y} = w \cdot x + b$

- → x es un escalar
- → w y b son independientes
- → 2 actualizaciones separadas

Columna derecha (MULTIVARIABLE — BIAS TRICK):
- 1 vector W unificado
```
W = [0.0, 0.0, ..., 0.0]
#    w0   w1       wd
```
Predicción:
$\hat{y} = \text{dot}(W, x\_ext)$

- → x_ext = [1, x1, x2, ..., xd]
- → W[0] = w0 actúa como b
- → 1 loop actualiza todo

Entre ambas columnas: "VS"

Pie de nota (recuadro inferior): Agregar x₀=1 al inicio de cada vector → W[0] absorbe b → 1 sola regla de actualización para todos los pesos

## Slide 3

**1 — predecir() — de escalar a producto punto**

**Figura:** Panel comparativo de dos columnas de código con parámetros y fórmula debajo.

Columna izquierda (UNIVARIABLE):
```python
def predecir(x, w, b):
    return w * x + b

# x = 5.3  (un número)
# w = 2.1  (escalar)
# b = -0.5 (escalar)
# resultado: 2.1 * 5.3 + (-0.5)
#          = 10.63
```
Parámetros de entrada: `x` escalar · `w` escalar · `b` escalar

$\hat{y} = w \cdot x + b$

*Operación: 1 multiplicación + 1 suma*

Columna derecha (MULTIVARIABLE):
```python
def predecir_mv(x_ext, W):
    return dot(W, x_ext)

# x_ext = [1,  5.3,  2.0,  8.1]
# W     = [w0, w1,   w2,   w3 ]
# dot → w0*1 + w1*5.3
#      + w2*2.0 + w3*8.1
```
Parámetros de entrada: `x_ext` vector [1,x1..xd] · `W` vector [w0,w1..wd]

$\hat{y} = \text{dot}(W, x\_ext)$

*Operación: d+1 multiplicaciones + d sumas*

Entre ambas columnas: "VS"

Pie de nota (recuadro inferior): `dot(W, x_ext)` cuando x_ext=[1, x] y W=[b, w] → da exactamente `w*x + b` ← misma fórmula

## Slide 4

**2 — calcular_mse() — la fórmula no cambia**

**Figura:** Panel comparativo de dos columnas de código con la fórmula MSE debajo de cada una.

Columna izquierda (UNIVARIABLE):
```python
def calcular_mse(datos, w, b):
    n = len(datos)
    total = 0.0

    for x, y in datos:
        y_pred = predecir(x, w, b)
        error  = y - y_pred
        total += error ** 2

    return total / n

# datos = [(x1,y1), (x2,y2), ...]
# cada x es un NÚMERO
```
$MSE = (1/N) \cdot \sum (y_i - \hat{y}_i)^2$

→ predecir() usa escalar x

Columna derecha (MULTIVARIABLE):
```python
def calcular_mse_mv(datos_ext, W):
    n = len(datos_ext)
    total = 0.0

    for x_ext, y in datos_ext:
        y_pred = predecir_mv(x_ext, W)
        error  = y - y_pred
        total += error ** 2

    return total / n

# datos_ext = [([1,x1,x2],y1), ...]
# cada x_ext es un VECTOR
```
$MSE = (1/N) \cdot \sum (y_i - \hat{y}_i)^2$

→ predecir_mv() usa vector x_ext

Entre ambas columnas: "VS"

Pie de nota (recuadro inferior): La fórmula MSE es IDÉNTICA — solo cambia predecir() por predecir_mv() y el tipo de x

## Slide 5

**3 — gradiente() — de 2 escalares a 1 vector**

**Figura:** Panel comparativo de dos columnas de código, cada una con un recuadro de resultado.

Columna izquierda (UNIVARIABLE — RETORNA (GW, GB)):
```python
def gradiente_mse(datos, w, b):
    n = len(datos)
    grad_w = 0.0  # dJ/dw
    grad_b = 0.0  # dJ/db

    for x, y in datos:
        error   = y - predecir(x, w, b)
        grad_w += -2 * x * error
        grad_b += -2 * error

    grad_w = grad_w / n
    grad_b = grad_b / n

    return grad_w, grad_b
    # retorna: 2 ESCALARES
```
Recuadro: Resultado: (grad_w, grad_b) → 2 valores independientes

Columna derecha (MULTIVARIABLE — RETORNA [G0,G1,...,GD]):
```python
def gradiente_mv(datos_ext, W):
    n = len(datos_ext)
    d = len(W)
    grad = [0.0] * d  # 1 grad por peso

    for x_ext, y in datos_ext:
        error = y - predecir_mv(x_ext, W)

        for j in range(d):
            grad[j] += -2 * x_ext[j] * error

    for j in range(d):
        grad[j] = grad[j] / n

    return grad
    # retorna: VECTOR de d+1 valores
```
Recuadro: Resultado: [g0, g1, g2, ..., gd] → 1 vector

Entre ambas columnas: "VS"

Pie de nota (recuadro inferior): j=0: x_ext[0]=1 siempre → grad[0] = (-2/N)·Σ error ← igual que grad_b | j=1: grad[1] = (-2/N)·Σ x·error ← igual que grad_w

## Slide 6

**4 — gradient_descent() — actualización de pesos · Forma 1**

**Figura:** Panel comparativo de dos columnas de código, con recuadros punteados resaltando el bloque de actualización.

Columna izquierda (UNIVARIABLE — 2 LÍNEAS SEPARADAS):
```python
def gradient_descent(datos, lr, iters):
    w, b = 0.0, 0.0  # 2 escalares

    for i in range(iters):

        # 1. Calcular gradiente
        gw, gb = gradiente_mse(datos, w, b)

        # 2. Actualizar w
        w = w - lr * gw

        # 3. Actualizar b
        b = b - lr * gb

    return w, b
```
Recuadro punteado (azul) resalta: `return w, b`

Nota: 2 líneas de actualización (w y b por separado)

Columna derecha (MULTIVARIABLE — LOOP EXPLÍCITO (FORMA 1)):
```python
def gradient_descent_mv(datos_ext, lr, iters):
    d = len(datos_ext[0][0])
    W = [0.0] * d  # vector de ceros

    for i in range(iters):

        # 1. Calcular gradiente vectorial
        grad = gradiente_mv(datos_ext, W)

        # 2. Actualizar CADA peso con loop
        W_nuevo = []
        for j in range(len(W)):
            W_nuevo.append(W[j] - lr * grad[j])
        W = W_nuevo

    return W
```
Recuadro punteado (rojo) resalta el bloque:
```
W_nuevo = []
for j in range(len(W)):
    W_nuevo.append(W[j] - lr * grad[j])
W = W_nuevo

return W
```

Nota: Loop sobre d+1 pesos (misma lógica, todos los wⱼ)

Entre ambas columnas: "VS"

Pie de nota (recuadro inferior): El loop `for j in range(len(W)):` hace exactamente: w=w-lr*gw y b=b-lr*gb pero para TODOS los pesos a la vez

## Slide 7

**4b — Zoom: la actualización de pesos explicada**

*¿Por qué el loop hace lo mismo que las 2 líneas del univariable?*

**Figura:** Panel comparativo de dos columnas con un diagrama de equivalencia entre ambas.

Columna izquierda (UNIVARIABLE (W TIENE SOLO W Y B)):
```python
# Solo 2 pesos: w y b
w = w - lr * gw   # j=1
b = b - lr * gb   # j=0

# Son 2 líneas SEPARADAS
```

Debajo, con flecha "equivale a":

Recuadro (SI APLICARAS EL LOOP AL UNIVARIABLE:):
```python
W = [b, w]     # j=0 es b, j=1 es w
W_nuevo = []
for j in range(2):       # solo 2 iter
    W_nuevo.append(W[j] - lr * grad[j])
W = W_nuevo    # idéntico resultado
```

Columna derecha (MULTIVARIABLE — EL LOOP GENERALIZADO):
```python
# d+1 pesos: W = [w0, w1, w2, w3, w4]
#             j=  0   1    2    3    4

W_nuevo = []
for j in range(len(W)):
    # misma fórmula: wj_nuevo = wj - lr*gj
    W_nuevo.append(W[j] - lr * grad[j])
W = W_nuevo

# Iteración por iteración:
# j=0: W[0] = W[0] - lr * grad[0]   ← w0
# j=1: W[1] = W[1] - lr * grad[1]   ← w1
# j=2: W[2] = W[2] - lr * grad[2]   ← w2
# j=3: W[3] = W[3] - lr * grad[3]   ← w3
# j=4: W[4] = W[4] - lr * grad[4]   ← w4
```

Pie de nota (recuadro inferior): La fórmula $w_j = w_j - lr \cdot grad[j]$ es IDÉNTICA a $w = w - lr \cdot g_w$ — solo cambia el índice j

## Slide 8

**✓ — Resumen: las 4 funciones comparadas**

**Figura:** Tabla comparativa de 4 columnas (Función / Univariable / Multivariable / Qué cambió) y 4 filas, una por función.

| Función | Univariable | Multivariable | Qué cambió |
|---|---|---|---|
| `predecir()` | `w * x + b` | `dot(W, x_ext)` | × escalar → · vectorial |
| `calcular_mse()` | `predecir(x, w, b)` | `predecir_mv(x_ext, W)` | solo cambia la llamada interna |
| `gradiente()` | retorna (gw, gb) — 2 escalares | retorna [g0,g1,...,gd] — 1 vector | 2 vars → loop sobre d+1 |
| `gradient_descent()` | `w -= lr*gw` / `b -= lr*gb` — 2 líneas | `for j in range(d): W_nuevo.append(W[j]-lr*grad[j])` | 2 líneas → loop explícito |

Pie de nota (recuadro inferior): La matemática es IDÉNTICA — solo cambia de manejar 2 variables a manejar un vector de d+1 elementos
