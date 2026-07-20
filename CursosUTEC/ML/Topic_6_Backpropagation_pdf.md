---
curso: ML
titulo: Topic 6 - Backpropagation
slides: 62
fuente: Topic 6 - Backpropagation.pdf
---

## Slide 1

# Backpropagation

## Slide 2

# Objetivos

1. Comprender el funcionamiento de Backpropagation en un MLP.
2. Evaluar las limitaciones de este modelo y cómo mitigarlos.
3. Aprender a calcular las gradientes para la optimización de una MLP.
4. Entender cómo se aplica la regla de la cadena en el cálculo de derivadas inversas capa a capa.

## Slide 3

0.

Multi-layer Perceptron
*Gradientes*

## Slide 4

# Descenso de la gradiente

**Step 1.** Compute the derivatives of the loss with respect to the parameters:

$\frac{\partial L}{\partial \phi} = \begin{bmatrix} \frac{\partial L}{\partial \phi_0} \\ \frac{\partial L}{\partial \phi_1} \\ \vdots \\ \frac{\partial L}{\partial \phi_N} \end{bmatrix}.$

**Step 2.** Update the parameters according to the rule:

$\phi \longleftarrow \phi - \alpha\frac{\partial L}{\partial \phi},$

where the positive scalar $\alpha$ determines the magnitude of the change.

## Slide 5

# Descenso de la gradiente

Step 1: Compute derivatives (slopes of function) with respect to the parameters

$L[\phi] = \sum_{i=1}^{I}\ell_i = \sum_{i=1}^{I}(\text{f}[x_i,\phi]-y_i)^2$

$= \sum_{i=1}^{I}(\phi_0+\phi_1 x_i-y_i)^2$

$\frac{\partial L}{\partial \phi} = \frac{\partial}{\partial \phi}\sum_{i=1}^{I}\ell_i = \sum_{i=1}^{I}\frac{\partial \ell_i}{\partial \phi}$

$\frac{\partial \ell_i}{\partial \phi} = \begin{bmatrix} \frac{\partial \ell_i}{\partial \phi_0} \\ \frac{\partial \ell_i}{\partial \phi_1} \end{bmatrix} = \begin{bmatrix} 2(\phi_0+\phi_1 x_i-y_i) \\ 2x_i(\phi_0+\phi_1 x_i-y_i) \end{bmatrix}$

**Figura:** Gráfico de contorno "Loss, $L[\phi]$" con eje X "Intercept, $\phi_0$" (rango 0.0 a 2.0) y eje Y "Slope, $\phi_1$" (rango -1.0 a 1.0). El fondo muestra un mapa de calor marrón/rojo con líneas de contorno diagonales; un punto celeste etiquetado "0" está ubicado en la zona superior derecha (valores altos de pérdida).

## Slide 6

# Descenso de la gradiente

Step 1: Compute derivatives (slopes of function) with Respect to the parameters

$\frac{\partial L}{\partial \phi} = \frac{\partial}{\partial \phi}\sum_{i=1}^{I}\ell_i = \sum_{i=1}^{I}\frac{\partial \ell_i}{\partial \phi}$

$\frac{\partial \ell_i}{\partial \phi} = \begin{bmatrix} \frac{\partial \ell_i}{\partial \phi_0} \\ \frac{\partial \ell_i}{\partial \phi_1} \end{bmatrix} = \begin{bmatrix} 2(\phi_0+\phi_1 x_i-y_i) \\ 2x_i(\phi_0+\phi_1 x_i-y_i) \end{bmatrix}$

Step 2: Update parameters according to rule

$\phi \longleftarrow \phi - \alpha\frac{\partial L}{\partial \phi}$

$\alpha$ = step size or learning rate if fixed

**Figura:** Mismo gráfico de contorno "Loss, $L[\phi]$" (ejes Intercept $\phi_0$ 0.0–2.0, Slope $\phi_1$ -1.0 a 1.0) mostrando ahora la trayectoria del descenso de gradiente: puntos numerados 0, 1, 2, 3, 4 conectados por una línea, comenzando en la esquina superior derecha (punto 0, pérdida alta) y descendiendo hacia la zona central-inferior izquierda (punto 4, pérdida menor), acercándose al mínimo de la función de pérdida.

## Slide 7

# Modelo de Gabor

$\text{f}[x,\phi] = \sin[\phi_0+0.06\cdot\phi_1 x]\cdot\exp\left(-\frac{(\phi_0+0.06\cdot\phi_1 x)^2}{8.0}\right)$

**Figura:** Tres gráficos "Output, $y$" vs "Input, $x$" (rango -15 a 15, salida -1 a 1) mostrando la función de Gabor (onda senoidal modulada por una envolvente gaussiana) para distintos parámetros:
a) $\phi_0=-5.0$, $\phi_1=25.0$: oscilación centrada cerca de x=0, picos en aproximadamente ±1.
b) $\phi_0=20.0$, $\phi_1=40.0$: oscilación de mayor frecuencia desplazada hacia la izquierda (cerca de x=-5).
c) $\phi_0=3.0$, $\phi_1=15.0$: oscilación más ancha y de menor frecuencia, desplazada levemente a la izquierda.

## Slide 8

**Figura:** Panel compuesto de gráficos sobre ajuste del modelo de Gabor mediante descenso de gradiente.
a) Mapa de contorno "Loss, $L[\phi]$" con eje X $\phi_0$ (-10.0 a 10.0) y eje Y $\phi_1$ (2.5 a 22.5), mostrando varios puntos celestes/turquesa dispersos sobre el paisaje de pérdida (con zonas de valle oscuras y crestas claras) y líneas punteadas que conectan puntos del contorno con los gráficos b, c, d, e, f de abajo/derecha. Un "+" marca un punto de referencia en el centro del gráfico.
b) Gráfico "Output, $y$" vs "Input, $x$" con puntos de datos naranjas dispersos y una curva turquesa clara ajustando parcialmente los datos; "Loss = 3.67".
c) Gráfico similar con una curva azul oscuro que ajusta mejor los datos (mayor coincidencia con los puntos naranjas); "Loss = 0.64".
d) Gráfico con curva turquesa que no ajusta bien los datos (oscilación de baja frecuencia); "Loss = 5.51".
e) Gráfico con curva turquesa (una sola oscilación amplia) que ajusta pobremente los datos; "Loss = 10.18".
f) Gráfico con curva turquesa de forma similar a b) pero desplazada, ajuste pobre; "Loss = 9.96".
A la derecha, un segundo gráfico "a)" repite el mapa de contorno "Loss, $L[\phi]$" (mismos ejes) etiquetado "Gradient descent", mostrando la trayectoria del descenso de gradiente: comienza en el punto 1 (arriba, en una zona de pérdida alta), desciende verticalmente, y termina en los puntos 3 y 2 (zona central-inferior, valle de menor pérdida), ilustrando cómo el algoritmo converge desde una inicialización lejana hacia un mínimo local.

## Slide 9

1.

Multi-layer Perceptron
*Backpropagation*

## Slide 10

# Backpropagation

**Backpropagation:** un método eficiente para calcular los gradientes necesarios para la optimización basada en gradiente de los pesos en un perceptrón multicapa (MLP).

Dada cualquier función de error $E$, y funciones de activación $g()$ y $f()$, solo es necesario derivar los gradientes.

**Figura:** Recuadro amarillo con texto "Training neural nets: Loop until convergence: for each example $n$ — 1. Given input $\mathbf{x}^{(n)}$, propagate activity forward ($\mathbf{x}^{(n)} \to \mathbf{h}^{(n)} \to o^{(n)}$) (**forward pass**). 2. Propagate gradients backward (**backward pass**). 3. Update each weight (via gradient descent)."

## Slide 11

# The forward pass

