---
curso: IO1
titulo: Semana11-Capitulo4B
slides: 43
fuente: Semana11-Capitulo4B.pdf
---

## Slide 1

Portada del capítulo. Título "Investigación de operaciones 1" y subtítulo "Algoritmo Simplex". Imagen decorativa: un poliedro 3D (icosaedro truncado tipo "fulereno") en verdes y ocres, con una arista resaltada en rojo grueso que recorre varias caras — probablemente una alusión visual a una trayectoria/camino sobre las caras/vértices de un poliedro, anticipando el tema del método simplex como recorrido por vértices de un politopo. Logo UTEC abajo a la izquierda.

## Slide 2

Título "Método Simplex". Ilustración decorativa: personaje de cómic (Linus de Peanuts, con su mantita) sentado, con el texto "HAPPINESS IS ASSUMING THE WORLD IS LINEAR" (chiste sobre programación lineal). Sin contenido técnico adicional.

## Slide 3

Título "Método simplex". Lista de viñetas sobre el método:
- Inventado por George Dantzig en 1947
- Todavía el método más utilizado en programación lineal
- Permite saber si un programa lineal es factible o no
- Permite encontrar una solución óptima si existe
- Demuestra que un programa lineal no es acotado cuando no lo es
- SUPER RAPIDO! (en negrita)

Imagen: fotografía en blanco y negro de George Dantzig superpuesta sobre una pizarra con fórmulas matemáticas de fondo (decorativa, ilustra al autor del método).

## Slide 4

Título "Método simplex: idea intuitiva". Tres viñetas:
- Se inicia el algoritmo en cualquier punto extremo.
- A cada iteración, consideramos los puntos adyacentes del punto actual y seleccionamos uno que mejora la solución actual.
- Iterar hasta que ningún punto adyacente mejore la solución actual.

Slide de solo texto (sin figura).

## Slide 5

Gráfico 2D: región factible poligonal ("Espacio de soluciones", sombreada en gris) con vértices etiquetados A, B, C, D, E, F, en el plano x1-x2, delimitada por varias rectas (incluida la recta horizontal x2 ≤ 2 marcada como restricción "(4)"). Se muestra la recta de nivel "Max" (roja) desplazándose en paralelo (líneas rojas punteadas) en la dirección del gradiente de maximización. Flechas azules trazan una trayectoria de vértices: A (etiquetado "start!") → B → C → D (etiquetado "stop!"), siguiendo el borde del polígono, ilustrando cómo el simplex recorre vértices adyacentes maximizando z hasta detenerse en el óptimo. Título "Espacio factible del modelo de Reddy Mikks" (referencia al modelo clásico de pinturas Reddy Mikks). Etiqueta "FIGURA 2.1".

## Slide 6

Imagen 3D: el mismo poliedro tipo fulereno de la slide 1 (esfera facetada multicolor), ahora con un plano de corte semitransparente y una trayectoria punteada azul de puntos (vértices) que va de un punto rojo etiquetado "start!" (abajo) a otro punto rojo etiquetado "stop!" (arriba), pasando por varios vértices intermedios en azul — analogía tridimensional del recorrido del método simplex sobre los vértices de un politopo de mayor dimensión.

## Slide 7

Título "Primera etapa: forma estándar" (manuscrito en rojo). Formulación general de un programa lineal:

```
max    c1 x1 + c2 x2 + ··· + cn xn
s.t.   a11 x1 + a12 x2 + ··· + a1n xn ≤ b1
       a21 x1 + a22 x2 + ··· + a2n xn ≤ b2
       ⋮
       am1 x1 + am2 x2 + ··· + amn xn ≤ bm
       x1, x2, ..., xn ≥ 0
```

Anotaciones manuscritas en rojo: llave a la derecha de las restricciones ≤ etiquetada "desigualdades"; llave bajo x1,...,xn ≥ 0 etiquetada "no-negatividad".

## Slide 8

Título "Segunda etapa: forma canónica". Muestra la transformación de una desigualdad a igualdad mediante variable de holgura:

$$a_1x_1 + a_2x_2 + \cdots + a_nx_n \le b$$

flecha azul hacia abajo →

$$a_1x_1 + a_2x_2 + \cdots + a_nx_n + s = b, \quad s \ge 0$$

con anotación roja señalando "s" como "variable de holgura (slack variable)".

## Slide 9

Título "Modelo completo". Presenta el modelo de ejemplo (Reddy Mikks simplificado a 2 variables) en forma estándar:

