---
curso: BD2
titulo: 10 BD Vectoriales - Modelos Recuperación Multimedia 1
slides: 65
fuente: 10 BD Vectoriales - Modelos Recuperación Multimedia 1.pdf
---

# 10 BD Vectoriales - Modelos Recuperación Multimedia 1

## Índice

- [Tratamiento de Datos No Estructurados](#tratamiento-de-datos-no-estructurados)
- [Base de Datos Vectoriales: Áreas de Aplicación](#base-de-datos-vectoriales-áreas-de-aplicación)
- [Modelos de Recuperación Multimedia: Introducción](#modelos-de-recuperación-multimedia-introducción)
  - [Base de Datos Multimedia y Sistemas de Gestión](#base-de-datos-multimedia-y-sistemas-de-gestión)
  - [Problemas y Desafíos](#problemas-y-desafíos)
  - [Arquitectura de Base de Datos Multimedia](#arquitectura-de-base-de-datos-multimedia)
- [Recuperación Basada en Contenido](#recuperación-basada-en-contenido)
  - [Imágenes](#imágenes)
  - [Vector de Características](#vector-de-características)
  - [Embedding](#embedding)
- [Búsqueda por Similitud](#búsqueda-por-similitud)
  - [Esquema General](#esquema-general)
  - [Modelo de Búsqueda](#modelo-de-búsqueda)
  - [Medidas de Distancia](#medidas-de-distancia)
  - [Espacios Métricos y Vectoriales](#espacios-métricos-y-vectoriales)
  - [Consultas por Rango y k-NN](#consultas-por-rango-y-k-nn)
  - [Consulta por Ranking Incremental](#consulta-por-ranking-incremental)
  - [Eficiencia y Efectividad](#eficiencia-y-efectividad)
  - [Colecciones de Referencia](#colecciones-de-referencia)
- [Búsqueda de Imágenes](#búsqueda-de-imágenes)
  - [Basado en Color](#basado-en-color)
  - [Basado en Descriptores (SIFT)](#basado-en-descriptores-sift)
  - [Distancia](#distancia)
  - [Reconocimiento de Rostros](#reconocimiento-de-rostros)
- [Segmentación Automática de Videos Grabados](#segmentación-automática-de-videos-grabados)
- [Búsqueda de Audio Musical](#búsqueda-de-audio-musical)
- [Búsqueda Multimedia: Representación Temporal](#búsqueda-multimedia-representación-temporal)
- [Referencias](#referencias)
- [Glosario](#glosario)

## Tratamiento de Datos No Estructurados

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

**Figura:** Diagrama central con un cilindro naranja etiquetado «MULTIMODAL DATABASE» en el centro. Desde él salen flechas hacia cinco tipos de datos periféricos, cada uno con su icono: «TEXT» (documento), «IMAGES» (foto/paisaje), «VIDEO» (película/reproducción), «AUDIO» (altavoz) y «TABULAR DATA» (tabla/cuadrícula). A la derecha, un recuadro azul claro contiene los dos ejemplos SQL transcritos arriba.

(slides 2)

## Base de Datos Vectoriales: Áreas de Aplicación

### Demos de recuperación

Content based Image Retrieval

Music Retrieval Demo

Even if you think Gregorian chant sounds nothing like Nat King Cole, do listen with an open ear: the similarities are often surprising.

Piano music · Grunge rock · Acoustic guitar · Reggae · Jazz · Medieval plainsong

1.000 AmericanMusicClub+IfIHadAHammer
0.785 SoftSounds+BrazillianSuiteNo2
0.714 SoftSounds+BeijaEu
0.711 Guru+Loungin
0.708 LizPhair+XRayMan
0.707 EricClapton+ChangeTheWorld
0.706 JeffersonAirplane+WhiteRabbit
0.705 Coolio+GangstasParadise

https://www.youtube.com/watch?v=M_Gziz-S4A0

http://www.rotorbrain.com/foote/musicr/

**Figura:** La slide se divide en dos columnas. **Columna izquierda — Content based Image Retrieval:** captura de pantalla de la interfaz «iSEARCH». A la izquierda, «Input Query Image» muestra una fotografía de un elefante. Una ventana superpuesta de selección de archivos muestra miniaturas de diversas imágenes (elefantes, dinosaurio, rosa, etc.). Debajo de la imagen de consulta, una fila horizontal muestra resultados de búsqueda, principalmente imágenes de elefantes. Botones visibles: «Search image», «Search without Relevance Feedback» y «Texture based search». URL inferior: `https://www.youtube.com/watch?v=M_Gziz-S4A0`. **Columna derecha — Music Retrieval Demo:** texto introductorio sobre encontrar clips de audio que suenen «similares» a un ejemplo. Enlaces de categorías: «Piano music · Grunge rock · Acoustic guitar · Reggae · Jazz · Medieval plainsong». Recuadro con lista desplazable de puntuaciones de similitud (de 1.000 hacia abajo) seguidas de nombres de pistas (AmericanMusicClub+IfIHadAHammer, SoftSounds+BrazillianSuiteNo2, etc.). Botones: «Search for similar files», «Play selected file», «Reset». URL inferior: `http://www.rotorbrain.com/foote/musicr/`.

### Áreas de aplicación

- Digital Libraries
- News-on-Demand
- Video-on-Demand
- Music database
- Telemedicine
- Biometry
- Manufacturing Industries
- ChatGPT
- Google Búsqueda

**Figura:** A la izquierda, la lista de bullets transcrita arriba. A la derecha, imágenes ilustrativas de las áreas de aplicación: (1) «VOD» formado por mosaicos de miniaturas de video, con una mano sosteniendo un control remoto; (2) estantería curva llena de portadas de medios (libros, películas, álbumes) representando bibliotecas digitales; (3) diagrama técnico que mapea notación musical a un gráfico de tono en el tiempo, con puntos conectados por flechas; (4) fotografía en escala de grises de un rostro masculino con puntos de seguimiento de colores sobre ojos, cejas, nariz y boca (biometría facial); (5) primer plano de un iris humano (escaneo de iris); (6) captura de «3D Warehouse» con una cuadrícula de modelos 3D de muebles (mesas, sillas).

(slides 3–4)

## Modelos de Recuperación Multimedia: Introducción

### Base de Datos Multimedia y Sistemas de Gestión

#### ¿Qué es una Base de Datos Multimedia (MMDB)?

- Es una colección de datos multimedia relacionados.
- Los datos multimedia incluyen uno o más tipos de datos de medios como texto, imágenes, objetos gráficos (incluidos dibujos, bocetos e ilustraciones) secuencia de animación, audio y video.

#### ¿Y un Sistema de Gestión de Base de Datos Multimedia?

- Sería entonces un software que gestione diferentes tipos de datos potencialmente representados en una amplia variedad de formatos y en una amplia gama de fuentes de medios.
- Proporciona soporte para tipos de datos multimedia y facilita la creación, almacenamiento, acceso, consulta y control de una base de datos multimedia.

**Figura:** En la imagen, las palabras «software», «tipos de datos multimedia» y «consulta» aparecen subrayadas.

(slides 6–7)

### Problemas y Desafíos

- Los datos multimedia consisten en una variedad de formatos o representaciones de archivos que incluyen TIFF, BMP, PPT, IVUE, FPX, JPEG, MPEG, AVI, MID, WAV, DOC, GIF, EPS, PNG, etc. Debido a las restricciones en la conversión de un formato a otro, el uso de los datos en un formato específico también ha sido limitado. Por lo general, el tamaño de los datos multimedia es grande (como el video); por lo tanto, los datos multimedia a menudo requieren un gran almacenamiento.

**Figura:** En la imagen, las frases «conversión de un formato a otro» y «gran almacenamiento» aparecen subrayadas.

- La base de datos multimedia consume mucho tiempo de procesamiento, así como ancho de banda.
- Algunos tipos de datos multimedia, como las secuencias de video, audio y animación, tienen requisitos temporales lo cual tienen implicaciones en su almacenamiento, manipulación y presentación.
- Los datos de imágenes, video y gráficos tienen también limitaciones espaciales en términos de su contenido.

**Figura:** En la imagen, los términos «tiempo de procesamiento», «ancho de banda» y «requisitos temporales» aparecen subrayados.

(slides 8–9)

### Arquitectura de Base de Datos Multimedia

#### Basado en el principio de autonomía

- Cada tipo de medio está organizado de una manera específica y adecuada para ese tipo de medio.
- Necesidad de computar uniones a través de diferentes estructuras de datos.
- El procesamiento de consultas es relativamente rápido debido al uso de estructuras especializadas.

**Figura:** Diagrama de flujo de la arquitectura basada en autonomía. En la parte superior: «User». Flecha descendente etiquetada «Query» hacia el bloque central «Multimedia query engine». Desde el motor de consultas, conexiones bidireccionales hacia cuatro módulos de índice especializados en la parte inferior, cada uno conectado a dos iconos de almacenamiento de base de datos (cilindros grises): «Image Index», «Video Index», «Document Index» y «Other data». Desde el «Multimedia query engine», flecha ascendente hacia «Presentation engine», y desde este último flecha etiquetada «Answer» de regreso al «User».

#### Basado en el principio de uniformidad

- Una única estructura abstracta para indexar todos los tipos de medios.
- Resume la parte común de los diferentes tipos de medios (¡difícil!) - metadatos.
- Una estructura - fácil implementación.

Gran desafío

**Figura:** A la izquierda, los bullets y la etiqueta roja con forma de explosión que dice «Gran desafío». A la derecha, diagrama de flujo: «User» en la parte superior envía «Query» al «Multimedia query engine». Desde el motor, flecha bidireccional hacia una barra horizontal larga etiquetada «Unified Index». Líneas verticales conectan la barra «Unified Index» con varios pares de rectángulos grises en la parte inferior que representan fuentes de datos multimedia. Desde el motor de consultas, flecha ascendente al «Presentation engine», y desde este, flecha «Answer» de regreso al «User». Número de slide «11» visible en la esquina inferior derecha.

(slides 10–11)

## Recuperación Basada en Contenido

### Imágenes

- "Basado en el contenido" significa que la búsqueda analiza el contenido de la imagen en lugar de los metadatos, como palabras claves, etiquetas o descripciones asociadas con la imagen.
- El término "contenido" en este contexto puede referirse a colores, formas, texturas o cualquier otra información que se pueda derivar de la propia imagen.

**Figura:** En la imagen, las palabras «colores, formas, texturas» aparecen subrayadas.

(slides 12)

### Vector de Características

- Un sistema de recuperación basado en contenido procesa la información contenida en los datos del objeto y crea una abstracción de su contenido en términos de atributos característicos.
- Cualquier operación de consulta trata únicamente con esta abstracción en lugar de con el objeto en sí.
- Por lo tanto, cada objeto insertado en la base de datos se analiza, y una representación compacta de su contenido se almacena en un vector de características o signature.

**Figura:** Diagrama de flujo en tres columnas. **Columna 1 — Objetos / Entidades:** iconos de Imagen (paisaje), Audio (altavoz), Video (claqueta), Texto (documento), Persona (silueta), Lugar (pin de mapa). **Columna 2 — Extracción de características** (subtítulo: «manual / específica del dominio»): flechas desde cada objeto hacia sus características extraídas — Imagen: color, edges, textures, shapes, histograms, etc.; Audio: MFCC, pitch, energy, rhythm, spectrum, etc.; Video: keyframes, movement, color, histograms, etc.; Texto: word frequency (BoW), TF-IDF, n-grams, etc.; Persona: age, gender, height, hair color, etc.; Lugar: coordinates, climate, population, zone type, etc. **Columna 3 — Vector característico** (subtítulo: «típicamente alta dimensionalidad y disperso»): flechas hacia vectores numéricos de ejemplo — Imagen: `[0, 0, 3, 0, 12, 0, ..., 0]`; Audio: `[0, 1.2, 0, 0, 0, 5.1, ...]`; Video: `[2, 0, 0, 1, 0, 0, ..., 7]`; Texto: `[0, 4, 0, 0, 13, 0, ..., 0]`; Persona: `[0, 0, 5, 0, 0, 0, ..., 1]`; Lugar: `[0, 1, 0, 0, 0, 3, ..., 0]`. Puntos verticales al final indican que el patrón se repite para otros tipos de datos.

(slides 13)

### Embedding

- Representación vectorial denso que captura la semántica de datos (texto, imágenes, audio) en un espacio matemático de alta dimensión donde la similitud geométrica refleja similitud semántica.
- Es una representación aprendida automáticamente por modelos de machine learning o Deep learning
- Captura relaciones semánticas y contextuales

**Figura:** Diagrama de flujo a la derecha. **Entrada (Objetos / Entidades):** iconos de Imagen, Audio, Video, Texto, Persona y Lugar. **Proceso — Modelo de aprendizaje (Autoaprendizaje):** flechas hacia una red neuronal con nodos verdes y capas interconectadas. Texto debajo: «Aprende patrones y relaciones semánticas directamente de los datos». **Salida — Embedding (baja dimensionalidad y denso):** flechas hacia cajas con vectores numéricos, por ejemplo `[0.21, -0.37, 0.82, ..., 0.15]`, `[-0.41, 0.11, -0.26, ..., 0.67]`, `[0.53, -0.22, 0.31, ..., -0.12]`. **Espacio semántico (2D):** gráfico 2D con cuatro clusters de puntos de colores: cluster azul etiquetado «Imágenes de playa», cluster verde «Documentales de naturaleza», cluster morado «Música clásica», cluster rojo «Ciudades europeas».

(slides 14)

## Búsqueda por Similitud

### Esquema General

KNN Search

**Figura:** Diagrama del flujo de un sistema de recuperación multimedia con base de datos vectorial, dividido en dos fases. **Fase de Indexing (arriba-izquierda al centro):** a la izquierda, un conjunto de imágenes diversas (paisajes, calle urbana, perros de distintas razas, gatos, autos antiguos). Flecha etiquetada «Indexing» apunta hacia un icono de base de datos. Debajo de la flecha, tres corchetes verticales con puntos representan «feature vectors». La flecha llega a un cilindro etiquetado «Database». **Fase de Search (abajo-izquierda al centro-inferior):** imagen de consulta de un auto antiguo negro. Flecha etiquetada «Search» con un corchete vertical que representa el feature vector de la consulta. Apunta a un recuadro amarillo con «ANN search» y «KNN Search» (en cursiva debajo). Una flecha descendente desde «Database» también apunta a este bloque de búsqueda. **Resultados (derecha):** flecha curva ascendente hacia una columna etiquetada «Similar results» con tres imágenes de autos antiguos similares al de la consulta.

**Figura:** Dos diagramas lado a lado que ilustran Indexing y Querying. **Indexing (izquierda):** en la parte superior, forma amorfa etiquetada «Data». Flecha sólida descendente hacia un triángulo etiquetado «Index». Desde la base del triángulo, múltiples flechas discontinuas apuntan a una forma amorfa inferior dividida en varias regiones irregulares, etiquetada «Equivalence classes». **Querying (derecha):** en la parte superior, «Query q» con flecha sólida descendente hacia un triángulo que representa el índice. Dentro del triángulo, una línea discontinua muestra un camino de arriba hacia abajo. A la derecha del triángulo: «Traverse index (internal complexity)». Desde la base del triángulo, dos flechas discontinuas apuntan a una forma particionada idéntica a la de Indexing. Una partición contiene un círculo etiquetado «q»; la partición con «q» y algunas adyacentes están sombreadas en gris como «candidate classes». Debajo: «Search in candidate classes (external complexity)».

(slides 16–17)

### Modelo de Búsqueda

Feature Vector

Vector Space

Imágenes similares entre si, deben mapearse a puntos cercanos en el espacio.

**Figura:** A la izquierda, imagen de globos aerostáticos al atardecer. Flecha hacia una caja vertical «Feature Vector» con valores numéricos: 21.9, 3.4, 2.0, ..., 1.3, 9.7, 9.6. Flecha hacia un gráfico 2D titulado «Vector Space» con un punto rojo (consulta) y varios puntos azules (otros objetos). Un círculo verde rodea el punto rojo y tres puntos azules cercanos; flechas desde dos de esos puntos apuntan a imágenes de globos aerostáticos. Fuera del círculo, puntos azules distantes con flechas hacia imágenes de un gato y un perro.

Search

Data collection

P $\cong$ Q

$\delta(P, Q)$

?

**Figura:** En la esquina superior derecha, una forma de onda roja etiquetada con «Q» (consulta). Línea naranja con flecha etiquetada «Search» apunta hacia el centro. Abajo a la izquierda, icono cilíndrico de base de datos etiquetado «Data collection», con cajas internas que contienen distintos patrones de ondas/gráficos en negro. En el centro, recuadro con forma de onda morada «P» comparada con forma de onda roja «Q», con símbolo de similitud $\cong$ entre ellas. Debajo, dentro de una forma de estallido azul con bordes irregulares: $\delta(P, Q)$. A la derecha, un signo de interrogación grande «?».

- Modelo de búsqueda
  - Extracción de características
    - Descriptor (vector)
    - Estructura del descriptor está oculta al usuario
  - Función de similitud
    - Permite comparar descriptores
    - Debe "imitar" la similitud semántica de los objetos
    - Similitud: parte concordante entre objetos

$P_1 = \langle \ldots \ldots \ldots \rangle$    $P_3 = \langle \ldots \ldots \ldots \rangle$    $P_2 = \langle \ldots \ldots \ldots \rangle$

$$f_s(P_1, P_3) > f_s(P_1, P_2)$$

**Figura:** A la derecha, dos diagramas con frutas. **Diagrama superior (comparación de descriptores):** manzana roja y pera amarilla. Encima de la manzana: $d_{apple} = \langle \ldots \rangle$; encima de la pera: $d_{pear} = \langle \ldots \rangle$; entre las etiquetas, símbolo azul de flecha doble horizontal cruzada por barra vertical; entre las frutas, flecha doble horizontal verde. **Diagrama inferior (ranking de similitud):** tres frutas etiquetadas P1 (manzana roja con hoja), P3 (otra manzana roja) y P2 (pera verde con hoja). Encima de cada una: $P_1 = \langle \ldots \ldots \ldots \rangle$, $P_3 = \langle \ldots \ldots \ldots \rangle$, $P_2 = \langle \ldots \ldots \ldots \rangle$. Debajo, la desigualdad $f_s(P_1, P_3) > f_s(P_1, P_2)$, indicando mayor similitud entre las dos manzanas que entre la manzana y la pera.

(slides 18–20)

### Medidas de Distancia

- Modelos para definir objetivamente "similitud"
- Similitud basada en distancias:
  - Una función de distancia mide la disimilitud entre objetos
  - A mayor distancia, más disímiles los objetos
  - Un objeto P tiene (por lo general) distancia 0 a sí mismo
- Se puede formalizar matemáticamente en:
  - Espacios vectoriales
  - Espacios métricos

**Figura:** Plano cartesiano 2D con cuadrícula de 10×10 unidades. Eje horizontal y eje vertical numerados del 1 al 10. Sobre el plano se distribuyen múltiples iconos de peces de distintos colores y formas, representando objetos de datos en un espacio de características bidimensional. Dos puntos rojos están resaltados: uno cerca de un pez oscuro en aproximadamente (7, 8.5) y otro cerca de un pez claro en aproximadamente (8, 4). Entre ambos puntos rojos hay una flecha de doble sentido de color azul claro etiquetada con la palabra **distancia**, ilustrando la separación entre dos objetos en el espacio.

- **Manhattan (p=1):**
  $$d(x, y) = \sum_{i=1}^{D} |x_i - y_i|$$

- **Euclidiana (p=2):**
  $$d(x, y) = \sqrt{\sum_{i=1}^{D} |x_i - y_i|^2}$$

- **Máximo (p=infinito):**
  $$d(x, y) = \max_{1 \le i \le D} |x_i - y_i|$$

- **Similitud Coseno (Angular):**
  $$\cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \times \|\mathbf{b}\|}$$

- **Producto Punto (Dot Product):**
  $$\text{dot}(a, b) = \Sigma(a_i \times b_i)$$

**Figura:** A la derecha de las fórmulas, plano cartesiano 2D con cuadrícula de 10×10 unidades y ejes numerados del 1 al 10. Múltiples iconos de peces dispersos representan puntos de datos. Dos vectores naranjas parten del origen (0,0): uno apunta a un punto rojo en aproximadamente (7, 8.5) y el otro a un punto rojo en aproximadamente (8.2, 4). El ángulo entre ambos vectores en el origen está etiquetado con la letra griega $\theta$, correspondiente a la similitud coseno. Una flecha de doble sentido azul claro conecta las puntas de los dos vectores y está etiquetada **distancia**, representando la distancia euclidiana entre los dos puntos.

**Distancia Euclidiana** (panel izquierdo, resaltado en azul):

- **QUÉ CONSIDERA:** Magnitud, escala y diferencias absolutas
- **USO TÍPICO:**
  - KNN
  - Clustering
  - Coordenadas físicas
  - Datos métricos

**Figura (panel izquierdo):** Gráfico 2D con dos vectores $\mathbf{a}$ y $\mathbf{b}$ que parten del origen. Una línea recta entre las puntas de ambos vectores está etiquetada $d(\mathbf{a}, \mathbf{b})$, representando la distancia euclidiana. Icono de gráfico de barras junto a "QUÉ CONSIDERA".

**Similitud Coseno** (panel derecho, resaltado en verde):

- **QUÉ CONSIDERA:** Dirección o patrón, no la magnitud
- **USO TÍPICO:**
  - Embeddings
  - NLP / Texto
  - Imágenes
  - Audio

**Figura (panel derecho):** Gráfico 2D con dos vectores $\mathbf{a}$ y $\mathbf{b}$ que parten del origen. El foco visual está en el ángulo $\alpha$ formado entre ambos vectores en el origen, en lugar de la distancia entre sus puntas. Icono de dos flechas horizontales en direcciones opuestas junto a "QUÉ CONSIDERA".

- Transformación entre similitud ($s$) - disimilitud ($d$) o viceversa

  i. $d = 1 - s$

  ii. $s = \frac{1}{d + 1}$

      $s = 1 - \frac{d - \text{min\_d}}{\text{max\_d} - \text{min\_d}}$

  iii. $s = e^{-d}$

- En general, cualquier función monótona decreciente sirve

- Propiedades de funciones de disimilitud:

  1. **No-negatividad:** $d(x, y) \geq 0$
  2. **Reflexividad:** $d(x, y) = 0 \iff x = y$
  3. **Simetría:** $d(x, y) = d(y, x)$
  4. **Desigualdad triangular:** $d(x, z) \leq d(x, y) + d(y, z)$

- Una función que cumpla con estas cuatro propiedades se denomina métrica

- Formas cuadráticas

  $$d(x, y) = \sqrt{(x - y)' A (x - y)}$$

  - $A$: matriz de similitud

- Ejemplos
  - Euclidiana ($A$=matriz identidad)
  - Mahalanobis ($A$=inversa de matriz de covarianza)
  - Signature Quadratic Form Distance (SQFD)
    - Permite medir distancia entre vectores de distinta dimensión

**Complejidad de las distancias:**
- Minkowski: $O(D)$
- Forma cuadrática: $O(D^2)$

(slides 21–26)

### Espacios Métricos y Vectoriales

#### Espacios Métricos

- Objetos se pueden representar como:

  - Vectores multidimensionales: $x \in \mathcal{R}^D$
    - $D$: dimensión del espacio

  - Histogramas
    - Normalizados
    - Se manejan igual que los vectores

  - Signatures
    - Conjuntos de vectores con un peso asociado

- Objetos de $X$ son directamente comparados utilizando $\delta$.

- $\delta$ indica el grado de disimilitud entre dos objetos.

- Ejemplo: strings + distancia de edición
  - Distancia de edición: mínimo # de inserciones, borrados o substituciones para transformar un string en otro.

#### Espacios Vectoriales

- Espacio vectorial: caso particular de espacio métrico.

- $\mathbb{R}^d$: d-tuplas de números reales (vectores)

$$x \in \mathbb{R}^d \Rightarrow x = \begin{bmatrix} x_1 \\ x_2 \\ \dots \\ x_d \end{bmatrix}, \quad x_i \in \mathbb{R}$$

(slides 27–29)

### Consultas por Rango y k-NN

Las dos técnicas de búsqueda mas comunes son:

- Búsqueda por rango
- Búsqueda de los K vecinos más cercanos.

- KNN retorna k elementos.
- Búsqueda por rango retorna entre 0 y toda la colección.

**Figura:** Gráfico 2D titulado **Q** (consulta). Eje vertical etiquetado **Width** con escala del 1 al 10. Eje horizontal etiquetado **Length** con escala del 1 al 10. Múltiples iconos de peces dispersos representan puntos de datos en el plano (por ejemplo, en aproximadamente (2, 9), (4, 7), (4, 4), (4, 1.5), (7, 7.5), (9, 0.5)). Dos puntos rojos representan consultas: uno en aproximadamente (7, 4) rodeado por un círculo rojo que indica el radio de búsqueda por rango (un pez dentro del círculo en (6, 4) y otro en o cerca del borde en (8.5, 3.5)); una flecha apunta desde un pez rayado fuera de la cuadrícula hacia este punto rojo. Un segundo punto rojo en aproximadamente (7, 8.5) ilustra KNN, con una flecha desde un pez negro y naranja fuera de la cuadrícula hacia ese punto.

- Sea $\mathbb{U}$ el conjunto de datos multimedia (BD)

- Consulta por rango
  - Objeto de consulta: $q \in \mathbb{X}$
  - Radio de tolerancia: $r \in \mathbb{R}^+$

  $$(q, r) = \{u \in \mathbb{U}, \delta(u, q) \leq r\}$$

- Bola de consulta: subespacio definido por $q$ y $r$

- Ejemplo de consulta por rango en $(\mathbb{R}^2, L_2)$.

**Figura:** Diagrama central con un punto de consulta representado por un cuadrado pequeño etiquetado $q$. Un círculo rodea a $q$; una línea punteada desde el centro $q$ hasta el borde del círculo está etiquetada $r$ (radio de búsqueda). Nueve puntos de datos representados por círculos abiertos etiquetados $u_1$ a $u_9$. Puntos dentro del círculo (en el rango): $u_2$, $u_4$, $u_6$, $u_7$. Puntos fuera del círculo: $u_1$, $u_3$, $u_5$, $u_8$, $u_9$.

Resultado de la consulta a la derecha del diagrama:

$$(q, r) = \{u_2, u_4, u_6, u_7\}$$

- Problema de la consulta por rango: ¿Qué valor debe tener el radio de tolerancia?

**Figura:** Dos diagramas lado a lado mostrando un espacio 2D con puntos negros (datos) y un punto de consulta etiquetado $q$.

- **Diagrama izquierdo:** Círculo gris pequeño centrado en $q$. Ningún punto de datos cae dentro del círculo. Etiqueta debajo: **Muy pequeño: no retorna nada**.
- **Diagrama derecho:** Mismo conjunto de puntos y mismo $q$, pero con un círculo gris significativamente más grande. Un gran número de puntos negros cae dentro del círculo. Etiqueta debajo: **Muy grande: retorna demasiado**.

- Consulta por vecinos más cercanos ($k$-NN)
  - Objeto de consulta: $q \in \mathbb{X}$
  - Número de vecinos: $k \in \mathbb{N}$
  - Retorna conjunto $\mathbb{C}$, $|\mathbb{C}| = k$ tal que

  $$\forall x \in \mathbb{C}, y \in \mathbb{U} - \mathbb{C}, \delta(x, q) \leq \delta(y, q)$$

- Ejemplo de consulta por 3-NN en $(\mathbb{R}^2, L_2)$.

**Figura:** Diagrama con nueve puntos de datos representados por círculos abiertos etiquetados $u_1$ a $u_9$. Un punto de consulta $q$ representado por un cuadrado con un punto interior. Líneas punteadas conectan $q$ con los tres puntos más cercanos: $u_2$ (debajo de $q$), $u_6$ (a la izquierda de $q$) y $u_7$ (arriba de $q$). Los demás puntos ($u_1$, $u_3$, $u_4$, $u_5$, $u_8$, $u_9$) están más alejados y no conectados a $q$. Disposición aproximada: $u_7$ directamente arriba de $q$; $u_6$ a la izquierda; $u_2$ debajo; $u_4$ a la derecha y ligeramente arriba; $u_1$ en la parte superior central; $u_5$ a la derecha de $u_4$; $u_8$ debajo de $u_4$; $u_3$ debajo de $u_5$; $u_9$ en la parte inferior izquierda.

Resultado de la consulta a la derecha del diagrama:

$$3\text{-NN}(q) = \{u_2, u_6, u_7\}$$

(slides 30–35)

### Consulta por Ranking Incremental

- Consulta por ranking incremental:
  - A menudo uno no conoce ni un radio de tolerancia adecuado ni un valor de $k$ razonable
    - Ejemplo: búsqueda en Internet
  - Se desea un resultado ordenado por distancias al objeto de consulta: **ranking**.
  - También conocida como consulta ***give-me-more***

- Consulta por ranking incremental:
  - Dado un objeto de consulta $q$, se repite el llamado de la función **getnext($k_i$)** para retornar los siguientes $k_i$ objetos relevantes, hasta que se alcance la cantidad deseada de objetos.

**Figura:** Dos diagramas de dispersión lado a lado que ilustran la recuperación incremental en un espacio vectorial 2D.

- **Diagrama izquierdo:** Punto de consulta central etiquetado $q'$. Múltiples puntos negros (objetos de datos) dispersos alrededor. Seis puntos específicos conectados a $q'$ mediante líneas grises finas, numerados del 1 al 6 según su ranking de proximidad a $q'$. Etiqueta debajo: **6x getnext(1) para $q'$**.
- **Diagrama derecho:** Punto de consulta diferente etiquetado $q''$ en otra zona del espacio. Seis puntos conectados a $q''$ y numerados del 1 al 6 según su distancia a $q''$. Etiqueta debajo: **6x getnext(1) para $q''$**.

(slides 36–37)

### Eficiencia y Efectividad

#### Eficiencia

- ¿Cómo se mide la eficiencia?
  - Se relaciona con el costo de búsqueda
  - Se mide el tiempo de CPU y tiempo de E/S (acceso a memoria secundaria)
  - Estructuras de datos para agilizar búsquedas.
    - Índices multidimensionales (*spatial access methods*) [BBK01]
    - Índices métricos (*metric access methods*) [CNB01]

(slide 38)

#### Efectividad

- ¿Cómo se mide la efectividad?
  - Efectividad: calidad de la respuesta retornada por el motor de búsqueda.
    - Ejemplo en espacios vectoriales: función de transformación efectiva mapea dos objetos similares en puntos cercanos.
  - Descriptores finos se obtienen con resoluciones altas
    - Pero no necesariamente implican mejor efectividad
  - Evaluación de la efectividad:
    - Medir su habilidad de recuperar objetos relevantes de la BD y de evitar los objetos no relevantes.

¿Qué tan bueno son los objetos recuperados?

- Por lo general, no todo el conjunto de objetos recuperados son relevantes para la consulta.

**Figura:** Rectángulo grande etiquetado **DB** (base de datos) dividido en dos secciones verticales: sección izquierda de color azul claro etiquetada **Relevant Objects** y sección derecha de color rosa claro etiquetada **No-Relevant Objects**. Una elipse naranja en el centro, etiquetada **Ranked Objects**, se superpone a ambas secciones, mostrando que algunos objetos recuperados son relevantes y otros no. Una flecha apunta desde la elipse **Ranked Objects** hacia la fila **Retrieval Objects** de la tabla de la derecha.

| | Relevant Objects | No-Relevant Objects |
| :--- | :--- | :--- |
| **Retrieval Objects** | True Positive (TP) | False Positive (FP) |
| **No-Retrieval Objects** | False Negative (FN) | True Negative (TN) |

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall} = \frac{TP}{TP + FN}$$

Son usados para evaluar el resultado obtenido

- Cuantificación de la similitud entre objetos recuperados y objetos relevantes.

- **Precision:** ¿Cuántos de los objetos recuperados son relevantes?

- **Recall:** ¿Cuántos de los objetos relevantes fueron encontrados?

$$Precision = \frac{TP}{TP + FP}$$

$$Recall = \frac{TP}{TP + FN}$$

**Figura:** Recuadro gris a la derecha del texto que contiene las dos fórmulas de Precision y Recall, cada una con su numerador $TP$ y denominador correspondiente ($TP + FP$ para Precision, $TP + FN$ para Recall). A la izquierda, las definiciones textuales de Precision y Recall aparecen alineadas con sus fórmulas respectivas.

- Relación empírica entre Precision y Recall

**Figura:** Eje vertical (izquierda) etiquetado **Precisión**, escala de 0 a 1. Eje horizontal (abajo) etiquetado **Exhaustividad**, escala de 0 a 1. Una curva azul descendente conecta la zona superior izquierda con la inferior derecha, ilustrando el trade-off entre precisión y exhaustividad.

- **Zona superior izquierda** (círculo naranja): flecha con texto **↑ precisión → ↓ exhaustividad**. Recuadro de texto: **Documentos pertinentes pero, en menor número.**
- **Zona inferior derecha** (círculo naranja): flecha con texto **↓ precisión → ↑ exhaustividad**. Recuadro de texto: **Documentos pertinentes pero, también muchos irrelevantes.**
- **Esquina superior derecha** en el punto (1, 1) (círculo naranja): etiqueta **El ideal**, indicando el objetivo de lograr precisión y exhaustividad perfectas simultáneamente.

(slides 39–42)

### Colecciones de Referencia

- Es una colección de documentos usados para probar modelos de RI y algoritmos [BR99].

- Usualmente incluye:
  - Conjunto de objetos
  - Conjunto de consultas
  - Conjunto de objetos relevantes a cada consulta

- Son difíciles de construir

- **TREC collection**
  - Text REtrieval Conference, empezó en 1992.
  - Colección de documentos de TREC
  - Varios gigabytes de datos
  - Documentos provienen de fuentes diversas

- **URL:** https://trec.nist.gov/

- **MIR Flickr**
  - Se inició con 25.000 imágenes de alta calidad con anotaciones
  - En 2010 fue extendida a 1 millón de imágenes más descriptores para las imágenes (+100 Gb de información)

- **URL:** http://press.liacs.nl/mirflickr/

- **CoPhIR (Content-based Photo Image Retrieval**
  - Una de las mayores colecciones de imágenes disponibles para investigación (106 millones)
  - Se compone de:
    - Imágenes
    - Thumbnails
    - XML con metadatos (uno por imágen)
    - Descriptores para imágenes (MPEG-7)

- **URL:** http://cophir.isti.cnr.it/

(slides 43–46)

## Búsqueda de Imágenes

### Generalidades

- Búsqueda por contenido de la imagen misma
  - Contenido derivado de la representación interna de la imagen (píxeles)
  - Evita los problemas de las anotaciones manuales
  - Características a considerar
    - **Colores**
      - Histogramas de colores
      - Correlograma de colores
    - **Descriptores de imágenes**
      - Gradientes en puntos clave de imagen
      - Cuantización para "palabras visuales"
    - **Texturas:** estructuras de segmentos de imágenes (madera, piedra, etc.)
    - **Formas (contornos):** modelo de similitud morfológico.

(slide 50)

### Basado en Color

- **Histograma de colores**
  - Distribución de colores de píxel en la imagen.
  - No se guarda información espacial
  - Similitud basado en la distancia entre histogramas.

- **Correlograma de colores**
  - Histograma de color en función de la distancia entre píxeles.
  - Distribución del color del píxel más información espacial.
  - Similitud basada en la diferencia de correlogramas.

An Efficient Content Based Image Retrieval System Based on Color Space Approach Using Color Histogram and Color Correlogram | IEEE Conference Publication | IEEE Xplore

**Figura:** Panel derecho con dos elementos visuales apilados verticalmente. Arriba: fotografía de un niño jugando en una piscina de bolas de plástico de colores brillantes (rojo, amarillo, verde y azul). Abajo: gráfico de barras horizontal titulado **Bottom Left**. A la izquierda del gráfico, un espectro de color vertical (arcoíris) que indica los distintos bins de color. El eje horizontal del gráfico está etiquetado **Bin Count** con escala de 0 a 2000. Barras horizontales negras representan la frecuencia o conteo de píxeles en cada bin de color, ilustrando cómo se vería un vector de características basado en color para una imagen.

- **Comparación de métodos**
  - Histograma de colores
  - Correlograma de colores

- Los correlogramas son mejores para la recuperación de imágenes.

**Figura (arriba derecha):** Dos rectángulos azules que ilustran imágenes con histogramas idénticos pero correlogramas diferentes. El primero contiene un único rectángulo rojo grande en el centro. El segundo contiene dos cuadrados rojos más pequeños separados por un espacio azul. Etiqueta: **Imágenes con histogramas de color idénticos pero con diferentes correlogramas.**

**Figura (abajo izquierda):** Dos fotografías similares de un sitio de construcción industrial (estructura metálica sobre construcciones de concreto), tomadas desde ángulos o distancias ligeramente diferentes. Etiqueta: **Imágenes con diferentes histogramas de color pero de correlogramas similares.**

Número de slide **52** visible en la esquina inferior derecha.

- De todas formas es un problema difícil…

**Figura:** Dos fotografías en retrato colocadas lado a lado sobre un fondo amarillo-anaranjado cálido. **Imagen izquierda:** retrato de una mujer joven con cabello largo, voluminoso y rizado de color castaño rojizo, mirando directamente a la cámara. **Imagen derecha:** retrato de un perro Cocker Spaniel dorado-marrón cuyas orejas largas y onduladas cuelgan a ambos lados, imitando en color, textura y forma el cabello de la mujer en la foto adyacente.

(slides 51–53)

### Basado en Descriptores (SIFT)

- **SIFT Features**
  - Scale Invariant Feature Transform (2004: David Lowe, UBC)

- Seleccionar regiones keypoint en la imagen desde los extremos en el espacio escalado
  - Diferentes imágenes tienen diferentes números de keypoint.

- Calcular los vectores característicos X para cada región keypoint
  - Ejemplo: basado en Edge Histogram genera vectores de tamaño 128.

- La imágen es representada por N SIFT features
  - Features son los vectores $X_1, \dots, X_N$
  - N varía según la imágen.

SIFT Interest Point Detector Using Python – OpenCV | GeeksforGeeks

**Figura:** Panel derecho con fotografía en escala de grises de varios objetos (cajas o empaques) dentro de una bolsa o contenedor. Sobre la imagen se superponen numerosos cuadrados blancos pequeños con líneas radiantes que representan los keypoints detectados y sus orientaciones por el algoritmo SIFT. Rectángulos blancos más grandes delimitan regiones de interés específicas sobre los objetos.

(slide 54)

### Distancia

- **Distancia Euclidiana:**
  - Sean $H^P$ y $H^Q$ los histogramas de colores de las imágenes $P$ y $Q$.

$$\delta(P, Q) = \sqrt{(H^P - H^Q) \cdot (H^P - H^Q)^T}$$

$$\delta(RED, PINK) = \sqrt{2}$$

$$\delta(RED, BLUE) = \sqrt{2}$$

$$\delta(PINK, BLUE) = \sqrt{2}$$

**Figura:** Tres cuadrados de color — **RED**, **PINK** y **BLUE** — cada uno acompañado de un histograma de barras 3D simplificado y su representación vectorial correspondiente:
- **RED:** histograma con una barra completa en el bin rojo. Vector: $(1, 0, 0, \dots)$
- **PINK:** histograma con una barra completa en el bin rosado. Vector: $(0, 1, 0, \dots)$
- **BLUE:** histograma con una barra completa en el bin azul. Vector: $(0, 0, 1, \dots)$

Debajo se muestran los tres resultados de distancia euclidiana entre pares, todos iguales a $\sqrt{2}$.

- **Problemas de la distancia euclidiana:**

  - En el ejemplo anterior, todos los pares de imágenes tienen distancia 2.

  - No se tiene en cuenta el hecho que el rojo se parece más al rosado que al azul.

  - **No se consideran las interrelaciones entre dimensiones (semántica del contexto).**

- **Forma Cuadrática:**
  - Definición: sea $A$ una matriz de similitud. Se cumple que:

$$\delta(P, Q) = \sqrt{(H^P - H^Q) \cdot A \cdot (H^P - H^Q)^T} = \sqrt{\sum_i \sum_j a_{ij} (H_i^P - H_i^Q) \cdot (H_j^P - H_j^Q)}$$

  - Los valor $a_{i,j}$ de la matriz $A$ describen la similitud entre las dimensiones $i$ y $j$ de los vectores (bins $i$ y $j$ del histograma).

  - Para el ejemplo, dada la matriz se obtienen las distancias:

$$A = \begin{bmatrix} 1 & 0.9 & 0 \\ 0.9 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

$$\delta_A(RED, PINK) = \sqrt{0.2}$$

$$\delta_A(RED, BLUE) = \sqrt{2}$$

$$\delta_A(PINK, BLUE) = \sqrt{2}$$

- **Forma Cuadrática:**
  - Ejemplos de matrices de similitud:

$$a_{ij} = \left( 1 - \frac{d_{ij}}{d_{máx}} \right)$$

$$a_{ij} = e^{-\sigma \cdot \left( \frac{d_{ij}}{d_{máx}} \right)^2}, \quad \sigma \text{ constante}$$

  - $d_{i,j}$ es la distancia entre colores $i$ y $j$.

- **Forma Cuadrática:**
  - **Adaptabilidad para el Usuario**
    - Similitud es inherentemente subjetiva
    - Es posible que un usuario no esté satisfecho con la matriz de similitud $A$ utilizada
    - Construir de nuevo un índice al cambiar $A$ puede ser muy costoso
    - Se desearía tener una técnica más flexible, que permitiera modificar $A$ al momento de realizar una consulta

(slides 55–59)

### Reconocimiento de Rostros

- **Reconocimiento de rostros**
  - Detectar rostros en imágenes.
  - Búsqueda por similitud de rostros para reconocer los rostros detectados.
  - Ej: Búsqueda avanzada de Google para imágenes con rostros.

- **Librerías:**
  - Javascript: face-api.js
  - Python: face-recognition

**Figura:** Diagrama de flujo de reconocimiento facial con tres etapas conectadas por flechas, con etiquetas en texto rojo:

1. **Photo Collection** (arriba derecha): cuadrícula de fotografías grupales, principalmente de estudiantes con togas de graduación o vestimenta formal.
2. **Detect Faces in Photo Collection** (abajo derecha): flecha descendente desde la colección de fotos hacia una nueva cuadrícula compuesta por rostros individuales recortados extraídos de las fotografías anteriores.
3. **Face Recognition** (abajo izquierda): flecha desde la cuadrícula de rostros detectados hacia una imagen final que muestra un grupo de cinco mujeres jóvenes de pie juntas. El rostro de una mujer está rodeado por un círculo rojo y un recuadro de texto azul junto al círculo la identifica como **Ann Smith**, demostrando la identificación exitosa de un individuo específico en la colección.

**Figura:** Diagrama titulado **FACE RECOGNITION PIPELINE** que describe cuatro etapas del proceso de reconocimiento facial, dispuestas de izquierda a derecha con flechas que conectan cada etapa.

**Etapa 1 — Input & Landmark Detection:**
- Entrada: imagen de una mujer con rostro visible.
- Sobre el rostro se superponen puntos rojos (landmarks) sobre rasgos faciales clave: ojos, nariz, boca y mandíbula.
- Los puntos están conectados por líneas rojas que forman una malla o rejilla facial sobre el rostro.

**Etapa 2 — Geometric Alignment:**
- El rostro con sus landmarks se procesa para producir una **Normalized, Frontal Face** (cara normalizada y frontal).
- El proceso implica rotar y escalar la imagen de modo que el rostro quede centrado y orientado directamente hacia el frente dentro de un recuadro cuadrado (bounding box).
- Salida: retrato limpio y alineado.

**Etapa 3 — Global Descriptor Extraction (Face Embedding):**
- Una flecha azul grande etiquetada **CNN (Deep Neural Network) Feature Extractor** conduce desde la imagen alineada hacia una representación de la arquitectura de red neuronal.
- **Arquitectura:** el diagrama muestra iconos para capas **Conv** (convolucionales), capas **Pool** (pooling) y pilas de mapas de características (feature maps).
- **Entrenamiento:** nota que indica que la red está **Trained with Triplet Loss**.
- **Salida:** **FACE EMBEDDING (GLOBAL DESCRIPTOR - 128D Vector)**, descrito como un **Unique 'Digital Fingerprint'** (huella digital única).
- Debajo se muestra una tabla horizontal con los valores numéricos del vector 128D (por ejemplo: 0.13, 0.27, 0.23, ...).

**Etapa 4 — Comparison & Recognition:**
- Una flecha verde grande apunta a la etapa final donde el embedding generado se compara contra datos almacenados.
- **Proceso:** el vector embedding de entrada se compara con un vector de **Database Face B**.
- **Lógica de decisión:** la comparación usa una **Distance Metric (e.g. Euclidean)** y el resultado se contrasta contra un **> Threshold**.
- **Resultado:** **MATCH / NO-MATCH**. Un checkmark verde aparece junto al texto, indicando un match exitoso en el ejemplo mostrado.

(slides 60–61)

## Segmentación Automática de Videos Grabados

- Play video and view slides
- Skip to next slide
- **Skip to next relevant slide**

**Figura:** Captura de pantalla de una aplicación reproductora multimedia titulada **StainedGlass Photo Collages 02-22-06 4:11 PM** en una barra de encabezado azul. La interfaz se divide en varias secciones:

- **Video Feed (izquierda):** ventana de video pequeña que muestra a un hombre presentando ante un grupo reducido de personas en una sala con pantalla grande y mesa de conferencia. Debajo del video aparece la marca de tiempo: **Wed, 22 Feb 2006 16:12:07**.
- **Slide Display (derecha):** ventana más grande que muestra la diapositiva de presentación específica que se discute en el video. La diapositiva se titula **StainedGlass Photo Collage Web Application** por FXPAL. Enumera características como: creación automática de collages, resumen de eventos, ajustes del usuario, compartir por email/web, mejora del intercambio de fotos en línea, integración con servicios de impresión e interfaz con Flickr.
- **Controles de reproducción:** iconos estándar de pausa, avance rápido, retroceso y volumen ubicados debajo de la ventana de video.
- **Timeline y segmentación (parte inferior):** barra de timeline horizontal amarilla que abarca el ancho de la interfaz. Contiene dos tipos de marcadores:
  - **Líneas verticales negras:** una flecha apunta a estas líneas con la etiqueta **Slides marked by black lines**. Indican dónde ocurren los cambios de diapositiva en el video.
  - **Cuadrados rojos pequeños:** una flecha apunta a estos cuadrados, ubicados sobre el timeline, con la etiqueta **Relevant Slides marked by red squares**. Indican segmentos «clave» o «relevantes» de la presentación.

Source: Lynn Wilcox

**Contexto:**
- Colección de videos de conferencias (por ejemplo, material para una clase). El objetivo es encontrar únicamente la parte específica de una conferencia que se desea visualizar.

**Método de indexación:**
- Captura del audio y video de la conferencia.
- Captura del material de presentación (diapositivas).
- Extracción del texto contenido en las diapositivas.
- Segmentación del video basada en los cambios de diapositiva.
- Creación de un índice textual con palabras clave asociadas a cada segmento del video según la diapositiva correspondiente.
- Construcción de un índice espacio-temporal que relacione los segmentos de video y audio con su posición en el tiempo.

**Método de búsqueda:**
- Búsqueda por palabras claves.
- Reproducción del video a partir del segmento relevante identificado.
- Búsqueda mediante otro segmento de video (por similitud de contenido o contexto).

**Figura:** Captura de pantalla de una aplicación web ejecutándose en una ventana del navegador Mozilla Firefox titulada **StainedGlass Photo Collages 02-22-06 4:11 PM**, que sirve como ejemplo del sistema de segmentación de video.

- **Panel de video (arriba izquierda):** muestra un video pequeño de un presentador de pie en una sala con pantalla de proyector.
- **Panel de diapositiva (derecha):** muestra una vista clara y de alta resolución de la diapositiva actual que se discute en el video. Enumera viñetas sobre las características de la aplicación (por ejemplo: collages de fotos automáticos, resumen de eventos, integración con Flickr).
- **Controles de reproducción y timeline (parte inferior):** incluye controles estándar de video (play, pausa, saltar). Debajo de los controles hay un timeline horizontal con marcadores amarillos y rojos, que representan los segmentos o cambios de diapositiva mencionados en el método de indexación. Marcas de tiempo como **16:15** y **16:20** son visibles en el timeline. Una barra de estado en la parte inferior dice **Applet Player started**.

(slides 62–63)

## Búsqueda de Audio Musical

**Proceso:**
- Calcular vectores de características espectrales, como los coeficientes cepstrales en las frecuencias de Mel (MFCC).
- Cuantizar estas características para construir un histograma de audio.
- El histograma resultante representa la distribución general de los sonidos en una pista.
- Nota: Este enfoque no conserva el orden temporal de los sonidos, lo que puede limitar la precisión en ciertas aplicaciones.

**Ejemplo**
- http://www.rotorbrain.com/foote/musicr/
- Music Retrieval Demo

**Figura (interfaz de demo):** Captura de pantalla de la interfaz **Music Retrieval Demo**. Muestra una lista de canciones con puntuaciones de similitud decimales. La entrada superior está resaltada en rojo: **1.000 NatKingCole+AintMisbehavin**. Otras entradas incluyen puntuaciones como **0.772**, **0.712**, etc. En la parte inferior hay tres botones: **Search for similar files**, **Play selected file** y **Reset**.

**Figura (diagrama de flujo):** Diagrama de flujo vertical en el lado derecho de la slide que ilustra el proceso técnico:

1. **Waveform:** muestra una onda de audio oscilante estándar.
2. **Window:** ilustra cómo la forma de onda continua se divide en segmentos horizontales superpuestos (ventanas) para el análisis.
3. **Compute MFCCs:** caja de procesamiento donde los datos ventaneados se transforman en coeficientes cepstrales en frecuencias de Mel.
4. **MFCCs:** visualización tipo rejilla que representa los vectores de características calculados a lo largo del tiempo.
5. **Quantize via Tree:** caja de procesamiento que contiene un diagrama de árbol de decisión, mostrando cómo los datos MFCC de alta dimensión se categorizan en bins discretos.
6. **Accumulate Histogram Counts:** salida final es un gráfico de barras (histograma) donde cada barra representa la frecuencia de ocurrencia de características sonoras cuantizadas específicas dentro del archivo de audio.

Evaluation of MFCC estimation techniques for music similarity | IEEE Conference Publication | IEEE Xplore

(slide 64)

## Búsqueda Multimedia: Representación Temporal

- Los datos de video, pueden pensarse mejor como series de tiempo ...

**Figura (sección superior — acción «Point»):** Cuatro fotogramas secuenciales de una persona de pie de perfil. Comienza con la mano a su lado, luego levanta el brazo hasta apuntar directamente hacia adelante.

**Gráfico (sección superior):** A la derecha de las imágenes hay un gráfico de líneas con tres curvas de colores (verde, azul y magenta) que representan el movimiento a lo largo del tiempo. Las curvas muestran una tendencia ascendente pronunciada que se estabiliza en una meseta superior. Eje horizontal con valores: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90.

**Anotaciones del gráfico (sección superior):**
- **Hand at rest:** apunta al inicio de las curvas (valores bajos).
- **Hand moving to shoulder level:** apunta a la parte ascendente pronunciada de las curvas.
- **Steady pointing:** apunta a la meseta plana al final de las curvas.

**Figura (sección inferior — acción «Gun-Draw»):** Cuatro fotogramas secuenciales de una persona de perfil. Comienza con la mano a su lado, baja la mano hacia una funda en la cadera, agarra un arma y luego la levanta para apuntar directamente hacia adelante.

**Gráfico (sección inferior):** A la derecha hay un gráfico de líneas con tres curvas (roja, verde y magenta). Estas curvas son más complejas que las anteriores: muestran un ascenso inicial pequeño, una caída (correspondiente a bajar la mano hacia el arma), seguida de un ascenso pronunciado y una meseta. Eje horizontal con valores: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90.

**Anotaciones del gráfico (sección inferior):**
- **Hand at rest:** apunta al inicio.
- **Hand moving above holster:** apunta al primer ascenso pequeño.
- **Hand moving down to grasp gun:** apunta a la caída subsiguiente en las curvas.
- **Hand moving to shoulder level:** apunta a la parte ascendente final pronunciada.
- **Steady pointing:** apunta a la meseta final.

Towards Parameter-Free Data Mining

(slide 65)

## Referencias

- [BBK01] C. Böhm, S. Berchtold, and D. Keim. Searching in high-dimensional spaces: Index structures for improving the performance of multimedia databases. ACM Computing Surveys, 33(3):322—373, 2001.
- [BR99] R. Baeza-Yates, B. Ribeiro-Neto. Modern Information Retrieval. Addison-Wesley, 1999.
- [CNB01] E. Chávez, G. Navarro, J. Marroquín, and R. Baeza-Yates. Searching in metric spaces. ACM Computing Surveys, 33(3):273—321, 2001

(slide 47)

## Glosario

- **Base de Datos Multimedia (MMDB):** Colección de datos multimedia relacionados. Los datos multimedia incluyen uno o más tipos de datos de medios como texto, imágenes, objetos gráficos (incluidos dibujos, bocetos e ilustraciones) secuencia de animación, audio y video.

- **Sistema de Gestión de Base de Datos Multimedia:** Software que gestiona diferentes tipos de datos potencialmente representados en una amplia variedad de formatos y en una amplia gama de fuentes de medios. Proporciona soporte para tipos de datos multimedia y facilita la creación, almacenamiento, acceso, consulta y control de una base de datos multimedia.

- **Recuperación basada en contenido:** La búsqueda analiza el contenido de la imagen en lugar de los metadatos, como palabras claves, etiquetas o descripciones asociadas con la imagen. El término "contenido" puede referirse a colores, formas, texturas o cualquier otra información que se pueda derivar de la propia imagen.

- **Vector de características (signature):** Representación compacta del contenido de un objeto, creada a partir de una abstracción de su contenido en términos de atributos característicos. Cualquier operación de consulta trata únicamente con esta abstracción en lugar de con el objeto en sí.

- **Embedding:** Representación vectorial denso que captura la semántica de datos (texto, imágenes, audio) en un espacio matemático de alta dimensión donde la similitud geométrica refleja similitud semántica. Es una representación aprendida automáticamente por modelos de machine learning o Deep learning. Captura relaciones semánticas y contextuales.

- **Feature Vector:** Abstracción numérica del contenido de un objeto multimedia, utilizada para mapear objetos similares a puntos cercanos en un espacio vectorial.

- **Vector Space:** Espacio matemático en el que los objetos multimedia se representan como puntos; imágenes similares entre sí deben mapearse a puntos cercanos en el espacio.

- **Función de similitud ($f_s$):** Permite comparar descriptores. Debe "imitar" la similitud semántica de los objetos. Similitud: parte concordante entre objetos.

- **Métrica:** Función de disimilitud que cumple con las cuatro propiedades de no-negatividad, reflexividad, simetría y desigualdad triangular.

- **Bola de consulta:** Subespacio definido por el objeto de consulta $q$ y el radio de tolerancia $r$.

- **Precision:** ¿Cuántos de los objetos recuperados son relevantes? $Precision = \frac{TP}{TP + FP}$

- **Recall:** ¿Cuántos de los objetos relevantes fueron encontrados? $Recall = \frac{TP}{TP + FN}$

- **Colección de referencia:** Colección de documentos usados para probar modelos de RI y algoritmos. Usualmente incluye conjunto de objetos, conjunto de consultas y conjunto de objetos relevantes a cada consulta.

- **Histograma de colores:** Distribución de colores de píxel en la imagen. No se guarda información espacial. Similitud basada en la distancia entre histogramas.

- **Correlograma de colores:** Histograma de color en función de la distancia entre píxeles. Distribución del color del píxel más información espacial. Similitud basada en la diferencia de correlogramas.

- **SIFT (Scale Invariant Feature Transform):** Método de selección de regiones keypoint en la imagen desde los extremos en el espacio escalado, con cálculo de vectores característicos para cada región keypoint.

- **Forma Cuadrática:** Distancia definida como $\delta(P, Q) = \sqrt{(H^P - H^Q) \cdot A \cdot (H^P - H^Q)^T}$, donde $A$ es una matriz de similitud cuyos valores $a_{i,j}$ describen la similitud entre las dimensiones $i$ y $j$ de los vectores.

- **Face Embedding:** Descriptor global de 128 dimensiones generado por una red neuronal convolucional entrenada con Triplet Loss, que actúa como huella digital única de un rostro para comparación y reconocimiento.
