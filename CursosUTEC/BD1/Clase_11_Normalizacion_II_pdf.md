---
curso: BD1
titulo: Clase 11 Normalizacion II
slides: 48
fuente: Clase 11 Normalizacion II.pdf
---

## Slide 1

Portada decorativa (imagen de fondo con túnel azul y figura de robot/científico, logo UTEC arriba izquierda, tagline "Reinventa el mundo" arriba derecha).

Título: "NORMALIZACIÓN (II)" — "CS2041- Base de Datos I" — "Ciclo 2024 - 1".

Pie: contacto de los profesores — Teófilo Chambilla (tchambilla@utec.edu.pe) y Brenner Ojeda (bojeda@utec.edu.pe). Logos UTEC / TransformaTec (decorativo).

## Slide 2

Slide de índice. Encabezado con curso "CS2041 Base de Datos I / Teófilo Chambilla Aquino" y logo UTEC (decorativo).

Título: "Índice". Lista de bullets:
- Formas normales
- 1NF
- 2NF
- 3NF
- FNBC
- Heurísticas

A la derecha, imagen decorativa de una mano robótica sobre un mapa de Sudamérica (sin contenido informativo).

## Slide 3

Slide de portada de sección con roadmap del curso. Texto: "CS2041 / Bases de Datos I / Ciclo 2024-1".

Diagrama tipo línea de tiempo horizontal con 8 bloques de barras de color (temas del curso), de izquierda a derecha:
Introducción → Modelo Relacional → Algebra Relacional & Cálculo Relacional → SQL → Entidad-Relación → Actualización, Restricciones → Formas Normales (resaltado, barra activa) → Optimización y Procesamiento (recuadro celeste destacado como próximo tema) → meta (bandera a cuadros, ícono decorativo de "llegada").

Un ícono decorativo de mago/ninja apuntando con una vara hacia la barra "Formas Normales" (mascota recurrente del curso).

## Slide 4

Slide de transición/portada de capítulo. Solo texto: "FORMAS NORMALES" (título grande gris) y referencia bibliográfica "Capítulo 12 | Ramakrishnan / Gehrke" abajo a la derecha. Resto de la slide en blanco.

## Slide 5

Título: "Hacia un buen diseño".

Tabla grande (10 filas de datos + fila de puntos suspensivos) con columnas: Nombre Municipalidad, Departamento, Tasa x m2, DNI, Nombre, Apellido, Rol Lote, M2, Avalúo.

| Nombre Municipalidad | Departamento | Tasa x m2 | DNI | Nombre | Apellido | Rol Lote | M2 | Avalúo |
|---|---|---|---|---|---|---|---|---|
| A | I | 2 | 111111 | Claudio | Gonzalez | 34 | 455 | 910 |
| A | I | 2 | 111111 | Claudio | Gonzalez | 35 | 570 | 1140 |
| A | I | 2 | 222222 | Maria | Zapata | 27 | 895 | 1790 |
| B | III | 1.1 | 111111 | Claudio | Gonzalez | 10 | 150 | 165 |
| B | III | 1.1 | 333333 | Carlos | Fernandez | 11 | 200 | 220 |
| B | X | 1.1 | 444444 | Elena | Abarca | 13 | 150 | 165 |
| C | V | 0.5 | 555555 | Luisa | Muñoz | 2 | 500 | 250 |
| D | V | 3.5 | 111111 | Claudio | Gonzalez | 11 | 100 | 350 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| G | III | 4.5 | 111111 | Claudio | Gonzalez | 62 | 200 | 220 |

Sobre la tabla hay flechas curvas rojas que conectan visualmente: (Nombre Municipalidad, Departamento) → (Tasa x m2); (DNI) → (Nombre, Apellido); y una flecha larga que conecta (Nombre Municipalidad, Departamento, Rol) → (DNI). Estas flechas ilustran las dependencias funcionales que se explican en la slide siguiente. Además, algunas filas están resaltadas con recuadros de color para mostrar repetición de datos: filas de "A/I/2" resaltadas en naranja (mismo DNI 111111 repetido), filas de "B/III/1.1" resaltadas en verde, y la fila "D" y "G" con recuadro rojo alrededor del DNI 111111 repetido — todas ilustran redundancia del mismo Claudio Gonzalez apareciendo múltiples veces.

## Slide 6

Título: "Dependencias funcionales".

