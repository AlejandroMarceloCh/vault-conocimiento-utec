---
curso: BIGDATA
titulo: 04 - Semana 2/S2 Sistemas de Archivos Distribuidos
slides: 36
fuente: 04 - Semana 2/S2 Sistemas de Archivos Distribuidos.pdf
---

SISTEMA DE
ARCHIVOS
DISTRIBUIDOS
Semana 2
   Objetivos de la sesión

Comprender qué es un sistema de archivos distribuido y cómo
permite manejar grandes volúmenes de datos garantizando
escalabilidad, tolerancia a fallos y disponibilidad.
Analizar la arquitectura de Hadoop, con énfasis en sus componentes
principales: HDFS (almacenamiento distribuido) y YARN (gestión de
recursos)
Explorar el ecosistema Hadoop y sus herramientas (Hive, Pig,
HBase, Spark, MongoDB, Cassandra, etc.), entendiendo cómo aportan
valor en el procesamiento y análisis de Big Data
Contenido de la sesión

     01.         02.

  Sistema de
   Archivos      Hadoop
  Distribuidos
01.   Sistema de Archivos
      Distribuidos
Sistemas de Archivos Distribuidos

Un sistema de archivos distribuido (DFS) permite a los clientes
acceder al almacenamiento de archivos desde múltiples hosts a
través   de   una   red   informática   como   si   accedieran   al
almacenamiento local. Los archivos se distribuyen entre varios
servidores de almacenamiento y en múltiples ubicaciones, lo
que permite a los usuarios compartir datos y recursos de
almacenamiento. Un DFS puede diseñarse para que los
usuarios geográficamente dispersos, como los trabajadores
remotos y los equipos distribuidos, puedan acceder y compartir
archivos de forma remota como si estuvieran almacenados
localmente.
Sistemas de Archivos Distribuidos

Un DFS agrupa varios nodos de almacenamiento y
distribuye lógicamente los conjuntos de datos entre
múltiples nodos, cada uno con su propia capacidad de
procesamiento y almacenamiento. Los datos en un DFS
pueden residir en diversos dispositivos de almacenamiento,
como unidades de estado sólido y discos duros.
Sistemas de Archivos Distribuidos

Los conjuntos de datos se replican en varios servidores, lo que
garantiza la redundancia y una alta disponibilidad de los datos .
El DFS se ubica en un conjunto de servidores, mainframes o un
entorno en la nube a través de una red de área local (AN), lo
que permite que múltiples usuarios accedan y almacenen datos
no estructurados . Las organizaciones que necesiten ampliar su
infraestructura pueden agregar más nodos de almacenamiento
al DFS.
Sistemas de Archivos Distribuidos

Los clientes acceden a los datos en un DFS mediante
namespaces. Las organizaciones pueden agrupar carpetas
compartidas en namespaces lógicos. Un espacio de nombres
es el grupo compartido de almacenamiento en red en la raíz de
un DFS. Estos espacios presentan los archivos a los usuarios
como una carpeta compartida con varias subcarpetas. Cuando
un usuario solicita un archivo, el DFS carga la primera copia
disponible.
Sistemas de Archivos Distribuidos

Existen dos tipos de espacios de nombres:


• Standalone DFS namespaces. Un standalone o namespace
  independiente tiene un único servidor host y no utiliza Active
  Directory ( AD). En un namespace standaalone, los datos de
  configuración del DFS se almacenan en el registro del servidor
  host. Este tipo de espacio se suele utilizar en entornos que solo
  requieren un servidor.
Sistemas de Archivos Distribuidos

Existen dos tipos de espacios de nombres:


• Domain-based DFS namespaces. Los namespaces DFS
  basados ​en dominio integran y almacenan la configuración DFS
  en Active Directory (AD). Cuentan con varios servidores host y
  los datos de topología DFS se almacenan en AD. Estos
  namespaces se utilizan habitualmente en entornos que
  requieren una mayor disponibilidad.
Ventajas de los Sistemas de Archivos Distribuidos
Quizás la ventaja más significativa de un DFS sea que proporciona a las organizaciones un sistema escalable para gestionar
datos no estructurados de forma remota. Puede ayudar a las organizaciones a utilizar el almacenamiento heredado para
ahorrar en costes de dispositivos y hardware de almacenamiento.


