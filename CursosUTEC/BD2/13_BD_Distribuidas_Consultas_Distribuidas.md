---
curso: BD2
titulo: 13 BD Distribuidas - Consultas Distribuidas
slides: 74
fuente: 13 BD Distribuidas - Consultas Distribuidas.pdf
---

# 13 BD Distribuidas - Consultas Distribuidas

## Índice

- [Procesamiento de Consultas Distribuidas](#procesamiento-de-consultas-distribuidas)
  - [Visión general](#visión-general)
  - [Pasos generales](#pasos-generales)
- [Descomposición](#descomposición)
  - [Pasos](#pasos)
  - [Normalización Algebraica](#normalización-algebraica)
  - [Eliminación de Redundancias](#eliminación-de-redundancias)
  - [Optimización Sintáctica](#optimización-sintáctica)
- [Localización](#localización)
  - [Pasos](#pasos-1)
  - [Notación para el fragmento](#notación-para-el-fragmento)
  - [Ejemplo 1](#ejemplo-1)
  - [Regla 1](#regla-1)
  - [Ejemplo 2](#ejemplo-2)
  - [Regla 2](#regla-2)
  - [Ejemplo 3](#ejemplo-3)
  - [Ejemplo 4](#ejemplo-4)
  - [Regla 3](#regla-3)
- [Optimización](#optimización)
  - [Proceso de optimización](#proceso-de-optimización)
  - [Diferencias respecto a la optimización centralizada](#diferencias-respecto-a-la-optimización-centralizada)
  - [Ordenación paralela / distribuida](#ordenación-paralela--distribuida)
  - [Join paralelo / distribuido](#join-paralelo--distribuido)
  - [Otras operaciones paralelas](#otras-operaciones-paralelas)
  - [Agregación en Paralelo / Distribuido](#agregación-en-paralelo--distribuido)
  - [Selección en Paralelo / Distribuido](#selección-en-paralelo--distribuido)
- [Glosario](#glosario)

## Procesamiento de Consultas Distribuidas

### Visión general

Consulta de usuario – alto nivel

Procesador de
Consultas

Comandos de manipulación de datos – bajo nivel

**Figura:** Diagrama de flujo vertical centrado en la slide. En la parte superior, el texto «Consulta de usuario – alto nivel». Una flecha descendente conduce a un recuadro gris claro etiquetado «Procesador de Consultas». Debajo del recuadro, un icono de cuatro servidores o computadoras interconectados en una red (bus compartido). Otra flecha descendente conduce al texto «Comandos de manipulación de datos – bajo nivel». El diagrama muestra la transformación de una consulta de alto nivel en comandos de bajo nivel distribuidos sobre una red de servidores.

(slides 3)

### Pasos generales

Pasos Generales:

1. Descomposición
   - Uno o más árboles de consulta algebraica sobre las relaciones.

2. Localización
   - Reemplazo de relaciones por sus fragmentos correspondientes.

3. Optimización
   - Reducir la transmisión de tuplas por la red.

**Figura:** Slide con título «Procesamiento de Consultas Distribuidas» en la parte superior izquierda. Debajo, el subtítulo «Pasos Generales:» seguido de una lista numerada con tres pasos: «Descomposición», «Localización» y «Optimización», cada uno con su viñeta de descripción.

Descomposición
- Uno o más árboles de consulta algebraica sobre las relaciones.

Localización
- Reemplazo de relaciones por sus fragmentos correspondientes.

Optimización
- Reducir la transmisión de tuplas por la red.

**Figura:** Diagrama de flujo vertical con tres recuadros redondeados conectados por flechas naranjas apuntando hacia abajo. El recuadro superior es azul y está etiquetado «Descomposición» con la viñeta «Uno o más árboles de consulta algebraica sobre las relaciones.». El recuadro central es verde claro y está etiquetado «Localización» con la viñeta «Reemplazo de relaciones por sus fragmentos correspondientes.». El recuadro inferior es verde más oscuro y está etiquetado «Optimización» con la viñeta «Reducir la transmisión de tuplas por la red.».

(slides 4–5)

## Descomposición

### Pasos

Pasos:

1. Normalización Algebraica
2. Eliminación de Redundancias
3. Optimización Sintáctica

**Figura:** Slide con título «Descomposición» y subtítulo «Pasos:». Tres flechas horizontales apuntan de izquierda a derecha, cada una con un paso numerado: la flecha azul con «1. Normalización Algebraica», la flecha verde claro con «2. Eliminación de Redundancias», y la flecha verde oscuro con «3. Optimización Sintáctica».

(slides 7)

### Normalización Algebraica

- Normalización Algebraica

  - Convertir del notación SQL a una forma estándar

    Ejemplo:

```sql
select R.A, R.C
from R, S
where R.A = S.A and
      ((R.B = 1 and S.D = 2) or
       (R.C > 3 and S.D = 2))
```

También se debe detectar las expresiones inválidas

**Figura:** La slide muestra la transformación de una consulta SQL a un árbol de álgebra relacional. A la izquierda, el bloque de código SQL del ejemplo. Una flecha horizontal apunta hacia la derecha, donde se representa el árbol de álgebra relacional de arriba hacia abajo: en la raíz, la proyección $\Pi_{R.A, R.C}$; debajo, una selección $\sigma_{(R.B=1 \lor R.C>3) \land S.D=2}$ (la condición simplificada mediante leyes distributivas, con una flecha señalando la expresión lógica simplificada); debajo, un join $\bowtie_A$ sobre el atributo $A$ (derivado de `R.A = S.A`); en las hojas, las relaciones $R$ y $S$. En la parte inferior izquierda, el texto en rojo «También se debe detectar las expresiones inválidas».

(slides 8)

### Eliminación de Redundancias

- Eliminación de Redundancias
  - Por ejemplo: condiciones falsas, condiciones redundantes:

$(S.A = 1) \land (S.A > 5) \Rightarrow \text{false}$

$(S.A < 10) \land (S.A < 5) \Rightarrow S.A < 5$

**Figura:** Slide con título «Descomposición» y viñeta «Eliminación de Redundancias» con sub-viñeta «Por ejemplo: condiciones falsas, condiciones redundantes:». Debajo, dos expresiones lógicas: la primera muestra que $(S.A = 1) \land (S.A > 5)$ implica $\text{false}$; la segunda muestra que $(S.A < 10) \land (S.A < 5)$ se simplifica a $S.A < 5$.

- Eliminación de Redundancias
  - Por ejemplo, cuando comparten sub-expresiones:

**Figura:** Dos árboles de álgebra relacional conectados por una flecha negra horizontal de izquierda a derecha, mostrando la eliminación de sub-expresiones redundantes.

**Árbol izquierdo (antes de la optimización):**
- Raíz: operador de unión ($\cup$).
- Rama izquierda: join natural ($\bowtie$) entre la relación $S$ y el resultado de $\sigma_{cond}$ sobre la relación $R$.
- Rama derecha: join natural ($\bowtie$) entre el resultado de $\sigma_{cond}$ sobre la relación $R$ y la relación $T$.
- La sub-expresión $(\sigma_{cond}\, R)$ aparece duplicada en ambas ramas.

**Árbol derecho (después de la optimización):**
- Raíz: operador de unión ($\cup$).
- Dos joins naturales ($\bowtie$) como hijos de la unión: el join izquierdo conecta a $S$ y el join derecho conecta a $T$.
- Ambos joins apuntan a una **única instancia** compartida de la sub-expresión $\sigma_{cond}$ sobre $R$, formando un grafo acíclico dirigido (DAG) en lugar de un árbol simple.

(slides 9–10)

### Optimización Sintáctica

- Optimización Sintáctica
  - Llevar las condiciones y proyecciones lo más abajo posible.

**Figura:** Dos árboles de álgebra relacional conectados por una flecha negra horizontal de izquierda a derecha, mostrando el empuje de selecciones hacia abajo.

**Árbol izquierdo (antes de la optimización):**
- Raíz: selección $\sigma_{cond}$.
- Debajo: join natural ($\bowtie$) entre las relaciones $R$ y $S$.
- La condición de filtrado se aplica después del join.

**Árbol derecho (después de la optimización):**
- Raíz: selección $\sigma_{cond3}$ (condiciones restantes que solo pueden evaluarse tras el join).
- Debajo: join natural ($\bowtie$) entre los resultados filtrados.
- Sobre la relación $R$: selección $\sigma_{cond1}$.
- Sobre la relación $S$: selección $\sigma_{cond2}$.
- Las selecciones se empujan lo más abajo posible, filtrando cada relación antes del join.

(slides 11)

## Localización

### Pasos

- Pasos:

  - Comenzar con una consulta.
  - Reemplazar relaciones por fragmentos.
  - Empujar $\cup$ hacia arriba, y $\sigma$, $\pi$ hacia abajo.
  - Simplificar/Eliminar operaciones innecesarias.

**Figura:** Diagrama de flujo con cuatro recuadros conectados en forma de U (de arriba-izquierda a arriba-derecha, luego abajo-izquierda y abajo-derecha):

1. **Recuadro azul claro (arriba-izquierda):** «Comenzar con una consulta.»
2. **Recuadro verde azulado (arriba-derecha):** «Reemplazar relaciones por fragmentos.»
3. **Recuadro verde medio (abajo-izquierda):** «Empujar $\cup$ hacia arriba, y $\sigma$, $\pi$ hacia abajo»
4. **Recuadro verde oliva claro (abajo-derecha):** «Simplificar/Eliminar operaciones innecesarias.»

Flechas conectan los recuadros en secuencia: 1 → 2 → 3 → 4.

(slides 13)

### Notación para el fragmento

- Notación para el fragmento:

$[R : \text{cond}]$

Fragmento

Condiciones que satisfacen sus tuplas

**Figura:** En el centro de la slide aparece la notación formal $[R : \text{cond}]$ en fuente monoespaciada. Una flecha descendente desde la letra «$R$» apunta al texto «Fragmento». Una flecha en forma de L desde la porción «$\text{cond}$» apunta hacia la derecha al texto «Condiciones que satisfacen sus tuplas».

(slides 14)

### Ejemplo 1

- Ejemplo 1:

  - Sea la consulta:

```sql
SELECT * FROM R WHERE R.E = 3
```

  - Y R está compuesto por los fragmentos

$\{ [R_1: E < 10]\ , [R_2: E \ge 10] \}$

**Figura:** Slide con título «Localización» y viñeta «Ejemplo 1:». Muestra la consulta SQL `SELECT * FROM R WHERE R.E = 3` y la definición de fragmentación horizontal de la relación $R$ en dos fragmentos: $[R_1: E < 10]$ (tuplas con $E$ menor que 10) y $[R_2: E \ge 10]$ (tuplas con $E$ mayor o igual a 10).

- Ejemplo 1:

**Figura:** Dos árboles de álgebra relacional conectados por una flecha negra horizontal de izquierda a derecha, mostrando el reemplazo de la relación global por sus fragmentos.

**Árbol izquierdo (consulta global):**
- Raíz: selección $\sigma_{E=3}$.
- Hoja: relación $R$.

**Árbol derecho (consulta localizada):**
- Raíz: selección $\sigma_{E=3}$.
- Debajo: operador de unión ($\cup$).
- Hoja izquierda: fragmento $[R_1: E < 10]$.
- Hoja derecha: fragmento $[R_2: E \ge 10]$.

La flecha indica que la relación global $R$ se reemplaza por la unión de sus fragmentos horizontales.

- Ejemplo 1:

**Figura:** Dos árboles de álgebra relacional conectados por una flecha negra horizontal de izquierda a derecha, mostrando la distribución de la selección sobre la unión.

**Árbol izquierdo:**
- Raíz: selección $\sigma_{E=3}$.
- Debajo: operador de unión ($\cup$).
- Hoja izquierda: fragmento $[R_1: E < 10]$.
- Hoja derecha: fragmento $[R_2: E \ge 10]$.
- Representa: $\sigma_{E=3}(R_1 \cup R_2)$.

**Árbol derecho:**
- Raíz: operador de unión ($\cup$).
- Rama izquierda: selección $\sigma_{E=3}$ sobre el fragmento $[R_1: E < 10]$.
- Rama derecha: selección $\sigma_{E=3}$ sobre el fragmento $[R_2: E \ge 10]$.
- Representa: $(\sigma_{E=3}\, R_1) \cup (\sigma_{E=3}\, R_2)$.

La transformación aplica la regla algebraica $\sigma_P(R \cup S) \equiv \sigma_P(R) \cup \sigma_P(S)$.

- Ejemplo 1:

**Figura:** Tres elementos conectados por flechas, mostrando la poda de un fragmento innecesario.

**Elemento izquierdo (árbol con poda):**
- Raíz: operador de unión ($\cup$).
- Rama izquierda: selección $\sigma_{E=3}$ sobre el fragmento $[R_1: E < 10]$.
- Rama derecha (circulada en rojo): selección $\sigma_{E=3}$ sobre el fragmento $[R_2: E \ge 10]$.

**Elemento central:**
- Flecha doble roja ($\Rightarrow$) desde la rama circulada hacia el símbolo de conjunto vacío ($\emptyset$), indicando que la rama derecha se elimina porque la condición $E=3$ es contradictoria con el predicado del fragmento $E \ge 10$.

**Elemento derecho (resultado simplificado):**
- Árbol reducido a una sola operación: selección $\sigma_{E=3}$ sobre el fragmento $[R_1: E < 10]$.

- Ejemplo 1:

$$\sigma_{E=3}\,[R_2: E \ge 10]$$

$$\Rightarrow \sigma_{E=3}\,[R_2: E=3 \land E \ge 10]$$

$$\Rightarrow \sigma_{E=3}\,[R_2: \text{false}]$$

$$\Rightarrow \emptyset$$

**Figura:** Slide con título «Localización» y viñeta «Ejemplo 1:». Muestra una derivación paso a paso en cuatro líneas: (1) selección $\sigma_{E=3}$ sobre el fragmento $[R_2: E \ge 10]$; (2) combinación de la condición de selección con el predicado del fragmento: $E=3 \land E \ge 10$; (3) simplificación a condición $\text{false}$ porque $E=3$ y $E \ge 10$ son mutuamente excluyentes; (4) resultado final $\emptyset$ (conjunto vacío), demostrando que el fragmento $R_2$ no necesita ser escaneado para esta consulta.

(slides 15–18, 20)

### Regla 1

- Regla 1:

$$\sigma_{c1}\,[R: c2] \Rightarrow \sigma_{c1}\,[R: c1 \land c2]$$

$$[R: \text{false}] \Rightarrow \emptyset$$

**Figura:** Slide con título «Localización» y viñeta «Regla 1:». Muestra dos fórmulas de álgebra relacional: la primera indica que una selección con condición $c1$ sobre un fragmento $[R: c2]$ se transforma en $\sigma_{c1}\,[R: c1 \land c2]$ (combinando ambas condiciones con $\land$); la segunda indica que un fragmento con condición falsa $[R: \text{false}]$ produce el conjunto vacío $\emptyset$.

(slides 19)

### Ejemplo 2

- Ejemplo 2:

Sea la consulta:

```sql
SELECT * FROM R JOIN S ON R.A = S.A
```

**Figura:** Árbol de álgebra relacional con el operador de join ($\bowtie$) en la raíz, con la letra $A$ debajo del símbolo indicando el atributo de join. Dos ramas descienden desde el join: la rama izquierda conduce a la relación $R$ y la rama derecha conduce a la relación $S$. A la derecha del diagrama aparece la anotación: $A$ = atributo en común.

- Ejemplo 2:

**Figura:** Árbol de álgebra relacional que muestra la localización de la consulta con fragmentación horizontal en $R$ y $S$. En la raíz está el operador de join ($\bowtie_A$). Debajo, dos ramas conducen a operadores de unión ($\cup$):

- **Fragmentación en R** (rama izquierda): el operador $\cup$ tiene tres fragmentos como hojas:
  - $[R_1: A < 5]$
  - $[R_2: 5 \le A \le 10]$
  - $[R_3: A > 10]$

- **Fragmentación en S** (rama derecha): el operador $\cup$ tiene dos fragmentos como hojas:
  - $[S_1: A < 5]$
  - $[S_2: A \ge 5]$

- Ejemplo 2:

**Figura:** Árbol de álgebra relacional con el operador de unión ($\cup$) en la raíz. Seis ramas descienden hacia seis operadores de join ($\bowtie_A$), agrupados en tres pares dentro de recuadros azules:

1. **Grupo izquierdo** (fragmentos de $R_1$):
   - $[R_1: A < 5] \bowtie_A [S_1: A < 5]$
   - $[R_1: A < 5] \bowtie_A [S_2: A \ge 5]$

2. **Grupo central** (fragmentos de $R_2$):
   - $[R_2: 5 \le A \le 10] \bowtie_A [S_1: A < 5]$
   - $[R_2: 5 \le A \le 10] \bowtie_A [S_2: A \ge 5]$

3. **Grupo derecho** (fragmentos de $R_3$):
   - $[R_3: A > 10] \bowtie_A [S_1: A < 5]$
   - $[R_3: A > 10] \bowtie_A [S_2: A \ge 5]$

Cada join tiene dos hojas: un fragmento de $R$ (con su predicado de selección) y un fragmento de $S$ (con su predicado de selección).

- Ejemplo 2:

**Figura:** Mismo árbol de la slide anterior con el operador de unión ($\cup$) en la raíz y seis joins ($\bowtie_A$) debajo. Tres de los seis joins están tachados con una gran X roja, indicando que se eliminan por predicados contradictorios:

- **No tachado:** $[R_1: A < 5] \bowtie_A [S_1: A < 5]$
- **Tachado con X roja:** $[R_1: A < 5] \bowtie_A [S_2: A \ge 5]$
- **Tachado con X roja:** $[R_2: 5 \le A \le 10] \bowtie_A [S_1: A < 5]$
- **No tachado:** $[R_2: 5 \le A \le 10] \bowtie_A [S_2: A \ge 5]$
- **Tachado con X roja:** $[R_3: A > 10] \bowtie_A [S_1: A < 5]$
- **No tachado:** $[R_3: A > 10] \bowtie_A [S_2: A \ge 5]$

- Ejemplo 2:

**Figura:** Árbol de álgebra relacional optimizado. En la raíz está el operador de unión ($\cup$) con tres ramas, cada una con un join ($\bowtie_A$) y dos fragmentos como hojas:

1. **Subárbol izquierdo:** $[R_1: A < 5] \bowtie_A [S_1: A < 5]$
2. **Subárbol central:** $[R_2: 5 \le A \le 10] \bowtie_A [S_2: A \ge 5]$
3. **Subárbol derecho:** $[R_3: A > 10] \bowtie_A [S_2: A \ge 5]$

- Ejemplo 2:

$$[R_1: A < 5] \bowtie_A [S_2: A \ge 5]$$

$$\Rightarrow [R_1 \bowtie_A S_2: R_1.A < 5 \land S_2.A \ge 5 \land R_1.A = S_2.A]$$

$$\Rightarrow [R_1 \bowtie_A S_2: \text{false}]$$

(slides 21–25, 27)

### Regla 2

- Regla 2:

$$[R: c_1] \bowtie_A [S: c_2] \Rightarrow [R \bowtie_A S: c_1 \land c_2 \land R.A = S.A]$$

$$[R: \text{false}] \Rightarrow \emptyset$$

(slides 26)

### Ejemplo 3

Sea la consulta:

```sql
SELECT * FROM R, S WHERE R.K = S.K
```

- Ejemplo 3:

**Figura:** Árbol de álgebra relacional con el operador de join ($\bowtie_K$) en la raíz. Dos ramas descienden hacia operadores de unión ($\cup$):

- **Rama izquierda (relación $R$):** el operador $\cup$ tiene dos fragmentos:
  - $[R_1: A < 10]$
  - $[R_2: A \ge 10]$

- **Rama derecha (relación $S$):** el operador $\cup$ tiene dos fragmentos:
  - $[S_1: K = R.K \land R.A < 10]$
  - $[S_2: K = R.K \land R.A \ge 10]$

Sea la consulta:

```sql
SELECT * FROM R, S WHERE R.K = S.K
```

- Ejemplo 3:

**Figura:** Mismo árbol de álgebra relacional de la slide anterior: join ($\bowtie_K$) en la raíz, con dos uniones ($\cup$) debajo. La rama izquierda tiene fragmentos $[R_1: A < 10]$ y $[R_2: A \ge 10]$. La rama derecha tiene fragmentos $[S_1: K = R.K \land R.A < 10]$ y $[S_2: K = R.K \land R.A \ge 10]$.

**Fragmentación Derivada**

- $S_1 : S \text{ sj}_K R_1$
- $S_2 : S \text{ sj}_K R_2$

- Ejemplo 3:

**Figura:** Árbol de álgebra relacional con el operador de unión ($\cup$) en la raíz. Cuatro ramas descienden hacia cuatro operadores de join ($\bowtie_K$), cada uno con dos fragmentos como hojas:

1. $[R_1] \bowtie_K [S_1]$
2. $[R_1] \bowtie_K [S_2]$
3. $[R_2] \bowtie_K [S_1]$
4. $[R_2] \bowtie_K [S_2]$

- Ejemplo 3:

**Figura:** Mismo árbol de la slide anterior con el operador de unión ($\cup$) en la raíz y cuatro joins ($\bowtie_K$) debajo. Dos de los cuatro joins están tachados con una gran X roja:

- **No tachado:** $[R_1] \bowtie_K [S_1]$
- **Tachado con X roja:** $[R_1] \bowtie_K [S_2]$
- **Tachado con X roja:** $[R_2] \bowtie_K [S_1]$
- **No tachado:** $[R_2] \bowtie_K [S_2]$

- Ejemplo 3:

$$[R_1: A < 10] \bowtie_K [S_2: K = R.K \land R.A \ge 10]$$

$$\Rightarrow [R_1 \bowtie_K S_2: R_1.A < 10 \land S_2.K = R.K \land R.A \ge 10 \land R_1.K = S_2.K]$$

$$\Rightarrow [R_1 \bowtie_K S_2: \text{false}]$$

$$\Rightarrow \emptyset$$

(slides 28–32)

### Ejemplo 4

- Ejemplo 4:

- Sea la consulta:

```sql
SELECT A FROM R
```

Y R está compuesto por los fragmentos

$$\{ R_1(K, A, B),\; R_2(K, C, D) \}$$

- Ejemplo 4:

**Figura:** Diagrama de transformación de consulta con fragmentación vertical. A la izquierda, un árbol simple con el operador de proyección $\Pi_A$ en la raíz conectado a la relación $R$ como hoja. Una flecha horizontal negra apunta hacia la derecha. A la derecha, el árbol localizado muestra $\Pi_A$ en la raíz, conectado a un join ($\bowtie_K$) en el nivel intermedio, con dos hojas: $R_1(K, A, B)$ a la izquierda y $R_2(K, C, D)$ a la derecha. Debajo del diagrama derecho aparece el texto «Fragmentación Vertical».

- Ejemplo 4:

**Figura:** Diagrama de optimización con flecha de transformación de izquierda a derecha.

- **Árbol izquierdo (inicial):** $\Pi_A$ en la raíz, $\bowtie_K$ en el nivel intermedio, con hojas $R_1(K, A, B)$ y $R_2(K, C, D)$.

- **Árbol derecho (optimizado):** $\Pi_A$ en la raíz, $\bowtie_K$ en el nivel intermedio. La rama izquierda tiene $\Pi_{K,A}$ sobre $R_1(K, A, B)$. La rama derecha tiene $\Pi_{K,A}$ sobre $R_2(K, C, D)$.

- Ejemplo 4:

**Figura:** Árbol de álgebra relacional simplificado con el operador de proyección $\Pi_A$ en la raíz, conectado directamente a la hoja $R_1$ con esquema $(K, A, B)$.

(slides 33–36)

### Regla 3

- Regla 3:

- Considerando la fragmentación vertical

$$R_i = \Pi_{A_i}(R),\; A_i \subseteq A$$

- Entonces, para algún $B \subseteq A$

$$\Pi_B(R) = \Pi_B\left(\bowtie_i R_i \mid B \cap A_i \neq \emptyset\right)$$

(slides 37)

## Optimización

### Proceso de optimización

- Proceso de optimización

1. Generar planes de consulta.

2. Estimar el tamaño de los resultados intermedios.

3. Estimar el costo del plan

**Figura:** Diagrama a la derecha del texto que ilustra el proceso de optimización. En la fila superior, una serie horizontal de puntos etiquetados $P_1, P_2, P_3, \ldots, P_n$ (planes de consulta). Cada plan está conectado por una línea vertical punteada a un costo correspondiente en la fila inferior: $C_1, C_2, C_3, \ldots, C_n$. Debajo de los costos, un corchete horizontal grande abarca desde $C_1$ hasta $C_n$ con la etiqueta «4. Elegir el mínimo».

(slides 39)

### Diferencias respecto a la optimización centralizada

- Diferencias respecto a la optimización centralizada.

- Nuevas estrategias para algunas operaciones.

  - Ordenación paralela / distribuida

  - Join paralelo / distribuido

  - Eliminación de duplicados

  - Agregación

  - Selección

- Muchas formas de asignar y programar procesadores.

(slides 40, 73)

### Ordenación paralela / distribuida

- Casos de entrada:

     a)   La relación R en un solo sitio /disco

     b)   La relación R fragmentado por el atributo de ordenación

     c)   La relación R fragmentado por otro atributo

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Optimización: Ordenación paralela / distribuida» aparece en la parte superior en texto grande (la palabra «Optimización:» en gris oscuro y «Ordenación paralela / distribuida» en gris claro). Debajo, un bullet principal «Casos de entrada:» en negrita, seguido de tres sub-items etiquetados a), b) y c) con sus respectivas descripciones.

- Casos de salida:

     a)   La relación R ordenado en un solo sitio /disco
     b)   Fragmentos ordenados de R

**Figura:** A la derecha del item b), se muestran tres fragmentos ordenados de R, etiquetados $F_1$, $F_2$ y $F_3$. Cada fragmento se representa como una tabla con dos columnas: la primera columna está etiquetada «k» y la segunda columna muestra «...» (indicando otros atributos). Los valores en la columna k de cada fragmento son:

- **$F_1$:** 5, 6, 10 (ordenados de menor a mayor)
- **$F_2$:** 12, 15 (ordenados de menor a mayor)
- **$F_3$:** 19, 20, 21, 50 (ordenados de menor a mayor)

Los tres fragmentos están dispuestos horizontalmente de izquierda a derecha, ilustrando que cada fragmento está internamente ordenado y que los rangos de valores son disjuntos y crecientes entre fragmentos ($F_1 < F_2 < F_3$).

- Caso b) R fragmentado por el atributo de ordenación:

     -   R(k, …) para ser ordenado en k.   Select * from R order by k
     -   R esta fragmentado horizontalmente en k usando el vector [k0, k1, …., kn]

**Figura:** Diagrama de fragmentación horizontal de R por el atributo k. Se muestran tres fragmentos (cajas rectangulares) dispuestos horizontalmente de izquierda a derecha, separados por puntos de partición representados como círculos:

- **Fragmento izquierdo:** contiene los valores 7 y 3 (sin ordenar internamente).
- **Punto de partición $k_0$:** círculo con el valor 10.
- **Fragmento central:** contiene los valores 11, 17 y 14 (sin ordenar internamente).
- **Punto de partición $k_1$:** círculo con el valor 20.
- **Fragmento derecho:** contiene los valores 27 y 22 (sin ordenar internamente).

La consulta SQL `Select * from R order by k` aparece en la esquina superior derecha.

- Caso b) R fragmentado por el atributo de ordenación:

     -   Algoritmo:
          1.   Ordenar cada fragmento de forma independiente
          2.   Enviar los resultados si es necesario

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Optimización: Ordenación paralela / distribuida» aparece en la parte superior. Debajo, el encabezado «Caso b) R fragmentado por el atributo de ordenación:» en negrita, seguido del sub-bullet «Algoritmo:» con dos pasos numerados (1 y 2).

- Caso c) R fragmentado por otro atributo :

     -   R(k, …) para ser ordenado en k.   Select * from R order by k
     -   R ubicado en uno o más sitios, no esta fragmentado en K

**Figura:** En el centro de la slide se muestran dos cajas cuadradas apiladas verticalmente, etiquetadas $R_a$ (arriba) y $R_b$ (abajo), representando dos fragmentos de la relación R alojados en sitios distintos (sitio a y sitio b). La consulta SQL `Select * from R order by k` aparece a la derecha del primer bullet.

- Caso c) R fragmentado por otro atributo :
                                                       Select * from R order by k
     -   Algoritmo
          1.   Fragmentación intermedia en k

          2.   Ordenación básica en cada fragmento intermedio

**Figura:** Diagrama de flujo del algoritmo de ordenación cuando R está fragmentado por otro atributo. De izquierda a derecha:

1. **Entrada (izquierda):** dos fragmentos fuente $R_a$ y $R_b$ (cajas cuadradas apiladas verticalmente).
2. **Fragmentación intermedia (centro-izquierda):** flechas sólidas desde $R_a$ y $R_b$ hacia tres fragmentos intermedios $R_1$, $R_2$ y $R_3$ (cajas apiladas verticalmente). Entre $R_1$ y $R_2$ hay un círculo con $k_0$; entre $R_2$ y $R_3$ hay un círculo con $k_1$, indicando los límites de rango de la partición por k.
3. **Ordenación local (centro-derecha):** flechas etiquetadas «local sort» desde cada $R_i$ hacia $R'_i$ (i = 1, 2, 3).
4. **Resultado (derecha):** flechas punteadas desde $R'_1$, $R'_2$ y $R'_3$ convergen hacia un bloque final etiquetado «result».

La consulta SQL `Select * from R order by k` aparece en la esquina superior derecha.

- Vector de partición:

     -   Problema:
          -   Seleccione un buen vector de partición dado los fragmentos:

**Figura:** Tres fragmentos de datos, etiquetados $R_a$, $R_b$ y $R_c$, cada uno representado como una tabla con dos columnas (la primera columna contiene valores numéricos y la segunda columna muestra «...» en la primera fila, indicando otros atributos). Los valores en la primera columna de cada fragmento son:

- **$R_a$:** 7, 52, 11, 14 (4 tuplas)
- **$R_b$:** 31, 8, 15, 11, 32, 17 (6 tuplas)
- **$R_c$:** 10, 12, 4 (3 tuplas)

Los tres fragmentos están dispuestos horizontalmente de izquierda a derecha.

- Vector de partición:
     -   Estrategia:
          -   Cada sitio envía al coordinador
               -   MIN valor de k
               -   MAX valor de k
               -   Número de tuplas
          -   Coordinador
               -   Calcula el vector y distribuye a los sitios.
               -   Decide el número de sitios para realizar las ordenaciones
                   locales.

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Optimización: Ordenación paralela / distribuida» aparece en la parte superior. Debajo, el encabezado «Vector de partición:» con sub-bullet «Estrategia:» que contiene dos sub-secciones con bullets cuadrados: «Cada sitio envía al coordinador» (con tres sub-items circulares: MIN valor de k, MAX valor de k, Número de tuplas) y «Coordinador» (con dos sub-items circulares: Calcula el vector y distribuye a los sitios; Decide el número de sitios para realizar las ordenaciones locales).

- Vector de partición:
     -   Ejemplo:
          -   El coordinador recibe:
                                                      # tuplas = 10
                                                      # tuplas = 10
          -   Tuplas esperadas

                                       Asumiendo que queremos ordenar en dos sitios

**Figura:** Diagrama del ejemplo de cálculo del vector de partición. El coordinador recibe estadísticas de dos sitios:

- **$S_A$:** $MIN = 5$, $MAX = 9$, $\# \text{ tuplas} = 10$
- **$S_B$:** $MIN = 7$, $MAX = 16$, $\# \text{ tuplas} = 10$

Debajo, bajo el encabezado «Tuplas esperadas», se muestra una recta numérica horizontal con marcas del 5 al 20. Sobre la recta hay dos barras horizontales que representan los rangos de datos:

- **Barra superior:** cubre el intervalo $[5, 9]$ (correspondiente a $S_A$), con la etiqueta «2» a la derecha, indicando densidad de 2 tuplas por unidad de rango: $2 = 10 / (9 - 5 + 1)$.
- **Barra inferior:** cubre el intervalo $[7, 16]$ (correspondiente a $S_B$), con la etiqueta «1» a la derecha, indicando densidad de 1 tupla por unidad de rango: $1 = 10 / (16 - 7 + 1)$.

Una flecha apunta a un valor en la recta numérica etiquetado «$k_0?$», ubicado entre 7 y 10. Debajo del diagrama aparece el texto «Asumiendo que queremos ordenar en dos sitios».

- Vector de partición:
     -   Ejemplo:
          -   Tuplas esperadas

          -   Tuplas esperadas con clave < k0 = la mitad de las tuplas totales

**Figura:** Continuación del ejemplo de cálculo del vector de partición. Se muestra la misma recta numérica horizontal (valores del 5 al 20) con las dos barras de densidad:

- **Barra superior:** intervalo $[5, 9]$, densidad = 2.
- **Barra inferior:** intervalo $[7, 16]$, densidad = 1.

Una flecha apunta al valor «$k_0?$» en la recta numérica, ubicado en el valor 9.

Debajo del diagrama, las ecuaciones para calcular $k_0$:

$$2(k_0 - 5) + (k_0 - 7) = 10$$

$$3k_0 - 10 - 7 = 10$$

$$k_0 = (10 + 10 + 7) / 3 = 9$$

- Vector de partición:

     -   Variantes

         Herodotos Herodotou, Nedyalko Borisov, and Shivnath Babu. 2011. Query optimization
         techniques for partitioned tables. In Proceedings of the 2011 ACM SIGMOD International
         Conference on Management of data (SIGMOD '11). ACM, New York, NY, USA

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Optimización: Ordenación paralela / distribuida» aparece en la parte superior. Debajo, el encabezado «Vector de partición:» con sub-bullet «Variantes» y la referencia bibliográfica completa de Herodotou, Borisov y Babu (2011).

- Ordenación usando Merge:

    -   Primero se ordena localmente, y luego se mezclan en una fragmentación intermedia en K.

**Figura:** Diagrama de flujo del algoritmo de ordenación usando Merge. De izquierda a derecha:

1. **Entrada (izquierda):** dos fragmentos $R_a$ y $R_b$ (cajas cuadradas apiladas verticalmente).
2. **Ordenación local:** flechas etiquetadas «local sort» desde $R_a$ y $R_b$ hacia $R'_a$ y $R'_b$ respectivamente.
3. **Merge y redistribución (centro):** múltiples flechas cruzadas desde $R'_a$ y $R'_b$ hacia una columna vertical de tres bloques $R'_1$, $R'_2$ y $R'_3$. Entre $R'_1$ y $R'_2$ hay un círculo con $k_0$; entre $R'_2$ y $R'_3$ hay un círculo con $k_1$. Una flecha etiquetada «in order» apunta hacia la transición de los bloques localmente ordenados a la columna de merge. Una flecha etiquetada «merge» apunta directamente a la columna $R'_1$, $R'_2$, $R'_3$.
4. **Resultado (derecha):** flechas punteadas desde $R'_1$, $R'_2$ y $R'_3$ convergen hacia un bloque final etiquetado «result».

(slides 41–52)

### Join paralelo / distribuido

- Entrada:

     -   Relaciones R y S

     -   Podrían o no estar fragmentados

- Salida:

     -   $R \bowtie S$

     -   El resultado es alojado en uno o más sitios

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Optimización: Join paralelo / distribuido» aparece en la parte superior. Debajo, dos secciones principales con bullets: «Entrada:» (con dos sub-items: Relaciones R y S; Podrían o no estar fragmentados) y «Salida:» (con dos sub-items: $R \bowtie S$; El resultado es alojado en uno o más sitios).

- Join particionado (Equijoin):
                                       Select * from R join S on R.k = S.k

                  k0              k0

                  k1              k1

        $f(k)$

                                       $f(k)$

**Figura:** Diagrama de flujo del Join particionado (Equijoin). La consulta SQL `Select * from R join S on R.k = S.k` aparece en la esquina superior derecha.

De izquierda a derecha:

1. **Estado inicial (particiones fuente):**
   - **Lado izquierdo:** relación R distribuida en dos nodos $R_A$ y $R_B$ (cajas apiladas verticalmente).
   - **Lado derecho:** relación S distribuida en tres nodos $S_A$, $S_B$ y $S_C$ (cajas apiladas verticalmente).

2. **Fase de redistribución ($f(k)$):** flechas punteadas desde las particiones fuente ($R_A$, $R_B$, $S_A$, $S_B$, $S_C$) hacia el área central de procesamiento, etiquetadas con $f(k)$ (función de partición aplicada al atributo de join k).

3. **Estado particionado intermedio (centro):** tres nodos de destino para R ($R_1$, $R_2$, $R_3$) y tres nodos de destino para S ($S_1$, $S_2$, $S_3$), apilados verticalmente y alineados. Debajo de los pares correspondientes aparecen etiquetas $k_0$ y $k_1$ indicando rangos o buckets de la clave de join.

4. **Fase de join local:** barras horizontales de doble línea conectan $R_1$ con $S_1$, $R_2$ con $S_2$, y $R_3$ con $S_3$. Una etiqueta «local join» aparece sobre la barra superior.

5. **Agregación de resultados:** flechas verticales descendentes desde cada «local join» convergen hacia una etiqueta central en la parte inferior: «result».

- Join particionado (Equijoin):

     -   Se utiliza la misma función de partición $f$ para R y S

     -   $f$ puede ser partición por rango o por hash

     -   El join local puede ser de cualquier tipo (cs2701)

     -   Varias opciones de programación, por ejemplo:

          a)   Particionar R; particionar S; ordenar y join

          b)   Particionar R; construir tablas hash locales para R;
               particionar S; join.

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Optimización: Join paralelo / distribuido» aparece en la parte superior. Debajo, el encabezado «Join particionado (Equijoin):» con cuatro sub-bullets circulares que describen la función de partición $f$, los tipos de partición (rango o hash), el tipo de join local (cs2701), y dos opciones de programación (a y b).

- Join particionado (Equijoin):

     -   Ya sabemos por qué funciona.

     o A veces particionamos solo para hacer posible este join

**Figura:** Diagrama de transformación de álgebra relacional que ilustra por qué funciona el join particionado. Una flecha apunta de izquierda a derecha:

- **Árbol izquierdo (antes de la optimización):** en la raíz hay un operador de join ($\bowtie$). Dos ramas descienden hacia operadores de unión ($\cup$):
  - Unión izquierda combina tres particiones: $[R_1]$, $[R_2]$, $[R_3]$.
  - Unión derecha combina tres particiones: $[S_1]$, $[S_2]$, $[S_3]$.
  - Esto representa un join realizado después de reunir todas las particiones de R y S.

- **Árbol derecho (después de la optimización):** en la raíz hay un operador de unión ($\cup$) con tres ramas, cada una con un operador de join ($\bowtie$):
  - $[R_1] \bowtie [S_1]$
  - $[R_2] \bowtie [S_2]$
  - $[R_3] \bowtie [S_3]$
  - Esto demuestra que el join se «empuja» a través de la unión: en lugar de un join grande, se realizan múltiples joins más pequeños en particiones correspondientes y sus resultados se unen.

- Join particionado (Equijoin):

     -   Seleccionar una buena función de partición $f$ es muy importante.

     -   El objetivo es hacer todo $| R_i | + | S_i |$ el mismo tamaño.

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Optimización: Join paralelo / distribuido» aparece en la parte superior. Debajo, el encabezado «Join particionado (Equijoin):» con dos sub-bullets circulares: la importancia de seleccionar una buena función de partición $f$, y el objetivo de hacer que todas las sumas $| R_i | + | S_i |$ tengan el mismo tamaño.

(slides 53–57)

### Otras operaciones paralelas

- Eliminación de duplicados                         Select distinct k from R

     -   [Opción 1] Fragmentación intermedia en k (rango o hash), eliminar
         localmente o eliminar en el merge.

     -   [Opción 2] Ordenar primero (en paralelo) luego eliminar duplicados en
         el resultado.

- Agregación

     -   Partición por el atributo de agrupación.

     -   Calcular la función de agregación localmente.

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Optimización: Otras operaciones paralelas» aparece en la parte superior. Debajo, dos secciones principales: «Eliminación de duplicados» (con la consulta SQL `Select distinct k from R` a la derecha, y dos opciones de procesamiento paralelo) y «Agregación» (con dos sub-bullets sobre partición por atributo de agrupación y cálculo local de la función de agregación).

(slides 58)

### Agregación en Paralelo / Distribuido

**Figura:** Dos tablas que representan fragmentos de la relación R distribuida en dos sitios:

**Tabla $R_a$:**

| id | dept | salary |
|----|------|--------|
| 1  | toy  | 10     |
| 2  | toy  | 20     |
| 3  | sales| 15     |

**Tabla $R_b$:**

| id | dept | salary |
|----|------|--------|
| 4  | sales| 5      |
| 5  | toy  | 20     |
| 6  | mgmt | 15     |
| 7  | sales| 10     |
| 8  | mgmt | 30     |

En la parte inferior de la slide aparece la consulta SQL:

```sql
select dept, sum (sal) from R group by dept
```

**Figura:** Diagrama de flujo de agregación paralela/distribuida que muestra la redistribución de datos por el atributo de agrupación `dept`. De izquierda a derecha:

1. **Tablas de entrada (izquierda):**
   - **$R_a$:** id=1 (toy, 10), id=2 (toy, 20), id=3 (sales, 15)
   - **$R_b$:** id=4 (sales, 5), id=5 (toy, 20), id=6 (mgmt, 15), id=7 (sales, 10), id=8 (mgmt, 30)

2. **Redistribución (centro):** flechas indican que los datos se redistribuyen según la columna `dept` (clave de GROUP BY):
   - Filas con `dept = 'toy'` y `dept = 'mgmt'` se envían al nodo superior derecho.
   - Filas con `dept = 'sales'` se envían al nodo inferior derecho.

3. **Tablas de destino (derecha):**
   - **Nodo superior** (procesa 'toy' y 'mgmt'): (1, toy, 10), (2, toy, 20), (5, toy, 20), (6, mgmt, 15), (8, mgmt, 30)
   - **Nodo inferior** (procesa 'sales'): (3, sales, 15), (4, sales, 5), (7, sales, 10)

En la parte inferior de la slide aparece la consulta SQL:

```sql
select dept, sum (sal) from R group by dept
```

**Figura:** Diagrama de flujo que ilustra la ejecución distribuida de una agregación con redistribución (shuffle) por la clave de agrupación. La relación $R$ está fragmentada horizontalmente en dos particiones, $R_a$ (arriba) y $R_b$ (abajo), ubicadas en nodos distintos.

**Tabla $R_a$:**

| id | dept | salary |
|----|------|--------|
| 1 | toy | 10 |
| 2 | toy | 20 |
| 3 | sales | 15 |

**Tabla $R_b$:**

| id | dept | salary |
|----|------|--------|
| 4 | sales | 5 |
| 5 | toy | 20 |
| 6 | mgmt | 15 |
| 7 | sales | 10 |
| 8 | mgmt | 30 |

Flechas desde $R_a$ y $R_b$ apuntan hacia el centro, donde los datos se redistribuyen según el atributo `dept` para que todas las filas de un mismo departamento queden en el mismo nodo de procesamiento. Los departamentos **toy** y **mgmt** se dirigen al camino superior; el departamento **sales** se dirige al camino inferior.

**Tabla intermedia superior** (tras la redistribución, contiene filas de toy y mgmt de ambos fragmentos):

| id | dept | salary |
|----|------|--------|
| 1 | toy | 10 |
| 2 | toy | 20 |
| 5 | toy | 20 |
| 6 | mgmt | 15 |
| 8 | mgmt | 30 |

**Tabla intermedia inferior** (tras la redistribución, contiene filas de sales de ambos fragmentos):

| id | dept | salary |
|----|------|--------|
| 3 | sales | 15 |
| 4 | sales | 5 |
| 7 | sales | 10 |

Flechas etiquetadas **sum** apuntan desde las tablas intermedias hacia las tablas de resultado final a la derecha:

**Resultado superior:**

| dept | sum |
|------|-----|
| toy | 50 |
| mgmt | 45 |

**Resultado inferior:**

| dept | sum |
|------|-----|
| sales | 30 |

```sql
select dept, sum (sal) from R group by dept
```

**Figura:** Mismas tablas de entrada $R_a$ y $R_b$ que en la slide anterior, sin el diagrama de flujo de redistribución.

**Tabla $R_a$:**

| id | dept | salary |
|----|------|--------|
| 1 | toy | 10 |
| 2 | toy | 20 |
| 3 | sales | 15 |

**Tabla $R_b$:**

| id | dept | salary |
|----|------|--------|
| 4 | sales | 5 |
| 5 | toy | 20 |
| 6 | mgmt | 15 |
| 7 | sales | 10 |
| 8 | mgmt | 30 |

```sql
select dept, sum (sal) from R group by dept
```

**con menos datos** (texto en rojo a la derecha de la consulta)

**Figura:** Diagrama de flujo que muestra agregación parcial local antes de la redistribución, reduciendo el volumen de datos transmitidos. Las tablas de entrada $R_a$ y $R_b$ son las mismas que en las slides anteriores.

Desde $R_a$ y $R_b$, flechas etiquetadas **sum** apuntan hacia tablas intermedias con agregaciones parciales por departamento:

**Tabla intermedia superior** (departamentos toy y mgmt):

| dept | salary |
|------|--------|
| toy | 30 |
| toy | 20 |
| mgmt | 45 |

**Tabla intermedia inferior** (departamento sales):

| dept | salary |
|------|--------|
| sales | 15 |
| sales | 15 |

Los valores representan sumas locales: toy 30 proviene de $R_a$ (10+20), toy 20 de $R_b$, mgmt 45 de $R_b$ (15+30), sales 15 de $R_a$ y sales 15 de $R_b$ (5+10).

```sql
select dept, sum (sal) from R group by dept
```

**con menos datos** (texto en rojo a la derecha de la consulta)

**con menos datos** (subtítulo en rojo debajo del título)

**Figura:** Diagrama de flujo completo en dos niveles horizontales que muestra agregación parcial local, redistribución y agregación final.

**Nivel superior — fragmento $R_a$:**

**Tabla $R_a$:**

| id | dept | salary |
|----|------|--------|
| 1 | toy | 10 |
| 2 | toy | 20 |
| 3 | sales | 15 |

Flecha **sum** hacia tabla intermedia:

| dept | salary |
|------|--------|
| toy | 30 |
| sales | 15 |

Flecha **sum** hacia resultado final superior:

| dept | sum |
|------|-----|
| toy | 50 |
| mgmt | 45 |

**Nivel inferior — fragmento $R_b$:**

**Tabla $R_b$:**

| id | dept | salary |
|----|------|--------|
| 4 | sales | 5 |
| 5 | toy | 20 |
| 6 | mgmt | 15 |
| 7 | sales | 10 |
| 8 | mgmt | 30 |

Flecha **sum** hacia tabla intermedia:

| dept | salary |
|------|--------|
| toy | 20 |
| mgmt | 45 |
| sales | 15 |

Flecha **sum** hacia resultado final inferior:

| dept | sum |
|------|-----|
| sales | 30 |

Los datos de toy y mgmt se redistribuyen al camino superior; los de sales al camino inferior. La agregación final combina las sumas parciales: toy = 30+20 = 50, mgmt = 45, sales = 15+15 = 30.

```sql
select dept, sum(sal) from R group by dept
```

- Mejoras:

- Realizar la agregación durante la partición para reducir los datos transmitidos.

- → No funciona igual para todas las funciones agregadas,

- ¿Cómo se optimiza la consulta para las funciones count, max, min, avg?

**Figura:** Dos tablas de fragmentos horizontales de la relación $R$.

**Tabla $R_a$:**

| id | dept | salary |
|----|------|--------|
| 1 | toy | 10 |
| 2 | toy | 20 |
| 3 | sales | 15 |

**Tabla $R_b$:**

| id | dept | salary |
|----|------|--------|
| 4 | sales | 5 |
| 5 | toy | 20 |
| 6 | mgmt | 15 |
| 7 | sales | 10 |
| 8 | mgmt | 30 |

```sql
select dept, avg(sal) from R group by dept
```

**Figura:** Diagrama de flujo en tres etapas para calcular el promedio distribuido. A la izquierda, las tablas $R_a$ y $R_b$ (mismos datos que en la slide anterior). En el centro, la etiqueta **Sum as S, count as C** indica la agregación parcial local. A la derecha, la etiqueta **Sum(S) / Sum(C)** indica la agregación final.

**Tablas de entrada $R_a$ y $R_b$:** (mismos datos que en la slide 66)

**Agregación parcial — Sum as S, count as C:**

**Tabla intermedia superior:**

| dept | s | c |
|------|---|---|
| toy | 30 | 2 |
| toy | 20 | 1 |
| mgmt | 45 | 2 |

**Tabla intermedia inferior:**

| dept | s | c |
|------|---|---|
| sales | 15 | 1 |
| sales | 15 | 2 |

**Agregación final — Sum(S) / Sum(C):**

**Resultado superior:**

| dept | avg |
|------|-----|
| toy | 50/3 |
| mgmt | 45/2 |

**Resultado inferior:**

| dept | avg |
|------|-----|
| sales | 30/3 |

```sql
select dept, avg(sal) from R group by dept
```

- MapReduce (previa)

**Figura:** Diagrama del flujo MapReduce con tres etapas dispuestas de izquierda a derecha.

**Etapa de entrada (izquierda):** tres cajas rectangulares apiladas verticalmente etiquetadas **data $A_1$**, **data $A_2$** y **data $A_3$**.

**Fase map:** flechas desde cada caja $A_i$ ($i = 1, 2, 3$) hacia dos cajas intermedias. La palabra **map** aparece sobre las flechas que salen de $A_1$. Cada entrada se conecta a ambas cajas intermedias.

**Etapa intermedia (centro):** dos cajas rectangulares apiladas verticalmente etiquetadas **data $B_1$** y **data $B_2$**.

**Fase reduce:** flechas horizontales desde $B_1$ hacia la caja de salida superior y desde $B_2$ hacia la caja de salida inferior. La palabra **reduce** aparece sobre la flecha que sale de $B_1$.

**Etapa de salida (derecha):** dos cajas rectangulares apiladas verticalmente, ambas etiquetadas **data $C_1$**.

(slides 59–68)

### Selección en Paralelo / Distribuido

- Sencillo si uno puede aprovechar el rango o la partición hash

- ¿Cómo funcionan los índices?

- El vector de partición puede actuar como la raíz de un índice distribuido:

**Figura:** Diagrama de índice distribuido con un vector de partición como raíz y tres índices locales B+ Tree en sitios distintos.

**Raíz (centro superior):** caja rectangular con las claves $k_0$ y $k_1$, representando el **vector de partición**.

**Tres flechas** descienden desde la raíz hacia tres estructuras de árbol etiquetadas **site 1** (izquierda), **site 2** (centro) y **site 3** (derecha). Cada sitio contiene un **B+ Tree** con nodos internos (óvalos) y nodos hoja (círculos con tres flechas pequeñas hacia abajo que indican punteros a registros de datos).

**Etiqueta lateral derecha:** un corchete vertical agrupa los tres árboles con la leyenda **local indexes**.

Las tuplas de los nodos hojas están alojados en el mismo sitio.

- Los índices distribuidos sobre atributos que no son de partición es complicado.

**Figura:** Diagrama de un **B+ Tree** distribuido donde los nodos hoja apuntan a tuplas en sitios distintos.

**Nodo raíz (arriba):** nodo central con las claves $k_0$ y $k_1$.

**Capa de index sites:** tres cajas etiquetadas **index sites**, cada una conteniendo una estructura parcial de árbol con nodos internos (óvalos) y nodos hoja (óvalos en el nivel inferior). Flechas descienden desde la raíz hacia cada index site.

**Capa de tuple sites:** dos cajas etiquetadas **tuple sites** debajo de los index sites. Dentro de cada caja hay varios cuadrados negros pequeños que representan **tuplas** (registros de datos).

**Conexiones:** flechas desde los nodos hoja de los index sites apuntan a cuadrados (tuplas) en los tuple sites. Un mismo index site puede apuntar a tuplas en distintos tuple sites, y un mismo tuple site puede recibir referencias de múltiples index sites.

Las tuplas de los nodos hojas están alojados en diferentes sitios.

- Esquemas de indexación

- ¿Cuál es mejor en un entorno distribuido?

- ¿Cómo hacer que las actualizaciones y la expansión sean eficientes?

- ¿Dónde almacenar el directorio y el conjunto de participantes?

- ¿Es necesario un conocimiento global?

- → Si el índice no es demasiado grande, puede ser mejor mantenerlo completo y replicarlo.

(slides 69–72)

## Glosario

**$[R : \text{cond}]$** — Notación para el fragmento. $R$ es el fragmento; $\text{cond}$ son las condiciones que satisfacen sus tuplas.

**Fragmentación Derivada** — Fragmentación de una relación derivada de la fragmentación de otra relación mediante semi-join: $S_1 : S \text{ sj}_K R_1$, $S_2 : S \text{ sj}_K R_2$.

**Fragmentación Vertical** — Fragmentación de una relación en fragmentos con atributos distintos que comparten una clave común, por ejemplo $\{ R_1(K, A, B),\; R_2(K, C, D) \}$.
