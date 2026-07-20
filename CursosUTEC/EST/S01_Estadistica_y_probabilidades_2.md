---
curso: EST
titulo: S01_Estadística y probabilidades 2
slides: 33
fuente: S01_Estadística y probabilidades 2.pdf
---

# S01_Estadística y probabilidades 2

## Índice

Capítulo de Estadística y Probabilidades 2. Contenido transcrito de las diapositivas (fórmulas en LaTeX, figuras descritas).

# Estadística y Probabilidades 2 — Tema 1: Probabilidades y Variables aleatorias

## Slide 1 — Portada

**ESTADÍSTICA y PROBABILIDADES 2**

**Tema 1:**

**Probabilidades y Variables aleatorios**

**Sesión 1.1**

**UTEC** — Universidad de Ingeniería y Tecnología

**Figura:** Portada con imagen de edificio moderno (concreto y vidrio) en perspectiva diagonal, con líneas geométricas de marco.

---

## Slide 2 — Objetivos

**OBJETIVOS:**

- Recordar el cálculo básico de las probabilidades.
- Conocer la interpretación que pueden tener estas probabilidades, para un problema de contexto.
- Formular variables que sean consideradas como aleatorias.
- Calcular la distribución de probabilidades, el esperado y la varianza de una variable aleatoria.

---

## Slide 3 — Teoría Básica de Probabilidades

**TEORÍA BÁSICA DE PROBABILIDADES**

**Figura:** Tres imágenes representativas: 1) Mano dentro de globo azul (urna/sorteo), 2) Dados rojos entre bolitas blancas, 3) Dados rojos de múltiples puntos.

---

## Slide 4 — Experimento Aleatorio (Definición)

**EXPERIMENTO ALEATORIO**

Un **experimento aleatorio**, es un experimento cuyo resultado no está garantizado, aunque tomemos todas las precauciones necesarias para que las condiciones de su realización sean las mismas.

Un experimento aleatorio **depende del azar** y lo que pretendemos hacer con teoría de **probabilidades**, es establecer un lenguaje que sirva para hablar, entender y tratar de predecir los **eventos sujetos a la incertidumbre**.

**Figura:** Dos dados rojos de distintos ángulos sobre fondo blanco.

---

## Slide 5 — Experimento Aleatorio (Ejemplos y Descripción Formal)

**EXPERIMENTO ALEATORIO**

**Ejemplos de Experimento aleatorio:**

1) De una mina, extraer un kilo de un mineral y pesar la cantidad de impurezas que contiene.

2) Adquirir un vehículo de segunda y ver la cantidad de defectos que posee.

3) Participar de la Tinka.

4) La duración de la batería de una laptop.

---

Desde el punto de vista formal, para describir un **experimento aleatorio** hacen falta tres ingredientes:

- El **espacio de resultados, universo o espacio muestral**: aquí van todos los resultados individuales pertinentes.
- La **colección de todos los eventos** relevantes: cada evento es un **subconjunto del universo**.
- Una **función de probabilidad**; una función que a cada evento le asigne un número entre cero y uno.

**Figura:** Dos dados rojos.

---

## Slide 6 — Función de Probabilidad

**FUNCIÓN DE PROBABILIDAD**

Para calcular probabilidades, se necesita:

1) Un experimento aleatorio
2) Un espacio muestral $\Omega$ (el conjunto que tiene a todas las posibilidades)
3) Un evento $E$ (subconjunto del espacio muestral: contiene solo lo que quiero)
4) Hacer un conteo de los casos en que ocurren $\Omega$ y $E$.

**5) PROBABILIDAD DE UN EVENTO:**

$$P(E) = \frac{n(E)}{n(\Omega)}$$

---

**PROPIEDADES DE PROBABILIDADES**

$$1) P(\emptyset) = 0$$

$$2) P(\Omega) = 1$$

$$3) \text{Si } E \text{ es un evento: } 0 \leq P(E) \leq 1$$

