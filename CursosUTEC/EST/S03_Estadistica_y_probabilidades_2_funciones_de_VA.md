---
curso: EST
titulo: S03_Estadística y probabilidades 2 _ funciones de VA
slides: 16
fuente: S03_Estadística y probabilidades 2 _ funciones de VA.pdf
---

# S03_Estadística y probabilidades 2 _ funciones de VA

## Índice

Capítulo de Estadística y Probabilidades 2. Contenido transcrito de las diapositivas (fórmulas en LaTeX, figuras descritas).

# S03 — Estadística y Probabilidades II — Funciones de Variables Aleatorias

## Slide 1 — Portada

**Tema:**

# Funciones de variables aleatorias

**S03**

Estadística y probabilidades II — UTEC

Logo UTEC (Universidad de Ingeniería y Tecnología)

**Figura:** Portada con imagen de edificio de concreto (arquitectura moderna) en la esquina derecha. Diseño con marco gris metálico. Encabezado azul celeste "Estadística y probabilidades II" con logo UTEC. Título principal en rojo "Funciones de variables aleatorias".

---

## Slide 2 — Funciones de variables aleatorias

**Funciones de variables aleatorias**

En muchas situaciones reales se llegará a obtener que una variable $U$ depende de los valores que toma una variable aleatoria $X$. Entonces $U$ también será una variable aleatoria y por ello para que esté bien definida, debe hallarse sus probabilidades en base a su función de distribución y de su función de densidad, conociendo las correspondientes de $X$.

Ese es el objetivo que se tiene en esta sección.

---

## Slide 3 — Método de las funciones de distribución

**Método de las funciones de distribución**

Se debe tener una variable aleatoria continua $X$, de la cual se conoce su función de distribución $F(X)$, además se debe tener una función $U = U(X)$.

Se desea hallar la función de distribución $F_U(u)$.

| Paso | Descripción | Notas |
|------|-------------|-------|
| **Paso 1:** | $F_U(u) = P(U \leq u)$ | $U$ es variable aleatoria.<br/>$u$ es un valor numérico. |
| **Paso 2:** | $F_U(u) = P(U(X) \leq u)$ | $U = u(x)$ y se despeja $x$ |
| **Paso 3:** | $F_U(u) = P(X \leq U^{-1}(u))$ | |
| **Paso 4:** | $F_U(u) = F_X(U^{-1}(u))$ ➔ | Se halló la función de distribución de $U$. |
| **Paso 5:** | $f_U(u) = \frac{dF_U(u)}{du}$ ➔ | Se halló la función de densidad de $U$. |

---

## Slide 4 — Actividad de clase — Ejemplo 1

**Actividad de clase**

**Ejemplo 1:**

Una empresa azucarera debe producir diario 1 tonelada, pero tienen el inconveniente temporal de que su equipo industrial debe ser renovado, pero mientras no lo hagan, la cantidad de azúcar producida al día es una variable aleatoria $X$ con función de densidad

$$f(x) = \begin{cases} 2x, & 0 \leq x \leq 1 \\ 0, & \text{otros casos} \end{cases}$$

Cada día se vende todo lo que producen y el precio es de 500 dólares por tonelada, pero deben hacer cada día un pago de 100 dólares por mantenimiento de su equipo.

Halle la función de distribución y la función de densidad de la ganancia de la empresa, por día.

---

## Slide 5 — Solución (Ejemplo 1)

**Solución**

**Ejemplo 1:**

Una empresa azucarera debe producir diario 1 tonelada, pero tienen el inconveniente temporal de que su equipo industrial debe ser renovado, pero mientras no lo hagan, la cantidad de azúcar producida al día es una variable aleatoria $X$ con función de densidad

$$f(x) = \begin{cases} 2x, & 0 \leq x \leq 1 \\ 0, & \text{otros casos} \end{cases}$$

Cada día se vende todo lo que producen y el precio es de 500 dólares por tonelada, pero deben hacer cada día un pago de 100 dólares por mantenimiento de su equipo.

Halle la función de distribución y la función de densidad de la ganancia de la empresa, por día.

**Nota:** Esta página contiene principalmente la repetición del enunciado del Ejemplo 1 para referencia durante la resolución.

---

## Slide 6 — Continuación (Ejemplo 1 — Funciones halladas)

**Continuación**