A continuación, se detallan algunos beneficios adicionales:
• Alta disponibilidad y redundancia. La replicación de archivos preserva los datos en caso de fallos puntuales, lo que
  confiere al sistema una alta tolerancia a fallos.
• Mejor rendimiento. La distribución del almacenamiento de datos entre nodos permite el acceso paralelo y una mejor
  entrada/salida ( E/S ).
• Compartir datos de forma colaborativa. Gracias a los mecanismos de bloqueo y al control de versiones, varios usuarios
  pueden trabajar en los mismos archivos simultáneamente y desde diferentes ubicaciones.
• Ahorro de costes. La mayoría de las opciones de DFS pueden ejecutarse en hardware estándar, lo que abarata la
  infraestructura.
Desventajas de los Sistemas de Archivos Distribuidos
Las siguientes desventajas de los deportes de fantasía diarios (DFS) no son evidentes a primera vista, pero deben
considerarse cuidadosamente:


• Complejidad. Planificar y construir un DFS no es fácil; la arquitectura de red por sí sola puede requerir mucho tiempo y
  esfuerzo.
• Cuellos de botella. Debido a que las comprobaciones de coherencia y la sincronización son constantes, a menudo pueden
  producirse cuellos de botella de E/S.
• Desafíos de seguridad. Los datos distribuidos en múltiples nodos y ubicaciones requieren que todos ellos estén protegidos,
  lo cual puede resultar abrumador.
• Problemas de ancho de banda. La replicación y sincronización perpetuas generan una gran cantidad de tráfico de red,
  además del propio movimiento de datos.
Características de Sistemas de Archivos Distribuidos
Las organizaciones utilizan un DFS por sus características como la escalabilidad , la seguridad y el acceso remoto a los
datos. Las características adicionales de un DFS incluyen las siguientes:
• Independencia de la ubicación. Los usuarios no necesitan saber dónde se almacenan los datos. El DFS gestiona la
  ubicación y presenta los archivos como si estuvieran almacenados localmente.
• Escalabilidad. Para escalar un DFS, las organizaciones pueden agregar servidores de archivos o nodos de
  almacenamiento.
• Alta disponibilidad. El DFS debe seguir funcionando en caso de un fallo parcial del sistema, como un fallo de nodo o
  un fallo de disco. Además, debe crear copias de seguridad si el sistema falla.
• Seguridad. Los datos deben cifrarse tanto en reposo como en tránsito para evitar el acceso no autorizado o la
  eliminación de datos.
   Características de Sistemas de Archivos Distribuidos
• Transparencia. La transparencia mantiene los detalles de un sistema de archivos alejados de otros sistemas de archivos y
  usuarios. Existen varios tipos de transparencia en los sistemas de archivos distribuidos, entre los que se incluyen los
  siguientes:
❑ Transparencia estructural. Los datos aparecen como si estuvieran en el dispositivo del usuario. Los usuarios no pueden ver
  cómo está configurado el DFS, como por ejemplo el número de servidores de archivos o dispositivos de almacenamiento.
❑ Acceso transparente. Los usuarios pueden acceder a archivos ubicados localmente o de forma remota. Se puede acceder a
  los archivos independientemente de la ubicación del usuario, siempre que haya iniciado sesión en el sistema. Si los datos no
  se almacenan en el mismo servidor, los usuarios no deberían poder detectarlo, y las aplicaciones que trabajan con archivos
  locales también deberían poder ejecutarse en archivos remotos.
❑ Transparencia en la replicación. Los archivos replicados ubicados en diferentes nodos del sistema de archivos, como por
  ejemplo en otro sistema de almacenamiento, permanecen ocultos para los demás nodos del sistema. Esto permite que el
  sistema cree varias copias sin afectar el rendimiento.
❑ Transparencia en la nomenclatura. Los archivos no deben cambiar al moverlos entre nodos de almacenamiento
Sistemas de Archivos Distribuidos
Ejemplo: Google usa su Google File System (GFS) para manejar
millones de archivos en sus data centers.
Sistemas de Archivos Distribuidos
Hadoop Distributed File System


