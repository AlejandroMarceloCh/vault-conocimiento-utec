---
curso: BD1
titulo: Clase 15 Otros modelos de datos y base de datos
slides: 36
fuente: Clase 15 Otros modelos de datos y base de datos.pdf
---

## Slide 1

Portada (decorativa: fondo túnel azul con figura de persona caminando, logo UTEC, banner "Reinventa el mundo", logo "TRANSFORMATEC").

**OTROS MODELOS DE DATOS Y BASE DE DATOS**
CS2041 - Base de Datos I, Ciclo 2024-1
Profesores: Teófilo Chambilla (tchambilla@utec.edu.pe), Brenner Ojeda (bojeda@utec.edu.pe)

## Slide 2

**Agenda** (icono decorativo de documento a la derecha)
- Bases de datos, recuperación de la información y bases de conocimiento
- Volúmenes de Datos (datos grandes)
- Modelos y formatos de datos (texto, imágenes, video)
- Ciclo de los datos
- Bases de datos No SQL
- Introducción a MongoDB

## Slide 3

**Nuestro mundo de los datos**

Slide con tres elementos visuales:
- Izquierda: infografía tipo "nube de iconos" (dinero, reloj, email, gráficos, calculadora, engranajes, chat, etc.) que fluye hacia abajo en flechas de colores (naranja, celeste, azul oscuro) hacia dispositivos: torre de servidores, laptop con gráfico de barras, carrito de compras/móvil, y más servidores. Representa la generación de datos desde múltiples fuentes hacia infraestructura de almacenamiento.
- Centro superior: captura de pantalla de un conversor XML→JSON: panel izquierdo "XML" con código `<?xml version="1.0" encoding="UTF-8"?>`, `<article xmlns=...>`, `<info><title>Welcome to DocBook Support</title></info>`, `<sect1>`, etc.; flecha bidireccional (→ ←) hacia panel derecho "JSON" con el mismo contenido en formato `{ "article": { "xmlns": ..., "info": {"title": "Welcome to DocBoo...", "sect1": [ {"title": "Inline Markup and Imag...", "para": [...] } ] } } }`. Botones "Choose File", "Download", "Copy", "Clear" en ambos paneles.
- Debajo del conversor: icono de tabla/planilla.
- Abajo izquierda: icono de "SENSOR" (ondas emitidas por un dispositivo).
- Abajo derecha: collage "MultiMedia" con cámara, TV, control remoto, tijeras, fotos, texto multicolor "Multi Media".

## Slide 4

**Proceso de base de datos relacional**

Diagrama de flujo horizontal con 4 etapas conectadas por flechas azules:
1. **Mundo Real** (icono de globo con cadena)
2. **Modelo Conceptual / Lógico** — diagrama entidad-relación con entidades "Cliente" (1) → relación "Realiza" (N) → "Pedido" (N) — relación "Se compone" (N:M) → "Artículo"; atributos: Dni, Fecha, Núm Serie, Cantidad
3. **Modelo Físico / BD** — cilindro de base de datos con tres tablas: "Artiste" (ArtistId, ArtistName), "Albums" (AlbumId, AlbumName, Artist), "Ratings" (RatingId, AlbumId, Rating)
4. **Consultas SQL** — bloque de código:
```sql
UPDATE CURSOS
SET CICLO = '2020-1'
WHERE ACTIVE = 1
```

Debajo, en texto rojo grande:
"¿Datos multimedia?"
"¿Datos con estructura primitiva?"

## Slide 5

Slide separador (banda azul centrada, resto en blanco). Texto:
"Bases de datos
Recuperación de información
Bases de conocimiento"

## Slide 6

**Capas de procesamiento de datos**

Diagrama de "prisma" en 3 capas apiladas (vista isométrica, color lila arriba, naranja en medio, lila abajo):
- Capa superior: **APIs** (icono herramientas+lupa), **Aplicaciones** (icono ventana + icono HTML), **Servicios** (icono globo con tabla)
- Capa media (naranja): **Estructura de datos: Tablas, Grafos** (con dos mini-diagramas de grafos), **Lenguaje de consultas** (iconos X1, X2, ..., Xn con flechas)
- Capa inferior: **Almacenamiento nativo** (icono cubos azules apilados), **Archivos** (icono hojas), **RDBMS** (iconos cilindros: Oracle, DB2, MySQL, MSQL, Postgres)