Texto: "Esas 'relaciones' de dependencia se llaman dependencias funcionales:"

Lista de dependencias funcionales (formato matemático):
- NombreMuni, Departamento → Tasa
- DNI → Nombre, Apellido
- NombreMuni, Departamento, Rol → DNI
- Tasa, m2 → Avalúo

Pregunta: "¿hay otras?"

Debajo, encabezado de tabla vacío (solo headers, sin filas) repitiendo las columnas: Nombre Municipalidad, Departamento, Tasa x m2, DNI, Nombre, Apellido, Rol Lote, M2, Avalúo.

## Slide 7

Título: "Dependencias funcionales" (continuación).

Texto: "Pregunta capciosa: Dadas las dependencias funcionales anteriores, ¿cuál son las llave de este esquema?"

Repite las 4 DFs:
- NombreMuni, Departamento → Tasa
- DNI → Nombre, Apellido
- NombreMuni, Departamento, Rol → DNI
- Tasa, m2 → Avalúo

Respuesta destacada en un recuadro rojo/burdeos: "¿cuál son las llave de este esquema?" → respuesta: **{NombreMuni, Departamento, Rol}**

## Slide 8

Título: "Idea de buen diseño". Texto: "Cada 'tema' en una tabla aparte:"

Misma tabla completa de la slide 5 (Nombre Municipalidad, Departamento, Tasa x m2, DNI, Nombre, Apellido, Rol Lote, M2, Avalúo) con las 10 filas de datos, presentada sin resaltados/flechas — como punto de partida antes de descomponerla.

## Slide 9

Título: "Idea de buen diseño" / "Un modelo (casi) ideal". Texto: "Cada 'tema' en una tabla aparte:"

Muestra la descomposición de la tabla original en 3 tablas separadas por color, cada una representando un "tema":

Tabla 1 (naranja) — Municipalidad: Nombre Municipalidad, Departamento, Tasa x m2 (8 filas: A/I/2, B/III/1.1, B/V/1.1, B/X/1.1, C/V/0.5, D/V/3.5, ...).

Tabla 2 (verde) — Persona: DNI, Nombre, Apellido (111111 Claudio Gonzalez, 222222 Maria Zapata, 333333 Carlos Fernandez, 444444 Elena Abarca, 555555 Luisa Muñoz, ...).

Tabla 3 (azul) — Lote: Rol Lote, M2, Avalúo (34/455/910, 35/570/1140, 27/895/1790, 10/150/165, 11/200/220, 13/150/165, 2/500/250, ...).

## Slide 10

Continuación de la slide 9 ("Idea de buen diseño" / "Un modelo (casi) ideal"): las mismas 3 tablas (Municipalidad naranja, Persona verde, Lote azul) reproducidas con datos similares, ahora agregando debajo las 4 dependencias funcionales:
- NombreMuni, Departamento → Tasa
- DNI → Nombre, Apellido
- NombreMuni, Departamento, Rol → DNI
- Tasa, m2 → Avalúo

Un recuadro rojo con flecha señala hacia las dos últimas DFs (las que cruzan tablas) con el texto: "Pero perdimos las relaciones entre ellos" — indicando que al separar en 3 tablas independientes se pierde la relación entre Municipalidad, Persona y Lote (el vínculo Rol→DNI y Tasa,m2→Avalúo ya no puede reconstruirse solo con esas 3 tablas sueltas).

## Slide 11

Título: "Normalización de las relaciones". Ilustración decorativa de un mago/ninja apuntando con una vara (mascota recurrente).

Dos bullets con definiciones:
- **Normalización.** El proceso de descomponer las relaciones "malas" insatisfactorias dividiendo sus atributos en relaciones más pequeñas.
- **Forma normal.** Condición mediante el uso de claves y DF de una relación para certificar si un esquema de relación se encuentra en una forma normal particular.

## Slide 12

Título: "Normalización de las relaciones".

Diagrama: a la izquierda una lista vertical de formas normales (1FN, 2FN dentro de un círculo negro; 3FN, Boyce-Codd dentro de un óvalo morado; 4FN, 5FN dentro de un círculo naranja). Flechas conectan cada grupo a la derecha con su criterio de clasificación:
- 1FN/2FN → "MALAS"
- 3FN/Boyce-Codd → "Dependencias funcionales" (llave morado) → "BUENAS"
- 4FN/5FN → "Dependencias Multivaluadas" (naranja) y "Dependencias de JOIN" (verde) → también apunta a "BUENAS"

