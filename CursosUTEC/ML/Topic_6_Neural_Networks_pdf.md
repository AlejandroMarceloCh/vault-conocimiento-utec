---
curso: ML
titulo: Topic 6 - Neural Networks
slides: 46
fuente: Topic 6 - Neural Networks.pdf
---

## Slide 1

INTRODUCCIÓN A REDES NEURONALES

## Slide 2

### Objetivos

1. Desarrollar intuición sobre redes neuronales (perceptrón)
2. Entender el Perceptrón Multicapa (MLP) sin backpropagation
3. Comprender el Teorema del Aproximador Universal
4. Explorar el impacto de la profundidad y el ancho de la red

## Slide 3

0.

Introducción
*Recap*

## Slide 4

¿Modelos Lineares?

## Slide 5

### Regresión linear 1D y funciones de error

**Figura:** Cuatro paneles (a, b, c, d) con gráficos de dispersión "Output, $y$" vs "Input, $x$" (ejes de 0.0 a 2.0). El panel a) muestra solo los puntos de datos (círculos naranjas) sin línea de ajuste. Los paneles b), c) y d) muestran la misma nube de puntos con distintas rectas de regresión ajustadas y sus residuos (líneas punteadas verticales naranjas) marcados:
- b) recta con $\phi_0=0.4, \phi_1=0.2$, Loss $L=7.07$.
- c) recta con $\phi_0=1.60, \phi_1=-0.8$, Loss $L=10.28$.
- d) recta con $\phi_0=0.82, \phi_1=0.52$, Loss $L=0.20$ (la que mejor ajusta, menor pérdida).

## Slide 6

### Funciones de error y parámetros

**Figura:** Panel a) superficie 3D de la función de pérdida $L[\phi]$ en función de Slope ($\phi_1$, eje de -1.0 a 1.0) e Intercept ($\phi_0$, eje de 0.0 a 2.0), con forma de valle curvo; se marcan tres puntos (uno gris claro en la ladera alta, dos verdes cerca del mínimo). Panel b) el mismo paisaje de pérdida representado como mapa de contorno 2D (Intercept $\phi_0$ en eje x de 0.0 a 2.0, Slope $\phi_1$ en eje y de -1.0 a 1.0), con los mismos tres puntos marcados sobre las curvas de nivel.

Ecuaciones:

$\hat{\boldsymbol\phi} = \underset{\boldsymbol\phi}{\operatorname{argmin}}\big[L[\boldsymbol\phi]\big]$

$= \underset{\boldsymbol\phi}{\operatorname{argmin}}\left[\sum_{i=1}^{I} (\mathrm{f}[x_i,\boldsymbol\phi] - y_i)^2\right]$

$= \underset{\boldsymbol\phi}{\operatorname{argmin}}\left[\sum_{i=1}^{I} (\phi_0 + \phi_1 x_i - y_i)^2\right]$

## Slide 7

### Optimización

**Figura:** Panel a) mapa de contorno de pérdida $L[\phi]$ (Intercept $\phi_0$ en eje x de 0.0 a 2.0, Slope $\phi_1$ en eje y de -1.0 a 1.0) con una trayectoria de puntos numerados 0, 1, 2, 3, 4 que descienden desde la esquina superior izquierda hacia el mínimo de la función, conectados por una línea gris con flechas. Panel b) gráfico de dispersión Output $y$ vs Input $x$ (ejes 0.0–2.0) con los puntos de datos naranjas y cinco rectas de regresión (numeradas 0 a 4, en tonos de verde cada vez más oscuros) que representan las iteraciones sucesivas del ajuste, mejorando progresivamente hasta la recta 4 (verde oscuro), la de mejor ajuste.

Esta técnica se llama **descenso de la gradiente**.

## Slide 8

### Limitaciones de Clasificadores Lineales

Los clasificadores lineales (por ejemplo, regresión logística) clasifican entradas basándose en combinaciones lineales de las características $x_i$.

Muchas decisiones implican funciones no lineales de la entrada.

Ejemplo clásico: ¿Tienen dos elementos de entrada el mismo valor?

Los casos positivos y negativos no pueden separarse con un plano.

¿Qué podemos hacer?

**Figura:** Cuadrado unitario con vértices etiquetados (0,0) en negro abajo a la izquierda, (0,1) en negro arriba a la izquierda, (1,1) en blanco/vacío arriba a la derecha, (1,0) en negro abajo a la derecha. Una línea recta diagonal cruza el cuadrado dividiéndolo en dos regiones etiquetadas "output = 1" (arriba) y "output = 0" (abajo), ilustrando que una frontera lineal no puede separar correctamente los vértices con el mismo valor (XOR) de los que tienen valores distintos.

## Slide 9