• El más conocido en Big Data es HDFS (usado por Hadoop).
• Divide archivos grandes en bloques (por defecto de 128 MB).
• Guarda copias de cada bloque en diferentes nodos (ej. 3 copias).
• Tiene un NameNode (coordina la metadata: quién tiene qué bloque) y
  múltiples DataNodes (guardan los datos).


Ejemplo: Si subes un dataset de 1GB, HDFS lo divide en 8 bloques de
128 MB y los distribuye en varios servidores, con redundancia.
Sistemas de Archivos Distribuidos
Ejemplos Reales de DFS
• HDFS: usado en empresas que procesan Big Data (Netflix, Yahoo,
  Facebook).
• Google File System (GFS): base de Google Drive y su buscador.
• Amazon     S3:   aunque    más    que    un   DFS,   funciona   como
  almacenamiento distribuido en la nube.
• Ceph: muy usado en entornos de cloud privados.


Caso práctico: Netflix guarda historiales de reproducción de millones de
usuarios en HDFS para luego analizarlos con Spark.
02.   Hadoop
Historia
En los años 2000, la web crecía exponencialmente y las empresas
necesitaban procesar terabytes y petabytes de datos.
Google publicó en 2003 y 2004 dos artículos clave:
• GFS (Google File System): sistema de archivos distribuido.
• MapReduce: modelo para procesar grandes volúmenes en
  paralelo.
Inspirados en estos papers, Doug Cutting y Mike Cafarella
desarrollaron un proyecto open source para manejar datos
                                                                   Doug Cutting   Mike Cafarella
masivos. Inicialmente, Hadoop formó parte del proyecto Nutch (un
motor de búsqueda de código abierto).
Historia
• En 2006, Yahoo! adoptó Hadoop para su buscador y fue clave
  en su consolidación.
• En 2008, Hadoop se convirtió en proyecto de nivel superior en la
  Apache Software Foundation.
• Pronto empresas como Facebook, Twitter, LinkedIn y Netflix lo
  adoptaron para almacenar y analizar Big Data.
• Hoy, Hadoop es un ecosistema con HDFS, MapReduce, Hive,
  Pig, HBase, Spark y más, usado en todo tipo de industrias.
• Se le considera el inicio de la era del Big Data en el mundo
  tecnológico.

Hadoop
Hadoop es un framework de código abierto, diseñado específicamente
para almacenar y procesar grandes volúmenes de datos en entornos
distribuidos. La filosofía detrás de Hadoop es simple pero poderosa:
“mover el procesamiento hacia donde están los datos”. En lugar de
trasladar enormes cantidades de información a un servidor central para
analizarlas, Hadoop distribuye el procesamiento entre los nodos que ya
almacenan los datos, optimizando así el rendimiento. Se caracteriza por
ser altamente escalable (basta con añadir más máquinas para
incrementar su capacidad), tolerante a fallos (gracias a la replicación de
los datos), y económico, pues funciona sobre hardware común, sin
necesidad de servidores especializados de alto costo.
Hadoop
Objetivos del Ecosistema Hadoop


• Escalabilidad: Capacidad de almacenar grandes volúmenes de
  datos
• Tolerancia a fallos: Capacidad de recuperarse de errores de
  hardware
• Tipos de datos: Capacidad de gestionar datos de diferentes tipos
• Entorno compartido: Capacidad de gestionar tareas de forma
  simultánea.
• Aportar valor: Capacidad de extraer valor de los datos
Arquitectura Hadoop
La arquitectura de Hadoop descansa sobre dos pilares principales:
HDFS (Hadoop Distributed File System) y YARN (Yet Another Resource
Negotiator).
HDFS es el sistema de archivos distribuido que permite dividir un archivo
en bloques (normalmente de 128 MB) y almacenarlos en diferentes
nodos del clúster. Cada bloque se replica en varios servidores para
garantizar disponibilidad y resiliencia ante fallos. HDFS está compuesto
por dos tipos de nodos: el NameNode, que actúa como servidor maestro
y administra los metadatos (qué bloques existen y dónde están
guardados), y los DataNodes, que son los nodos que almacenan
físicamente los bloques de datos.
Arquitectura Hadoop
YARN, por su parte, es el gestor de recursos del clúster. Su tarea
principal es coordinar cómo se asignan la memoria, la CPU y los
procesos entre los diferentes nodos. Está compuesto por tres elementos
fundamentales: el ResourceManager, que administra los recursos
globales; los NodeManagers, que gestionan los recursos en cada
servidor; y los ApplicationMasters, que se encargan de ejecutar
aplicaciones específicas.


