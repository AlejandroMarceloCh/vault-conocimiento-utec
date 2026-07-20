---
curso: BD2
titulo: 15 BD No SQL 3
slides: 35
fuente: 15 BD No SQL 3.pdf
---

# 15 BD No SQL 3

## Índice

- [BD de Columna Ancha](#bd-de-columna-ancha)
  - [Características](#características)
  - [Agregar registro con nueva columna](#agregar-registro-con-nueva-columna)
  - [Nombre «columna ancha» y familia de columnas](#nombre-columna-ancha-y-familia-de-columnas)
  - [Productos](#productos)
  - [Casos de uso](#casos-de-uso)
  - [Apache Cassandra](#apache-cassandra)
  - [Apache Cassandra: modelo de datos](#apache-cassandra-modelo-de-datos)
  - [Apache Cassandra: Keyspace y Cluster](#apache-cassandra-keyspace-y-cluster)
  - [Apache Cassandra: fragmentación horizontal](#apache-cassandra-fragmentación-horizontal)
  - [Apache Cassandra: Partition Key y Clustering Key](#apache-cassandra-partition-key-y-clustering-key)
  - [Apache Cassandra: ejemplo de fragmentación con sensor_data](#apache-cassandra-ejemplo-de-fragmentación-con-sensor_data)
  - [Ejemplo: detección de fraude en pagos](#ejemplo-detección-de-fraude-en-pagos)
- [BD Clave-Valor](#bd-clave-valor)
  - [Características](#características-1)
  - [Casos de uso](#casos-de-uso-1)
  - [Productos](#productos-1)
  - [Redis: características](#redis-características)
  - [Redis: uso clásico](#redis-uso-clásico)
  - [Redis: persistencia](#redis-persistencia)
  - [Redis: escalabilidad](#redis-escalabilidad)
  - [Redis Enterprise](#redis-enterprise)
  - [Redis: configuración](#redis-configuración)
  - [Redis: operaciones CRUD](#redis-operaciones-crud)
  - [Redis: TTL](#redis-ttl)
  - [Redis: ejemplo caché de respuestas de API](#redis-ejemplo-caché-de-respuestas-de-api)
  - [Redis: ejemplo caché de autenticación de usuarios](#redis-ejemplo-caché-de-autenticación-de-usuarios)
  - [Redis: comandos básicos](#redis-comandos-básicos)
  - [Redis: comandos de listas](#redis-comandos-de-listas)
  - [Redis: comandos de hashes](#redis-comandos-de-hashes)
  - [Redis: comandos de conjuntos](#redis-comandos-de-conjuntos)
  - [Redis: comandos de sorted sets](#redis-comandos-de-sorted-sets)
- [Glosario](#glosario)

## BD de Columna Ancha

### Características

Características:

- Inspirado en el modelo BigTable de Google.
- Datos organizados en columnas en lugar de filas tradicionales.
  - Esquema flexible, permite que determinadas columnas solo se apliquen a determinados registros.
  - Las filas se identifican por una clave primaria, que puede ser simple o compuesta.
- Escalamiento horizontal y procesamiento distribuido para Big Data.
- Alta disponibilidad: Datos replicados automáticamente entre nodos.

**Figura:** Dos diagramas a la derecha del texto. **Diagrama superior — «Table with single-row partitions»:** tabla con columnas `performer` (etiquetada como *partition key*), `born`, `country`, `died`, `founded`, `style` y `type`. Tres filas (particiones): **John Lennon** — born: 1940, country: England, died: 1980, style: Rock, type: artist (celda `founded` vacía); **Paul McCartney** — born: 1942, country: England, style: Rock, type: artist (celdas `died` y `founded` vacías); **The Beatles** — country: England, founded: 1957, style: Rock, type: band (celdas `born` y `died` vacías). Flechas y etiquetas señalan «columns», «partitions», «rows» y «cells». **Diagrama inferior — «Column family view»:** cada clave de fila (John Lennon, Paul McCartney, The Beatles) a la izquierda con flechas hacia celdas individuales nombre-valor solo para los atributos presentes en ese registro (por ejemplo, John Lennon tiene born, country, died, style, type pero no founded; The Beatles tiene country, founded, style, type pero no born ni died). Ilustra el esquema flexible donde cada fila almacena únicamente las columnas relevantes.

(slide 3)

### Agregar registro con nueva columna

Agregar Registro con Nueva Columna

- En una BD Relacional agregar una nueva columna implica completar con valores nulos las demás filas.
- En una BD de Columna Ancha, se agrega elementos a la nueva columna sin afectar los datos existentes.

**Figura:** Mismos dos diagramas de la slide anterior a la derecha. **Diagrama superior — «Table with single-row partitions»:** tabla con columnas `performer` (*partition key*), `born`, `country`, `died`, `founded`, `style`, `type`; tres filas con datos de John Lennon, Paul McCartney y The Beatles; celdas vacías donde no aplica el atributo. Etiquetas señalan «partitions», «columns» y «cells». **Diagrama inferior — «Column family view»:** cada performer como bloque con pares clave-valor solo para sus atributos existentes (John Lennon: born 1940, country England, died 1980, style Rock, type artist; Paul McCartney: born 1942, country England, style Rock, type artist; The Beatles: country England, founded 1957, style Rock, type band). Sin entradas para columnas inexistentes en cada fila, contrastando con la necesidad de valores nulos en BD relacional.

(slide 4)

### Nombre «columna ancha» y familia de columnas

¿Por qué se llama BD de Columna Ancha?

- Cada fila puede contener un número muy grande de columnas.

¿Qué es una Familia de Columnas (Column Family)?

- Es una agrupación de columnas que comparten una misma clave de fila.
- En BigTable y Hbase, Column Family es un grupo lógico explicito de columnas dentro de la tabla.
- En Cassandra, Column Family es equivalente a una tabla.

**Figura:** Dos diagramas a la derecha. **Diagrama superior — «Google Bigtable Column-family data storage»** (fuente: scaleyourapp.com): **Row Key** `com.google.maps/index.html` apunta a dos column families. **column family: content** — tres versiones temporales: `content:cont__t1`, `content:cont__t2`, `content:cont__t3`, cada una con fragmento HTML y timestamp distinto. **column family: anchors** — dos entradas: `anchor:wiki__t1` (referencia wiki.com, tiempo t1) y `anchor:scp__t1` (referencia scaleyourapp.com, tiempo t1). **Diagrama inferior — representación abstracta de tabla wide-column:** columna de claves de fila con valores `a`, `b`, `bb`, `c`. Cada fila tiene un conjunto distinto de columnas: fila `a` — `colA:value1`, `colFoo:a value`, `fram:zilk`; fila `b` — `colA:value1`, `colB:a value`, icono de pieza de ajedrez `:chesspiece`; fila `bb` — `colA:value1`, `colB:`, `colFoo:a value`, icono de nota musical; fila `c` — `colA` (símbolo de paz), `colBaz:anything`, `colFoo:a value`. Muestra que las filas no comparten el mismo conjunto de columnas.

(slide 5)

### Productos

| Base de Datos | Año de Creación | Empresa que la Soporta | Características Clave | Casos de Uso |
|---|---|---|---|---|
| Google Bigtable | 2005 | Google | Análisis en tiempo real, almacenamiento masivo, IoT. | Análisis predictivo, personalización, servicios IoT. |
| Apache Cassandra | 2008 | Apache Software Foundation | Escalabilidad horizontal, alta disponibilidad, Big Data. | Monitoreo en tiempo real, IoT, aplicaciones financieras. |
| HBase | 2008 | Apache Software Foundation | Integración con Hadoop, consistencia fuerte, Big Data. | Almacenamiento para análisis de datos, log de eventos. |
| ScyllaDB | 2015 | ScyllaDB Inc. | Compatibilidad con Cassandra, baja latencia, alto rendimiento. | Aplicaciones de baja latencia, sistemas de recomendación. |

**Figura:** Slide con título «BD de Columna Ancha: Productos» y tabla comparativa de cuatro productos wide-column. Triángulo decorativo azul en esquina superior izquierda.

(slide 6)

### Casos de uso

Casos de Uso:

- Análisis en tiempo real: Procesamiento rápido de grandes volúmenes de datos.
- Aplicaciones IoT: Gestión de datos de sensores y dispositivos conectados.
- Sistemas de mensajería: Soporte para chats y redes sociales.
- Big Data distribuido: Consultas paralelas para análisis de datos.

**Figura:** Tres conjuntos de iconos a la derecha. **Icono superior:** gráfico de barras, gráfico de líneas y reloj azul, representando análisis en tiempo real. **Icono central:** figura de persona junto a iconos de media (botón play), documentos y engranaje; **Icono inferior:** cinco cilindros de base de datos conectados en patrón hub-and-spoke, simbolizando sistema distribuido.

(slide 7)

### Apache Cassandra

- Inicialmente desarrollado por Facebook
- En Cassandra, los datos se organizan en tablas dentro de keyspaces.
- Utiliza CQL como lenguaje de consulta para interactuar con los Keyspaces.
- Características clave:
  - Alta disponibilidad: Diseñada para garantizar que los datos estén accesibles incluso si fallan algunos nodos (replicación).
  - Escalabilidad horizontal: Puede añadir nodos al clúster fácilmente para manejar más datos y tráfico (utiliza P2P).

Avinash Lakshman and Prashant Malik. 2010. Cassandra: a decentralized structured storage system. SIGOPS Oper. Syst. Rev. 44, 2 (April 2010)

**Figura:** iris azul con patrón de red blanca; debajo la palabra «cassandra» en minúsculas. A la derecha, viñetas con las características. Cita académica en la parte inferior izquierda.

(slide 8)

### Apache Cassandra: modelo de datos

MODELO DE DATOS

- Columna: Un par nombre/valor.
- Fila: Un contenedor de columnas identificado por una clave primaria.
- Tabla: Un contenedor de filas que están organizadas por particiones.
- Partición: Una colección de filas relacionadas que se almacenan juntas en los mismos nodos.

Cassandra representa las filas internamente como:

`Map<RowKey, SortedMap<ColumnKey, ColumnValue>>`

**Figura:** Diagrama a la derecha titulado «Column Family (Table)». **Row Key 1** apunta a tres columnas: Column 1 → Value 1, Column 2 → Value 2, Column 3 → Value 3. **Row Key 2** apunta a dos columnas: Column 1 → Value 1, Column 4 → Value 4. Demuestra que filas en la misma tabla pueden tener columnas distintas. Recuadro azul oscuro en la parte inferior derecha con la representación interna `Map<RowKey, SortedMap<ColumnKey, ColumnValue>>`. La definición de «Partición» resaltada en azul claro en el texto.

(slide 9)

### Apache Cassandra: Keyspace y Cluster

MODELO DE DATOS

Keyspace

Es un contenedor de tablas (Column Family)

Cluster

Es un contenedor de Keyspaces que abarca uno o más nodos

```sql
CREATE KEYSPACE mi_keyspace WITH
replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 3
};
```

**Figura:** Diagrama jerárquico anidado a la derecha. Contenedor exterior «Cassandra Cluster»; dentro, caja «Node 1..n»; dentro del nodo, múltiples contenedores «Keyspace 1» a «Keyspace n»; dentro de cada Keyspace, cajas rosadas «Column Family 1» a «Column Family n»; dentro de cada Column Family, rectángulos morados redondeados «Row 1» a «Row n». Bloque de código CQL en la parte inferior izquierda para crear un keyspace con replicación SimpleStrategy y factor 3.

(slide 10)

### Apache Cassandra: fragmentación horizontal

Fragmentación Horizontal

**Figura:** **Tabla de datos (derecha):** columnas COUNTRY, CITY, POPULATION. Bracket azul bajo COUNTRY etiquetado «Partition Key». Filas: USA — New York (8M), Los Angeles (4M); FR — Paris (2.23M), Toulouse (1.1M); DE — Berlin (3.35M), Nuremberg (0.5M); UK — London (9.2M); AU — Sydney (4.9M); CA — Toronto (6.2M), Montreal (4.2M); JP — Tokyo (37.43M); IN — Mumbai (20.2M). **Diagrama central — clúster Cassandra:** anillo de 7 nodos circulares verdes con logo de Cassandra (ojo) en el centro. Flecha azul desde la tabla hacia el anillo. Datos distribuidos por nodo según Partition Key (COUNTRY): nodo superior — USA; superior-derecha — FR; superior-izquierda — DE; medio-izquierda — UK; inferior-medio-derecha — CA; inferior-derecha — JP; inferior-medio-izquierda — AU e IN. Ilustra fragmentación horizontal por clave de partición.

(slide 11)

### Apache Cassandra: Partition Key y Clustering Key

Fragmentación Horizontal

Primary Key = Partition Key + Clustering Key

```sql
CREATE TABLE sensor_data
(
    Sensor int,
    Date date,
    Timestamp timestamp,
    Speed float,
    Torque float,
    Power float,
    PRIMARY KEY ((Sensor, Date), Timestamp)
) WITH CLUSTERING ORDER BY (Timestamp ASC);
```

Como los datos están distribuidos a través de los nodos — **Partition Key:** `(Sensor, Date)` (resaltado en amarillo).

Como los datos están almacenados en un nodo — **Clustering Key:** `Timestamp` (resaltado en azul claro).

**Figura:** Bloque de código CQL a la izquierda con la definición de tabla `sensor_data`. A la derecha, ecuación «Primary Key = Partition Key + Clustering Key». En el código, `(Sensor, Date)` resaltado en amarillo con recuadro amarillo explicativo «Como los datos están distribuidos a través de los nodos»; `Timestamp` resaltado en azul claro con recuadro azul «Como los datos están almacenados en un nodo».

(slide 12)

### Apache Cassandra: ejemplo de fragmentación con sensor_data

Fragmentación Horizontal

| Sensor # | Date | Timestamp | Speed | Torque | Power |
|---|---|---|---|---|---|
| 1 | 2015-01-01 | … | … | … | … |
| 1 | 2015-01-02 | … | … | … | … |
| 2 | 2015-01-02 | … | … | … | … |

Primary Key = Partition Key + Clustering Key

- **Partition Key:** Sensor #, Date
- **Clustering Key:** Timestamp
- **Primary Key:** `((Sensor, Date), Timestamp)`

```sql
CREATE TABLE sensor_data
(
    Sensor int,
    Date date,
    Timestamp timestamp,
    Speed float,
    Torque float,
    Power float,
    PRIMARY KEY ((Sensor, Date), Timestamp)
) WITH CLUSTERING ORDER BY (Timestamp ASC);
```

**Figura:** Diagrama de distribución de datos. **Node 1** (cilindro): bloque con Sensor # = 1, Date = 2015-01-01 y sus filas de datos (Timestamp, Speed, Torque, Power). **Node 2** (cilindro): dos bloques — Sensor # = 1, Date = 2015-01-02 y Sensor # = 2, Date = 2015-01-02. Brackets bajo la tabla señalan Partition Key (Sensor # + Date) y Clustering Key (Timestamp). Bloque de código CQL en recuadro azul inferior izquierdo; `PRIMARY KEY ((Sensor, Date), Timestamp)` y `Timestamp ASC` resaltados en amarillo.

(slide 13)

### Ejemplo: detección de fraude en pagos

Detección de fraude en pagos

Un sistema de pagos en línea quiere detectar transacciones sospechosas en tiempo real.

- Clave de partición: ID del usuario
- Clave de clustering: Fecha de la transacción.
- Beneficios: Se pueden construir sistemas de alerta en tiempo real altamente escalables para consultas por rango.

```sql
CREATE TABLE transacciones (
    id_usuario UUID,
    timestamp timestamp,
    monto decimal,
    ubicacion text,
    metodo_pago text,
    PRIMARY KEY (id_usuario, timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);

-- Insertar transacción sospechosa (monto elevado):
INSERT INTO transacciones (id_usuario, timestamp, monto, ubicacion, metodo_pago)
VALUES (uuid(), toTimestamp(now()), 5000.00, 'New York', 'Tarjeta de Crédito');

-- Consultar transacciones en las últimas 24 horas
SELECT * FROM transacciones WHERE id_usuario = <UUID>
AND timestamp >= <TIMESTAMP_HACE_24_HORAS>;
```

- Las transacciones de cada usuario se almacenan en la misma partición.
- Dentro de esa partición, están ordenadas por timestamp descendente (útil para ver primero las más recientes).

**Figura:** Lado izquierdo, contexto del caso de uso de detección de fraude con claves de partición y clustering. Lado derecho, bloque de código CQL con CREATE TABLE, INSERT de transacción sospechosa ($5000.00, New York, Tarjeta de Crédito) y SELECT por rango de 24 horas. Recuadro azul inferior derecho con los dos puntos sobre almacenamiento por partición y orden descendente por timestamp.

(slide 14)

## BD Clave-Valor

### Características

Características:

- Ideal para operaciones CRUD básicas
- No está diseñado para consultas complejas
- Los datos se organizan en una colección de pares clave-valor.
  - La clave debe ser única.
- Los valores pueden ser números enteros, cadenas o tipos de datos más complejos, como un documento JSON.
- Los datos se obtienen mediante una coincidencia exacta con la clave.

**Figura:** Diagrama a la derecha con dos columnas «Key» y «Value», flechas desde cada clave hacia su valor: `User1:Position` → `"Striker"`; `User1:Name` → `"Sami"`; `User1:Team` → `{33,12,65,99}`; `User2:Salary` → `45000`. Ilustra pares clave-valor con tipos de datos variados (cadena, entero, conjunto). Triángulo decorativo azul en esquina superior izquierda.

(slide 16)

### Casos de uso

Casos de Uso:

- Operaciones CRUD básicas rápidas en datos no interconectados
- Almacenamiento de perfiles y preferencias de usuario en la aplicación
- Almacenamiento de sesiones de usuario
- Almacenamiento de datos del carrito de compras para tiendas en línea.
- Aplicaciones basadas en la ubicación (datos geoespaciales)

**Figura:** Tres iconos alineados verticalmente a la derecha: icono de documento de identificación (perfiles de usuario); pantalla de laptop con icono de login de usuario (sesiones); carrito de compras rojo (e-commerce).

(slide 17)

### Productos

| Base de Datos | Año de Creación | Empresa | Almacenamiento | Persistencia | Escalabilidad | Casos de Uso |
|---|---|---|---|---|---|---|
| Redis | 2009 | Redis Inc. | En memoria | Opcional (snapshot y AOF) | Alta (Cluster y Sentinel) | Caché, sesiones, colas de mensajes |
| DynamoDB | 2012 | Amazon Web Services (AWS) | SSD (gestionado) | Sí (gestionado por AWS) | Muy alta (serverless) | Aplicaciones web y móviles, IoT, gaming |
| Memcached | 2003 | Open Source | En memoria | No | Alta (sharding) | Caché distribuido, aceleración de bases de datos |
| Riak KV | 2009 | Open Source | Disco y memoria | Sí | Alta (replicación automática) | Aplicaciones distribuidas, big data |
| Berkeley DB | 1991/2006 | Oracle Corporation | Disco y memoria | Sí | Baja (embebida) | Aplicaciones móviles, dispositivos embebidos |

**Figura:** Slide con título «BD Clave-Valor: Productos» y tabla comparativa de cinco productos key-value con siete columnas. Encabezado de tabla en azul.

(slide 18)

### Redis: características

- Redis sigue un modelo clave-valor en memoria, lo que le permite ofrecer una latencia extremadamente baja.
- Puede configurarse en modo standalone, modo sentinel (replication) o en modo cluster (sharding).
- Características clave:
  - ✓ Master-Slave Replication para alta disponibilidad
  - ✓ Cluster Mode para escalabilidad horizontal
  - ✓ Persistence (AOF y RDB) para almacenamiento en disco

Redis Explained - by Mahdi Yusuf

**Figura:** Viñetas con características a la derecha. Enlace «Redis Explained - by Mahdi Yusuf» en la parte inferior central. Acentos triangulares azules en esquinas superior izquierda e inferior derecha.

(slide 19)

### Redis: uso clásico

Uso clásico de REDIS

**Figura:** Diagrama de arquitectura cache-aside con tres componentes principales conectados por flechas numeradas. **Client** (iconos de smartphone y laptop) se conecta a **Application Logic** (cubo wireframe 3D). **Paso 1 — Look in cache:** la aplicación consulta Redis; si hay *cache hit*, retorna los datos directamente. **Paso 2 — Cache miss > look in persistent datastore:** si no está en caché, la aplicación consulta la SQL Database. **Paso 3 — Prime cache with data:** los datos obtenidos de la BD se escriben en Redis para futuras consultas. Recuadro con ejemplo de datos key-value: `User1:Position` → `"Striker"`, `User1:Name` → `"Sami"`, `User1:Team` → `{33, 12, 65, 99}`, `User2:Salary` → `45000`. Flecha naranja desde el recuadro hacia el icono de Redis.

(slide 20)

### Redis: persistencia

**Snapshot (RDB):** copias puntuales del dataset en intervalos configurables.

**Append Only File (AOF):** registra cada operación de escritura en un archivo de log. El archivo AOF puede crecer mucho.

### Modo híbrido: RDB + AOF

Combina rendimiento (RDB) y durabilidad (AOF).

- Al iniciar Redis, primero se carga el último RDB para restaurar el estado completo más reciente.
- Luego, se reproduce el archivo AOF para aplicar los cambios más recientes y llegar al estado actual.

**Figura:** Slide dividida en tres secciones. Arriba a la izquierda, bloque «Snapshot (RDB)» con un icono de almacén de datos rojo que apunta con una flecha etiquetada «snapshot» hacia un cilindro etiquetado «persistent snapshot (rdb)». Arriba a la derecha, bloque «Append Only File (AOF)» con el mismo icono de almacén de datos rojo que apunta con una flecha etiquetada «append only file» (con secuencia 1, 2, 3, 4… n) hacia una barra horizontal segmentada etiquetada «persisted (aof)». Abajo, bloque «Modo híbrido: RDB + AOF» con diagrama que muestra el almacén de datos alimentando tanto el cilindro RDB como la barra AOF, ambos convergiendo en un archivo combinado «RDB + AOF». La sección RDB (mitad superior, fondo verde) muestra un snapshot del estado actual: `name -> "Alice"`, `counter -> 0`, `tasks -> ["task1", "task2"]`, `fruits -> ["apple", "banana", "orange"]`. `set name "Bob"`, 2. `incr counter`, 3. `LPOP tasks`, 4. `RPOP tasks`, 5. `SREM fruits "apple"`, 6. `SREM fruits "orange"`.

(slide 21)

### Redis: escalabilidad

Redis Standalone

Redis Cluster

Redis Sentinel

Different Types of Redis Architecture | Medium

**Figura:** Slide con tres diagramas de arquitectura Redis. Arriba a la izquierda, «Redis Standalone»: tres cajas rojas etiquetadas «API» en la parte superior con flechas que apuntan hacia abajo a una única instancia Redis (icono de base de datos roja), sin redundancia ni escalado horizontal. Abajo a la izquierda, «Redis Sentinel»: tres cajas «API» conectadas a una instancia Redis etiquetada «Master»; debajo del Master, dos instancias Redis etiquetadas «Slave» con flechas del Master hacia cada Slave indicando replicación de datos. A la derecha, «Redis Cluster»: tres cajas «API» con flechas hacia tres instancias «Master» en fila media; flechas bidireccionales horizontales conectan los tres Masters entre sí (comunicación inter-nodo); debajo de cada Master hay una instancia «Slave» correspondiente con flecha descendente del Master al Slave (cada shard tiene respaldo). Enlace de fuente al pie: «Different Types of Redis Architecture | Medium».

(slide 22)

### Redis Enterprise

- Shard automático.
- Rebalanceo sin interrupciones.
- Rendimiento extremo.

Redis Cluster Architecture | Redis Enterprise

**Figura:** Slide con subtítulo «Redis Enterprise». A la izquierda, tres viñetas: «Shard automático», «Rebalanceo sin interrupciones», «Rendimiento extremo». En el centro, cuatro diagramas de configuración de despliegue con iconos de nodos de base de datos rojos: (1) «Simple Database»: un solo nodo etiquetado «Primary». (2) «HA Database»: dos nodos, «Primary» con flecha hacia «Replica» indicando replicación para alta disponibilidad. (3) «Clustered Database»: pila vertical de nodos primarios «P1», «P2», «Pn» representando escalado horizontal por sharding. (4) «HA Clustered Database»: dos columnas, izquierda con primarios «P1», «P2», «Pn» y derecha con réplicas «R1», «R2», «Rn»; flechas horizontales de cada primario a su réplica correspondiente (P1→R1, P2→R2, Pn→Rn). Enlace al pie: «Redis Cluster Architecture | Redis Enterprise».

(slide 23)

### Redis: configuración

- Instalación de REDIS con Docker

```bash
docker pull redis/redis-stack-server:latest
```

- Levantar el contenedor

```bash
docker run -d --name redis -p 6379:6379 redis/redis-stack-server:latest
```

- Conexión con DBeaverEE

### Opciones Online

- https://aws.amazon.com/es/elasticache/
- https://cloud.redis.io/#/databases

**Figura:** Slide con comandos Docker a la izquierda y captura de pantalla de configuración de conexión a la derecha. La captura muestra la pestaña «Main» de un gestor de conexiones con flechas rojas señalando los campos: Host `localhost`, Port `6379`, Database `0` (seleccionado en dropdown), Deployment `Standalone` (seleccionado en dropdown). Otros campos visibles: Type «Manual» (seleccionado) o URL; Authentication «Database Native»; Username vacío; Password vacío con «Save password» marcado.

(slide 24)

### Redis: operaciones CRUD

**Comandos CRUD:**

1. **Crear (Create):** Utiliza el comando SET para almacenar un par clave-valor.

```redis
SET clave1 valor1
```

2. **Leer (Read):** Usa el comando GET para obtener el valor asociado a una clave.

```redis
GET clave1
```

3. **Actualizar (Update):** Redis no tiene un comando específico para actualizar. Puedes usar nuevamente SET para sobrescribir el valor de una clave existente.

```redis
SET clave1 nuevo_valor1
```

4. **Eliminar (Delete):** Usa el comando DEL para eliminar una clave.

```redis
DEL clave1
```

**Figura:** Slide con título «BD Clave-Valor: Operaciones en REDIS» y lista numerada de los cuatro comandos CRUD con ejemplos de comandos Redis en bloques de código.

(slide 25)

### Comandos CRUD en Python

```python
import redis

# Conectar a Redis
rc = redis.StrictRedis(host='localhost', port=6379, db=0)

# Crear (Insertar un par clave-valor)
rc.set('username:1', 'heider_cs')
rc.set('nombre:1', 'Heider Sanchez')
rc.set('pais:1', 'Perú')
rc.set('rol:1', 'Administrador')

# Leer (Obtener el valor de una clave)
nombre = rc.get('nombre')
print(f"Nombre: {nombre.decode('utf-8')}")

# Actualizar (Modificar el valor de una clave)
rc.set('rol', 'Operador')

# Eliminar (Eliminar un par clave-valor)
rc.delete('pais:1')
```

**Figura:** Slide con encabezado «Comandos CRUD en Python:» a la izquierda y bloque de código Python a la derecha mostrando conexión con `redis.StrictRedis`, operaciones de crear cuatro claves con convención `campo:id`, leer con `rc.get` y decodificar con `.decode('utf-8')`, actualizar con `rc.set`, y eliminar con `rc.delete`.

(slide 26)

### Redis: TTL

- TTL (Time To Live) es el tiempo de vida de una key en Redis antes de que sea eliminada automáticamente.

- Como se utiliza:
  - EXPIRE clave tiempo (en segundos)
  - PEXPIRE clave tiempo (en milisegundos)
  - TTL clave (para conocer el tiempo restante)
  - PERSIST clave (para que la clave no expire)

```python
# Crear una clave con un TTL de 10 sec.
rc.setex("mi_clave", 10, "mi_valor")

# Comprobar el TTL de la clave
ttl = rc.ttl("mi_clave")
```

**Figura:** Slide con título «TTL en REDIS» a la izquierda: definición de TTL y lista de comandos (EXPIRE, PEXPIRE, TTL, PERSIST). A la derecha, recuadro con código Python de ejemplo usando `rc.setex` para crear clave con TTL de 10 segundos y `rc.ttl` para comprobar el tiempo restante.

(slide 27)

### Redis: ejemplo caché de respuestas de API

Caché de respuestas de API

- Se sabe que el servicio de clima actualiza los datos cada 10 minutos.
- Con REDIS almacenamos en caché por 10 minutos para reducir llamadas innecesarias.
- Beneficios: Menos peticiones a la API externa, reducción de costos y menor tiempo de respuesta para el usuario.

```python
def obtener_clima(ciudad):
    cache_key = f"clima:{ciudad}"

    # Intentar obtener desde Redis
    clima = rc.get(cache_key)
    if clima:
        return json.loads(clima)

    # Si no está en caché, llamar a la API
    url = f"{URL_WEATHERAPI}?key={API_KEY}&q={ciudad}"
    response = requests.get(url)
    data = response.json()

    # Guardar en Redis con una expiración de 10 minutos
    rc.setex(cache_key, 600, json.dumps(data))

    return data
```

**Figura:** Slide con subtítulo «Caché de respuestas de API» a la izquierda (tres viñetas sobre servicio de clima, estrategia de caché de 10 minutos y beneficios) y bloque de código Python a la derecha con función `obtener_clima` que consulta Redis con clave `clima:{ciudad}`, si no existe llama a API externa y guarda resultado con `rc.setex` y TTL de 600 segundos.

(slide 28)

### Redis: ejemplo caché de autenticación de usuarios

Caché de autenticación de usuarios

Un sistema web donde se evita la verificación repetitiva de credenciales en la base de datos.

- Con REDIS el token de sesión en caché y se renueva automáticamente.
- Beneficios: Evita múltiples validaciones de token en la base de datos, reduciendo la carga del sistema.

```python
def guardar_sesion(usuario_id, token):
    # Expira en 1 hora
    rc.setex(f"sesion:{usuario_id}", 3600, token)

def verificar_sesion(usuario_id, token):
    token_guardado = rc.get(f"sesion:{usuario_id}")
    if token_guardado and token_guardado.decode() == token:
        return True

    # Si no hay token en Redis, renovar con un Refresh Token.
    refresh_token = get_refresh_token_de_bd(usuario_id)
    if refresh_token:
        nuevo_token = generar_nuevo_token(usuario_id)
        guardar_sesion(usuario_id, nuevo_token)
        return nuevo_token

    return False
```

**Figura:** Slide con subtítulo «Caché de autenticación de usuarios» a la izquierda (descripción del sistema web, uso de REDIS para token de sesión con renovación automática, y beneficios de reducción de carga) y bloque de código Python a la derecha con funciones `guardar_sesion` (usa `rc.setex` con clave `sesion:{usuario_id}` y TTL de 3600 segundos) y `verificar_sesion` (compara token decodificado, si no existe intenta renovar con refresh token de BD).

(slide 29)

### Redis: comandos básicos

Comandos Básicos

| Comando Redis | Equivalente en Python | Ejemplo en Python |
|---|---|---|
| SET clave valor | r.set(clave, valor) | r.set("nombre", "Carlos") |
| GET clave | r.get(clave) | r.get("nombre") → "Carlos" |
| DEL clave | r.delete(clave) | r.delete("nombre") |
| EXISTS clave | r.exists(clave) | r.exists("nombre") → 1 (True) |
| EXPIRE clave segundos | r.expire(clave, segundos) | r.expire("nombre", 10) |
| TTL clave | r.ttl(clave) | r.ttl("nombre") |

**Figura:** Slide con subtítulo «Comandos Básicos» y tabla de tres columnas (Comando Redis, Equivalente en Python, Ejemplo en Python) con seis filas de comandos básicos. Encabezado de tabla con fondo azul y filas alternadas blanco/gris claro.

(slide 30)

### Redis: comandos de listas

Trabajando con Listas

| Comando Redis | Python | Ejemplo |
|---|---|---|
| LPUSH lista valor | r.lpush(lista, valor) | r.lpush("tareas", "Estudiar") |
| RPUSH lista valor | r.rpush(lista, valor) | r.rpush("tareas", "Dormir") |
| LPOP lista | r.lpop(lista) | r.lpop("tareas") |
| RPOP lista | r.rpop(lista) | r.rpop("tareas") |
| LRANGE lista inicio fin | r.lrange(lista, inicio, fin) | r.lrange("tareas", 0, -1) |

**Figura:** Slide con subtítulo «Trabajando con Listas» y tabla de tres columnas con cinco comandos de listas Redis y sus equivalentes Python.

(slide 31)

### Redis: comandos de hashes

Trabajando con Hashes (Diccionarios)

| Comando Redis | Python | Ejemplo |
|---|---|---|
| HSET hash campo valor | r.hset(hash, campo, valor) | r.hset("usuario:1", "nombre", "Juan") |
| HGET hash campo | r.hget(hash, campo) | r.hget("usuario:1", "nombre") |
| HGETALL hash | r.hgetall(hash) | r.hgetall("usuario:1") |
| HDEL hash campo | r.hdel(hash, campo) | r.hdel("usuario:1", "nombre") |

**Figura:** Slide con subtítulo «Trabajando con Hashes (Diccionarios)» y tabla de tres columnas con cuatro comandos de hashes Redis y sus equivalentes Python.

(slide 32)

### Redis: comandos de conjuntos

Trabajando con Conjuntos (Sets)

| Comando Redis | Python | Ejemplo |
|---|---|---|
| SADD set valor | r.sadd(set, valor) | r.sadd("colores", "rojo") |
| SMEMBERS set | r.smembers(set) | r.smembers("colores") |
| SREM set valor | r.srem(set, valor) | r.srem("colores", "rojo") |

**Figura:** Slide con subtítulo «Trabajando con Conjuntos (Sets)» y tabla de tres columnas con tres comandos de sets Redis y sus equivalentes Python.

(slide 33)

### Redis: comandos de sorted sets

Trabajando con Sorted Sets (ZSET)

| Comando Redis | Python | Ejemplo |
|---|---|---|
| ZADD ranking score valor | r.zadd(ranking, {valor: score}) | r.zadd("ranking", {"Carlos": 100}) |
| ZRANGE ranking 0 -1 WITHSCORES | r.zrange(ranking, 0, -1, withscores=True) | r.zrange("ranking", 0, -1, withscores=True) |

**Figura:** Slide con subtítulo «Trabajando con Sorted Sets (ZSET)» y tabla de tres columnas con dos comandos de sorted sets Redis y sus equivalentes Python.

(slide 34)

## Glosario

- **Columna:** Un par nombre/valor.
- **Fila:** Un contenedor de columnas identificado por una clave primaria.
- **Tabla:** Un contenedor de filas que están organizadas por particiones.
- **Partición:** Una colección de filas relacionadas que se almacenan juntas en los mismos nodos.
- **Familia de Columnas (Column Family):** Agrupación de columnas que comparten una misma clave de fila. En BigTable y Hbase es un grupo lógico explícito de columnas dentro de la tabla; en Cassandra es equivalente a una tabla.
- **Keyspace:** Contenedor de tablas (Column Family).
- **Cluster:** Contenedor de Keyspaces que abarca uno o más nodos.
- **CQL:** Lenguaje de consulta para interactuar con los Keyspaces en Cassandra.
- **Partition Key:** Determina cómo los datos están distribuidos a través de los nodos.
- **Clustering Key:** Determina cómo los datos están almacenados en un nodo.
- **Primary Key:** Partition Key + Clustering Key.
- **Snapshot (RDB):** Copias puntuales del dataset en intervalos configurables.
- **Append Only File (AOF):** Registra cada operación de escritura en un archivo de log.
- **TTL (Time To Live):** Tiempo de vida de una key en Redis antes de que sea eliminada automáticamente.