1.

Introducción
*Motivación*

## Slide 10

### Inspiración: El cerebro

Muchos métodos de aprendizaje supervisado están inspirados en la biología, por ejemplo, en el cerebro (humano).

Nuestro cerebro tiene ~10¹¹ neuronas, cada una de las cuales se comunica (está conectada) con alrededor de 10⁴ otras neuronas.

**Figura:** Diagrama de una neurona biológica con las partes etiquetadas en inglés: "dendrites" (dendritas, con flecha "impulses carried toward cell body"), "nucleus" (núcleo), "cell body" (cuerpo celular), "axon" (axón, con flecha "impulses carried away from cell body"), "branches of axon" (ramas del axón) y "axon terminals" (terminales del axón).

## Slide 11

### Matemática de una neurona

Las redes neuronales definen funciones de los inputs (**características ocultas**), calculadas por neuronas.

Las neuronas artificiales se llaman unidades.

**Figura:** Diagrama de una neurona artificial (analogía con la biológica). Entrada $x_0$ llega por "axon from a neuron", pasa por una "synapse" (punto rojo) que la pondera como $w_0 x_0$ vía "dendrite"; junto con otras entradas ponderadas $w_1x_1$ y $w_2x_2$, todas convergen al "cell body", donde se calcula la suma $\sum_i w_i x_i + b$, que pasa por la "activation function" $f$ (punto morado), produciendo la salida $f\left(\sum_i w_i x_i + b\right)$ que sale por el "output axon".

## Slide 12

### Funciones de activación

Sigmoid: $\sigma(z) = \dfrac{1}{1+\exp(-z)}$

Tanh: $\tanh(z) = \dfrac{\exp(z)-\exp(-z)}{\exp(z)+\exp(-z)}$

ReLU (Rectified Linear Unit): $\mathrm{ReLU}(z) = \max(0,z)$

**Figura:** Tres gráficos lado a lado, eje x $z$ de -8 a 8. Izquierda: curva sigmoide (morada) $f(z)=1/(1+\exp(-z))$, forma de S de 0 a 1. Centro: curva tanh (roja) $f(z)=[\exp(z)-\exp(-z)]/[\exp(z)+\exp(-z)]$, forma de S de -1 a 1. Derecha: curva ReLU (verde) $f(z)=\max(0,z)$, plana en 0 para $z<0$ y lineal creciente para $z\geq0$, hasta 8.

## Slide 13

### Arquitectura: Multi-Layer Perceptron

Cada unidad calcula su valor basado en una combinación lineal de los valores de las unidades que apuntan hacia ella y una función de activación.

**Figura:** Dos diagramas de redes neuronales. Izquierda: red con "input units" (3 nodos inferiores), dos capas ocultas intermedias (nodos rojos y verdes resaltados en cada capa) y "output units" (2 nodos superiores), con flechas conectando cada nodo de una capa con los de la siguiente. Derecha: diagrama equivalente organizado en columnas de color, etiquetadas "input layer" (rosa, 3 nodos), "hidden layer" (azul, 4 nodos) y "output layer" (verde, 2 nodos), con todas las conexiones (flechas) entre capas adyacentes.

## Slide 14

### Ejemplos de Redes Neuronales

**Regresión Lineal 1D**

$y = \mathrm{f}[x,\boldsymbol\phi]$
$= \phi_0 + \phi_1 x$

**Shallow network**

$y = \mathrm{f}[x,\boldsymbol\phi]$
$= \phi_0 + \phi_1 \mathrm{a}[\theta_{10}+\theta_{11}x] + \phi_2 \mathrm{a}[\theta_{20}+\theta_{21}x] + \phi_3 \mathrm{a}[\theta_{30}+\theta_{31}x]$

## Slide 15

### Ejemplo de Red Neuronal

$y = \mathrm{f}[x,\boldsymbol\phi]$
$= \phi_0 + \phi_1 \mathrm{a}[\theta_{10}+\theta_{11}x] + \phi_2 \mathrm{a}[\theta_{20}+\theta_{21}x] + \phi_3 \mathrm{a}[\theta_{30}+\theta_{31}x]$

$\mathrm{a}[z] = \mathrm{ReLU}[z] = \begin{cases} 0 & z<0 \\ z & z\geq0 \end{cases}$

**Rectified Linear Unit** (particular kind of activation function)

**Figura:** Gráfico de la función ReLU$[z]$ vs $z$ (ambos ejes de -5.0 a 5.0), línea naranja plana en 0 para $z<0$ y creciente linealmente con pendiente 1 para $z\geq0$, alcanzando 5.0 en $z=5.0$. Etiqueta "Activation function" con flechas apuntando a los términos a[...] de la ecuación.

## Slide 16