**4) PROPIEDAD DEL COMPLEMENTO:**

$$P(E') = 1 - P(E)$$

**5) PROPIEDAD DE LA UNIÓN:**

$$P(E \cup F) = P(E) + P(F) - P(E \cap F)$$

**6) EVENTOS MUTUAMENTE EXCLUYENTES:**

Dos eventos son excluyentes si no se pueden realizar simultáneamente.

Es decir: $P(E \cap F) = 0$

**Figura:** Persona en traje con manos abiertas junto a varios dados de diferentes colores.

---

## Slide 7 — Ejemplos de Cálculo de Probabilidades

**Ejemplos:**

En una sección se tiene 15 varones y 10 mujeres.

1) Seleccionando una persona al azar ¿Cuál es la probabilidad de elegir una mujer?

2) Seleccionando dos personas con reposición ¿Cuál es la probabilidad de elegir dos mujeres?

3) Seleccionando dos personas al azar sin reposición ¿Cuál es la probabilidad de elegir dos mujeres?

4) Seleccionando dos personas con reposición ¿Cuál es la probabilidad de elegir dos personas de sexo diferente?

5) Seleccionando dos personas sin reposición ¿Cuál es la probabilidad de elegir dos personas de sexo diferente?

---

## Slide 8 — Soluciones (Blanca)

**SOLUCIONES:**

*(slide con solo título, sin contenido visible)*

---

## Slide 9 — Soluciones (Blanca)

**SOLUCIONES:**

*(slide con solo título, sin contenido visible)*

---

## Slide 10 — Probabilidad Condicional

**PROBABILIDAD CONDICIONAL**

Sean los eventos $U$ y $V$.

- **$U$:** Evento que se desea que suceda.
- **$V$:** Evento que ya sucedió y del cual se tiene información.

$$\text{U/V: U sabiendo V}$$
$$\text{U dado V}$$

**PROBABILIDAD DE $U$ DADO $V$:**

$$P(U|V) = \frac{P(U \cap V)}{P(V)}$$

**Ejemplo con datos:**

Se conoce: $P(A) = \frac{1}{4}$, $P(B) = \frac{1}{8}$, $P(A|B) = \frac{2}{3}$.

$$\Rightarrow P(A \cap B) = \frac{P(A|B) \cdot P(B) \cdot P(A|B)}{P(B)} = \frac{2}{3} \cdot \frac{1}{8} = \frac{1}{12}$$

**a) Calcule $P(B|A)$:**

$$P(B|A) = \frac{P(A \cap B)}{P(A)} = \frac{\frac{1}{12}}{\frac{1}{4}} = \frac{1}{3}$$