**Figura:** Diagrama de una red neuronal multicapa (MLP) con capas etiquetadas: "Training input, $\mathbf{x}$" (3 nodos), "Hidden layer, $\mathbf{h}_1$" (4 nodos, conectados desde la entrada mediante pesos $\Omega_0$), "Hidden layer, $\mathbf{h}_2$" (2 nodos, pesos $\Omega_1$), "Hidden layer, $\mathbf{h}_3$" (3 nodos, pesos $\Omega_2$), "Output, $\text{f}[\mathbf{x},\phi]$" (2 nodos, pesos $\Omega_3$), seguido de "Training output, $y$" (1 nodo) y "Loss, $\ell$" (1 nodo). Todas las conexiones entre capas se muestran como flechas grises, excepto una conexión resaltada en naranja que va desde el segundo nodo de $\mathbf{h}_1$ hacia el segundo nodo de $\mathbf{h}_2$, ilustrando un peso específico dentro de la red.

## Slide 12

# Calcular Gradientes

Loss: sum of individual terms: $L[\phi] = \sum_{i=1}^{I}\ell_i = \sum_{i=1}^{I} \text{l}[\text{f}[\mathbf{x}_i,\phi], y_i]$

SGD Algorithm: $\phi_{t+1} \longleftarrow \phi_t - \alpha\sum_{i\in\mathcal{B}_t}\frac{\partial \ell_i[\phi_t]}{\partial \phi}$

Parameters: $\phi = \{\beta_0,\Omega_0,\beta_1,\Omega_1,\beta_2,\Omega_2,\beta_3,\Omega_3\}$

Need to compute gradients $\dfrac{\partial \ell_i}{\partial \beta_k}$ and $\dfrac{\partial \ell_i}{\partial \Omega_k}$

## Slide 13

# Calcular Gradientes

**Figura:** Mismo diagrama de red neuronal multicapa que en la Slide 11 (capas "Training input, $\mathbf{x}$" → $\Omega_0$ → "Hidden layer, $\mathbf{h}_1$" → $\Omega_1$ → "Hidden layer, $\mathbf{h}_2$" → $\Omega_2$ → "Hidden layer, $\mathbf{h}_3$" → $\Omega_3$ → "Output, $\text{f}[\mathbf{x},\phi]$" → "Training output, $y$" → "Loss, $\ell$"), ahora en tono gris claro (desactivado), con una única conexión resaltada en azul oscuro que va del segundo nodo de $\mathbf{h}_1$ al segundo nodo de $\mathbf{h}_2$, indicando el peso específico cuyo gradiente se está analizando.

## Slide 14

# Calcular Gradientes

**Figura:** Dos diagramas de la misma red neuronal (paneles a y b), ambos en tono gris claro de fondo.
a) Una conexión resaltada en azul oscuro entre el segundo nodo de $\mathbf{h}_1$ y el segundo nodo de $\mathbf{h}_2$; a partir de ahí, todas las conexiones "aguas abajo" (desde $\mathbf{h}_2$ hacia $\mathbf{h}_3$, hacia la salida, hacia $y$ y hacia $\ell$) se muestran resaltadas en naranja, ilustrando qué parte del cómputo (el flujo hacia adelante desde ese peso) afecta a la pérdida.
b) Una conexión resaltada en azul oscuro entre un nodo de entrada y el segundo nodo de $\mathbf{h}_1$; de manera similar, todas las conexiones posteriores (desde $\mathbf{h}_1$ en adelante hasta $\ell$) se muestran en naranja, mostrando que un peso más temprano en la red afecta una porción mayor del grafo de cómputo posterior.

## Slide 15

# Toy Model

**Figura:** Diagrama de flujo lineal (grafo de cómputo) con nodos circulares conectados por flechas en secuencia: $x_i \to f_0 \to h_1 \to f_1 \to h_2 \to f_2 \to h_3 \to f_3 \to \ell_i$.

$\text{f}[x,\phi] = \beta_3+\omega_3\cdot\cos\Big[\beta_2+\omega_2\cdot\exp\big[\beta_1+\omega_1\cdot\sin[\beta_0+\omega_0\cdot x]\big]\Big]$

$\ell_i = (\text{f}[x_i,\phi]-y_i)^2$

- Consiste en una serie de funciones que se componen entre sí.
- A diferencia de las redes neuronales, solo utiliza escalares (no vectores).
- "Funciones de activación": seno, exponencial, coseno.

## Slide 16

# Toy Model

**Figura:** Mismo diagrama de flujo lineal: $x_i \to f_0 \to h_1 \to f_1 \to h_2 \to f_2 \to h_3 \to f_3 \to \ell_i$.

$\text{f}[x,\phi] = \beta_3+\omega_3\cdot\cos\Big[\beta_2+\omega_2\cdot\exp\big[\beta_1+\omega_1\cdot\sin[\beta_0+\omega_0\cdot x]\big]\Big]$

$\ell_i = (\text{f}[x_i,\phi]-y_i)^2$

**Derivadas**

$\dfrac{\partial \cos[z]}{\partial z} = -\sin[z]$ $\qquad \dfrac{\partial \exp[z]}{\partial z} = \exp[z]$ $\qquad \dfrac{\partial \sin[z]}{\partial z} = -\cos[z]$

## Slide 17

# Forward Pass

$\text{f}[x,\phi] = \beta_3+\omega_3\cdot\cos\Big[\beta_2+\omega_2\cdot\exp\big[\beta_1+\omega_1\cdot\sin[\beta_0+\omega_0\cdot x]\big]\Big]$

$\ell_i = (\text{f}[x_i,\phi]-y_i)^2$

1. Escribe esto como una serie de cálculos intermedios.
2. Calcula estas cantidades intermedias.

$f_0 = \beta_0+\omega_0\cdot x_i$ $\qquad f_2 = \beta_2+\omega_2\cdot h_2$

$h_1 = \sin[f_0]$ $\qquad h_3 = \cos[f_2]$

$f_1 = \beta_1+\omega_1\cdot h_1$ $\qquad f_3 = \beta_3+\omega_3\cdot h_3$

$h_2 = \exp[f_1]$ $\qquad \ell_i = (f_3-y_i)^2.$

**Figura:** Diagrama de flujo lineal: $x_i \to f_0 \to h_1 \to f_1 \to h_2 \to f_2 \to h_3 \to f_3 \to \ell_i$.

## Slide 18

# Backward pass

**Figura:** Diagrama de flujo lineal: $x_i \to f_0 \to h_1 \to f_1 \to h_2 \to f_2 \to h_3 \to f_3 \to \ell_i$.

$\text{f}[x,\phi] = \beta_3+\omega_3\cdot\cos\Big[\beta_2+\omega_2\cdot\exp\big[\beta_1+\omega_1\cdot\sin[\beta_0+\omega_0\cdot x]\big]\Big]$

$\ell_i = (\text{f}[x_i,\phi]-y_i)^2$

1. Calcula las derivadas de la pérdida con respecto a estas cantidades intermedias, pero en orden inverso.

$\dfrac{\partial \ell_i}{\partial f_3}, \quad \dfrac{\partial \ell_i}{\partial h_3}, \quad \dfrac{\partial \ell_i}{\partial f_2}, \quad \dfrac{\partial \ell_i}{\partial h_2}, \quad \dfrac{\partial \ell_i}{\partial f_1}, \quad \dfrac{\partial \ell_i}{\partial h_1}, \quad \text{and} \quad \dfrac{\partial \ell_i}{\partial f_0}$

## Slide 19

# Backward pass

$\text{f}[x,\phi] = \beta_3+\omega_3\cdot\cos\Big[\beta_2+\omega_2\cdot\exp\big[\beta_1+\omega_1\cdot\sin[\beta_0+\omega_0\cdot x]\big]\Big]$

$\ell_i = (\text{f}[x_i,\phi]-y_i)^2$

1. Calcula las derivadas de la función de pérdida con respecto a estas cantidades intermedias, pero en orden inverso.

$\dfrac{\partial \ell_i}{\partial f_3}, \quad \dfrac{\partial \ell_i}{\partial h_3}, \quad \dfrac{\partial \ell_i}{\partial f_2}, \quad \dfrac{\partial \ell_i}{\partial h_2}, \quad \dfrac{\partial \ell_i}{\partial f_1}, \quad \dfrac{\partial \ell_i}{\partial h_1}, \quad \text{and} \quad \dfrac{\partial \ell_i}{\partial f_0}$