### Ejemplo de Red Neuronal

$y = \mathrm{f}[x,\boldsymbol\phi]$
$= \phi_0 + \phi_1 \mathrm{a}[\theta_{10}+\theta_{11}x] + \phi_2 \mathrm{a}[\theta_{20}+\theta_{21}x] + \phi_3 \mathrm{a}[\theta_{30}+\theta_{31}x]$

This model has 10 parameters:

$\boldsymbol\phi = \{\phi_0,\phi_1,\phi_2,\phi_3,\theta_{10},\theta_{11},\theta_{20},\theta_{21},\theta_{30},\theta_{31}\}$

- Represents a family of functions
- Parameters determine particular function
- Given parameters can perform inference (run equation)
- Given training dataset $\{\mathbf{x}_i,\mathbf{y}_i\}_{i=1}^{I}$
- Define loss function $L[\boldsymbol\phi]$ (least squares)
- Change parameters to minimize loss function

## Slide 17

### Unidades Ocultas

$y = \phi_0 + \phi_1 \mathrm{a}[\theta_{10}+\theta_{11}x] + \phi_2 \mathrm{a}[\theta_{20}+\theta_{21}x] + \phi_3 \mathrm{a}[\theta_{30}+\theta_{31}x].$

Desglosado en dos partes:

$y = \phi_0 + \phi_1 h_1 + \phi_2 h_2 + \phi_3 h_3$

donde:

$h_1 = \mathrm{a}[\theta_{10}+\theta_{11}x]$
$h_2 = \mathrm{a}[\theta_{20}+\theta_{21}x]$
$h_3 = \mathrm{a}[\theta_{30}+\theta_{31}x]$

## Slide 18

### Neural Network: Paso a Paso

$y = \phi_0 + \phi_1 \mathrm{a}[\theta_{10}+\theta_{11}x] + \phi_2 \mathrm{a}[\theta_{20}+\theta_{21}x] + \phi_3 \mathrm{a}[\theta_{30}+\theta_{31}x].$

1. Calcula tres funciones lineales.

**Figura:** Tres gráficos (a, b, c) de Output vs eje x (0.0 a 2.0), eje y de -1.0 a 1.0, cada uno con una recta: a) $\theta_{10}+\theta_{11}x$ (naranja, pendiente positiva); b) $\theta_{20}+\theta_{21}x$ (verde/turquesa, pendiente positiva más pronunciada); c) $\theta_{30}+\theta_{31}x$ (gris oscuro, pendiente negativa).

## Slide 19

### Neural Network: Paso a Paso

$y = \phi_0 + \phi_1 \mathrm{a}[\theta_{10}+\theta_{11}x] + \phi_2 \mathrm{a}[\theta_{20}+\theta_{21}x] + \phi_3 \mathrm{a}[\theta_{30}+\theta_{31}x].$

2. Pásalas por funciones ReLU (crea unidades ocultas).

**Figura:** Tres gráficos (d, e, f) de Output vs eje x (0.0 a 2.0), eje y de -1.0 a 1.0, mostrando las mismas tres rectas del paso anterior pero recortadas por ReLU (parte plana en 0 y luego la pendiente original): d) $h_1=\mathrm{a}[\theta_{10}+\theta_{11}x]$ (naranja, plano hasta ~x=0.5 luego sube); e) $h_2=\mathrm{a}[\theta_{20}+\theta_{21}x]$ (verde/turquesa, plano hasta ~x=1.0 luego sube fuerte); f) $h_3=\mathrm{a}[\theta_{30}+\theta_{31}x]$ (gris oscuro, empieza alto en 1.0 y decrece linealmente, sin tramo plano visible en el rango mostrado).

## Slide 20

### Neural Network: Paso a Paso

$y = \phi_0 + \phi_1 \mathrm{a}[\theta_{10}+\theta_{11}x] + \phi_2 \mathrm{a}[\theta_{20}+\theta_{21}x] + \phi_3 \mathrm{a}[\theta_{30}+\theta_{31}x].$

3. Asigna pesos a las unidades ocultas.

**Figura:** Tres gráficos (g, h, i) de Output vs eje x (0.0 a 2.0), eje y de -1.0 a 1.0, mostrando las unidades ocultas ya ponderadas por $\phi_i$: g) $\phi_1 h_1$ (naranja, plano en 0 hasta ~x=0.5, luego decrece hasta cerca de -0.8 en x=2.0, indicando peso negativo); h) $\phi_2 h_2$ (verde/turquesa, plano en 0 hasta ~x=1.0, luego sube hasta cerca de 1.0 en x=2.0, peso positivo); i) $\phi_3 h_3$ (gris oscuro, comienza alto cerca de 0.7 en x=0, decrece linealmente hasta 0 alrededor de x=1.5 y luego se mantiene plano en 0).

