---
curso: BIGDATA
titulo: 05 - Semana 3/Semana 3 - Arquitectura de Apache Hadoop
slides: 37
fuente: 05 - Semana 3/Semana 3 - Arquitectura de Apache Hadoop.pdf
---

Arquitectura de Apache Hadoop:
HDFS, MapReduce y YARN
Mg. Aldo Lezama Benavides


Semana 3
     Objetivo de la sesión

Comprender el funcionamiento del modelo HDFS como framework
de   almacenamiento      y    MapReduce   como   framework   de
procesamiento distribuido y paralelo.
Identificar los componentes principales de YARN (Resource
Manager, Node Manager, Application Master y Containers) y su rol
dentro del ecosistema Hadoop.
Analizar cómo las interfaces web de Hadoop (HDFS NameNode y
YARN ResourceManager) permiten monitorear datos, nodos y
aplicaciones en un clúster.
       Contenido de la sesión

01.         02.         03.        04.

HDFS       MapReduce    Yarn    Interfaces Web
01.   HDFS
                                                        HDFS
                                       ¿Cómo vamos a guardar esa información?


                                                                              Concepto:

Hive              Pig                                                         • Sistema de almacenamiento de Apache Hadoop
                                                                              • Diseñado para grandes volúmenes de datos (Big
MapReduce                                                                        Data)


                                                HBase
                                                                              • Distribuye archivos en múltiples nodos del cluster



                                                        Cassandra   MongoDB
YARN Yet Another Resource Negotiator                                          Características:
                                                                              • Distribuido
HDFS Hadoop
     Hadoop Distributed File System
                                                                              • Escalable
                                                                              • Tolerante a fallos
                         Hardware Básico
                                                                              • Optimizado para Big Data
                                                        HDFS
                                       ¿Cómo vamos a guardar esa información?


                                                                              NameNode (Master)

Hive              Pig                                                         • Administra el sistema de archivos
                                                                              • Guarda metadatos:
MapReduce                                                                     ❖ dónde están los archivos

                                                HBase
                                                                              ❖ cómo están divididos


                                                        Cassandra   MongoDB
YARN Yet Another Resource Negotiator                                          No guarda los datos


HDFS Hadoop
     Hadoop Distributed File System                                           DataNodes (Workers)
                                                                              • Almacenan los datos reales
                         Hardware Básico                                      • Ejecutan operaciones de lectura/escritura
                                                     HDFS
                                       ¿Cómo vamos a guardar esa información?




                                                       600MB

                                                                       Audio       Video   Imagen      Correo




         Nodo A                    Nodo B               Nodo C                 Nodo D               Nodo E


         128MB                     128MB                128MB                  128MB                88MB


HDFS va separar los datos en tipos, según
capacidad de información
                                          HDFS
                            ¿Cómo vamos a guardar esa información?




                                            600MB




         Nodo A          Nodo B              Nodo C               Nodo D             Nodo E


          128MB          128MB               128MB                 128MB              88MB


HDFS hace copias de
la data y lo almacena    Nodo A              Nodo A         Método de replicación   TOLERANTE A FALLOS!!!
entre diferentes nodos
02.   MAPREDUCE
                                             MapReduce
                                       ¿Cómo vamos a procesar los datos?



                                                                           MapReduce permite procesar grandes cantidades de
Hive              Pig                                                      datos en forma paralela


MapReduce                                                                  MapReduce puede explotar las características de los

                                             HBase
                                                                 MongoDB
                                                                           sistemas de cómputo paralelos/distribuidos


                                                     Cassandra
YARN Yet Another Resource Negotiator
                                                                           MapReduce es un framework altamente escalable
HDFS Hadoop
     Hadoop Distributed File System


                         Hardware Básico                                   MapReduce divide el procesamiento en dos fases
                                                                           fundamentales: la fase de mapeo “Map” y la fase de
                                                                           reducción “Reduce”
                            Flujo de MapReduce

               Input


División      División       División    Los datos se particionan