**b) Calcule $P(B|A')$:**

$$P(B|A') = \frac{P(A' \cap B)}{P(A')} = \frac{\frac{1}{24}}{\frac{3}{4}} = \frac{1}{18}$$

**Figura:** Pizarrón verde con preguntas sobre probabilidad condicional.

---

## Slide 11 — Ejemplo de Probabilidad Condicional

**EJEMPLO**

En una sección se tiene 10 mujeres y 15 hombres.

Se selecciona dos personas con reposición y se encontró que la primera es mujer ¿cuál es la probabilidad de que la segunda sea hombre?

---

## Slide 12 — Variable Aleatoria (Portada)

**VARIABLE ALEATORIA**

**Figura:** Composición artística con un dado 3D sobre fondo de números descubiertos (6, 8, 4, 1, etc.) y distribuciones de densidad (curvas de campana) en tons rojos y naranjas.

---

## Slide 13 — Definición de Variables Aleatorias

**Variables aleatorias**

Una **variable aleatoria** es una función que asigna un número real a cada elemento del espacio muestral de un experimento aleatorio.

Se denotan con letras mayúsculas como $W, X, Y, Z, \ldots$

Las **variables aleatorias pueden ser discretas o continuas**.

- **Discretas:** cuando los valores numéricos son aislados y contables.
- **Continuas:** cuando los valores numéricos no son contables y es necesario considerar intervalos.

---

## Slide 14 — Variable Discreta

**Variable discreta**

En el diagrama observamos que $X$ lleva a cada elemento $\omega_i$ de $\Omega$ a un número $x_i$ de un conjunto denominado **rango de $X$**:

$$R_X = \{x_1, x_2, x_3, \ldots\}$$

Matemáticamente se expresa: $X: \Omega \to R_X \subset \mathbb{R}$

**Figura:** Diagrama de mapeo. A la izquierda: óvalo $\Omega$ con punto $\omega$ adentro. En el centro: flecha etiquetada $X$. A la derecha: recta numérica $\mathbb{R}$ con puntos rojos en $R_X$ indicando valores discretos $X(\omega) = x \in R_X$. Botón "Dar ejemplos" en gris.

---

## Slide 15 — Variable Continua

**Variable continua**

En el diagrama observamos que $X$ lleva a cada elemento $\omega_i$ de $\Omega$ a un número $x_i$ de un conjunto denominado **rango de $X$**, el cual siempre será algún intervalo cerrado o abierto:

$$R_X = [a; b]$$

Matemáticamente se expresa: $X: \Omega \to R_X \subset \mathbb{R}$

**Figura:** Diagrama de mapeo. A la izquierda: óvalo $\Omega$ con punto $\omega$ adentro. En el centro: flecha etiquetada $X$. A la derecha: recta numérica $\mathbb{R}$ con intervalo rojo $[a, b]$ indicando $X(\omega) = x \in R_X$. Botón "Dar ejemplos" en gris.

---

## Slide 16 — Función de Distribución de una Variable Continua

**Función de distribución de una variable continua**

Para que una variable aleatoria contínua $X$ esté bien definida es necesario conocer su Rango $R_X$ (valores que adopta $X(\omega)$ para $\omega \in \Omega$) pero también sus probabilidades.

Así, se define la **función de distribución** $F(\mathbf{x})$ en base a las probabilidades de intervalos de la forma $X \leq \mathbf{x}$:

$$F(\mathbf{x}) = P(X \leq \mathbf{x}) \quad \text{para todo } \mathbf{x} \in \mathbb{R}$$

---

## Slide 17 — Función de Distribución (Composición)

**Función de distribución**

En el diagrama observamos que $X$ lleva de $\Omega$ a un intervalo $R_X$ y finalmente los números de este intervalo son llevados a un número entre 0 y 1 mediante la función de distribución

$$X: \Omega \to R_X \subset \mathbb{R}, \quad F: R_X \to [0; 1]$$

**Figura:** Diagrama de composición. A la izquierda: óvalo $\Omega$ con punto $\omega$. Centro-izquierda: flecha $X$ a intervalo $R_X$ en $\mathbb{R}$. Centro-derecha: flecha $F$ a recta entre 0 y 1. Los valores F($\omega$) = x se mapean a valores entre 0 y 1.

---

## Slide 18 — Propiedades de la Función de Distribución

**Propiedades de la función de distribución**

1) Dado que $F(x)$ representa probabilidades:

$$0 \leq F(x) \leq 1, \quad \text{para todo } x \in \mathbb{R}$$

2) También:

$$F(-\infty) = 0, \quad F(\infty) = 1$$

3) Si $x_1 < x_2$ entonces $F(x_1) < F(x_2)$. Es decir, es función creciente.