## Slide 21

# Neural Network: Paso a Paso

4. Suma las unidades ocultas ponderadas para generar la salida.

**Figura:** Cuatro paneles.
- g) curva $\phi_1 h_1$ (naranja): 0 constante desde x=0 hasta x≈0.5, luego decrece linealmente hasta aprox. -0.75 en x=2.0. Eje Output de -1.0 a 1.0, eje Input, $x$ de 0.0 a 2.0.
- h) curva $\phi_2 h_2$ (verde agua): 0 constante desde x=0 hasta x=1.0, luego crece linealmente hasta 1.0 en x≈1.8.
- i) curva $\phi_3 h_3$ (gris oscuro): comienza en aprox. 0.75 en x=0, decrece linealmente hasta 0 en x≈1.5, luego constante en 0.
- j) curva suma $\phi_0+\phi_1h_1+\phi_2h_2+\phi_3h_3$ (azul oscuro): comienza en aprox. 0.55 en x=0, decrece hasta un mínimo local de aprox. -0.25 cerca de x=1.0, luego sube ligeramente y termina cerca de 0.05 en x=2.0. Tiene una región sombreada en gris entre aprox. x=0.5 y x=1.0.

## Slide 22

# Neural Network: Paso a Paso

Patrón de activación = qué unidades ocultas están activadas

Región sombreada:
Unidad 1 activa
Unidad 2 inactiva
Unidad 3 activa

**Figura:** Los mismos cuatro paneles g), h), i), j) de la slide anterior, idénticos en forma y valores (curvas $\phi_1h_1$, $\phi_2h_2$, $\phi_3h_3$ y su suma), reutilizados para ilustrar el concepto de patrón de activación sobre la región sombreada del panel j).

## Slide 23

# Representando redes neuronales

$y = \phi_0 + \phi_1 \text{a}[\theta_{10} + \theta_{11}x] + \phi_2 \text{a}[\theta_{20} + \theta_{21}x] + \phi_3 \text{a}[\theta_{30} + \theta_{31}x].$

Funciones lineales a trozos con tres uniones.

**Figura:** Tres paneles a), b), c), cada uno con eje Output, $y$ de -1.0 a 1.0 y eje Input, $x$ de 0.0 a 2.0, mostrando funciones lineales a trozos con tres puntos de quiebre (uniones):
- a) (azul oscuro): comienza en aprox. 0.55, baja con pendiente suave hasta aprox. 0.3 en x≈0.5, cae más pronunciado hasta un mínimo de aprox. -0.2 en x≈1.0, luego se mantiene casi plano y sube levemente hasta aprox. 0.05 en x=2.0.
- b) (naranja): comienza en 0, se mantiene plano hasta x≈0.6, sube hasta un máximo de aprox. 0.4 en x≈1.1, baja levemente hasta x≈1.3, y luego cae fuertemente hasta aprox. -0.7 en x=2.0.
- c) (gris oscuro): comienza en aprox. 0.3, sube hasta un máximo de aprox. 0.9 en x≈0.5-0.6, luego decrece con fuerte pendiente hasta aprox. -0.6 en x≈1.5, y se mantiene plano hasta x=2.0.

## Slide 24

# Representando redes neuronales

$h_1 = \text{a}[\theta_{10} + \theta_{11}x]$
$h_2 = \text{a}[\theta_{20} + \theta_{21}x]$
$h_3 = \text{a}[\theta_{30} + \theta_{31}x]$

$y = \phi_0 + \phi_1 h_1 + \phi_2 h_2 + \phi_3 h_3$

Cada parámetro multiplica su origen y se suma a su destino.

**Figura:** Diagrama de red neuronal etiquetado a). Nodo de sesgo "1" (naranja) conectado a los nodos ocultos $h_1$, $h_2$, $h_3$ mediante flechas etiquetadas $\theta_{10}$, $\theta_{20}$, $\theta_{30}$. Nodo de entrada $x$ conectado a $h_1$, $h_2$, $h_3$ mediante flechas etiquetadas $\theta_{11}$, $\theta_{21}$, $\theta_{31}$. Un segundo nodo de sesgo "1" (naranja) conectado directamente al nodo de salida $y$ con peso $\phi_0$. Los nodos ocultos $h_1$, $h_2$, $h_3$ (con símbolo de activación no lineal en su interior) se conectan al nodo de salida $y$ mediante flechas etiquetadas $\phi_1$, $\phi_2$, $\phi_3$.

## Slide 25

# 2.

# Teorema de aproximador universal

*Teorema base*

