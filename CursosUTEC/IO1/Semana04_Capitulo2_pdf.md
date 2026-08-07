---
curso: IO1
titulo: Semana04-Capitulo2
slides: 61
fuente: Semana04-Capitulo2.pdf
---

## Slide 1

Portada. "Investigación de operaciones I — Capítulo 2: Introducción a la programación lineal". Logo UTEC (decorativa) y pie de página con crédito ©Fabien Cornillier.

## Slide 2

**Planta de cemento: condiciones de producción**

- Una planta produce dos tipos de cemento: cemento 1 y cemento 2.
- La utilidad por tonelada es de $50 para el cemento 1, y $70 para el cemento 2.
- Para producir una tonelada del cemento 1, se necesitan 40 minutos de calcinación y 20 minutos de trituración.
- Para producir una tonelada del cemento 2, se necesitan 30 minutos de calcinación y 30 minutos de trituración.
- El horno y el triturador son disponibles 6 horas y 8 horas por día respectivamente.

## Slide 3

**Planta de cemento: problema**

¿Cuánto cemento de cada tipo deberíamos producir cada día para maximizar la utilidad?

## Slide 4

**Planta de cemento: modelamiento**

- El problema se modela con un programa lineal.
- La respuesta del problema son dos cantidades: la cantidad de cada tipo de cemento por producir cada día.
- Denotamos por $x_1$ la cantidad de cemento 1, y por $x_2$ la cantidad de cemento 2.

## Slide 5

**Planta de cemento: programa lineal**

1. Las variables $x_1$ y $x_2$ se llaman: variables de decisión (o simplemente: variables).
2. Escribimos lo que queremos hacer, la función objetivo:

$$\max\ z = 50x_1 + 70x_2$$

3. Escribimos las restricciones:

$$40x_1 + 30x_2 \le 360$$
$$20x_1 + 30x_2 \le 480$$
$$x_1, x_2 \ge 0$$

## Slide 6

**Planta de cemento: programa lineal**

Los valores (50, 70) de la función objetivo, (40, 30, 360) de la primera restricción y (20, 30, 480) de la segunda restricción se llaman: **parámetros**.

## Slide 7

**Programa matemático**

- De manera general, llamamos programa matemático un problema de optimización de una función objetivo con variables y restricciones.
- Decimos que el programa es lineal si la función objetivo y las restricciones son todas combinaciones lineales de las variables de decisión.

## Slide 8

**Forma algebraica de un programa matemático**

El problema de cemento se puede reescribir de manera más general para cualquier número de cementos y cualquier número de procesos.

- Definimos un conjunto $C$ de cementos: $C = \{1, 2, \ldots, |C|\}$.
- Definimos un conjunto $P$ de procesos: $P = \{1, 2, \ldots, |P|\}$.

## Slide 9

**Forma algebraica de un programa matemático**

- Definimos los parámetros:
  - $u_i$: Utilidad por tonelada del cemento $i \in C$.
  - $r_{ij}$: Tiempo de proceso $j \in P$ para producir una tonelada de cemento $i \in C$.
  - $R_j$: Tiempo disponible por día para el proceso $j \in P$.
- Definimos las variables de decisión:
  - $x_i$: Cantidad de cemento $i$ por producir cada día.

## Slide 10

**Forma algebraica de un programa matemático**

$$\max\ z = \sum_{i \in C} u_i x_i$$
$$\text{s.t.}\quad \sum_{i \in C} r_{ij} x_i \le R_j \quad \forall j \in P$$
$$x_i \ge 0 \quad \forall i \in C.$$

Es la forma que se utiliza generalmente. Utilizaremos esa forma en las sesiones de laboratorio para resolver los problemas de optimización con Julia y JuMP.

## Slide 11

**Forma genérica de un programa matemático**

- La forma genérica de un programa lineal tiene:
  - $n$ variables no-negativas.
  - $m$ restricciones de igualdad o de desigualdad.
  - una función objetivo por optimizar.
- El parámetro (coeficiente) de costo (o de utilidad) de la variable $x_j$ se denota por $c_j$.
- El coeficiente de la variable $x_j$ en la restricción $i$ se denota por $a_{ij}$.
- La restricción $i$ tiene un segundo término constante $b_i$.
- Las restricciones simples de no-negatividad no son parte de las $m$ restricciones (los algoritmos las tratan a parte).

## Slide 12

**Forma genérica de un programa matemático de maximización**