Mapper       Mapper          Mapper


           Sort & Shuffle



Reducer      Reducer         Reducer



              Output
                            Flujo de MapReduce

               Input


División      División       División

                                        La fase Map se ejecuta en subtareas llamadas mappers. Estos se ejecutan en los nodos en que se
                                        encuentran los datos.
Mapper       Mapper          Mapper     Estos componentes son los responsables de generar pares clave-valor filtrando, agrupando,
                                        ordenando o transformando los datos originales. Los pares de datos intermedios, no se almacenan
                                        en HDFS.

           Sort & Shuffle



Reducer      Reducer         Reducer



              Output
                            Flujo de MapReduce

               Input


División      División       División



Mapper       Mapper          Mapper

                                        En la fase de ordenación, los datos se ordenan y particionan de acuerdo con las claves obtenidas
           Sort & Shuffle               por los mappers.
                                        Los datos particionados y ordenados se envían a los procesos reductores




Reducer      Reducer         Reducer



              Output
                            Flujo de MapReduce

               Input


División      División       División



Mapper       Mapper          Mapper


           Sort & Shuffle


                                        La fase Reduce gestiona la agregación de los valores producidos por todos los mappers del
Reducer      Reducer         Reducer    sistema (o por la fase shuffle) de tipo clave-valor en función de su clave. Por último, cada reducer
                                        genera su fichero de salida de forma independiente, generalmente escrito en HDFS.




              Output
                            Flujo de MapReduce

               Input


División      División       División



Mapper       Mapper          Mapper


           Sort & Shuffle



Reducer      Reducer         Reducer



                                            Los datos se combinan
              Output
  Ejemplo: Conteo de Palabras
                                                Manzana Plátano Mango
                                                 Tomate Mango Mango
                                Input           Manzana Plátano Tomate




          División             División         División



          Mapper               Mapper           Mapper




                         Sort & Shuffle



Reducer              Reducer              Reducer              Reducer



                               Output
  Ejemplo: Conteo de Palabras
                                 Input


          División              División              División
    Manzana Plátano Mango   Tomate Mango Mango   Manzana Plátano Tomate



          Mapper                Mapper                Mapper




                            Sort & Shuffle



Reducer               Reducer                Reducer                  Reducer



                                Output
  Ejemplo: Conteo de Palabras
                                Input


          División             División            División



          Mapper               Mapper              Mapper
               Manzana, 1      Tomate, 1     Manzana, 1
               Plátano, 1      Mango, 2      Plátano, 1
                Mango, 1                     Tomate, 1


                            Sort & Shuffle



Reducer              Reducer               Reducer            Reducer



                               Output
  Ejemplo: Conteo de Palabras
                                   Input


          División               División                  División



          Mapper                 Mapper                    Mapper




                            Sort & Shuffle

     Manzana, [1,1]     Plátano, [1,1]      Mango, [1,2]       Tomate, [1,1]



Reducer               Reducer                  Reducer                    Reducer



                                  Output
  Ejemplo: Conteo de Palabras
                                  Input


          División              División            División



          Mapper                Mapper              Mapper




                            Sort & Shuffle



Reducer               Reducer               Reducer            Reducer

             Manzana, 2   Plátano, 2   Mango, 3   Tomate, 2



                                 Output

  Ejemplo: Conteo de Palabras
                                                                   Manzana Plátano Mango
                                                                    Tomate Mango Mango
                                       Input                       Manzana Plátano Tomate




          División                   División                      División
    Manzana Plátano Mango       Tomate Mango Mango        Manzana Plátano Tomate



          Mapper                     Mapper                        Mapper
                 Manzana, 1           Tomate, 1          Manzana, 1
                 Plátano, 1           Mango, 2           Plátano, 1
                  Mango, 1                               Tomate, 1


                                Sort & Shuffle

      Manzana, [1,1]        Plátano, [1,1]        Mango, [1,2]          Tomate, [1,1]



