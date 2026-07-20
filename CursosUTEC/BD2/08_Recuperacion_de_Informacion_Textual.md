---
curso: BD2
titulo: 08 Recuperación de Información Textual
slides: 87
fuente: 08 Recuperación de Información Textual.pdf
---

# 08 Recuperación de Información Textual

**Figura:** Slide de portada con fondo fotográfico de un túnel o corredor circular futurista en tonos azules profundos, con patrones tecnológicos, anillos concéntricos luminosos y líneas tipo circuito. En el centro, una persona vista de espaldas camina hacia el interior del túnel; la persona parece tener una pierna protésica en el lado derecho. En la parte superior central, el código y nombre del curso «CS2042 - BASES DE DATOS II». En el centro, el título principal «Base de Datos Vectoriales» en letras grandes blancas; debajo, «SEMANA 08» en cursiva. Una línea horizontal punteada amarilla separa el título de los datos del instructor: «Heider Sanchez» y «hsanchez@utec.edu.pe».

## Índice

| Sección | Tema |
|---|---|
| 1 | [Modelos de Recuperación de Información](#modelos-de-recuperación-de-información) |
| 1.1 | [Tratamiento de datos no estructurados](#tratamiento-de-datos-no-estructurados) |
| 1.2 | [Solución en base de datos relacionales](#solución-en-base-de-datos-relacionales) |
| 1.3 | [Information Retrieval](#information-retrieval) |
| 2 | [Modelos de Recuperación de Texto: Bag of Words](#modelos-de-recuperación-de-texto-bag-of-words) |
| 2.1 | [Vectorización del texto](#vectorización-del-texto) |
| 2.2 | [Preprocesamiento](#preprocesamiento) |
| 2.3 | [Ponderación y selección de keywords](#ponderación-y-selección-de-keywords) |
| 2.4 | [Ejemplo](#ejemplo) |
| 2.5 | [Modelo Booleano](#modelo-booleano) |
| 2.6 | [Bag of Words en PostgreSQL](#bag-of-words-en-postgresql) |
| 3 | [Modelos de Recuperación de Texto: TF-IDF y Similitud de Coseno](#modelos-de-recuperación-de-texto-tf-idf-y-similitud-de-coseno) |
| 3.1 | [Problemas con la búsqueda booleana](#problemas-con-la-búsqueda-booleana) |
| 3.2 | [Ranked Retrieval](#ranked-retrieval) |
| 3.3 | [Term Frequency (TF)](#term-frequency-tf) |
| 3.4 | [Document Frequency e IDF](#document-frequency-e-idf) |
| 3.5 | [Ponderación TF-IDF](#ponderación-tf-idf) |
| 3.6 | [Espacio vectorial y proximidad](#espacio-vectorial-y-proximidad) |
| 3.7 | [Similitud de coseno](#similitud-de-coseno) |
| 3.8 | [Ejemplo de consulta TF-IDF](#ejemplo-de-consulta-tf-idf) |
| 3.9 | [Resumen de Ranked Retrieval](#resumen-de-ranked-retrieval) |
| 4 | [Índice Invertido](#índice-invertido) |
| 4.1 | [Desventajas de la matriz vectorial](#desventajas-de-la-matriz-vectorial) |
| 4.2 | [Estructura del índice invertido](#estructura-del-índice-invertido) |
| 4.3 | [Consultas booleanas sobre el índice](#consultas-booleanas-sobre-el-índice) |
| 4.4 | [Ejemplo de construcción y consulta](#ejemplo-de-construcción-y-consulta) |
| 4.5 | [Índice invertido con similitud de coseno](#índice-invertido-con-similitud-de-coseno) |
| 5 | [Glosario](#glosario) |

## Modelos de Recuperación de Información

**Figura:** Slide dividida en dos zonas. en el centro un número grande «1.» con subrayado azul, un icono de portapapeles azul con lista de verificación, y el título «Modelos de Recuperación de Información» con subtítulo «Introducción» en cursiva azul claro.

### Tratamiento de datos no estructurados

En las aplicaciones modernas, resulta fundamental el procesamiento eficiente de datos no estructurados para permitir consultas basadas en su contenido. Esto requiere la integración de técnicas avanzadas de indexación, que optimicen la velocidad y precisión de las búsquedas.

```sql
-- Buscar artículos que contengan la frase "big data y análisis de datos" en su contenido
SELECT id, titulo, contenido
FROM articulos
WHERE MATCH(contenido_vector, "big data y análisis de datos");

-- Buscar rostros similares a una foto de un empleado
SELECT id, nombre, fecha_registro, rostro_path
FROM fotos_empleados
WHERE MATCH(rostro_vector, ExtractVector('/path/to/any_photo.jpg'));
```

**Figura:** Slide dividida en dos columnas. Columna izquierda: diagrama de una base de datos multimodal. En el centro, un cilindro naranja etiquetado «MULTIMODAL DATABASE». Desde él salen flechas hacia cinco iconos periféricos que representan tipos de datos: «TEXT» (icono de documento), «IMAGES» (icono de montaña/foto), «VIDEO» (icono de película), «TABULAR DATA» (icono de hoja de cálculo) y «AUDIO» (icono de altavoz). Columna derecha: el párrafo descriptivo en español (con «basadas en su contenido» y «optimicen la velocidad y precisión de las búsquedas» resaltados en negrita) y, debajo, un recuadro azul claro con los dos ejemplos SQL de búsqueda vectorial. Acento triangular azul en el borde superior izquierdo.

Ejemplo: Full-Text Search en Repositorio Científico

https://www.youtube.com/watch?v=ACp_GgtZ6IA

**Figura:** Slide con título «Ejemplo: Full-Text Search en Repositorio Científico» en la parte superior. En el centro, un recuadro que contiene una captura de pantalla borrosa de una interfaz de repositorio científico. En la esquina superior izquierda del recuadro aparece el texto «We provide wordcloud for each article.». En el centro del recuadro hay una nube de palabras multicolor con muchos términos pequeños. Debajo de la nube de palabras, una línea de texto borrosa que parece ser una ruta o nombre de archivo de artículo, terminando en «...-meta-algorithm-with-provable-guarantees.txt». En la parte inferior central de la slide, la URL del video de YouTube.

Ejemplo: Búsquedas en Google

**Figura:** Diagrama de flujo que ilustra una búsqueda en Google con tres componentes conectados por flechas. Arriba a la derecha: captura de la página de inicio de Google (`www.google.com/webhp`) con la barra de búsqueda rellena con la consulta «TREC conference». Una flecha descendente apunta desde esta captura hacia un recuadro central con borde azul etiquetado «Google». Debajo del recuadro «Google» hay un icono de nube azul etiquetado «Web», conectado al recuadro «Google» mediante una flecha vertical de doble sentido (interacción bidireccional entre el motor de búsqueda y la Web). Una flecha horizontal apunta desde el recuadro «Google» hacia la izquierda, hacia una captura de la página de resultados (`www.google.com/search`) para la consulta «TREC conference», mostrando enlaces como «Text REtrieval Conference (TREC) Home Page» (trec.nist.gov), «Text REtrieval Conference (TREC) | NIST» (nist.gov) y «Text Retrieval Conference - Wikipedia».

(slides 3–5)

### Solución en base de datos relacionales

- Los datos se manejan en tablas de acuerdo al modelo relacional
- El campo textual generalmente es un atributo de tipo **text**
- En las búsquedas se utiliza el operador **like** o **ilike**

**Figura:** Slide con título «Solución en Base de Datos Relacionales» en la parte superior izquierda. Tres viñetas de texto en el cuerpo de la slide; los términos «text», «like» e «ilike» aparecen en negrita.

```sql
Select * from News
where content ilike '%keyword1%'
  and content ilike '%keyword2%'
```

| Id | Title | Content | Date |
| :--- | :--- | :--- | :--- |

**Figura:** Diagrama de flujo cíclico con cuatro componentes conectados por flechas. Una flecha apunta desde la interfaz de búsqueda hacia arriba a la derecha, donde aparece la consulta SQL `Select * from News where content ilike '%keyword1%' and content ilike '%keyword2%'`. Una flecha descendente conecta la consulta SQL con una representación de almacenamiento en la parte inferior derecha: una tabla con columnas «Id», «Title», «Content» y «Date», junto a un icono de cilindro gris que representa la base de datos. Una flecha desde la base de datos apunta hacia abajo a la izquierda, hacia una tabla de resultados con columnas «Year» (todas las filas visibles muestran «2018»), «Similarity» (todas «1.0»), «Author» (nombres como «Casals», «Castro», «Chen»), «Article» (títulos de artículos científicos con etiquetas de palabras clave, por ejemplo «brain computer interface with corrupted eeg data a tensor completion approach», «inferno inference aware neural optimisation», «on landscape of lagrangian function and stochastic search for constrained nonconvex optimization»), «# of words» (valores como 20687, 5400, 31248) y «Detail» (botón azul «Abstract» en cada fila).

```sql
Select * from News
where content ilike '%keyword1%' and content ilike '%keyword2%'
```

En producción la aplicación no sirve …
¿Por qué?

1. No se considera la relación léxica de palabras en textos escrito por humanos.
2. Demasiados resultados sin ordenar desesperan al usuario.
3. Excesivo tiempo computacional para grandes cantidades de datos.

**Figura:** Slide con título «Solución en Base de Datos Relacionales». En la parte superior, la consulta SQL en texto azul/cian. Debajo, en rojo y negrita, la pregunta «En producción la aplicación no sirve … ¿Por qué?». A continuación, una lista numerada de tres razones, también en rojo.

```sql
CREATE TABLE articulos (
    id INT PRIMARY KEY,
    contenido TEXT
);

INSERT INTO articulos (id, contenido) VALUES
(1, 'Aprender a programar es esencial en el mundo actual.'),
(2, 'La programación es una habilidad clave para los desarrolladores.'),
(3, 'Los programadores crean soluciones innovadoras con código.');
```

```sql
SELECT * FROM articulos
WHERE contenido LIKE '%programación%' OR LIKE '%desarrollador%';
```

**Figura:** Slide con título «Solución en Base de Datos Relacional». En la parte superior, consulta SQL en texto azul/cian (`Select * from News where content ilike '%keyword1%' and content ilike '%keyword2%'`). Debajo, en rojo, «En producción la aplicación no sirve ... ¿Por qué?». Punto 1 en rojo y negrita: «No se considera la relación léxica de palabras en textos escrito por humanos.». En la parte inferior, dos recuadros de código SQL lado a lado: el izquierdo con `CREATE TABLE articulos` e `INSERT INTO articulos` con tres filas de datos de ejemplo sobre programación; el derecho con `SELECT * FROM articulos WHERE contenido LIKE '%programación%' OR LIKE '%desarrollador%';` (la segunda parte del WHERE carece de nombre de columna antes del segundo LIKE, tal como aparece en la slide).

```sql
Select * from News
where content ilike '%keyword1%' and content ilike '%keyword2%'
```

En producción la aplicación no sirve …

¿Por qué?

1. ~~No se considera la relación léxica de palabras en textos escrito por humanos.~~
2. Demasiados resultados sin ordenar desesperan al usuario.
3. Excesivo tiempo computacional para grandes cantidades de datos.

**Figura:** Consulta SQL en fuente azul/cian. Texto en rojo «En producción la aplicación no sirve ...» seguido de «¿Por qué?» en negrita. Tres razones numeradas en rojo y negrita; el punto 1 aparece tachado. Acento triangular azul en el borde superior izquierdo.

Tras abordar el preprocesamiento léxico (Bag of Words), la limitación 1 queda resuelta:

1. ~~No se considera la relación léxica de palabras en textos escrito por humanos.~~
2. Demasiados resultados sin ordenar desesperan al usuario.
3. Excesivo tiempo computacional para grandes cantidades de datos.

**Figura:** Consulta SQL en fuente azul/cian. Texto en rojo «En producción la aplicación no sirve ...» seguido de «¿Por qué?» en negrita. Tres razones numeradas en rojo; el punto 1 aparece tachado. Acentos azules en los bordes izquierdo y derecho.

Tras abordar TF-IDF y Ranked Retrieval, las limitaciones 1 y 2 quedan resueltas:

1. ~~No se considera la relación léxica de palabras en textos escrito por humanos.~~
2. ~~Demasiados resultados sin ordenar desesperan al usuario.~~
3. Excesivo tiempo computacional para grandes cantidades de datos.

Sobre la limitación 3 (tiempo computacional):

3. Excesivo tiempo computacional para grandes cantidades de datos.
   - Complejidad Computacional $O(N \cdot n)$
     - $N$: # tuplas, $n$: tamaño del texto
   - ¿Si aplicamos índice Hash o B+ Tree?

```sql
Select * from News
where content ilike '%keyword1%' and content ilike '%keyword2%'
```

En producción la aplicación no sirve …

¿Por qué?

1. No se considera la relación léxica de palabras en textos escrito por humanos.
2. Demasiados resultados sin ordenar desesperan al usuario.
3. Excesivo tiempo computacional para grandes cantidades de datos.

**Figura:** Los puntos 1 y 2 aparecen tachados (crossed out) en la slide; el punto 3 no está tachado.

Tras abordar el Índice Invertido, las tres limitaciones quedan resueltas:

1. ~~No se considera la relación léxica de palabras en textos escrito por humanos.~~
2. ~~Demasiados resultados sin ordenar desesperan al usuario.~~
3. ~~Excesivo tiempo computacional para grandes cantidades de datos.~~

```sql
Select * from News where content ilike '%keyword1%'
and content ilike '%keyword2%'
```

En producción la aplicación no sirve …

¿Por qué?

1. No se considera la relación léxica de palabras en textos escrito por humanos.
2. Demasiados resultados sin ordenar desesperan al usuario.
3. Excesivo tiempo computacional para grandes cantidades de datos.

**Figura:** Acento triangular azul en el borde superior izquierdo. Se muestra un bloque de código SQL con la consulta `Select * from News where content ilike '%keyword1%' and content ilike '%keyword2%'`. Debajo, en texto rojo y negrita: «En producción la aplicación no sirve …». Luego la pregunta «¿Por qué?» seguida de una lista numerada con tres razones, cada una tachada con una línea horizontal roja: (1) no se considera la relación léxica de palabras en textos escrito por humanos; (2) demasiados resultados sin ordenar desesperan al usuario; (3) excesivo tiempo computacional para grandes cantidades de datos.

(slides 6–8, 20, 30–33, 71–73, 86)

### Information Retrieval

- **Information Retrieval:** es la ciencia de la búsqueda de información en documentos digitales, de naturaleza no estructurada que satisfaga una necesidad de información dentro de grandes colecciones.

**Figura:** Slide con título «Information Retrieval» en la parte superior izquierda. Dos flechas azules descienden desde el recuadro de definición hacia un cilindro gris claro en la parte inferior etiquetado «Multimedia Database». Dentro del cilindro hay dos rectángulos azules: «Full-Text Search» (izquierda) y «Content-Based Image Search» (derecha).

**Full-Text Search: Inverted Index, TF-IDF, Cosine Similarity**

**Figura:** Slide con título «Information Retrieval». El recuadro superior contiene la definición de Information Retrieval (con «documentos digitales», «no estructurada» y «grandes colecciones» en negrita). El recuadro inferior contiene el texto «Full-Text Search: Inverted Index, TF-IDF, Cosine Similarity». Acento triangular azul en el borde superior izquierdo.

**Figura:** Diagrama de comparación vertical apilada de tres campos, de arriba hacia abajo:

1. **Artificial Inteligence** (izquierda): bloque rectangular amarillo con el texto «Conceptos + Conocimiento (cuerpo organizado de afirmaciones)».
2. **Data Bases** (izquierda): cilindro naranja (representación de base de datos) con el texto «Objetos (entidades) + relaciones».
3. **Information Retrieval** (izquierda): recuadro con borde azul que contiene dos grupos de iconos en blanco y negro de pilas de documentos/páginas, representando colecciones de documentos no estructurados.

Título «Information Retrieval» en la parte superior izquierda.

- 1950, Calvin N. Moores: "La búsqueda de información en un stock de documentos, efectuada a partir de la especificación de un tema"
- 1983, Salton: "La recuperación de la información tiene que ver con la representación, almacenamiento, organización y acceso a los elementos de la información."
- 1999, Ricardo Baeza: "La representación y organización debería proveer al usuario un fácil acceso a la información en la que se encuentra interesado. Desafortunadamente dicha caracterización no es un problema sencillo a resolver. "

Baeza-Yates, R., & Ribeiro-Neto, B. (1999). Modern information retrieval (Vol. 463). New York: ACM press.

**Figura:** Slide con título «Information Retrieval» y tres definiciones históricas en viñetas, cada una con año y autor. En la parte inferior, la cita bibliográfica de Baeza-Yates y Ribeiro-Neto.

- Primeras aplicaciones en bibliotecas (1950s)

| Campo | Valor |
| :--- | :--- |
| ISBN | 0-201-12227-8 |
| Author | Salton, Gerard |
| Title | Automatic text processing: the transformation, analysis, and retrieval of information by computer |
| Editor | Addison-Wesley |
| Date | 1989 |
| Content | `<Text>` |

- Atributos externos y atributos internos (contenido)
- Búsqueda por atributos externos = Búsqueda en BD
- Búsqueda por atributos internos = IR: búsqueda basado en contenido.

**Figura:** Slide con título «Information Retrieval». Primera viñeta sobre aplicaciones en bibliotecas en los años 1950, seguida de un ejemplo de metadatos bibliográficos de un libro (ISBN, Author, Title, Editor, Date, Content). Debajo, tres viñetas que contrastan atributos externos vs. internos y distinguen búsqueda en BD de búsqueda basada en contenido (IR).

- ¿Que tipo de información ahora se necesita recuperar?

  - Texto (documentos y/o porsiones de ello)
  - XML y otros documentos (semi) estructurados.
  - Codigo fuente
  - Imágenes
  - Audio (efectos de sonido, canciones, etc.)
  - Video
  - Aplicaciones Web Services

**Figura:** Slide con título «Information Retrieval». Pregunta central «¿Que tipo de información ahora se necesita recuperar?» con la palabra «ahora» resaltada en rojo. Debajo, lista anidada de siete tipos de información a recuperar.

Recuperación de Información vs Bases de Datos Relacionales

| | Recuperación en BD Relacionales | Recuperación de la información |
| :--- | :--- | :--- |
| Acierto | Exacto | Aproximado, El mejor |
| Inferencia | Algebraica | Inductiva |
| Modelo | Determinístico | Heurístico, Probabilístico |
| Lenguaje de consulta | Fuertemente estructurado | No-Estructurado, Natural |
| Especificación de consulta | Preciso | Imprecisa |
| Error en la respuesta | Sensible | Insensible |

**Figura:** Slide con título «Information Retrieval» y subtítulo «Recuperación de Información vs Bases de Datos Relacionales». Tabla comparativa de seis filas con encabezados en azul: primera columna con las categorías (Acierto, Inferencia, Modelo, Lenguaje de consulta, Especificación de consulta, Error en la respuesta), segunda columna «Recuperación en BD Relacionales» y tercera columna «Recuperación de la información». Filas alternadas en azul claro y blanco.

- Input:
  - Una gran colección de documentos de texto no estructurados.
  - Una consulta de usuario expresada como texto.
- Output:
  - Una lista ordenada de documentos que son relevantes para la consulta.

**Figura:** Diagrama de flujo de un sistema de Information Retrieval. A la izquierda, un icono de usuario (figura de palo) con signo de interrogación sobre la cabeza; Arriba del centro, un icono de pila de libros conectado a un óvalo azul «Collection of documents». Flechas desde «Query String» y desde «Collection of documents» convergen hacia un recuadro 3D verde etiquetado «IR System». Una flecha sale del lado derecho del «IR System» hacia un óvalo azul «Ranked Documents». Junto a este óvalo, un recuadro blanco con lista numerada: «1. Doc1», «2. Doc2», «3. Doc3», seguido de puntos suspensivos indicando más documentos.

- Proceso Genérico:

**Figura:** Diagrama de flujo del proceso genérico de recuperación de información. Arriba a la izquierda, silueta de usuario con tres signos de interrogación alrededor de la cabeza (buscador de información). Flecha hacia recuadro «Information Needed». Flecha hacia recuadro «Information Resource Selection». Desde «Information Resource Selection», flechas apuntan al recuadro central con borde azul «ISR System» y al cilindro azul grande a la derecha etiquetado «Documents» (con iconos de páginas apiladas en su interior). Flecha bidireccional entre «ISR System» y «Documents». Desde «ISR System», flecha hacia un recuadro inferior izquierdo dividido en «Relevant Documents» (iconos verdosos) y «No Relevant Documents» (iconos azul claro). Desde los resultados, flecha hacia recuadro «Result Evaluation». Desde «Result Evaluation», flecha de retroalimentación hacia el usuario (arriba a la izquierda) y otra flecha de retroalimentación hacia «ISR System».

- Disciplinas relacionadas

**Figura:** Diagrama de disciplinas relacionadas con Information Retrieval, organizado en cuatro cuadrantes delimitados por rectángulos punteados grises, cada uno con una etiqueta amarilla en su esquina exterior: arriba-izquierda «Mathematics», abajo-izquierda «Algorithms», arriba-derecha «Applications», abajo-derecha «Systems». En el centro, un óvalo amarillo etiquetado «Information Retrieval» en la intersección de los cuatro cuadrantes. Óvalos blancos periféricos con disciplinas específicas: a la izquierda (lado Mathematics/Algorithms) «Statistics Optimization» (extremo izquierdo), «Machine Learning / Pattern Recognition» (arriba-izquierda, solapándose con el centro), «Natural Language Processing» (directamente a la izquierda del centro), «Data Mining» (abajo-izquierda, solapándose con el centro). A la derecha (lado Applications/Systems) «Web Applications, Bioinformatics...» (arriba-derecha), «Library & Info Science» (centro-derecha), «Databases» (abajo-centro-derecha), «Software engineering / Computer systems» (abajo-derecha, solapándose con el centro). Los óvalos se solapan entre sí y con el óvalo central, mostrando la naturaleza multidisciplinaria del campo.

(slides 9–18)

## Modelos de Recuperación de Texto: Bag of Words

**Figura:** Slide dividida en dos zonas. en el centro un número grande «2.» con subrayado azul, un icono de portapapeles azul con lista de verificación, y el título «Modelos de Recuperación de Texto» con subtítulo «Bag of Words» en cursiva azul claro.

### Vectorización del texto

La técnica Bag of Words es muy utilizada en el Procesamiento del Lenguaje Natural (NLP) para transformar texto en una representación numérica vectorial con el fin de dar soporte a técnicas de Machine Learning e Information Retrieval (que generalmente operan en espacios vectoriales).

Este vector sirve como input para diferentes tareas :
- Clasificación de textos
- Clustering / Segmentación de textos
- Recuperación de la información (full-text search)
- Sistemas de Recomendación
- Análisis de sentimientos
- Detección de tópicos
- Etc.

**Figura:** En la parte inferior derecha, un ejemplo visual de conversión de cuatro oraciones en una matriz Bag of Words. Cuatro oraciones de entrada apuntan con flechas naranjas hacia una tabla con encabezado naranja:

1. "the red dog"
2. "cat eats dog"
3. "dog eats food"
4. "red cat eats"

La matriz tiene columnas de vocabulario: **the**, **red**, **dog**, **cat**, **eats**, **food**. Cada fila representa una oración, con valores `1` (presencia) o `0` (ausencia):

| Sentence | the | red | dog | cat | eats | food |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| 1. the red dog | 1 | 1 | 1 | 0 | 0 | 0 |
| 2. cat eats dog | 0 | 0 | 1 | 1 | 1 | 0 |
| 3. dog eats food | 0 | 0 | 1 | 0 | 1 | 1 |
| 4. red cat eats | 0 | 1 | 0 | 1 | 1 | 0 |

Acento triangular azul en el borde superior izquierdo.

**Bag of Words Model:**

1. **Corpus:** A collection of text documents.
2. **Tokenize:** Divide the text into smaller units called tokens, usually words or phrases.
3. **Count word frequencies:** Create a vocabulary of unique words and count the number of times each word appears in each document.
4. **Encode the data:** Encoding the text data as numerical values by creating a vector for each document, where each element represents the frequency count of a particular word.

**Example:**

- **Corpus:**
  - Document 1 (D1): "The dog is happy."
  - Document 2 (D2): "The child makes the dog happy."
  - Document 3 (D3): "The dog makes the child happy."

- **Tokenization:**
  - D1: `[The] [dog] [is] [happy]`
  - D2: `[The] [child] [makes] [the] [dog] [happy]`
  - D3: `[The] [dog] [makes] [the] [child] [happy]`

- **Counting Word Frequencies:**
  - D1: the: 1, dog: 1, is: 1, happy: 1
  - D2: the: 2, dog: 1, makes: 1, child: 1, happy: 1
  - D3: the: 2, child: 1, makes: 1, dog: 1, happy: 1

- **Data Encoding:**

| Encode | child | dog | happy | is | makes | the | BoW Vector representations |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| D1 | 0 | 1 | 1 | 1 | 0 | 1 | [0, 1, 1, 1, 0, 1] |
| D2 | 1 | 1 | 1 | 0 | 1 | 2 | [1, 1, 1, 0, 1, 2] |
| D3 | 1 | 1 | 1 | 0 | 1 | 2 | [1, 1, 1, 0, 1, 2] |

**Figura:** Slide dividido en dos columnas. Columna izquierda: cuatro pasos del modelo Bag of Words en recuadros naranjas. Columna derecha: ejemplo concreto con corpus, tokenización, conteo de frecuencias y tabla de codificación. Marca de agua central «© AIML.com Research». Acento triangular azul en el borde superior izquierdo.

(slides 21–22)

### Preprocesamiento

Etapas iniciales del procesamiento de texto

- Tokenización
  - Cortar la secuencia de caracteres del texto en tokens de palabras.
- Normalización
  - Mapear el texto y los términos de consulta a la misma forma.
    - ¿Quieres que O.N.U. y ONU coincidan?
- Reducción (stemming)
  - Podemos hacer coincidir palabras de la misma raíz.
    - autorizar, autorización
- Stop words
  - Podemos omitir palabras muy comunes (o no).
    - de, el, los, uno,

**Figura:** Cuatro viñetas principales con sub-viñetas que describen las etapas de preprocesamiento. Acentos azules en el borde izquierdo.

**Figura:** Flujograma vertical en el lado izquierdo con las siguientes etapas conectadas por flechas descendentes:

1. **Document**
2. **Tokenization**
3. **Lexical Analysis**
4. **Stop words Removal**
5. **Stemming and Lemmatization**

Existe una flecha de bypass desde «Lexical Analysis» directamente hacia «Stemming and Lemmatization», indicando que la eliminación de stop words puede omitirse o realizarse en otro momento.

En el lado derecho, un ejemplo en español:

- **Documento original:** «Mis amigas y amigos peruanos son estudiosos.»
- **Después de Tokenization/Stop words Removal:** cuatro recuadros con las palabras `amigas`, `amigos`, `peruanos`, `estudiosos` (se eliminaron «Mis», «y» y «son»).
- **Después de Stemming/Lemmatization:** tres recuadros con las formas reducidas `amigo`, `peruano`, `estudio` (`amigas` y `amigos` → `amigo`; `peruanos` → `peruano`; `estudiosos` → `estudio`).

En la parte inferior derecha, un recuadro con borde naranja:

- **Count word frequencies**
- Create a vocabulary of unique words and count the number of times each word appears in each document.

(slides 23–24)

### Ponderación y selección de keywords

**Figura:** Flujograma vertical en el lado izquierdo con las siguientes etapas conectadas por flechas descendentes:

1. **Document**
2. **Document Parsing**
3. **Lexical Analysis**
4. **Stop words Removal**
5. **Stemming and Lemmatization**
6. **Weighting** (resaltado con borde rojo grueso)

Existe una flecha de bypass desde «Lexical Analysis» directamente hacia «Stemming and Lemmatization».

En el lado derecho, un ejemplo en español:

- **Texto original:** «Mis amigas y amigos peruanos están estudiando.»
- **Tokens (después de parsing/eliminación):** `amigas`, `amigos`, `peruanos`, `estudiando`
- **Resultado de stemming/lemmatization:** `amigo`, `peruano`, `estudiar`
- **Representación vectorial final** (recuadro con borde rojo grueso): `[ (amigo, w1), (peruano, w2), (estudiar, w3) ]`

Pesos: incidencia (1/0), conteo, TF-IDF

- ¿Cómo seleccionar los keywords importantes?
  - Metodo simple: usando las palabras de frecuencia media

**Figura:** Gráfico con eje Y etiquetado «Frequency/Informativity» y eje X etiquetado «Rank». Dos curvas:

- **Frequency:** comienza muy alta para palabras de bajo rango (ranks 1, 2, 3…) y cae abruptamente hacia la derecha (comportamiento tipo ley de Zipf).
- **Informativity:** curva en forma de campana; baja para palabras muy frecuentes (bajo rango) y muy infrecuentes (alto rango), con pico en frecuencia/rango medio. Se indican umbrales «Max.» y «Min.» en el eje Y.

La informatividad de un tipo de palabra es la probabilidad promedio con que ocurrirá dicha palabra, dado cada uno de los contextos en los que puede ocurrir.

$$-\sum_{c} P(C=c \mid W=w) \log P(W=w \mid C=c)$$

Seyfarth, S. (2014). Word informativity influences acoustic duration: Effects of contextual predictability on lexical representation. Cognition, 133(1), 140-155.

Una colección N de documentos

Se extrae todas las palabras que aparecen en los documentos

Se muestra el ranking de las palabras por su frecuencia

(slides 25–26)

### Ejemplo

Tokenización y Eliminación de Stopwords

```python
documentos = [
    "La casa es grande",
    "El gato está en la casa",
    "La casa es bonita y grande",
    "El sol brilla sobre la casa"
]

documentos_procesados = [
    ["casa", "grande"],
    ["gato", "casa"],
    ["casa", "bonita", "grande"],
    ["sol", "brilla", "casa"]
]
```

Matriz de Incidencia

| | casa | grande | gato | bonita | sol | brilla |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Doc 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| Doc 2 | 1 | 0 | 1 | 0 | 0 | 0 |
| Doc 3 | 1 | 1 | 0 | 1 | 0 | 0 |
| Doc 4 | 1 | 0 | 0 | 0 | 1 | 1 |

**Figura:** Flujo de tres etapas de izquierda a derecha y de arriba hacia abajo. Flecha azul etiquetada «Tokenización y Eliminación de Stopwords» conecta la lista `documentos` con `documentos_procesados`. Flecha final apunta hacia la tabla «Matriz de Incidencia».

(slide 27)

### Modelo Booleano

| | Antony and Cleopatra | Julius Caesar | The Tempest | Hamlet | Othello | Macbeth |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Antony | 1 | 1 | 0 | 0 | 0 | 1 |
| Brutus | 1 | 1 | 0 | 1 | 0 | 0 |
| Caesar | 1 | 1 | 0 | 1 | 1 | 1 |
| Calpurnia | 0 | 1 | 0 | 0 | 0 | 0 |
| Cleopatra | 1 | 0 | 0 | 0 | 0 | 0 |
| mercy | 1 | 0 | 1 | 1 | 1 | 1 |
| worser | 1 | 0 | 1 | 1 | 1 | 0 |

Query = Brutus AND Caesar AND NOT Calpurnia

Answer = M(Brutus) $\land$ M(Caesar) $\land$ $\lnot$M(Calpurnia)

$= 110100 \land 110111 \land 101111$

$= 100100$

$\Rightarrow$ Anthony and Cleopatra, Hamlet

**Figura:** Matriz término-documento de incidencia booleana donde filas son términos y columnas son obras de Shakespeare. La fila «Brutus» está resaltada con borde rojo rectangular. En la esquina inferior derecha, un recuadro estilo post-it amarillo muestra la alineación vertical del cálculo bit a bit:

```
110100 ∧
110111 ∧
101111
100100
```

Acento triangular azul en el borde superior izquierdo.

(slide 28)

### Bag of Words en PostgreSQL

Tabla `frases`:

| id | content |
| :--- | :--- |
| 1 | Un buen día para pasear en moto |
| 2 | Todo estaba lindo hasta que tu llegaste |
| 3 | No eres lo que logras, eres lo que superas |
| 4 | Sube a mi moto mas allá te boto |
| 5 | Paseando por las praderas me acorde d... |

```sql
select * from frases
where content like '%pasear%';
```

Resultado: solo **ID 1** (contiene la subcadena exacta «pasear»). No encuentra la fila 5 porque «Paseando» no coincide exactamente.

```sql
select * from frases
where to_tsvector('spanish', content) @@
      to_tsquery('spanish', 'pasear');
```

Resultado: **ID 1** («...pasear...») y **ID 5** («Paseando...»). Con la configuración `'spanish'`, PostgreSQL realiza stemming; «pasear» y «Paseando» se reducen al mismo lexema.

Vectores `tsvector` generados:

| Fila | tsvector |
| :--- | :--- |
| 1 | `'buen':2 'dia':3 'mot':7 'pas':5` |
| 5 | `'acord':6 'pas':1 'prader':4 'ti':8` |

Ambas filas contienen el lexema `'pas'`, por lo que la consulta `tsquery` para 'pasear' coincide con ambas.

**Figura:** Slide con tabla fuente a la izquierda, dos consultas SQL a la derecha (arriba `LIKE`, abajo full-text search) y tabla de vectores `tsvector` resultantes.

(slide 29)

**Figura:** Slide de portada con fotografía de fondo de dos estudiantes (hombre y mujer) con bata de laboratorio trabajando en equipo de laboratorio, cubierta por un filtro azul/cian semitransparente. Texto central grande en blanco: «Laboratorio 8.1». Línea decorativa horizontal tipo diagrama técnico en el borde inferior con segmentos discontinuos y marcadores verticales de colores (azul, amarillo, naranja).

## Modelos de Recuperación de Texto: TF-IDF y Similitud de Coseno

**Figura:** Número «3.» con subrayado azul. Título «Modelos de Recuperación de Texto» en negrita. Subtítulo «TF-IDF & Similitud de Coseno» en cursiva azul claro. Icono de portapapeles con checklist a la izquierda del título. Mano robótica tocando un globo digital brillante en el lado derecho.

### Problemas con la búsqueda booleana

- Consulta booleana es bueno para usuarios expertos con una comprensión precisa de sus necesidades y la colección.
  - También es bueno para las aplicaciones que pueden consumir fácilmente miles de resultados para un refinamiento posterior.

- Pero no es bueno para la mayoría de usuarios.
  - La mayoría de usuarios son incapaces de escribir consultas booleanas (o lo son, pero creen que es demasiado trabajo).
  - La mayoría de los usuarios no quieren pasar a través de miles de resultados.
    - Esto es particularmente cierto en la búsqueda web.

**Figura:** Texto «Ch. 6» tenue en la esquina superior derecha. Frases resaltadas en verde/teal: «bueno para usuarios expertos con una comprensión precisa de sus necesidades y la colección» y «La mayoría de los usuarios no quieren pasar a través de miles de resultados.» Sub-viñeta con marcador cuadrado verde. Acento triangular azul en el borde superior izquierdo.

- Las consultas booleanas a menudo dan como resultados muy pocos (= 0) o demasiados (1000).

- Query 1: "standard AND user AND dlink 650" → 200,000 results

- Query 2: "standard AND user AND dlink 650 AND NOT card": 0 results

- Se requiere mucha habilidad para llegar a una consulta que produzca un número manejable de resultados.
  - AND da muy pocos
  - OR da demasiados

**Figura:** Sub-viñetas «AND da muy pocos» y «OR da demasiados» en color naranja. Acento triangular azul en el borde superior izquierdo.

(slides 34–35)

### Ranked Retrieval

- En lugar de un lenguaje de consulta de operadores y expresiones,
  - En Ranked Retrieval, la consulta es de texto libre, una o más palabras en lenguaje natural.
- En lugar de un conjunto de documentos que satisfacen una expresión de consulta,
  - En Ranked Retrieval, el sistema devuelve un orden de documentos de la colección para una consulta dada.
- En principio, hay dos opciones separadas aquí, pero en la práctica, el ranked retrieval normalmente se ha asociado con consultas de texto libre.

**Figura:** Slide con título en inglés «Ranked Retrieval». Términos clave en negrita: «consulta», «texto libre», «orden», «ranked retrieval», «consultas de texto libre». Acento triangular azul en el borde superior izquierdo.

- Scoring es la base de la recuperación por ranking.

- Se desea devolver los documentos en orden para que sean mas útiles al usuario.

- ¿Cómo podemos ranquear los documentos de la colección con respecto a una consulta?

- Asignando un score, entre [0, 1], a cada documento.

- Este score mide que tan bien "coinciden" el documento y la consulta.

**Figura:** Título «Ranked Retrieval: Scoring». Las viñetas sobre cómo ranquear documentos y sobre qué mide el score aparecen en texto rojo. Texto «Ch. 6» tenue en la esquina superior derecha. Acento triangular azul en el borde superior izquierdo.

- Necesitamos una forma de asignar un score al par

  $\langle$consulta , documento$\rangle$

- Empecemos con un término de la consulta
  - Si el término de la consulta no ocurre en el documento, el score debería ser 0.
  - Cuanto más frecuente sea el término en el documento, mayor será el score (debería serlo).
- Vamos a ver una serie de alternativas para esto.

**Figura:** Título «Ranked Retrieval: Scoring». Segunda viñeta «Empecemos con un término de la consulta» en rojo. Sub-viñeta sobre frecuencia del término también en rojo. Texto «Ch. 6» tenue en la esquina superior derecha. Acento triangular azul en el borde superior izquierdo.

(slides 36–38)

### Term Frequency (TF)

**Figura:** En el centro, texto grande en blanco: «Term Frequency» y debajo «TF». Las letras «UTEC» visibles en la fachada del edificio en el lado derecho.

- Considere la cantidad de ocurrencias de un término en un documento:
  - Cada documento es un vector de conteo $\mathbb{N}^v$:

| | Antony and Cleopatra | Julius Caesar | The Tempest | Hamlet | Othello | Macbeth |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Antony | 157 | 73 | 0 | 0 | 0 | 0 |
| Brutus | 4 | 157 | 0 | 1 | 0 | 0 |
| Caesar | 232 | 227 | 0 | 2 | 1 | 1 |
| Calpurnia | 0 | 10 | 0 | 0 | 0 | 0 |
| Cleopatra | 57 | 0 | 0 | 0 | 0 | 0 |
| mercy | 2 | 0 | 3 | 5 | 5 | 1 |
| worser | 2 | 0 | 1 | 1 | 1 | 0 |

**Figura:** Matriz de conteo término-documento donde filas son términos (en color rojizo-marrón) y columnas son obras de Shakespeare (en azul). La frase «vector de conteo $\mathbb{N}^v$» está resaltada con un recuadro rojo delgado. La columna «Julius Caesar» está encerrada en un recuadro rojo rectangular, enfatizando que esa columna vertical es un vector de conteo para ese documento (por ejemplo, $[73, 157, 227, 10, 0, 0, 0]^T$ respecto a los términos listados). Texto «Sec. 6.2» tenue en la esquina superior derecha. Acento triangular azul en el borde superior izquierdo.

- La frecuencia del término $tf_{t,d}$ es definido como el número de veces que ocurre el término $t$ en el documento $d$.
- → Queremos utilizar tf para calcular el score de coincidencia entre documento y consulta. ¿Pero cómo?
- La frecuencia del término en bruto no es lo que queremos:
  - Un documento con 10 apariciones del término sería más relevante que un documento con una sola ocurrencia del término.
  - Pero no es 10 veces más relevante.
- **La relevancia no aumenta proporcionalmente con la frecuencia del término.**

Tener en cuenta: frecuencia = conteo en IR

**Figura:** En la parte superior izquierda, un triángulo decorativo azul. Título «Ranked Retrieval: Term frequency TF» en texto grande y negrita. Cuatro viñetas principales con el contenido sobre frecuencia de término; la segunda viñeta (objetivo de usar tf) está en texto rojo con flecha «→». La tercera viñeta tiene dos sub-viñetas. La cuarta viñeta está en negrita. En la parte inferior central, un recuadro naranja con el texto «Tener en cuenta: frecuencia = conteo en IR». En la esquina superior derecha, texto tenue «Sec. 6.2».

- El log-frequency weight de un término $t$ en $d$ es:

$$w_{t,d} = \begin{cases} 1 + \log_{10} tf_{t,d}, & \text{if } tf_{t,d} > 0 \\ 0, & \text{otherwise} \end{cases}$$

- $0 \rightarrow 0$, $1 \rightarrow 1$, $2 \rightarrow 1.3$, $10 \rightarrow 2$, $1000 \rightarrow 4$, etc.
- El score para el par documento-consulta: suma de los términos $t$ que coinciden en ambos $q$ y $d$:

$$\text{Score}(q,d) = \sum_{t \in q \cap d} (1 + \log tf_{t,d})$$

- El score es 0 si ninguno de los términos de la consulta está presente en el documento.

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Log-frequency weighting» en texto grande y negrita. Cuatro viñetas: la primera introduce la fórmula de log-frequency weighting centrada en el slide; la segunda lista ejemplos de mapeo de valores; la tercera introduce la fórmula del score como suma; la cuarta indica la condición de score cero. En la esquina superior derecha, texto tenue «Sec. 6.2».

(slides 40–42)

### Document Frequency e IDF

**Figura:** En el centro del slide, texto grande en blanco en dos líneas: «Document Frequency» y «IDF». En el lado derecho del edificio, las letras «UTEC» visibles en la fachada.

- Los **términos raros** tienden a ser más informativos que los términos más frecuentes
  - Recordar los stop words
- Considere un término en la consulta que sea raro en la colección
  - Por ejemplo, *aracnocéntrico*
- Un documento que contiene este término es muy probable que sea relevante para la consulta *aracnocéntrico*.
- → Queremos un peso elevado para términos raros como *aracnocéntrico*.

Los **términos frecuentes** son menos informativos que los términos raros.

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Document frequency» en texto grande y negrita. Cinco viñetas principales; las viñetas sobre término raro en la consulta y el ejemplo *aracnocéntrico* están en texto rojo. La viñeta con flecha «→» sobre peso elevado para términos raros también está en rojo. Frase final en negrita sobre términos frecuentes vs. raros. En la esquina superior derecha, texto tenue «Sec. 6.2.1».

Los **términos frecuentes** son menos informativos que los términos raros.

Ejemplo: en una colección de documentos técnicos tenemos la siguiente frecuencia:

- «para» → 50 veces
- «computación» → 25 veces
- «indexación» → 5 veces
- «hardware» → 1 vez

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Document frequency» en texto grande y negrita. Debajo, frase en negrita sobre términos frecuentes. Luego texto de ejemplo introductorio seguido de cuatro líneas con términos entre comillas y sus frecuencias con flecha «→». En la esquina superior derecha, texto tenue «Sec. 6.2.1».

- Ahora, considere un término de consulta que sea frecuente en la colección (por ejemplo: alto, aumentar, línea).
- Es más probable que un documento que contenga dicho término sea más relevante que un documento que no lo tenga.
  - Pero no es un indicador seguro de relevancia.
- → Para términos frecuentes, queremos pesos altos y positivos, para palabras como: alto, aumentar y línea.
- → Pero a su vez, sus pesos deben ser más bajos que para los términos raros.
- Usaremos la frecuencia de documentos (df).

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Document frequency» en texto grande y negrita. Cinco viñetas: la primera (término frecuente en la colección) está en texto rojo; la segunda en negro con sub-viñeta; las tercera y cuarta con flechas «→»; la quinta sobre frecuencia de documentos (df). En la esquina superior derecha, texto tenue «Sec. 6.2.1».

- $df_t$ es la frecuencia de documento de $t$: número de documentos que contienen a $t$
  - $df_t$ es una medida inversa de la informatividad de $t$
  - $df_t \leq N$
- Definimos idf (frecuencia de documento inverso) de $t$ mediante:
  - Usamos $\log (N / df_t)$ en lugar de $N/df_t$ para "amortiguar" el efecto de idf.

$$idf_t = \log_{10} (N/df_t)$$

La base del log es irrelevante

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: IDF weight» en texto grande y negrita. Dos viñetas principales con sub-viñetas. Fórmula central de $idf_t$ con logaritmo en base 10. Desde la parte «$\log_{10}$» de la fórmula parte una línea roja hacia un recuadro en la parte inferior central con texto azul «La base del log es irrelevante». En la esquina superior derecha, texto tenue «Sec. 6.2.1».

- Ejemplo, suponer $N = 1$ millón

| term | $df_t$ | $idf_t$ |
|------|--------|---------|
| calpurnia | 1 | 6 |
| animal | 100 | 4 |
| sunday | 1,000 | 3 |
| fly | 10,000 | 2 |
| under | 100,000 | 1 |
| the | 1,000,000 | 0 |

$$idf_t = \log_{10} (N/df_t)$$

Hay un solo valor idf para cada término $t$ en una colección.

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: IDF weight» en texto grande y negrita. Viñeta con ejemplo suponiendo $N = 1$ millón. Tabla de tres columnas (term, $df_t$, $idf_t$) con seis filas de datos. Debajo de la tabla, la fórmula $idf_t = \log_{10}(N/df_t)$. Al pie, nota «Hay un solo valor idf para cada término $t$ en una colección.» En la esquina superior derecha, texto tenue «Sec. 6.2.1».

(slides 44–48)

### Ponderación TF-IDF

**Figura:** En el centro del slide, texto grande en blanco «TF-IDF». En el lado derecho del edificio, las letras «UTEC» visibles en la fachada.

- El peso TF-IDF de un término es el producto de sus pesos TF e IDF.
- Es el mejor esquema de ponderación conocido en recuperación de información:

$$w_{t,d} = \log_{10} (1 + tf_{t,d}) \times \log_{10} (N/df_t)$$

$$w_{t,d} = tf_{t,d} \times idf_t$$

- Aumenta con el número de ocurrencias dentro de un documento.
- Aumenta con la rareza del término en la colección.

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: TF-IDF weighting» en texto grande y negrita. Dos viñetas: la segunda («Es el mejor esquema de ponderación conocido en recuperación de información:») está en texto azul. Dos fórmulas centradas de peso TF-IDF. Dos sub-viñetas sobre las propiedades del peso. En la esquina superior derecha, texto tenue «Sec. 6.2.2».

- $w_{t,d} = \log_{10} (1 + tf_{t,d}) \times \log_{10} (N/df_t)$
- $w_{t,d} = tf_{t,d} \times idf_t$

  - $tf_{t,d}$: Es la **frecuencia** del término, es decir es el número de veces que ocurre el término $t$ en el documento $d$.
  - $df_t$: Es la frecuencia de documento del termino $t$, es decir es el número de documentos que contienen a $t$
  - $N/df_t$: Es la inversa de la frecuencia documental, mide la **rareza** de un termino en la colección.
  - Usamos $\log$ para "amortiguar" el efecto de los valores grandes

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: TF-IDF weighting» en texto grande y negrita. Dos fórmulas de peso TF-IDF. Cuatro sub-viñetas con definiciones de $tf_{t,d}$, $df_t$, $N/df_t$ y uso del logaritmo; las palabras «frecuencia» y «rareza» aparecen en negrita y subrayadas.

**Documentos:**

- $D_1$: Cargamento de oro dañado por el fuego
- $D_2$: La entrega de la plata llegó en el camión color plata
- $D_3$: El cargamento de oro llegó en un camión

**Consulta:** oro plata camión

**Vocabulario:** llegó, dañado, entrega, fuego, oro, plata, cargamento, camión, color.

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ejemplo de pesos TF-IDF» en texto grande y negrita. Sección «Documentos:» con tres documentos $D_1$, $D_2$, $D_3$ y su texto en español. Sección «Consulta:» con los términos «oro plata camión». Sección «Vocabulario:» con lista de nueve términos separados por comas.

Las representaciones vectoriales de $D_1$, $D_2$ y $D_3$ son, respectivamente, $\vec{W}_1$, $\vec{W}_2$ y $\vec{W}_3$ (las tres últimas columnas de la tabla)

| Término $t$ | $tf_{t,1}$ | $tf_{t,2}$ | $tf_{t,3}$ | $df_t$ | $N/df_t$ | $idf_t$ | $\vec{W}_1$ | $\vec{W}_2$ | $\vec{W}_3$ |
|-------------|------------|------------|------------|--------|----------|---------|-------------|-------------|-------------|
| llegó | 0 | 1 | 1 | 2 | 1.5 | 0.1761 | 0 | 0.1761 | 0.1761 |
| dañado | 1 | 0 | 0 | 1 | 3 | 0.4771 | 0.4771 | 0 | 0 |
| entrega | 0 | 1 | 0 | 1 | 3 | 0.4771 | 0 | 0.4771 | 0 |
| fuego | 1 | 0 | 0 | 1 | 3 | 0.4771 | 0.4771 | 0 | 0 |
| oro | 1 | 0 | 1 | 2 | 1.5 | 0.1761 | 0.1761 | 0 | 0.1761 |
| plata | 0 | 2 | 0 | 1 | 3 | 0.4771 | 0 | 0.9542 | 0 |
| cargamento | 1 | 0 | 1 | 2 | 1.5 | 0.1761 | 0.1761 | 0 | 0.1761 |
| camión | 0 | 1 | 1 | 2 | 1.5 | 0.1761 | 0 | 0.1761 | 0.1761 |
| color | 0 | 1 | 0 | 1 | 3 | 0.4771 | 0 | 0.4771 | 0 |

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ejemplo de pesos TF-IDF» en texto grande y negrita. Texto explicativo sobre representaciones vectoriales $\vec{W}_1$, $\vec{W}_2$, $\vec{W}_3$ como las tres últimas columnas de la tabla. Tabla grande de 10 columnas y 9 filas de datos con frecuencias de término ($tf$), frecuencia de documento ($df_t$), $N/df_t$, $idf_t$ y pesos vectoriales para cada documento.

- El score para un documento dado una consulta sería:

$$\text{Score}(q,d) = \sum_{t \in q \cap d} tf.idf_{t,d}$$

- Hay muchas variantes:
  - Cómo se calcula "tf" (con / sin log)
  - Si los términos en la consulta también están ponderados…

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: TF-IDF weighting» en texto grande y negrita. Viñeta con fórmula del score como suma de $tf.idf_{t,d}$ para términos en la intersección de consulta y documento. Segunda viñeta «Hay muchas variantes:» con dos sub-viñetas. En la esquina superior derecha, texto tenue «Sec. 6.2.2». Número de slide «54» en la esquina inferior derecha.

(slides 50–54)

### Espacio vectorial y proximidad

**Figura:** En el centro del slide, texto grande en blanco «Similitud de Coseno». En el lado derecho del edificio, las letras «UTEC» visibles en la fachada.

- Vector space = all the terms encountered
  - $[t_1, t_2, t_3, \ldots, t_n]$
- Document
  - $D = [a_1, a_2, a_3, \ldots, a_n]$
  - $a_i = \text{weight of } t_i \text{ in } D$
- Query
  - $Q = [b_1, b_2, b_3, \ldots, b_n]$
  - $b_i = \text{weight of } t_i \text{ in } Q$
- $\text{Score}(D,Q) = \text{Sim}(D,Q)$

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Vector Space» en texto grande y negrita. Cuatro viñetas en inglés definiendo el espacio vectorial, documento, consulta y score como similitud. Cada viñeta incluye notación vectorial con subíndices. Número de slide «56» en la esquina inferior derecha.

- Formalización del espacio vectorial de proximidad.
  - Euclidean distance?
  - Angle distance?
  - *Distancia Euclidiana es una mala idea...*

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Proximidad» en texto grande y negrita. Viñeta sobre formalización del espacio vectorial con tres sub-viñetas: las dos primeras («Euclidean distance?» y «Angle distance?») en rojo; la tercera («Distancia Euclidiana es una mala idea...») en cursiva. A la derecha, diagrama de plano cartesiano con ejes $x$ e $y$ desde el origen $(0,0)$: vector corto terminando en punto **A** y vector más largo terminando en punto **B**, ambos desde el origen. Segmento de línea roja conecta A con B (distancia euclidiana), con flecha azul curva desde el texto «Euclidean distance?». Arco rosa etiquetado con $\theta$ entre los dos vectores (ángulo), con flecha azul curva desde el texto «Angle distance?».

La distancia Euclidiana entre $q$ y $d_2$ es grande aunque la distribución de términos en la consulta $q$ y la distribución de términos en el documento $d_2$ son muy similares.

La distancia Euclidiana es grande para vectores de diferentes longitudes.

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Proximidad» en texto grande y negrita. Texto explicativo a la izquierda. Al pie en rojo: «La distancia Euclidiana es grande para vectores de diferentes longitudes.» A la derecha, gráfico de espacio vectorial 2D: eje horizontal etiquetado «JEALOUS» (de 0 a 1), eje vertical etiquetado «GOSSIP» (de 0 a 1), formando una cuadrícula unitaria. Vectores desde el origen: $d_1$ apuntando hacia arriba (dirección GOSSIP), $q$ apuntando diagonalmente hacia el interior de la cuadrícula terminando en un punto rojo, $d_2$ en la misma dirección que $q$ pero mucho más largo (más allá de la cuadrícula unitaria) terminando en otro punto rojo, $d_3$ apuntando hacia la derecha (dirección JEALOUS). Línea roja delgada conecta las puntas de $q$ y $d_2$ representando la distancia euclidiana. En la esquina superior derecha, texto tenue «Sec. 6.3».

- Usando el ángulo en lugar de la distancia
  - Experimento mental: tome un documento $d$ y adjúntelo a sí mismo. Llama a este documento $d'$.
  - "Semánticamente" $d$ y $d'$ tienen el mismo contenido.
  - La distancia euclidiana entre los dos documentos puede ser bastante grande.
  - El ángulo entre los dos documentos es 0, el cual corresponde a la similitud máxima.
  - Key idea: rankear los documentos según el ángulo que forman con la consulta.

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Proximidad» en texto grande y negrita. Viñeta principal «Usando el ángulo en lugar de la distancia» con cinco sub-viñetas en texto rojo: experimento mental de duplicar documento $d$ en $d'$, equivalencia semántica, gran distancia euclidiana, ángulo cero como similitud máxima, e idea clave de rankear por ángulo con la consulta. En la esquina superior derecha, texto tenue «Sec. 6.3».

- De ángulos a cosenos
  - Las dos nociones siguientes son equivalentes:
    - Ordenar los documentos en orden decreciente del ángulo entre la consulta y el documento.
    - Ordenar los documentos en orden creciente de coseno (consulta y documento)
  - El coseno es una función monótonamente decreciente para el intervalo $[0º, 180º]$

**Figura:** En la parte superior izquierda, triángulo decorativo azul. Título «Ranked Retrieval: Proximidad» en texto grande y negrita. Viñeta «De ángulos a cosenos» con dos sub-viñetas: la primera introduce equivalencia entre dos nociones de ordenamiento (decreciente por ángulo y creciente por coseno; las palabras «decreciente» y «creciente» subrayadas); la segunda sobre el coseno como función monótonamente decreciente en $[0º, 180º]$. En la esquina superior derecha, texto tenue «Sec. 6.3».

Sec. 6.3

- De ángulos a cosenos
- ¿Cómo --y por qué-- debemos calcular los cosenos?

**Figura:** Gráfico de la función coseno $f(x) = \cos(x)$ en color rojo. El eje horizontal (ángulos en grados) va de 0 a 360, con marcas en 50, 100, 150, 200, 250, 300 y 350. El eje vertical (valor del coseno) va de $-1$ a $1$, con marcas en $-1$, $-0.5$, $0$, $0.5$ y $1$. La curva parte de $(0, 1)$, cruza $(90, 0)$, alcanza su mínimo en $(180, -1)$, vuelve a cruzar $(270, 0)$ y termina en $(360, 1)$. Un recuadro azul delgado enmarca la región de $x = 0$ a $x = 180$ y de $y = -1$ a $y = 1$, destacando el rango donde el coseno decrece monótonamente de 1 a $-1$ conforme aumenta el ángulo.

(slides 56–61)

### Similitud de coseno

Sec. 6.3

**Dot product** — **Unit vectors**

$$\cos(\vec{q}, \vec{d}) = \frac{\vec{q} \cdot \vec{d}}{|\vec{q}| |\vec{d}|}$$

$$\cos(\vec{q}, \vec{d}) = \frac{\vec{q}}{|\vec{q}|} \cdot \frac{\vec{d}}{|\vec{d}|}$$

$$\cos(\vec{q}, \vec{d}) = \frac{\sum_{i=1}^{|V|} q_i d_i}{\sqrt{\sum_{i=1}^{|V|} q_i^2} \sqrt{\sum_{i=1}^{|V|} d_i^2}}$$

- $q_i$ is the tf-idf weight of term $i$ in the query
- $d_i$ is the tf-idf weight of term $i$ in the document

$\cos(\vec{q}, \vec{d})$ is the cosine similarity of $\vec{q}$ and $\vec{d}$ … or, equivalently, the cosine of the angle between $\vec{q}$ and $\vec{d}$.

Sec. 6.3

- Normalizar la longitud:
  - Dividir un vector por su norma lo convierte en un vector unidad (longitud) (en la superficie de la unidad hiperesférica)

$$\|\vec{x}\|_2 = \sqrt{\sum_i x_i^2}$$

  - El efecto en los dos documentos $d$ y $d'$ ($d$ anexado a sí mismo) de la diapositiva anterior:
    - Tienen vectores idénticos después de la normalización de la longitud.
    - Los documentos largos y cortos ahora tienen pesos comparables.

- Ilustración de la similitud coseno:

**Figura:** Gráfico 2D en un espacio vectorial con ejes horizontal y vertical escalados de 0 a 1 sobre una cuadrícula. El extremo superior del eje vertical está etiquetado **POOR**; el extremo derecho del eje horizontal está etiquetado **RICH**. Cuatro vectores parten del origen $(0,0)$:
- $\vec{v}(d_1)$: apunta con pendiente pronunciada hacia el eje **POOR** (superior).
- $\vec{v}(q)$: vector de la **consulta**, trazado con línea más gruesa que los demás, apunta hacia la zona superior-central.
- $\vec{v}(d_2)$: apunta hacia la zona central-derecha.
- $\vec{v}(d_3)$: apunta con pendiente suave hacia el eje **RICH** (derecha).

Un ángulo etiquetado con la letra griega $\theta$ se muestra entre $\vec{v}(d_1)$ y $\vec{v}(q)$. Un arco discontinuo conecta los extremos de los vectores, sugiriendo que están normalizados (vectores unidad) para la comparación. Número de slide **64** en la esquina inferior derecha.

Sec. 6.3

Que tan similares son las novelas:

- **SS:** Sentido y Sensibilidad
- **OP:** Orgullo y Prejuicio
- **CB:** Cumbres Borrascosas

| term | SS | OP | CB |
|---|---|---|---|
| afecto | 115 | 58 | 20 |
| celoso | 10 | 7 | 11 |
| chisme | 2 | 0 | 6 |
| borrascoso | 0 | 0 | 38 |

**Frecuencia de Terminos (TF)**

Nota: para simplificar este ejemplo, no hacemos ponderación idf.

Sec. 6.3

- Log frequency weighting

| term | SS | OP | CB |
|---|---|---|---|
| afecto | 3.06 | 2.76 | 2.30 |
| celosa | 2.00 | 1.85 | 2.04 |
| chisme | 1.30 | 0 | 1.78 |
| borrascoso | 0 | 0 | 2.58 |

- After length normalization

| term | SS | OP | CB |
|---|---|---|---|
| afecto | 0.789 | 0.832 | 0.524 |
| celosa | 0.515 | 0.555 | 0.465 |
| chisme | 0.335 | 0 | 0.405 |
| borrascoso | 0 | 0 | 0.588 |

$\cos(SS, OP) \approx$

$0.789 \times 0.832 + 0.515 \times 0.555 + 0.335 \times 0.0 + 0.0 \times 0.0 \approx 0.94$

$\cos(SS, CB) \approx 0.79$

$\cos(OP, CB) \approx 0.69$

¿Por qué tenemos $\cos(SS, OP) > \cos(SS, CB)$?

Efecto de la normalización:

$$\|\vec{x}\|_2 = \sqrt{\sum_{i} x_i^2}$$

**Figura:** Diagrama conceptual que compara una consulta con dos documentos de distinto tamaño. **Doc1** (color morado) es un rectángulo grande. **Doc2** (color naranja) es un rectángulo mucho más pequeño. **Query** (color azul, forma de píldora) se superpone parcialmente a ambos documentos. Aunque la consulta solapa un área absoluta mayor con **Doc1**, el solapamiento representa un porcentaje mucho mayor del área total de **Doc2**.

$\cos(\text{Query}, \text{Doc2}) > \cos(\text{Query}, \text{Doc1})$

Sec. 6.4

Documento: "seguro de carro, seguro de auto"

Query: "el mejor seguro de carro"

| Term | Query tf-raw | Query tf-wt | Query df | Query idf | Query wt | Query n'lize | Document tf-raw | Document tf-wt | Document wt | Document n'lize | Prod |
|---|---|---|---|---|---|---|---|---|---|---|---|
| auto | 0 | 0 | 5000 | 2.3 | 0 | 0 | 1 | 1 | 1 | 0.52 | 0 |
| mejor | 1 | 1 | 50000 | 1.3 | 1.3 | 0.34 | 0 | 0 | 0 | 0 | 0 |
| carro | 1 | 1 | 10000 | 2.0 | 2.0 | 0.52 | 1 | 1 | 1 | 0.52 | 0.27 |
| seguro | 1 | 1 | 1000 | 3.0 | 3.0 | 0.78 | 2 | 1.3 | 1.3 | 0.68 | 0.53 |

¿Que valor tiene $N$ (número de documentos)?

$$\text{Doc length} = \sqrt{1^2 + 0^2 + 1^2 + 1.3^2} \approx 1.92$$

$$\text{Score} = 0 + 0 + 0.27 + 0.53 = 0.8$$

(slides 62–68)

### Ejemplo de consulta TF-IDF

Consulta: oro plata camión

$$\vec{Q} = (0,\ 0,\ 0,\ 0,\ 0.1761,\ 0.4771,\ 0,\ 0.1761,\ 0)$$

$sim(\vec{Q}, \vec{W_1}) = 0.00801$

$sim(\vec{Q}, \vec{W_2}) = 0.7561$

$sim(\vec{Q}, \vec{W_3}) = 0.3272$

$D_2,\ D_3,\ D_1$

(slide 69)

### Resumen de Ranked Retrieval

- Representar la consulta como un vector de pesos tf-idf.
- Representar cada document como un vector de pesos tf-idf.
- Calcular el score de la similitude coseno para la consulta y cada vector de documento.
- Ranquear los documentos a la consulta con su respectivo score.
- Retornar el Top-K al usuario que hizo la consulta.

(slide 70)

## Índice Invertido

**Figura:** Slide de portada de sección con el número **4.** en la esquina superior izquierda subrayado con una barra cian. Título principal: **Modelos de Recuperación de Texto**. Subtítulo en cursiva azul: **Índice Invertido**. Icono de portapapeles con líneas de texto a la izquierda del título. Panel gráfico a la derecha con una mano robótica señalando un globo terráqueo holográfico en tonos azul y teal.

### Desventajas de la matriz vectorial

Formato disperso:

- Asumir:
  - Colección de 1 millón de documentos.
  - Cada documento tiene aproximadamente 1000 palabras.
  - Cada palabra toma 6 bytes, en promedio.
  - De los mil millones de tokens de palabras, 500 000 son únicos (quitando repetidos).
- Entonces:
  - Costo de almacenamiento:
    - $1\text{M} \times 1\,000 \times 6 = 6\text{GB}$ ✓
  - Term-Document incidence matrix tomaría:
    - $500{,}000 \times 1{,}000{,}000 = 0.5 \times 10^{12}$ bits ✗

**Figura:** El cálculo de costo de almacenamiento (6 GB) aparece con marca de verificación verde; el cálculo de la matriz term-document (0.5 × 10¹² bits) aparece resaltado en rojo con marca ✗.

- De las 500 mil millones de entradas, a lo sumo mil millones no son cero.
  - $\Rightarrow$ Al menos el 99.8% de las entradas son cero.
  - $\Rightarrow$ Se puede utilizar una **representación dispersa** para reducir el tamaño de almacenamiento!
- Almacenar solo entradas que no sean cero $\Rightarrow$ **Índice Invertido**.

(slides 74–75)

### Estructura del índice invertido

- Para cada termino $t$, se mapea una lista de todos los documentos que contienen $t$.
  - Identifique cada documento por un ID de documento, un número de serie del documento.
- ¿Arreglos o Listas?

**Figura:** Diagrama que muestra tres términos a la izquierda, cada uno con una flecha hacia una secuencia horizontal de cajas con IDs de documento:
- **Bruto** → 1, 2, 4, 11, 31, 45, 173, 174 (orden ascendente).
- **Cesar** → 1, 2, 4, 5, 6, 16, 57, 132, **14** (el **14** aparece al final, fuera de orden respecto al resto de la lista).
- **Calpurnia** → 2, 31, 54, 101 (orden ascendente).

¿Qué sucede si se agrega la palabra Cesar al documento 14?

- Necesitamos listas de publicaciones de tamaño variable.
  - En el disco, una lectura continua de publicaciones es normal y mejor.
  - En memoria, se pueden usar listas enlazadas o vectores de longitud dinámica.
    - Algún trade-off entre tamaño / facilidad de inserción.

**Figura:** Diagrama dividido en dos componentes etiquetados con recuadros azules:
- **Diccionario** (izquierda): tres términos en cajas verticales — **Bruto**, **Cesar**, **Calpurnia** — cada uno con flecha hacia su lista de publicaciones.
- **Publicaciones** (derecha): filas horizontales de cajas numeradas con docIDs:
  - Bruto: 1, 2, 4, 11, 31, 45, 173, 174
  - Cesar: 1, 2, 4, 5, 6, 16, 57, 132, 14
  - Calpurnia: 2, 31, 54, 101

Ordenado por el docID (más adelante veremos por qué).

(slides 76–77)

### Consultas booleanas sobre el índice

- Considere procesar la siguiente consulta:
  - Bruto AND Cesar
    - Localizar Bruto en el diccionario;
      - Recuperar sus publicaciones.
    - Localizar Cesar en el diccionario;
      - Recuperar sus publicaciones.
    - "Mezclar" las dos publicaciones (intersección de conjunto de documentos):

**Figura:** Dos listas de publicaciones representadas como cadenas de cajas enlazadas con flechas hacia la derecha:
- **Bruto:** 2 → 4 → 8 → 16 → 32 → 64 → 128
- **Cesar:** 1 → 2 → 3 → 5 → 8 → 13 → 21 → 34

Una flecha azul apunta al resultado de la intersección en la parte inferior: **2 → 8** (los docIDs comunes a ambas listas).

Sec. 1.3

- Mezclar:
  - Recorrer las dos publicaciones simultáneamente, en forma lineal sobre el número total de entradas.

**Figura:** Las mismas dos listas de publicaciones con flechas de recorrido hacia la derecha:
- **Bruto:** 2 → 4 → 8 → 16 → 32 → 64 → 128
- **Cesar:** 1 → 2 → 3 → 5 → 8 → 13 → 21 → 34

Si las longitudes de la lista son $n$ y $m$, la combinación toma $O(n + m)$ operaciones.

**Crucial:** las publicaciones deben estar ordenadas por el docID.

Número de slide **79** en la esquina inferior derecha.

```
INTERSECT(p1, p2)
1  answer ← ⟨⟩
2  while p1 ≠ NIL and p2 ≠ NIL
3    do if docID(p1) = docID(p2)
4         then ADD(answer, docID(p1))
5              p1 ← next(p1)
6              p2 ← next(p2)
7         else if docID(p1) < docID(p2)
8              then p1 ← next(p1)
9              else p2 ← next(p2)
10 return answer
```

- $p_1, p_2$ — punteros a listas de publicación correspondientes a $t_1$ y $t_2$.
- $docID$: función que devuelve el Id del documento en la ubicación señalada por $p_i$.

**Union**

$p_1$, $p_2$ – punteros a listas de publicación correspondientes a $t_1$ y $t_2$.

$docID$: función que devuelve el Id del documento en la ubicación señalada por $p_i$.

```
INTERSECT(p1, p2)
1  answer <- < >
2  while p1 != NIL and p2 != NIL
3  do if docID(p1) = docID(p2)
4     then ADD(answer, docID(p1))
5          p1 <- next(p1)
6          p2 <- next(p2)
7     else if docID(p1) < docID(p2)
8          then p1 <- next(p1)
9          else p2 <- next(p2)
10 return answer
```

`ADD(answer, docID(p1))`

`ADD(answer, docID(p2))`

**Figura:** Slide que muestra el pseudocódigo del algoritmo `INTERSECT(p1, p2)` y anotaciones en recuadros amarillos con flechas azules que indican las modificaciones necesarias para adaptarlo a una consulta OR (unión). En la esquina superior derecha aparece el texto explicativo sobre $p_1$, $p_2$ y $docID$. Un recuadro amarillo etiquetado **Union** apunta al nombre de la función `INTERSECT`, indicando que debe renombrarse a `UNION`. Un recuadro amarillo con `ADD(answer, docID(p1))` apunta a la línea 8 (rama `else if docID(p1) < docID(p2)`), indicando que antes de avanzar $p_1$ se debe agregar el documento de $p_1$ al resultado. Un recuadro amarillo con `ADD(answer, docID(p2))` apunta a la línea 9 (rama `else`), indicando que antes de avanzar $p_2$ se debe agregar el documento de $p_2$ al resultado.

- Ejercicio: adaptar el seucodigo para ejecutar la consulta.
  $t_1$ AND NOT $t_2$
  ej., Bruto AND NOT Cesar

- ¿Podemos seguir ejecutando el algoritmo en tiempo $O(n + m)$?

  - Diseñe el algoritmo.

**Figura:** Acento triangular azul en el borde superior izquierdo. El contenido consiste en dos viñetas principales: la primera plantea el ejercicio de adaptar el pseudocódigo para la consulta booleana $t_1$ AND NOT $t_2$ con el ejemplo «Bruto AND NOT Cesar»; la segunda pregunta si el algoritmo puede ejecutarse en tiempo $O(n + m)$ con una sub-viñeta que pide diseñar el algoritmo.

(slides 78–82)

### Ejemplo de construcción y consulta

**Figura:** Diagrama de flujo de izquierda a derecha en tres etapas que ilustra la construcción de un índice invertido a partir de documentos, filtrando stop words.

**Etapa 1 — Documentos de entrada (izquierda):** tres documentos de ejemplo con el siguiente texto:
- **Document 1:** "The bright blue butterfly hangs on the breeze."
- **Document 2:** "It's best to forget the great sky and to retire from every wind."
- **Document 3:** "Under blue sky, in bright sunlight, one need not search around."

**Etapa 2 — Stopword list (centro):** recuadro vertical etiquetado **Stopword list** por el que pasa el texto de los documentos. Contiene las palabras: a, and, around, every, for, from, in, is, it, not, on, one, the, to, under.

**Etapa 3 — Inverted index (derecha):** tabla etiquetada **Inverted index** con tres columnas: ID, Term, Document.

| ID | Term | Document |
| :--- | :--- | :--- |
| 1 | best | 2 |
| 2 | blue | 1, 3 |
| 3 | bright | 1, 3 |
| 4 | butterfly | 1 |
| 5 | breeze | 1 |
| 6 | forget | 2 |
| 7 | great | 2 |
| 8 | hangs | 1 |
| 9 | need | 3 |
| 10 | retire | 2 |
| 11 | search | 3 |
| 12 | sky | 2, 3 |
| 13 | wind | 2 |

Las palabras de la stopword list (the, on, and, to, from, every, under, in, one, not, around, etc.) han sido filtradas y no aparecen en el índice. Los términos se listan en orden alfabético. Algunos términos como blue, bright y sky aparecen en múltiples documentos.

Query = "blue & sky"

Consulta Booleana usando operador AND

Complejidad $O(m)$

$m$ : tamaño de la query

Blue [1,3]

Sky [2,3]

Result : [3]

**Figura:** Slide que ilustra el procesamiento de una consulta booleana AND sobre el índice invertido del ejemplo anterior. A la izquierda se muestra la consulta `Query = "blue & sky"`, la descripción «Consulta Booleana usando operador AND» y la nota de complejidad $O(m)$ donde $m$ es el tamaño de la query. En el centro aparece la tabla **Inverted index** con las columnas ID, Term y Document:

| ID | Term | Document |
| :--- | :--- | :--- |
| 1 | best | 2 |
| 2 | blue | 1, 3 |
| 3 | bright | 1, 3 |
| 4 | butterfly | 1 |
| 5 | breeze | 1 |
| 6 | forget | 2 |
| 7 | great | 2 |
| 8 | hangs | 1 |
| 9 | need | 3 |
| 10 | retire | 2 |
| 11 | search | 3 |
| 12 | sky | 2, 3 |
| 13 | wind | 2 |

A la derecha, una flecha conduce desde la tabla a un recuadro que muestra las listas de documentos recuperadas para los términos de la consulta: `Blue [1,3]` y `Sky [2,3]`. Una flecha descendente conduce al recuadro de resultado final: `Result : [3]`, que representa la intersección (operación AND) de las dos listas, siendo el documento 3 el único presente en ambos conjuntos.

(slides 83–84)

### Índice invertido con similitud de coseno

| Term | Posting List |
| :--- | :--- |
| casa | [1: 1, 2: 1, 3: 2, 4: 1] |
| grande | [1: 1, 3: 2] |
| gato | [2: 1] |
| bonita | [3: 1] |
| sol | [1:2, 4: 2] |
| brilla | [4: 3] |

```
CosineScore(q)
1  float Scores[N] = 0
2  float Length[N]
3  for each query term t
4  do calculate w_{t,q} and fetch postings list for t
5     for each pair(d, tf_{t,d}) in postings list
6     do Scores[d] += w_{t,d} × w_{t,q}
7  Read the array Length
8  for each d
9  do Scores[d] = Scores[d] / Length[d]
10 return Top K components of Scores[]
```

**Figura:** Slide dividida en dos secciones. A la izquierda, tabla bajo el encabezado verde **Index** con dos columnas **Term** y **Posting List**. Las posting lists siguen el formato `[document_id: term_frequency]` con los seis términos y sus listas indicadas arriba. A la derecha, el pseudocódigo del algoritmo `CosineScore(q)` para calcular los puntajes de similitud de coseno entre una consulta $q$ y un conjunto de $N$ documentos. El algoritmo inicializa un arreglo `Scores[N]` en cero y un arreglo `Length[N]`; para cada término $t$ de la consulta calcula $w_{t,q}$ y obtiene la posting list; para cada par $(d, tf_{t,d})$ en la posting list acumula `Scores[d] += w_{t,d} × w_{t,q}`; lee el arreglo `Length`; normaliza dividiendo `Scores[d] / Length[d]` para cada documento $d$; y retorna los Top $K$ componentes de `Scores[]`. Variables clave: $w_{t,q}$ (peso del término $t$ en la consulta $q$), $w_{t,d}$ (peso del término $t$ en el documento $d$), $tf_{t,d}$ (frecuencia del término $t$ en el documento $d$), $Length[d]$ (norma L2 del vector documento para normalización), $N$ (número total de documentos), $K$ (número de resultados top a retornar).

(slide 85)

## Glosario

| Término | Definición |
|---|---|
| Information Retrieval | Es la ciencia de la búsqueda de información en documentos digitales, de naturaleza no estructurada que satisfaga una necesidad de información dentro de grandes colecciones. |
| Búsqueda por atributos internos | IR: búsqueda basado en contenido. |
| Búsqueda por atributos externos | Búsqueda en BD. |
| Corpus | A collection of text documents. |
| Tokenize | Divide the text into smaller units called tokens, usually words or phrases. |
| Tokenización | Cortar la secuencia de caracteres del texto en tokens de palabras. |
| Normalización | Mapear el texto y los términos de consulta a la misma forma. |
| Reducción (stemming) | Podemos hacer coincidir palabras de la misma raíz. |
| Stop words | Podemos omitir palabras muy comunes (o no). |
| $tf_{t,d}$ | La frecuencia del término $t$ en el documento $d$: el número de veces que ocurre el término $t$ en el documento $d$. |
| $df_t$ | La frecuencia de documento del término $t$: el número de documentos que contienen a $t$. |
| $idf_t$ | Frecuencia de documento inverso de $t$; $idf_t = \log_{10}(N/df_t)$. |
| TF-IDF | El peso TF-IDF de un término es el producto de sus pesos TF e IDF. |
| Similitud coseno | $\cos(\vec{q}, \vec{d})$ is the cosine similarity of $\vec{q}$ and $\vec{d}$ … or, equivalently, the cosine of the angle between $\vec{q}$ and $\vec{d}$. |
| Índice Invertido | Para cada término $t$, se mapea una lista de todos los documentos que contienen $t$; almacenar solo entradas que no sean cero. |
| Representación dispersa | Se puede utilizar una representación dispersa para reducir el tamaño de almacenamiento. |
