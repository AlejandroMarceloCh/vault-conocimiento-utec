---
curso: BIGDATA
titulo: 12 - Semana 10/Sem10_Base de Datos NoSQL
slides: 31
fuente: 12 - Semana 10/Sem10_Base de Datos NoSQL.pdf
---

## Slide 1

Portada. Título grande **"Base de datos NoSQL"**, subtítulo **Mg. Aldo Lezama Benavides**, etiqueta **"Semana 10"**. Fondo celeste degradado con foto del edificio de UTEC a la derecha y patrón de chevrones. Chrome decorativo (logo UTEC, "Reinventa el mundo").

## Slide 2

**Objetivo de la sesión**

- **Comprender** los fundamentos de las bases de datos NoSQL, su origen, propósito y diferencias clave frente a los sistemas relacionales tradicionales (SQL).
- **Identificar** los principales tipos de bases de datos NoSQL (documento, clave-valor, columna-familia y grafos), sus características, ventajas y limitaciones.
- **Reconocer** las aplicaciones prácticas de NoSQL en la nube (GCP), explorando ejemplos como Cassandra, MongoDB Atlas y Neo4j para distintos casos de uso empresariales.

Fondo celeste; los bullets van dentro de un marco de corchetes blancos (decorativo).

## Slide 3

**Contenido de la sesión**

Diagrama de tres columnas, cada una encerrada en corchetes blancos con numeral grande arriba:

- **01.** Base de Datos SQL
- **02.** Introducción a NoSQL
- **03.** Soluciones en GCP

## Slide 4

Divisor de sección. Numeral grande **"01."** entre corchetes, ícono de portapapeles y título **"Base de Datos SQL"**. Fondo celeste (decorativo).

## Slide 5

**Base de datos SQL**

- En 1970, el Dr. Edgar Codd presentó el modelo relacional de bases de datos en su histórico artículo "Un modelo relacional de datos para grandes bancos de datos compartidos". Este modelo proponía una forma eficiente de organizar y almacenar información en tablas estructuradas por filas y columnas.
- Cuatro años más tarde, en 1974, IBM desarrolló el Sistema R, el primer proyecto que implementó el modelo relacional, y creó SQL como lenguaje estándar para interactuar con este tipo de bases de datos.

Solo texto.

## Slide 6

**Base de datos SQL**

- Con el tiempo, se establecieron nuevos estándares para SQL, y compañías como Oracle, IBM y Microsoft desarrollaron sus propios sistemas de gestión de bases de datos relacionales (RDBMS), enfocados en ofrecer entornos más seguros, eficientes y fáciles de usar.
- Posteriormente, surgieron alternativas de código abierto, como MySQL, que democratizaron el acceso a SQL y a las bases de datos relacionales. Hoy en día, SQL es una tecnología ampliamente disponible tanto en infraestructuras locales como en plataformas en la nube como AWS, Azure y Google Cloud.

Solo texto.

## Slide 7

**Características de las bases de datos SQL**

Las bases de datos SQL se basan en el modelo relacional, que organiza la información en tablas estructuradas e interconectadas. Están conformadas principalmente por esquemas y tablas:

- **Esquema:** define la estructura general de la base de datos, especificando las tablas, sus campos, los tipos de datos, los valores permitidos y las relaciones entre ellas.
- **Tablas:** son las unidades fundamentales. Cada tabla representa una entidad (clientes, productos, transacciones) y se compone de filas (registros individuales) y columnas (atributos de esa entidad, como el nombre o el correo electrónico).

Solo texto.

## Slide 8

**Ventajas de SQL**

SQL proporciona un conjunto estándar de comandos para definir, consultar, actualizar y administrar datos en un RDBMS. Operaciones clave: **SELECT** (consulta), **INSERT** (adición de nuevos registros), **UPDATE** (modificación) y **DELETE** (eliminación).

Al usar estos comandos, SQL asegura que se mantienen las propiedades **ACID** (Atomicidad, Consistencia, Aislamiento y Durabilidad), lo que garantiza fiabilidad y coherencia de los cambios. Solo texto.

## Slide 9

**Características de las bases de datos SQL**

El modelo relacional garantiza integridad y coherencia mediante dos tipos de claves:

- **Claves primarias:** identifican de forma única cada registro.
- **Claves foráneas:** permiten establecer relaciones entre diferentes tablas.

Estas características hacen a las bases SQL ideales para manejar información estructurada de manera consistente, segura y organizada. Solo texto.

## Slide 10

**Propiedades ACID** — 1. Atomicidad

