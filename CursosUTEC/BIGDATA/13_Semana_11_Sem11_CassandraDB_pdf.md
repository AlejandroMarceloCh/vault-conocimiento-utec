---
curso: BIGDATA
titulo: 13 - Semana 11/Sem11_CassandraDB
slides: 38
fuente: 13 - Semana 11/Sem11_CassandraDB.pdf
---

CassandraDB
Mg. Aldo Lezama Benavides


Semana 11
      Objetivo de la sesión

•   Comprender los fundamentos de Apache CassandraDB como base de

    datos NoSQL distribuida, su arquitectura, modelo de datos y mecanismos

    de replicación

•   Aplicar los principales comandos CQL (Cassandra Query Language)

    para la creación y gestión de keyspaces, tablas e índices, así como para

    realizar operaciones CRUD

•   Analizar las características de escalabilidad, rendimiento y disponibilidad

    que posicionan a Cassandra como una solución eficiente para entornos

    de Big Data y sistemas distribuidos
Contenido de la sesión

      01.          02.

   Introducción   Comandos
01.   Introducción a CassandraDB
                                Apache CassandraDB




• Apache Cassandra es una base de datos distribuida,
  altamente escalable y de alto rendimiento, diseñada para
  gestionar grandes cantidades de datos en numerosos
  servidores, lo que proporciona alta disponibilidad sin un
  solo punto de fallo.
• Es un tipo de base de datos NoSQL
                          Características de Cassandra


• Escalabilidad elástica: Cassandra es altamente escalable; permite agregar
  más hardware para dar cabida a más clientes y más datos según las
  necesidades.
• Arquitectura siempre activa: Cassandra no tiene un único punto de fallo y
  está continuamente disponible para aplicaciones críticas para el negocio
  que no pueden permitirse un fallo.
• Rendimiento rápido y lineal: Cassandra es linealmente escalable; es decir,
  aumenta el rendimiento a medida que aumenta el número de nodos en el
  clúster. Por lo tanto, mantiene un tiempo de respuesta rápido.
                            Características de Cassandra


• Almacenamiento de datos flexible: Cassandra admite todos los formatos
  de datos posibles, incluyendo: estructurados, semiestructurados y no
  estructurados. Puede adaptarse dinámicamente a los cambios en sus
  estructuras de datos según sus necesidades.
• Almacenamiento de datos flexible: Cassandra admite todos los formatos
  de datos posibles, incluyendo: estructurados, semiestructurados y no
  estructurados. Puede adaptar dinámicamente los cambios en sus
  estructuras de datos según sus necesidades.
• Distribución sencilla de datos: Cassandra ofrece la flexibilidad de distribuir
  datos donde los necesite, replicando datos en múltiples centros de datos.
                            Características de Cassandra



• Compatibilidad con transacciones: Cassandra admite propiedades como
  Atomicidad, Consistencia, Aislamiento y Durabilidad (ACID).


• Escrituras rápidas: Cassandra fue diseñada para funcionar en hardware
  económico y de consumo. Realiza escrituras increíblemente rápidas y
  puede almacenar cientos de terabytes de datos sin sacrificar la eficiencia de
  lectura.
                              Historia de CassandraDB


• Cassandra se desarrolló en Facebook para la búsqueda
  en la bandeja de entrada.
• Facebook la lanzó al mercado de código abierto en julio
  de 2008.
• Cassandra fue aceptada en la Incubadora Apache en
  marzo de 2009.
• Se convirtió en un proyecto de alto nivel de Apache
  desde febrero de 2010
                         Replicación de datos en Cassandra


• En Cassandra, uno o más nodos de un clúster actúan
  como réplicas de un dato determinado.
• Si se detecta que alguno de los nodos respondió con un
  valor desactualizado, Cassandra devolverá el valor más
  reciente al cliente.
• Tras devolver el valor más reciente, Cassandra realiza
  una reparación de lectura en segundo plano para
  actualizar los valores obsoletos
                           Cassandra Query Language


• Los usuarios pueden acceder a Cassandra a través de
  sus nodos mediante el lenguaje de consulta Cassandra
  (CQL). ​CQL trata la base de datos (espacio de claves)
  como un contenedor de tablas.
