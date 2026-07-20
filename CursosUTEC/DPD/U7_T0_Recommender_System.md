---
curso: DPD
titulo: U7_T0_Recommender System.pptx
slides: 33
fuente: U7_T0_Recommender System.pptx.pdf
---

# U7_T0_Recommender System.pptx

## Índice

| Sección | Subtemas |
| --- | --- |
| Contexto e importancia | Interés en industria e investigación; aumento de servicios de contenido; valor empresarial; inventario limitado vs ilimitado; tienda física vs online |
| Paradoja de la elección | Experimento de la Cabina de Degustación |
| Sistemas de recomendación | Definición; feedback de usuario |
| Matriz de calificaciones | Ejemplo de películas; matriz dispersa; inferencia de preferencias |
| Enfoques principales | Filtrado colaborativo vs basado en contenido |
| Filtrado colaborativo (CF) | KNN; UBCF; IBCF; ejemplo numérico; Colab; problemas (cold start) |
| Factorización de matrices (SVD) | Descomposición; definición de P, Q, R; aproximación; vectores de factores; predicción; minimización; gradient descent |
| Recursos | Notebooks Colab y referencias |

## Contexto e importancia de los sistemas de recomendación

### Interés en industria e investigación

Interés significativo en la industria e investigación en sistemas de recomendación:

- 2 de cada 3 horas vistas provienen de recomendaciones
- Aumenta su tiempo de visualización en un 50% por año
- El 35% de todas las ventas son generadas por recomendaciones

**Figura:** En la parte superior izquierda, el encabezado «Interés significativo en la industria e investigación en sistemas de recomendación:» en tipografía sans-serif negrita de color negro.

una sección superior tiene una superposición de color cian brillante; en una foto inferior se distingue parcialmente el texto arquitectónico «IN GEN NIE CI RA BLE» (parte de «INGENIERÍA») sobre un muro.

(slides 2)

### Aumento de servicios de contenido y rol de los SR

Aumento dramático de los servicios de entrega de contenido y contenido multimedia
Amplia gama de opciones y limitaciones de tiempo estrictas

Mecanismos eficientes necesarios para descubrir contenido preferido
☞ Mejora de la satisfacción del usuario, disminución de las tasas de abandono

Los sistemas de recomendación (SR) abordan estos problemas
✔ Aprovechan la información sobre las preferencias de los usuarios
✔ Recomiendan contenido apropiado de manera precisa y eficiente

**Figura:** Tres cajas rectangulares apiladas horizontalmente, ligeramente escalonadas de arriba-izquierda a abajo-derecha:

1. **Caja superior (fondo verde claro):** Texto en negrita «Aumento dramático de los servicios de entrega de contenido y contenido multimedia». Subtexto: «Amplia gama de opciones y limitaciones de tiempo estrictas».
2. **Caja central (fondo morado/lila claro):** Texto en negrita «Mecanismos eficientes necesarios para descubrir contenido preferido». Subtexto precedido por ícono de mano señalando (☞): «Mejora de la satisfacción del usuario, disminución de las tasas de abandono».
3. **Caja inferior (fondo coral/naranja-rojizo):** Texto en negrita «Los sistemas de recomendación (SR) abordan estos problemas». Dos viñetas con marca de verificación (✔): «Aprovechan la información sobre las preferencias de los usuarios» y «Recomiendan contenido apropiado de manera precisa y eficiente».

(slides 3)

### Valor empresarial y personalización

Muchas empresas generan su valor al comprender las preferencias de los usuarios y proporcionar recomendaciones.

Las recomendaciones pueden influir en las noticias que leemos, los productos que compramos y el entretenimiento que consumimos.

**Figura:** En el lado izquierdo, el texto en español descrito arriba; la frase «recomendaciones pueden influir en las noticias que leemos» aparece resaltada en negrita. En el lado derecho, tres ejemplos visuales de sistemas de recomendación:

1. Círculos de perfiles de personas diversas conectados por líneas blancas formando una red.
2. **Servicio de streaming (abajo izquierda):** Captura de interfaz similar a **Netflix** con filas de contenido categorizadas:
   - «Emmy-winning US TV Shows»: pósters de *Rick and Morty*, *Family Guy*, *House of Cards*, *Orange is the New Black*.
   - «Police Detective TV Dramas»: pósters de *Peaky Blinders*, *iZombie*, *Dark*, *Altered Carbon*.
   - «Critically Acclaimed Witty TV Shows»: pósters de *The Good Place*, *BoJack Horseman*, *The IT Crowd*, *Big Mouth*.
3. **E-commerce (abajo derecha):** Logo de **Amazon.com**. Encabezado «Recommended for You» en azul. Subtexto: «Amazon.com has new recommendations for you based on items you purchased or told us you own.»

(slides 4)

### Inventario limitado vs inventario ilimitado

Inventario Limitado   Inventario Ilimitado

**Figura:** La parte superior contrasta dos tipos de inventario:

- **Inventario Limitado (izquierda):** Fotografía de una librería física tradicional con estanterías de madera llenas de libros, representando un espacio físico limitado.
- **Inventario Ilimitado (derecha):** Una flecha azul apunta desde la tienda física hacia una captura de pantalla de resultados de búsqueda de **Amazon** para libros de «Python», mostrando una grilla densa de numerosas portadas y títulos.

Debajo, cuatro ejemplos de sistemas de recomendación en acción:

1. **Amazon:** Sección «Customers who bought this item also bought...» con una fila de libros técnicos (p. ej., «Deep Learning», «Introduction to Machine Learning with Python»).
2. **Netflix:** Sección «Because you watched Narcos...» con miniaturas de *Breaking Bad*, *Sing*, *Surviving Escobar*.
3. **Compras en línea:** Fila de jeans azules bajo el encabezado «Similar items based on your browsing history...».
4. **Medium:** Lista de artículos bajo «Based on your reading history...» con títulos como «Sampling Techniques» y «Kubernetes Ingress Controllers».