```
maximizar z = 5x1 + 4x2
s.t.       6x1 + 4x2 ≤ 24
            x1 + 2x2 ≤ 6
           -x1 +  x2 ≤ 1
                  x2 ≤ 2
              x1, x2 ≥ 0
```

Slide de solo texto matemático, sin gráfico.

## Slide 10

Dos recuadros mostrando la introducción de variables de holgura al modelo de la slide 9:
- Recuadro superior izquierdo: el mismo sistema con desigualdades (≤), corchete rojo "desigualdades" a la derecha.
- Flecha azul (etiquetada "introducción de variables de holgura") hacia recuadro inferior izquierdo: sistema con igualdades tras añadir s1, s2, s3, s4: 6x1+4x2+s1=24, x1+2x2+s2=6, -x1+x2+s3=1, x2+s4=2, con x1,x2,s1,s2,s3,s4≥0. Corchete rojo "igualdades".
- Flecha azul hacia recuadro derecho: sistema despejado para las variables de holgura (diccionario):
  s1 = 24 − 6x1 − 4x2
  s2 = 6 − x1 − 2x2
  s3 = 1 + x1 − x2
  s4 = 2 − x2
  z = 5x1 + 4x2
  Etiquetado "reescritura del problema como un sistema de ecuaciones".

Texto manuscrito rojo arriba a la derecha explica la equivalencia de soluciones óptimas entre la formulación con y sin variables de holgura: "Si (x1,x2,s1,s2,s3,s4) es una solución óptima, (x1,x2) es también una solución óptima" y viceversa.

## Slide 11

Recuadro con el diccionario inicial (mismo de la slide 10):
s1 = 24 − 6x1 − 4x2, s2 = 6 − x1 − 2x2, s3 = 1 + x1 − x2, s4 = 2 − x2, z = 5x1 + 4x2.

Anotaciones manuscritas rojas debajo:
- "Aumentar x1 de 1 aumenta z de 5"
- "Aumentar x2 de 1 aumenta z de 4"

Texto rojo a la derecha: "(0,0,24,6,1,2) es una solución (no óptima), es una solución factible"; "Intentamos aumentar x1 sin que ninguna variable de holgura sea negativa. ¿De cuánto podemos aumentar x1?"; flecha azul hacia abajo con el resultado: x1 = min(24/6, 6/1) = 4.

## Slide 12

Recuadro izquierdo: mismo diccionario inicial (s1..s4, z). Flecha roja hacia arriba a una fórmula despejada: x1 = 4 − (2/3)x2 − (1/6)s1.

Gráfico central: el mismo polígono "Espacio de soluciones" con vértices A,B,C,D,E,F (0 a 4 en x1, 0 a 2 en x2), con una flecha roja horizontal gruesa desde A hasta B (recorrido sobre el eje x1) marcando el movimiento del punto factible desde el origen A hacia B.

Anotaciones rojas: "(0,0,24,6,1,2) es una solución (no óptima)"; "x1 = min(24/6, 6/1) = 4"; "si aumentamos de 4, la primera variable de holgura se anula"; "la nueva solución es (4,0,0,2,5,2)".

Recuadro derecho: sistema reescrito tras el pivote (x1 entra, s1 sale):
x1 = 4 − (2/3)x2 − (1/6)s1
s2 = 2 − (4/3)x2 + (1/6)s1
s3 = 5 − (5/3)x2 − (1/6)s1
s4 = 2 − x2
z = 20 + (2/3)x2 − (5/6)s1
Texto: "por substitución, el sistema se reescribe:".

## Slide 13

Recuadro izquierdo: el diccionario resultante del pivote anterior (x1, s2, s3, s4, z en función de x2, s1). Flecha roja hacia una fórmula despejada: x2 = 3/2 + (1/8)s1 − (3/4)s2.

Gráfico derecho: mismo polígono con flecha roja desde B hacia C, marcando el nuevo movimiento (segunda iteración) del punto factible.

Anotaciones rojas: "Intentamos aumentar x2"; "podemos aumentar x2 de 1.5 (¿porqué?)"; "la nueva solución es (3, 1.5, 0, 0, 2.5, 0.5)".

Recuadro inferior derecho: sistema tras el segundo pivote (x2 entra, s2 sale):
x1 = 3 − (1/4)s1 + (1/2)s2
x2 = 3/2 + (1/8)s1 − (3/4)s2
s3 = 5/2 − (3/8)s1 + (5/4)s2
s4 = 1/2 − (1/8)s1 + (3/4)s2
z = 21 − (3/4)s1 − (1/2)s2

## Slide 14