$$\max\ z = \sum_{j=1}^{n} c_j x_j$$
$$\text{s.t.}\quad \sum_{j=1}^{n} a_{ij} x_j \le b_i \quad \forall i \in \{1,\ldots,m\}$$
$$x_j \ge 0 \quad \forall j \in \{1,\ldots,n\}$$

## Slide 13

**Forma genérica de un programa matemático de minimización**

$$\min\ z = \sum_{j=1}^{n} c_j x_j$$
$$\text{s.t.}\quad \sum_{j=1}^{n} a_{ij} x_j \ge b_i \quad \forall i \in \{1,\ldots,m\}$$
$$x_j \ge 0 \quad \forall j \in \{1,\ldots,n\}$$

## Slide 14

**Forma genérica de un programa matemático**

- Una solución que satisface todas las restricciones (como $x_1 = 4$ y $x_2 = 2$ en el ejemplo del cemento) se llama: **solución factible**.
- Si ninguna otra solución es mejor que una solución factible, es una **solución óptima**.
- A cualquier solución corresponde un valor de la función objetivo: un **valor objetivo**.
- A una solución óptima corresponde el **valor óptimo** de la función objetivo.

## Slide 15

**Forma genérica de un programa matemático**

- Si todas las variables tienen la restricción de ser enteras, el programa matemático se llama: **programa lineal entero** (en inglés: Integer Program).
- Un caso particular es cuando todas las variables son binarias (0 ó 1), se llama: **programa lineal binario**.
- Un programa que tiene a la vez variables continuas y variables enteras se llama: **programa lineal mixto**.
- Si al menos una restricción o la función objetivo no es una combinación lineal de variables, tenemos un **programa no-lineal**.

## Slide 16

**Forma genérica de un programa matemático**

- Los programas lineales enteros, binarios y mixtos son más difíciles que los programas lineales.
- Los programas no-lineales son aún más difíciles, excepto por unos casos específicos, como por ejemplo cuando las funciones objetivos son convexas.

## Slide 17

**¿Programa lineal?**

$$\max\ z = x_1 + x_2$$
$$\text{s.t.}\quad x_1 \ge x_2$$
$$x_1 \le 60 - 3x_2$$
$$x_1, x_2 \ge 0.$$

(Pregunta de reflexión: sí es lineal, restricciones y objetivo son combinaciones lineales de $x_1, x_2$.)

## Slide 18

**¿Cuál es el problema con esa formulación?**

Misma formulación que en el slide 17 pero con desigualdades estrictas:

$$\max\ z = x_1 + x_2$$
$$\text{s.t.}\quad x_1 > x_2$$
$$x_1 < 60 - 3x_2$$
$$x_1, x_2 \ge 0.$$

Problema: las desigualdades estrictas (>, <) no definen un espacio factible cerrado, complicando la existencia de un óptimo bien definido (los algoritmos de PL requieren ≤/≥).

## Slide 19

**¿Programa lineal?**

$$\max\ z = x_1 + x_2$$
$$\text{s.t.}\quad x_1^2 \ge x_2$$
$$x_1 \le 60 - 3x_2$$
$$x_1, x_2 \ge 0.$$

No es lineal: la primera restricción tiene $x_1^2$ (término cuadrático).

## Slide 20

**¿Programa lineal?**

$$\max\ z = x_1 + x_2$$
$$\text{s.t.}\quad |x_1| \ge 30$$
$$x_1 \le 60 - 3x_2$$
$$x_1, x_2 \ge 0.$$

No es lineal en su forma actual: la restricción usa valor absoluto $|x_1|$, que no es una combinación lineal (aunque se puede reformular linealmente en algunos casos).

## Slide 21

**¿Programa lineal?**

$$\max\ z = x_1 + x_2$$
$$\text{s.t.}\quad x_1 \ge |u|$$
$$x_1 \le v - 3x_2$$
$$x_1, x_2 \ge 0.$$

Con parámetros $u$ y $v$. Nota: aquí $|u|$ es un parámetro (constante conocida), no una variable, por lo que la restricción SÍ es lineal en las variables de decisión $x_1, x_2$.

## Slide 22

**¿Programa lineal?**

$$\max\ z = x_1 + x_2$$
$$\text{s.t.}\quad x_1 \ge \sqrt{u}$$
$$x_1 \le v - 3x_2$$
$$x_1, x_2 \ge 0.$$

Con parámetros $u$ y $v$. Igual que en el slide 21, $\sqrt{u}$ es una constante (parámetro), no una variable, así que sigue siendo un programa lineal en $x_1, x_2$. (Nota: el texto extraído de esta slide coincidía por error con el de la slide 21 — la fórmula visual real usa raíz cuadrada de $u$, $\sqrt{u}$, no valor absoluto.)