(slides 5)

### Tienda física vs tienda online

"Un tienda física no puede ser reconfigurada sobre la marcha para atender a cada cliente según sus intereses particulares."
Chris Anderson

Pero una tienda online si

**Figura:** En el centro, la cita en texto azul claro negrita: «Un tienda física no puede ser reconfigurada sobre la marcha para atender a cada cliente según sus intereses particulares.» Debajo, la atribución «Chris Anderson» en texto gris claro. Más abajo, la frase «Pero una tienda online si» en color naranja-rojizo/coral.

(slides 6)

## Paradoja de la elección

### Experimento de la Cabina de Degustación

El Experimento de la Cabina de Degustación
Cuando la elección es desmotivadora: ¿Puede alguien desear demasiado algo bueno?
Sheena S. Iyengar
Universidad de Columbia
Mark R. Lepper
Universidad de Stanford

Vs

El 40% de los clientes se detuvieron en la cabina de elección limitada.
El 60% de los clientes se detuvieron en la cabina de elección extensa.

**Figura:** Slide con título «El Experimento de la Cabina de Degustación» en la parte superior. Subtítulo: «Cuando la elección es desmotivadora: ¿Puede alguien desear demasiado algo bueno?» Autores: Sheena S. Iyengar (Universidad de Columbia) y Mark R. Lepper (Universidad de Stanford). En el centro, comparación de dos escenarios separados por un «Vs» grande en color rosa:

- **Lado izquierdo (elección limitada):** Etiqueta «6 jam samples» (6 muestras de mermelada). Imagen de 6 frascos distintos de mermelada. Texto debajo: «El 40% de los clientes se detuvieron en la cabina de elección limitada.»
- **Lado derecho (elección extensa):** Etiqueta «24 jam samples» (24 muestras de mermelada). Imagen de una grilla de 24 frascos de mermelada. Texto debajo: «El 60% de los clientes se detuvieron en la cabina de elección extensa.»

Vs

30% de conversión
3% de conversión

**Figura:** Slide con el mismo título, subtítulo y autores que la slide 7. En el centro, la misma comparación de dos escenarios separados por «Vs» en rosa:

- **Lado izquierdo:** Etiqueta «6 jam samples». Imagen de 6 frascos de mermelada. Texto debajo: «30% de conversión».
- **Lado derecho:** Etiqueta «24 jam samples». Imagen de grilla de 24 frascos de mermelada. Texto debajo: «3% de conversión».

**Figura:** Slide con el mismo título, subtítulo y autores que las slides 7 y 8. Dos elementos visuales principales:

1. **Gráfico (lado izquierdo):** Eje vertical etiquetado «happiness» (felicidad) y eje horizontal etiquetado «choices» (opciones). Una curva parte del origen, sube en color verde (más opciones aumentan la felicidad inicialmente), alcanza un pico y luego desciende gradualmente en color rojo (demasiadas opciones reducen la felicidad). Anotaciones sobre el gráfico: «Less is more» y «Too much choice = Stressful».
2. **Portada de libro (lado derecho):** Portada amarilla del libro «THE PARADOX OF CHOICE» de Barry Schwartz, con subtítulo «WHY MORE IS LESS» (con una marca de verificación roja junto a esta línea en un formato de lista de casillas). Diseño estilizado como formulario de opción múltiple o lista de verificación.

(slides 7–9)

## Sistemas de recomendación

### Definición

Un sistema de recomendación es un sistema que proporciona sugerencias de ítems que son más relevantes para un usuario en particular.

Ejemplos:
- Generadores de listas de reproducción para servicios de video y música
- Recomendadores de productos para tiendas en línea
- Recomendadores de contenido para plataformas de redes sociales
- Recomendadores de viajes
- Resultados de búsqueda
- …

**Figura:** Título «Sistemas de Recomendación»: la palabra «Sistemas» en azul brillante y «de Recomendación» en negro. Debajo, la definición y los ejemplos en viñetas descritos arriba. Ícono de tres hexágonos azules agrupados en la esquina inferior derecha.

(slides 10)

### Feedback de usuario

Feedback Explícito: El usuario indica su preferencia por algunos items.
- Ratings scales (1-5 estrellas, 1-10 estrellas)
- Binary values (liked/disliked)

Feedback Implícito: Los usuarios interactúan con los items.
- Histórico de Compras
- Duración de visita
- Patrones de Clicks

**Figura:** Slide con título «Feedback de Usuario» en negrita negra. Dos secciones:

1. **Feedback Explícito** (subencabezado en azul): Definición y ejemplos descritos arriba. Debajo del texto, dos filas de cinco estrellas: la primera con una estrella amarilla rellena (calificación baja) y la segunda con cuatro estrellas amarillas rellenas (calificación alta).
2. **Feedback Implícito** (subencabezado en azul): Definición y ejemplos descritos arriba. Debajo del texto, dos íconos de reproductor de video con barras de progreso:
   - Primer reproductor: barra de progreso roja muy corta, con un círculo negro que contiene un signo de interrogación blanco encima (bajo compromiso o señal incierta).
   - Segundo reproductor: barra de progreso roja casi completa, con un círculo verde que contiene una marca de verificación blanca encima (alto compromiso, señal positiva implícita).

(slides 11)

## Matriz de calificaciones y objetivo del sistema

### Ejemplo de calificaciones de películas