Recuadro izquierdo: mismo diccionario de la slide 13 tras el segundo pivote. Texto rojo debajo: "Intentamos aumentar x2, podemos aumentar x2 de 1.5 (¿porqué?)".

Gráfico derecho: polígono con punto C resaltado (flecha roja apuntando a C desde el borde, entre D y B). Texto: "la nueva solución es (3, 1.5, 0, 0, 2.5, 0.5)".

Recuadro inferior derecho: mismo sistema final (idéntico al mostrado al final de la slide 13). Texto rojo grande: "Todos los coeficientes de la variables de holgura en z son negativos -> TERMINADO!" — indica que se alcanzó la condición de optimalidad (criterio de parada del simplex).

## Slide 15

Título implícito "Variable de salida <–> Variable de entrada". Gráfico del polígono con las tres soluciones básicas encontradas marcadas:
- Solución básica 1: (0,0,24,6,1,2) en el vértice A — "x1 entra en la base, s1 sale de la base"
- Solución básica 2: (4,0,0,2,5,2) en el vértice B
- Solución básica 3: (3,1.5,0,0,2.5,0.5) en el vértice C — marcada "óptima!"

Texto derecho: "Para pasar de una solución básica a otra solución básica se necesita un intercambio entre variables básicas y variables no básicas"; preguntas "¿cuál variable entra en la base? ¿cuál sale de la base?". Resume visualmente las 3 iteraciones del ejemplo anterior sobre el mismo polígono.

## Slide 16

Diagrama 3D: un cubo/politopo en ejes x1, x2, x3 con vértices etiquetados A, B, C, D, E, F, G, H, I, J (A=(0,0,0), B=(1,0,0), C=(0,1,0), D=(0,0,1), y otros vértices truncados F, G, H, I, J formando un poliedro más complejo con caras cortadas). Aristas dibujadas en negro (algunas punteadas para las ocultas). Pregunta manuscrita roja: "¿Cuáles de los siguientes pares de puntos extremos no pueden representar iteraciones simplex sucesivas: (A,B), (B,D), (E,H) y (A,I)?" — ejercicio sobre adyacencia de vértices en un politopo.

## Slide 17

Mismo diagrama 3D del politopo (vértices A–J). Pregunta manuscrita roja: "Suponga que las iteraciones simplex se inician en A y que el óptimo ocurre en H. Indique si alguna de las siguientes trayectorias son no legítimas para el algoritmo simplex, y explique la razón: (i) A–B–G–H, (ii) A–E–I–H, (iii) A–C–E–B–A–D–G–H".

## Slide 18

Mismo diagrama 3D del politopo, ahora con las variables de holgura s1, s2, s3, s4 señaladas mediante líneas rojas hacia distintas caras/aristas del sólido (s3 y s4 hacia arriba cerca de D-G, s2 hacia B-H, s1 hacia abajo cerca de C-E). Pregunta roja: "Si s1, s2, s3 y s4 son las variables de holgura asociadas a las restricciones representadas por los planos CEIJF, BEIHG, DFJHG e IJH, respectivamente, identificar las variables básicas y las variables no básicas en cada punto extremo."

## Slide 19

Mismo diagrama 3D del politopo. Pregunta roja: "Para cada una de las funciones objetivo abajo, cuál es la variable de entrada en la base? Con cuál valor entra en la base?" con 4 funciones objetivo listadas:
1) Maximizar z = x1 − 2x2 + 3x3
2) Maximizar z = 5x1 + 2x2 + 4x3
3) Maximizar z = −2x1 + 7x2 + 2x3
4) Maximizar z = x1 + x2 + x3

## Slide 20

Gráfico 2D: región factible poligonal (sombreada gris) en el plano x1-x2 con vértices etiquetados A, B, C, D, E, F, G (heptágono irregular entre x1∈[-1,5], x2∈[-1,4]). Función objetivo mostrada arriba: "Maximizar z = 3x1 + 6x2". Pregunta roja: "Si el simplex se inicia en el punto A, ¿cuál es la trayectoria que conduce al punto E óptimo?"

## Slide 21

Mismo gráfico y polígono de la slide 20 (vértices A-G). Función objetivo cambiada: "Maximizar z = 4x1 + x2". Pregunta roja: "Determine la variable de entrada y el cambio del valor de z, suponiendo que el punto inicial es el punto A".

## Slide 22

Mismo gráfico y polígono. Función objetivo: "Maximizar z = 16x1 + 15x2". Misma pregunta roja: "Determine la variable de entrada y el cambio del valor de z, suponiendo que el punto inicial es el punto A".

## Slide 23