**Figura:** Diagrama de flujo con nodos y flechas apuntando de derecha a izquierda (orden inverso al forward pass): $\ell_i \to \frac{\partial \ell_i}{\partial f_3} \to \frac{\partial \ell_i}{\partial h_3} \to \frac{\partial \ell_i}{\partial f_2} \to \frac{\partial \ell_i}{\partial h_2} \to \frac{\partial \ell_i}{\partial f_1} \to \frac{\partial \ell_i}{\partial h_1} \to \frac{\partial \ell_i}{\partial f_0}$, terminando en $x_i$ (sin flecha entrante activa, mostrado como nodo final aislado a la izquierda).

## Slide 20

# Backward pass

1. Calcula las derivadas de la función de pérdida con respecto a estas cantidades intermedias, pero en orden inverso.

$f_0 = \beta_0+\omega_0\cdot x_i$ $\qquad f_2 = \beta_2+\omega_2\cdot h_2$

$h_1 = \sin[f_0]$ $\qquad h_3 = \cos[f_2]$

$f_1 = \beta_1+\omega_1\cdot h_1$ $\qquad f_3 = \beta_3+\omega_3\cdot h_3$

$h_2 = \exp[f_1]$ $\qquad \ell_i = (f_3-y_i)^2.$

- La primera de estas derivadas es trivial.

$\dfrac{\partial \ell_i}{\partial f_3} = 2(f_3-y_i)$

## Slide 21

# Backward pass

1. Calcula las derivadas de la función de pérdida con respecto a estas cantidades intermedias, pero en orden inverso.

$f_0 = \beta_0 + \omega_0 \cdot x_i$
$h_1 = \sin[f_0]$
$f_1 = \beta_1 + \omega_1 \cdot h_1$
$h_2 = \exp[f_1]$

$f_2 = \beta_2 + \omega_2 \cdot h_2$
$h_3 = \cos[f_2]$
$f_3 = \beta_3 + \omega_3 \cdot h_3$
$\ell_i = (f_3 - y_i)^2.$

- La segunda de estas derivadas se calcula mediante la regla de la cadena.

$\dfrac{\partial \ell_i}{\partial h_3} = \dfrac{\partial f_3}{\partial h_3} \dfrac{\partial \ell_i}{\partial f_3}$

**Figura:** Diagrama con tres flechas señalando cada factor de la fórmula, con textos explicativos: "How does a small change in $h_3$ change $l_i$?" (apunta a $\partial \ell_i/\partial h_3$), "How does a small change in $h_3$ change $f_3$?" (apunta a $\partial f_3/\partial h_3$), "How does a small change in $f_3$ change $l_i$?" (apunta a $\partial \ell_i/\partial f_3$).

## Slide 22

# Backward pass

1. Calcula las derivadas de la función de pérdida con respecto a estas cantidades intermedias, pero en orden inverso.

$f_0 = \beta_0 + \omega_0 \cdot x_i$
$h_1 = \sin[f_0]$
$f_1 = \beta_1 + \omega_1 \cdot h_1$
$h_2 = \exp[f_1]$

$f_2 = \beta_2 + \omega_2 \cdot h_2$
$h_3 = \cos[f_2]$
$f_3 = \beta_3 + \omega_3 \cdot h_3$
$\ell_i = (f_3 - y_i)^2.$

- La segunda de estas derivadas se calcula mediante la regla de la cadena.

$\dfrac{\partial \ell_i}{\partial h_3} = \dfrac{\partial f_3}{\partial h_3} \dfrac{\partial \ell_i}{\partial f_3}$

**Figura:** Misma fórmula que en el slide anterior, pero ahora con dos anotaciones: "How does a small change in $h_3$ change $l_i$?" (apunta a $\partial \ell_i/\partial h_3$) y "Already computed!" (apunta a $\partial \ell_i/\partial f_3$); el término $\partial f_3/\partial h_3$ se etiqueta directamente como $\omega_3$.

## Slide 23

# Backward pass

1. Calcula las derivadas de la función de pérdida con respecto a estas cantidades intermedias, pero en orden inverso.

$f_0 = \beta_0 + \omega_0 \cdot x_i$
$h_1 = \sin[f_0]$
$f_1 = \beta_1 + \omega_1 \cdot h_1$
$h_2 = \exp[f_1]$

$f_2 = \beta_2 + \omega_2 \cdot h_2$
$h_3 = \cos[f_2]$
$f_3 = \beta_3 + \omega_3 \cdot h_3$
$\ell_i = (f_3 - y_i)^2.$

- Las derivadas restantes también se calculan mediante un uso adicional de la regla de la cadena.

$\dfrac{\partial \ell_i}{\partial f_2} = \dfrac{\partial h_3}{\partial f_2}\left(\dfrac{\partial f_3}{\partial h_3}\dfrac{\partial \ell_i}{\partial f_3}\right)$

$\dfrac{\partial \ell_i}{\partial h_2} = \dfrac{\partial f_2}{\partial h_2}\left(\dfrac{\partial h_3}{\partial f_2}\dfrac{\partial f_3}{\partial h_3}\dfrac{\partial \ell_i}{\partial f_3}\right)$

$\dfrac{\partial \ell_i}{\partial f_1} = \dfrac{\partial h_2}{\partial f_1}\left(\dfrac{\partial f_2}{\partial h_2}\dfrac{\partial h_3}{\partial f_2}\dfrac{\partial f_3}{\partial h_3}\dfrac{\partial \ell_i}{\partial f_3}\right)$

$\dfrac{\partial \ell_i}{\partial h_1} = \dfrac{\partial f_1}{\partial h_1}\left(\dfrac{\partial h_2}{\partial f_1}\dfrac{\partial f_2}{\partial h_2}\dfrac{\partial h_3}{\partial f_2}\dfrac{\partial f_3}{\partial h_3}\dfrac{\partial \ell_i}{\partial f_3}\right)$

$\dfrac{\partial \ell_i}{\partial f_0} = \dfrac{\partial h_1}{\partial f_0}\left(\dfrac{\partial f_1}{\partial h_1}\dfrac{\partial h_2}{\partial f_1}\dfrac{\partial f_2}{\partial h_2}\dfrac{\partial h_3}{\partial f_2}\dfrac{\partial f_3}{\partial h_3}\dfrac{\partial \ell_i}{\partial f_3}\right)$

## Slide 24

# Backward pass

1. Calcula las derivadas de la función de pérdida con respecto a estas cantidades intermedias, pero en orden inverso.

$f_0 = \beta_0 + \omega_0 \cdot x_i$
$h_1 = \sin[f_0]$
$f_1 = \beta_1 + \omega_1 \cdot h_1$
$h_2 = \exp[f_1]$

$f_2 = \beta_2 + \omega_2 \cdot h_2$
$h_3 = \cos[f_2]$
$f_3 = \beta_3 + \omega_3 \cdot h_3$
$\ell_i = (f_3 - y_i)^2.$

- Las derivadas restantes también se calculan mediante un uso adicional de la regla de la cadena.

**Figura:** Cadena de nodos circulares conectados por flechas, en orden de derecha a izquierda: $\ell_i \rightarrow \partial \ell_i/\partial f_3 \rightarrow \partial \ell_i/\partial h_3 \rightarrow \partial \ell_i/\partial f_2 \rightarrow \partial \ell_i/\partial h_2 \rightarrow \partial \ell_i/\partial f_1 \rightarrow \partial \ell_i/\partial h_1 \rightarrow \partial \ell_i/\partial f_0$, con $x_i$ como nodo aislado al inicio (sin flecha de entrada). Cada flecha lleva encima la etiqueta de la derivada parcial correspondiente ($\partial f_3/\partial h_3$, $\partial h_3/\partial f_2$, $\partial f_2/\partial h_2$, $\partial h_2/\partial f_1$, $\partial f_1/\partial h_1$, $\partial h_1/\partial f_0$).

## Slide 25

# Backward pass

2. Determina cómo cambia la pérdida en función de los parámetros β y ω.

$f_0 = \beta_0 + \omega_0 \cdot x_i$
$h_1 = \sin[f_0]$
$f_1 = \beta_1 + \omega_1 \cdot h_1$
$h_2 = \exp[f_1]$

$f_2 = \beta_2 + \omega_2 \cdot h_2$
$h_3 = \cos[f_2]$
$f_3 = \beta_3 + \omega_3 \cdot h_3$
$\ell_i = (f_3 - y_i)^2.$