| Movie | Alice (1) | Bob (2) | Carol (3) | Dave (4) | (romance) | (action) |
| --- | --- | --- | --- | --- | --- | --- |
| Love at last | 5 | 5 | 0 | 0 | 0.9 | 0 |
| Romance forever | 5 | ? | ? | 0 | 1.0 | 0.01 |
| Cute puppies of love | ? | 4 | 0 | ? | 0.99 | 0 |
| Nonstop car chases | 0 | 0 | 5 | 4 | 0.1 | 1.0 |
| Swords vs. karate | 0 | 0 | 5 | ? | 0 | 0.9 |

$n_u = \text{no. users}$

$n_m = \text{no. movies}$

$r(i, j) = 1$ if user $j$ has rated movie $i$

$y^{(i, j)} = \text{rating given by user } j \text{ to movie } i$ (defined only if $r(i, j) = 1$)

**Figura:** Slide con una tabla central que muestra calificaciones de películas por cuatro usuarios y dos características de contenido por película. Los signos «?» indican calificaciones desconocidas que el sistema de recomendación buscaría predecir. A la derecha de la tabla, las definiciones matemáticas listadas arriba. En la esquina superior derecha, una leyenda de calificación con estrellas: una caja con una grilla 5×5 de estrellas; cada fila muestra una calificación diferente de 1 a 5 estrellas (estrellas rojas rellenas representan la calificación, contornos grises el resto).

(slides 12)

### Matriz dispersa y predicción

Ratings matrix

Matriz dispersa : La mayoría de los valores son desconocidos
Predicción: La tarea de llenar los valores desconocidos

**Figura:** Slide titulada «Ratings matrix». En el centro, una matriz usuario-ítem:

- **Filas ($u$):** Usuarios etiquetados de $u_1$ a $u_n$. La fila $u_j$ está resaltada con fondo rojo.
- **Columnas ($i$):** Ítems etiquetados de $i_1$ a $i_m$.
- **Valores de las celdas:** Calificaciones representadas con escala de 5 estrellas (estrellas doradas para la calificación, contornos tenues para las vacías). Por ejemplo, el usuario $u_1$ dio 5 estrellas al ítem $i_1$ y 1 estrella al ítem $i_m$; el usuario $u_n$ dio 2 estrellas al ítem $i_1$ y 4 estrellas al ítem $i_k$.
- **Celdas vacías:** Muchas celdas en blanco indican que esos usuarios aún no han calificado esos ítems.
- **Celda objetivo:** En la fila resaltada $u_j$, bajo la columna $i_k$, hay una celda verde con un signo de interrogación grande negro (**?**), representando una calificación faltante que el sistema debe predecir.

Debajo de la matriz, las dos definiciones en español descritas arriba.

(slides 13)

### Inferencia de preferencias

Inferir las preferencias de los usuarios sobre ítems
Producir listas de ítems altamente relevantes y personalizadas

items

rating: level of preference

users

unknown preferences

ratings matrix

**Figura:** Slide titulada «Sistemas de Recomendación». En la mitad superior, una caja rectangular de color melocotón/naranja claro con el objetivo del sistema:

- Tarea principal: «Inferir las preferencias de los usuarios sobre ítems».
- Salida deseada: «Producir listas de ítems **altamente relevantes y personalizadas**» (esta frase en negrita).

En el centro, un diagrama de la **matriz de calificaciones (ratings matrix)**:

- Eje vertical: **users** — filas etiquetadas `user A`, `user B`, `user C`.
- Eje horizontal: **items** — columnas etiquetadas `Movie A`, `Movie B`, `Movie C`, `Movie D`.
- **Valores de la matriz:**
  - User A: Movie A (4), Movie C (3), Movie D (5); celda Movie B vacía.
  - User B: Movie B (5), Movie C (4); celdas Movie A y Movie D vacías.
  - User C: Movie A (5), Movie B (4), Movie C (2); celda Movie D vacía.

Flechas azules con anotaciones:

- Una flecha apunta al valor «5» (calificación de User A para Movie D) con la etiqueta «rating: level of preference».
- Una flecha apunta a una celda vacía (calificación faltante de User C para Movie D) con la etiqueta «unknown preferences».

Etiqueta «ratings matrix» debajo del diagrama.

(slides 14)

## Enfoques principales

### Filtrado colaborativo vs basado en contenido

Filtrado Colaborativo (CF):
Inspeccionar patrones de calificación para encontrar usuarios/ítems similares

Content-based (CB):
Analizar atributos de los ítems para construir perfiles de usuario

En general, el CF (Filtrado Colaborativo) funciona mejor que el CB (Basado en Contenido).
- El CF no puede proporcionar predicciones precisas con calificaciones insuficientes.
- El CB puede aliviar el problema de dispersión.

**Figura:** Slide titulada «Enfoques Principales». Dos métodos presentados en cajas de colores:

1. **Filtrado Colaborativo (CF)** (caja verde): «Inspeccionar patrones de calificación para encontrar usuarios/ítems similares».
2. **Content-based (CB)** (caja naranja; en la slide aparece escrito «Conten-based»): «Analizar atributos de los ítems para construir perfiles de usuario».

Debajo, texto comparativo y dos viñetas:

- «En general, el CF (Filtrado Colaborativo) funciona mejor que el CB (Basado en Contenido).»
- Viñeta en rojo: «El CF no puede proporcionar predicciones precisas con calificaciones insuficientes.»
- Viñeta en verde: «El CB puede aliviar el problema de dispersión.»

(slides 15)

## Filtrado colaborativo (CF)

### Recomendadores populares: enfoque K-Nearest Neighbors

Recomendadores Populares: Enfoque de K-Vecinos Más Cercanos (K-Nearest Neighbors)