Título rojo "Ejemplo en dimensión 3 (sin gráfico)". Formulación:
```
max    5x1 + 4x2 + 3x3
s.t.   2x1 + 3x2 + x3 ≤ 5
       4x1 + x2 + 2x3 ≤ 11
       3x1 + 4x2 + 2x3 ≤ 8
       x1, x2, x3 ≥ 0
```
Slide de solo texto matemático, explícitamente sin figura (problema de 3 variables, no graficable en 2D).

## Slide 24

Recuadro izquierdo: mismo problema de la slide 23. Flecha roja "Introducción de variables de holgura" hacia recuadro inferior: primera restricción convertida a igualdad: 2x1+3x2+x3+w1=5, w1≥0, despejada como w1 = 5 − 2x1 + 3x2 + x3 (nota: en la slide el signo aparece inconsistente respecto al enunciado original, revisar transcripción exacta en la imagen — se muestra "w1 = 5 − 2x1 + 3x2 + x3" con recuadro rojo).

## Slide 25

Recuadro izquierdo: problema original (misma formulación 3x3). Flecha roja hacia el sistema completo con las 3 variables de holgura:
ζ = 5x1 + 4x2 + 3x3
w1 = 5 − 2x1 − 3x2 − x3
w2 = 11 − 4x1 − x2 − 2x3
w3 = 8 − 3x1 − 4x2 − 2x3
x1,x2,x3,w1,w2,w3 ≥ 0

## Slide 26

Mismo sistema de la slide 25 en recuadro. Texto rojo: "Solución factible inicial? (0,0,0,5,11,8)".

## Slide 27

Mismo sistema en recuadro. Pregunta roja: "Que variable debería entrar en la base?"

## Slide 28

Mismo sistema en recuadro. Cálculo rojo: x1 = min{5/2, 11/4, 8/3} = 5/2. Pregunta: "Que variable debería salir de la base?"

## Slide 29

Mismo sistema en recuadro. Mismo cálculo x1 = min{5/2, 11/4, 8/3} = 5/2. Texto rojo: "Que variable debería salir de la base? Nueva solución (5/2, 0, 0, 0, 1, 1/2)".

## Slide 30

Recuadro izquierdo: mismo sistema original, con anotaciones rojas "Entra" (sobre x1 en ζ) y "Pivot" (sobre el coeficiente de x1 en w1) y "Sale" (sobre w1). Recuadro derecho: resultado del pivote, x1 despejada:
x1 = 5/2 − (1/2)w1 − (3/2)x2 − (1/2)x3
Texto rojo: "Podemos reescribir x1 en función de las nuevas variables no básicas... y no sólo x1, sino también todas las variables básicas". Recuadro inferior derecho muestra el sistema resultante completo:
ζ = 12.5 − 2.5w1 − 3.5x2 + 0.5x3
x1 = 2.5 − 0.5w1 − 1.5x2 − 0.5x3
w2 = 1 + 2w1 + 5x2
w3 = 0.5 + 1.5w1 + 0.5x2 − 0.5x3

## Slide 31

Recuadro con el sistema resultante de la slide 30 (ζ, x1, w2, w3 en función de w1, x2, x3). Preguntas rojas a la derecha: "Variable de entrada? Variable de salida? Pivot?"

## Slide 32

Recuadro izquierdo: mismo sistema anterior. Flecha roja hacia recuadro derecho con el resultado del siguiente pivote:
ζ = 13 − w1 − 3x2 − w3
x1 = 2 − 2w1 − 2x2 + w3
w2 = 1 + 2w1 + 5x2
x3 = 1 + 3w1 + x2 − 2w3

Todos los coeficientes de las variables no básicas en ζ son negativos ⇒ solución óptima alcanzada (z=13). Slide sin texto rojo adicional visible salvo la flecha de transición.

## Slide 33

Título rojo "De manera general, un P.L. en forma estándar se puede escribir así" con flecha hacia la formulación general con sumatorias:

$$\max \sum_{j=1}^n c_j x_j$$
$$\text{s.t.} \sum_{j=1}^n a_{ij}x_j \le b_i, \quad i=1,\dots,m$$
$$x_j \ge 0, \quad j=1,\dots,n$$

## Slide 34

Misma formulación general con sumatorias (izquierda). Texto rojo derecha: "Hasta ahora, el diccionario inicial se ha obtenido asignando el valor 0 a todas las variables x y el valor bi a cada variable wi"; "Eso es válido solo si los valores bi son todos no-negativos"; "¿Que hacemos si no es el caso?". Se muestra el diccionario general:
ζ = Σ cj xj
wi = bi − Σ aij xj, i=1,...,m