Es un mapa visual jerárquico mostrando cómo las formas normales avanzadas (3FN en adelante) se basan en DFs/MVDs/JOINs y llevan a relaciones "buenas", mientras 1FN/2FN solas son insuficientes ("malas").

## Slide 13

Título: "Normalización de las relaciones". Mascota mago/ninja a la izquierda.

Dos bullets:
- **2NF, 3NF, BCNF.** basadas en claves y DF de un esquema de relación.
- **4NF** basado en claves, dependencias de múltiples valores: MVDs; 5NF basado en claves, unir dependencias.

Texto adicional en morado: "Es posible que se necesiten propiedades adicionales para garantizar un buen diseño relacional (unión sin pérdida, conservación de la dependencia; Capítulo 11)".

## Slide 14

Título: "Normalización de las relaciones". Mascota mago/ninja a la izquierda.

Definiciones (texto en azul y rojo):
"Un dominio es **atómico** si se considera que los elementos del dominio son unidades indivisibles."

"Un esquema relacional R está en primera **1NF** si los dominios de todos los atributos de R son atómicos"

## Slide 15

Título: "Normalización de las relaciones". Mascota mago/ninja a la izquierda.

Texto: "No permite" (azul) con sub-bullets:
- atributos compuestos
- atributos multivaluados
- relaciones anidadas; atributos cuyos valores para una tupla individual no son atómicos

"Considerado como parte de la definición de una relación." (naranja)

"La mayoría de los RDBMS permiten que solo se definan las relaciones que están en Primera Forma Normal" (verde)

## Slide 16

Título: "Normalización de las relaciones". Mascota mago/ninja a la izquierda.

Diagrama entidad-relación tipo Chen: rectángulo central "ENTIDAD" conectado por líneas a 5 óvalos:
- "Atributo" (óvalo simple, arriba izquierda)
- "Atributo Multivaluado" (óvalo de doble línea, arriba derecha — notación estándar para multivaluado)
- "Atributo de Entidad Débil" (óvalo abajo izquierda)
- "Atributo Clave" (óvalo subrayado, abajo centro — notación de clave)
- "Atributo Derivado" (óvalo de línea punteada, derecha — notación de derivado)

Diagrama de repaso de la notación ER para tipos de atributos, relevante para entender por qué el "Atributo Multivaluado" viola 1NF.

## Slide 17

Título: "Normalización de las relaciones". Mascota mago/ninja a la izquierda.

Esquema de relación: **Matricula(dni, nombres, ApePat, ApeMat, cursos)** — con "dni" subrayado (clave) y "cursos" en azul (implícitamente multivaluado).

Recuadro punteado: "¿Algún problema aquí? …" (el atributo "cursos" no es atómico si un alumno tiene varios cursos).

## Slide 18

Título: "Normalización de las relaciones". Mascota mago/ninja a la izquierda.

Recuadro: "¿La solución? …" → "Crear otra tabla con Alumnos y Matrícula"

Esquemas resultantes:
- **Alumnos(dni, nombres, ApePat, ApeMat)**
- **Matricula(dni, curso)**

## Slide 19

Título: "Todo bien". 

Tabla de ejemplo "Cliente":
| rut | nombre | fono | dirección |
|---|---|---|---|
| 32.000.273-K | Kelvin | +56976698463 | Campo de Hielo Sur, Depto 273 |

Pregunta en recuadro punteado: "¿Pero si un cliente puede tener varios números de teléfono?" seguida de "…" en verde, anticipando el problema de la próxima slide.

## Slide 20

Título: "UNF: Forma No Normalizada (UnNormalised Form)".

Tabla "Cliente" ahora con 2 filas, la segunda con múltiples valores en la celda "fono":
| rut | nombre | fono | dirección |
|---|---|---|---|
| 32.000.273-K | Kelvin | +56976698463 | Campo de Hielo Sur, Depto 273 |
| 12.491.671-K | Rankine | +56991324842,+56223491234 | Campo de Hielo Norte, Depto 502 |

Recuadro amarillo destacado: "**UNF:** Varias multiplicidades de valores en una columna de la tabla" — ilustra visualmente la violación de 1NF (celda con dos teléfonos separados por coma).

## Slide 21

Título: "1NF: Primera Forma Normal (First Normal Form)".