Filtrado colaborativo basado en usuarios (UBCF)
Suposición: Usuarios similares tienen preferencias similares
- Similitud entre usuarios: acuerdo en ítems co-calificados
- Predicción: suma ponderada de las calificaciones de usuarios similares

Filtrado colaborativo basado en ítems (IBCF)
Suposición : Los usuarios tienen gustos similares para ítems similares
- Similitud entre ítems: acuerdo entre usuarios que calificaron ambos ítems
- Predicción: suma ponderada de las calificaciones de ítems similares

**Figura:** Slide dividida en dos secciones principales, cada una con texto a la izquierda y un diagrama de matriz usuario-ítem a la derecha. La matriz es una grilla de 6 filas (usuarios, indicados con íconos de avatar) × 5 columnas (ítems/películas, indicados con miniaturas de pósters). Calificaciones numéricas del 1 al 5 dispersas en las celdas; celdas vacías donde no hay calificación.

**Sección superior — UBCF:** Dos filas específicas (usuarios 2 y 5) están encerradas en rectángulos verdes horizontales, representando los «vecinos más cercanos» o usuarios similares. Calificaciones visibles en la grilla:

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Usuario 1 | — | 2 | — | 1 | 4 | 5 |
| Usuario 2 (resaltado) | 5 | — | 4 | — | — | 1 |
| Usuario 3 | — | — | 5 | — | 2 | 2 |
| Usuario 4 | — | 1 | — | 5 | — | 4 |
| Usuario 5 (resaltado) | 4 | — | 4 | — | 2 | — |
| Usuario 6 | 4 | 5 | — | 1 | — | — |

**Sección inferior — IBCF:** En la misma grilla, dos columnas específicas (columnas 1 y 3, películas/ítems) están encerradas en rectángulos verdes verticales, representando ítems similares basados en las calificaciones de los usuarios.

(slides 17)

### Filtrado colaborativo basado en usuarios (UBCF)

Filtrado colaborativo basado en usuarios (UBCF)
Suposición: Usuarios similares tienen preferencias similares
- Similitud entre usuarios: acuerdo en ítems co-calificados
- Predicción: suma ponderada de las calificaciones de usuarios similares

Encontrar la similitud de los usuarios con el usuario objetivo U. La similitud para cualquier par de usuarios 'a' y 'b' puede... $r_{up}$: rating del usuario $u$ respecto al item $p$

$$\text{sim}(u, v) = \frac{\sum_{i \in I} (r_{u,i} - \bar{r}_u)(r_{v,i} - \bar{r}_v)}{\sqrt{\sum_{i \in I} (r_{u,i} - \bar{r}_u)^2} \sqrt{\sum_{i \in I} (r_{v,i} - \bar{r}_v)^2}}$$

$$r_{up} = \bar{r}_u + \frac{\sum_{i \in \text{users}} \text{sim}(u, i) \cdot r_{ip}}{\sum_{i \in \text{users}} |\text{sim}(u, i)|}$$

**Figura:** Slide titulada «Filtrado colaborativo basado en usuarios (UBCF)». A la derecha, una **matriz de calificaciones usuario-ítem**: columnas representan ítems (pósters de películas), filas representan usuarios (avatares). Las celdas contienen calificaciones del 1 al 5. Dos usuarios específicos (filas 2 y 5) están delineados con cajas verdes, indicando la comparación entre ellos para calcular similitud. Debajo del diagrama, el texto introductorio a las fórmulas y las dos ecuaciones descritas arriba: la primera calcula la similitud $\text{sim}(u, v)$ entre dos usuarios $u$ y $v$ (correlación de Pearson centrada en la media, donde $r_{u,i}$ es la calificación del usuario $u$ para el ítem $i$ y $\bar{r}_u$ es el promedio de calificaciones del usuario $u$); la segunda predice la calificación $r_{up}$ que el usuario $u$ daría al ítem $p$, ajustando el promedio $\bar{r}_u$ del usuario con una suma ponderada de las calificaciones $r_{ip}$ de usuarios similares $i$, donde los pesos son los puntajes de similitud $\text{sim}(u, i)$.

(slides 18)

### Filtrado colaborativo basado en ítems (IBCF)

Filtrado colaborativo basado en ítems (IBCF)

Los usuarios tienen gustos similares para ítems similares
- Similitud entre ítems: acuerdo entre usuarios que calificaron ambos ítems
- Predicción: suma ponderada de las calificaciones de ítems similares

$$similarity(i, j) = \frac{\sum_{u}^{U} r_{(u,i)} \cdot r_{(u,j)}}{\sqrt{\sum_{u}^{U} r_{(u,i)}^2} \cdot \sqrt{\sum_{u}^{U} r_{(u,j)}^2}}$$

- $i$: el ítem principal para el cual se buscan ítems similares.
- $j$: el ítem que se compara con el ítem $i$.
- $r_{(u,i)}$: la calificación dada por el usuario $u$ al ítem $i$.
- $r_{(u,j)}$: la calificación dada por el usuario $u$ al ítem $j$.

https://towardsdatascience.com/comprehensive-guide-on-item-based-recommendation-systems-d67e40e2b75d#:~:text=Item%2Ditem%20collaborative%20filtering%20is,great%20role%20in%20Amazon's%20success.

**Figura:** Slide titulada «Filtrado colaborativo basado en ítems (IBCF)». A la derecha, una matriz usuario-ítem con usuarios en filas (íconos de avatar) e ítems en columnas (pósters de películas). Algunas celdas contienen calificaciones numéricas (1, 2, 4, 5) y otras están en blanco. Dos columnas específicas (ítems $i$ y $j$) están resaltadas con cajas verdes para ilustrar que la similitud se calcula entre columnas (ítems). En el centro de la slide, la fórmula de **similitud coseno** entre dos ítems $i$ y $j$:

- **Numerador** ($\sum_{u}^{U} r_{(u,i)} \cdot r_{(u,j)}$): suma de los productos de las calificaciones de ambos ítems dados por todos los usuarios $U$ que calificaron ambos.
- **Denominador** ($\sqrt{\sum_{u}^{U} r_{(u,i)}^2} \cdot \sqrt{\sum_{u}^{U} r_{(u,j)}^2}$): producto de las raíces cuadradas de la suma de calificaciones al cuadrado para el ítem $i$ y el ítem $j$ respectivamente.

Anotaciones con flechas señalando $i$, $j$, $r_{(u,i)}$ y $r_{(u,j)}$ en la fórmula. URL de referencia en la parte inferior apuntando a una guía de sistemas de recomendación basados en ítems en towardsdatascience.com. Número de slide «19» visible en la esquina inferior.

(slides 19)

### Ejemplo numérico de filtrado colaborativo

Preferencias pasadas dan información de preferencias futuras

Ejemplo: 3 usuarios ($u_1$, $u_2$, $u_3$) y 8 películas (1–8).

| Usuario | Película 1 | Película 2 | Película 3 | Película 4 | Película 5 | Película 6 | Película 7 | Película 8 |
|---------|------------|------------|------------|------------|------------|------------|------------|------------|
| $u_1$   | 5          | 1          | 4          | ?          | ?          | ?          | 2          | 1          |
| $u_2$   | 5          | ?          | 3          | 2          | 5          | ?          | 2          | 1          |
| $u_3$   | 1          | 4          | 2          | 5          | 2          | ?          | 5          | 4          |

Pregunta: Recomendación para $u_1$

Prior: $\bar{r}_4 = \bar{r}_5 = 3.5$

Prior (notación alternativa): $\bar{S}_4 = \bar{S}_5 = 3.5$

Pero, ¿quién es más parecido?

Comparación $u_1$ vs $u_2$ (películas 1, 3, 7, 8): vectores $[5, 4, 2, 1]$ y $[5, 3, 2, 1]$.

Comparación $u_1$ vs $u_3$ (películas 1, 2, 3, 7, 8): vectores $[5, 1, 4, 2, 1]$ y $[1, 4, 2, 5, 4]$.

Similaridad Coseno:

$$Sim(u_i, u_j) = \frac{u_i \cdot u_j}{\|u_i\| \cdot \|u_j\|} = \cos(\theta)$$

$Sim(u_1, u_2) = 0.94$

$Sim(u_1, u_2) = 0.99$ (notas manuscritas)

$Sim(u_1, u_3) = 0.57$

Predicción para la película 4:

$$\hat{r}_{1,4} = \frac{S_{1,2} \cdot 2 + S_{1,3} \cdot 5}{S_{1,2} + S_{1,3}} = 3.1$$

Predicción para la película 5:

$$\hat{r}_{1,5} = \frac{0.94 \cdot 5 + 0.57 \cdot 2}{0.94 + 0.57} = 3.9$$

$$r_{1,5} = 3.9$$

**Figura:** En la parte superior, el título «Filtrado colaborativo» subrayado. Debajo, la frase «Preferencias pasadas dan información de preferencias futuras». A continuación, una tabla o matriz de calificaciones con 3 filas de usuarios ($u_1$, $u_2$, $u_3$) y 8 columnas de películas (numeradas 1 a 8), con valores numéricos de calificación (1–5) y celdas vacías marcadas con «?» para calificaciones desconocidas. En rojo, la pregunta «Pregunta: Recomendación para $u_1$». Se indica un prior $\bar{r}_4 = \bar{r}_5 = 3.5$. En rojo, la pregunta «Pero, ¿quién es más parecido?». Se muestran comparaciones de vectores de calificaciones entre pares de usuarios para los ítems co-calificados. La fórmula de Similaridad Coseno aparece escrita con numerador (producto punto) y denominador (normas). Los resultados $Sim(u_1, u_2) = 0.94$ y $Sim(u_1, u_3) = 0.57$ están calculados y subrayados. Al final, las fórmulas de predicción ponderada por similitud para las películas 4 y 5, con resultados finales **3.1** y **3.9** subrayados respectivamente.

**Figura:** Slide con notas manuscritas en español sobre filtrado colaborativo. Título manuscrito «Filtrado colaborativo». Principio: «Preferencias pasadas dan información de preferencias futuras». Ejemplo: «3 usuarios, 8 películas». Tabla usuario-ítem con filas $u_1$, $u_2$, $u_3$ y columnas numeradas 1 a 8; las calificaciones conocidas están marcadas en verde según la tabla arriba; las celdas vacías son calificaciones faltantes a predecir (películas 4, 5 y 6 para $u_1$). Pregunta central: «Recomendación para $u_1$». Prior/baseline: $\bar{S}_4 = \bar{S}_5 = 3.5$ (promedio simple de calificaciones conocidas para películas 4 y 5). Pregunta: «Pero, ¿Quien es más parecido?». Debajo de la matriz principal, dos sub-tablas de comparación aislan las calificaciones en común entre pares de usuarios. Fórmula de similitud coseno manuscrita con resultados calculados: $Sim(u_1, u_2) = 0.99$ y $Sim(u_1, u_3) = 0.57$. Una flecha verde conecta las tablas de comparación con las fórmulas de predicción. Predicción para película 4: $\bar{r}_{1,4} = \frac{S_{1,2} * 2 + S_{1,3} * 5}{S_{1,2} + S_{1,3}} = 3.1$ (donde 2 y 5 son las calificaciones de $u_2$ y $u_3$ a la película 4). Predicción para película 5: $r_{1,5} = 3.9$ (calculada como $\frac{0.99 * 5 + 0.57 * 2}{0.99 + 0.57} \approx 3.9$).