Garantiza que cada conjunto de cambios se trate como una unidad de trabajo única e indivisible: o se consigna toda la unidad, o no se consigna ninguna si falla alguna parte de la transacción.

*Ejemplo (transferencia bancaria):* María transfiere S/500 a Juan. Dos pasos: restar S/500 de la cuenta de María y sumar S/500 a la de Juan. Si ocurre un error entre los pasos (se resta pero no se acredita), la transacción se revierte completamente.

**Visual:** a la derecha, un recuadro cuadrado **naranja** con la letra grande **"A"** y el texto **"ATOMICITY"** (badge del acrónimo ACID).

## Slide 11

**Propiedades ACID** — 2. Consistencia

Garantiza que una transacción finaliza con la base de datos en un estado válido; debe satisfacer las restricciones de integridad antes y después.

*Ejemplo:* la suma total de saldos del banco debe mantenerse constante. Antes: María (S/1,000) + Juan (S/2,000) = S/3,000. Después: María (S/500) + Juan (S/2,500) = S/3,000. Si el dinero se "duplica" o "pierde", se viola la consistencia y se rechaza la transacción.

**Visual:** recuadro cuadrado **verde** con la letra **"C"** y el texto **"CONSISTENCY"** (badge ACID).

## Slide 12

**Propiedades ACID** — 3. Aislamiento

Garantiza que las transacciones simultáneas no provoquen incoherencias. Cada transacción parece ejecutarse de forma aislada, sin conocimiento de otras en ejecución, evitando interferencias.

*Ejemplo:* Usuario A consulta el saldo de Juan mientras Usuario B le transfiere dinero en ese mismo momento. El sistema garantiza que A vea el saldo final confirmado, no un valor intermedio mientras la transacción de B está incompleta.

**Visual:** recuadro cuadrado **gris azulado** con la letra **"I"** y el texto **"ISOLATION"** (badge ACID).

## Slide 13

**Propiedades ACID** — 4. Durabilidad

Garantiza que, una vez consignada una transacción, sus efectos persistan incluso ante fallos del sistema. Los cambios se almacenan permanentemente y sobreviven a caídas o cortes de energía.

*Ejemplo:* María transfiere S/500 a Juan y el sistema se apaga justo después de COMMIT. Al reiniciar, la base de datos recordará que la transacción fue completada. Esto se logra porque SQL registra cada transacción en el **log de transacciones**, guardado en disco antes de confirmarse.

Nota al pie (cursiva): estas propiedades garantizan sistemas fiables y coherentes incluso ante sucesos inesperados o fallos.

**Visual:** recuadro cuadrado **gris oscuro** con la letra **"D"** y el texto **"DURABILITY"** (badge ACID).

## Slide 14

**Sistemas comunes de bases de datos SQL**

Tres columnas con logo + descripción:

| Sistema (logo) | Descripción |
|---|---|
| **MySQL** (logo delfín) | RDBMS de código abierto, ahora propiedad de Oracle; conocido por velocidad, fiabilidad y facilidad de uso. Usado en entornos LAMP stack (Linux, Apache, MySQL, PHP/Python/Perl) para aplicaciones web pequeñas o medianas. |
| **PostgreSQL** (logo elefante azul) | Sistema objeto-relacional de código abierto con características avanzadas (funciones y procedimientos personalizados, consultas complejas, indexación, transacciones). Ideal para aplicaciones a gran escala, almacenamiento de datos y datos geoespaciales. |
| **Microsoft SQL Server** (logo cilindros + malla roja) | RDBMS propietario de Microsoft; parte de una suite con ediciones Express, Standard y Enterprise. Se integra bien en el ecosistema Microsoft; apto desde pequeñas empresas hasta grandes compañías. |

## Slide 15

Divisor de sección. Numeral grande **"02."** entre corchetes y título **"Introducción a las bases de Datos NoSQL"**. Fondo celeste (decorativo).

## Slide 16

**Introducción a las Bases de Datos NoSQL**

Las organizaciones generan grandes volúmenes de datos a velocidad sin precedentes, lo que desafía a los modelos tradicionales. Las bases de datos **NoSQL ("Not Only SQL")** emergen como alternativa a los modelos relacionales clásicos, ofreciendo flexibilidad, escalabilidad y adaptabilidad para datos variados y de alta velocidad. NoSQL no significa "sin SQL" sino "no solo SQL": una filosofía abierta a diversos modelos estructurales y lenguajes de consulta. Solo texto.

## Slide 17

**Motivaciones y Necesidades que Impulsan NoSQL**

El crecimiento de internet, las redes sociales y los sistemas distribuidos expuso limitaciones de los modelos relacionales:

- **Escalabilidad limitada verticalmente:** los RDBMS escalan incrementando la capacidad de un solo servidor (RAM, CPU), proceso costoso y finalmente limitado.
- **Esquemas rígidos:** requieren definir previamente la estructura; cualquier cambio impone migraciones costosas.
- **Baja tolerancia a datos no estructurados:** dificultad para manejar imágenes, videos, documentos, logs, sensores.
- **Transacciones y ACID imponen overhead:** asegurar atomicidad y consistencia penaliza el rendimiento y dificulta la escalabilidad.
- **Limitantes en alto rendimiento y baja latencia** en grandes volúmenes.

NoSQL surge para abordar necesidades más flexibles, eficientes y escalables ante Big Data, aplicaciones web/móviles, IoT y servicios que requieren adaptación rápida.

## Slide 18

**Ventajas de NoSQL**

Texto (izquierda): las bases NoSQL destacan en escalabilidad, flexibilidad y rendimiento con datos no estructurados. Ofrecen **escalabilidad horizontal y elasticidad**: escalan añadiendo más servidores a un sistema distribuido, adecuadas para cargas crecientes o impredecibles. Muchas proporcionan **fragmentación automática y equilibrio de carga**, distribuyendo datos entre nodos; los sistemas se amplían o reducen dinámicamente según demanda (elasticidad).

**Visual — diagrama radial:** en el centro un cilindro verde etiquetado **"NoSQL Database"** con flechas azules hacia cinco tarjetas (encabezado verde + ícono):

- **High Scalability** (ícono gráfico ascendente): "NoSQL databases can handle increasing demand by adding more servers to the infrastructure."
- **High Availability** (ícono engranaje con check): "They can run continuously without interruption of service."
- **Efficient Big Data Management** (ícono nube/servidor): "Storage capacity of large amount of unstructured data make them good fits for Big data."
- **Partition Tolerance** (ícono servidores): "They continue to operate even in case of unavailable network connection between nodes."
- **Fast Development** (ícono cohete): "They are adapted to the fast changing agile environment which need constant feedbacks and fast iterations."

## Slide 19

**Ventajas de NoSQL** (continuación)

Texto (izquierda): también proporcionan **flexibilidad de esquema** mediante esquemas dinámicos: los campos de un registro pueden variar entre distintos documentos, dando cabida a estructuras diversas y cambiantes de las aplicaciones modernas. Funcionan bien con datos no estructurados y semiestructurados (JSON, XML); los datos suelen ser impredecibles, sobre todo los generados por usuarios, y NoSQL gestiona bien su almacenamiento.

**Visual:** el mismo diagrama radial de la Slide 18 (cilindro verde "NoSQL Database" rodeado de las cinco tarjetas: High Scalability, High Availability, Efficient Big Data Management, Partition Tolerance, Fast Development).

## Slide 20

**Tipos de bases de datos NoSQL** — Almacenes de documentos

**Visual:** logo de **MongoDB** (hoja verde) a la izquierda.

Descripción: usa una estructura flexible, similar a JSON, para almacenar datos como documentos. Útiles para datos complejos y jerárquicos; admiten esquemas dinámicos. Usados en gestión de contenidos, comercio electrónico y aplicaciones en tiempo real.

**Ventajas:**
- **Sin esquema:** no hay limitaciones de formato ni estructura de almacenamiento; beneficioso cuando la base se transforma continuamente.
- **Fácil de actualizar:** se agrega o elimina información nueva sin cambiar el resto de los campos existentes del documento.
- **Rendimiento mejorado:** toda la información está en el mismo documento; no hay que consultar información externa (a diferencia del relacional, que podría requerir otras tablas).

**Limitaciones:**
- **Problemas de comprobación de coherencia:** los documentos no necesariamente tienen relación entre sí y dos documentos pueden tener campos diferentes.
- **Problemas de atomicidad:** cambiar dos colecciones requiere ejecutar una consulta separada para cada documento.

## Slide 21

**Tipos de bases de datos NoSQL** — Base de datos clave-valor

**Visual:** logos de **redis** (rojo) y **DynamoDB** (azul, AWS) a la izquierda.

Descripción: la forma más sencilla de NoSQL; cada unidad de datos se almacena como un par clave-valor. Eficaces cuando se necesita acceder rápidamente a muchos datos con tiempos de respuesta rápidos.

**Ventajas:**
- **Simplicidad:** la estructura clave-valor es sencilla; la ausencia de tipo de dato facilita su uso.
- **Velocidad:** el formato simple hace más rápidas las operaciones de lectura y escritura.