## Slide 23

**Forma matricial clásica**

Denotamos por:
- $x = (x_1, x_2, \ldots, x_n)^T$ el vector de variables,
- $b = (b_1, b_2, \ldots, b_m)^T$ el vector de segundos términos de las restricciones,
- $c = (c_1, c_2, \ldots, c_n)^T$ el vector de coeficientes asociadas a las variables de la función objetivo,
- $A$ la matriz de los coeficientes $a_{ij}$ de tamaño $m \times n$.

## Slide 24

**Forma matricial clásica**

Podemos escribir un programa lineal en forma matricial de dos maneras. Tabla comparativa:

| | Forma estándar | Forma canónica |
|---|---|---|
| max | $c^T x$ | $c^T x$ |
| s.t. | $Ax \le b$ | $Ax = b$ |
| | $x \ge 0$ | $x \ge 0$ |

Esas formas matriciales se utilizan principalmente en presentaciones teóricas para simplificar las notaciones.

## Slide 25

**Comentarios importantes**

- En la realidad un programa lineal puede tener igualdades y desigualdades.
- Podemos siempre convertir una restricción de igualdad con dos restricciones de desigualdad.

## Slide 26

**Comentarios importantes**

- Podemos convertir una restricción de desigualdad en una restricción de igualdad con una nueva variable (lo veremos más tarde).
- También podemos convertir un programa de maximización en un programa de minimización: Para minimizar una función objetivo $z$, maximizamos la función objetivo $-z$ conservando las mismas restricciones. Si el valor óptimo del programa de maximización es $z^*$ entonces el valor óptimo del programa de minimización es $-z^*$.
- Una variable sin restricción de no-negatividad (se llama: variable **libre**) se puede escribir como la diferencia de dos variables no-negativas.

## Slide 27

**Terminología**

En las restricciones de un programa lineal:
- la parte izquierda, función de las variables ($Ax$), se denota frecuentemente por **LHS** (Left Hand Side).
- la parte derecha constante ($b$) se denota por **RHS** (Right Hand Side).

## Slide 28

**Resolución gráfica de programas lineales con dos variables**

$$\max\ z = x_1 + 2x_2$$
$$\text{s.t.}\quad x_1 + x_2 \le 6$$
$$x_2 \le 3$$
$$x_1, x_2 \ge 0$$

- ¿Este problema está escrito en forma canónica o estándar?
- ¿Cómo se puede escribir en forma canónica matricial?

## Slide 29

**Resolución gráfica**

Diagrama manuscrito (dibujo a mano alzada, tipo pizarra) del plano cartesiano $x_1$ (eje horizontal, 0 a 6) vs $x_2$ (eje vertical, 0 a 6), que resuelve gráficamente el problema del slide 28:

- Se dibujan dos rectas de restricción: $x_1 + x_2 \le 6$ (recta diagonal que va de $(0,6)$ a $(6,0)$, con flecha indicando el lado factible hacia el origen) y $x_2 \le 3$ (recta horizontal en $x_2=3$, con flecha hacia abajo indicando el lado factible).
- El **espacio factible** es la región sombreada (rayada) delimitada por ambas restricciones y los ejes: un pentágono con vértices en $(0,0)$, $(6,0)$, $(3,3)$, $(0,3)$.
- Se dibujan varias rectas paralelas naranjas representando la **función objetivo** $z = x_1 + 2x_2$ para diferentes valores objetivo (líneas de nivel), desplazándose en la dirección de la flecha (hacia arriba-derecha, dirección de maximización).
- Se marca el punto óptimo con un círculo naranja en la intersección de las dos restricciones: $(x_1=3, x_2=3)$.
- Anotación manuscrita: "solución óptima → $(x_1=3, x_2=3)$, valor óptimo: 9".
- Leyenda al pie del diagrama: cuadro rayado = "Espacio factible"; línea naranja = "función objetivo para diferentes valores objetivos"; línea azul con flechas = "Restricción con flechas orientadas hacia el espacio factible".

## Slide 30

**Casos especiales**

- Sin la restricción $x_1 + x_2 \le 6$, tendríamos un espacio factible **no acotado**.
- ¿Tendríamos una solución óptima?
- ¿Se podría tener un programa lineal con espacio factible no acotado y un valor óptimo finito?
- ¿Se podría tener un programa lineal con espacio factible vacío?

## Slide 31

**Casos especiales**

