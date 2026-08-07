---
curso: IO1
titulo: Semana10-Capitulo4A
slides: 47
fuente: Semana10-Capitulo4A.pdf
---

## Slide 1

Portada del capítulo. Título "Investigación de operaciones I", subtítulo "Capítulo 4: Programación Lineal". Logo UTEC (decorativa).

## Slide 2

**Objetivos del capítulo**
- Presentar de manera intuitiva los fundamentos teóricos de la programación lineal.
- Resolver problemas lineales de optimización con el método simplex.
- Presentar aspectos teóricos y prácticos de la dualidad.

## Slide 3

Slide separador: "Parte 1: Aspectos teóricos de la programación lineal" (título grande, sin más contenido).

## Slide 4

**La colección de combinaciones**. Lista de 4 items, cada uno con la palabra clave resaltada en azul:
- Combinaciones **lineales**
- Combinaciones **afines**
- Combinaciones **cónicas**
- Combinaciones **convexas**

## Slide 5

**Combinaciones lineales**

Nos damos:
- un espacio vectorial $E$, por ejemplo $\mathbb{R}^n$.
- un conjunto $x_1,\dots,x_m$ de vectores de $E$.
- un conjunto $\alpha_1,\dots,\alpha_m$ de escalares en $\mathbb{R}$.

Llamamos:
$$\alpha_1 x_1 + \dots + \alpha_m x_m$$
una **combinación lineal** de los vectores $x_1,\dots,x_m$.

## Slide 6

**Combinaciones afines**

Una combinación lineal $\alpha_1 x_1 + \dots + \alpha_m x_m$ de vectores $x_1,\dots,x_m$ se llama **combinación afín** si
$$\sum_{i=1}^{m}\alpha_i = 1.$$

## Slide 7

**Combinaciones cónicas**

Una combinación lineal $\alpha_1 x_1 + \dots + \alpha_m x_m$ de vectores $x_1,\dots,x_m$ se llama **combinación cónica** si
$$\alpha_i \ge 0,\ \forall i \in \{1,\dots,m\}.$$

## Slide 8

**Combinaciones convexas**

Una combinación lineal $\alpha_1 x_1 + \dots + \alpha_m x_m$ de vectores $x_1,\dots,x_m$ se llama **combinación convexa** si
$$\sum_{i=1}^{m}\alpha_i = 1 \quad \text{y} \quad \alpha_i \ge 0,\ \forall i \in \{1,\dots,m\}.$$

## Slide 9

**Conjunto convexo (espacio convexo)**

$X \subseteq \mathbb{R}^n$ es convexo si y sólo si para cualquier par de vectores $x_1, x_2 \in X$ tenemos $\alpha x_1 + (1-\alpha)x_2 \in X$ para todo $\alpha \in [0,1]$.

Dicho de otra manera:
- Un espacio $X$ es convexo si para cualquier par de puntos $A$ y $B$ de $X$, el segmento $[A,B]$ está incluido en $X$.
- Un espacio $X$ es convexo si todas las combinaciones convexas de cualquier conjunto de puntos de $X$ pertenecen a $X$.

## Slide 10

**Pregunta**: ¿La combinación convexa de un número finito de elementos de un conjunto convexo $S$ pertenece siempre a $S$? (solo texto, pregunta retórica sin respuesta visible en la slide).

## Slide 11

**Identifica los objetos convexos:** — grid de 7 figuras geométricas en dos filas para que el alumno identifique cuáles son convexas:

Fila superior (2D):
- Una figura azul en forma de "cruz/Tetris" (forma de T con muescas) — claramente NO convexa (tiene entrantes).
- Un pentágono azul regular — convexo.
- Un anillo/dona azul (círculo con hueco en el centro) — NO convexo.

Fila inferior (sólidos 3D coloreados, estilo poliedro):
- Un toroide multicolor (forma de dona con caras de colores: rosa, verde, celeste, magenta) — NO convexo.
- Una estrella roja de 6 puntas (estrella de David 3D, tipo "estrellado") — NO convexa.
- Un poliedro rojo/amarillo tipo icosidodecaedro con muescas (forma dentada) — NO convexo.
- Un tetraedro rojo simple — convexo.