Recuadro amarillo: "**1NF:** Un valor en cada celda de la tabla" (texto solo, sin tabla en esta slide — es la definición contraste con el UNF anterior).

## Slide 22

Título: "¿Todo bien con sola la 1NF?".

Tabla "Cliente" ahora normalizada a 1NF, la fila de Rankine se separó en dos filas (una fila por cada teléfono):
| rut | nombre | fono | dirección |
|---|---|---|---|
| 32.000.273-K | Kelvin | +56976698463 | Campo de Hielo Sur, Depto 273 |
| 12.491.671-K | Rankine | +56991324842 | Campo de Hielo Norte, Depto 502 |
| 12.491.671-K | Rankine | +56223491234 | Campo de Hielo Norte, Depto 502 |

Pregunta: "¿Algún problema aquí? …"

## Slide 23

Título: "¿Todo bien con sola la 1NF? No" (con "No" en rojo).

Misma tabla Cliente en 1NF (3 filas, Rankine duplicado).

Recuadro amarillo aparte: "Soluciones con nulos no cuentan aquí."

Análisis de problemas en recuadros rojos:
- "¿Algún problema aquí? …" → **Redundancia**
- "¿Pero por qué es un problema? ¿Sólo espacio? …"
- **Anomalía de actualización:** Por ejemplo, se puede actualizar la dirección de Rankine en un lugar sin actualizar todos los valores
- **Anomalía de inserción:** No podemos insertar un nuevo cliente a la tabla hasta tengamos un número de teléfono
- **Anomalía de borrado:** Si el número de teléfono ahora está invalido, tendremos que borrar la fila entera con la dirección, etc.

## Slide 24

Título: "¿Todo bien con sola la 1NF? No".

Misma tabla Cliente en 1NF (3 filas).

Recuadro: "¿La solución? …" → "Crear otra tabla con rut y fono"

Pregunta final abierta: "¿Pero cómo podemos definir el problema aquí? …"

## Slide 25

Slide decorativa: solo un ícono grande de reloj con flecha circular apuntando a la izquierda (ícono de "retroceso/repaso"), fondo blanco, sin texto. Marca transición de sección (recordatorio/repaso).

## Slide 26

Título: "Modelo Relacional: Restricciones (Llaves)".

Definición con texto coloreado por concepto:
"Un **conjunto de atributos** de **una relación** forma **una llave candidata** si es una **súper llave** y no hay un **subconjunto propio** de esos atributos que es una súper llave"

## Slide 27

Título: "Modelo Relacional: Restricciones (Llaves)".

Esquema: **Persona(rut, nombre, fecha-de-nacimiento, madre-rut, padre-rut)** con "rut" subrayado.

Pregunta: "¿Hay otra llave candidata?"

Dos posibles respuestas en recuadros de color:
- Verde: "Probablemente …" → Persona(rut, **nombre**, fecha-de-nacimiento, **madre-rut**, padre-rut) — con nombre y madre-rut subrayados como llave candidata alternativa.
- Naranja: "…o puede ser…" → Persona(rut, **nombre**, fecha-de-nacimiento, madre-rut, **padre-rut**) — con nombre y padre-rut subrayados, más nota "(si no tenemos un tipo como Gengis Kan)" — chiste sobre que Gengis Kan tuvo muchísimos hijos, rompiendo la unicidad de (nombre, padre-rut).

## Slide 28

Título: "Modelo Relacional: Restricciones (Llaves)".

Definición: "Un **atributo** es **primo** si está en alguna **llave** candidata"

## Slide 29

Slide decorativa: ícono grande de reloj con flecha circular apuntando a la derecha, fondo blanco, sin texto. Marca otra transición de sección.

## Slide 30

Título: "Como obtener clave candidatas / desde las Dependencias funcionales" (segunda línea en color morado).

Definición: "Una **llave** (súper o candidata) de **una relación** determina funcionalmente a todos los atributos de la relación"

## Slide 31

Título: "Como obtener clave candidatas" / "Heurística de solución" (morado).

Texto: "Sea la relación R y su conjunto de DFs F y Sea S el conjunto de llaves candidatas:"

Algoritmo numerado:
1. Para cada atributo atómico Ai de R
   - Si {Ai}⁺ = R → Entonces Ai es una llave candidata S=S ∪ Ai
2. Para cada par de atributos Ai ∉ S y Aj ∉ S
   - Si {AiAj}⁺ = R → Entonces S=S ∪ {AiAj}
