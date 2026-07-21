---
curso: BIGDATA
titulo: 13 - Semana 11/Sem11_CassandraDB
slides: 38
fuente: 13 - Semana 11/Sem11_CassandraDB.pdf
---

## Slide 1

Portada. Título grande: **CassandraDB**. Autor: Mg. Aldo Lezama Benavides. Etiqueta: Semana 11. Foto decorativa del edificio de UTEC (concreto) y branding UTEC / "Reinventa el mundo".

## Slide 2

Título: **Objetivo de la sesión**. Lista de objetivos (dentro de un recuadro decorativo con corchetes):

- **Comprender** los fundamentos de Apache CassandraDB como base de datos NoSQL distribuida, su arquitectura, modelo de datos y mecanismos de replicación.
- **Aplicar** los principales comandos CQL (Cassandra Query Language) para la creación y gestión de keyspaces, tablas e índices, así como para realizar operaciones CRUD.
- **Analizar** las características de escalabilidad, rendimiento y disponibilidad que posicionan a Cassandra como una solución eficiente para entornos de Big Data y sistemas distribuidos.

## Slide 3

Título: **Contenido de la sesión**. Índice con dos bloques numerados en corchetes:

- **01.** Introducción
- **02.** Comandos

## Slide 4

Slide separador de sección. Número grande **01.** dentro de corchetes, icono de portapapeles/checklist, y título: **Introducción a CassandraDB**.

## Slide 5

Título: **Apache CassandraDB**. Bullets:

- Apache Cassandra es una base de datos distribuida, altamente escalable y de alto rendimiento, diseñada para gestionar grandes cantidades de datos en numerosos servidores, lo que proporciona alta disponibilidad sin un solo punto de fallo.
- Es un tipo de base de datos NoSQL.

Visual: logo de Cassandra a la derecha (el ojo azul estilizado con el patrón de nodos/estrella en la pupila) y la palabra "cassandra" en cursiva gris.

## Slide 6

Título: **Características de Cassandra**. Bullets:

- **Escalabilidad elástica:** Cassandra es altamente escalable; permite agregar más hardware para dar cabida a más clientes y más datos según las necesidades.
- **Arquitectura siempre activa:** Cassandra no tiene un único punto de fallo y está continuamente disponible para aplicaciones críticas para el negocio que no pueden permitirse un fallo.
- **Rendimiento rápido y lineal:** Cassandra es linealmente escalable; es decir, aumenta el rendimiento a medida que aumenta el número de nodos en el clúster. Por lo tanto, mantiene un tiempo de respuesta rápido.

Visual (diagrama de rueda/dona de 6 segmentos alrededor del logo del ojo "cassandra" en el centro). Segmentos coloreados con las características en inglés:
- ELASTIC SCALABILITY (morado)
- EFFICIENT WRITES (naranja)
- HA & FAULT TOLERANT (verde)
- TUNABLE CONSISTENCY (azul)
- CASSANDRA QUERY LANGUAGE (marrón)
- FLEXIBLE DATA STORAGE (turquesa)
- EASY DATA DISTRIBUTION (rojo/rosa)

## Slide 7

Título: **Características de Cassandra**. Bullets:

- **Almacenamiento de datos flexible:** Cassandra admite todos los formatos de datos posibles, incluyendo: estructurados, semiestructurados y no estructurados. Puede adaptarse dinámicamente a los cambios en sus estructuras de datos según sus necesidades.
- **Almacenamiento de datos flexible:** (repetido) Cassandra admite todos los formatos de datos posibles, incluyendo: estructurados, semiestructurados y no estructurados. Puede adaptar dinámicamente los cambios en sus estructuras de datos según sus necesidades.
- **Distribución sencilla de datos:** Cassandra ofrece la flexibilidad de distribuir datos donde los necesite, replicando datos en múltiples centros de datos.

Visual: misma rueda/dona de 6 segmentos de características (ELASTIC SCALABILITY, EFFICIENT WRITES, HA & FAULT TOLERANT, TUNABLE CONSISTENCY, CASSANDRA QUERY LANGUAGE, FLEXIBLE DATA STORAGE, EASY DATA DISTRIBUTION) con el ojo cassandra al centro.

## Slide 8