**FUNCIÓN DE DISTRIBUCIÓN:**

[La slide muestra el título de sección pero las fórmulas específicas de $F_U(u)$ no son claramente visibles en esta diapositiva; aparentemente continuarían en la siguiente o se presentarían de manera visual]

**FUNCIÓN DE DENSIDAD:**

[De manera similar, los detalles de $f_U(u)$ se presentarían]

**Nota de transcripción:** Esta slide marca el título de las secciones donde se presentarían las soluciones completas de distribución y densidad del Ejemplo 1, pero el contenido específico de las fórmulas aparentemente se presenta en el desarrollo paso a paso (no visible completo en esta vista).

---

## Slide 7 — Actividad de clase — Ejemplo 2

**Actividad de clase**

**Ejemplo 2:**

Un abastecedor de gasolina de un grifo pequeño, tiene un tanque de 150 galones, que llena cada madrugada a un costo de S/ 12 el galón, para la venta del día. La demanda diaria muestra un comportamiento de frecuencia relativa que aumenta gradualmente hasta los 100 galones y luego se estabiliza en un nivel de entre 100 y 150 galones. Considerando que $x$ denota la demanda diaria total en cientos de galones y que la frecuencia relativa de demanda se representa mediante el modelo:

$$f(x) = \begin{cases} x, & 0 \leq x \leq 1 \\ k, & 1 < x \leq 1.5 \\ 0, & \text{en otros casos} \end{cases}$$

Cada día se vende el galón a S/ 20 y lo que no se llega a vender es enviado a una empresa que lo adquiere a un costo de S/ 10 el galón.

Halle la función de distribución y calcule además la ganancia diaria esperada del grifo.

---

## Slide 8 — Solución (Ejemplo 2)

**Solución**

**Ejemplo 2:**

Un abastecedor de gasolina de un grifo pequeño, tiene un tanque de 150 galones, que llena cada madrugada a un costo de S/ 12 el galón, para la venta del día. La demanda diaria muestra un comportamiento de frecuencia relativa que aumenta gradualmente hasta los 100 galones y luego se estabiliza en un nivel de entre 100 y 150 galones. Considerando que $x$ denota la demanda diaria total en cientos de galones y que la frecuencia relativa de demanda se representa mediante el modelo:

$$f(x) = \begin{cases} x, & 0 \leq x \leq 1 \\ k, & 1 < x \leq 1.5 \\ 0, & \text{en otros casos} \end{cases}$$

Cada día se vende el galón a S/ 20 y lo que no se llega a vender es enviado a una empresa que lo adquiere a un costo de S/ 10 el galón.

Halle la función de distribución y calcule además la ganancia diaria esperada del grifo.

**Nota de transcripción:** Esta slide repite el enunciado del Ejemplo 2 para referencia durante la resolución. La solución paso a paso se presentaría en las diapositivas subsecuentes.

---

## Slide 9 — Continuación

**Continuación**

[Esta slide aparece en blanco o con contenido mínimo en la vista del PDF proporcionada. Podría ser una página de transición o dedicada a trabajo de resolución no visible.]

---

## Slide 10 — Continuación

**Continuación**

[Esta slide aparece en blanco o con contenido mínimo en la vista del PDF proporcionada. Podría ser una página de transición o dedicada a trabajo de resolución no visible.]

---

## Slide 11 — Actividad de clase — Ejemplo 3

**Actividad de clase**

**Ejemplo 3:**

Consideremos la función de densidad de una variable aleatoria $X$:

$$f(x) = \begin{cases} 2x, & 0 \leq x \leq \beta \\ 0, & \text{otros casos} \end{cases}$$

Sea $U = 3(1 - X) - X$

Obtener la función de densidad de la variable $U$.

---

## Slide 12 — Continuación

**Continuación**

[Esta slide aparece en blanco o con contenido mínimo en la vista del PDF proporcionada. Podría ser una página de transición o dedicada a trabajo de resolución no visible.]

---

## Slide 13 — ¿Qué es la Ciencia de Datos?

**¿Qué es la Ciencia de Datos?**

Al estudiar la carrera de Ciencia de Datos en UTEC te convertirás en el profesional capaz de descifrar grandes volúmenes de información, predecir escenarios, tomar decisiones y crear soluciones a partir de ellos. Serás el responsable de encontrar y extraer tendencias a partir de grandes conjuntos de datos usando, por ejemplo, algoritmos de inteligencia artificial.