- Otra aplicación de la regla de la cadena.

$\dfrac{\partial \ell_i}{\partial \omega_k} = \dfrac{\partial f_k}{\partial \omega_k}\dfrac{\partial \ell_i}{\partial f_k}$

**Figura:** Tres flechas señalando cada término de la fórmula con las anotaciones: "How does a small change in $\omega_k$ change $l_i$?" (apunta a $\partial \ell_i/\partial \omega_k$), "How does a small change in $\omega_k$ change $f_k$?" (apunta a $\partial f_k/\partial \omega_k$), "How does a small change in $f_k$ change $l_i$?" (apunta a $\partial \ell_i/\partial f_k$).

## Slide 26

# Backward pass

2. Determina cómo cambia la pérdida en función de los parámetros β y ω.

$f_0 = \beta_0 + \omega_0 \cdot x_i$
$h_1 = \sin[f_0]$
$f_1 = \beta_1 + \omega_1 \cdot h_1$
$h_2 = \exp[f_1]$

$f_2 = \beta_2 + \omega_2 \cdot h_2$
$h_3 = \cos[f_2]$
$f_3 = \beta_3 + \omega_3 \cdot h_3$
$\ell_i = (f_3 - y_i)^2.$

- Otra aplicación de la regla de la cadena.

$\dfrac{\partial \ell_i}{\partial \omega_k} = \dfrac{\partial f_k}{\partial \omega_k}\dfrac{\partial \ell_i}{\partial f_k}$

**Figura:** Misma fórmula, ahora con anotaciones: "How does a small change in $\omega_k$ change $l_i$?" (apunta a $\partial \ell_i/\partial \omega_k$) y "Already calculated in part 1." (apunta a $\partial \ell_i/\partial f_k$); el término $\partial f_k/\partial \omega_k$ se etiqueta directamente como $h_k$.

## Slide 27

# Backward pass

2. Determina cómo cambia la pérdida en función de los parámetros β y ω.

$f_0 = \beta_0 + \omega_0 \cdot x_i$
$h_1 = \sin[f_0]$
$f_1 = \beta_1 + \omega_1 \cdot h_1$
$h_2 = \exp[f_1]$

$f_2 = \beta_2 + \omega_2 \cdot h_2$
$h_3 = \cos[f_2]$
$f_3 = \beta_3 + \omega_3 \cdot h_3$
$\ell_i = (f_3 - y_i)^2.$

- Otra aplicación de la regla de la cadena.
- De manera similar para los parámetros β.

$\dfrac{\partial \ell_i}{\partial \omega_k} = \dfrac{\partial f_k}{\partial \omega_k}\dfrac{\partial \ell_i}{\partial f_k}$

$\dfrac{\partial \ell_i}{\partial \beta_k} = \dfrac{\partial f_k}{\partial \beta_k}\dfrac{\partial \ell_i}{\partial f_k}$

## Slide 28

# Backward pass

2. Determina cómo cambia la pérdida en función de los parámetros β y ω.

$f_0 = \beta_0 + \omega_0 \cdot x_i$
$h_1 = \sin[f_0]$
$f_1 = \beta_1 + \omega_1 \cdot h_1$
$h_2 = \exp[f_1]$

$f_2 = \beta_2 + \omega_2 \cdot h_2$
$h_3 = \cos[f_2]$
$f_3 = \beta_3 + \omega_3 \cdot h_3$
$\ell_i = (f_3 - y_i)^2.$

**Figura:** Diagrama con nodo $x_i$ y una cadena horizontal de nodos circulares conectados de derecha a izquierda: $\ell_i \rightarrow \partial \ell_i/\partial f_3 \rightarrow \partial \ell_i/\partial h_3 \rightarrow \partial \ell_i/\partial f_2 \rightarrow \partial \ell_i/\partial h_2 \rightarrow \partial \ell_i/\partial f_1 \rightarrow \partial \ell_i/\partial h_1 \rightarrow \partial \ell_i/\partial f_0$. De cada nodo $\partial \ell_i/\partial f_k$ salen dos flechas descendentes hacia un par de nodos hijos: una etiquetada $\partial f_k/\partial \beta_k$ que lleva al nodo $\partial \ell_i/\partial \beta_k$, y otra etiquetada $\partial f_k/\partial \omega_k$ que lleva al nodo $\partial \ell_i/\partial \omega_k$. Esto se repite para k = 0, 1, 2, 3 (mostrando los pares $\partial \ell_i/\partial \beta_0, \partial \ell_i/\partial \omega_0$; $\partial \ell_i/\partial \beta_1, \partial \ell_i/\partial \omega_1$; $\partial \ell_i/\partial \beta_2, \partial \ell_i/\partial \omega_2$; $\partial \ell_i/\partial \beta_3, \partial \ell_i/\partial \omega_3$).

## Slide 29

**Figura:** Slide de transición con fondo degradado azul y comillas decorativas grandes de fondo. Texto central: "¿Cómo se vería el backpropagation en una MLP?"

## Slide 30

# Forward pass

**Figura:** Diagrama de una red neuronal multicapa (MLP): capa de entrada con 3 nodos ("Training input, x"), seguida de cuatro capas ocultas de 4, 2, 3 y 2 nodos respectivamente (etiquetadas $\Omega_0$, $\Omega_1$, $\Omega_2$, $\Omega_3$ sobre las flechas de conexión: "Hidden layer, $h_1$", "Hidden layer, $h_2$", "Hidden layer, $h_3$"), luego una capa de salida ("Output, $f[x,\phi]$"), conectada a un nodo "Training output, y" y finalmente al nodo de pérdida $\ell$ ("Loss, $\ell$"). Todas las conexiones entre capas son flechas grises completamente conectadas (fully connected), excepto una flecha naranja resaltada entre dos nodos específicos de la primera capa oculta y la segunda capa oculta.

1. Escribe esto como una serie de cálculos intermedios.
2. Calcula estas cantidades intermedias.

$\mathbf{f}_0 = \boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}_i$
$\mathbf{h}_1 = \mathbf{a}[\mathbf{f}_0]$
$\mathbf{f}_1 = \boldsymbol{\beta}_1 + \boldsymbol{\Omega}_1 \mathbf{h}_1$
$\mathbf{h}_2 = \mathbf{a}[\mathbf{f}_1]$
$\mathbf{f}_2 = \boldsymbol{\beta}_2 + \boldsymbol{\Omega}_2 \mathbf{h}_2$
$\mathbf{h}_3 = \mathbf{a}[\mathbf{f}_2]$
$\mathbf{f}_3 = \boldsymbol{\beta}_3 + \boldsymbol{\Omega}_3 \mathbf{h}_3$
$\ell_i = \mathrm{l}[\mathbf{f}_3, y_i]$

## Slide 31

# Backward pass

**Figura:** Mismo diagrama de MLP del slide anterior (capas $\Omega_0$ a $\Omega_3$, entrada $x$, salidas $h_1$, $h_2$, $h_3$, output $f[x,\phi]$, training output $y$, loss $\ell$).

1. Escribe esto como una serie de cálculos intermedios.
2. Calcula estas cantidades intermedias.
3. Toma las derivadas de la salida con respecto a las cantidades intermedias.

$\mathbf{f}_0 = \boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}_i$
$\mathbf{h}_1 = \mathbf{a}[\mathbf{f}_0]$
$\mathbf{f}_1 = \boldsymbol{\beta}_1 + \boldsymbol{\Omega}_1 \mathbf{h}_1$
$\mathbf{h}_2 = \mathbf{a}[\mathbf{f}_1]$
$\mathbf{f}_2 = \boldsymbol{\beta}_2 + \boldsymbol{\Omega}_2 \mathbf{h}_2$
$\mathbf{h}_3 = \mathbf{a}[\mathbf{f}_2]$
$\mathbf{f}_3 = \boldsymbol{\beta}_3 + \boldsymbol{\Omega}_3 \mathbf{h}_3$
$\ell_i = \mathrm{l}[\mathbf{f}_3, y_i]$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_2} = \dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}$ (recuadro resaltando el factor $\partial \mathbf{f}_3/\partial \mathbf{h}_3$)

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_1} = \dfrac{\partial \mathbf{h}_2}{\partial \mathbf{f}_1}\dfrac{\partial \mathbf{f}_2}{\partial \mathbf{h}_2}\left(\dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}\right)$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_0} = \dfrac{\partial \mathbf{h}_1}{\partial \mathbf{f}_0}\dfrac{\partial \mathbf{f}_1}{\partial \mathbf{h}_1}\left(\dfrac{\partial \mathbf{h}_2}{\partial \mathbf{f}_1}\dfrac{\partial \mathbf{f}_2}{\partial \mathbf{h}_2}\dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}\right)$