**Figura:** Imagen decorativa de fondo — mano robótica señalando una representación abstracta de un cerebro/red digital sobre fondo azul oscuro, con líneas y marcas de medición punteadas en amarillo y celeste.

## Slide 26

# Teorema de aproximador universal

Con 3 unidades ocultas:

$h_1 = \text{a}[\theta_{10} + \theta_{11}x]$
$h_2 = \text{a}[\theta_{20} + \theta_{21}x]$
$h_3 = \text{a}[\theta_{30} + \theta_{31}x]$

$y = \phi_0 + \phi_1 h_1 + \phi_2 h_2 + \phi_3 h_3$

Con D unidades ocultas:

$h_d = \text{a}[\theta_{d0} + \theta_{d1}x]$

$y = \phi_0 + \sum_{d=1}^{D} \phi_d h_d$

## Slide 27

# Teorema de aproximador universal

Con suficientes unidades ocultas, podemos describir cualquier función unidimensional con precisión arbitraria.

**Figura:** Tres paneles a), b), c), cada uno con eje Output, $y$ de -1.0 a 1.0 y eje Input, $x$ de 0.0 a 2.0. En cada panel se superpone una curva objetivo (línea negra punteada, forma de "W" suave: baja desde aprox. 0.55, forma un valle profundo cerca de x≈0.8-0.9 llegando a aprox. -0.85, sube de nuevo hasta un pico de aprox. 0.85 cerca de x≈1.7, y desciende levemente al final) junto con la aproximación lineal a trozos de la red neuronal:
- a) "5 linear regions" (gris): aproximación gruesa con 5 segmentos rectos, sigue la forma general pero con pérdida de detalle en las curvas.
- b) "10 linear regions" (naranja): aproximación con 10 segmentos, sigue más de cerca la curva objetivo.
- c) "20 linear regions" (verde agua): aproximación con 20 segmentos, prácticamente se superpone a la curva punteada objetivo.

## Slide 28

# Capacidad de Representación

Una red neuronal con al menos una capa oculta es un aproximador universal (puede representar cualquier función).

La capacidad de la red aumenta con más unidades ocultas y más capas ocultas. ¿Redes más profundas?

**Figura:** Tres mapas de clasificación 2D ("3 hidden neurons", "6 hidden neurons", "20 hidden neurons"), cada uno con puntos rojos y verdes dispersos sobre un plano dividido en dos regiones de color (rosa/rojo y verde) por una frontera de decisión curva:
- "3 hidden neurons": frontera simple, una única curva diagonal que separa aproximadamente la mitad izquierda (rosa) de la derecha (verde), con algunos puntos mal clasificados.
- "6 hidden neurons": frontera algo más compleja, con una pequeña muesca adicional, mejor ajuste a los puntos.
- "20 hidden neurons": frontera muy compleja con múltiples entrantes y salientes en forma de "dedos" o ramificaciones, ajustándose de manera muy fina a la distribución de puntos rojos y verdes.

## Slide 29

# Dos salidas

$h_1 = \text{a}[\theta_{10} + \theta_{11}x]$
$h_2 = \text{a}[\theta_{20} + \theta_{21}x]$
$h_3 = \text{a}[\theta_{30} + \theta_{31}x]$
$h_4 = \text{a}[\theta_{40} + \theta_{41}x]$

$y_1 = \phi_{10} + \phi_{11}h_1 + \phi_{12}h_2 + \phi_{13}h_3 + \phi_{14}h_4$
$y_2 = \phi_{20} + \phi_{21}h_1 + \phi_{22}h_2 + \phi_{23}h_3 + \phi_{24}h_4$

**Figura:** Panel a) diagrama de red: nodo de entrada $x$ conectado a cuatro nodos ocultos $h_1$, $h_2$, $h_3$, $h_4$, y estos conectados a dos nodos de salida $y_1$ e $y_2$ (todas las conexiones ocultas→salidas presentes). Panel b) gráfico con eje Output, $y$ de -1.0 a 1.0 y eje Input, $x$ de 0.0 a 2.0, mostrando dos curvas lineales a trozos con líneas verticales punteadas marcando los puntos de quiebre: $y_1$ (azul oscuro) comienza en aprox. 0.15, baja levemente hasta un mínimo cerca de -0.25 en x≈1.1, sube hasta aprox. 0.1 en x≈1.5, y termina en aprox. 0.4 en x=2.0; $y_2$ (naranja) comienza en aprox. -0.4, sube hasta un máximo de aprox. 0.35 en x≈1.1, baja hasta aprox. 0.15 en x≈1.5, cae bruscamente a aprox. -0.4 en x≈1.75, y sube levemente al final.

## Slide 30

# Dos salidas