Aprenderás bajo una malla curricular de estándar internacional y nuestros convenios internacionales con las instituciones más top del mundo te llevarán a compartir tus conocimientos y tu ingenio.

La Ciencia de Datos es una profesión que las empresas están demandando cada vez más, especialmente en tiempos de transformación digital. Esta carrera en UTEC, primera de su tipo en el Perú, te llevará a dominar la relación entre las matemáticas, la estadística y la computación. Con tus conocimientos en análisis y procesamiento de datos, podrás ser el líder de los nuevos retos que el mundo afronta.

---

## Slide 14 — Analítica

**Analítica descriptiva**

¿Qué pasó? El primer nivel de complejidad permite responder a la pregunta qué sucedió en un determinado fenómeno bajo análisis. Las técnicas de estadística descriptiva nos permiten analizar una gran variedad de datos históricos (estructurados y no estructurados) y con diferentes métodos estadísticos podemos organizar estos datos y obtener información sobre lo que sucedió.

**Analítica prescriptiva**

¿Qué hacer para que ocurra? El cuarto nivel de complejidad es la analítica prescriptiva, donde mediante diferentes técnicas estadísticas es posible "prescribir" el comportamiento futuro de determinadas variables, mediante la simulación de escenarios y estimación de probabilidades de ocurrencia, cuantificando así el efecto de las decisiones futuras.

**Analítica diagnóstica**

¿Por qué sucedió? El segundo nivel de complejidad analítica nos permite responder a la pregunta ¿por qué sucedió en determinado fenómeno. En este nivel de complejidad encontramos las técnicas de inferencia estadística, que mediante la construcción de modelos nos permite estudiar la relación y comparación de variables para obtener conclusiones útiles.

**Analítica predictiva**

¿Qué pasará? El tercer nivel de complejidad corresponde a la analítica predictiva, que mediante la aplicación de algoritmos matemáticos y estadísticos a datos históricos, nos permitirá identificar patrones, detectar tendencias y realizar pronósticos para orientar el comportamiento de fenómenos futuros. Dentro de estas técnicas encontramos los modelos de regresión, modelos lineales generalizados y series de tiempo.

**Figura:** Diagrama con cuatro cuadrantes representando los niveles de complejidad analítica: 
- Cuadrante 1 (inferior izquierda): "Analítica descriptiva" (¿Qué ha pasado?) — color turquesa
- Cuadrante 2 (inferior centro): "Analítica diagnóstica" (¿Por qué hubo?) — color naranja/amarillo
- Cuadrante 3 (superior centro): "Analítica prescriptiva" (¿Qué va a pasar?) — color rosado/magenta
- Cuadrante 4 (superior derecha): Eje en blanco
- Eje horizontal: "Complejidad"
- Eje vertical: "Valor para la organización"

En el lado derecho superior, gráfico tipo tarta de pastel con variables $px, py=y_0, y_0=py, X=0$ mostrando distribución angular.

En el lado derecho medio: gráfico de "Analítica de diagnóstico" con curvas de distribución de probabilidad en color púrpura.

En el lado derecho inferior: gráfico de "Analítica predictiva" mostrando una línea de tendencia verde ascendente con puntos dispersos.

---

## Slide 15 — Página en blanco

[Esta slide aparece completamente en blanco. Podría ser una página de transición o espacio reservado.]

---

## Slide 16 — Bibliografía complementaria

**Bibliografía complementaria**

**Estadística matemática con aplicaciones.**

Wackerly, D; Mendenhall, W; Scheaffer, R

Cengage Learning

**Estadística para todos. Análisis de datos.**

Eva Romero Ramos.

Editorial Pirámide.

Madrid, España.

**Figura:** Se muestran dos portadas de libros:
- Izquierda: Portada de "ESTADÍSTICA MATEMÁTICA CON APLICACIONES" (Séptima edición), con diseño de colores suaves en turquesa y blanco, autores Wackerly, Mendenhall, Scheaffer, editorial Cengage Learning
- Derecha: Portada de "Estadística para TODOS — Análisis de datos: estadística descriptiva, teoría de la probabilidad e inferencia" de Eva Romero Ramos, Editorial Pirámide, Madrid, España, con diseño azul marino y gráfico de pirámide con rayas amarillas