## Slide 7

Misma imagen que slide 6 (Capas de procesamiento de datos) pero con un recuadro azul que resalta la columna derecha (Lenguaje de consultas + RDBMS) y una flecha azul apuntando a la derecha con la etiqueta "Base de datos relacionales" — indica que esa combinación específica constituye las bases de datos relacionales.

## Slide 8

**Tres niveles de abstracción de datos**

Diagrama de bloques 3D apilados en forma de escalera ascendente, con tres franjas de colores (de abajo hacia arriba: rojo/salmón, naranja, verde lima) más dos bloques blancos arriba (Demostraciones, Confianza) y una columna lateral vertical "Firma Digital":
- Nivel inferior (rojo): **"Sintaxis + formatos (Texto + Links + Lenguajes de codificación)"**, etiquetado a la izquierda como "Recuperación de información". A la derecha, iconos de documentos/HTML conectados. Base: "Unicode" y "URI".
- Nivel medio (naranja): **"Datos + esquemas (entidades + relaciones)"**, etiquetado como "Bases de datos". A la derecha, mini-diagrama de grafo con nodos numerados.
- Nivel superior (verde): **"Lógicas + Ontologías (conceptos + Conocimiento)"**, etiquetado como "KR - Lógica". Incluye fórmulas lógicas:
$$\forall x \exists y (R(x,y) \rightarrow \exists z Q(z))$$
$$A \cup B, C \rightarrow D \sqcap E$$
- Encima: "Demostraciones" y "Confianza" (niveles conceptuales superiores no detallados).

## Slide 9

**Tres niveles de acceso a datos**

Diagrama de 3 cajas transparentes apiladas verticalmente (estilo vitrina 3D, color verde/celeste), cada una con una flecha dorada apuntando desde la derecha con su etiqueta:
- Superior: **"Conceptos + Conocimientos (cuerpo organizado de afirmaciones)"** ← "Inteligencia Artificial"
- Media: **"Objetos (entidades) + relaciones"** (representado con un cilindro verde de base de datos) ← "Bases de Datos"
- Inferior: icono de documentos apilados con flecha circular (refresh) ← "Recuperación de la información"

Debajo de la caja inferior: "Texto + Enlaces"

## Slide 10

**Tres enfoques / tres áreas**

Tres bloques de texto con encabezado en azul y contenido en lila, más una viñeta cómica (dibujo de hombre vomitando en un inodoro, etiqueta "INFORMATION RETRIEVAL" — chiste visual sobre "recuperar información").

1. **Recuperación de información**
   - recuperar información a partir de fuentes
   - Aproximación / cobertura / escalabilidad
   - Ojalá precisión

2. **Bases de datos**
   - Administrar y organizar datos limpios con precisión
   - Separación de modelamiento e implementación
   - Ojalá razonamiento/deducción sobre ellos

3. **Representación del Conocimiento**
   - Razonar sobre datos organizados
   - Preocupación por la expresividad

## Slide 11

Slide separador (banda azul centrada). Texto: "¿QUÉ SON GRANDES DATOS? VOLUMEN DE DATOS"

## Slide 12

**Tamaño de datos**

Tabla:

| Nombre | Estándar SI | Uso Binario |
|---|---|---|
| Kilobyte | 10 e 3 | 2 e 10 |
| Megabyte | 10 e 6 | 2 e 20 |
| Gigabyte | 10 e 9 | 2 e 30 |
| Terabyte | 10 e 12 | 2 e 40 |
| Petabyte | 10 e 15 | 2 e 50 |
| Exabyte | 10 e 18 | 2 e 60 |
| Zettabyte | 10 e 21 | 2 e 70 |