Título: **Características de Cassandra**. Bullets:

- **Compatibilidad con transacciones:** Cassandra admite propiedades como Atomicidad, Consistencia, Aislamiento y Durabilidad (ACID).
- **Escrituras rápidas:** Cassandra fue diseñada para funcionar en hardware económico y de consumo. Realiza escrituras increíblemente rápidas y puede almacenar cientos de terabytes de datos sin sacrificar la eficiencia de lectura.

Visual: misma rueda/dona de 6 segmentos de características con el ojo cassandra al centro.

## Slide 9

Título: **Historia de CassandraDB**. Bullets:

- Cassandra se desarrolló en Facebook para la búsqueda en la bandeja de entrada.
- Facebook la lanzó al mercado de código abierto en julio de 2008.
- Cassandra fue aceptada en la Incubadora Apache en marzo de 2009.
- Se convirtió en un proyecto de alto nivel de Apache desde febrero de 2010.

Visual (línea de tiempo con logos y flechas descendentes que indican la genealogía de Cassandra):
Google (**Bigtable, 2005**) + Amazon (**Dynamo, 2007**) → flecha hacia abajo → Facebook (**Open Source, 2008**) → flecha → pluma de Apache (**Apache, 2009**) → flecha → logo del ojo (**Cassandra, 2010**).

## Slide 10

Título: **Replicación de datos en Cassandra**. Bullets:

- En Cassandra, uno o más nodos de un clúster actúan como réplicas de un dato determinado.
- Si se detecta que alguno de los nodos respondió con un valor desactualizado, Cassandra devolverá el valor más reciente al cliente.
- Tras devolver el valor más reciente, Cassandra realiza una reparación de lectura en segundo plano para actualizar los valores obsoletos.

Visual (diagrama de anillo de replicación): seis servidores/torres etiquetados "Cassandra" dispuestos en anillo alrededor de dos nodos centrales etiquetados "Application". Flechas curvas entre los nodos del anillo rotuladas "Replication" muestran la replicación entre réplicas; los nodos Application en el centro tienen flechas hacia los nodos Cassandra del anillo.

## Slide 11

Título: **Cassandra Query Language**. Bullets:

- Los usuarios pueden acceder a Cassandra a través de sus nodos mediante el lenguaje de consulta Cassandra (CQL). CQL trata la base de datos (espacio de claves) como un contenedor de tablas.
- Los programadores utilizan cqlsh: un indicador para trabajar con CQL o controladores de lenguajes de aplicación independientes.
- Los clientes acceden a cualquiera de los nodos para sus operaciones de lectura y escritura. Ese nodo (coordinador) actúa como intermediario entre el cliente y los nodos que almacenan los datos.

Visual: gráfico con el texto "Cassandra Query Language" y un diagrama en cruz alrededor del logo cassandra (centro). Cuatro nodos-burbuja de colores: **Insert Dml Statement** (arriba, azul), **Update Dml Statement** (izquierda, naranja), **Where Criteria** (derecha, rojo), **Delete Dml Statement** (abajo, verde).

## Slide 12

Título: **Modelo de datos**. Bullets:

- El modelo de datos de Cassandra es significativamente diferente al que solemos ver en un RDBMS.
- La base de datos de Cassandra se distribuye en varias máquinas que operan conjuntamente.
- El contenedor más externo se conoce como Clúster.
- Para la gestión de fallos, cada nodo contiene una réplica y, en caso de fallo, la réplica toma el control.
- Cassandra organiza los nodos en un clúster, en formato de anillo, y les asigna datos.

Visual: gráfico comparativo "**SQL** vs **Cassandra**" — icono de cilindro azul de base de datos SQL, un "vs" rojo, y el icono del ojo de Cassandra.

## Slide 13

Título: **Modelo de datos**. Bullets:

- **Keyspaces** es el contenedor más externo para los datos en Cassandra. Los atributos básicos de un espacio de claves en Cassandra son:
- **Replication Factor:**
  - Representa la cantidad de máquinas del clúster que recibirán copias de los mismos datos.
- **Replica placement strategy:**
  - Es la estrategia para colocar réplicas en el anillo. Existen estrategias como la estrategia simple (estrategia basada en racks), la estrategia de topología de red antigua (estrategia basada en racks) y la estrategia de topología de red (estrategia compartida por centro de datos).