(slides 20–21)

### Ejemplo en Colab

Ejemplo:

https://colab.research.google.com/drive/1Sx9trUnfVKm1dzLDZidrTWgVXC-cridHy?usp=sharing

**Figura:** En la parte superior izquierda, el encabezado «Ejemplo:» en tipografía sans-serif negra grande y en negrita. En el centro de la slide, un enlace de texto a un notebook de Google Colab: `https://colab.research.google.com/drive/1Sx9trUnfVKm1dzLDZidrTWgVXC-cridHy?usp=sharing` (con salto de línea después de «VXC-»).

(slides 22)

### Problemas con el filtrado colaborativo

Problemas con el filtrado colaborativo

**Figura:** En la parte superior, un banner rectangular de color verde azulado claro con el título centrado «Problemas con el filtrado colaborativo» en tipografía negra negrita. En el lado izquierdo de la slide, una fotografía de un automóvil completamente cubierto por una gruesa capa de hielo, estacionado cerca de un cuerpo de agua en un clima frío, como metáfora visual del problema «cold start». En el lado derecho, un diagrama de matriz usuario-ítem: un grid rectangular donde el eje vertical está etiquetado «Users» (usuarios, representados por íconos de personas de colores en las filas) y el eje horizontal está etiquetado «Movies» (películas, representadas por miniaturas de posters de películas en las columnas). La mayoría de las celdas contienen calificaciones numéricas (valores entre 1 y 5) o están vacías, mostrando una matriz dispersa. Una columna vertical completa está resaltada en color naranja claro y todas sus celdas contienen signos de interrogación «?», representando un ítem nuevo sin calificaciones. Una fila horizontal completa también está resaltada en color naranja claro y todas sus celdas contienen «?», representando un usuario nuevo sin calificaciones. La intersección de la fila y columna resaltadas también muestra «?».

(slides 23)

## Factorización de matrices (SVD)

### SVD: enfoque de factorización de matrices

SVD: Enfoque de Factorización de
Matrices

Descomposición de la matriz de calificaciones $R$ en el producto de $P$ y $Q$.
Cada usuario y cada ítem se describen con $F$ características latentes.

- $P$: factores de usuario
- $Q$: factores de ítem

Predicción del usuario u acerca del item i :

$$p_{u,i} = q_i^T p_u = \sum_{f=1}^{F} q_{i,f} \cdot p_{u,f}$$

**Figura:** Slide con banner verde azulado claro en la parte superior con el título «SVD: Enfoque de Factorización de Matrices». En el lado izquierdo, una matriz de calificaciones («Ratings matrix») representada como un grid: las filas corresponden a usuarios (íconos de personas) y las columnas a películas (miniaturas de posters). Algunas celdas contienen calificaciones numéricas (por ejemplo 1, 2, 4, 5) y muchas celdas están vacías (datos faltantes). En el centro, un diagrama de factorización: la matriz de calificaciones se muestra como aproximadamente igual ($\approx$) al producto de dos matrices rectangulares grises etiquetadas $P$ y $Q$. La matriz $P$ es vertical (alta y estrecha), con altura igual al número de usuarios y ancho etiquetado «$F$ factors». La matriz $Q$ es horizontal (ancha y baja), con ancho igual al número de ítems y altura etiquetada «$F$ factors». En la parte inferior derecha, una matriz completada donde todas las celdas vacías de la matriz original han sido rellenadas con valores numéricos predichos. En la parte inferior, la fórmula de predicción. Número de slide «24» en la esquina inferior derecha.

(slides 24)

### Factorización de una matriz

Matrix - Factorization

Factorización de una matriz:

- Encontrar dos (o más) matrices de manera que al multiplicarlas
   se obtenga la matriz original.

Perspectiva de la aplicación:

- Se puede utilizar para descubrir características latentes que
   subyacen en las interacciones entre dos tipos diferentes de
   entidades.

**Figura:** En la parte superior central, un banner rectangular verde azulado claro con el título centrado «Matrix - Factorization» en tipografía negra negrita. Debajo, dos puntos principales precedidos por íconos de viñeta cuadrados: «Factorización de una matriz:» con un sub-bullet circular, y «Perspectiva de la aplicación:» con un sub-bullet circular. El texto de los bullets está en español, en tipografía sans-serif negra.

(slides 25)

### Definición de P, Q y R

Matrix - Factorization

P: a |U| x K matrix

Q: a |D| x K matrix

R: Tamaño de la matriz |U| x |D| que contiene los ratings que los
usuarios colocaron a los items.

**Figura:** Slide con banner verde azulado claro en la parte superior con el título «Matrix - Factorization». Tres componentes dispuestos horizontalmente de izquierda a derecha: (1) Matriz $R$ (Ratings Matrix): un rectángulo vertical grande con el eje horizontal superior etiquetado «Movies» y el eje vertical izquierdo etiquetado «Users», con la letra «R» en negrita en el centro. (2) Matriz $P$: un rectángulo vertical alto y delgado en el centro con un signo de interrogación «?» en su interior, etiquetado arriba como «P: a |U| x K matrix». (3) Matriz $Q$: un rectángulo horizontal corto y ancho a la derecha con un signo de interrogación «?» en su interior, etiquetado arriba como «Q: a |D| x K matrix» y con la letra «Q» a su derecha. En la parte inferior, el texto descriptivo de $R$.

(slides 26)

### Aproximación de ratings

Matrix - Factorization: Intentamos
                  aproximar los ratings

