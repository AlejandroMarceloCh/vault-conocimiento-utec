---
curso: ML
titulo: Topic 1 - Types of Learning
slides: 31
fuente: Topic 1 - Types of Learning.pdf
---

## Slide 1

TIPOS DE APRENDIZAJE

**Figura:** Imagen de portada — un robot humanoide visto de espaldas, caminando por un túnel circular futurista de color azul con anillos concéntricos y líneas de datos superpuestas.

## Slide 2

¿CÓMO ESTUVO EL QUIZ?

**Figura:** Comillas decorativas grandes (") de fondo, centradas arriba y abajo del texto, sobre fondo degradado azul a negro.

## Slide 3

1.
Aprendizaje
*Tipos*

**Figura:** Mano robótica futurista señalando/tocando una proyección holográfica de un globo terráqueo digital con líneas de red y datos, sobre fondo oscuro azulado en el lado derecho de la slide.

## Slide 4

SUPERVISED LEARNING
UNSUPERVISED LEARNING
REINFORCEMENT LEARNING

**Figura:** Tres iconos 3D en escala de grises debajo de cada título: (1) bajo "Supervised Learning", dos figuras humanas genéricas junto a una pizarra, una señalando con un puntero (rol de profesor enseñando a un alumno); (2) bajo "Unsupervised Learning", una figura humana genérica sentada a una mesa leyendo un periódico con una taza de café al lado (sin supervisión externa); (3) bajo "Reinforcement Learning", un pequeño robot blanco con ojos azules brillantes, de pie, sin acompañamiento humano.

## Slide 5

Aprendizaje Supervisado

**Figura:** Diagrama de flujo: "Input" (izquierda) → flecha → recuadro "Model" (etiquetado arriba como "Student") → flecha → "Output" (derecha). Desde "Output" sale una flecha diagonal hacia abajo hacia un recuadro "Error", y desde "Error" sale otra flecha diagonal hacia un recuadro "Ground Truth" (etiquetado abajo como "Teacher"). Del recuadro "Error" también sale una flecha que retroalimenta hacia arriba al recuadro "Model", cerrando el ciclo de corrección.

## Slide 6

Aprendizaje Supervisado

**Figura:** Tabla con encabezados "task, T" | "performance measure, P" | "experience, E", con las tres columnas vacías (solo encabezados, sin contenido debajo).

## Slide 7

Aprendizaje Supervisado

**Figura:** Misma tabla de tres columnas, ahora completa:
- **task, T**: Predict a value / (boolean, numerical, categorical) / How is the expected output?
- **performance measure, P**: Error / (MSE, MAE, Cross Entropy) / How do we measure how close we are to the expected results?
- **experience, E**: (Input, GT) / Input: Numerical, images, text, signals / Output: Expected value / What are we learning?

## Slide 8

Aprendizaje No Supervisado

**Figura:** Diagrama de flujo idéntico al de la slide 5: "Input" → "Model" (etiquetado "Student") → "Output"; "Output" → "Error" → retroalimenta a "Model"; pero aquí "Error" NO conecta a un recuadro "Ground Truth" — en su lugar, debajo del diagrama aparece el texto suelto "Similar != Different" (no hay Teacher/Ground Truth explícito).

## Slide 9

Aprendizaje No Supervisado

**Figura:** Tabla con encabezados "task, T" | "performance measure, P" | "experience, E", con las tres columnas vacías (solo encabezados, sin contenido debajo).

## Slide 10

Aprendizaje No Supervisado

**Figura:** Misma tabla de tres columnas, ahora completa:
- **task, T**: Predict a representation / (multidimensional vector) / How is the expected output?
- **performance measure, P**: Error / (Intrinsic measures, similar != different) / How do we measure how close we are to the expected results?
- **experience, E**: Input / Input: Numerical, images, text, signals / What are we learning?

## Slide 11

Aprendizaje Por Refuerzo

**Figura:** Diagrama clásico de bucle agente-entorno en Reinforcement Learning. Recuadro "Agent" (arriba) y recuadro "Environment" (abajo), conectados por flechas etiquetadas: desde "Agent" sale "Action ($A_t$)" hacia "Environment" (lado derecho, flecha descendente); desde "Environment" salen "$R_{(t+1)}$" y "$S_{(t+1)}$" (lado izquierdo, flechas ascendentes) que retornan hacia "Agent" como "State ($S_t$)" y "Reward ($R_t$)" en la parte superior izquierda.

## Slide 12

Aprendizaje Por Refuerzo

**Figura:** Tabla con encabezados "task, T" | "performance measure, P" | "experience, E", con las tres columnas vacías (solo encabezados, sin contenido debajo).

## Slide 13

Aprendizaje Por Refuerzo

**Figura:** Misma tabla de tres columnas, ahora completa:
- **task, T**: Predict a step / (multidimensional vector) / How is the expected output?
- **performance measure, P**: Error / (Regret of best reward) / How do we measure how close we are from the maximum reward?
- **experience, E**: (Input, GT) / Input: Description of the environment / Output: Action / What are we learning?

## Slide 14

2.
Ejemplo
*Nuestro Primer ML Task*

**Figura:** Misma imagen de mano robótica futurista señalando un holograma de globo terráqueo digital, sobre fondo oscuro azulado en el lado derecho de la slide (idéntica composición a la slide 3, con distinto número de sección).

## Slide 15

**Figura:** Tabla con encabezados "task, T" | "performance measure, P" | "experience, E", con las tres columnas vacías (solo encabezados, sin contenido debajo). No hay título de slide visible.

## Slide 16

Dataset de Medical Diagnosis

Doctor diagnoses the patient as sick or not $y \in \{+, -\}$

based on attributes of the patient $x_1, x_2, ..., x_M$

**Figura:** Tabla de datos con columnas "y" (encabezada "allergic?") y "$x_1$" a "$x_4$" (encabezadas "hives?", "sneezing?", "red eye?", "has cat?"). Solo una fila visible, índice i=1: allergic?=- , hives?=Y, sneezing?=N, red eye?=N, has cat?=N.

## Slide 17

Medical Diagnosis Dataset

Doctor diagnoses the patient as sick or not $y \in \{+, -\}$

based on attributes of the patient $x_1, x_2, ..., x_M$

**Figura:** Misma tabla, ahora completa con 5 filas (i=1 a 5):
| i | allergic? (y) | hives? ($x_1$) | sneezing? ($x_2$) | red eye? ($x_3$) | has cat? ($x_4$) |
|---|---|---|---|---|---|
| 1 | - | Y | N | N | N |
| 2 | - | N | Y | N | N |
| 3 | + | Y | Y | N | N |
| 4 | - | Y | N | Y | Y |
| 5 | + | N | Y | Y | N |

## Slide 18

Medical Diagnosis Dataset

Doctor diagnoses the patient as sick or not $y \in \{+, -\}$

based on attributes of the patient $x_1, x_2, ..., x_M$

**Figura:** Misma tabla de 5 filas que en la slide 17, pero con notación indexada añadida a cada celda: cada valor de y se muestra como $y^{(i)}$ (ej. $y^{(1)}$, $y^{(2)}$, ..., $y^{(5)}$) y cada valor de x se muestra como $x_j^{(i)}$ (ej. $x_1^{(1)}$, $x_2^{(1)}$, etc.), en color verde/celeste para distinguir la notación superindexada de los valores Y/N/+/-.

## Slide 19

Medical Diagnosis Dataset

Doctor diagnoses the patient as sick or not $y \in \{+, -\}$

based on attributes of the patient $x_1, x_2, ..., x_M$

N = 5 training examples
M = 4 attributes

**Figura:** Misma tabla con notación indexada de la slide 18, con un recuadro punteado verde que encierra las columnas $x_1$ a $x_4$ de cada fila, y a la derecha de cada fila se añade la etiqueta del vector completo: $x^{(1)}$, $x^{(2)}$, $x^{(3)}$, $x^{(4)}$, $x^{(5)}$ (agrupando las 4 features de cada ejemplo en un vector).

## Slide 20

Our First Machine Learning Task

Learning to diagnose heart disease as a (**supervised**) binary classification task

**Figura:** Tabla con dos llaves (brackets) encima: una llave morada etiquetada "labels" que abarca la columna "allergic?", y una llave verde/azul etiquetada "features" que abarca las columnas "hives?", "sneezing?", "red eye?", "has cat?". A la izquierda, una llave dorada etiquetada "examples" que abarca las 5 filas numeradas (i=1 a 5). Contenido de la tabla:
| i | allergic? | hives? | sneezing? | red eye? | has cat? |
|---|---|---|---|---|---|
| 1 | - | Y | N | N | N |
| 2 | - | N | Y | N | N |
| 3 | + | Y | Y | N | N |
| 4 | - | Y | N | Y | Y |
| 5 | + | N | Y | Y | N |

## Slide 21

Our First Machine Learning Task

Learning to diagnose heart disease as a **(supervised)** **binary classification** task

**Figura:** Tabla de ejemplos con columna "i" (índice de ejemplo, 1 a 5), columna "labels" con encabezado "allergic?" (valores: -, -, +, -, +) y columna "features" con encabezados "hives?", "sneezing?", "red eye?", "has cat?" (valores Y/N por fila). Fila 3 (i=3) resaltada con recuadro en la columna de labels.

## Slide 22

Our First Machine Learning Task

Learning to diagnose heart disease as a **(supervised)** **classification** task

**Figura:** Misma tabla que el slide anterior, pero la columna de labels ahora se llama "allergy" y toma valores categóricos (no binarios): "none", "none", "dust", "none", "mold" para i=1 a 5. Columnas de features iguales: "hives?", "sneezing?", "red eye?", "has cat?" (Y/N). Filas 3, 4 y 5 resaltadas con recuadro en la columna de labels.

## Slide 23

Our First Machine Learning Task

Learning to diagnose heart disease as a **(supervised)** **regression** task

**Figura:** Misma tabla de ejemplos (i=1 a 5), ahora con columna "output" llamada "treatment cost" con valores numéricos: $10, $25, $1000, $25, $2000. Columnas de "features" iguales: "hives?", "sneezing?", "red eye?", "has cat?" (Y/N).

## Slide 24

Medical Diagnosis Dataset

Doctor diagnoses the patient as sick or not $y \in \{+, -\}$

based on attributes of the patient $x_1, x_2, \ldots, x_M$

**Figura:** Tabla con columnas etiquetadas y=allergic? (con flechas rojas curvas etiquetadas $c^*$ apuntando desde cada $x^{(i)}$ hacia $y^{(i)}$, indicando que el target function $c^*$ mapea el vector de atributos a la etiqueta) y $x_1$=hives?, $x_2$=sneezing?, $x_3$=red eye?, $x_4$=has cat?. Filas i=1 a 5 con valores: (y=-, x1=Y, x2=N, x3=N, x4=N), (y=-, x1=N, x2=Y, x3=N, x4=N), (y=+, x1=Y, x2=Y, x3=N, x4=N), (y=-, x1=Y, x2=N, x3=Y, x4=Y), (y=+, x1=N, x2=Y, x3=Y, x4=N). Cada fila de features está agrupada como vector $x^{(i)}$ (recuadro punteado verde). Debajo: "N = 5 training examples", "M = 4 attributes". Recuadro celeste con "Example hypothesis function:" y la fórmula $h(\mathbf{x}) = \begin{cases} + & \text{if sneezing} = Y \\ - & \text{otherwise} \end{cases}$

## Slide 25

Supervised Machine Learning

● **Problem Setting**
➔ Set of possible inputs, $x \in X$ (all possible patients)
➔ Set of possible outputs, $y \in Y$ (all possible diagnoses)
➔ Exists an unknown target function, $c^* : X \rightarrow Y$ (the doctor's brain)
➔ Set, $\mathcal{H}$, of candidate hypothesis functions, $h : X \rightarrow Y$ (all possible algorithms)

● **Learner** is given **N training examples** $D = \{(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), \ldots, (x^{(N)}, y^{(N)})\}$
where
$y^{(i)} = c^*(x^{(i)})$ (history of patients and their diagnoses)

● **Learner** produces a hypothesis function, $\hat{y} = h(x)$, that best approximates unknown target function $y = c^*(x)$ on the training data

## Slide 26

Error Rate

● **Consider a hypothesis h its…**

…error rate over all training data: **error(h, D_train)**

…error rate over all test data: **error(h, D_test)**

…true error over all data: **error_true(h)**

This is the quantity we care most about! But, in practice, **error_true(h)** is unknown.

## Slide 27

Algorithms for Classification

**Algorithm 1** **majority vote:** predict the most common label in the training dataset

**Figura:** Tabla con columna "predictions" (todas con valor "-") junto a la tabla de datos original: y=allergic? (-, -, +, -, +) y features x1=hives?, x2=sneezing?, x3=red eye?, x4=has cat? (valores Y/N por fila, i=1 a 5). Ilustra que el algoritmo de mayoría siempre predice la etiqueta más frecuente ("-") para todos los ejemplos.

## Slide 28

Algorithms for Classification

**Algorithm 2** **memorizer:** if a set of features exists in the training dataset, predict its corresponding label; otherwise, predict a random label

**Figura:** Misma tabla de datos (y=allergic?, x1=hives?, x2=sneezing?, x3=red eye?, x4=has cat?), con columna "predictions" que ahora coincide exactamente con los valores reales de "y" para cada fila (-, -, +, -, +), mostrando que el memorizador reproduce perfectamente las etiquetas ya vistas.

The memorizer always gets zero training error!

## Slide 29

Algorithms for Classification

**Algorithm 3** **decision stump:** based on a single feature, $x_d$, predict the most common label in the training dataset among all data points that have the same value for $x_d$

**Figura:** Misma tabla de datos (y=allergic?, x1=hives?, x2=sneezing?, x3=red eye?, x4=has cat?), con columna "predictions" con valores -, +, +, -, + (distintos a las etiquetas reales en las filas 2 y 3, mostrando error de entrenamiento no nulo). Recuadro celeste a la derecha: "Example decision stump:" con la fórmula $h(\mathbf{x}) = \begin{cases} + & \text{if sneezing} = Y \\ - & \text{otherwise} \end{cases}$

Nonzero training error, but perhaps still better than the memorizer

## Slide 30

Kahoot Time!

## Slide 31

**Figura:** Fotografía decorativa con overlay de color azul, mostrando a dos estudiantes con lentes de seguridad y bata de laboratorio observando un mecanismo/estructura metálica con cables y componentes electrónicos sobre una mesa de laboratorio. Sin texto de contenido.