**Limitaciones:**
- No pueden filtrar en la columna de valor porque el valor devuelto es toda la información almacenada en el campo.
- Se optimiza solo con una única clave y valor; almacenar varios valores requeriría un analizador.
- El valor se actualiza solo en su conjunto: obtener datos completos, procesarlos y almacenarlos; puede generar problemas de rendimiento si el procesamiento es largo.

## Slide 22

**Tipos de bases de datos NoSQL** — Base de datos gráfica

**Visual:** logo de **neo4j** (con nodos azules) a la izquierda.

Descripción: representan relaciones entre entidades de datos. Más útiles cuando las relaciones son importantes, como redes sociales o sistemas de recomendación.

**Ventajas:**
- Son una estructura ágil y flexible.
- La relación entre los nodos es legible y explícita, fácil de entender.

**Limitaciones:**
- No existe un lenguaje de consulta estandarizado; cada lenguaje depende de la plataforma.
- Por lo anterior, es difícil encontrar ayuda en línea al enfrentar un problema.

## Slide 23

**Comparativa entre Bases de Datos SQL y NoSQL**

**Visual — tabla:**

| Característica | Bases de datos SQL | Bases de datos NoSQL |
|---|---|---|
| Modelo de datos | Tablas, filas, columnas | Documentos, clave-valor, grafos, columnas |
| Esquema | Fijo y riguroso | Flexible y opcional |
| Escalabilidad | Vertical (mejor hardware) | Horizontal (más servidores) |
| Relacionamiento | JOINs, claves foráneas | Embedding, referencias manuales |
| Transacciones y consistencia | ACID | BASE / eventual (a menudo) |
| Lenguaje de consulta | SQL | Varía según sistema (JSON, APIs, CQL, Cypher, etc.) |
| Casos de uso | Datos estructurados, relaciones complejas | Volumen, alta velocidad, flexibilidad, datos variados |
| Soporte y madurez | Muy alto, estandarizado | Variable, en crecimiento |

## Slide 24

**Cuándo se debe usar bases de datos NoSQL**

Las industrias necesitan recopilar la mayor cantidad de datos posible; almacenarlos en la infraestructura adecuada es otro desafío, pues los datos pueden ser de distintos tipos (imágenes, videos, texto, sonido) y las bases relacionales no siempre son la mejor opción.

Se debería considerar NoSQL en estos escenarios:

- **Cambio constante de datos:** cuando no sabes cómo crecerá tu sistema/aplicaciones y podrías agregar nuevos tipos de datos o funciones.
- **Una gran cantidad de datos:** cuando la empresa trabaja con grandes volúmenes que pueden crecer con el tiempo.
- **Falta de consistencia:** cuando la consistencia y la integridad total no son prioridad (p. ej. una red social interna donde no importa que todos vean las publicaciones a la vez).
- **Escalabilidad y costo:** NoSQL permite mayor flexibilidad y controlar costos a medida que cambian las necesidades de datos.

Solo texto.

## Slide 25

**Tipos de bases de datos NoSQL** — Base de datos columna-familia

**Visual:** logos de **cassandra** (ojo estilizado) y **Apache HBASE** (orca) a la izquierda.

Descripción: representan los datos en columnas en lugar de filas. Mejores para sistemas distribuidos a gran escala y sistemas que leen y escriben a menudo, como aplicaciones de series temporales e IoT.

**Ventajas:**
- Alto rendimiento en lecturas y escrituras masivas distribuidas.
- Escalabilidad horizontal, agregando nodos fácilmente.
- Esquema flexible, cada fila puede tener distintas columnas.
- Alta disponibilidad gracias a la replicación entre nodos.
- Eficientes para series temporales y grandes volúmenes de datos.
- Soportan consultas rápidas por clave-partición.

**Limitaciones:**
- Modelado complejo, requiere diseño cuidadoso de claves.
- No garantizan transacciones ACID completas.
- Usan lenguajes propios (como CQL), no SQL estándar.
- Mayor curva de aprendizaje y administración técnica.
- Mantenimiento complejo en clústeres distribuidos.
- No aptas para consultas ad hoc o relaciones complejas.
- Limitadas para sistemas financieros o críticos.

## Slide 26

Divisor de sección. Numeral grande **"03."** entre corchetes, ícono de portapapeles y título **"Soluciones en GCP MarketPlace"**. Fondo celeste (decorativo).

## Slide 27

**MongoDB Atlas**