La matriz de calificaciones se aproxima encontrando dos matrices P y Q de tal manera
que su producto se acerque a R.

**Figura:** Slide con banner verde azulado claro en la parte superior con el título «Matrix - Factorization: Intentamos aproximar los ratings». En el centro, una ecuación visual con tres matrices rectangulares grises: (1) Matriz $R$: rectángulo vertical grande con «R» en negrita en el centro; eje vertical izquierdo etiquetado «Users»; eje horizontal superior etiquetado «Movies». (2) Símbolo de aproximación «$\approx$» a la derecha de $R$. (3) Matriz $P$: rectángulo vertical alto y estrecho con «P» en negrita arriba y un signo de interrogación «?» en el interior. (4) Símbolo de multiplicación «×» entre $P$ y $Q$. (5) Matriz $Q$: rectángulo horizontal corto y ancho con «Q» a su derecha y un signo de interrogación «?» en el interior. En la parte inferior, sobre fondo gris muy claro, la frase descriptiva donde las letras «P», «Q» y «R» aparecen resaltadas en color rojo.

(slides 27)

### Vectores de factores de usuario e ítem

Matrix - Factorization:
Cada usuario & item es caracterizado con un vector de factores.

User-factors vector

$u_1$
$u_2$
$..$
$u_f$

P: Vector que representa la fuerza de las asociaciones entre un usuario y las características.

Item-factors vector

$i_1$
$i_2$
$..$
$i_f$

Q: Vector que representa la fuerza de las asociaciones entre un ítem y las características.

Factors - f: artefacto matemático para calcular la relación

**Figura:** Slide dividida en dos secciones horizontales. Banner verde azulado claro en la parte superior con el título «Matrix - Factorization:» y subtítulo «Cada usuario & item es caracterizado con un vector de factores.» **Sección superior (User-factors):** A la izquierda, un ícono de silueta de persona en gris oscuro. Una flecha apunta desde el ícono hacia un vector columna etiquetado «User-factors vector» con elementos $u_1, u_2, \dots, u_f$. Un recuadro circular azul explica que $P$ es el «Vector que representa la fuerza de las asociaciones entre un usuario y las características». A la derecha, un rectángulo vertical alto y estrecho con la etiqueta «Users» en el lado izquierdo, «$f$» en la parte superior, y la letra «$P$» grande en el interior, representando la matriz de factores de usuario. **Sección inferior (Item-factors):** A la izquierda, un ícono de carrete de película en gris oscuro. Una flecha apunta hacia un vector columna etiquetado «Item-factors vector» con elementos $i_1, i_2, \dots, i_f$. Un recuadro circular azul explica que $Q$ es el «Vector que representa la fuerza de las asociaciones entre un ítem y las características». A la derecha, un rectángulo horizontal corto y ancho con la etiqueta «Movies» en la parte superior y la letra «$Q$» grande en el interior. En la parte inferior, una barra azul con el texto «Factors - $f$: artefacto matemático para calcular la relación». Número de slide «28» en la esquina inferior derecha.

(slides 28)

### Predicción por producto punto de factores

Matrix - Factorization:
        La predicción de la preferencia es el producto punto de los
                        factores de usuario e ítem.

$[0.8,\ 0.7,\ -0.5,\ 1.3] \cdot [0.9,\ 0.8,\ -0.6,\ 1.2] = 3.14$

$[0.8,\ 0.7,\ -0.5,\ 1.3] \cdot [-0.3,\ -0.5,\ 0.2,\ 0] = -0.69$

Factores de ítem: La medida en que un ítem tiene ciertas características.
Factores de usuario: Nivel de preferencia por las características correspondientes.

**Figura:** Slide con banner verde azulado claro en la parte superior con el título «Matrix - Factorization:» y subtítulo «La predicción de la preferencia es el producto punto de los factores de usuario e ítem.» En el centro, dos ejemplos de producto punto mostrados como vectores horizontales: **Primer ejemplo:** vector de usuario $[0.8, 0.7, -0.5, 1.3]$ (con ícono de persona debajo) multiplicado por vector de ítem $[0.9, 0.8, -0.6, 1.2]$ (con ícono de carrete de película debajo), resultado «$= 3.14$» en fuente grande verde. **Segundo ejemplo:** el mismo vector de usuario $[0.8, 0.7, -0.5, 1.3]$ multiplicado por vector de ítem $[-0.3, -0.5, 0.2, 0]$, resultado «$= -0.69$» en fuente grande roja. En la parte inferior, un recuadro azul con las definiciones de «Factores de ítem» y «Factores de usuario». Número de slide «29» en la esquina inferior derecha.

Para obtener la predicción de una calificación de un ítem j por un usuario i, calcular el
producto punto de los dos vectores correspondientes a ui y dj

$$\hat{r}_{ij} = p_i^T q_j = \sum_{k=1}^{k} p_{ik} q_{kj}$$

Entonces ¿cómo calculamos las
matrices P y Q?

**Figura:** Slide con banner verde azulado claro en la parte superior con el título «Matrix - Factorization:» y subtítulo «La predicción de la preferencia es el producto punto de los factores de usuario e ítem.» Texto instructivo donde «ítem j» y «usuario i» aparecen en negrita, y «ui» y «dj» en cursiva. En el centro, la fórmula matemática de predicción $\hat{r}_{ij} = p_i^T q_j = \sum_{k=1}^{k} p_{ik} q_{kj}$. Dos flechas azules apuntan a partes de la fórmula: una hacia $p_{ik}$ etiquetada «Vector correspondiente a $u_i$», otra hacia $q_{kj}$ etiquetada «Vector correspondiente a $d_j$». En la parte inferior izquierda, un recuadro azul claro con la pregunta «Entonces ¿cómo calculamos las matrices P y Q?». A la derecha de la pregunta, un personaje caricaturesco blanco con expresión confundida junto a un signo de interrogación rojo grande. Número de slide «30» en la esquina inferior derecha.