3. Continuar para tres atributos ...

## Slide 32

Título: "Como obtener clave candidatas" / "Heurística de solución: Ejemplo" (morado).

Ejemplo: Sea la relación **R(A, B, C, D, E)** y **F={BD→E, CD→AB, E→C, B→D}**

Cálculo de clausuras:
- {E}⁺ = {E,C}
- {B}⁺ = **{B,D,E,C,A}** (resaltado en negrita, indica que = R, o sea B es llave candidata)
- {CD}⁺ = **{C,D,A,B,E}** (resaltado en negrita, CD también es llave candidata)
- {AC}⁺ = {A,C}
- {AD}⁺ = {A,D}

## Slide 33

Título: "Descomposición" / "Definición" (morado).

Texto: "Sea la relación R y su conjunto de DFs F / Una descomposición R1 y R2 sin pérdida:"

Recuadro amarillo con 3 condiciones:
- Conservan los atributos de R → R = R1 ∪ R2
- Conservan las dependencias funcionales → F⁺ = {F1 ∪ F2}⁺
- No genera tuplas falsas, para ello: {R1 ∩ R2} → R1 ó {R1 ∩ R2} → R2
  - *La intersección genera una DF válida en F (nota en rojo)

## Slide 34

Título: "Descomposición" / "Ejemplo 1" (morado).

Sea **R(A,B,C,D,E)** y **F={AB→C, C→D, C→E}**. La descomposición **R1(A,B,C,D)** y **R2(C,E)** genera F1={AB→C, C→D} y F2={C→E}

Verificación:
- Sí conservan los atributos de R
- Sí conserva las dependencias funcionales
- No genera tuplas falsas, ya que: {R1 ∩ R2} → R2, y C → E ⊂ F⁺

## Slide 35

Título: "Descomposición" / "Ejemplo 2" (morado).

Sea **R(A,B,C,D,E,F)** y **F= {AB→D, AC→E, ABD→F}**. La descomposición **R1(A,B,D,F)** y **R2(A,C,E)** genera F1={AB→D, ABD→F} y F2={AC→E}

Verificación (con "A,B,C" subrayados como clave en R):
- Sí conservan los atributos de R
- Sí conserva las dependencias funcionales
- **SÍ genera tuplas falsas** (en rojo), ya que: {R1 ∩ R2} → R1: A → BDF ⊄ F⁺; {R1 ∩ R2} → R2: A → CE ⊄ F⁺

Ejemplo de descomposición "mala" que sí produce join lossy.

## Slide 36

Título: "Recordando! Dependencias parciales".

Texto explicativo: "Dependencia parcial significa que un **atributo no primo** depende funcionalmente de parte de una clave candidata. (Un **atributo no primo** es un atributo que no forma parte de ninguna clave candidata)."

"Por ejemplo, comencemos con R{ABCD} y las dependencias funcionales AB→CD y A→C."

"La única clave candidata para R es AB. C y D son atributos no primo. C depende funcionalmente de A. A es parte de una clave candidata. Eso es una dependencia parcial."

Diagrama debajo con tabla "PROGRAM" de 5 columnas: codProgramador, codModulo, nomProgramador, nomModulo, horasTrab (los dos primeros con subrayado, clave compuesta). Flechas curvas de colores indican:
- Flecha azul arriba: "Dependencia funcional completa" — desde {codProgramador, codModulo} hacia nomProgramador, nomModulo, horasTrab (toda la clave compuesta determina esos atributos).
- Flecha amarilla: "Dependencia funcional parcial" — desde codModulo hacia nomModulo.
- Flecha roja abajo: "Dependencia funcional parcial" — desde codProgramador hacia nomProgramador.

Diagrama concreto que ilustra visualmente cómo codProgramador (parte de la clave) determina por sí solo a nomProgramador, y codModulo determina por sí solo a nomModulo — ambas dependencias parciales que violan 2FN.

## Slide 37

Título: "Normalización en 2FN".

- **Definición**
  - Está en 1FN
  - Cada atributo no primo depende funcionalmente de manera total de toda clave de R
- **Descomposición**
  - Las DF parciales (no totales) se llevan a nuevas tablas.
  - En la tabla original queda la clave y los atributos que dependen totalmente de ella

## Slide 38

Título: "Normalización en 2FN" / "Ejemplo".