Visual (diagrama de arquitectura anidada de un keyspace): recuadro azul externo **Keyspace** que contiene un bloque "Settings" y un recuadro naranja **Column family**. Dentro de Column family hay un bloque "Settings" y un bloque amarillo **Row**: una "Row Key" verde con flecha que apunta a una serie de columnas — cada una "Column Key₁ (Cell Key)", "Column Key₂ (Cell Key)", … "Column Keyₙ (Cell Key)" — con flechas rojas hacia abajo a "Column Value (Cell)". Pie: "A representation of the basic architecture of a Cassandra keyspace."

## Slide 14

Título: **Modelo de datos**. Bullets:

- **Column families:**
  - Keyspace contiene una lista de una o más familias de columnas. Una familia de columnas, a su vez, contiene un conjunto de filas. Cada fila contiene columnas ordenadas. Las familias de columnas representan la estructura de los datos. Cada keyspace tiene al menos una y, a menudo, varias familias de columnas.

Visual (diagrama azul teal anidado): recuadro **keyspace** que contiene "settings" y un recuadro **column family**; dentro, "settings" y un recuadro **column** con tres celdas: **name**, **value**, **timestamp**.

## Slide 15

Título: **Modelo de datos**. Bloque de código CQL:

```cql
CREATE KEYSPACE Keyspace name WITH
replication =
{
'class': 'SimpleStrategy',
'replication_factor' : 3
};
```

Visual (diagrama): un recuadro **Keyspace** que contiene dos cajas **Column Family** una al lado de otra, cada una con varias filas de pequeñas celdas grises (representando filas y columnas de datos).

## Slide 16

Título: **Modelo de datos**. Bullets:

- **Column Family** contiene una colección ordenada de filas. Cada fila, a su vez, es una colección ordenada de columnas.
- Una familia de columnas de Cassandra tiene los siguientes atributos:
  - **keys_cached:** Representa el número de ubicaciones que se mantendrán en caché por SSTable.
  - **rows_cached:** Representa el número de filas cuyo contenido completo se almacenará en caché.
  - **preload_row_cache:** Especifica si se desea rellenar previamente la caché de filas.

Visual (diagrama de filas y columnas): "Row Key 1" con flecha a un bloque de columnas — Column 1 → Value 1, Column 2 → Value 2, Column 3 → Value 3. "Row Key 2" con flecha a otro bloque — Column 1 → Value 1, Column 4 → Value 4 (ilustra que cada fila puede tener columnas distintas).

## Slide 17

Slide separador de sección. Número grande **02.** en corchetes, icono de portapapeles/checklist, título: **Comandos**.

## Slide 18

Título: **Comandos del Shell (1)**.

**HELP**
- El comando HELP muestra una sinopsis y una breve descripción de todos los comandos cqlsh.

**CAPTURE**
- Este comando captura la salida de un comando y la agrega a un archivo.

**CONSISTENCY**
- Este comando muestra el nivel de consistencia actual o establece un nuevo nivel de consistencia.
- Este comando copia datos desde y hacia Cassandra a un archivo.

**COPY**
Ejemplo para copiar la tabla llamada emp al archivo myfile.
```cql
COPY emp (emp_id, emp_city, emp_name, emp_phone, emp_sal) TO 'myfile';
```

Visual: imagen "Cassandra Shell Commands" — un ojo estilizado y un racimo de burbujas de colores con nombres de comandos: FILE, U, OVERVIEW, HELP, COLOR, NO COLOR, VERSION, EXECUTE, DEBUG, P.

## Slide 19

Título: **Comandos del Shell (2)**.

**DESCRIBE**
- Este comando describe el clúster actual de Cassandra y sus objetos. Las variantes de este comando se explican a continuación.
- Describir CLUSTER: Este comando proporciona información sobre el clúster.
- Describir KEYSPACES: Este comando enumera todos los espacios de claves de un clúster.
- Describir TABLES: Este comando enumera todas las tablas de un espacio de claves.

**EXPAND**
- Este comando se usa para expandir la salida. Antes de usarlo, debe activar el comando de expansión.