Reducer                Reducer                       Reducer                       Reducer

             Manzana, 2       Plátano, 2      Mango, 3           Tomate, 2



                                      Output
03.   YARN
                        YARN Yet Another Resource Negotiator
                                       ¿Qué recursos o hardware vamos a utilizar?




Hive              Pig                                                          YARN es un gestor de recursos y aplicaciones que
                                                                               pretende extender el procesamiento en los clústeres
MapReduce                                                                      Hadoop más allá del modelo MapReduce


                                                 HBase
                                                         Cassandra   MongoDB
YARN Yet Another Resource Negotiator                                           Yarn incluye dos aspectos fundamentales:


HDFS Hadoop
     Hadoop Distributed File System
                                                                               • Gestión de recursos
                                                                               • Planificación y monitorización de tareas
                         Hardware Básico
                        YARN Yet Another Resource Negotiator
                                       ¿Qué recursos o hardware vamos a utilizar?




Hive              Pig                                                          Recursos con las cuales contamos:
                                                                               • Unidades de almacenamiento
MapReduce                                                                      • Memoria


                                                 HBase
                                                                               • CPU



                                                         Cassandra   MongoDB
YARN Yet Another Resource Negotiator
                                                                               El YARN asigna los recursos a las tareas, según sea
HDFS Hadoop
     Hadoop Distributed File System
                                                                               necesario y que estén disponibles en ese momento.
                                                                               Administra un cluster
                         Hardware Básico
                        YARN Yet Another Resource Negotiator
                                       ¿Qué recursos o hardware vamos a utilizar?




Hive              Pig                                                          Recursos con las cuales contamos:
                                                                               • Unidades de almacenamiento
MapReduce                                                                      • Memoria


                                                 HBase
                                                                               • CPU



                                                         Cassandra   MongoDB
YARN Yet Another Resource Negotiator
                                                                               El YARN asigna los recursos a las tareas, según sea
HDFS Hadoop
     Hadoop Distributed File System
                                                                               necesario y que estén disponibles en ese momento.
                                                                               Administra un CLUSTER
                         Hardware Básico
Clúster

          Un clúster es un conjunto de computadoras conectadas
          que trabajan como un solo sistema para procesar
          grandes volúmenes de datos.


          Tipos de nodos
          ❑ Nodo maestro (Master Node)
          Es el que coordina todo el clúster.
          Funciones:
          • Gestiona recursos
          • Controla dónde están los datos
          • Orquesta los procesos
          No está pensado para procesar datos masivamente
Cluster

          Un cluster es un conjunto de computadoras conectadas
          que trabajan como un solo sistema para procesar
          grandes volúmenes de datos.


          Tipos de nodos
          ❑ Nodos trabajadores (Worker Nodes)
          Son los que hacen el trabajo pesado.
          Funciones:
          • Procesan datos
          • Almacenan datos
          • Ejecutan tareas
          Aquí ocurre el “cómputo real”
           Cluster
¿Qué se ejecuta dentro de los nodos?



                          Los nodos son infraestructura, pero dentro corre software


                          En el nodo maestro:
                          • HDFS (NameNode)
                          • YARN (ResourceManager)


                          En cada nodo worker:
                          • DataNode (almacenamiento)
                          • NodeManager (ejecución de tareas)
                                              YARN
                             ¿Qué recursos o hardware vamos a utilizar?

                                                           RESOURCE MANAGER
                                                           • Corre en el nodo maestro
               Resource                                    • Controla la gestión de recursos del sistema
               Manager                                     • Introduce Schedulers para asignar las tareas entre los distintos nodos
                                                           • Acepta envíos de tareas por parte de los clientes y gestiona la ejecución


                                                           NODE MANAGER
                                                           • Corre en los nodos workers
                                                           • Controla los recursos locales de cada nodo