## Slide 32

# Backward pass

**Figura:** Mismo diagrama de MLP.

1. Escribe esto como una serie de cálculos intermedios.
2. Calcula estas cantidades intermedias.
3. Toma las derivadas de la salida con respecto a las cantidades intermedias.

$\mathbf{f}_0 = \boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}_i$
$\mathbf{h}_1 = \mathbf{a}[\mathbf{f}_0]$
$\mathbf{f}_1 = \boldsymbol{\beta}_1 + \boldsymbol{\Omega}_1 \mathbf{h}_1$
$\mathbf{h}_2 = \mathbf{a}[\mathbf{f}_1]$
$\mathbf{f}_2 = \boldsymbol{\beta}_2 + \boldsymbol{\Omega}_2 \mathbf{h}_2$
$\mathbf{h}_3 = \mathbf{a}[\mathbf{f}_2]$
$\mathbf{f}_3 = \boldsymbol{\beta}_3 + \boldsymbol{\Omega}_3 \mathbf{h}_3$
$\ell_i = \mathrm{l}[\mathbf{f}_3, y_i]$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}$

Recuadro resaltado: $\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3} = \dfrac{\partial}{\partial \mathbf{h}_3}(\boldsymbol{\beta}_3 + \boldsymbol{\Omega}_3 \mathbf{h}_3) = \boldsymbol{\Omega}_3^T$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_2} = \dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}$ (recuadro resaltando de nuevo $\partial \mathbf{f}_3/\partial \mathbf{h}_3$)

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_1} = \dfrac{\partial \mathbf{h}_2}{\partial \mathbf{f}_1}\dfrac{\partial \mathbf{f}_2}{\partial \mathbf{h}_2}\left(\dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}\right)$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_0} = \dfrac{\partial \mathbf{h}_1}{\partial \mathbf{f}_0}\dfrac{\partial \mathbf{f}_1}{\partial \mathbf{h}_1}\left(\dfrac{\partial \mathbf{h}_2}{\partial \mathbf{f}_1}\dfrac{\partial \mathbf{f}_2}{\partial \mathbf{h}_2}\dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}\right)$

## Slide 33

# Derivada de ReLU

**Figura:** Gráfico cartesiano con eje X "Input, $z$" de -2.0 a 2.0 y eje Y "Output" de -2.0 a 2.0. Se muestran dos curvas: ReLU[$z$] (línea naranja/roja) que vale 0 para z≤0 y crece linealmente (pendiente 1) para z>0; y su derivada $\partial \mathrm{ReLU}[z]/\partial z$ (línea turquesa/verde agua) que vale 0 para z<0 y salta a 1 (constante) para z>0, formando un escalón.

$\mathbb{I}[z > 0]$

"Función indicadora"

## Slide 34

# Derivada de ReLU

1. Considera:

$\mathbf{a} = \mathrm{ReLU}[\mathbf{b}]$

donde:

$\mathbf{a} = \begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} \qquad \mathbf{b} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$

2. Podemos escribir:

$\begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} = \begin{bmatrix} \mathrm{ReLU}[b_1] \\ \mathrm{ReLU}[b_2] \\ \mathrm{ReLU}[b_3] \end{bmatrix}$

3. Tomando la derivada

$\dfrac{\partial \mathbf{a}}{\partial \mathbf{b}} = \begin{bmatrix} \dfrac{\partial a_1}{\partial b_1} & \dfrac{\partial a_2}{\partial b_1} & \dfrac{\partial a_3}{\partial b_1} \\ \dfrac{\partial a_1}{\partial b_2} & \dfrac{\partial a_2}{\partial b_2} & \dfrac{\partial a_3}{\partial b_2} \\ \dfrac{\partial a_1}{\partial b_3} & \dfrac{\partial a_2}{\partial b_3} & \dfrac{\partial a_3}{\partial b_3} \end{bmatrix} = \begin{bmatrix} \mathbb{I}[b_1 > 0] & 0 & 0 \\ 0 & \mathbb{I}[b_2 > 0] & 0 \\ 0 & 0 & \mathbb{I}[b_3 > 0] \end{bmatrix}$

4. Podemos multiplicar punto a punto por una matriz diagonal de manera equivalente.

$\mathbb{I}[\mathbf{b} > 0] \odot$

## Slide 35

# Backward pass

**Figura:** Mismo diagrama de MLP (capas $\Omega_0$-$\Omega_3$, $x$, $h_1$, $h_2$, $h_3$, output, $y$, $\ell$).

1. Escribe esto como una serie de cálculos intermedios.
2. Calcula estas cantidades intermedias.
3. Toma las derivadas de la salida con respecto a las cantidades intermedias.

$\mathbf{f}_0 = \boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}_i$
$\mathbf{h}_1 = \mathbf{a}[\mathbf{f}_0]$
$\mathbf{f}_1 = \boldsymbol{\beta}_1 + \boldsymbol{\Omega}_1 \mathbf{h}_1$
$\mathbf{h}_2 = \mathbf{a}[\mathbf{f}_1]$
$\mathbf{f}_2 = \boldsymbol{\beta}_2 + \boldsymbol{\Omega}_2 \mathbf{h}_2$
$\mathbf{h}_3 = \mathbf{a}[\mathbf{f}_2]$
$\mathbf{f}_3 = \boldsymbol{\beta}_3 + \boldsymbol{\Omega}_3 \mathbf{h}_3$
$\ell_i = \mathrm{l}[\mathbf{f}_3, y_i]$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}$

$\mathbb{I}[\mathbf{f}_2 > 0]$ (recuadro resaltado, valor de referencia)

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_2} = \dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}$ (recuadro resaltando el factor $\partial \mathbf{h}_3/\partial \mathbf{f}_2$)

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_1} = \dfrac{\partial \mathbf{h}_2}{\partial \mathbf{f}_1}\dfrac{\partial \mathbf{f}_2}{\partial \mathbf{h}_2}\left(\dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}\right)$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_0} = \dfrac{\partial \mathbf{h}_1}{\partial \mathbf{f}_0}\dfrac{\partial \mathbf{f}_1}{\partial \mathbf{h}_1}\left(\dfrac{\partial \mathbf{h}_2}{\partial \mathbf{f}_1}\dfrac{\partial \mathbf{f}_2}{\partial \mathbf{h}_2}\dfrac{\partial \mathbf{h}_3}{\partial \mathbf{f}_2}\dfrac{\partial \mathbf{f}_3}{\partial \mathbf{h}_3}\dfrac{\partial \ell_i}{\partial \mathbf{f}_3}\right)$

## Slide 36

# Backward pass

**Figura:** Mismo diagrama de MLP.

1. Escribe esto como una serie de cálculos intermedios.
2. Calcula estas cantidades intermedias.
3. Toma las derivadas de la salida con respecto a las cantidades intermedias.
4. Toma las derivadas con respecto a los parámetros.

$\mathbf{f}_0 = \boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}_i$
$\mathbf{h}_1 = \mathbf{a}[\mathbf{f}_0]$
$\mathbf{f}_1 = \boldsymbol{\beta}_1 + \boldsymbol{\Omega}_1 \mathbf{h}_1$
$\mathbf{h}_2 = \mathbf{a}[\mathbf{f}_1]$
$\mathbf{f}_2 = \boldsymbol{\beta}_2 + \boldsymbol{\Omega}_2 \mathbf{h}_2$
$\mathbf{h}_3 = \mathbf{a}[\mathbf{f}_2]$
$\mathbf{f}_3 = \boldsymbol{\beta}_3 + \boldsymbol{\Omega}_3 \mathbf{h}_3$
$\ell_i = \mathrm{l}[\mathbf{f}_3, y_i]$