Visual: misma imagen "Cassandra Shell Commands" (racimo de burbujas de comandos: FILE, U, OVERVIEW, HELP, COLOR, NO COLOR, VERSION, EXECUTE, DEBUG, P).

## Slide 20

Título: **Comandos del Shell (3)**.

**SHOW**
- Este comando muestra los detalles de la sesión cqlsh actual, como la versión de Cassandra, el host o los supuestos de tipo de datos.
  - show host
  - show version

**SOURCE**
- Usando este comando, puedes ejecutar los comandos en un archivo.

Visual: misma imagen "Cassandra Shell Commands" (racimo de burbujas de comandos).

## Slide 21

Título: **Operaciones Keyspace**. Bullets:

- Un **keyspace** en Cassandra es un espacio de nombres que define la replicación de datos en los nodos.
- Un clúster contiene un espacio de claves por nodo. A continuación, se muestra la sintaxis para crear un espacio de claves mediante la instrucción CREATE KEYSPACE.
- Sintaxis:
  - `CREATE KEYSPACE <identifier> WITH <properties>`
  - Example:
  - `CREATE KEYSPACE "KeySpace Name" WITH replication = {'class': 'Strategy name', 'replication_factor' : 'No.Of replicas'};`

Visual (diagrama gris de tabla dentro de un keyspace): recuadro **Keyspace** que contiene una **Table** con filas etiquetadas x, y, z y celdas en una cuadrícula. Flechas/etiquetas anotan los conceptos: **columns** (arriba), **partitions** (izquierda, apuntando a filas x/y/z), **cell** (derecha, apuntando a una celda), **rows** (derecha), **Partition key** (abajo, apuntando a la fila z).

## Slide 22

Título: **Create table**. Bloque de código (sintaxis en rojo, ejemplo en azul):

```cql
CREATE TABLE tablename(
column1 name datatype PRIMARYKEY,
column2 name data type,
column3 name data type)
```
Ejemplo:
```cql
CREATE TABLE emp(
emp_id int PRIMARY KEY,
emp_name text,
emp_city text,
emp_sal varint,
emp_phone varint
);
```

## Slide 23

Título: **Alter Table**. Texto:

Puede modificar una tabla con el comando ALTER TABLE. Usando el comando ALTER, puede realizar las siguientes operaciones:
- Añadir una columna
- Eliminar una columna
- Actualizar las opciones de una tabla con la palabra clave.

Ejemplo (en rojo):
```cql
ALTER TABLE emp
ADD emp_email text;
ALTER TABLE emp DROP emp_email
```

## Slide 24

Título: **Drop and Truncate Table**.

- Comando **Drop table**:
  - Puede eliminar una tabla con el comando "Eliminar tabla".
  - Ejemplo:
```cql
DROP TABLE emp;
```
- **Truncar una tabla**
  - Puede truncar una tabla con el comando "TRUNCATE". Al truncar una tabla, todas sus filas se eliminan permanentemente.
  - Ejemplo:
```cql
TRUNCATE student;
```

## Slide 25

Título: **Crear Index**. Bullets:

- Puedes crear un índice en Cassandra usando el comando CREATE INDEX. Su sintaxis es la siguiente:
```cql
CREATE INDEX <identifier> ON <tablename>
```
- A continuación, se muestra un ejemplo de cómo crear un índice para una columna. Aquí creamos un índice para la columna "emp_name" en una tabla llamada emp.
```cql
CREATE INDEX name ON emp1 (emp_name);
```

## Slide 26

Título: **Sentencias Bash** (BATCH). Bullets:

- Usando BATCH, puedes ejecutar múltiples declaraciones de modificación (insertar, actualizar, eliminar) simultáneamente. Su sintaxis es la siguiente:
```cql
BEGIN BATCH
<insert-stmt> / <update-stmt> / <delete-stmt>
APPLY BATCH
```
- Ejemplo:
```cql
BEGIN BATCH
... INSERT INTO emp (emp_id, emp_city, emp_name, emp_phone, emp_sal) values ( 4,'Pune','rajeev', 9848022331, 30000);
... UPDATE emp SET emp_sal = 50000 WHERE emp_id =3;
... DELETE emp_city FROM emp WHERE emp_id = 2;
... APPLY BATCH;
```

## Slide 27