## Slide 35

Misma formulación general (izquierda). Texto rojo: "Trabajamos temporalmente con un problema auxiliar para el cual: 1. Es fácil encontrar una solución factible. 2. Una solución óptima proporciona un diccionario factible para el problema original."

## Slide 36

Diagrama 3D (sin etiquetas de ejes numéricas más que x0, x1, x2): representa geométricamente el "problema auxiliar" — un politopo extendido en una dimensión adicional x0, con puntos rojos marcando cómo el desplazamiento en x0 (flechas verticales y las líneas punteadas "x0" repetidas) permite "levantar" un punto infactible del plano original (región gris/azul) hasta hacerlo factible en el espacio aumentado. Ilustra la idea de la variable auxiliar x0 que se resta a cada restricción para crear holgura artificial.

## Slide 37

Recuadros: izquierda, problema original (max Σcjxj, s.t. Σaijxj≤bi, xj≥0), etiquetado "<- problema original". Derecha, el "problema auxiliar ->": max −x0, s.t. (Σj=1..n aij xj) − x0 ≤ bi para i=1..m, xj≥0 para j=0..n.

## Slide 38

Formulación completa del problema auxiliar (misma de la slide 37) repetida arriba. Texto rojo explicativo en dos columnas: "El problema original tiene una solución factible ssi el problema auxiliar tiene una solución factible con x0=0"; "En otras palabras: El problema original tiene una solución factible ssi la solución óptima del problema auxiliar tiene un valor objetivo igual a 0."

## Slide 39

Título "Ilustración". Ejemplo numérico concreto:
```
max   -2x1 - x2      <- problema original
s.t.  -x1 + x2 ≤ -1
      -x1 - 2x2 ≤ -2
             x2 ≤ 1
         x1, x2 ≥ 0
```
Pregunta roja: "problema auxiliar ?" — nótese que bi negativos (−1, −2) hacen que el diccionario inicial trivial no sea factible, motivando el método de la fase auxiliar.

## Slide 40

Mismo ejemplo de la slide 39 (izquierda). Derecha: el problema auxiliar construido:
```
max   -x0
s.t.  -x1 + x2 - x0 ≤ -1
      -x1 - 2x2 - x0 ≤ -2
             x2 - x0 ≤ 1
         x0, x1, x2 ≥ 0
```
Etiquetado "problema auxiliar ->".

## Slide 41

Título "Ilustración" (continuación). Diccionario inicial del problema auxiliar (infactible):
ξ = −x0
w1 = −1 + x1 − x2 + x0
w2 = −2 + x1 + 2x2 + x0
w3 = 1 − x2 + x0
Texto rojo: "Diccionario no factible, pero... aplicamos un pivote donde x0 entra en la base y donde la variable más 'infactible' sale" (es decir, w2, que tiene el b más negativo, −2).

## Slide 42

Recuadro izquierdo: mismo diccionario infactible de la slide 41. Recuadro derecho "Resultado:" tras el pivote (x0 entra, w2 sale):
ξ = −2 + x1 + 2x2 − w2
w1 = 1 − 3x2 + w2
x0 = 2 − x1 − 2x2 + w2
w3 = 3 − x1 − 3x2 + w2
Texto: "...un diccionario factible".

## Slide 42

Título rojo "Después de 2 otros pivotes:" con el diccionario resultante:
ξ = 0 − x0
x2 = 0.33 − 0.33w1 + 0.33w2
x1 = 1.33 − x0 + 0.67w1 + 0.33w2
w3 = 0.67 + x0 + 0.33w1 − 0.33w2
Texto rojo: "Función objetivo del problema original: ζ = −2x1 − x2". Derecha: "Eliminamos los x0 y reemplazamos la función objetivo auxiliar con la función objetivo original: obtenemos un diccionario inicial factible para el problema original:"
ζ = −3 − w1 − w2
x2 = 0.33 − 0.33w1 + 0.33w2
x1 = 1.33 + 0.67w1 + 0.33w2
w3 = 0.67 + 0.33w1 − 0.33w2
Pregunta roja: "¿Sólo factible?" — cierra el ejemplo de la fase auxiliar/fase 1 del método simplex de dos fases.

## Slide 43

Título manuscrito rojo "Para practicar..." Slide de cierre que remite a una herramienta externa: logo negro "neos Guide", texto "Simple Pivot Tool" y la URL https://neos-guide.org/content/simple-pivot-tool. Decorativa/referencial (recurso externo recomendado), sin contenido matemático nuevo.