Gracias a esta combinación, Hadoop puede almacenar datos a gran
escala y al mismo tiempo procesarlos de manera distribuida y paralela.
Ecosistema Hadoop

                                                                             El   ecosistema    Hadoop   incluye    un      conjunto   de
    Hive              Pig
                                                                             herramientas   y     aplicaciones     para   alcanzar   estos
                                                                             objetivos.
    MapReduce

                                               HBase
                                                       Cassandra   MongoDB
                                                                             Estas aplicaciones se pueden organizar en un diagrama
    YARN Yet Another Resource Negotiator
                                                                             de capas.

    HDFS Hadoop
         Hadoop Distributed File System
                                                                             Las capas representan distintas interfaces, desde el
                                                                             almacenamiento a los lenguajes de alto nivel.
                             Hardware Básico
Ecosistema Hadoop

                                                                             Hive: Permite acceder a HDFS como si fuera una Base de
    Hive              Pig
                                                                             datos, ejecutando comandos muy parecido a SQL para
                                                                             recuperar valores (HiveSQL). Simplifica enormemente el
    MapReduce
                                                                             desarrollo y la gestión con Hadoop.

                                               HBase
                                                       Cassandra   MongoDB
    YARN Yet Another Resource Negotiator

    HDFS Hadoop
         Hadoop Distributed File System


                             Hardware Básico
Ecosistema Hadoop

    Hive              Pig
                                                                             Pig: Lenguaje de alto de nivel para analizar grandes
                                                                             volúmenes de datos. Trabaja en paralelo, lo que permite
    MapReduce
                                                                             gestionar gran cantidad de información. Realmente es un

                                               HBase
                                                       Cassandra   MongoDB
                                                                             compilador que genera comandos MapReduce, mediante
    YARN Yet Another Resource Negotiator
                                                                             el lenguaje textual denominado Pig Latin.

    HDFS Hadoop
         Hadoop Distributed File System


                             Hardware Básico
Ecosistema Hadoop

                                                                             Spark: Es un motor muy eficiente de procesamiento de
    Hive              Pig
                                                                             datos a gran escala. Implementa procesamiento en tiempo
                                                                             real al contrario que MapReduce, lo que provoca que sea
    MapReduce
                                                                             más rápido. Para ello, en vez de almacenar los datos en

                                               HBase
                                                       Cassandra   MongoDB
                                                                             disco, trabaja de forma masiva en memoria. Puede trabajar
    YARN Yet Another Resource Negotiator
                                                                             de forma autónoma, sin necesidad de Hadoop.

    HDFS Hadoop
         Hadoop Distributed File System


                             Hardware Básico
Ecosistema Hadoop

                                                                             HBase: Es el sistema de almacenamiento NoSQL basado
    Hive              Pig
                                                                             en columnas para Hadoop.
                                                                             • Es una base de datos de código abierto, distribuida y
    MapReduce
                                                                               escalable para el almacenamiento de Big Data.

                                               HBase
                                                       Cassandra   MongoDB
                                                                             • Escrita en Java, implementa y proporciona capacidades
    YARN Yet Another Resource Negotiator
                                                                               similares sobre Hadoop y HDFS.
                                                                             • El objetivo de este proyecto es el de trabajar con
    HDFS Hadoop
         Hadoop Distributed File System
                                                                               grandes tablas, de miles de millones de filas de millones
                                                                               de columnas, sobre un clúster Hadoop.
                             Hardware Básico
Ecosistema Hadoop

                                                                             Storm: es un sistema distribuido de procesamiento en
    Hive              Pig
                                                                             tiempo real, diseñado para trabajar con flujos de datos
                                                                             continuos como sensores, redes sociales o transacciones
    MapReduce
                                                                             financieras. Funciona mediante topologías que conectan

                                               HBase
                                                       Cassandra   MongoDB
                                                                             spouts   (fuentes   de   datos)   y   bolts   (unidades   de
    YARN Yet Another Resource Negotiator
                                                                             procesamiento) para transformar la información al instante.
                                                                             Se integra con Hadoop, HDFS, Kafka y bases NoSQL
    HDFS Hadoop
         Hadoop Distributed File System
                                                                             como Cassandra o MongoDB, complementando el análisis
                                                                             batch con streaming. Sus principales ventajas son la baja
                             Hardware Básico
                                                                             latencia, escalabilidad y tolerancia a fallos. Aunque hoy
                                                                             compite con Spark Streaming y Flink, sigue siendo clave
                                                                             en aplicaciones que requieren inmediatez..