• Los programadores utilizan cqlsh: un indicador para
  trabajar con CQL o controladores de lenguajes de
  aplicación independientes.
• Los clientes acceden a cualquiera de los nodos para sus
  operaciones   de    lectura   y   escritura.   Ese   nodo
  (coordinador) actúa como intermediario entre el cliente y
  los nodos que almacenan los datos.
                                        Modelo de datos


• El modelo de datos de Cassandra es significativamente
  diferente al que solemos ver en un RDBMS.
• La base de datos de Cassandra se distribuye en varias
  máquinas que operan conjuntamente.
• El contenedor más externo se conoce como Clúster.
• Para la gestión de fallos, cada nodo contiene una réplica
  y, en caso de fallo, la réplica toma el control.
• Cassandra organiza los nodos en un clúster, en formato
  de anillo, y les asigna datos.
                                       Modelo de datos

• Keyspaces es el contenedor más externo para los datos en
  Cassandra. Los atributos básicos de un espacio de claves en
  Cassandra son:
• Replication Factor:
– Representa la cantidad de máquinas del clúster que recibirán
copias de los mismos datos.
• Replica placement strategy:
– Es la estrategia para colocar réplicas en el anillo. Existen
estrategias como la estrategia simple (estrategia basada en
racks), la estrategia de topología de red antigua (estrategia
basada en racks) y la estrategia de topología de red (estrategia
compartida por centro de datos).
                                   Modelo de datos


• Column families:
– Keyspace contiene una lista de una o más familias de
columnas. Una familia de columnas, a su vez, contiene un
conjunto de filas. Cada fila contiene columnas ordenadas.
Las familias de columnas representan la estructura de los
datos. Cada keyspace tiene al menos una y, a menudo,
varias familias de columnas.
                             Modelo de datos



CREATE KEYSPACE Keyspace name WITH
replication =
{
'class’: 'SimpleStrategy’,
'replication_factor' : 3
};
                                      Modelo de datos

• Column Family contiene una colección ordenada de
  filas. Cada fila, a su vez, es una colección ordenada de
  columnas.
• Una familia de columnas de Cassandra tiene los
siguientes atributos:
– keys_cached: Representa el número de ubicaciones
que se mantendrán en caché por SSTable.
– rows_cached: Representa el número de filas cuyo
contenido completo se almacenará en caché.
– preload_row_cache: Especifica si se desea rellenar
previamente la caché de filas.
02.   Comandos
                                   Comandos del Shell (1)

HELP
• El comando HELP muestra una sinopsis y una breve descripción de
  todos los comandos cqlsh.
CAPTURE
• Este comando captura la salida de un comando y la agrega a un
  archivo.
CONSISTENCY
• Este comando muestra el nivel de consistencia actual o establece un
  nuevo nivel de consistencia
• Este comando copia datos desde y hacia Cassandra a un archivo.
COPY
Ejemplo para copiar la tabla llamada emp al archivo myfile.
– COPY emp (emp_id, emp_city, emp_name, emp_phone, emp_sal)
TO ‘myfile’;
                                Comandos del Shell (2)

DESCRIBE
• Este comando describe el clúster actual de Cassandra y sus
  objetos. Las variantes de este comando se explican a
  continuación.
• Describir CLUSTER: Este comando proporciona información
  sobre el clúster.
• Describir KEYSPACES: Este comando enumera todos los
  espacios de claves de un clúster.
• Describir TABLES: Este comando enumera todas las tablas
  de un espacio de claves.
EXPAND
• Este comando se usa para expandir la salida. Antes de
  usarlo, debe activar el comando de expansión.
                                Comandos del Shell (3)

SHOW
• Este comando muestra los detalles de la sesión cqlsh actual,
    como la versión de Cassandra, el host o los supuestos de
    tipo de datos.
o    show host
o    show version
SOURCE
• Usando este comando, puedes ejecutar los comandos en un
    archivo..

                                       Operaciones Keyspace


• Un keyspace en Cassandra es un espacio de nombres que define
   la replicación de datos en los nodos.
• Un clúster contiene un espacio de claves por nodo. A continuación,
   se muestra la sintaxis para crear un espacio de claves mediante la
   instrucción CREATE KEYSPACE.