(Filas coloreadas: verde para KB/MB/GB, amarillo para TB/PB, rojo para EB/ZB — codificación visual de escala creciente de magnitud/peligro.)

## Slide 13

**Modelos y formatos de datos**

Texto con iconos ilustrativos a la derecha (email/arroba, libro "Cien años de soledad", foto de un perro, video de fútbol con botón play):
- KILO 10^3 (2^10): Texto (email, documento)
- MEGA 10^6 (2^20): Libro, fotografía
- GIGA 10^9 (2^30): Memoria RAM, buen video
- (Este es nuestro mundo...)

## Slide 14

**Volumen de datos I: poniéndose serios**

TERA 10^12  2^{40}
- Tráfico Global de Internet (20 TB p. sec)
- Biblioteca del Congreso (USA): 200 TB
- Discos de 1TB (2007)
- Wikipedia: 10 Terabyte dump (2015)
- 3-D movie Monsters Vs Aliens (necesitó 100 TB disco) [enlace subrayado]

Nota adhesiva cian rotada con texto: "No escala humana. Pero, lo maneja cualquier empresa/ experimento que se respete"

## Slide 15

**Modelos y formatos de datos**

PETA 10^15  2^50
- Tráfico Global Internet por hora: 70 PB
- Internet Archive (50 PB) (crece 100 TB por mes)
- Google procesa 100 petabytes de datos cada día
- 1/2 PB: filmar la vida de una persona (100 años en alta definición)
- Facebook tiene 60 mil millones de imágenes, esto es 1,5PB
- Los experimentos del LHC (Large Hadron Collider) [enlace] producen 30 petabytes de datos al año

## Slide 16

**Futuro próximo**

Dos recuadros celestes con ilustración decorativa central (dibujo de persona escribiendo/pensando con nube de texto manuscrito):

EXA 10^18 (2^60)
- Todas las palabras que se han hablado aprox. 5 EXB texto (digitalizadas)
- Google almacena 15 EB
- Tráfico internet diario 2 EB
- El premio del Sultán en el ajedrez: 2^64: casi 1 EXP

Zetta 10^21 (2^70)
- El universo digital (todos los datos o archivos almacenados digitalmente) alcanza 1,2 millones de petabytes, o 1,2 zettabytes.
- Tráfico Internet anual: 1 ZB

## Slide 17

Slide separador (banda azul centrada). Texto: "MODELOS Y FORMATOS DE DATOS"

## Slide 18

**¿Formato de datos? Depende...**

Lista de formatos mencionados (texto centrado en negrita):
XML, JSON, RSS, Atom, YAML, iCalendar, CSV, Serialized PHP, HTML, PNG, GeoRSS, vCard, Text, RDF, OPML, MediaRSS, VML, TV-Anytime, hCalendar, FOAX, XSPF, SQL, GML, CDF

## Slide 19

**Modelo =/= Formato**

Lista numerada:
1. **Binario** (eficiente, ilegible)
2. **Texto** (natural para humanos, ineficiente, poca o nada estructura)
3. **Tablas** (buena organización, históricamente popular, eficiente, excelente soporte: RDBMS; versión "reguleque": CSV)
4. **Documentos** (natural para humanos, semi-estructurado, formalizado como XML, JSON, et al.)
5. **Grafos** (excelente expresividad, difícil -aún- de procesar, poco soporte. Es lo que viene)

## Slide 20

**Tres modelos básicos**

Tres ejemplos visuales lado a lado:
- Izquierda: captura de una tabla de datos numérica (estadísticas con columnas y filas densas, ilegibles en detalle) — etiquetada "Tablas / relaciones"
- Centro: diagrama de árbol jerárquico — nodo "HTML" se ramifica en "Head" (→ "Title") y "Body" (→ "Content" → "Page Link", "Some Text"; → "Footer" → "Footer content Link" → flecha hacia bloque "A" → óvalo "W3") — etiquetado "Documentos / árboles"
- Derecha: grafo de ontologías biomédicas con nodos verdes elípticos (Disease Ontology, Human Phenotype Ontology, Pathway Ontology, Mammalian Phenotype Ontology) conectados mediante relaciones etiquetadas (involved_in, has_member, associated_with, etc.) a nodos celestes (Human Gene, Mouse Gene, Rat Gene) y estos a nodos verdes inferiores (Molecular Function, Cell Component, Biological Process / Gene Ontology) — etiquetado "Grafos / redes"