$h_1 = \text{a}[\theta_{10} + \theta_{11}x_1 + \theta_{12}x_2]$
$h_2 = \text{a}[\theta_{20} + \theta_{21}x_1 + \theta_{22}x_2]$
$h_3 = \text{a}[\theta_{30} + \theta_{31}x_1 + \theta_{32}x_2]$

$y = \phi_0 + \phi_1 h_1 + \phi_2 h_2 + \phi_3 h_3$

**Figura:** Diagrama de red con dos nodos de entrada $x_1$ y $x_2$, cada uno conectado a los tres nodos ocultos $h_1$, $h_2$, $h_3$ (conexiones cruzadas completas), y estos conectados a un único nodo de salida $y$.

## Slide 31

# Dos entradas

**Figura:** Seis paneles en cuadrícula 2x3, cada uno con ejes Input, $x_2$ (vertical) e Input, $x_1$ (horizontal), rango -1.0 a 1.0, representados como mapas de calor con líneas diagonales de contorno:
- a) $\theta_{10}+\theta_{11}x_1+\theta_{12}x_2$: gradiente diagonal de oscuro (esquina superior izquierda) a claro (esquina inferior derecha... realmente claro en esquina superior derecha), con líneas de contorno paralelas diagonales.
- b) $\theta_{20}+\theta_{21}x_1+\theta_{22}x_2$: gradiente muy oscuro en la izquierda que se aclara hacia la derecha, líneas de contorno casi verticales.
- c) $\theta_{30}+\theta_{31}x_1+\theta_{32}x_2$: gradiente oscuro arriba-izquierda a claro abajo-derecha, líneas de contorno diagonales en sentido opuesto a (a).
- d) $h_1=\text{a}[\theta_{10}+\theta_{11}x_1+\theta_{12}x_2]$: mismo patrón que (a) pero con una línea verde agua marcando el límite de activación (recta diagonal de esquina superior izquierda a esquina inferior derecha).
- e) $h_2=\text{a}[\theta_{20}+\theta_{21}x_1+\theta_{22}x_2]$: región izquierda uniforme (activación 0), región derecha con gradiente, separadas por una línea verde agua casi vertical.
- f) $h_3=\text{a}[\theta_{30}+\theta_{31}x_1+\theta_{32}x_2]$: gradiente diagonal con línea verde agua recta que cruza de izquierda (centro) a esquina superior derecha.

## Slide 32

# Dos entradas

**Figura:** Seis paneles en cuadrícula 2x3, ejes Input, $x_2$ (vertical) e implícito Input, $x_1$ (horizontal), rango -1.0 a 1.0:
- d) $h_1=\text{a}[\theta_{10}+\theta_{11}x_1+\theta_{12}x_2]$: repetición del panel d) de la slide anterior, con línea verde agua diagonal.
- e) $h_2=\text{a}[\theta_{20}+\theta_{21}x_1+\theta_{22}x_2]$: repetición del panel e), línea verde agua casi vertical.
- f) $h_3=\text{a}[\theta_{30}+\theta_{31}x_1+\theta_{32}x_2]$: repetición del panel f), línea verde agua diagonal.
- g) $\phi_1h_1$: patrón similar a d) pero con tonos más oscuros (ponderado por $\phi_1$), línea verde agua diagonal.
- h) $\phi_2h_2$: patrón similar a e), región izquierda uniforme y derecha con gradiente claro, línea verde agua casi vertical.
- i) $\phi_3h_3$: patrón similar a f) ponderado, línea verde agua diagonal.

## Slide 33

# Dos entradas

**Figura:** Tres paneles superiores g), h), i) (idénticos a los de la slide anterior: $\phi_1h_1$, $\phi_2h_2$, $\phi_3h_3$, cada uno con eje Input, $x_1$ e Input, $x_2$ de -1.0 a 1.0 y su línea verde agua de frontera) y un panel inferior j) etiquetado $y=\phi_0+\phi_1h_1+\phi_2h_2+\phi_3h_3$: mapa de calor 2D con tres líneas verde agua rectas que se cruzan dividiendo el plano en varias regiones poligonales convexas, con gradiente de color de oscuro (rojo/marrón) a claro (crema) según la región. Al costado, texto destacado en naranja: "Polígonos convexos".

## Slide 34

# 3.

# Generalización

*Inputs arbitrarios*

**Figura:** Imagen decorativa de fondo — mano robótica señalando una representación abstracta de un cerebro/red digital sobre fondo azul oscuro, con marcas de medición punteadas en amarillo y celeste (misma imagen que la slide del teorema del aproximador universal).

## Slide 35

# Inputs, hidden units y outputs arbitrarios

- $D_o$ Outputs, $D$ hidden units, and $D_i$ inputs

$y_j = \phi_{j0} + \sum_{d=1}^{D} \phi_{jd}h_d,$