$\dfrac{\partial \ell_i}{\partial \boldsymbol{\beta}_k} = \dfrac{\partial \mathbf{f}_k}{\partial \boldsymbol{\beta}_k}\dfrac{\partial \ell_i}{\partial \mathbf{f}_k}$

$= \dfrac{\partial}{\partial \boldsymbol{\beta}_k}(\boldsymbol{\beta}_k + \boldsymbol{\Omega}_k \mathbf{h}_k)\dfrac{\partial \ell_i}{\partial \mathbf{f}_k}$

$= \dfrac{\partial \ell_i}{\partial \mathbf{f}_k},$

## Slide 37

# Backward pass

**Figura:** Mismo diagrama de MLP.

1. Escribe esto como una serie de cálculos intermedios.
2. Calcula estas cantidades intermedias.
3. Toma las derivadas de la salida con respecto a las cantidades intermedias.
4. Toma las derivadas con respecto a los parámetros.

$\mathbf{f}_0 = \boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}_i$
$\mathbf{h}_1 = \mathbf{a}[\mathbf{f}_0]$
$\mathbf{f}_1 = \boldsymbol{\beta}_1 + \boldsymbol{\Omega}_1 \mathbf{h}_1$
$\mathbf{h}_2 = \mathbf{a}[\mathbf{f}_1]$
$\mathbf{f}_2 = \boldsymbol{\beta}_2 + \boldsymbol{\Omega}_2 \mathbf{h}_2$
$\mathbf{h}_3 = \mathbf{a}[\mathbf{f}_2]$
$\mathbf{f}_3 = \boldsymbol{\beta}_3 + \boldsymbol{\Omega}_3 \mathbf{h}_3$
$\ell_i = \mathrm{l}[\mathbf{f}_3, y_i]$

$\dfrac{\partial \ell_i}{\partial \boldsymbol{\Omega}_k} = \dfrac{\partial \mathbf{f}_k}{\partial \boldsymbol{\Omega}_k}\dfrac{\partial \ell_i}{\partial \mathbf{f}_k}$

$= \dfrac{\partial}{\partial \boldsymbol{\Omega}_k}(\boldsymbol{\beta}_k + \boldsymbol{\Omega}_k \mathbf{h}_k)\dfrac{\partial \ell_i}{\partial \mathbf{f}_k}$

$= \dfrac{\partial \ell_i}{\partial \mathbf{f}_k}\mathbf{h}_k^T$

## Slide 38

# Resumen de Backpropagation

**Forward pass:** We compute and store the following quantities:

$\mathbf{f}_0 = \boldsymbol{\beta}_0 + \boldsymbol{\Omega}_0 \mathbf{x}_i$
$\mathbf{h}_k = \mathbf{a}[\mathbf{f}_{k-1}] \qquad k \in \{1, 2, \dots K\}$
$\mathbf{f}_k = \boldsymbol{\beta}_k + \boldsymbol{\Omega}_k \mathbf{h}_k. \qquad k \in \{1, 2, \dots K\}$

**Figura:** Cadena horizontal de nodos circulares conectados por flechas de izquierda a derecha: $x_i \rightarrow f_0 \rightarrow h_1 \rightarrow f_1 \rightarrow h_2 \rightarrow f_2 \rightarrow h_3 \rightarrow f_3 \rightarrow \ell_i$.

## Slide 39

# Resumen de Backpropagation

**Backward pass:** We start with the derivative $\partial \ell_i/\partial \mathbf{f}_K$ (recuadro resaltado) of the loss function $\ell_i$ with respect to the network output $\mathbf{f}_K$ and work backward through the network:

$\dfrac{\partial \ell_i}{\partial \boldsymbol{\beta}_k} = \dfrac{\partial \ell_i}{\partial \mathbf{f}_k} \qquad k \in \{K, K-1, \dots 1\}$

$\dfrac{\partial \ell_i}{\partial \boldsymbol{\Omega}_k} = \dfrac{\partial \ell_i}{\partial \mathbf{f}_k}\mathbf{h}_k^T \qquad k \in \{K, K-1, \dots 1\}$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_{k-1}} = \mathbb{I}[\mathbf{f}_{k-1} > 0] \odot \left(\boldsymbol{\Omega}_k^T \dfrac{\partial \ell_i}{\partial \mathbf{f}_k}\right), \qquad k \in \{K, K-1, \dots 1\} \qquad (7.13)$

where $\odot$ denotes pointwise multiplication and $\mathbb{I}[\mathbf{f}_{k-1} > 0]$ is a vector containing ones where $\mathbf{f}_{k-1}$ is greater than zero and zeros elsewhere. Finally, we compute the derivatives with respect to the first set of biases and weights:

**Figura:** Cadena horizontal de nodos circulares: $x_i \rightarrow \partial \ell_i/\partial f_0 \rightarrow \partial \ell_i/\partial h_1 \rightarrow \partial \ell_i/\partial f_1 \rightarrow \partial \ell_i/\partial h_2 \rightarrow \partial \ell_i/\partial f_2 \rightarrow \partial \ell_i/\partial h_3 \rightarrow \partial \ell_i/\partial f_3 \rightarrow \ell_i$, con recuadros resaltando los nodos $\partial \ell_i/\partial f_2$ y $\partial \ell_i/\partial f_3$. De cada nodo $\partial \ell_i/\partial f_k$ (k=0,1,2,3) salen dos flechas hacia un par de nodos hijos $\partial \ell_i/\partial \beta_k$ y $\partial \ell_i/\partial \Omega_k$; el par correspondiente a k=3 aparece resaltado con recuadro.

## Slide 40

# Resumen de Backpropagation

**Backward pass:** We start with the derivative $\partial \ell_i/\partial \mathbf{f}_K$ of the loss function $\ell_i$ with respect to the network output $\mathbf{f}_K$ and work backward through the network:

$\dfrac{\partial \ell_i}{\partial \boldsymbol{\beta}_k} = \dfrac{\partial \ell_i}{\partial \mathbf{f}_k} \qquad k \in \{K, K-1, \dots 1\}$

$\dfrac{\partial \ell_i}{\partial \boldsymbol{\Omega}_k} = \dfrac{\partial \ell_i}{\partial \mathbf{f}_k}\mathbf{h}_k^T \qquad k \in \{K, K-1, \dots 1\}$

$\dfrac{\partial \ell_i}{\partial \mathbf{f}_{k-1}} = \mathbb{I}[\mathbf{f}_{k-1} > 0] \odot \left(\boldsymbol{\Omega}_k^T \dfrac{\partial \ell_i}{\partial \mathbf{f}_k}\right), \qquad k \in \{K, K-1, \dots 1\} \qquad (7.13)$

where $\odot$ denotes pointwise multiplication and $\mathbb{I}[\mathbf{f}_{k-1} > 0]$ is a vector containing ones where $\mathbf{f}_{k-1}$ is greater than zero and zeros elsewhere. Finally, we compute the derivatives with respect to the first set of biases and weights:

$\dfrac{\partial \ell_i}{\partial \boldsymbol{\beta}_0} = \dfrac{\partial \ell_i}{\partial \mathbf{f}_0}$

$\dfrac{\partial \ell_i}{\partial \boldsymbol{\Omega}_0} = \dfrac{\partial \ell_i}{\partial \mathbf{f}_0}\mathbf{x}_i^T$

## Slide 41

**3.**
Multi-layer Perceptron
*Ejemplo*

## Slide 42

Ejemplo

**Figura:** Diagrama de una red neuronal multicapa. Input layer con dos nodos ($i_1$, $i_2$, en amarillo). Hidden layer con dos nodos ($h_1$, $h_2$, en celeste). Output layer con un nodo (out, en verde), etiquetado como "prediction". Las conexiones de $i_1$ e $i_2$ hacia $h_1$ y $h_2$ pasan por pesos $w_1$, $w_2$ (azul, hacia $h_1$) y $w_3$, $w_4$ (naranja, hacia $h_2$). Las conexiones de $h_1$ y $h_2$ hacia "out" pasan por pesos $w_5$ y $w_6$ (gris).

## Slide 43