## Slide 21

**Dos modelos "nuevos" (en base de datos)**

Dos ejemplos visuales:
- Izquierda: captura de un documento de texto en dos columnas (ilegible en detalle, sobre contaminación de suelos) — etiquetado "Texto"
- Derecha: captura de una interfaz de editor de video mostrando una niña en un columpio, con controles de reproducción, línea de tiempo, botón "Cortar Video (Edit)", ícono de tijeras cortando una cinta de película — etiquetado "Imágenes y videos"

## Slide 22

Slide separador (banda azul centrada). Texto: "EL CICLO DE LOS DATOS"

## Slide 23

**Ciclo de vida de los datos**

Diagrama circular sobre fondo celeste. Círculo central con texto "Ciclo de vida de los datos" rodeado por una flecha circular roja de dos tramos que indica dirección de flujo. Alrededor, 10 círculos rosados numerados en sentido horario, cada uno con un punto de color indicando nivel de riesgo (leyenda arriba derecha: rojo=Alto peligro, amarillo=Peligro moderado, verde=Poco peligro):

1. Colección — amarillo
2. Relevancia — verde
3. Clasificación — verde
4. Manipulación y Almacenamiento — rojo
5. Transmisión y Transporte — amarillo
6. Manipulación Conversión o Alteración — rojo
7. Publicación — amarillo
8. Backup — amarillo
9. Retención — amarillo
10. Destrucción — amarillo

Fuente citada: "Referencian: SearchSecurity TechTarget"

## Slide 24

Slide separador (banda azul centrada). Texto: "EL MUNDO DE LAS BASES DE DATOS No SQL"

## Slide 25

**Formas de accesos a datos**

Tabla/matriz 2x3 (ejes: filas = estructurado/no estructurado; columnas = humana/semi/automática):

| | humana | semi | automática |
|---|---|---|---|
| **no estructurado** | Navegación | Buscador / expresiones regulares | Técnicas estadísticas (NLP / AI) |
| **estructurado** | Formulario | Lenguaje de consulta (SQL) | API / Web Service Endpoints |

## Slide 26

**Tipo de base de datos NoSQL**

Tabla comparativa de 4 columnas (Document, Graph, Key-Value, Wide-Column) con 3 filas: diagrama conceptual, ejemplo de datos, y logos de productos.

Fila 1 (diagramas):
- Document: iconos de documentos apilados
- Graph: grafo con nodos y aristas
- Key-Value: pares Key→Value apilados
- Wide-Column: cuadrícula tipo tabla de tonos grises

Fila 2 (ejemplos de datos):
- Document: código JSON `{"user":{"id":"143","name":"improgrammer","city":"New York"}}`
- Graph: grafo con nodos numerados 1-4 conectados por "edge"
- Key-Value: pares `143→John Smith`, `78→Oduor park`, `285→New york`, `129→(0 856 1489)`
- Wide-Column: tabla con filas 1,2,3 (Fruit, City, State) y columnas con valores tipo A|Foo B|Baz

Fila 3 (logos de productos):
- Document: mongoDB, ArangoDB, CouchDB
- Graph: AllegroGraph, neo4j
- Key-Value: redis, Ignite, Memcached, riak
- Wide-Column: cassandra, Apache HBase, Scylla

## Slide 27

**(sin título visible en la slide — diagrama de ecosistema de bases de datos, no capturado en el texto plano)**