Sea **R(A,B,C,D,E)** y **F = {AB→ CE, B→D}** — No está en 2FN

Descomposición:
- DF Parcial AB→CE, entonces:
  - **R1(A,B,C,E)**
  - **R2(B,D)**
    - (R1∩R2 → R2) ⊂ F⁺

## Slide 39

Título: "Normalización en 3FN".

- **Definición**
  - Está en 2FN
  - Una tabla está en 3FN ssi para toda df no trivial X→Y en R: X es superclase ó Y es atributo primo
- **Descomposición**
  - R(A,X,Y,B) donde X → Y incumple 3FN
  - Crear otra relación con X⁺, donde X es clave
  - Eliminar Y de R

(Nota: esta descripción corresponde también a la slide 44, que trae el diagrama visual asociado — ver ahí).

## Slide 40

Título: "Normalización en 3FN" / "Ejemplo".

Sea **R(A,X,Y,B)** y **F = {A →XB, X→Y}**. No es 3FN, X no es superclave.

Tomando las F como base:
- **R1(A,X,B)**
- **R2(X,Y)**
  - (R1∩R2 → R2) ⊂ F⁺

## Slide 41

Título: "Normalización en 3FN" (continuación) / "Descomposición (usando F⁻)".

- Calcular F mínimo
- Convertir cada dependencia en una relación (X → Y ⇒ Ri(XY))
- Si no está la llave en una relación, agregarla

## Slide 42

Título: "Normalización en 3FN" / "Ejemplo".

Sea **R(A, B, C, D, E)** y **F = {A → B, A → C, C → D, B → E}**. F es mínimo.

{A}⁺ = {A,B,C,D,E} ⇒ A es clave única

Tomando las cuatro DFs:
- R1(A,B), preserva la clave
- R2(A,C), preserva la clave
- R3(C,D)
- R4(B,E)

## Slide 43

Título: "Normalización en FNBC".

- **Definición**
  - Está en 3FN (... válido desde 1FN)
  - Para toda DF X→Y en R: X es superclave

Diagrama: fila de columnas A,B,C,D,E,F,G donde A,B están agrupados (resaltados naranja) como superllave, con flecha curva roja desde A,B hacia el resto (C-G), ilustrando "X es superclave → determina todo el resto".

- **Descomposición**
  - R(A,X,Y,B) donde X → Y incumple FNBC
  - Crear dos relaciones: R1 = R - Y ; R2(X,Y)

Nota en rojo al pie: "Esta estrategia de normalización no asegura preservar dependencias, pero sí asegura la recuperación de la información por join."

## Slide 44

Título: "Normalización en FNBC" / "Ejemplo".

Sea **R(A, B, C, D, E)** y **F = {A → BC, C → D, B → E}**.

1. R no está en FNBC, C→D incumple FNBC. Partimos: R1(A,B,C,E) y R2(C,D).
2. R1 no está en FNBC, B→E incumple FNBC. Partimos: R3(A,B,C) y R4(B,E)

**Resultado: R2(C,D), R3(A,B,C) y R4(B,E)**

## Slide 45

Título: "Ejercicio" (sin sección de curso en el encabezado, formato distinto).

Enunciado: R(A,B,C,D,E) y F{A->B, A->D, C->E} Normalizar en 3FN y FNBC

Resolución paso a paso:
- AC -> ABCDE, AC es una superllave.
- No hay atributos primos y tampoco está en 3FN
- A->B y A->D ⇒ A->BD
- C->E viola FNBC. Partimos R1(ABCD) y R2(CE)
- A-BD viola FNBC. Partimos R3(AC) y R4(ABD)

## Slide 46

Título: "Resumen".

1. Buen diseño evita anomalías
2. Las dependencias funcionales ayudan a un buen diseño
3. Ideal es FNBC, pero no siempre se logra
4. Pero siempre se puede 3FN

## Slide 47

Título: "Preguntas?". Imagen decorativa de un muñeco de nieve con bufanda amarilla frente a una casa nevada — foto de cierre sin contenido académico.

## Slide 48

Slide de cierre decorativa: fondo azul con foto de dos estudiantes con guantes de laboratorio (decorativa), logo UTEC y tagline "Reinventa el mundo" (decorativo).

Texto: "GRACIAS" (grande) — "TEÓFILO CHAMBILLA". Logo TransformaTec al pie (decorativo).