## Slide 12

**¿El conjunto de puntos (en azul) es convexo?** Gráfico de cuadrícula (ejes 0 a 5+) con puntos azules dispuestos en un patrón tipo "L" o escalonado: fila inferior con 4 puntos (x=0,1,2,3, y=0), segunda fila con 4 puntos (x=0,1,2,3, y=1), luego el patrón se estrecha hacia arriba y a la derecha formando una especie de escalera irregular con puntos en (2,3),(3,3),(4,3), (2,4),(3,4), (2,5),(3,5), (1,2). El conjunto de puntos discretos NO es convexo (hay huecos entre los puntos, no es una región continua, y la forma tiene entrantes).

## Slide 13

Misma pregunta y mismo gráfico de puntos azules que la slide 12 (idéntica cuadrícula y disposición de puntos), repetida — probablemente para dar tiempo a discusión antes de mostrar la envolvente convexa en slides posteriores.

## Slide 14

**Envolvente convexa (envoltura convexa)**

La envolvente convexa de $X \subseteq \mathbb{R}^n$, denotada $\mathrm{conv}(X)$, es el conjunto de todas las combinaciones convexas de $X$.

## Slide 15

**¿Identifica la envolvente convexa de los puntos en azul?** Mismo gráfico de puntos azules de las slides 12-13 (misma cuadrícula, mismo patrón escalonado), planteando la pregunta de cuál sería el polígono envolvente.

## Slide 16

Repetición del mismo gráfico/pregunta que la slide 15 (mismos puntos azules), aparentemente para pausa didáctica antes de revelar la solución.

## Slide 17

**Envolvente convexa:** Se muestra el mismo conjunto de puntos azules de las slides anteriores, pero ahora con la región de la envolvente convexa sombreada en gris y su contorno dibujado con línea gruesa gris — un polígono irregular que conecta los puntos extremos (aproximadamente los puntos en (0,0),(0,1),(1,2),(2,3),(3,3),(4,2),(4,1),(3,0),(1,0)) formando el borde de la envolvente, dejando los puntos interiores dentro de la región sombreada.

## Slide 18

**Intersección de conjuntos convexos**

Resultado importante: La intersección de conjuntos convexos es un conjunto convexo o un conjunto vacío.

## Slide 19

**Hiperplano**
- Definición wikipedia: Un hiperplano es un análogo de muchas dimensiones al plano (de dos dimensiones) en el espacio tridimensional.
- ¿Cómo representar matemáticamente un hiperplano en dimensión $n$?

## Slide 20

**Hiperplano**

Un hiperplano es un conjunto de puntos $\{x \mid \alpha_1 x_1 + \cdots + \alpha_n x_n = b\}$ en $\mathbb{R}^n$ donde $\alpha$ es un vector no nulo.

## Slide 21

**Semiespacio (cerrado)**
- Definición wikipedia: Cada una de las dos partes en que un espacio queda dividido por un (hiper)plano contenido en él.
- ¿Cómo representar matemáticamente un semiespacio en dimensión $n$?

## Slide 22

**Semiespacio**

Un semiespacio es un conjunto de puntos $\{x \mid \alpha_1 x_1 + \cdots + \alpha_n x_n \le b\}$ en $\mathbb{R}^n$ donde $\alpha$ es un vector no nulo.

## Slide 23

**Pregunta**: ¿Un semiespacio es convexo? (solo texto).

## Slide 24

**Pregunta**: ¿Un hiperplano es convexo? (solo texto).

## Slide 25

**Poliedros convexos y politopos convexos**
- La intersección de un número finito de semiespacios es un **poliedro convexo**.
- Un poliedro convexo acotado es un **politopo convexo**.

## Slide 26

**Pregunta**: ¿La región factible de un programa lineal es convexa? (solo texto).

## Slide 27

**Puntos extremos**
- Un punto $x$ de un conjunto convexo $P$ es un punto extremo si no se puede escribir como combinación convexa de otros dos puntos de $P$.
- Matemáticamente: $x \in P$ es un punto extremo si no existen dos puntos $x_1 \neq x$ y $x_2 \neq x$ de $P$ distintos de $x$ y un escalar $\alpha \in [0,1]$ tal que $x = \alpha x_1 + (1-\alpha)x_2$.