**Visual — captura de Google Cloud Marketplace:** cabecera "Google Cloud · Proyecto BigData-UTEC2026", vista "Detalles del producto" del ítem **"MongoDB Atlas (pago por uso)"** de MongoDB Inc. Texto "Empieza gratis con Atlas...", badge verde "Prueba de 14 días disponible", botones **Suscribirse** y **Comunicarse con Ventas**. Pestañas: Descripción general / Precios / Documentación / Asistencia / Productos relacionados. Sección "Descripción general" y panel "Detalles adicionales" (Tipo: SaaS y API; Última actualización 26/8/25; Categoría: Big data, Analytics, Databases, Firebase).

Texto (derecha): MongoDB Atlas es la plataforma en la nube oficial y totalmente administrada de MongoDB, para crear, desplegar y escalar bases MongoDB sin gestionar infraestructura.

**¿Qué es MongoDB Atlas?** Es un servicio **Database-as-a-Service (DBaaS)** de MongoDB Inc. Permite ejecutar MongoDB en la nube (sin instalar ni administrar servidores) en cualquiera de los principales proveedores:
- Google Cloud Platform (GCP)
- Amazon Web Services (AWS)
- Microsoft Azure

Puedes elegir dónde alojar la base; Atlas se encarga de mantenimiento, seguridad, actualizaciones y copias de seguridad.

## Slide 28

**Apache Cassandra**

**Visual — captura de GCP Marketplace:** "Detalles del producto" del ítem **"Casandra"** (logo ojo cassandra), "Hacer clic para implementar de Google", descripción "Base de datos NoSQL con replicación sin maestro para alta disponibilidad", botones **Comenzar** y **Ver implementaciones**. Sección "Descripción general" + "Acerca de Google Click to Deploy". Panel "Detalles adicionales": Se ejecuta en Google Compute Engine; Tipo Virtual machines, VM múltiples; Arquitectura X86_64; Última actualización 27/8/25; Categoría Databases; Versión latest.

Texto (derecha):
**¿Qué es Apache Cassandra?** Base de datos NoSQL distribuida y altamente escalable, para manejar grandes volúmenes de datos en muchos servidores sin un único punto de falla. Ideal cuando se necesita alta disponibilidad, baja latencia y tolerancia a fallos.

**En resumen:**
- Modelo de datos: clave-valor / columna ancha.
- Arquitectura: sin maestro (peer-to-peer).
- Escalabilidad: horizontal, agregando nodos.
- Lenguaje de consulta: CQL (Cassandra Query Language), similar a SQL.

**Se usa mucho en:**
- Telecomunicaciones (registros de llamadas).
- IoT (sensores y datos de tiempo real).
- Analítica de grandes volúmenes (logs, clics, telemetría).

## Slide 29

**Neo4j**

**Visual — captura de GCP Marketplace:** cabecera "Google Cloud · Proyecto BigData-UTEC2026", "Detalles del producto" del ítem **"Edición empresarial de Neo4j"** (logo neo4j), "La plataforma líder de datos gráficos para datos conectados", botones **Comenzar** / **Ver implementaciones** / **Comunicarse con Ventas**. Sección "Descripción general" (Neo4j es una base gráfica nativa compatible con ACID; acceso mediante protocolo Bolt y lenguaje Cypher, o shell visual) + "Acerca de BYOL". Panel "Detalles adicionales": Google Compute Engine; Virtual machines, VM múltiples, BYOL; X86_64; Última actualización 23/9/25; Categoría Analítica, Big data, Bases de datos, Aprendizaje automático; Versión latest.

Texto (derecha):
**¿Qué es Neo4j?** Base de datos NoSQL orientada a grafos, diseñada para almacenar y analizar relaciones entre datos de manera eficiente. A diferencia de las relacionales (SQL) o de documentos (MongoDB), Neo4j modela los datos como **nodos (entidades)** y **relaciones (conexiones)**, lo que permite consultas muy rápidas sobre redes complejas.

## Slide 30

**Conclusiones**

Tres puntos numerados (01/02/03, cada uno en corchetes):

1. Las bases de datos NoSQL surgieron como respuesta a las limitaciones de escalabilidad y flexibilidad de los sistemas relacionales, ofreciendo soluciones más adecuadas para entornos de Big Data y alta disponibilidad.
2. Cada tipo de base de datos NoSQL responde a necesidades específicas de modelado y rendimiento, por lo que la elección depende del tipo de datos, las relaciones y la carga de trabajo.
3. Las soluciones NoSQL en la nube, como Cassandra, MongoDB Atlas y Neo4j, permiten implementar arquitecturas distribuidas, elásticas y seguras, integradas con servicios analíticos modernos en plataformas como Google Cloud Platform (GCP).

## Slide 31

Cierre. Logo grande de **UTEC — Universidad de Ingeniería y Tecnología** centrado sobre fondo celeste (decorativa).