(slides 29–30)

### Obtención de las matrices P y Q

Matrix - Factorization:
         ¿Cómo obtenemos las matrices $P$ y $Q$?

1. Primero inicializamos las matrices con algunos
valores.

2. Calculamos cuán diferente es su producto
respecto a $M$.

3. Tratamos de minimizar esta diferencia de manera iterativa.

¡Por lo tanto, es realmente un problema de minimización!

**Figura:** Slide con banner verde azulado claro en la parte superior con el título «Matrix - Factorization:» y subtítulo «¿Cómo obtenemos las matrices $P$ y $Q$?». Debajo del banner, tres pasos numerados (1, 2, 3) en texto negro plano describiendo el proceso iterativo de inicialización, cálculo de diferencia respecto a $M$, y minimización. En la parte inferior izquierda, un ícono circular rojo con una bombilla amarilla y rayos blancos, seguido del texto en negrita «¡Por lo tanto, es realmente un problema de minimización!». Número de slide «31» en la esquina inferior derecha en gris claro.

(slides 31)

### Minimización y gradient descent

Matrix - Factorization:
                  Solution to our minimization problem

Gradient Descent: Busca encontrar un mínimo local de la
diferencia.

Difference: El error entre la calificación estimada y la
calificación real. Se puede calcular para cada par usuario-
ítem.

$$e_{ij}^2 = (r_{ij} - \hat{r}_{ij})^2 = \left(r_{ij} - \sum_{k=1}^{K} p_{ik} q_{kj}\right)^2$$

Consideramos el error cuadrático porque la calificación estimada puede ser
mayor o menor que la real.

**Figura:** Slide con banner verde azulado claro en la parte superior con el título «Matrix - Factorization: Solution to our minimization problem». Debajo, dos definiciones en texto: «Gradient Descent:» seguido de su descripción en español, y «Difference:» seguido de su descripción en español. En el centro, la fórmula del error cuadrático $e_{ij}^2 = (r_{ij} - \hat{r}_{ij})^2 = \left(r_{ij} - \sum_{k=1}^{K} p_{ik} q_{kj}\right)^2$, donde $e_{ij}^2$ es el error cuadrado para el usuario $i$ e ítem $j$, $r_{ij}$ es la calificación real, $\hat{r}_{ij}$ es la calificación estimada, y $\sum_{k=1}^{K} p_{ik} q_{kj}$ es el producto punto de los vectores de factores latentes. En la parte inferior, un recuadro azul con la nota sobre el error cuadrático. Número de slide «32» en la esquina inferior derecha.

(slides 32)

## Recursos

### Ejemplos y referencias

Ejemplo:

https://colab.research.google.com/drive/1m9LH5kKtE6mtqydwkBLkoLCOV_Ihbr3B?usp=sharing

https://machinelearningmastery.com/using-singular-value-decomposition-to-build-a-recommender-system/

**Figura:** En la parte superior izquierda, el encabezado «Ejemplo:» en tipografía sans-serif negra grande y en negrita. Debajo del encabezado, dos URLs: (1) `https://colab.research.google.com/drive/1m9LH5kKtE6mtqydwkBLkoLCOV_Ihbr3B?usp=sharing` (subrayado), y (2) `https://machinelearningmastery.com/using-singular-value-decomposition-to-build-a-recommender-system/`.

(slides 33)

## Glosario

| Término | Definición |
| --- | --- |
| Sistema de recomendación (SR) | Sistema que proporciona sugerencias de ítems que son más relevantes para un usuario en particular. |
| Feedback explícito | El usuario indica su preferencia por algunos items (p. ej., ratings scales 1–5 o 1–10 estrellas, binary values liked/disliked). |
| Feedback implícito | Los usuarios interactúan con los items (p. ej., histórico de compras, duración de visita, patrones de clicks). |
| Matriz dispersa | La mayoría de los valores son desconocidos. |
| Predicción | La tarea de llenar los valores desconocidos. |
| Filtrado colaborativo (CF) | Inspeccionar patrones de calificación para encontrar usuarios/ítems similares. |
| Content-based (CB) | Analizar atributos de los ítems para construir perfiles de usuario. |
| UBCF | Filtrado colaborativo basado en usuarios; suposición: usuarios similares tienen preferencias similares. |
| IBCF | Filtrado colaborativo basado en ítems; suposición: los usuarios tienen gustos similares para ítems similares. |
| $n_u$ | Número de usuarios. |
| $n_m$ | Número de películas. |
| $r(i, j)$ | Igual a 1 si el usuario $j$ calificó la película $i$. |
| $y^{(i, j)}$ | Calificación dada por el usuario $j$ a la película $i$ (definida solo si $r(i, j) = 1$). |
| $P$ | Factores de usuario; matriz de tamaño $\|U\| \times K$. |
| $Q$ | Factores de ítem; matriz de tamaño $\|D\| \times K$. |
| $R$ | Matriz de tamaño $\|U\| \times \|D\|$ que contiene los ratings que los usuarios colocaron a los items. |
| Factors ($f$) | Artefacto matemático para calcular la relación. |
| Factores de ítem | La medida en que un ítem tiene ciertas características. |
| Factores de usuario | Nivel de preferencia por las características correspondientes. |
| Gradient Descent | Busca encontrar un mínimo local de la diferencia. |
| Difference | El error entre la calificación estimada y la calificación real; se puede calcular para cada par usuario-ítem. |