Ecosistema Hadoop

                                                                             Cassandra: es una base de datos NoSQL distribuida y
    Hive              Pig
                                                                             orientada   a   columnas,     diseñada   para   ofrecer   alta
                                                                             disponibilidad sin puntos únicos de fallo gracias a su
    MapReduce
                                                                             arquitectura peer-to-peer. Está optimizada para manejar

                                               HBase
                                                       Cassandra   MongoDB
                                                                             escrituras rápidas en tiempo real y utiliza CQL, un lenguaje
    YARN Yet Another Resource Negotiator
                                                                             similar a SQL. Se integra con Hadoop y Spark mediante
                                                                             conectores, permitiendo combinar análisis en lote con
    HDFS Hadoop
         Hadoop Distributed File System
                                                                             datos en línea. Es ideal para sectores como banca,
                                                                             telecomunicaciones e IoT, donde la velocidad y la
                             Hardware Básico
                                                                             resiliencia son esenciales.
Ecosistema Hadoop

                                                                             MongoDB: es una base de datos NoSQL orientada a
    Hive              Pig
                                                                             documentos que almacena datos en BSON (JSON
                                                                             binario), ofreciendo gran flexibilidad de esquemas. Soporta
    MapReduce
                                                                             replicación y sharding, lo que le otorga escalabilidad y

                                               HBase
                                                       Cassandra   MongoDB
                                                                             disponibilidad en entornos distribuidos. Destaca por sus
    YARN Yet Another Resource Negotiator
                                                                             consultas rápidas y potentes a través de su lenguaje
                                                                             basado en JSON y pipelines de agregación. Mediante el
    HDFS Hadoop
         Hadoop Distributed File System
                                                                             Mongo-Hadoop Connector, puede integrarse al ecosistema
                                                                             Hadoop para análisis masivos. Es muy usado en
                             Hardware Básico
                                                                             aplicaciones web, móviles y redes sociales.
Ecosistema Hadoop

                                                                             Flume: Servicio distribuido y altamente eficiente para
    Hive              Pig
                                                                             distribuir, agregar y recolectar grandes cantidades de
                                                                             información. Es útil para cargar y mover información en
    MapReduce
                                                                             Hadoop, como ficheros de logs, datos de Twitter/Reddit,

                                               HBase
                                                       Cassandra   MongoDB
                                                                             etc. Utiliza una arquitectura de tipo streaming con un flujo
    YARN Yet Another Resource Negotiator
                                                                             de datos muy potente y personalizables

    HDFS Hadoop
         Hadoop Distributed File System


                             Hardware Básico
Ecosistema Hadoop

                                                                             Sqoop: Permite transferir un gran volumen de datos de
    Hive              Pig
                                                                             manera eficiente entre Hadoop y sistemas gestores de
                                                                             base de datos relacionales.
    MapReduce

                                               HBase
                                                       Cassandra   MongoDB
    YARN Yet Another Resource Negotiator

    HDFS Hadoop
         Hadoop Distributed File System


                             Hardware Básico
                      Conclusiones

01.   Los sistemas de archivos distribuidos son la base del Big Data porque permiten
      almacenar datos en múltiples nodos como si fueran un solo repositorio lógico




02.   Hadoop revolucionó la industria al introducir HDFS y MapReduce, posibilitando el
      procesamiento distribuido y paralelo de datos masivos


      La escalabilidad, la tolerancia a fallos y el uso de hardware económico hacen que
03.   Hadoop sea una solución eficiente para empresas que gestionan grandes
      volúmenes de información


      El ecosistema Hadoop ofrece un conjunto de herramientas complementarias
04.   (Spark, Hive, HBase, Cassandra, MongoDB, etc.) que extienden sus capacidades para
      análisis batch, en tiempo real y con diferentes tipos de datos

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