4) Si $R_X = [a; b]$ o $]a; b[$ se debe cumplir:

- $F(a) = P(X \leq a) = 0$.
- $F(b) = P(X \leq b) = 1$.

---

## Slide 19 — Función de Densidad

**Función de densidad**

Dada una variable aleatoria contínua $X$ con función de distribución $F(x)$, se define la **función de densidad** mediante una función $f(x)$ tal que

$$f(\mathbf{x}) = F'(\mathbf{x})$$

Equivalentemente la función de densidad puede definirse mediante una función $f(x)$ tal que

$$F(\mathbf{x}) = P(X \leq \mathbf{x}) = \int_{-\infty}^{\mathbf{x}} f(t) \, dt$$

**La función de densidad debe cumplir con lo siguiente:**

- $f(x) \geq 0 \quad \text{para todo } x \in R_X$
- $\int_{-\infty}^{\infty} f(x) \, dx = 1$

---

## Slide 20 — Función de Densidad y Función de Distribución (Gráficas)

**Función de densidad y función de distribución**

**Ejemplo de gráficas:**

**Figura:** Dos gráficos superpuestos:

1. **Gráfico superior — Función de densidad del modelo normal estándar:** Curva de campana simétrica centrada en 0 (x = 0). Eje vertical (f) de 0 a 0.5. Eje horizontal (x) de -6 a 6. Fórmula mostrada: $f(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$

2. **Gráfico inferior — Función de distribución del modelo normal estándar:** Curva sigmoide (S) que va de 0 (en $-\infty$) a 1 (en $+\infty$), con punto de inflexión en x = 0. Eje vertical (F) de 0 a 1. Eje horizontal (x) de -6 a 6. Fórmula mostrada: $F(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}} e^{-\frac{t^2}{2}} dt$

**Notas importantes:**

- La función de densidad **no representa una probabilidad**.
- El **área debajo de la gráfica de la densidad y arriba del eje X sobre un intervalo**, sí representa una probabilidad.
- La **función de distribución siempre es una gráfica creciente**.

---

# Estadística y probabilidades II — Slides 21-33

## Slide 21 — Actividad de clase: Ejemplo 1

**Ejemplo 1:** En una sección se tiene 10 mujeres y 15 hombres. Se va a seleccionar con reposición, al azar, dos personas. Sea la variable aleatoria X: # de hombres seleccionados.

a) ¿Cuál es el rango de X?
b) Obtenga la función de probabilidad.
c) Obtenga la función de distribución acumulada.
d) Si la muestra se selecciona ahora, sin reposición y la primera persona seleccionada es un hombre, ¿cuál es la probabilidad de que en la muestra se tenga dos hombres?

**Nota:** En la esquina superior derecha de la slide aparece un recuadro amarillo con la propiedad fundamental: $\int_{-\infty}^{\infty} f(x)dx = 1$

---

## Slide 22 — Actividad de clase: Ejemplo 2

**Ejemplo 2:** Una variable aleatoria continua $X$ tiene función de densidad

$$f(x) = \begin{cases}
kx^2, & 0 \leq x \leq 3 \\
0, & \text{en otros casos}
\end{cases}$$

a) Calcule el valor de $k$.
b) Calcular $P(2 < X < 4)$

---

## Slide 23 — Actividad de clase: Ejemplo 3

**Ejemplo 3:** Una variable aleatoria continua $X$ tiene función de densidad

$$f(x) = \begin{cases}
kx^2, & 0 \leq x \leq 3 \\
0, & \text{en otros casos}
\end{cases}$$

a) Obtener la función de distribución.
b) Calcular $P(2 < X < 4)$

---

## Slide 24 — Actividad de clase: Ejemplo 4

**Ejemplo 4:** La duración de un foco hasta que falle, medido en cientos de horas, es una variable aleatoria con función de distribución dada por:

$$F(x) = \begin{cases}
0, & x < 0 \\
k - e^{-x^2}, & x \geq 0
\end{cases}$$

Calcule $k$ y Obtenga la función de densidad.

---

## Slide 25 — Actividad de clase: Ejemplo 5

**Ejemplo 5:** La duración de un foco hasta que falle, medido en cientos de horas, es una variable aleatoria con función de distribución dada por:

$$F(x) = \begin{cases}
0, & x < 0 \\
k - e^{-x^2}, & x \geq 0
\end{cases}$$

