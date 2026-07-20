---
curso: BD2
titulo: 14 BD No SQL 1
slides: 36
fuente: 14 BD No SQL 1.pdf
---

# 14 BD No SQL 1

## Índice

- [Introducción](#introducción)
  - [Línea de tiempo: orígenes de las bases de datos relacionales](#línea-de-tiempo-orígenes-de-las-bases-de-datos-relacionales)
  - [Línea de tiempo: características de las bases de datos relacionales](#línea-de-tiempo-características-de-las-bases-de-datos-relacionales)
  - [Línea de tiempo: la World Wide Web y la evolución del almacenamiento](#línea-de-tiempo-la-world-wide-web-y-la-evolución-del-almacenamiento)
  - [Línea de tiempo: bases de datos no relacionales](#línea-de-tiempo-bases-de-datos-no-relacionales)
  - [Línea de tiempo: primeros enfoques distribuidos](#línea-de-tiempo-primeros-enfoques-distribuidos)
  - [Línea de tiempo: origen del término NoSQL](#línea-de-tiempo-origen-del-término-nosql)
  - [Línea de tiempo: smartphones y nuevas necesidades de datos](#línea-de-tiempo-smartphones-y-nuevas-necesidades-de-datos)
- [Limitaciones del Modelo Relacional](#limitaciones-del-modelo-relacional)
  - [¿Cuándo no usar un SGBD Relacional?](#cuándo-no-usar-un-sgbd-relacional)
  - [El costo del ACID](#el-costo-del-acid)
  - [Complejidad del esquema relacional](#complejidad-del-esquema-relacional)
- [Escalabilidad](#escalabilidad)
  - [Escalabilidad horizontal y vertical](#escalabilidad-horizontal-y-vertical)
  - [Teorema CAP](#teorema-cap)
- [Tendencias Emergentes](#tendencias-emergentes)
- [Modelos de Datos NoSQL](#modelos-de-datos-nosql)
  - [Panorama de modelos](#panorama-de-modelos)
  - [BD Clave-Valor](#bd-clave-valor)
  - [BD de Documentos](#bd-de-documentos)
  - [BD de Columnas Anchas](#bd-de-columnas-anchas)
  - [BD de Grafos](#bd-de-grafos)
- [Comparativa Relacional vs. NoSQL](#comparativa-relacional-vs-nosql)
  - [Caso 1: Sitio Web de Comercio Electrónico](#caso-1-sitio-web-de-comercio-electrónico)
  - [Caso 2: Análisis de datos en tiempo real](#caso-2-análisis-de-datos-en-tiempo-real)
  - [Caso 3: Juegos MultiPlayer en Tiempo Real](#caso-3-juegos-multiplayer-en-tiempo-real)
  - [Caso 4: Sistema de Recomendación de Productos](#caso-4-sistema-de-recomendación-de-productos)
- [Conclusiones](#conclusiones)
- [Glosario](#glosario)

## Introducción

### Línea de tiempo: orígenes de las bases de datos relacionales

**Figura:** Línea de tiempo horizontal con flecha azul apuntando hacia la derecha. Al inicio de la línea, una marca vertical con el año «1970» arriba y el texto «BD Relacionales» debajo. A la izquierda, fotografía histórica en tonos sepia de un técnico con traje de sala limpia (capucha y guantes) trabajando sobre un enorme dispositivo de almacenamiento mecánico montado en un marco metálico turquesa con ruedas.

- Las bases de datos relacionales fueron diseñadas en los años 70 por Edgar F. Codd.
- Su objetivo principal era estructurar la información de manera que se evitara la redundancia, es decir, que los datos no se repitieran innecesariamente.
- **En esa época, el costo de almacenamiento era considerablemente alto, por lo que era crucial optimizar el uso del espacio disponible**

Codd, E. F. (1970). A Relational Model of Data for Large Shared Data Banks. Communications of the ACM, 13(6), 377-387.

(slides 3)

### Línea de tiempo: características de las bases de datos relacionales

**Figura:** Línea de tiempo horizontal con flecha azul apuntando hacia la derecha. Al inicio, marca vertical con el año «1979» arriba y el texto «BD Relacionales» debajo. Debajo de la línea de tiempo, a la izquierda, la misma fotografía histórica de un técnico en sala limpia trabajando sobre hardware de almacenamiento de gran tamaño. Una flecha gris apunta de izquierda a derecha hacia un recuadro gris con un diagrama de características: a la derecha del recuadro, un cilindro tridimensional de base de datos dividido verticalmente en mitad gris oscura y mitad gris clara. Tres líneas verdes conectan el cilindro con tres características a la izquierda, cada una con su icono: lupa con icono de persona — «Expressive Query Language & Secondary Indexes»; monitor con marca de verificación — «Strong Consistency»; maletín — «Enterprise Management & Integrations».

1979

BD Relacionales

**Figura:** Línea de tiempo horizontal con flecha azul; marca en «1979» con texto «BD Relacionales» debajo. A la izquierda, icono de cilindro de base de datos en color teal oscuro. A la derecha, dos tablas relacionales conectadas por una línea azul con la palabra «Relación» escrita verticalmente junto a la conexión.

| Código | Nombre | Curso |
|---|---|---|
| ... | | |
| 201710042 | Molina Orellana Diego | CS1100 |
| 201710043 | Paredes Sanchez Bruno | CS2701 |
| 201710044 | Perez Fu Luis Adrian | CS1102 |
| 201710044 | Perez Fu Luis Adrian | CS2701 |
| ... | | |

**alumnos**

| Código | Nombre |
|---|---|
| … | |
| CS2701 | Base de datos I |
| CS11001 | Programación Orientada a O |
| CS1100 | Introducción a ciencia de la C. |
| ... | |

**cursos**

1979

BD Relacionales

**Figura:** Línea de tiempo horizontal con flecha azul; marca en «1979» con texto «BD Relacionales» debajo. En el centro, diagrama entidad-relación (ER) con las siguientes tablas y columnas conectadas por líneas que representan relaciones: **Address** (`address_id`, `client_id`, `street`, `number`, `zip_code`, `state`, `country_id`); **Client** (`client_id`, `first_name`, `last_name`, `age`); **Order** (`order_id`, `client_id`, `date`); **Country** (`country_id`, `name`); **Phone** (`phone_id`, `client_id`, `country_code`, `phone`); **Item** (`item_id`, `order_id`, `description`, `value`, `amount`). `Client` es la entidad central vinculada a `Address`, `Order` y `Phone`; `Address` se vincula a `Country`; `Order` se vincula a `Item`. A la izquierda, icono de cilindro de base de datos en color teal oscuro. A la derecha del diagrama ER, dos iconos pequeños (engranaje y triángulo) seguidos de la lista de características.

- Restricciones
- Llaves primarias
- Llaves foráneas
- Índices
- Transacciones

1979

BD Relacionales

**Figura:** Línea de tiempo horizontal con flecha azul; marca en «1979» con texto «BD Relacionales» debajo. Una barra horizontal gris clara se extiende desde poco después de 1979 a lo largo de la línea de tiempo. A la izquierda inferior, icono de cilindro de base de datos en color teal/gris oscuro. En el centro inferior, una flecha gris gruesa apunta verticalmente hacia arriba hacia la línea de tiempo y el diagrama de la derecha. A la derecha, un recuadro grande con un diagrama ER masivo y extremadamente denso: cientos de cajas pequeñas (tablas) interconectadas por una red densa de líneas (relaciones), tan denso que los nombres individuales de tablas son ilegibles, visualizando la complejidad de esquemas relacionales a gran escala. El diagrama se superpone parcialmente al extremo de la barra gris de la línea de tiempo.

1979

BD Relacionales

(slides 4–7)

### Línea de tiempo: la World Wide Web y la evolución del almacenamiento

**Figura:** Línea de tiempo horizontal con flecha azul apuntando hacia la derecha. Dos marcas verticales azules: «1979» con texto «BD Relacionales» debajo y un icono de cilindro de base de datos teal plano; «1991» con un icono de globo terráqueo y cursor de ratón señalándolo. Una barra horizontal gris abarca el período entre 1979 y poco después de 1991. Debajo de la marca 1991, el texto «WWW» en fuente serif gris en negrita. Debajo, ilustración enmarcada en óvalo que muestra una red densa de pantallas de computadora, laptops y tablets interconectadas sobre una superficie con tonos naranjas que parece un circuito impreso.

1979

BD Relacionales

WWW

1991

**Figura:** Línea de tiempo horizontal con flecha azul y barra gris gruesa. Marcas en «1979» («BD Relacionales») y «1991» (icono de globo con cursor). Debajo: a la izquierda, icono de cilindro de base de datos gris oscuro (base de datos centralizada tradicional). En el centro, collage ovalado con red densa de pantallas y hardware con el texto «WWW» en negrita encima. Una flecha gris apunta del centro hacia iconos modernos a la derecha: icono de nube con red jerárquica de servidores debajo (uno ramificando en tres nodos); icono de engranaje con el texto «API»; icono de cilindro de base de datos con candado superpuesto (almacenamiento seguro/distribuido).

1979

BD Relacionales

WWW

1991

(slides 8–9)

### Línea de tiempo: bases de datos no relacionales

**Figura:** Línea de tiempo horizontal con tres puntos marcados: «1979» — «BD Relacionales»; «1991» — icono de globo con cursor de ratón; «00'» — «BD No Relacionales». Diagrama comparativo debajo: lado izquierdo con icono de rack de servidores, monitor y engranajes dentro de un círculo; flecha hacia abajo a otro círculo con signo de dólar ($) cayendo en una mano. Flecha desde el lado izquierdo hacia un panel gris grande en el centro-derecha con un cilindro de base de datos 3D en el centro. A la izquierda del cilindro (líneas grises, apariencia atenuada): «Expressive Query Language & Secondary Indexes» (icono de lupa), «Strong Consistency» (icono de documento con marca de verificación), «Enterprise Management & Integrations» (icono de maletín). A la derecha del cilindro (líneas verdes con flechas): «Flexibility» (icono de dial radiante), «Scalability & Performance» (icono de velocímetro), «Always On, Global Deployments» (icono de globo con reloj).

1979

BD Relacionales

00'

BD No Relacionales

1991

(slides 10)

### Línea de tiempo: primeros enfoques distribuidos

**Figura:** Línea de tiempo horizontal con barra gris y tres marcas: «1979» — «BD Relacionales»; «2006» — «BigTable»; «2007» — «DynamoDB». Debajo de la marca 1979, recuadro blanco con texto explicativo. Debajo del recuadro, tres iconos de racks de servidores azules en fila; flecha amarilla apuntando hacia la derecha debajo de los servidores con las etiquetas «Horizontal Scaling» y «(Scaling out)» en texto más pequeño. A la derecha, logos oficiales: Google BigTable (icono hexagonal azul) junto a 2006; amazon DynamoDB (icono de globo/base de datos azul) junto a 2007.

Primeros enfoques distribuidos para el almacenamiento y la recuperación de datos, priorizando la escalabilidad horizontal.

1979

BD Relacionales

2006

BigTable

2007

DynamoDB

(slides 11)

### Línea de tiempo: origen del término NoSQL

**Figura:** Línea de tiempo horizontal con dos marcas: «1979» — «BD Relacionales»; «2009» — icono de hoja verde con el texto «mongoDB». A la izquierda debajo de la línea de tiempo, icono de cilindro de base de datos con lista de viñetas. A la derecha, recuadro de texto con la explicación de Eric Evans. En la parte inferior derecha, definición del acrónimo.

Google, Amazon, …
- Sistemas Distribuidos
- Open Source
- No Relacionales

Eric Evans reutilizó el término para un evento sobre bases de datos no relacionales, distribuidas y no conformes a las propiedades ACID propias de los sistemas relacionales. A partir de ese año se ha observado un incremento significativo de las tecnologías NoSQL.

NoSQL:
Not Only SQL

1979

BD Relacionales

2009

**Figura:** Línea de tiempo horizontal con barra gris y flecha azul. Marca «1979» a la izquierda con «BD Relacionales» debajo. Marca «2009» a la derecha con el logo de MongoDB (hoja verde) debajo. A la izquierda inferior, icono de cilindro de base de datos gris con lista de viñetas. A la derecha inferior, captura de pantalla de un tweet de Chris Anderson (@jchris) fechado 12 de mayo de 2009 con el texto: «@spyced I'm living in Portland today, maybe in SF by the #nosql date. Hoping @skr still has time for a CouchDB talk.» Debajo de la captura, recuadro prominente con el hashtag «#nosql».

Google, Amazon, …
- Sistemas Distribuidos
- Open Source
- No Relacionales

#nosql

1979

BD Relacionales

2009

(slides 12–13)

### Línea de tiempo: smartphones y nuevas necesidades de datos

**Figura:** Línea de tiempo horizontal con flecha azul. Marca «1979» a la izquierda con «BD Relacionales» y un icono de cilindro de base de datos gris oscuro grande. Marca «2007» a la derecha con icono de smartphone; una barra rectangular gris sobre la línea de tiempo comienza justo antes de 2007 y se extiende hacia la derecha. Entre las marcas, imagen circular grande etiquetada «SmartPhones» en tipografía estilizada, mostrando múltiples smartphones interconectados por una red de líneas brillantes e iconos de apps/redes sociales. A la derecha de la imagen circular, flecha gris apuntando hacia un grupo de iconos y lista: iconos de tira de película, foto y nota musical (medios); icono de nube conectada a tres nodos de servidor; icono de engranaje con «API» y cilindro de base de datos con candado.

SmartPhones

- BD en Cache
- BD Vectorial
  - Streaming
  - Visión Artificial
  - Inteligencia Artificial

1979

BD Relacionales

2007

(slides 14)

## Limitaciones del Modelo Relacional

### ¿Cuándo no usar un SGBD Relacional?

- Structured Query Language (SQL):
  - Lenguaje declarativo, Rico en características
  - Modelo poco flexible, Difícil de optimizar!
- Atomicity, Consistency, Isolation, Durability (ACID):
  - Asegura de que la base de datos se mantenga correcta
    - Incluso si hay mucho tráfico!
  - Las transacciones son costosas y complejas
    - Multi-phase locks, multi-versioning, write ahead logging
- La distribución no es sencilla.

**Figura:** Lista jerárquica con viñetas: los puntos en verde representan ventajas («Lenguaje declarativo, Rico en características»; «Asegura de que la base de datos se mantenga correctas» con subpunto «Incluso si hay mucho tráfico!») y los puntos en rojo representan desventajas o desafíos («Modelo poco flexible, Difícil de optimizar!»; «Las transacciones son costosas y complejas» con subpunto «Multi-phase locks, multi-versioning, write ahead logging»; «La distribución no es sencilla.»).

(slides 16)

### El costo del ACID

**Figura:** Gráfico de barras apiladas que muestra la distribución de instrucciones de CPU para una transacción. Segmentos de la barra (de abajo hacia arriba): «Useful work» — 6.8%; «Buffer manager» — 34.6%; «Latching» — 14.2%; «Locking» — 16.3%; «Logging» — 11.9%; «Hand-coded optimizations» — 16.2%. El 93.2% restante corresponde a sobrecarga administrativa. A la derecha del gráfico, dos puntos de comparación de rendimiento en texto rojo y azul. En la parte inferior derecha, captura de fragmento del artículo «OLTP Through the Looking Glass, and What We Found There» de Stavros Harizopoulos, Daniel J. Abadi, Samuel Madden y Michael Stonebraker.

- 640 transacciones por segundo para un sistema con soporte transaccional completo (ACID).
- 12700 transacciones por segundo para un sistema sin logging y sin transacciones o programación de bloqueos

Más del 90% de las instrucciones se dedican a sobrecarga administrativa, no al procesamiento directo de la transacción.

https://dl.acm.org/doi/10.1145/1376616.1376713

(slides 17)

### Complejidad del esquema relacional

**Figura:** Diagrama entidad-relación (ERD) o esquema de base de datos relacional a gran escala, visto con zoom alejado. Consiste en cientos de representaciones de tablas (rectángulos pequeños) conectadas por una red densa e intrincada de líneas que representan relaciones (llaves foráneas). Cada rectángulo tiene una barra de encabezado azul (nombre de tabla) seguida de una lista de columnas. Las líneas son tan numerosas que en muchas áreas crean un efecto de borrón gris sólido. Hay un cluster central donde la densidad de tablas y conexiones es máxima, con submódulos o grupos de tablas relacionadas ramificándose hacia los bordes. La mayoría de las tablas tienen tema azul y blanco; unas pocas tablas hacia el centro-inferior están resaltadas en verde. El texto específico (nombres de tablas, columnas, tipos de datos) es completamente ilegible debido a la perspectiva alejada; la imagen transmite la escala y complejidad del esquema.

(slides 18)

## Escalabilidad

### Escalabilidad horizontal y vertical

**Figura:** Diagrama comparativo de escalado vertical y horizontal. Lado izquierdo — Escalado vertical: dos iconos de racks de servidores, uno significativamente más grande que el otro; flecha amarilla apuntando hacia arriba junto al servidor más grande con etiquetas «RAM», «CPU» e «I/O»; debajo, texto «Vertical Scaling» y «(Scaling up)». Sección central — recuadro vertical gris con dos mitades: mitad superior con icono de velocímetro y texto «Scalability & Performance»; mitad inferior con icono de globo y texto «Always On, Global Deployments». Lado derecho — Escalado horizontal: tres iconos idénticos de racks de servidores colocados en fila; flecha amarilla apuntando hacia la derecha debajo de los servidores; debajo, texto «Horizontal Scaling» y «(Scaling out)».

RAM

CPU

I/O

(slides 19)

### Teorema CAP

Teorema CAP

**Figura:** Diagrama de Venn con tres círculos superpuestos. Círculo superior verde — «Consistency»: «All clients see the same view of data, even right after update or delete.» Círculo inferior izquierdo azul — «Availability»: «All clients can find a replica of data, even in case of partial node failures.» Círculo inferior derecho naranja — «Partitioning»: «The system continues to work as expected, even in presence of partial network failure.» Intersecciones etiquetadas: «CA» (Consistency y Availability), «CP» (Consistency y Partitioning), «AP» (Availability y Partitioning). En el centro donde los tres círculos se superponen, una «X» roja indicando que un sistema distribuido no puede garantizar simultáneamente las tres propiedades.

- Consistencia (Consistency): Todos los nodos del sistema ven los mismos datos al mismo tiempo. Es decir, una lectura devuelve siempre la última escritura realizada.
- Disponibilidad (Availability): Cada solicitud recibe una respuesta, incluso si algunos nodos están caídos.
- Tolerancia a particiones (Partitioning): El sistema sigue funcionando incluso si hay fallos de comunicación entre nodos.

El teorema afirma que un sistema distribuido debe elegir entre:

- Consistencia y tolerancia a particiones (CP): El sistema puede rechazar solicitudes para mantener datos coherentes.
  - Fuerte consistencia, Bases de datos relacionales distribuidas.
- Disponibilidad y tolerancia a particiones (AP): El sistema responde siempre, aunque los datos puedan estar desactualizados.
  - Alta disponibilidad, Bases NoSQL

No es posible garantizar las tres simultáneamente en presencia de fallos de red.

**Figura:** Diagrama de Venn con tres círculos superpuestos que representan las propiedades del teorema CAP. Círculo superior verde etiquetado **Consistency** con el texto: «All clients see the same view of data, even right after update or delete.» Círculo inferior izquierdo azul etiquetado **Availability** con el texto: «All clients can find a replica of data, even in case of partial node failures.» Círculo inferior derecho naranja etiquetado **Partitioning** con el texto: «The system continues to work as expected, even in presence of partial network failure.» En las intersecciones aparecen las etiquetas **CA** (entre Consistency y Availability), **CP** (entre Consistency y Partitioning) y **AP** (entre Availability y Partitioning). En el centro, donde convergen los tres círculos, hay una **X** roja que indica que no es posible garantizar las tres propiedades simultáneamente. A la derecha del diagrama, el texto en español desarrolla las opciones CP y AP con sus viñetas asociadas.

(slides 20–21)

## Tendencias Emergentes

Integración de IA y Machine Learning

- La integración de inteligencia artificial y machine learning en bases de datos está revolucionando la forma en que se gestionan y analizan los datos.

Bases de Datos en la Nube

- El uso de bases de datos en la nube facilita el acceso y la escalabilidad, permitiendo a las empresas gestionar grandes volúmenes de datos de manera eficiente.

Datos en Tiempo Real

- El crecimiento de tecnologías de datos en tiempo real permite a las empresas tomar decisiones informadas basadas en análisis instantáneos de datos.

**Figura:** Ilustración en el lado izquierdo que muestra una cuadrícula tridimensional en perspectiva de color azul oscuro. Sobre la cuadrícula se disponen múltiples iconos de nubes en tonos cian brillante, cada uno dentro de un rectángulo redondeado. Algunos iconos tienen un círculo punteado alrededor de su base, sugiriendo nodos conectados o distribuidos en un entorno de nube. A la derecha, el texto con los tres apartados de tendencias emergentes.

(slides 22)

## Modelos de Datos NoSQL

### Panorama de modelos

**Key-Value**

- DynamoDB (2007/2012)
- Redis (2009)

**Column-Family**

- Google BigTable (2006/2015)
- Apache Cassandra (2008)
- Hbase (2008)

**Graph**

- Neo4j (2007)

**Document**

- CouchDB (2005)
- MongoDB (2009)
- CouchBase (2012)

**Figura:** Recuadro con borde azul titulado «NoSQL» en el lado izquierdo, que contiene cuatro diagramas apilados verticalmente, cada uno con su etiqueta y ejemplos a la derecha:

1. **Key-Value:** Tres filas, cada una con un rectángulo azul claro etiquetado «key» y una flecha apuntando a un óvalo azul oscuro etiquetado «value».
2. **Column-Family:** Estructura tabular con filas numeradas 1, 2 y 3. Cada fila contiene celdas con pares clave-valor internos:
   - Fila 1: `Fruit A|Foo`, `B|Baz`
   - Fila 2: `City E|DC`, `D|PLA`, `G|FLD`
   - Fila 3: `State A|NZ`, `C|CL`
3. **Graph:** Diagrama de red con varios nodos circulares en distintos tonos de azul conectados por flechas direccionales que representan relaciones entre entidades.
4. **Document:** Icono de dos hojas de papel superpuestas con líneas horizontales que representan documentos de texto (como JSON o XML).

A la derecha de cada diagrama, la lista de bases de datos con sus años de lanzamiento.

(slides 24)

### BD Clave-Valor

Casos de Uso: Caché, almacenamiento de sesiones, configuraciones.

**Figura:** Diagrama que ilustra el funcionamiento de una base de datos clave-valor como caché entre una aplicación cliente y una base de datos SQL persistente.

**Representación de datos clave-valor (parte superior derecha):** Ejemplos en color naranja:
- Clave `User1:Position` → Valor `"Striker"`
- Clave `User1:Name` → Valor `"Sami"`
- Clave `User1:Team` → Valor `{33, 12, 65, 99}` (lista/conjunto)
- Clave `User2:Salary` → Valor `45000` (número)

Una flecha naranja apunta desde estos ejemplos hacia un icono rojo que representa la base de datos clave-valor.

**Flujo del sistema (centro):** Un **Client** (iconos de laptop y teléfono) se conecta a un servidor de aplicación (cubo wireframe). El servidor interactúa con un **Key-Value Store** (cilindro rojo en capas) y una **SQL Database** (cilindro estándar). El flujo numerado es:
1. **Look in cache:** La aplicación primero consulta el almacén clave-valor.
   - **Cache hit > return data:** Si los datos están en caché, se devuelven directamente desde el icono rojo a la aplicación.
2. **Cache miss > look in persistent datastore:** Si no están en caché, la aplicación consulta la **SQL Database**.
3. **Prime cache with data:** Tras obtener los datos de SQL, la aplicación los carga en el almacén clave-valor para futuras solicitudes.

Barra azul inferior con el texto de casos de uso.

(slides 25)

### BD de Documentos

| ENumber | Name | Title |
|---|---|---|
| (PK) | | |

| Type | Coordinate | ENumber |
|---|---|---|
| | | (FK) |

| address | zipcode | ENumber |
|---|---|---|
| | | (FK) |

```json
{
  "name" : "Rubén Terceño",
  "title" : "Senior Solutions Architect",
  "employee_number" : 653,
  "location" : {
    "type" : "Point",
    "coordinates" : [ 43.34, -3.26 ]
  },
  "expertise": [ "MongoDB", "Java", "Geospatial" ],
  "address" : {
    "address1" : "Rutilo 11",
    "address2" : "Piso 1, Oficina 2",
    "zipcode" : "28041"
  }
}
```

**Figura:** Comparación visual entre modelo relacional (izquierda) y modelo de documentos (derecha).

**Lado izquierdo — Representación relacional:** Tres tablas separadas conectadas por líneas que representan un esquema relacional normalizado:
- **Tabla superior:** columnas `ENumber` (subrayado, clave primaria), `Name` y `Title`.
- **Tabla central:** columnas `Type`, `Coordinate` y `ENumber` (subrayado, clave foránea).
- **Tabla inferior:** columnas `address`, `zipcode` y `ENumber` (subrayado, clave foránea).
Líneas conectan la clave primaria `ENumber` de la tabla superior con las claves foráneas `ENumber` de las otras dos tablas, mostrando relación uno-a-muchos.

**Lado derecho — Representación documental:** La misma información consolidada en un único documento JSON dentro de un recuadro blanco con sombra azul, con los campos `name`, `title`, `employee_number`, `location` (objeto anidado con `type` y `coordinates`), `expertise` (array) y `address` (objeto anidado con `address1`, `address2` y `zipcode`).

Barra azul horizontal en la parte inferior con los casos de uso.

(slides 26)

### BD de Columnas Anchas

Casos de Uso: Big Data, análisis de datos en tiempo real, almacenamiento distribuido.

**Figura:** La slide muestra dos representaciones de los mismos datos en una base de datos de columnas anchas.

**Sección superior — Vista tabular con particiones de una sola fila:**
Columnas: `performer`, `born`, `country`, `died`, `founded`, `style`, `type`.
Una flecha señala la columna `performer` como **Partition Key**.
Tres filas (particiones):
- **John Lennon:** 1940, England, 1980, [null], Rock, artist.
- **Paul McCartney:** 1942, England, [null], [null], Rock, artist.
- **The Beatles:** [null], England, [null], 1957, Rock, band.
Etiquetas señalan «partitions» (las filas), «columns» (los encabezados) y «cells» (los valores individuales).

**Sección inferior — Vista Column Family:**
Cada entidad es una fila con una clave seguida de pares columna-valor dinámicos:
- **John Lennon:** `born: 1940`, `country: England`, `died: 1980`, `style: Rock`, `type: artist`.
- **Paul McCartney:** `born: 1942`, `country: England`, `style: Rock`, `type: artist` (omite `died` y `founded` sin necesidad de valores nulos).
- **The Beatles:** `country: England`, `founded: 1957`, `style: Rock`, `type: band` (omite `born` y `died`).

Recuadro azul a la derecha con el texto de casos de uso.

(slides 27)

### BD de Grafos

Casos de Uso: Redes sociales, motores de recomendación, detección de fraudes.

```cypher
MATCH (persona:Persona)-[:AMIGO_DE]->(amigo)
WHERE persona.nombre = "Heider"
RETURN amigo
```

**Figura:** Grafo dirigido con 7 nodos en el centro de la slide. Cada nodo es un rectángulo blanco que contiene un icono de persona y tres propiedades: `feat1`, `feat2` y `name`:
- **node1:** `feat1: a`, `feat2: b`, `name: node1`
- **node2:** `feat1: a`, `feat2: b`, `name: node2`
- **node3:** `feat1: a`, `feat2: b`, `name: node3`
- **node4:** `feat1: c`, `feat2: d`, `name: node4`
- **node5:** `feat1: a`, `feat2: b`, `name: node5`
- **node6:** `feat1: a`, `feat2: b`, `name: node6`
- **node7:** `feat1: a`, `feat2: b`, `name: node7`

Los nodos están conectados por flechas etiquetadas **KNOWS**:
- **node5** → **node1**
- **node6** → **node1** y **node5**
- **node1** → **node2** y **node3**
- **node3** → **node5** y **node6**
- **node2** → **node4**
- **node4** → **node3** y **node7**

Recuadro azul redondeado a la derecha con los casos de uso. En la parte inferior, bloque de código negro con la consulta Cypher.

(slides 28)

## Comparativa Relacional vs. NoSQL

### Caso 1: Sitio Web de Comercio Electrónico

- Los sitios de comercio electrónico, como Temu, manejan una gran cantidad de datos diversos y en constante cambio.
- La variedad de productos es amplia, ya que cada categoría puede tener atributos únicos; por ejemplo, un televisor puede tener especificaciones como tamaño de pantalla y resolución, mientras que una prenda de ropa puede tener talla, color y material.

**Figura:** Ilustración a la derecha del texto que muestra una laptop plateada abierta sobre fondo verde claro. Varias ventanas tipo navegador flotan sobre la pantalla, cada una con un producto diferente y una calificación de cinco estrellas:
- Un maletín de cuero marrón.
- Un control de videojuegos negro.
- Una gorra de béisbol azul.
- Un zapato de tacón rojo.
- Una paleta de maquillaje/cosméticos.
Una figura 3D de una persona con traje azul (vista desde atrás) está de pie sobre el teclado de la laptop, mirando hacia las ventanas flotantes de productos.

- Diseñar el modelo relacional
- Analizar las desventajas del modelo relacional en este caso particular.
- Proponer un modelo de datos NoSQL como alternativa a dichas limitaciones.

**Figura:** Misma ilustración de e-commerce que en la slide anterior: laptop plateada con ventanas flotantes de productos diversos (maletín marrón, control de videojuegos, paleta de maquillaje, zapato de tacón rojo, gorra azul), cada una con sistema de calificación por estrellas (p. ej. el control tiene 3 estrellas, la gorra 4, el zapato 4). Figura 3D de persona con traje azul sobre el teclado mirando hacia los productos.

(slides 30–31)

### Caso 2: Análisis de datos en tiempo real

- Consideremos una red de sensores IoT instalada en una planta industrial, que supervisa variables clave como la temperatura, la presión, la vibración de las máquinas y la calidad del aire.
- Estos sensores producen miles de puntos de datos por segundo, y los administradores requieren acceso a esta información en tiempo real para identificar anomalías, anticipar fallos y hacer ajustes de manera proactiva.
- Los datos más recientes pueden ser esenciales para el análisis en tiempo real, mientras que la información más antigua puede perder relevancia con el tiempo.

**Figura:** A la derecha del texto, dos conjuntos de ilustraciones:
1. **Iconos industriales:** Un grupo de iconos en gris, cian y azul que representan un entorno industrial: fábricas con humo, turbina eólica, cinta transportadora, torre de radio, grúa de construcción, edificio de gran altura y pórtico eléctrico. 2. **Gráficos de datos:** Cuatro gráficos de líneas irregulares en colores azul, azul claro, magenta/morado y amarillo, que ilustran flujos continuos de datos de series temporales provenientes de distintos sensores.

- Diseñar la tabla relacional y las diferentes consultas
- Analizar las desventajas del modelo relacional en este caso particular.
- Proponer un modelo de datos NoSQL como alternativa a dichas limitaciones.

**Figura:** Misma composición visual que la slide anterior: iconos industriales (fábrica con humo, turbina eólica, bulldozer, torre de línea eléctrica, plataforma petrolera, edificio alto) y cuatro gráficos de líneas irregulares en colores teal, azul, magenta y amarillo a la derecha, sugiriendo flujos de datos en tiempo real de sensores.

(slides 32–33)

### Caso 3: Juegos MultiPlayer en Tiempo Real

- Investigar y diseñar el modelo de datos adecuado para una aplicación de juegos multijugador en tiempo real.
  - Se requiere una latencia extremadamente baja y un alto rendimiento en operaciones de lectura y escritura para garantizar una experiencia fluida en tiempo real.
- **NoSQL sugerido:** Bases de datos en memoria clave-valor (Redis).

**Figura:** Infografía en el lado derecho: un globo azul claro en la parte superior conectado por líneas a dos mandos de videojuegos (uno negro y otro rojizo/rosa). Los mandos se conectan hacia abajo a un icono azul oscuro que representa un servidor o base de datos, etiquetado **CACHE** en letras blancas mayúsculas.

(slides 34)

### Caso 4: Sistema de Recomendación de Productos

- Investigar y diseñar un modelo de datos adecuado para un sistema de recomendaciones similar a los utilizados en plataformas como Amazon o Netflix.
  - Se prioriza la flexibilidad y escalabilidad para almacenar y gestionar datos heterogéneos sobre usuarios, preferencias y comportamientos.
- **NoSQL sugerido:** Bases de datos documentales (MongoDB, CouchBase).

**Figura:** Diagrama de filtrado colaborativo en el lado derecho:
- Dos avatares de usuario: una mujer a la izquierda y un hombre a la derecha.
- Una flecha de doble sentido los conecta, etiquetada **similar users**.
- Arriba, dos iconos de claqueta de cine con flechas desde ambos usuarios, etiquetados **watched by both users**.
- Debajo de la mujer, una claqueta naranja con flecha desde ella etiquetada **watched by her**.
- Una flecha desde esa claqueta naranja hacia el hombre, etiquetada **recommended to him**.

(slides 35)

## Conclusiones

- Las bases de datos NoSQL son una solución ideal para aplicaciones en donde la flexibilidad, la escalabilidad y el rendimiento son fundamentales.
- Al eliminar las restricciones de los modelos rígidos y facilitar un almacenamiento eficaz de datos no estructurados, las bases de datos NoSQL se ajustan de manera ideal a las complejas y diversas necesidades de un sistema que requiere actualizaciones estructurales continuas, al mismo tiempo que permiten manejar el aumento en el volumen de datos y la personalización del usuario de forma efectiva.

**Figura:** Slide con título grande «Conclusiones» en gris en la parte superior izquierda. Dos viñetas con iconos de diamante negro precediendo cada punto.

(slides 36)

## Glosario

- **NoSQL (Not Only SQL):** Acrónimo que Eric Evans reutilizó para un evento sobre bases de datos no relacionales, distribuidas y no conformes a las propiedades ACID propias de los sistemas relacionales.
- **SQL (Structured Query Language):** Lenguaje declarativo, rico en características, asociado al modelo relacional.
- **ACID (Atomicity, Consistency, Isolation, Durability):** Propiedades que aseguran que la base de datos se mantenga correcta, incluso si hay mucho tráfico.
- **Consistencia (Consistency):** Todos los nodos del sistema ven los mismos datos al mismo tiempo. Es decir, una lectura devuelve siempre la última escritura realizada.
- **Disponibilidad (Availability):** Cada solicitud recibe una respuesta, incluso si algunos nodos están caídos.
- **Tolerancia a particiones (Partitioning):** El sistema sigue funcionando incluso si hay fallos de comunicación entre nodos.
- **Vertical Scaling (Scaling up):** Escalado vertical mediante incremento de recursos como RAM, CPU e I/O en un solo servidor.
- **Horizontal Scaling (Scaling out):** Escalado horizontal mediante adición de múltiples servidores en fila.