Título: **INSERT**. Captura de pantalla de terminal cqlsh (fondo negro, columnas coloreadas). Contenido:

```
select * from emp ;

 emp_id | emp_city | emp_name | emp_phone | emp_sal
--------+----------+----------+-----------+---------

(0 rows)
cqlsh:      INSERT INTO emp (emp_id, emp_name, emp_city,
       ... emp_phone, emp_sal) VALUES(1,'ram', 'Hyderabad', 9848022338, 50000);
cqlsh:      INSERT INTO emp (emp_id, emp_name, emp_city,
       ... emp_phone, emp_sal) VALUES(2,'robin', 'Hyderabad', 9848022339, 40000);
cqlsh:      INSERT INTO emp (emp_id, emp_name, emp_city,
       ... emp_phone, emp_sal) VALUES(3,'rahman', 'Chennai', 9848022330, 45000);
cqlsh:      select * from emp ;

 emp_id | emp_city  | emp_name | emp_phone  | emp_sal
--------+-----------+----------+------------+---------
      1 | Hyderabad |      ram | 9848022338 |   50000
      2 | Hyderabad |    robin | 9848022339 |   40000
      3 |   Chennai |   rahman | 9848022330 |   45000
```

## Slide 28

Título: **UPDATE**. Texto:

UPDATE es el comando que se utiliza para actualizar los datos de una tabla. Al actualizar los datos de una tabla, se utilizan las siguientes palabras clave:
- **Where:** Esta cláusula se utiliza para seleccionar la fila que se va a actualizar.
- **Set:** Establece el valor con esta palabra clave.
- **Must:** Incluye todas las columnas que componen la clave principal.

Ejemplo (en rojo):
```cql
UPDATE emp SET emp_city='Delhi', emp_sal=50000 WHERE emp_id=2;
```

## Slide 29

Título: **UPDATE**. Captura de terminal cqlsh mostrando el resultado del UPDATE:

```
cqlsh:      UPDATE emp SET emp_city='Delhi',emp_sal=50000
       ... WHERE emp_id=2;
cqlsh:      select * from emp ;

 emp_id | emp_city  | emp_name | emp_phone  | emp_sal
--------+-----------+----------+------------+---------
      1 | Hyderabad |      ram | 9848022338 |   50000
      2 |     Delhi |    robin | 9848022339 |   50000
      3 |   Chennai |   rahman | 9848022330 |   45000

(3 rows)
```
(La fila emp_id=2 ahora tiene emp_city=Delhi y emp_sal=50000.)

## Slide 30

Título: **LECTURA**. Captura de terminal cqlsh con dos consultas SELECT:

```
cqlsh:      select * from emp ;

 emp_id | emp_city  | emp_name | emp_phone  | emp_sal
--------+-----------+----------+------------+---------
      1 | Hyderabad |      ram | 9848022338 |   50000
      2 |     Delhi |    robin | 9848022339 |   50000
      3 |   Chennai |   rahman | 9848022330 |   45000

(3 rows)
cqlsh:      SELECT emp_name, emp_sal from emp;

 emp_name | emp_sal
----------+---------
      ram |   50000
    robin |   50000
   rahman |   45000

(3 rows)
```

## Slide 31

Título: **LECTURA**. Captura de terminal cqlsh: creación de índice y SELECT con WHERE:

```
cqlsh:      CREATE INDEX ON emp(emp_sal);
cqlsh:      SELECT * FROM emp WHERE emp_sal=50000;

 emp_id | emp_city  | emp_name | emp_phone  | emp_sal
--------+-----------+----------+------------+---------
      1 | Hyderabad |      ram | 9848022338 |   50000
      2 |     Delhi |    robin | 9848022339 |   50000

(2 rows)
```

## Slide 32

Título: **Borrar una data**. Captura de terminal cqlsh mostrando DELETE de una columna específica:

```
cqlsh: select * from emp ;

 emp_id | emp_city  | emp_name | emp_phone  | emp_sal
--------+-----------+----------+------------+---------
      1 | Hyderabad |      ram | 9848022338 |   50000
      2 |     Delhi |    robin | 9848022339 |   50000
      3 |   Chennai |   rahman | 9848022330 |   45000

(3 rows)
cqlsh: DELETE emp_sal FROM emp WHERE emp_id=3;
cqlsh: select * from emp ;

 emp_id | emp_city  | emp_name | emp_phone  | emp_sal
--------+-----------+----------+------------+---------
      1 | Hyderabad |      ram | 9848022338 |   50000
      2 |     Delhi |    robin | 9848022339 |   50000
      3 |   Chennai |   rahman | 9848022330 |    null
```
(Al borrar solo la columna emp_sal de emp_id=3, el valor queda en **null**; la línea DELETE está resaltada en amarillo.)

## Slide 33

Título: **Borrar una data**. Captura de terminal cqlsh mostrando DELETE de una fila completa:

```
cqlsh: select * from emp ;

 emp_id | emp_city  | emp_name | emp_phone  | emp_sal
--------+-----------+----------+------------+---------
      1 | Hyderabad |      ram | 9848022338 |   50000
      2 |     Delhi |    robin | 9848022339 |   50000
      3 |   Chennai |   rahman | 9848022330 |    null

(3 rows)
cqlsh: DELETE FROM emp WHERE emp_id=3;
cqlsh: select * from emp ;

 emp_id | emp_city  | emp_name | emp_phone  | emp_sal
--------+-----------+----------+------------+---------
      1 | Hyderabad |      ram | 9848022338 |   50000
      2 |     Delhi |    robin | 9848022339 |   50000
```
(Al usar DELETE FROM ... WHERE emp_id=3 se elimina la fila completa; la línea DELETE está resaltada en amarillo.)

## Slide 34

Título: **Listas**. Texto:

- **List** se utiliza cuando se debe mantener el orden de los elementos y se debe almacenar un valor varias veces.
- Se pueden obtener los valores de un tipo de dato de lista utilizando el índice de los elementos de la lista.

Captura de terminal cqlsh:
```
cqlsh: CREATE TABLE data(name text PRIMARY KEY, email
       ... list<text>);
cqlsh: INSERT INTO data(name, email) VALUES ('ramu',
       ... ['abc@gmail.com','cba@yahoo.com']);
cqlsh: select * from data;

 name | email
------+------------------------------------
 ramu | ['abc@gmail.com', 'cba@yahoo.com']

(1 rows)
```

## Slide 35

Título: **Sets**. Texto:

- **Set** es un tipo de dato que se utiliza para almacenar un grupo de elementos.
- Los elementos de un conjunto se devolverán ordenados.

Captura de terminal cqlsh:
```
cqlsh: CREATE TABLE data2 (name text PRIMARY KEY, phone
       ... set<varint>);
cqlsh: INSERT INTO data2(name, phone) VALUES ('rahman',
       ... {9848022338,9848022339});
cqlsh: select * from data2;

 name   | phone
--------+----------------------------
 rahman | {9848022338, 9848022339}

(1 rows)
```

## Slide 36

Título: **Map**. Texto:

- **Map** es un tipo de dato que se utiliza para almacenar un par clave-valor de elementos.

Captura de terminal cqlsh:
```
cqlsh: CREATE TABLE data4 (name text PRIMARY KEY, address map<text, text>);
cqlsh: INSERT INTO data4 (name, address)
       ... VALUES ('robin', {'home' : 'Pune' , 'office': 'Nashik' });
cqlsh: select * from data4;

 name  | address
-------+----------------------------------------
 robin | {'home': 'Pune', 'office': 'Nashik'}

(1 rows)
```

## Slide 37

Título: **Conclusiones**. Tres puntos numerados (en corchetes decorativos):

- **01.** CassandraDB se destaca por su capacidad de manejo de grandes volúmenes de datos mediante una arquitectura distribuida sin punto único de fallo.
- **02.** Su modelo de datos basado en keyspaces y familias de columnas ofrece gran flexibilidad para adaptar estructuras de información a diferentes necesidades empresariales.
- **03.** Gracias a su alto rendimiento, escalabilidad lineal y replicación eficiente, Cassandra es una herramienta clave en aplicaciones críticas de Big Data y en infraestructuras en la nube.

## Slide 38

Slide de cierre. Solo el logo UTEC (Universidad de Ingeniería y Tecnología) centrado sobre fondo cian. Decorativa.