• Sintaxis:
– CREATE KEYSPACE <identifier> WITH
<properties>
– Example:
– CREATE KEYSPACE “KeySpace Name” WITH
replication = {'class': ‘Strategy name’,
'replication_factor' : ‘No.Of replicas’};
                              Create table

CREATE TABLE tablename(
column1 name datatype PRIMARYKEY,
column2 name data type,
column3 name data type)
• Ejemplo:
CREATE TABLE emp(
emp_id int PRIMARY KEY,
emp_name text,
emp_city text,
emp_sal varint,
emp_phone varint
);
                                            Alter Table


Puede modificar una tabla con el comando ALTER TABLE.
Usando el comando ALTER, puede realizar las siguientes
operaciones:
– Añadir una columna
– Eliminar una columna
– Actualizar las opciones de una tabla con la palabra clave.
• Ejemplo:
– ALTER TABLE emp
– ADD emp_email text;
– ALTER TABLE emp DROP emp_email
                                 Drop and Truncate Table


• Comando Drop table:
– Puede eliminar una tabla con el comando "Eliminar tabla".
Ejemplo:
DROP TABLE emp;
• Truncar una tabla
– Puede truncar una tabla con el comando "TRUNCATE".
Al   truncar   una    tabla,   todas   sus   filas   se   eliminan
permanentemente.
Ejemplo:
TRUNCATE student;
                                        Crear Index


• Puedes crear un índice en Cassandra usando el comando
  CREATE INDEX. Su sintaxis es la siguiente:
  CREATE INDEX <identifier> ON <tablename>
• A continuación, se muestra un ejemplo de cómo crear un
  índice para una columna. Aquí creamos un índice para la
  columna "emp_name" en una tabla llamada emp.
  CREATE INDEX name ON emp1 (emp_name);
                                      Sentencias Bash

• Usando BATCH, puedes ejecutar múltiples declaraciones de modificación (insertar, actualizar, eliminar)
  simultáneamente. Su sintaxis es la siguiente:
BEGIN BATCH
<insert-stmt> / <update-stmt> / <delete-stmt>
APPLY BATCH
• Ejemplo:
BEGIN BATCH
... INSERT INTO emp (emp_id, emp_city, emp_name,
emp_phone, emp_sal) values ( 4,'Pune','rajeev',
9848022331, 30000);
... UPDATE emp SET emp_sal = 50000 WHERE emp_id =3;
... DELETE emp_city FROM emp WHERE emp_id = 2;
... APPLY BATCH;
INSERT
                                                UPDATE


UPDATE es el comando que se utiliza para actualizar los datos de una tabla.
Al actualizar los datos de una tabla, se utilizan las siguientes palabras clave:
– Where: Esta cláusula se utiliza para seleccionar la fila que se va a actualizar.
– Set: Establece el valor con esta palabra clave.
– Must: Incluye todas las columnas que componen la clave principal.
• Ejemplo:
– UPDATE emp SET emp_city='Delhi',
emp_sal=50000 WHERE emp_id=2;
UPDATE
LECTURA
LECTURA
Borrar una data
Borrar una data
                                             Listas

List se utiliza cuando se debe mantener el orden de los elementos y se debe almacenar un valor varias veces.
• Se pueden obtener los valores de un tipo de dato de lista utilizando el índice de los elementos de la lista.
                                            Sets

Set es un tipo de dato que se utiliza para almacenar un grupo de elementos.
• Los elementos de un conjunto se devolverán ordenados.
                                            Map

Map es un tipo de dato que se utiliza para almacenar un par clave-valor de elementos.
                     Conclusiones

01.   CassandraDB se destaca por su capacidad de manejo de grandes volúmenes de
      datos mediante una arquitectura distribuida sin punto único de fallo


      Su modelo de datos basado en keyspaces y familias de columnas ofrece gran
02.   flexibilidad para adaptar estructuras de información a diferentes necesidades
      empresariales


      Gracias a su alto rendimiento, escalabilidad lineal y replicación eficiente,
03.   Cassandra es una herramienta clave en aplicaciones críticas de Big Data y en
      infraestructuras en la nube.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