## Slide 28

**¿Puntos extremos?** Diagrama: un pentágono verde claro (convexo) con 3 puntos marcados dentro/sobre la figura: $x_1$ está sobre un vértice inferior izquierdo del pentágono (punto extremo), $x_2$ está en el interior del pentágono (no es punto extremo), $x_3$ está sobre otro vértice superior del pentágono (punto extremo). Ilustra la diferencia entre puntos extremos (vértices) y puntos interiores.

## Slide 29

**¿Puntos extremos?** Diagrama: un círculo/óvalo verde claro sin ningún punto marcado — ilustra que en un círculo (conjunto convexo con frontera curva) cada punto de la frontera es un punto extremo (a diferencia del polígono de la slide anterior donde solo los vértices lo son).

## Slide 30

**Politopos convexos y puntos extremos**

Cada punto de un politopo convexo es combinación convexa de sus puntos extremos.

Gráfico: sistema de ejes (0 a 4 en x, 0 a 2 en y) con una región sombreada en naranja (forma tipo trapecio irregular con un pico) delimitada por puntos extremos azules en (0,0), (1,2) y (3,1) aproximadamente, y el borde continúa hasta (4,0). Dentro de la región hay un punto rojo (interior, en aprox (1,1)) conectado por líneas negras a los puntos extremos azules (0,0), (1,2) y (3,1), mostrando visualmente que el punto rojo interior es combinación convexa de los puntos extremos azules.

## Slide 31

**Puntos extremos y programación lineal**

Si todas las variables son no-negativas y si la región factible es no vacía, entonces existe un punto extremo.

## Slide 32

**Puntos extremos y programación lineal**

Si una solución óptima existe, entonces existe un punto extremo óptimo.

## Slide 33

**Puntos extremos y programación lineal**

Si un programa lineal tiene una única solución óptima, esa solución es un punto extremo.

## Slide 34

**Puntos extremos y programación lineal**

Si un programa lineal tiene una infinidad de soluciones óptimas, todas esas soluciones son combinaciones convexas de puntos extremos óptimos.

## Slide 35

**Puntos extremos y programación lineal**
1. Si un programa lineal tiene una solución óptima, al menos un punto extremo corresponde a una solución óptima.
2. Podríamos identificar todos los puntos extremos resolviendo todas las combinaciones de sistemas de $n$ ecuaciones (hiperplanos) con $n$ variables.
3. Si la solución de un sistema de ecuaciones corresponde a una solución factible, es un punto extremo.

## Slide 36

**Número de puntos extremos potenciales: Explosión combinatoria**
1. En un programa lineal con $n$ variables y $m$ restricciones, existen $m+n$ **restricciones** incluyendo las restricciones de no-negatividad.
2. $m+n$ restricciones son $m+n$ hiperplanos.
3. En dimensión $n$ un punto corresponde a la intersección de $n$ hiperplanos linealmente independientes.
4. ¿De cuántas maneras podemos seleccionar $n$ hiperplanos entre $m+n$?

Número potencial de puntos extremos: $\dfrac{(m+n)!}{m!\,n!}$

## Slide 37

**Puntos extremos y programación lineal**

Si la solución de un programa lineal que corresponde a un punto extremo es mejor que las soluciones que corresponden a sus puntos extremos **adyacentes**, entonces es una solución **óptima**.

## Slide 38

Slide separador: "Método Simplex" (título grande, sin más contenido).

## Slide 39

**Historia de la programación lineal**
- En el fin del siglo XVIII Fourier inventó un método para resolver sistemas de inecuaciones, conocido ahora como el método de eliminación de Fourier-Motzkin. Ese método es bastante ineficiente.
- En 1930, Kantorovich y Koopmans (Premio Nobel de Economía, 1975) muestran que la programación lineal tiene un gran potencial práctico, en particular para resolver problemas de alocación de recursos.

## Slide 40