Diagrama de conjuntos (Venn/burbujas anidadas) mostrando el panorama de tecnologías de bases de datos, dividido en dos grandes regiones "Non-relational" (izquierda) y "Relational" (derecha), con subcategorías:
- **Non-relational**: contiene "Operational" (con subcategorías "NoSQL" → "Key Value" (Riak, Redis, Membrain, Cassandra, Voldemort, BerkeleyDB), "Document" (Lotus Notes, CouchDB, MongoDB, RavenDB, Cloudant), "Big tables" (Hypertable, HBase), "Graph" (InfiniteGraph, Neo4J, GraphDB)) y "Analytic" (Mapr, Piccolo, Dryad, Hadoop, Brisk, Hadapt)
- **Relational**: contiene motores tradicionales (Infobright, Netezza, ParAccel, SAP Sybase IQ, Teradata, EMC, Calpont, IBM InfoSphere, Aster Data, Greenplum, VectorWise, HP Vertica, Oracle, IBM DB2, SQL Server, JustOne, MySQL, Ingres, PostgreSQL, SAP Sybase ASE, EnterpriseDB) y "NewSQL" (HandlerSocket, Akiban, Amazon RDS, SQL Azure, Database.com, Xeround, FathomDB, MySQL Cluster, Clustrix, Drizzle, GenieDB, ScalArc, Schooner MySQL, CodeFutures, Tokutek, ScaleBase, NimbusDB, Continuent, VoltDB, Translattice) y "as-a-Service" (App Engine Datastore, SimpleDB)
- Abajo: "Data Grid/Cache" (IBM eXtreme Scale, GridGain, ScaleOut, Terracotta, GigaSpaces, Oracle Coherence, VMware GemFire, InfiniSpan, memcached, CloudTran), conectado por flechas grandes etiquetadas "Data Cache", "SPRAIN", "Cloud Enablement" hacia las regiones NoSQL/NewSQL/Relational.

Es un mapa visual exhaustivo del ecosistema de motores de bases de datos clasificados por paradigma.

## Slide 28

**Guía visual de sistemas NoSQL**

Diagrama de triángulo (teorema CAP) con tres vértices etiquetados A, C, P:
- **A** (arriba, celeste): Disponibilidad — "Cada cliente siempre puede leer y escribir"
- **C** (abajo izquierda): Consistencia — "Todos los clientes siempre tienen la misma vista de los datos"
- **P** (abajo derecha): Tolerancia de partición — "El sistema funciona bien a pesar de las particiones físicas de la red"

Centro del triángulo: "Pick two"

En cada lado del triángulo, ejemplos de sistemas que cumplen esa combinación:
- **CA** (lado A-C): RDBMS (MySQL, Postgres, etc.) [rojo=Relacional], Aster Data, Greenplum, Vertica [verde=Column-Oriented]
- **AP** (lado A-P): Dynamo, Voldemort, Tokyo Cabinet, KAI [azul=Key-Value]; Cassandra, SimpleDB, Couch DB, Riak [verde]
- **CP** (lado C-P): BigTable, Hypertable, Hbase [verde]; MongoDB, Terrastore, Scalaris [azul]; Berkeley DB, MemcacheDB, Redis [azul oscuro=Document-Oriented]

Leyenda de colores de Data Models (arriba derecha): Relacional (rojo), Key-Value (azul), Column-Oriented/Tabular (verde), Document-Oriented (azul oscuro)

## Slide 29

**Habilidades de ciencia de los datos**

Diagrama de Venn de 4 círculos superpuestos (rojo, celeste, amarillo, verde) formando zonas de intersección, centrado en "Ciencia de datos":
- Rojo: **Habilidades de piratería**
- Celeste: **Experiencia sustantiva**
- Amarillo: **Conocimiento de matemáticas y estadísticas**
- Verde (no explícito como círculo propio pero presente en intersección): **Aprendizaje automático** e **Investigación tradicional**

Intersecciones etiquetadas:
- Rojo ∩ Celeste = "Zona peligrosa" (icono calavera)
- Rojo ∩ Amarillo = "Aprendizaje automático"
- Celeste ∩ Amarillo = "Investigación tradicional"
- Centro (los 3): "Ciencia de datos"