Ejemplo

**Figura:** Mismo diagrama de red que el slide anterior, ahora con valores numéricos asignados a los pesos: $w_1=.11$, $w_2=.21$, $w_3=.12$, $w_4=.08$, $w_5=.14$, $w_6=.15$. A la derecha se muestra el bloque "Input" con los valores $2$ (para $i_1$) y $3$ (para $i_2$), y el bloque "Actual output" con el valor $1$ (círculo morado).

## Slide 44

Ejemplo

**Figura:** Mismo diagrama de red con los inputs sustituidos por sus valores reales: el nodo $i_1$ ahora es $2$, el nodo $i_2$ es $3$. Los nodos ocultos muestran sus valores calculados: $h_1 = .85$, $h_2 = .48$. El nodo de salida muestra $.191$. A la derecha, "Input" = 2, 3; "Actual output" = 1.

Debajo del diagrama, una flecha etiquetada "Forward Pass" apunta hacia la derecha, y bajo ella se muestra la operación matricial equivalente, señalada como "Matrix multiplication":

$[2 \quad 3] \cdot \begin{bmatrix} 0.11 & 0.12 \\ 0.21 & 0.08 \end{bmatrix} = [0.85 \quad 0.48] \cdot \begin{bmatrix} 0.14 \\ 0.15 \end{bmatrix} = [0.191]$

Un recuadro "Details" muestra el desglose de las multiplicaciones:
$2 \times .11 + 3 \times .21 = .85$
$2 \times .12 + 3 \times .08 = .48$
$.85 \times .14 + .48 \times .15 = .191$

## Slide 45

Ejemplo

**Figura:** Mismo diagrama de red de los slides anteriores (valores $2$, $3$ como inputs; $h_1=.85$, $h_2=.48$; salida $.191$), con flechas que señalan "prediction" (apuntando al nodo de salida $.191$) y "actual" (apuntando al bloque morado con valor $1$ en "Actual output").

Debajo, un recuadro rojo con la fórmula del error:

$Error = \frac{1}{2}(prediction - actual)^2$

Con anotaciones:
- "Error = 0, if prediction = actual" (flecha hacia la fórmula)
- "$\frac{1}{2}$ is added to ease the calculation of the derivative" (flecha hacia el $\frac{1}{2}$)
- "Error is always positive because of the square" (flecha hacia el exponente 2)

Al final, el cálculo numérico:

$Error = \frac{1}{2}(0.191 - 1.0)^2 = 0.327$

## Slide 46

Ejemplo

**prediction** = out

$\downarrow$

**prediction** = $(h_1) w_5 + (h_2) w_6$

(con nota lateral: $h_1 = i_1 w_1 + i_2 w_2$; $h_2 = i_1 w_3 + i_2 w_4$)

$\downarrow$

**prediction** = $(i_1 w_1 + i_2 w_2) w_5 + (i_1 w_3 + i_2 w_4) w_6$

Recuadro amarillo: "to change **prediction** value, we need to change **weights**"

Fórmula de actualización de pesos (gradiente descendente):

$^*W_x = W_x - a \left( \frac{\partial Error}{\partial W_x} \right)$

Anotaciones:
- "Old weight" → $W_x$ (el que se resta)
- "New weight" → $^*W_x$
- "Learning rate" → $a$
- "Derivative of Error with respect to weight" → $\frac{\partial Error}{\partial W_x}$

## Slide 47

Ejemplo

Derivación de $\frac{\partial Error}{\partial W_6}$ mediante la regla de la cadena ("chain rule"):

$\frac{\partial Error}{\partial W_6} = \frac{\partial Error}{\partial prediction} * \frac{\partial prediction}{\partial W_6}$

Recuadros de referencia a la derecha:
- $Error = \frac{1}{2}(prediction - actual)^2$
- $prediction = (i_1 w_1 + i_2 w_2) w_5 + (i_1 w_3 + i_2 w_4) w_6$

Desarrollo paso a paso:

$\frac{\partial Error}{\partial W_6} = \frac{\partial \frac{1}{2}(prediction-actual)^2}{\partial prediction} * \frac{\partial (i_1 w_1 + i_2 w_2) w_5 + (i_1 w_3 + i_2 w_4) w_6}{\partial W_6}$

$\frac{\partial Error}{\partial W_6} = 2 * \frac{1}{2}(prediction - actual) \frac{\partial(prediction-actual)}{\partial prediction} * (i_1 w_3 + i_2 w_4)$

(con nota lateral: $h_2 = i_1 w_3 + i_2 w_4$)

$\frac{\partial Error}{\partial W_6} = (prediction - actual)*(h_2)$

(con nota lateral: $\Delta = prediction - actual$ → "delta")

$\frac{\partial Error}{\partial W_6} = \Delta h_2$

## Slide 48

Ejemplo

Derivación de $\frac{\partial Error}{\partial W_1}$ mediante la regla de la cadena ("chain rule"):

$\frac{\partial Error}{\partial W_1} = \frac{\partial Error}{\partial prediction} * \frac{\partial prediction}{\partial h_1} * \frac{\partial h_1}{\partial W_1}$

Recuadros de referencia a la derecha:
- $Error = \frac{1}{2}(prediction - actual)^2$
- $prediction = (h_1) w_5 + (h_2) w_6$
- $h_1 = i_1 w_1 + i_2 w_2$

Desarrollo paso a paso:

$\frac{\partial Error}{\partial W_1} = \frac{\partial \frac{1}{2}(prediction-actual)^2}{\partial prediction} * \frac{\partial (h_1) w_5 + (h_2) w_6}{\partial h_1} * \frac{\partial i_1 w_1 + i_2 w_2}{\partial w_1}$

$\frac{\partial Error}{\partial W_1} = 2 * \frac{1}{2}(prediction - actual) \frac{\partial(prediction-actual)}{\partial prediction} * (w_5) * (i_1)$

$\frac{\partial Error}{\partial W_1} = (prediction - actual)*(w_5 i_1)$

(con nota lateral: $\Delta = prediction - actual$ → "delta")

$\frac{\partial Error}{\partial W_1} = \Delta w_5 i_1$

## Slide 49

Ejemplo

Fórmulas de actualización de pesos ("Updated weights"):

$^*w_6 = w_6 - a (h_2 . \Delta)$
$^*w_5 = w_5 - a (h_1 . \Delta)$
$^*w_4 = w_4 - a (i_2 . \Delta w_6)$
$^*w_3 = w_3 - a (i_1 . \Delta w_6)$
$^*w_2 = w_2 - a (i_2 . \Delta w_5)$
$^*w_1 = w_1 - a (i_1 . \Delta w_5)$

## Slide 50

Ejemplo

**Figura:** Repetición del diagrama del slide 44/45 (recapitulación): red con inputs $2$, $3$; pesos $w_1=.11$, $w_2=.21$, $w_3=.12$, $w_4=.08$, $w_5=.14$, $w_6=.15$; nodos ocultos $h_1=.85$, $h_2=.48$; salida $.191$. A la derecha, "Input" = 2, 3; "Actual output" = 1.

Debajo, el recuadro rojo con la fórmula del error:

$Error = \frac{1}{2}(prediction - actual)^2$

Con las mismas anotaciones que en el slide 45: "Error = 0, if prediction = actual", "$\frac{1}{2}$ is added to ease the calculation of the derivative", "Error is always positive because of the square".

Cálculo numérico final:

$Error = \frac{1}{2}(0.191 - 1.0)^2 = 0.327$

## Slide 51

Ejemplo

$\Delta = 0.191 - 1 = -0.809$ (Delta = prediction - actual)

$a = 0.05$ (Learning rate, we smartly guess this number)

Actualización de los pesos de la capa de salida:

$\begin{bmatrix} w_5 \\ w_6 \end{bmatrix} = \begin{bmatrix} 0.14 \\ 0.15 \end{bmatrix} - 0.05(-0.809)\begin{bmatrix} 0.85 \\ 0.48 \end{bmatrix} = \begin{bmatrix} 0.14 \\ 0.15 \end{bmatrix} - \begin{bmatrix} -0.034 \\ -0.019 \end{bmatrix} = \begin{bmatrix} 0.17 \\ 0.17 \end{bmatrix}$