- ¿Se podría tener un programa lineal con múltiples soluciones óptimas?
- En el caso de tener múltiples soluciones óptimas, ¿cuántas tendríamos?
- Si existe al menos una solución óptima, ¿siempre existe una solución óptima que corresponde a una esquina (o **punto extremo**) del espacio factible?

## Slide 32

**Casos especiales**

- En un problema real como la optimización de un plan de producción, el espacio factible normalmente no es vacío: existe al menos el plan de producción actual no optimizado. Si el espacio factible es vacío, el problema es sobre-restringido.
- Si el valor objetivo es infinito en un problema real, hay un error en el programa matemático: inversión de signo, inversión de la dirección de una desigualdad, falta de restricción, etc.

## Slide 33

**Ejercicio: Problema de la dieta**

- Una granja necesita **al menos** 800kg por día de un alimento constituido de una mezcla de maíz y de soya.
- Se necesita **al menos** 30% de proteínas y un **máximo** de 5% de fibras.
- Los costos y los nutrientes del maíz y del soya son los siguientes:

| Cereal | Proteínas (%) | Fibras (%) | Costo ($/kg) |
|---|---|---|---|
| Maíz | 9 | 2 | 0.30 |
| Soya | 60 | 6 | 0.90 |

## Slide 34

**Ejercicio: Problema de la dieta**

- Se busca la mezcla de menos costo.
- Formular el problema con un programa lineal:
  i. Determinar las variables de decisión.
  ii. Escribir la función objetivo.
  iii. Escribir las restricciones.
- Escribir el problema en forma canónica.
- Escribir el problema de forma algebraica con un número indeterminado de cereales y de nutrientes.

## Slide 35

**Ejercicio: Problema de la mochila**

Formular el problema de la mochila con un número indeterminado de objetos y escribir el programa en forma algebraica.

- Identificar el (los) conjunto(s) necesario(s) y elegir una notación.
- Identificar los parámetros necesarios y elegir una notación.
- Identificar las variables de decisión necesarias y elegir una notación.
- Escribir la función objetivo.
- Escribir las restricciones.

## Slide 36

**Ejercicio: Problema de particionamiento**

- $S$ es un conjunto de números enteros de $\mathbb{N}^*$.
- Queremos partir el conjunto $S$ en dos subconjuntos $S_1$ y $S_2$.
- Denotamos por $s_1$ y $s_2$ las sumas de los números en $S_1$ y $S_2$.
- Escribir un programa lineal para minimizar la diferencia entre $s_1$ y $s_2$.

## Slide 37

**Ejercicio: Problema de particionamiento**

Generalización del slide 36:

- $S$ es un conjunto de números enteros de $\mathbb{N}^*$.
- Queremos partir el conjunto $S$ en $n$ subconjuntos $S_1, S_2, \ldots, S_n$.
- Denotamos por $s_1, \ldots, s_n$ las sumas de los números en $S_1, \ldots, S_n$.
- Escribir un programa lineal para minimizar la diferencia entre $\max\{s_1,\ldots,s_n\}$ y $\min\{s_1,\ldots,s_n\}$.

## Slide 38

Slide separador de sección: "**Variables binarias y restricciones lógicas**".

## Slide 39

Consideramos el caso de una empresa que tiene un conjunto $P = \{1,2,\ldots,|P|\}$ de proyectos en los cuales tiene la oportunidad de invertir.

Asociamos a cada proyecto $i \in P$ la variable binaria $x_i$ siguiente:

$$x_i = \begin{cases} 1 & \text{si se invierte en el proyecto } i \in P \\ 0 & \text{caso contrario} \end{cases}$$

## Slide 40

**Caso 1**

No se puede invertir en más de $N$ proyectos.

## Slide 41

**Caso 2**

Se debe invertir en un mínimo de $N$ proyectos.

## Slide 42

**Caso 3**

Si se invierte en el proyecto 1, entonces se invierte también en el proyecto 2.

## Slide 43

**Caso 4**

Los proyectos 1 y 2 son incompatibles. Si se invierte en uno, no se puede invertir en el otro.

## Slide 44

**Caso 5**

Se debe invertir al menos en uno de los proyectos 1 y 2.

## Slide 45

**Caso 6**

Si se invierte en el proyecto 1, entonces se debe también invertir en los proyectos 2 y 3.

## Slide 46

**Caso 7**

Si se invierte en el proyecto 1, entonces se debe también invertir en al menos uno de los proyectos 2 y 3.

## Slide 47

**Caso 8**

Si se invierte en al menos uno de los proyectos 1 y 2, entonces se debe invertir también en el proyecto 3.