**Historia de la programación lineal**
- En 1947, George Dantzig inventó el primer algoritmo práctico para resolver programas lineales: el **método Simplex**.
- En 1979, Khachiyan demuestra que se puede resolver programas lineales en **tiempo polinomial** con el método elipsoidal. Es una ruptura teórica, pero en práctica el algoritmo es lento.
- En 1984, Karmarkar propone otro método en tiempo polinomial, el método del punto interior, eficiente también en práctica.

## Slide 41

**Explicación intuitiva del método simplex**
- Se inicia el algoritmo en cualquier punto extremo.
- A cada iteración, consideramos los puntos adyacentes del punto actual y seleccionamos uno que mejora la solución actual.
- Iterar hasta que ningún punto adyacente mejore la solución actual.

## Slide 42

**Explicación intuitiva del método simplex** — Diagrama: un poliedro esférico tipo "balón de fútbol" (esfera facetada en polígonos, coloreada con un degradado de tonos púrpura/marrón en la parte inferior a crema/amarillo en la parte superior), simulando la superficie de un politopo de alta dimensión. Se dibuja un plano semitransparente celeste que corta la esfera cerca de la parte superior (representando el hiperplano de la función objetivo). Un camino de puntos azules conectados por flechas punteadas azules recorre la superficie de la esfera desde un punto rojo etiquetado "start!" (abajo a la izquierda) subiendo a través de varios vértices intermedios hasta llegar a un punto rojo etiquetado "stop!" (arriba, sobre el plano celeste) — ilustra visualmente cómo el simplex recorre vértices adyacentes del politopo hasta alcanzar el óptimo.

## Slide 43

**¿Qué tiene que ver la convexidad con eso?** (slide de transición, solo texto, pregunta retórica).

## Slide 44

**Método simplex y convexidad** — Diagrama: un polígono convexo (heptágono irregular) con relleno en degradado verde (más oscuro/saturado arriba a la derecha, más claro abajo a la izquierda). Sobre el borde del polígono se traza un camino en azul grueso desde un vértice inferior (punto azul, esquina inferior izquierda) siguiendo el contorno hacia la derecha y arriba hasta un vértice superior derecho marcado con un punto naranja/rojo, con una flecha azul indicando la dirección de avance hacia ese punto. Una línea roja diagonal (recta) atraviesa el polígono con un vector rojo (flecha) perpendicular a ella indicando la dirección de crecimiento de la función objetivo; una línea discontinua roja paralela pasa tangente por el vértice naranja, representando la curva/recta de nivel óptima que toca el polígono exactamente en ese vértice extremo.

## Slide 45

**Método simplex y convexidad** — Diagrama similar al de la slide 44 pero con un polígono de forma distinta (tipo "V" o flecha, con una muesca cóncava marcada, en degradado verde). El camino azul recorre el contorno desde un vértice inferior izquierdo (punto azul) hasta un vértice superior (punto naranja) siguiendo el borde superior de la figura, con flecha azul en la punta indicando la dirección. Igual que antes, aparece la línea roja diagonal con su vector perpendicular y la recta discontinua roja tangente en el punto óptimo naranja.

## Slide 46

**Método de puntos interiores y convexidad** — Diagrama: un polígono convexo (octágono irregular, degradado verde) con un punto azul en el interior (no en el borde) conectado por una flecha/curva azul gruesa que atraviesa el interior de la figura (no bordea el contorno como en el método simplex) hasta llegar a un punto naranja cerca del borde superior derecho. Se mantiene la línea roja diagonal con su vector perpendicular indicando la dirección de la función objetivo y la recta roja discontinua tangente en el punto óptimo — contrasta visualmente con las slides 44-45: el método de punto interior atraviesa el interior del politopo en vez de recorrer su frontera.

## Slide 47

**Método de puntos interiores y convexidad** — Mismo tipo de diagrama que la slide 46 pero sobre la figura tipo "V"/cóncava de la slide 45 (degradado verde, forma con muesca). Un punto azul en el interior conectado por una trayectoria azul curva que atraviesa el interior de la figura hasta un punto naranja cerca del vértice superior, nuevamente con la línea roja diagonal, su vector perpendicular y la recta discontinua roja tangente en el óptimo — refuerza la comparación entre método simplex (bordea el contorno) y método de punto interior (atraviesa el interior) en dos formas distintas de politopo.