- e.g., Three inputs, three hidden units, two outputs

**Figura:** Diagrama de red neuronal: tres nodos de entrada $x_1$, $x_2$, $x_3$, cada uno conectado a los tres nodos ocultos $h_1$, $h_2$, $h_3$ (conexiones cruzadas completas), y estos conectados a dos nodos de salida $y_1$ e $y_2$.

## Slide 36

# ¿Pregunta?

¿Cuántos parámetros tiene este modelo?

**Figura:** Diagrama de red neuronal: tres nodos de entrada $x_1$, $x_2$, $x_3$, cada uno conectado a los tres nodos ocultos $h_1$, $h_2$, $h_3$ (conexiones cruzadas completas), y estos conectados a dos nodos de salida $y_1$ e $y_2$ (mismo diagrama que la slide anterior).

## Slide 37

# Question?

How many parameters does this model have?

**Figura:** Diagrama de flujo: un bloque rectangular etiquetado "Input" con tres flechas de salida hacia tres mapas de calor 2D apilados verticalmente (cada uno con patrones de contorno diagonales distintos, similares a los paneles a), b), c) de "Dos entradas"), y estos tres mapas convergen mediante llaves hacia un único mapa de calor final etiquetado con ejes "Input 2" (vertical) e "Input 1" (horizontal), que muestra una combinación de las regiones con múltiples líneas de contorno y una frontera curva en forma de "V" o estrella.

## Slide 38

**Figura:** Dos paneles. Izquierda: mapa de calor 2D etiquetado $y=\phi_0+\phi_1h_1+\phi_2h_2+\phi_3h_3$, con ejes Input, $x_1$ e Input, $x_2$ de -1.0 a 1.0, mostrando tres líneas verde agua que se cruzan formando regiones poligonales convexas con gradiente de color. Derecha: gráfico de superficie 3D con ejes "Output" (vertical), "Input 2" e "Input 1", mostrando una superficie plegada en facetas planas (forma de "techo a varias aguas"), con líneas verde agua marcando las aristas entre facetas, correspondiente a la función lineal a trozos del panel izquierdo llevada a 3D.

## Slide 39

**Figura:** Dos elementos. Izquierda: mismo diagrama de flujo de la slide 37 — bloque "Input" con tres flechas hacia tres mapas de calor apilados, que convergen hacia un mapa combinado con ejes "Input 2" e "Input 1". Derecha: diagrama de red neuronal con dos nodos de entrada $x_1$, $x_2$ conectados a tres nodos ocultos $h_1$, $h_2$, $h_3$, y estos conectados a un nodo de salida $y$, con la etiqueta "neural network" debajo, seguido de las ecuaciones:

$y = \phi_0 + \phi_1 h_1 + \phi_2 h_2 + \phi_3 h_3$

$h_1 = \text{a}[\theta_{10} + \theta_{11}x_1 + \theta_{12}x_2]$
$h_2 = \text{a}[\theta_{20} + \theta_{21}x_1 + \theta_{22}x_2]$
$h_3 = \text{a}[\theta_{30} + \theta_{31}x_1 + \theta_{32}x_2]$

## Slide 40

# Número de regiones de salida

En general, cada salida consiste en politopos convexos de dimensión D.

Con dos entradas y tres salidas, vimos que había siete polígonos:

**Figura:** Mapa de calor 2D etiquetado $y=\phi_0+\phi_1h_1+\phi_2h_2+\phi_3h_3$, con ejes Input, $x_1$ e Input, $x_2$ de -1.0 a 1.0. Tres líneas verde agua rectas se cruzan dividiendo el plano en siete regiones poligonales convexas, cada una con un gradiente de color diferente (tonos de rojo/marrón a crema) según líneas de contorno diagonales dentro de cada región.

## Slide 41

# Número de regiones de salida

En general, cada salida consiste en politopos convexos de dimensión D.

¿Cuántos?

**Figura:** Dos gráficos lado a lado (a y b), ambos con eje vertical "Number of regions" en escala logarítmica de $10^0$ a $10^{150}$.
- Gráfico a): eje horizontal "Number of hidden units" de 0 a 1000. Se muestran cinco curvas crecientes etiquetadas $D_i=100$, $D_i=50$, $D_i=10$, $D_i=5$, $D_i=1$ (de mayor a menor crecimiento). La curva $D_i=100$ alcanza cerca de $10^{130}$ en x=1000; hay un punto marcado sobre la curva $D_i=100$ en x≈500 cercano a $10^{100}$.
- Gráfico b): eje horizontal "Number of parameters" de 0 a 100000. Mismas cinco curvas ($D_i=100$, $D_i=50$, $D_i=10$, $D_i=5$, $D_i=1$), con comportamiento similar: $D_i=100$ crece más rápido al inicio y domina; $D_i=50$ queda por debajo; $D_i=10$, $D_i=5$, $D_i=1$ casi planas cerca de la parte inferior. Punto marcado sobre la curva $D_i=100$ en x≈50000 cercano a $10^{100}$.

