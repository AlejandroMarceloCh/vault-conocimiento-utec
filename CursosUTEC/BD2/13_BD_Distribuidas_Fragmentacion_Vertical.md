---
curso: BD2
titulo: 13 BD Distribuidas - Fragmentación Vertical
slides: 39
fuente: 13 BD Distribuidas - Fragmentación Vertical.pdf
---

# 13 BD Distribuidas - Fragmentación Vertical

## Índice

- [Fragmentación Vertical](#fragmentación-vertical)
  - [Ejemplo](#ejemplo)
  - [Concepto y notación](#concepto-y-notación)
  - [Propiedades: Completitud](#propiedades-completitud)
  - [Propiedades: Desarticulación](#propiedades-desarticulación)
  - [Propiedades: Join sin pérdida](#propiedades-join-sin-pérdida)
- [Fragmentación por dependencias funcionales](#fragmentación-por-dependencias-funcionales)
  - [Dependencias funcionales](#dependencias-funcionales)
  - [Dependencias funcionales: Ejemplo 1](#dependencias-funcionales-ejemplo-1)
  - [Descomposición: Definición](#descomposición-definición)
  - [Descomposición: Ejemplo 1](#descomposición-ejemplo-1)
  - [Descomposición: Ejemplo 2](#descomposición-ejemplo-2)
  - [Descomposición en 3FN](#descomposición-en-3fn)
  - [Descomposición en 3FN: Ejemplo](#descomposición-en-3fn-ejemplo)
  - [Normalización en 3FN](#normalización-en-3fn)
  - [Normalización en 3FN: Ejemplo](#normalización-en-3fn-ejemplo)
  - [Normalización en FNBC](#normalización-en-fnbc)
  - [Normalización en FNBC: Ejemplo](#normalización-en-fnbc-ejemplo)
- [Fragmentación por afinidad de atributos](#fragmentación-por-afinidad-de-atributos)
  - [Matriz de afinidad de atributos](#matriz-de-afinidad-de-atributos)
  - [Vertical Clustering and Bond Energy Algorithm (BEA)](#vertical-clustering-and-bond-energy-algorithm-bea)
  - [Matriz de uso](#matriz-de-uso)
  - [Cálculo de afinidad: Paso 1](#cálculo-de-afinidad-paso-1)
  - [Ejemplo de cálculo de afinidad](#ejemplo-de-cálculo-de-afinidad)
  - [Matrices de uso y afinidad](#matrices-de-uso-y-afinidad)
  - [Paso 2: reordenamiento con BEA](#paso-2-reordenamiento-con-bea)
  - [Determinar el orden de $A_3$](#determinar-el-orden-de-a_3)
  - [Determinar el orden de $A_4$](#determinar-el-orden-de-a_4)
  - [Matriz de afinidad agrupada](#matriz-de-afinidad-agrupada)
  - [Paso 3: puntos de división](#paso-3-puntos-de-división)
  - [Función objetivo](#función-objetivo)
  - [Fragmentos resultantes](#fragmentos-resultantes)
- [Glosario](#glosario)

## Fragmentación Vertical

**Figura:** Slide de portada con fondo fotográfico de un túnel o corredor circular futurista en tonos azules profundos, con patrones tecnológicos y líneas tipo circuito. En el centro, una persona vista de espaldas camina hacia el interior del túnel. En la parte superior central, el código y nombre del curso «CS2042 - BASES DE DATOS II». En el centro, el título principal «Base de Datos Distribuidas» en letras grandes blancas; debajo, «SEMANA 13» en cursiva. Una línea horizontal punteada amarilla separa el título de los datos del instructor: «Heider Sanchez» y «hsanchez@utec.edu.pe».

**Figura:** Slide dividida en dos zonas. en el centro un número grande «4.» con subrayado azul, un icono de portapapeles azul con lista de verificación, y el título «Base de Datos Distribuidas» con subtítulo «Fragmentación Vertical» en cursiva azul claro.

### Ejemplo

- Ejemplo:

| id | name | location | salary |
|---|---|---|---|
| 1 | Tom | A | 15 |
| 2 | Ann | B | 23 |
| 3 | Ben | A | 21 |

**Figura:** En la parte superior, una tabla etiquetada **E** con cuatro columnas (`id`, `name`, `location`, `salary`) y tres filas de datos (1/Tom/A/15, 2/Ann/B/23, 3/Ben/A/21). Dos flechas descienden desde la tabla E hacia dos fragmentos: a la izquierda, la tabla **E₁** con columnas `id`, `name`, `location` y las mismas tres filas (1/Tom/A, 2/Ann/B, 3/Ben/A); a la derecha, la tabla **E₂** con columnas `id`, `salary` y las tres filas (1/15, 2/23, 3/21). El atributo `id` aparece en ambos fragmentos como clave de unión.

(slides 3)

### Concepto y notación

- Es parecido a la normalización de relaciones (formas normales).

$$R[A] \Rightarrow R_1[A_1]$$
$$\vdots$$
$$R_n[A_n]$$

Conjunto de atributos

$$A = \{a_1, a_2, \dots, a_n\}$$
$$A_i \subseteq A$$

**Figura:** Slide con título «Fragmentación Vertical» en la parte superior izquierda. A la izquierda, la notación matemática que muestra la descomposición de la relación $R[A]$ en fragmentos $R_1[A_1]$ hasta $R_n[A_n]$ separados por puntos suspensivos verticales ($\vdots$). A la derecha, bajo la etiqueta «Conjunto de atributos», las definiciones del conjunto total $A = \{a_1, a_2, \dots, a_n\}$ y de cada subconjunto $A_i \subseteq A$.

(slides 4)

### Propiedades: Completitud

- Propiedades:

  - Sea:

$$R[A] \Rightarrow R_i[A_i]$$

  - (1) Completitud:
    - Se cumple que:

$$\cup A_i = A \quad \forall i$$

**Figura:** Slide con título «Fragmentación Vertical» y viñeta «Propiedades:». Bajo «Sea:», la notación $R[A] \Rightarrow R_i[A_i]$. Bajo el subpunto «(1) Completitud:» y «Se cumple que:», la fórmula $\cup A_i = A \quad \forall i$, que indica que la unión de todos los conjuntos de atributos de los fragmentos debe igualar el conjunto de atributos original.

(slides 5)

### Propiedades: Desarticulación

- Propiedades:

  - (2) Desarticulación:

$$A_i \cap A_j = \emptyset \quad \forall i, j: i \neq j$$

**Figura:** Slide con título «Fragmentación Vertical» y viñeta «Propiedades:». Bajo el subpunto «(2) Desarticulación:», la fórmula $A_i \cap A_j = \emptyset \quad \forall i, j: i \neq j$. A la derecha, un diagrama muestra la relación original **E (id, location, salary)** con dos flechas que apuntan a dos fragmentos: **E₁ (id, location)** y **E₂ (salary)**.

No es una propiedad deseable
¿Por qué?

**Figura:** Slide con el mismo contenido de la slide anterior (fórmula de desarticulación y diagrama E → E₁ (id, location) / E₂ (salary)), pero con una gran **X roja** tachando tanto la fórmula como el diagrama. En la parte inferior, texto en rojo: «No es una propiedad deseable ¿Por qué?».

(slides 6–7)

### Propiedades: Join sin pérdida

- Propiedades:

  - (2) Join sin perdida:

$$\bowtie R_i = R \quad \forall i$$

  - Debe ser posible la reconstrucción total de R sin tuplas falsas y sin perdida de tuplas.
  - Formas de lograr el Join sin perdida:
    - a. Dependencias funcionales
    - b. Matriz de afinidad de atributos

**Figura:** Slide con título «Fragmentación Vertical» y viñeta «Propiedades:». Bajo «(2) Join sin perdida:», la fórmula con el operador de join natural ($\bowtie$) seguida de $R_i = R \quad \forall i$. Debajo, los tres puntos de texto sobre la reconstrucción sin tuplas falsas y las dos formas de lograr el join sin pérdida (dependencias funcionales y matriz de afinidad de atributos).

(slides 8)

## Fragmentación por dependencias funcionales

**Figura:** Slide dividida horizontalmente en dos mitades iguales: la mitad superior es blanca con el texto centrado «Fragmentación por dependencias funcionales» en negro; la mitad inferior es de color azul cian sólido. Pequeño acento triangular azul en la esquina superior izquierda.

### Dependencias funcionales

Dada una relación R
y dos conjuntos de atributos $X \in R$, $Y \in R$
**X determina funcionalmente a Y**
si y sólo si
dos tuplas que tiene el mismo valor de X
deben por fuerza tener el mismo valor de Y

- X y Y pueden ser atributos compuestos

**Figura:** Slide con título «Dependencias funcionales». El texto de la definición aparece con formato jerárquico indentado: «Dada una relación R» en verde; «y dos conjuntos de atributos $X \in R$, $Y \in R$» en azul; «X determina funcionalmente a Y» subrayado en morado; «si y sólo si» seguido de las dos líneas sobre tuplas con el mismo valor de X y Y en azul. Al pie, la nota «- X y Y pueden ser atributos compuestos» con «compuestos» en rojo.

(slides 11)

### Dependencias funcionales: Ejemplo 1

Sea la instancia (representativa):

| Profesor | Curso | Texto |
|---|---|---|
| Juan | Estructuras de datos | Bartram |
| Juan | Administración | Martín |
| Pedro | Compiladores | Hoffman |
| Celis | Estructura de datos | Horowitz |
| Pedro | Administración | Martín |

$$\{Texto\} \to \{Curso\}$$

$$\{Profesor\} \to \{Curso\}$$

**Figura:** Slide titulada «Dependencias funcionales: Ejemplo 1». En el centro, la tabla **IMPARTIR** con columnas Profesor, Curso y Texto y cinco filas de datos. Debajo de la tabla, dos recuadros con borde punteado: el superior en verde contiene $\{Texto\} \to \{Curso\}$; el inferior en rojo contiene $\{Profesor\} \to \{Curso\}$.

(slides 12)

### Descomposición: Definición

Definición

Sea la relación R y su conjunto de dependencias funcionales F
Una descomposición R1 y R2 es sin pérdida si:

- Conservan los atributos de R
  - $R = R1 \cup R2$
- Conservan las dependencias funcionales
  - $F^+ = \{F1 \cup F2\}^+$
- No genera tuplas falsas, para ello:
  - $\{R1 \cap R2\} \to R1$ ó
  - $\{R1 \cap R2\} \to R2$
  - * La intersección genera una dependencia funcional válida en F

**Figura:** Slide con título «Descomposición» y subtítulo «Definición» en morado. Tres condiciones principales con viñetas y sub-viñetas, cada una con su fórmula correspondiente. La nota al pie con asterisco indica que la intersección debe generar una dependencia funcional válida en F.

(slides 13)

### Descomposición: Ejemplo 1

Ejemplo 1

Sea R(A,B,C,D,E) y F={AB→C, C→D, C→E}
La descomposición R1(A,B,C,D) y R2(C,E)
genera F1={AB→C, C→D} y F2={C→E}

- ¿Conservan los atributos de R?
  - Si
- ¿Conserva las dependencias funcionales?
  - Si
- ¿No genera tuplas falsas?:
  - No
    - $\{R1 \cap R2\} \to R2$
    - $C \to CE \subset F^+$

**Figura:** Slide con título «Descomposición» y subtítulo «Ejemplo 1» en morado. Presenta la relación R(A,B,C,D,E), el conjunto F, la descomposición en R1 y R2 con sus respectivos F1 y F2, y tres preguntas de evaluación con respuestas «Si» / «No» y la verificación de join sin pérdida mediante $C \to CE \subset F^+$.

(slides 14)

### Descomposición: Ejemplo 2

Ejemplo 2

Sea R(A,B,C,D,E,F) y F= {AB→D, AC→E, ABD→F}
La descomposición R1(A,B,D,F) y R2(A,C,E)
genera F1={AB→D, ABD→F} y F2={AC→E}

- Si conservan los atributos de R
- Si conserva las dependencias funcionales
- SI genera tuplas falsas, ya que:
  - $\{R1 \cap R2\} \to R1$: $A \to BDF \not\subset F^+$
  - $\{R1 \cap R2\} \to R2$: $A \to CE \not\subset F^+$

**Figura:** Slide con título «Descomposición» y subtítulo «Ejemplo 2» en morado. Presenta la relación R(A,B,C,D,E,F) con atributos A, B, C subrayados como clave, el conjunto F con tres dependencias funcionales, la descomposición en R1(A,B,D,F) y R2(A,C,E) con F1 y F2, y la evaluación que concluye que sí genera tuplas falsas porque $A \to BDF$ y $A \to CE$ no pertenecen a $F^+$.

(slides 15)

### Descomposición en 3FN

- Definición
  - Está en 2FN
  - Para toda DF X→Y en R:
    - X es superclave ó Y es atributo primo
- Descomposición
  - R(A,X,Y,B) donde X → Y incumple 3FN
  - Crear otra relación con X+, donde X es clave
  - Eliminar Y de R

**Figura:** Slide con título «Descomposición en 3FN». Dos secciones con viñetas: «Definición» (condiciones de 3FN: estar en 2FN y que para toda DF X→Y, X sea superclave o Y sea atributo primo) y «Descomposición» (proceso para relación R(A,X,Y,B) donde X→Y incumple 3FN: crear relación con X⁺ donde X es clave, y eliminar Y de R).

(slides 16)

### Descomposición en 3FN: Ejemplo

Ejemplo

- Sea R($\underline{A}$,X,Y,B) y F = {A →XB, X→Y}.
  - No es 3FN, X no es superclave

- Tomando las F como base:
  - R1($\underline{A}$,X,B)
  - R2($\underline{X}$,Y)
    - $(R1 \cap R2 \to R2) \subset F^+$

**Figura:** Slide con título «Descomposición en 3FN» y subtítulo «Ejemplo» en morado. Muestra la relación R con A subrayado como clave primaria, el conjunto F, la observación de que no es 3FN porque X no es superclave, y la descomposición resultante en R1($\underline{A}$,X,B) y R2($\underline{X}$,Y) con la verificación en rojo $(R1 \cap R2 \to R2) \subset F^+$.

(slides 17)

### Normalización en 3FN

- Descomposición
  - Calcular F mínimo
  - Convertir cada dependencia en una relación
    $(X \to Y \Rightarrow R_i(XY))$
  - Si no está la llave en una relación, agregarla
  - Eliminar relaciones redundantes

**Figura:** Slide con título «Normalización en 3FN» y viñeta «Descomposición» con cuatro sub-pasos del algoritmo de normalización en 3FN: calcular F mínimo, convertir cada dependencia en una relación ($X \to Y \Rightarrow R_i(XY)$), agregar la llave si no está en ninguna relación, y eliminar relaciones redundantes.

(slides 18)

### Normalización en 3FN: Ejemplo

Ejemplo

- Sea R(A, B, C, D, E) y F = {A → B, A → C, C → D, B → E}.
  - F es mínimo
- $\{A\}^+ = \{A,B,C,D,E\} \Rightarrow A$ es clave única
- Tomando las cuatro DFs:
  - ~~R1(A,B),~~
  - ~~R2(A,C),~~
  - R3(A,C,D)
  - R4(A,B,E)

**Figura:** Slide con título «Normalización en 3FN» y subtítulo «Ejemplo» en morado. Presenta la relación R(A,B,C,D,E), el conjunto F con cuatro dependencias funcionales, la confirmación de que F es mínimo, el cálculo de la clausura $\{A\}^+ = \{A,B,C,D,E\}$ concluyendo que A es clave única, y el inicio del paso «Tomando las cuatro DFs:» sin listar aún las relaciones resultantes.

**Figura:** Slide con título «Normalización en 3FN» y subtítulo «Ejemplo» en morado. Mismo contenido que la slide anterior, pero con la lista completa de relaciones resultantes al tomar las cuatro DFs: R1(A,B) y R2(A,C) aparecen tachadas con línea horizontal, mientras que R3(A,C,D) y R4(A,B,E) permanecen activas.

(slides 19–20)

### Normalización en FNBC

- Definición
    - Está en 3FN (... válido desde 1FN)
    - Para toda DF $X \to Y$ en $R$:
         - $X$ es superclave
- Descomposición
    - $R(A,X,Y,B)$ donde $X \to Y$ incumple FNBC
    - Crear dos relaciones
         - $R1 = R - Y$
         - $R2(X,Y)$

Esta estrategia de normalización no asegura preservar dependencias, pero sí asegura la recuperación de la información por join.

(slides 21)

### Normalización en FNBC: Ejemplo

Ejemplo

Sea $R(A, B, C, D, E)$ y $F = \{A \to BC, C \to D, B \to E\}$.

1- $R$ no está en FNBC, $C \to D$ incumple FNBC

   Partimos: $R(A,B,C,E)$ y $R1(C,D)$.

2- $R$ no está en FNBC, $B \to E$ incumple FNBC

      Partimos: $R(A,B,C)$ y $R2(B,E)$

**Resultado:** $R1(C,D)$, $R(A,B,C)$ y $R2(B,E)$

(slides 22)

## Fragmentación por afinidad de atributos

**Figura:** En el centro aparece un icono negro de un reloj analógico (manecillas señalando aproximadamente las 3:00) con una flecha curva gruesa en sentido horario arqueándose sobre la parte superior del reloj. Acento triangular azul en la esquina superior izquierda. Barra horizontal azul en la parte inferior.

**Figura:** Slide de portada con fotografía del edificio de UTEC (Universidad de Ingeniería y Tecnología) cubierta por un filtro cian/azul. En el centro, el texto grande en blanco: «Fragmentación por afinidad de atributos». Las letras «UTEC» son visibles en la fachada del edificio a la derecha.

### Matriz de afinidad de atributos

- Matriz de afinidad de atributos:
    1. Repetir la clave en todos los fragmentos.

       $key \subseteq A_i \quad \forall i$

    2. Agrupar atributos por afinidad

           - ¿Cómo decidir

               que atributos agrupar?

**Figura:** En el centro de la slide aparece la relación original $E = (id, name, location, salary)$. Desde ella parten flechas hacia tres opciones de fragmentación vertical:

- **Opción 1 (dos fragmentos):**
  - $E = (id, name, location)$
  - $E = (id, salary)$

- **Opción 2 (tres fragmentos):**
  - $E = (id, name)$
  - $E = (id, location)$
  - $E = (id, salary)$

- **Opción 3:** una flecha apunta a un signo de interrogación (**?**), indicando otras posibilidades de partición.

En todas las opciones, el atributo $id$ (clave) aparece repetido en cada fragmento.

S. Navathe, S. Ceri, G. Wiederhold, J. Dou. Vertical partitioning algorithms for database design. ACM Trans. Database Syst., 9 (4) (1984), p. 680710

(slides 25)

### Vertical Clustering and Bond Energy Algorithm (BEA)

- Vertical Clustering and Bond Energy Algorithm (BEA)

      - El objetivo es agrupar atributos que tienen alta afinidad entre sí, es decir, aquellos que suelen ser consultados de manera conjunta.

https://infolab.usc.edu/csci585/Spring2008/Lectures/DDBMS-Design.pdf

P. Arabie and L. J. Hubert, "The bond energy algorithm revisited," in IEEE Transactions on Systems, Man, and Cybernetics, vol. 20, no. 1, pp. 268-274, Jan.-Feb. 1990.

(slides 26)

### Matriz de uso

- Matriz de afinidad de atributos:

     - Dado un conjunto de consultas $\{q_1, q_2, \ldots\}$ que se ejecutan sobre la relación $R[A_1, A_2, ..]$

$$use(q_k, A_j) = \begin{cases} 1 & \text{si } A_j \text{ es referenciado por } q_k \\ 0 & \text{en otro caso} \end{cases}$$

**Figura:** Matriz de uso de $4 \times 4$ donde las filas representan consultas ($q_1$ a $q_4$, en azul) y las columnas representan atributos ($A_1$ a $A_4$, en rojo):

| | $A_1$ | $A_2$ | $A_3$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $q_1$ | 1 | 0 | 1 | 0 |
| $q_2$ | 0 | 1 | 1 | 0 |
| $q_3$ | 0 | 1 | 0 | 1 |
| $q_4$ | 0 | 0 | 1 | 1 |

(slides 27)

### Cálculo de afinidad: Paso 1

- Matriz de afinidad de atributos:

     - Paso 1: Se crea una matriz que representa la frecuencia con la que los atributos son accedidos juntos en consultas (por las distintas aplicaciones):

$$Aff(A_i, A_j) = \sum_{k \mid use(q_k, A_i)=1 \land use(q_k, A_j)=1} \sum_{\forall l} ref_l(q_k) \cdot acc_l(q_k)$$

     - En donde:
          - $ref_l(q_k)$ indica el número de accesos a los atributos $(A_i, A_j)$ por la consulta $q_k$ en el sitio $l$.
          - $acc_l(q_k)$ indica la frecuencia de ejecución de la consulta $q_k$ en el sitio $l$.

(slides 28)

### Ejemplo de cálculo de afinidad

- Matriz de afinidad de atributos:

     - Ejemplo:
          - Sea $ref_l(q_k) = 1$ para todo $q_k$ en el sitio $l$. La frecuencia de ejecución es:

| | Site 1 | Site 2 | Site 3 |
| :--- | :---: | :---: | :---: |
| $q_1$ | 15 | 20 | 10 |
| $q_2$ | 5 | 0 | 0 |
| $q_3$ | 25 | 25 | 25 |
| $q_4$ | 3 | 0 | 0 |

          - $aff(A_1, A_3) = acc_1(q_1) + acc_2(q_1) + acc_3(q_1) = 45$, dado que $q_1$ que es la única consulta que accede a ambos atributos.
              $aff(A_2, A_4) = acc_1(q_3) + acc_2(q_3) + acc_3(q_3) = 75$

(slides 29)

### Matrices de uso y afinidad

- Matriz de afinidad de atributos:

     - Entonces la matriz quedaría de la siguiente forma:

**Figura:** Dos matrices lado a lado, separadas por una flecha. A la izquierda, la etiqueta «matriz de uso»; a la derecha, la etiqueta «matriz de afinidad».

**matriz de uso:**

| | $A_1$ | $A_2$ | $A_3$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $q_1$ | 1 | 0 | 1 | 0 |
| $q_2$ | 0 | 1 | 1 | 0 |
| $q_3$ | 0 | 1 | 0 | 1 |
| $q_4$ | 0 | 0 | 1 | 1 |

**matriz de afinidad:**

| | $A_1$ | $A_2$ | $A_3$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 0 | 45 | 0 |
| $A_2$ | 0 | 80 | 5 | 75 |
| $A_3$ | 45 | 5 | 53 | 3 |
| $A_4$ | 0 | 75 | 3 | 78 |

(slides 30)

### Paso 2: reordenamiento con BEA

- Matriz de afinidad de atributos:
   - Paso 2: reordenar los atributos permutando filas y columnas para maximizar la medida de afinidad global. Como resultado se obtendrá la matriz de afinidad agrupada.
       - Bond Energy Algorithm (BEA)

**Figura:** A la derecha del texto aparece el pseudocódigo del «Algorithm 2.3: BEA»:

```text
Input: AA: attribute affinity matrix
Output: CA: clustered affinity matrix

begin
  {initialize; remember that AA is an n x n matrix}
  CA(•, 1) ← AA(•, 1)
  CA(•, 2) ← AA(•, 2)
  index ← 3
  while index ≤ n do
    {choose the "best" location for attribute AA_index}
    for i from 1 to index - 1 by 1 do
      calculate cont(A_{i-1}, A_{index}, A_i)
    calculate cont(A_{index-1}, A_{index}, A_{index+1}) {boundary condition}

    loc ← placement given by maximum cont value

    for j from index to loc by -1 do
      CA(•, j) ← CA(•, j - 1) {shuffle the two matrices}
    end for

    CA(•, loc) ← AA(•, index)
    index ← index + 1
  end while

  order the rows according to the relative ordering of columns
end
```

(slides 31)

### Determinar el orden de $A_3$

- Matriz de afinidad de atributos:
     - Determinar el orden de $A_3$

**Figura:** Matriz de afinidad de atributos $4 \times 4$ (entrada del algoritmo BEA):

| | $A_1$ | $A_2$ | $A_3$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 0 | 45 | 0 |
| $A_2$ | 0 | 80 | 5 | 75 |
| $A_3$ | 45 | 5 | 53 | 3 |
| $A_4$ | 0 | 75 | 3 | 78 |

A la derecha, tabla parcial de la matriz agrupada con columnas reordenadas $A_1$, $A_3$, $A_2$, $A_4$ (la columna $A_4$ aún vacía):

| | $A_1$ | $A_3$ | $A_2$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 45 | 0 | |
| $A_2$ | 0 | 5 | 80 | |
| $A_3$ | 45 | 53 | 5 | |
| $A_4$ | 0 | 3 | 75 | |

Fórmulas del algoritmo:

$$cont(A_i, A_k, A_j) = 2 \cdot \{bond(A_i, A_k) + bond(A_k, A_j) - bond(A_i, A_j)\}$$

$$bond(A_x, A_y) = \sum_{z=1}^{n} aff(A_z, A_x) \cdot aff(A_z, A_y)$$

Fijamos $A_1$, $A_2$, y comenzamos el analisis desde $A_3$

$Cont(A_0, A_3, A_1) = 8820$ $\quad$ $Cont(A_1, A_3, A_2) = 10150$ $\quad$ $Cont(A_2, A_3, A_5) = 1780$

Dado que $Cont(A_1, A_3, A_2)$ es el más grande, entonces $[A_1, A_3, A_2]$ es el mejor orden.

Condición de contorno:

$$aff(A_0, A_j) = aff(A_i, A_0) = aff(A_{n+1}, A_j) = aff(A_i, A_{n+1}) = 0$$

**Figura:** Misma matriz de afinidad de atributos $4 \times 4$ de la slide anterior:

| | $A_1$ | $A_2$ | $A_3$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 0 | 45 | 0 |
| $A_2$ | 0 | 80 | 5 | 75 |
| $A_3$ | 45 | 5 | 53 | 3 |
| $A_4$ | 0 | 75 | 3 | 78 |

$[A_1, A_3, A_2]$ es el mejor orden.

Tabla parcial con columnas $A_1$, $A_3$, $A_2$:

| | $A_1$ | $A_3$ | $A_2$ |
| :--- | :---: | :---: | :---: |
| $A_1$ | 45 | 45 | 0 |
| $A_2$ | 0 | 5 | 80 |
| $A_3$ | 45 | 53 | 5 |
| $A_4$ | 0 | 3 | 75 |

Cálculos pendientes para determinar el orden de $A_4$:

$Cont(A_0, A_4, A_1) =$ $\quad$ $Cont(A_1, A_4, A_3) =$ $\quad$ $Cont(A_3, A_4, A_2) =$

$Cont(A_2, A_4, A_5) =$

(slides 32–33)

### Determinar el orden de $A_4$

- Matriz de afinidad de atributos:
     - Determinar el orden de $A_4$

**Figura:** Tabla de afinidad con filas y columnas ordenadas $A_1$, $A_3$, $A_2$, $A_4$:

| | $A_1$ | $A_3$ | $A_2$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 45 | 0 | 0 |
| $A_3$ | 45 | 53 | 5 | 3 |
| $A_2$ | 0 | 5 | 80 | 75 |
| $A_4$ | 0 | 3 | 75 | 78 |

Debajo, la misma matriz en notación matricial con etiquetas de fila en color naranja ($A_1$, $A_2$, $A_3$, $A_4$) y etiquetas de columna en color rosa ($A_1$, $A_3$, $A_2$, $A_4$):

```
    A1  A3  A2  A4
A1 [45  45   0   0]
A2 [ 0   5  80  75]
A3 [45  53   5   3]
A4 [ 0   3  75  78]
```

$[A_2, A_4, A_5]$ es el mejor orden.

**Figura:** Tabla de afinidad con filas y columnas ordenadas $A_1$, $A_3$, $A_2$, $A_4$:

| | $A_1$ | $A_3$ | $A_2$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 45 | 0 | 0 |
| $A_3$ | 45 | 53 | 5 | 3 |
| $A_2$ | 0 | 5 | 80 | 75 |
| $A_4$ | 0 | 3 | 75 | 78 |

Debajo, la misma matriz en notación matricial con etiquetas de fila en color naranja ($A_1$, $A_2$, $A_3$, $A_4$) y etiquetas de columna en color rosa ($A_1$, $A_3$, $A_2$, $A_4$):

```
    A1  A3  A2  A4
A1 [45  45   0   0]
A2 [ 0   5  80  75]
A3 [45  53   5   3]
A4 [ 0   3  75  78]
```

$[A_2, A_4, A_5]$ es el mejor orden.

(slides 34–35)

### Matriz de afinidad agrupada

- Matriz de afinidad de atributos:
     - Las filas son organizados en el mismo orden que las columnas

**Figura:** Dos matrices $4 \times 4$ conectadas por una flecha azul hacia la derecha, etiquetada «Matriz de afinidad agrupada».

**Matriz inicial** (filas y columnas en orden $A_1$, $A_2$, $A_3$, $A_4$):

| | $A_1$ | $A_2$ | $A_3$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 0 | 45 | 0 |
| $A_2$ | 0 | 80 | 5 | 75 |
| $A_3$ | 45 | 5 | 53 | 3 |
| $A_4$ | 0 | 75 | 3 | 78 |

**Matriz de afinidad agrupada** (filas y columnas reordenadas a $A_1$, $A_3$, $A_2$, $A_4$):

| | $A_1$ | $A_3$ | $A_2$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 45 | 0 | 0 |
| $A_3$ | 45 | 53 | 5 | 3 |
| $A_2$ | 0 | 5 | 80 | 75 |
| $A_4$ | 0 | 3 | 75 | 78 |

Los valores altos de afinidad quedan agrupados en dos bloques a lo largo de la diagonal: bloque superior izquierdo $\{A_1, A_3\}$ con valores $(45, 45, 45, 53)$ y bloque inferior derecho $\{A_2, A_4\}$ con valores $(80, 75, 75, 78)$. Los bloques fuera de la diagonal contienen valores bajos $(0, 0, 5, 3)$.

(slides 36)

### Paso 3: puntos de división

- Matriz de afinidad de atributos:

     - Paso 3: encuentre los conjuntos de atributos a los que se accede, en su mayor parte, por distintos conjuntos de aplicaciones (ejecución de consultas).
          - Se busca puntos de división a lo largo de la diagonal de manera que:
               - Se maximicen los accesos totales a un solo fragmento, mientras que
               - Se minimicen los accesos totales a más de un fragmento.

(slides 37)

### Función objetivo

- Matriz de afinidad de atributos:

**Figura:** Matriz cuadrada $n \times n$ con filas y columnas etiquetadas $A_1$, $A_2$, $A_3$, $\ldots$, $A_i$, $A_{i+1}$, $\ldots$, $A_n$. Una línea horizontal discontinua y una línea vertical discontinua se intersectan entre $A_i$ y $A_{i+1}$, dividiendo la matriz en cuatro cuadrantes:

- **TA (superior izquierdo):** patrón de guiones pequeños; incluye afinidades entre atributos de $A_1$ a $A_i$.
- **BA (inferior derecho):** sombreado en color beige sólido; incluye afinidades entre atributos de $A_{i+1}$ a $A_n$.
- **Cuadrantes restantes (superior derecho e inferior izquierdo):** sombreados en color beige sólido; representan la afinidad cruzada entre los conjuntos de atributos de TA y BA.

Se traduce en maximizar $z$

$$z = CTA \cdot CBA - COQ^2$$

$CTA$ = Suma total de afinidad en el cuadrante TA

$CBA$ = Suma total de afinidad en el cuadrante BA

$COQ$ = Suma total de afinidad en los cuadrantes restantes

(slides 38)

### Fragmentos resultantes

- Matriz de afinidad de atributos:

**Figura:** Matriz de afinidad agrupada $4 \times 4$ con filas y columnas en orden $A_1$, $A_3$, $A_2$, $A_4$ (etiquetas de fila en naranja, etiquetas de columna en rosa):

| | $A_1$ | $A_3$ | $A_2$ | $A_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $A_1$ | 45 | 45 | 0 | 0 |
| $A_3$ | 45 | 53 | 5 | 3 |
| $A_2$ | 0 | 5 | 80 | 75 |
| $A_4$ | 0 | 3 | 75 | 78 |

Un bloque $2 \times 2$ sombreado en verde en la esquina superior izquierda agrupa los atributos $A_1$ y $A_3$ (valores: 45, 45, 45, 53). Un bloque $2 \times 2$ sombreado en amarillo en la esquina inferior derecha agrupa los atributos $A_2$ y $A_4$ (valores: 80, 75, 75, 78). Los bloques fuera de la diagonal contienen valores bajos (0, 0, 5, 3).

$R_1 = [k, A_1, A_3]$ $\quad$ $R_2 = [k, A_2, A_4]$

(slides 39)

## Glosario

| Término | Definición |
|---|---|
| **Fragmentación vertical** | Descomposición de una relación $R[A]$ en fragmentos $R_1[A_1], \ldots, R_n[A_n]$ donde cada $A_i \subseteq A$; es parecido a la normalización de relaciones. |
| **Completitud** | Propiedad que exige $\cup A_i = A \quad \forall i$: la unión de todos los conjuntos de atributos de los fragmentos debe igualar el conjunto de atributos original. |
| **Desarticulación** | Propiedad formal $A_i \cap A_j = \emptyset \quad \forall i, j: i \neq j$; no es una propiedad deseable en fragmentación vertical. |
| **Join sin pérdida** | Propiedad $\bowtie R_i = R \quad \forall i$: debe ser posible la reconstrucción total de $R$ sin tuplas falsas y sin pérdida de tuplas. |
| **Dependencia funcional** | Dada una relación $R$ y dos conjuntos de atributos $X \in R$, $Y \in R$: **$X$ determina funcionalmente a $Y$** si y sólo si dos tuplas que tienen el mismo valor de $X$ deben por fuerza tener el mismo valor de $Y$. $X$ y $Y$ pueden ser atributos compuestos. |
| **Descomposición sin pérdida** | Sea la relación $R$ y su conjunto de dependencias funcionales $F$. Una descomposición $R1$ y $R2$ es sin pérdida si conservan los atributos de $R$ ($R = R1 \cup R2$), conservan las dependencias funcionales ($F^+ = \{F1 \cup F2\}^+$), y no genera tuplas falsas (mediante $\{R1 \cap R2\} \to R1$ ó $\{R1 \cap R2\} \to R2$, donde la intersección genera una dependencia funcional válida en $F$). |
| **Tercera forma normal (3FN)** | Está en 2FN y, para toda DF $X \to Y$ en $R$, $X$ es superclave ó $Y$ es atributo primo. |
| **Forma normal de Boyce-Codd (FNBC)** | Está en 3FN (válido desde 1FN) y, para toda DF $X \to Y$ en $R$, $X$ es superclave. |
| **Matriz de afinidad de atributos** | Matriz que representa la frecuencia con la que los atributos son accedidos juntos en consultas; se usa para agrupar atributos por afinidad en fragmentación vertical. |
| **$use(q_k, A_j)$** | Función que vale 1 si $A_j$ es referenciado por la consulta $q_k$, y 0 en otro caso. |
| **$Aff(A_i, A_j)$** | $\sum_{k \mid use(q_k, A_i)=1 \land use(q_k, A_j)=1} \sum_{\forall l} ref_l(q_k) \cdot acc_l(q_k)$: frecuencia con la que los atributos $A_i$ y $A_j$ son accedidos juntos. |
| **$ref_l(q_k)$** | Número de accesos a los atributos $(A_i, A_j)$ por la consulta $q_k$ en el sitio $l$. |
| **$acc_l(q_k)$** | Frecuencia de ejecución de la consulta $q_k$ en el sitio $l$. |
| **Bond Energy Algorithm (BEA)** | Algoritmo que reordena atributos permutando filas y columnas de la matriz de afinidad para maximizar la medida de afinidad global y obtener la matriz de afinidad agrupada. |
| **$cont(A_i, A_k, A_j)$** | $2 \cdot \{bond(A_i, A_k) + bond(A_k, A_j) - bond(A_i, A_j)\}$: medida usada por BEA para decidir la ubicación óptima de un atributo. |
| **$bond(A_x, A_y)$** | $\sum_{z=1}^{n} aff(A_z, A_x) \cdot aff(A_z, A_y)$. |
| **$CTA$** | Suma total de afinidad en el cuadrante TA (superior izquierdo) de la matriz dividida. |
| **$CBA$** | Suma total de afinidad en el cuadrante BA (inferior derecho) de la matriz dividida. |
| **$COQ$** | Suma total de afinidad en los cuadrantes restantes (afinidad cruzada entre TA y BA). |