Node Manager   Node Manager            Node Manager
                                                           • En cada uno de estos nodos se ejecuta un container
                                                           • Recibe las tareas que les va asignando el ResourceManager
                                                           • Manda información al RM sobre el estado del nodo

  Container      Container               Container
                                                           APPLICATION
                                                           • Es un proceso único que se lanza cada vez que envías una aplicación a YARN
                                                           • Pide recursos al ResourceManager
 Application                                               • Cuando los obtiene, ordena a los NodeManagers que arranquen containers para
                 Container               Container
  Master                                                     ejecutar tareas
                                                           • Monitorea el progreso de esas tareas


                                                           CONTAINER
                                                           • Un container es la unidad mínima de recursos que el clúster asigna para ejecutar
                                                             una tarea.
                                                           • Contiene CPU, Memoria y Permisos
                               ANALOGÍA


               Resource
               Manager
                                             RESOURCE MANAGER
                                             Es el administrador del hotel (decide en qué
                                             habitaciones se hospedan los huéspedes)


Node Manager   Node Manager   Node Manager   NODE MANAGER
                                             • Es el recepcionista de cada piso (habilita las
                                               habitaciones en su área).

  Container      Container      Container
                                             APPLICATION
                                             • Es el organizador de un         evento   (pide
                                               habitaciones para su grupo).
 Application
                 Container      Container
  Master
                                             CONTAINER
                                             • una habitación del hotel (donde se hospedan
                                               los asistentes, o sea, las tareas).
04.   INTERFACES
Clúster – Interfaces Web


                           HDFS NameNode
                           Sirve para:
                           •   Ver todos los archivos y carpetas que has guardado
                               en HDFS.
                           •   Revisar el uso de espacio en disco en el clúster.
                           •   Ver en qué DataNodes están almacenados los
                               bloques de un archivo.
                           •   Monitorear el estado de los DataNodes (salud,
                               capacidad, bloques replicados, bloques perdidos).
                           Clic en:
                           <Nombre del cluster> → Interfaz Web → HDFS
                           NameNode
el hostname interno de cada worker (cluster-14e6-w-0 y cluster-14e6-w-1).




                                                                            HDFS NameNode



                                                                                            El NameNode está activo
                                                                                            Es el servicio que administra el sistema de archivos HDFS.
                                                                                            •   Configured    Capacity:    Capacidad   total   del   HDFS   (≈   98   GB
                                                                                                configurados en tu clúster).
                                                                                            •   DFS Used: Uso DFS (archivos en HDFS).
                                                                                            •   Non DFS Used: Uso de Non DFS
                                                                                            •   DFS Remaining: DFS restante
                                                                                            •   Estado de los DataNodes
Clúster – Interfaces Web


                           YARN ResourceManager
                           Sirve para:
                           Ver el estado de las aplicaciones que corren en YARN
                           (ej. Spark jobs, MapReduce jobs).
                           Monitorear cuántos recursos (memoria, vCores) están
                           siendo usados por cada aplicación.
                           Ver la cola de trabajos (pendientes, en ejecución,
                           terminados, fallidos).
                           Consultar los NodeManagers (nodos workers) y los
                           contenedores que tienen asignados.
                           Clic en:
                           <Nombre del cluster> → Interfaz Web → YARN
                           ResourceManager
YARN ResourceManager




Total Resources   nos muestra la suma de la memoria y CPU de tus 2 nodos workers.


 Active Nodes     Nos muestra los 2 Node Managers (en los workers) están activos y reportando


Node Address      Muestra el hostname interno de cada worker (cluster-14e6-w-0 y cluster-14e6-w-1).
                     Conclusiones

01.   MapReduce es un modelo robusto y escalable para dividir grandes volúmenes de
      datos en tareas de mapeo y reducción, aprovechando la computación distribuida.




02.   YARN actúa como el gestor de recursos y aplicaciones de Hadoop, permitiendo
      ejecutar múltiples frameworks (no solo MapReduce) en el mismo clúster.


      Los componentes de YARN (Resource Manager, Node Managers, Application
03.   Master y Containers) trabajan de forma coordinada para asignar recursos y
      ejecutar aplicaciones de manera eficiente

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