Calcule la probabilidad de que el foco dure por lo menos 100 horas, conociendo que su duración no excede las 200 horas.

---

## Slide 26 — Esperanza y Varianza: caso discreto

**Esperanza:**
$$E(X) = \sum_{x \in R_X}(x \cdot P(x))$$

**Varianza:**
- $V(X) = E(X - E(X))^2$
- $V(X) = E(X^2) - (E(X))^2$

siendo:
$$E(X^2) = \sum_{x \in R_X}(x^2 \cdot p(x))$$

**Figura:** Dos recuadros amarillos con las definiciones de esperanza y varianza. La varianza se presenta en dos formas: la definición clásica y la forma de cálculo simplificada.

---

## Slide 27 — Esperanza y Varianza: caso continuo

**Esperanza:**
$$E(X) = \int_{-\infty}^{\infty} x \cdot f(x)dx$$

**Varianza:**
- $V(X) = E(X - E(X))^2$
- $V(X) = E(X^2) - (E(X))^2$

siendo:
$$E(X^2) = \int_{-\infty}^{\infty} x^2 \cdot f(x)dx$$

**Figura:** Dos recuadros amarillos presentando las definiciones para el caso continuo. La estructura es análoga al caso discreto, pero reemplazando sumatorias por integrales.

---

## Slide 28 — Actividad de clase: Ejemplo 6

**Ejemplo 6:** En una sección se tiene 10 mujeres y 15 hombres. Se va a seleccionar al azar dos personas. Sea la variable aleatoria X: # de hombres seleccionados.

a) ¿Cuál es la cantidad esperada de hombres?
b) ¿Cuál es su varianza?
c) ¿Cuál es su coeficiente de variación?

---

## Slide 29 — Para el alumno: Ejemplos 7 y 8

**Ejemplo 7:**
Halle el valor esperado de $X$, si se sabe que su Función de distribución es

$$F(x) = \begin{cases}
0, & x < 1 \\
Ln x, & 1 \leq x \leq e \\
1, & x > e
\end{cases}$$

---

**Ejemplo 8:**
Halle el coeficiente de variación de la variable aleatoria $X$, conociendo que su función de densidad es

$$f(x) = \begin{cases}
\frac{x^2}{4}, & 1 \leq x \leq \beta \\
0, & \text{en otros casos}
\end{cases}$$

---

## Slide 30 — Para el alumno: Ejemplos 9 y 10

**Ejemplo 9:**
Una empresa produce a pedido de otra, discos de tamaños variables. Se sabe que la longitud esperada de sus circunferencias es $12\pi$ cm, mientras que la varianza de sus diámetros es $16 \, cm^2$.
Calcule la esperanza del área de los círculos de los discos.

---

**Ejemplo 10:**
Si $x$ es una variable aleatoria continua con función de densidad

$$f(x) = \begin{cases}
\frac{kx}{e^x}, & 0 \leq x \leq 1 \\
0, & \text{en otros casos}
\end{cases}$$

Calcule $E(x)$.

---

## Slide 31 — Bibliografía complementaria

**Figura:** Portadas de dos libros de referencia con sus datos bibliográficos.

**Estadística matemática con aplicaciones**
- Autores: Wackerly, D; Mendenhall, W; Scheaffer, R
- Editorial: Cengage learning

**Estadística para todos. Análisis de datos**
- Autora: Eva Romero Ramos
- Editorial: Pirámide
- Ubicación: Madrid, España

---

## Slide 32 — Pizarra en blanco

**Figura:** Pizarra blanca en perspectiva con línea de horizonte punteada. Contiene rotuladores (marcadores de colores) y una regla en la parte inferior. Aparentemente destinada para notas o ejemplos adicionales durante la clase.

---

## Slide 33 — Pizarra en blanco (segunda)

**Figura:** Pizarra blanca idéntica a la slide 32, en perspectiva con línea de horizonte punteada, rotuladores y regla. Destinada para continuación de notas o desarrollo de ejercicios adicionales.