A la derecha, tabla explicativa con icono + descripción por cada segmento:
- Ciencia de datos: requiere intersección de habilidades de piratería, matemáticas/estadística y experiencia sustancial en un campo de la ciencia.
- Habilidades de piratería: necesarias para trabajar con datos electrónicos masivos (adquirir, limpiar, manipular).
- Matemáticas y estadística: permite elegir métodos/herramientas adecuados.
- Experiencia sostenida: crucial para generar preguntas/hipótesis e interpretar resultados.
- Investigación tradicional: intersección de matemáticas/estadística con experiencia científica.
- Aprendizaje automático: combina piratería + matemáticas/estadística, sin motivación científica.
- Zona peligrosa: piratería + experiencia científica sin métodos rigurosos → análisis incorrectos.

## Slide 30

Slide separador (banda azul centrada). Texto: "Introducción a MongoDB"

## Slide 31

**Basado en Documentos**

- Las bases de datos almacenan y recuperan documentos que pueden ser XML, JSON, BSON, etc.
- Los documentos almacenados son similares unos con otros pero no necesariamente con la misma estructura.

## Slide 32

**Mongo DB**

- Su nombre surge de la palabra en inglés "humongous" (que significa enorme).
- MongoDB guarda estructuras de datos en documentos tipo JSON (JavaScript Object Notation) con un esquema dinámico.
- Internamente MongoDB almacena los datos en formato BSON (Binary JavaScript Object Notation).
- BSON está diseñado para tener un almacenamiento y velocidad más eficiente.

## Slide 33

**Basado en Documentos** (línea de tiempo histórica)

Diagrama de línea de tiempo vertical con 4 hitos y 3 iconos categoría a la izquierda (Bases de Datos Documentales / Bases de Datos de Código Abierto / Bases de Datos de Propósitos Generales):

- **2007**: La empresa 10gen lo desarrolla cuando estaba desarrollando una Plataforma cómo servicio (PaaS - Platform as a Service). Similar a Google App Engine.
- **2009**: En este año MongoDB es lanzado como Producto. Es publicado bajo licencia de código abierto AGPL.
- **2011**: Se lanza la versión 1.4 considerada como una Base de Datos lista para producción.
- **2021**: Actualmente MongoDB está por la versión 5.x y es la Base de Datos NoSQL con mayor popularidad.

## Slide 34

**Terminología RDBMS vs. Document Based (MongoDB)**

Tabla:

| RDBMS | MongoDB |
|---|---|
| Database instance | MongoDB instance |
| Database / Schema | Database |
| Table | Collection |
| Row | Document |
| Rowid | _id |
| Join | Dbref |

## Slide 35

**Modelado de Relaciones entre Documentos**

Sección "Relaciones Uno a Uno con documentos embebidos": Si la dirección es un dato frecuentemente consultado junto con el Nombre de la persona, la mejor opción será embeber la dirección en los datos de la persona.

Modelo Normalizado (dos colecciones separadas):
```
Colección Personas
{ _id: "u0001",
nombre: "Juan Martín Hernandez" }

Colección Direcciones
{ persona_id: "u0001",
calle: "Malabia 2277",
ciudad: "CABA",
provincia: "CABA",
codPostal: "1425" }
```

Flecha (→) hacia Modelo Embebido:
```
Colección Personas
{ _id: "u0001",
nombre: "Juan Martín Hernandez"

direccion:{calle: "Malabia 2277",
           ciudad: "CABA",
           provincia: "CABA",
           codPostal: "1425" }
}
```

Texto: "Con una sola consulta podríamos recuperar toda la información de una persona."

## Slide 36

**En qué casos usarlas?**

- **Logging de Eventos**
  - Las bases de datos basadas en documentos puede loguear cualquier clase de eventos y almacenarlos con sus diferentes estructuras.
  - Pueden funcionar como un repositorio central de logueo de eventos.
- **CMS, blogging**
  - Su falta de estructura predefinida hace que funcionen bien para este tipo de aplicaciones.
- **Web-analytics / Real-Time analytics**
  - Almacenar cantidad de vistas a una página o visitantes únicos.
- **Commerce**
  - A menudo requieren tener esquemas flexibles para los productos y órdenes