## Slide 42

# Demostración de que hay más regiones que 2^D

**Figura:** Tres diagramas (a, b, c) que ilustran cómo el número de regiones lineales supera $2^D$ a medida que aumenta la dimensión de entrada y el número de unidades ocultas.
- a) Espacio 1D con eje $x_1$: una franja vertical resaltada sobre la recta, con un punto en el origen. Leyenda: "1D input with 1 hidden unit creates two regions (one joint)".
- b) Espacio 2D con ejes $x_1$ (horizontal, color naranja) y $x_2$ (vertical, color verde/turquesa), cruzándose en el origen formando una cruz. Leyenda: "2D input with 2 hidden units creates four regions (two lines)".
- c) Espacio 3D con ejes $x_1$, $x_2$, $x_3$: se muestran tres planos que se intersecan en el origen (un plano gris horizontal, un plano turquesa vertical, un plano naranja horizontal rotado), con una flecha punteada diagonal indicando una dirección. Leyenda: "3D input with 3 hidden units creates eight regions (three planes)".

## Slide 43

# Terminología

**Figura:** Diagrama de una red neuronal feedforward con tres capas.
- "Input layer": tres nodos circulares etiquetados $x_1$, $x_2$, $x_3$.
- "Hidden layer" (nodos en color marrón/óxido): cuatro nodos etiquetados $h_1$, $h_2$, $h_3$, $h_4$, cada uno conectado a todos los nodos de entrada mediante flechas (conexión totalmente conectada).
- "Output layer": dos nodos etiquetados $y_1$, $y_2$, cada uno conectado a todos los nodos de la capa oculta.
- Una flecha punteada azul señala una de las conexiones input→hidden con la etiqueta "Weight".
- Una flecha punteada marrón señala el nodo $h_4$ con la etiqueta "Neuron or hidden unit".

## Slide 44

# Funciones de activación

**Figura:** Rejilla de seis gráficos (a–f), todos con eje horizontal $z$ de -4.0 a 4.0 y eje vertical $a[z]$ de -2.0 a 2.0, mostrando distintas funciones de activación:
- a) Curvas $\text{sig}[z]$ (naranja, forma sigmoide acotada entre 0 y 1) y $\tanh[z]$ (turquesa, forma sigmoide acotada entre -1 y 1, más pronunciada cerca de z=0).
- b) Curvas $\text{LReLU}[z]$ (turquesa, pendiente pequeña negativa para z<0, pendiente 1 para z>0) y $\text{PReLU}[z, 0.25]$ (naranja, pendiente 0.25 para z<0, pendiente 1 para z>0).
- c) Curvas $\text{softplus}[z]$ (verde oscuro, suave y creciente, siempre positiva), $\text{GeLU}[z]$ (naranja) y $\text{SiLU}[z]$ (turquesa), las tres con una leve caída bajo cero para z negativo antes de crecer para z positivo.
- d) Curvas $\text{ELU}[z, 0.5]$ (turquesa) y $\text{ELU}[z, 1.0]$ (naranja): ambas planas/negativas saturando para z<0 y lineales (pendiente 1) para z>0, con distinta saturación negativa según el parámetro.
- e) Curva $\text{SELU}[z]$ (naranja): similar a ELU, satura en valores negativos para z<0 y crece linealmente (con mayor pendiente) para z>0.
- f) Curvas $\text{swish}[z, 1.4]$ (verde oscuro), $\text{swish}[z, 1.0]$ (turquesa punteada) y $\text{swish}[z, 0.4]$ (turquesa claro): todas con un mínimo leve bajo cero cerca de z negativo antes de crecer para z positivo, variando la profundidad y posición del mínimo según el parámetro.

## Slide 45

# Final Takeaways

1. Gracias al Teorema del Aproximador Universal, incluso redes simples son potentes aproximadores.

2. Las redes profundas pueden crear muchas más regiones lineales con relativamente pocos parámetros.

3. Funciones como ReLU, sigmoide y tanh definen cómo se transforma la información capa a capa.

4. La salida se obtiene mediante combinaciones lineales sucesivas y funciones de activación

## Slide 46

**Figura:** Fotografía de portada/cierre con superposición de color azul: dos estudiantes con guardapolvo blanco y lentes de protección observando un dispositivo mecánico con múltiples brazos/rieles metálicos en un laboratorio. Sin texto adicional de contenido (solo logos institucionales).