Actualización de los pesos de la capa oculta:

$\begin{bmatrix} w_1 & w_3 \\ w_2 & w_4 \end{bmatrix} = \begin{bmatrix} .11 & .12 \\ .21 & .08 \end{bmatrix} - 0.05(-0.809)\begin{bmatrix} 2 \\ 3 \end{bmatrix}.[0.14 \quad 0.15] = \begin{bmatrix} .11 & .12 \\ .21 & .08 \end{bmatrix} - \begin{bmatrix} -0.011 & -0.012 \\ -0.017 & -0.018 \end{bmatrix} = \begin{bmatrix} .12 & .13 \\ .23 & .10 \end{bmatrix}$

## Slide 52

Ejemplo

**Figura:** Diagrama de red con los pesos ya actualizados tras la primera iteración de backpropagation: $w_1=.12$, $w_2=.23$ (azul, hacia $h_1$); $w_3=.13$, $w_4=.1$ (naranja, hacia $h_2$); $w_5=.17$, $w_6=.17$ (gris, hacia out). Inputs $2$ y $3$. Valores calculados: $h_1=.92$, $h_2=.56$, salida (prediction) = $.26$.

Debajo, flecha "Forward Pass" y la operación matricial equivalente ("Matrix multiplication"):

$[2 \quad 3] \cdot \begin{bmatrix} 0.12 & 0.13 \\ 0.23 & 0.10 \end{bmatrix} = [0.92 \quad 0.56] \cdot \begin{bmatrix} 0.17 \\ 0.17 \end{bmatrix} = [0.26]$

Recuadro "Details" con el desglose:
$2 \times .12 + 3 \times .23 = .85$
$2 \times .13 + 3 \times .10 = .48$
$.92 \times .17 + .56 \times .17 = .26$

## Slide 53

**4.**
Multi-layer Perceptron
*Limitaciones*

## Slide 54

Monitorear el Error

Revisa cómo se comporta tu función de pérdida durante el entrenamiento para detectar hiperparámetros incorrectos, errores, etc.

**Figura (izquierda):** Gráfico de líneas "loss" vs. "epoch" con cuatro curvas etiquetadas: "very high learning rate" (naranja, diverge y sube abruptamente), "low learning rate" (morado, desciende lento y de forma sostenida), "high learning rate" (verde, desciende rápido al inicio y luego se estanca en un valor alto), "good learning rate" (rojo, desciende de forma rápida y sostenida hasta un valor bajo).

**Figura (derecha):** Gráfico real de "Loss" vs. "Epoch" (0 a 100) mostrando una curva morada ruidosa que oscila pero desciende en tendencia general desde ~2.0 hasta ~0.75-1.0.

## Slide 55

Learning Rate

Qué tan grandes o pequeños son los pasos que toma el descenso por gradiente en la dirección del mínimo local está determinado por la tasa de aprendizaje, que define qué tan rápido o lento nos moveremos hacia los pesos óptimos.

**Figura:** Tres gráficos de $J(\theta)$ vs. $\theta$ (forma de parábola), cada uno mostrando el recorrido del descenso por gradiente con flechas rojas:
- "Too low": muchos pasos pequeños acercándose lentamente al mínimo. Texto: "A small learning rate requires many updates before reaching the minimum point".
- "Just right": pocos pasos que llegan rápidamente al mínimo. Texto: "The optimal learning rate swiftly reaches the minimum point".
- "Too high": pasos grandes que rebotan de un lado a otro de la parábola, alejándose en vez de converger. Texto: "Too large of a learning rate causes drastic updates which lead to divergent behaviors".

## Slide 56

Descenso de la Gradiente

**El descenso de la gradiente estocástico** actualiza los parámetros del modelo uno por uno. Si el modelo tiene un conjunto de datos de 10,000 ejemplos, el SGD actualizará los parámetros del modelo 10,000 veces.

**El descenso de la gradiente con mini batch** divide el conjunto de datos de entrenamiento en pequeños batches y realiza una actualización para cada uno de esos batches. Mantiene robustez y eficiencia.

**Figura (izquierda):** Curvas de nivel elípticas concéntricas (contour plot) con una trayectoria en zigzag muy ruidosa (rojo) que rebota mucho antes de llegar al punto óptimo marcado con "+", ilustrando el comportamiento del descenso estocástico.

**Figura (derecha):** Mismas curvas de nivel elípticas con una trayectoria mucho más suave y directa (rojo) hacia el punto óptimo "+", ilustrando el comportamiento del descenso por mini-batch.

## Slide 57

Monitorear el Error

Optimizadores para descenso por gradiente

**Figura (izquierda):** Gráfico de contorno (curvas de nivel tipo silla de montar, coloreado en degradado azul-amarillo-rojo) mostrando las trayectorias de convergencia de distintos optimizadores desde un punto de inicio hasta el óptimo (marcado con una estrella): SGD (rojo), Momentum (verde), NAG (magenta), Adagrad (azul), Adadelta (amarillo claro), Rmsprop (negro). Las trayectorias muestran distintos caminos y velocidades de convergencia alrededor del punto de silla.

**Figura (derecha):** Superficie 3D tipo silla de montar (rojo en los bordes elevados, azul en el centro) con los mismos seis optimizadores (SGD, Momentum, NAG, Adagrad, Adadelta, Rmsprop) graficados como trayectorias de colores sobre la superficie, mostrando cómo cada uno desciende desde un punto inicial común hacia la región de menor error.

## Slide 58

Desvanecimiento de la gradiente

**Figura (izquierda) — "Vanishing Gradient":** Gráfico de "Gradient" vs. "Layer" (Input, Layer 1, Layer 2, Layer 3, Output) con una curva morada punteada que crece exponencialmente desde un valor muy bajo en el Input hasta un valor alto en el Output; una flecha en el extremo izquierdo (Input) señala hacia atrás indicando que el gradiente que llega ahí es casi nulo.

**Figura (derecha) — "Exploding Gradient":** Gráfico de "Gradient" vs. "Layer" con una curva morada punteada que empieza muy alta en el Input (con una flecha que sube aún más antes de bajar) y decae rápidamente hacia valores bajos en las capas siguientes hasta el Output.

## Slide 59

Regularización: Dropout

**Figura:** Cuatro diagramas (a, b, c, d) de una red neuronal con capa de entrada ($x_1$, $x_2$, $x_3$), dos capas ocultas y una salida ($y$):
- a) Red completa sin dropout, todas las neuronas y conexiones activas.
- b) Red con dos neuronas desactivadas (sombreadas en gris) en las capas ocultas, ilustrando una máscara de dropout distinta.
- c) Red con la mayoría de neuronas ocultas desactivadas, dejando solo una neurona activa por capa oculta.
- d) Red con otras neuronas desactivadas (patrón de dropout diferente al de b).

Texto bajo las figuras: "Dropout was applied in the fully connected layers".

## Slide 60

Monitorear el Error

Revisa cómo se comporta tu función de pérdida durante el entrenamiento para detectar hiperparámetros incorrectos, errores, etc.

**Figura:** Gráfico de "accuracy" vs. "epoch" con tres curvas: "training accuracy" (roja, sube y se estabiliza en un valor alto), "validation accuracy: little overfitting" (verde, sigue de cerca a la curva de entrenamiento con una brecha pequeña), "validation accuracy: strong overfitting" (morada, sube al inicio pero luego se estanca y comienza a descender levemente, mostrando una brecha grande respecto a la curva de entrenamiento).

## Slide 61

# Final Takeaways

1. La regla de la cadena se implementa mediante variables intermedias en el cálculo de gradientes.

2. En una MLP, el backward pass reutiliza los mismos valores intermedios para actualizar pesos y sesgos.

3. Las funciones de activación con regiones de pendiente constante (como ReLU) simplifican las derivadas y mejoran la propagación de gradientes.

4. Monitorear la evolución de la función de pérdida y escoger el optimizador adecuado es crítico para evitar estancamientos y errores.

## Slide 62

(Slide de cierre sin texto: fotografía de fondo con tinte azul mostrando a dos personas con bata de laboratorio y lentes de protección examinando un equipo/estructura metálica con cableado, en un laboratorio.)