## Slide 48

**Caso 9**

Si se invierte en los dos proyectos 1 y 2, entonces se debe invertir en el proyecto 3.

## Slide 49

Slide separador de sección: "**Método del Big-M**".

## Slide 50

El método del big-M consiste en utilizar un valor suficientemente grande en una restricción para que en ciertas condiciones esa restricción sea satisfecha para cualquier valor que las variables de decisión podrían tomar.

## Slide 51

**Ejemplo**

Consideramos un problema de *location-transportation* que consiste en elegir en un conjunto $W$ de almacenes aquellos que debemos abrir para abastecer un conjunto $S$ de tiendas, además de decidir de las cantidades de productos que se enviarán desde cada almacén hasta cada tienda.

## Slide 52

**Objetivo**

Minimizar el costo total calculado como la sumatoria de los costos fijos $f_i$ de apertura de un almacén $i$ y los costos variables $v_{ij}$ de transporte de cada unidad de producto desde el almacén $i$ hasta la tienda $j$. Definimos también $q_i$ como la capacidad de cada almacén $i$ y $d_j$ como la demanda de cada tienda $j$.

## Slide 53

**Variables de decisión**

Denotamos por $x_{ij}$ la variable de decisión que corresponde a la cantidad de productos enviados desde el almacén $i \in W$ hasta la tienda $j \in S$, y por $y_i$ la variable de decisión binaria que toma el valor 1 si se abre el almacén $i \in W$ y el valor 0 en el caso contrario.

## Slide 54

**Pregunta**

¿Cómo garantizar que ningún producto sea enviado a una tienda desde un almacén cerrado?

Traducción: ¿Cómo garantizar que las variables $x_{ij}$ sean nulas si $y_i = 0$?

## Slide 55

Podemos utilizar un valor $M$ grande y plantear la restricción siguiente:

$$x_{ij} \le M y_i, \quad \forall i \in W, j \in S.$$

Si sabemos por ejemplo que ninguna tienda necesita más de $d$ unidades del producto, un buen valor de $M$ podría ser $d$.

## Slide 56

**Peligro con el big-M**

Podríamos pensar que cualquier valor grande de $M$ es adecuado y, por ejemplo, fijar $M = 1000000000000000\ldots000$, pero "mezclar" coeficientes mayores en muchos órdenes de magnitud que cualquiera de los otros genera generalmente importantes problemas numéricos (en el capítulo 6, veremos por ejemplo que genera una pésima relajación lineal).

Por esa razón, el valor del big-M debería ser **suficientemente grande** para que las restricciones sean válidas, no más grande.

## Slide 57

**Ejemplo de modelo mejorado**

Si sabemos por ejemplo que cualquier tienda $j$ nunca necesita más de $d_j$ unidades del producto, podríamos plantear las restricciones siguientes:

$$x_{ij} \le d_j y_i, \quad \forall i \in W, j \in S.$$

**Importante:** Se puede ver que el big-M no tiene que ser único, sino que es frecuentemente preferible tener varios big-Ms cuando se puede. Aquí, tenemos un $M_j = q_j$ distinto para cada tienda. Es mejor que tener un único valor de $M$ para todas las tiendas.

(Nota: el texto de la slide dice $M_j = q_j$, aunque por contexto lógico correspondería a $d_j$; se transcribe literal lo que aparece.)

## Slide 58

**Aún mejor**

Si sabemos además que el stock de producto del almacén $i$ es limitado a $h_i$ unidades, podríamos plantear las restricciones siguientes:

$$x_{ij} \le \min\{q_i, d_j\}\, y_i, \quad \forall i \in W, j \in S.$$

## Slide 59

**Activar / desactivar restricciones con el big-M**

Consideramos una variable binaria $\delta$.

¿Cómo formular que la restricción:

$$\sum_{i \in N} a_i x_i \le b$$

sea satisfecha si $\delta = 1$?

## Slide 60

**Disyunción lógica con el big-M**

¿Cómo formular que de las dos restricciones siguientes:

$$(1)\quad \sum_{i \in N} a_i x_i \le b$$

y

$$(2)\quad \sum_{i \in N} c_i x_i \le d$$

al menos una sea satisfecha?

## Slide 61

Slide de cierre: "Fín del capítulo 2". Contiene una fotografía decorativa (fotograma de una escena de película/serie, hombre con lentes, bigote y polo claro, gesticulando) ocupando la mitad izquierda de la slide — es puramente decorativa/humorística, sin contenido técnico. Logo UTEC y pie de página estándar.
