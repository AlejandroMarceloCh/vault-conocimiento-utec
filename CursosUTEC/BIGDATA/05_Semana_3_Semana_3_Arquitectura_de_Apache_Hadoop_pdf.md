---
curso: BIGDATA
titulo: 05 - Semana 3/Semana 3 - Arquitectura de Apache Hadoop
slides: 37
fuente: 05 - Semana 3/Semana 3 - Arquitectura de Apache Hadoop.pdf
---

## Slide 1

Portada (decorativa: fondo cian degradado, foto del edificio UTEC, logo UTEC, cinta "Reinventa el mundo").

Título: **Arquitectura de Apache Hadoop: HDFS, MapReduce y YARN**
Autor: Mg. Aldo Lezama Benavides
Semana 3

## Slide 2

**Objetivo de la sesión**

Texto dentro de un recuadro de esquinas tipo corchetes:

- **Comprender** el funcionamiento del modelo HDFS como framework de almacenamiento y MapReduce como framework de procesamiento distribuido y paralelo.
- **Identificar** los componentes principales de YARN (Resource Manager, Node Manager, Application Master y Containers) y su rol dentro del ecosistema Hadoop.
- **Analizar** cómo las interfaces web de Hadoop (HDFS NameNode y YARN ResourceManager) permiten monitorear datos, nodos y aplicaciones en un clúster.

## Slide 3

**Contenido de la sesión**

Cuatro secciones numeradas, cada una dentro de corchetes:

| 01. | 02. | 03. | 04. |
|-----|-----|-----|-----|
| HDFS | MapReduce | Yarn | Interfaces Web |

## Slide 4

Slide divisor de sección. Número grande **01.** entre corchetes, ícono de portapapeles/checklist, y el título **HDFS**.

## Slide 5

**HDFS — ¿Cómo vamos a guardar esa información?**

Visual (izquierda): diagrama del **stack del ecosistema Apache Hadoop** en capas apiladas, con logo de Apache Software Foundation arriba. De arriba hacia abajo:
- Fila superior: **Hive** (con logo abeja Hive) · **Pig**; a la derecha columnas verticales **Storm**, **Spark**, **HBase** (ícono orca), **Cassandra**, **MongoDB**.
- **MapReduce** (logo hadoop MapReduce)
- **YARN** Yet Another Resource Negotiator (logo hadoop YARN)
- **HDFS** Hadoop Distributed File System (logo hadoop HDFS) — **resaltado con recuadro rojo**
- **Hardware Básico** (base verde)
- Abajo: logos de Flume y Sqoop.

Texto (derecha):

**Concepto:**
- Sistema de almacenamiento de Apache Hadoop
- Diseñado para grandes volúmenes de datos (Big Data)
- Distribuye archivos en múltiples nodos del cluster

**Características:**
- Distribuido
- Escalable
- Tolerante a fallos
- Optimizado para Big Data

## Slide 6

**HDFS — ¿Cómo vamos a guardar esa información?**

Mismo diagrama de stack Hadoop de la slide 5 (HDFS resaltado en rojo).

Texto (derecha):

**NameNode (Master)**
- Administra el sistema de archivos
- Guarda metadatos:
  - ❖ dónde están los archivos
  - ❖ cómo están divididos
- *No guarda los datos*

**DataNodes (Workers)**
- Almacenan los datos reales
- Ejecutan operaciones de lectura/escritura

## Slide 7

**HDFS — ¿Cómo vamos a guardar esa información?**

Diagrama de particionamiento por bloques. Arriba, un archivo de **600MB** (tres hojas grises apiladas) junto a íconos de tipos de datos: **Audio**, **Video**, **Imagen**, **Correo**.

Abajo, fila de 5 nodos de colores mostrando cómo se reparte el archivo en bloques:

| Nodo A | Nodo B | Nodo C | Nodo D | Nodo E |
|--------|--------|--------|--------|--------|
| 128MB | 128MB | 128MB | 128MB | 88MB |

(128×4 + 88 = 600MB)

Texto: "HDFS va separar los datos en tipos, según capacidad de información."

## Slide 8

**HDFS — ¿Cómo vamos a guardar esa información?**

Mismo esquema de la slide 7 (archivo 600MB + 5 nodos con 128/128/128/128/88 MB), pero ahora el **Nodo A aparece tachado con una gran X roja** (falla). Debajo, dentro de un recuadro redondeado, hay dos copias del bloque **Nodo A** replicadas en otros nodos.

Textos:
- "HDFS hace copias de la data y lo almacena entre diferentes nodos"
- "Método de replicación"
- **TOLERANTE A FALLOS!!!**

Ilustra que aunque un nodo falle, las réplicas garantizan disponibilidad.

## Slide 9

Slide divisor de sección. Número grande **02.**, ícono de checklist, título **MAPREDUCE**.

## Slide 10

**MapReduce — ¿Cómo vamos a procesar los datos?**

Visual (izquierda): mismo diagrama de stack Hadoop, ahora con la capa **MapReduce resaltada en recuadro rojo**.

Texto (derecha):
- MapReduce permite procesar grandes cantidades de datos en forma paralela
- MapReduce puede explotar las características de los sistemas de cómputo paralelos/distribuidos
- MapReduce es un framework altamente escalable
- MapReduce divide el procesamiento en dos fases fundamentales: la fase de mapeo "**Map**" (en rojo) y la fase de reducción "**Reduce**" (en rojo)

## Slide 11

**Flujo de MapReduce**

Diagrama de flujo vertical (de arriba hacia abajo), con flechas:
- **Input** (caja negra) → se ramifica a 3 cajas **División** (gris)
- Cada División → un **Mapper** (azul)
- Los 3 Mappers convergen en **Sort & Shuffle** (barra teal/verde-azulado)
- Sort & Shuffle → se ramifica a 3 **Reducer** (naranja)
- Los 3 Reducers convergen en **Output** (caja amarilla)

Nota resaltada (gris): "Los datos se particionan" (apunta a la fase de División).

## Slide 12

**Flujo de MapReduce**

Mismo diagrama de flujo (Input → División ×3 → Mapper ×3 → Sort & Shuffle → Reducer ×3 → Output).

Recuadro azul (destaca la fase Map):
"La fase **Map** se ejecuta en subtareas llamadas mappers. Estos se ejecutan en los nodos en que se encuentran los datos. Estos componentes son los responsables de generar pares clave-valor filtrando, agrupando, ordenando o transformando los datos originales. Los pares de datos intermedios, no se almacenan en HDFS."

## Slide 13

**Flujo de MapReduce**

Mismo diagrama de flujo.

Recuadro teal (destaca la fase de ordenación / Sort & Shuffle):
"En la fase de **ordenación**, los datos se ordenan y particionan de acuerdo con las claves obtenidas por los mappers. Los datos particionados y ordenados se envían a los procesos reductores."

## Slide 14

**Flujo de MapReduce**

Mismo diagrama de flujo.

Recuadro crema (destaca la fase Reduce):
"La fase **Reduce** gestiona la agregación de los valores producidos por todos los mappers del sistema (o por la fase shuffle) de tipo clave-valor en función de su clave. Por último, cada reducer genera su fichero de salida de forma independiente, generalmente escrito en HDFS."

## Slide 15

**Flujo de MapReduce**

Mismo diagrama de flujo.

Nota resaltada (amarilla, junto a Output): "Los datos se combinan".

## Slide 16

**Ejemplo: Conteo de Palabras**

Diagrama de flujo MapReduce (Input → División ×3 → Mapper ×3 → Sort & Shuffle → Reducer ×4 → Output). Aquí hay **4 Reducers**.

Recuadro de entrada (gris, junto a Input):
```
Manzana Plátano Mango
Tomate Mango Mango
Manzana Plátano Tomate
```

## Slide 17

**Ejemplo: Conteo de Palabras**

Mismo diagrama (Input → División ×3 → Mapper ×3 → Sort & Shuffle → Reducer ×4 → Output).

Ahora se muestra el **split de la entrada** en cada rama (entre División y Mapper):
- División 1: "Manzana Plátano Mango"
- División 2: "Tomate Mango Mango"
- División 3: "Manzana Plátano Tomate"

## Slide 18

**Ejemplo: Conteo de Palabras**

Mismo diagrama. Ahora se muestra la **salida de cada Mapper** (pares clave-valor):

- Mapper 1: `Manzana, 1` · `Plátano, 1` · `Mango, 1`
- Mapper 2: `Tomate, 1` · `Mango, 2`
- Mapper 3: `Manzana, 1` · `Plátano, 1` · `Tomate, 1`

## Slide 19

**Ejemplo: Conteo de Palabras**

Mismo diagrama. Ahora se muestra la **salida del Sort & Shuffle** (claves agrupadas con lista de valores), entrando a cada Reducer:

- `Manzana, [1,1]`
- `Plátano, [1,1]`
- `Mango, [1,2]`
- `Tomate, [1,1]`

## Slide 20

**Ejemplo: Conteo de Palabras**

Mismo diagrama. Ahora se muestra la **salida de cada Reducer** (agregación final):

- `Manzana, 2`
- `Plátano, 2`
- `Mango, 3`
- `Tomate, 2`

## Slide 21

**Ejemplo: Conteo de Palabras**

Slide resumen que muestra el **flujo completo con todos los datos superpuestos** en cada etapa:

- Input: "Manzana Plátano Mango / Tomate Mango Mango / Manzana Plátano Tomate"
- Divisiones: "Manzana Plátano Mango" | "Tomate Mango Mango" | "Manzana Plátano Tomate"
- Salida Mappers: (Manzana,1)(Plátano,1)(Mango,1) | (Tomate,1)(Mango,2) | (Manzana,1)(Plátano,1)(Tomate,1)
- Sort & Shuffle: Manzana,[1,1] · Plátano,[1,1] · Mango,[1,2] · Tomate,[1,1]
- Salida Reducers: Manzana,2 · Plátano,2 · Mango,3 · Tomate,2
- Output

## Slide 22

Slide divisor de sección. Número grande **03.**, ícono de checklist, título **YARN**.

## Slide 23

**YARN Yet Another Resource Negotiator — ¿Qué recursos o hardware vamos a utilizar?**

Visual (izquierda): mismo diagrama de stack Hadoop, con la capa **YARN resaltada en recuadro rojo**.

Texto (derecha):
- YARN es un gestor de recursos y aplicaciones que pretende extender el procesamiento en los clústeres Hadoop más allá del modelo MapReduce
- Yarn incluye dos aspectos fundamentales:
  - Gestión de recursos
  - Planificación y monitorización de tareas

## Slide 24

**YARN Yet Another Resource Negotiator — ¿Qué recursos o hardware vamos a utilizar?**

Mismo diagrama de stack (YARN resaltado en rojo).

Texto (derecha):
Recursos con las cuales contamos:
- Unidades de almacenamiento
- Memoria
- CPU

"El YARN asigna los recursos a las tareas, según sea necesario y que estén disponibles en ese momento. Administra un cluster"

## Slide 25

**YARN Yet Another Resource Negotiator — ¿Qué recursos o hardware vamos a utilizar?**

Idéntica a la slide 24 (mismo diagrama, mismos recursos: almacenamiento, memoria, CPU). Única diferencia: la última línea remata en mayúsculas — "Administra un **CLUSTER**".

## Slide 26

**Clúster**

Visual (izquierda): diagrama de arquitectura de clúster (fuente GeeksforGeeks). Arriba, un **Master** (monitor + torre de servidor) con dos recuadros verdes conectados: **Name Node** y **Resource Manager**. El Master se ramifica hacia abajo a 3 nodos **Slave** (cubos 3D azules), cada uno conteniendo: **Data Node** (verde), **Node Manager** (rojo), y cajitas **Map** y **Reduce**.

Texto (derecha):
"Un clúster es un conjunto de computadoras conectadas que trabajan como un solo sistema para procesar grandes volúmenes de datos."

**Tipos de nodos**
❑ **Nodo maestro (Master Node)**
Es el que coordina todo el clúster.
Funciones:
- Gestiona recursos
- Controla dónde están los datos
- Orquesta los procesos

*No está pensado para procesar datos masivamente*

## Slide 27

**Cluster**

Mismo diagrama de arquitectura de clúster (Master con Name Node y Resource Manager → 3 Slaves con Data Node / Node Manager / Map / Reduce).

Texto (derecha):
"Un cluster es un conjunto de computadoras conectadas que trabajan como un solo sistema para procesar grandes volúmenes de datos."

**Tipos de nodos**
❑ **Nodos trabajadores (Worker Nodes)**
Son los que hacen el trabajo pesado.
Funciones:
- Procesan datos
- Almacenan datos
- Ejecutan tareas

*Aquí ocurre el "cómputo real"*

## Slide 28

**Cluster — ¿Qué se ejecuta dentro de los nodos?**

Mismo diagrama de arquitectura de clúster.

Texto (derecha):
"Los nodos son infraestructura, pero dentro corre software"

**En el nodo maestro:**
- HDFS (NameNode)
- YARN (ResourceManager)

**En cada nodo worker:**
- DataNode (almacenamiento)
- NodeManager (ejecución de tareas)

## Slide 29

**YARN — ¿Qué recursos o hardware vamos a utilizar?**

Visual (izquierda): diagrama de componentes YARN. Un **Resource Manager** (verde) arriba, conectado por líneas punteadas a 3 **Node Manager** (cabecera roja, cuerpo amarillo). Cada Node Manager contiene **Containers** (elipses azules); el primer Node Manager además contiene un **Application Master** (elipse naranja).

Texto (derecha), cuatro recuadros de colores:

**RESOURCE MANAGER** (verde)
- Corre en el nodo maestro
- Controla la gestión de recursos del sistema
- Introduce *Schedulers* para asignar las tareas entre los distintos nodos
- Acepta envíos de tareas por parte de los clientes y gestiona la ejecución

**NODE MANAGER** (amarillo)
- Corre en los nodos workers
- Controla los recursos locales de cada nodo
- En cada uno de estos nodos se ejecuta un container
- Recibe las tareas que les va asignando el ResourceManager
- Manda información al RM sobre el estado del nodo

**APPLICATION** (naranja)
- Es un proceso único que se lanza cada vez que envías una aplicación a YARN
- Pide recursos al ResourceManager
- Cuando los obtiene, ordena a los NodeManagers que arranquen containers para ejecutar tareas
- Monitorea el progreso de esas tareas

**CONTAINER** (azul)
- Un container es la unidad mínima de recursos que el clúster asigna para ejecutar una tarea.
- Contiene CPU, Memoria y Permisos

## Slide 30

**ANALOGÍA**

Mismo diagrama de componentes YARN (Resource Manager → 3 Node Manager con Containers y un Application Master). A la derecha, recuadros de colores con íconos (edificio/administrador, recepcionista con auriculares, persona con portapapeles, sillón/lámpara).

Analogía de un hotel:

**RESOURCE MANAGER**: Es el administrador del hotel (decide en qué habitaciones se hospedan los huéspedes)

**NODE MANAGER**: Es el recepcionista de cada piso (habilita las habitaciones en su área).

**APPLICATION**: Es el organizador de un evento (pide habitaciones para su grupo).

**CONTAINER**: una habitación del hotel (donde se hospedan los asistentes, o sea, las tareas).

## Slide 31

Slide divisor de sección. Número grande **04.**, ícono de checklist, título **INTERFACES**.

## Slide 32

**Clúster – Interfaces Web**

Visual (izquierda): captura de pantalla de la **consola de Google Cloud → Dataproc → Clústeres → cluster-14e6 → Interfaces**. Muestra:
- Barra superior de Google Cloud ("My First Project"), buscador.
- Menú lateral: Descripción general, Notebooks/IDE (BigQuery Studio, Workbench), Clústeres (Clústeres, Trabajos, Flujos de trabajo, Políticas de escalado), Sin servidores (Lotes, Sesiones interactivas, Plantillas de sesión), Servicios de Metastore, Servicios públicos.
- Un banner de advertencia: "Failed to validate permissions required for default service account..." (error de permisos del service account).
- Detalles del clúster: Nombre = cluster-14e6, UUID = 21705bc8-9e2d-4e08-99da-cead91838f8d, Tipo = Clúster de Dataproc, Estado = En ejecución.
- Pestaña "Interfaces web" activa, con "Túnel SSH" y **Puerta de enlace del componente** listando enlaces: YARN ResourceManager, MapReduce Job History, Spark History Server, HDFS NameNode, YARN Application Timeline, Tez, Jupyter, JupyterLab.

Texto (derecha, recuadro naranja):
**HDFS NameNode** — Sirve para:
- Ver todos los archivos y carpetas que has guardado en HDFS.
- Revisar el uso de espacio en disco en el clúster.
- Ver en qué DataNodes están almacenados los bloques de un archivo.
- Monitorear el estado de los DataNodes (salud, capacidad, bloques replicados, bloques perdidos).

Clic en: *<Nombre del cluster>* → Interfaz Web → HDFS NameNode

## Slide 33

**HDFS NameNode**

(Fragmento de texto arrastrado desde la slide previa en el margen superior: "el hostname interno de cada worker (cluster-14e6-w-0 y cluster-14e6-w-1).")

Visual (izquierda): captura de la **interfaz web del HDFS NameNode (Hadoop)** del cluster-14e6. Barra azul con nombre del cluster; menú verde: Hadoop, Overview, Datanodes, Datanode Volume Failures, Snapshot, Startup Progress, Utilities.

**Overview** 'cluster-14e6-m.us-east1-d.c.infra-voyage-469707-g8.internal.:8020' (✔active)

Tabla de metadatos:
| Campo | Valor |
|-------|-------|
| Started | Mon Sep 01 12:57:00 -0500 2025 |
| Version | 3.3.6, r10b0346b9231a332e4cdff0a3ab87adfce2da9c2 |
| Compiled | Wed Aug 05 15:48:00 -0500 2025 by bigtop from dataproc-branch-3.3.6 |
| Cluster ID | CID-dbdc08cf-b76c-4123-88d7-8d221ad7d772 |
| Block Pool ID | BP-1225135396-10.142.0.25-1756705178418 |

**Summary**: Security is off. Safemode is off. 40 files and directories, 0 blocks (0 replicated blocks, 0 erasure coded block groups) = 40 total filesystem object(s). Heap Memory used 119.86 MB of 172.92 MB Heap Memory. Max Heap Memory is 1.54 GB. Non Heap Memory used 81.41 MB de 83.92 MB.

Tabla de capacidad:
| Métrica | Valor |
|---------|-------|
| Configured Capacity | 97.96 GB |
| Configured Remote Capacity | 0 B |
| DFS Used | 80 KB (0%) |
| Non DFS Used | 31.25 GB |
| DFS Remaining | 62.49 GB (63.79%) |
| Block Pool Used | 80 KB (0%) |
| DataNodes usages% (Min/Median/Max/stdDev) | 0.00% / 0.00% / 0.00% / 0.00% |

Texto (derecha, recuadro azul):
El NameNode está activo. Es el servicio que administra el sistema de archivos HDFS.
- **Configured Capacity:** Capacidad total del HDFS (≈ 98 GB configurados en tu clúster).
- **DFS Used:** Uso DFS (archivos en HDFS).
- **Non DFS Used:** Uso de Non DFS
- **DFS Remaining:** DFS restante
- Estado de los DataNodes

## Slide 34

**Clúster – Interfaces Web**

Visual (izquierda): misma captura de la consola de Google Cloud → Dataproc → Interfaces web que la slide 32 (mismos enlaces de Puerta de enlace del componente).

Texto (derecha, recuadro naranja):
**YARN ResourceManager** — Sirve para:
- Ver el estado de las aplicaciones que corren en YARN (ej. Spark jobs, MapReduce jobs).
- Monitorear cuántos recursos (memoria, vCores) están siendo usados por cada aplicación.
- Ver la cola de trabajos (pendientes, en ejecución, terminados, fallidos).
- Consultar los NodeManagers (nodos workers) y los contenedores que tienen asignados.

Clic en: *<Nombre del cluster>* → Interfaz Web → YARN ResourceManager

## Slide 35

**YARN ResourceManager**

Visual (izquierda): captura de la **interfaz web del YARN ResourceManager (Hadoop)**, ruta "infra-voyage-469707-g8 > cluster-14e6", logeado como dr.who. Título "Nodes of the cluster". Logo de Hadoop (elefante amarillo). Menú lateral: Cluster (About, Nodes, Node Labels, Applications: NEW, NEW_SAVING, SUBMITTED, ACCEPTED, RUNNING, FINISHED, FAILED, KILLED; Scheduler), Tools.

**Cluster Metrics**: Apps Submitted 0, Apps Pending 0, Apps Running 0, Apps Completed 0, Containers Running 0, Used Resources <memory:0 B, vCores:0>, **Total Resources <memory:12.80 GB, vCores:4>** (resaltado en rojo), Reserved Resources <memory:0 B, vCores:0>, Physical Mem Used % 16, Physical VCores Used % 0.

**Cluster Nodes Metrics**: **Active Nodes 2** (resaltado en azul), Decommissioning/Decommissioned/Lost/Unhealthy/Rebooted/Shutdown Nodes = 0.

**Scheduler Metrics**: Capacity Scheduler, [memory-mb (unit=Mi), vcores], Minimum Allocation <memory:1, vCores:1>, Maximum Allocation <memory:6554, vCores:2>.

Tabla de nodos (2 filas, resaltada la columna **Node Address** en verde):
| Rack | Node State | Node Address | Last health-update | Containers | Mem Used | Mem Avail | Phys Mem Used % | VCores Used | VCores Avail | Version |
|------|-----------|--------------|--------------------|-----------|----------|-----------|-----------------|-------------|--------------|---------|
| /default-rack | RUNNING | cluster-14e6-w-0.us-east1-d...:8026 | Mon Sep 01 18:20:29 +0000 2025 | 0 | 0 B | 6.40 GB | 16 | 0 | 2 | 3.3.6 |
| /default-rack | RUNNING | cluster-14e6-w-1.us-east1-d...:8026 | Mon Sep 01 18:20:28 +0000 2025 | 0 | 0 B | 6.40 GB | 16 | 0 | 2 | 3.3.6 |

Showing 1 to 2 of 2 entries.

Leyenda inferior (con recuadros de color):
- **Total Resources** (rojo): nos muestra la suma de la memoria y CPU de tus 2 nodos workers.
- **Active Nodes** (azul): Nos muestra los 2 Node Managers (en los workers) están activos y reportando.
- **Node Address** (verde): Muestra el hostname interno de cada worker (cluster-14e6-w-0 y cluster-14e6-w-1).

## Slide 36

**Conclusiones**

Tres puntos numerados (cada uno entre corchetes):

01. MapReduce es un modelo robusto y escalable para dividir grandes volúmenes de datos en tareas de mapeo y reducción, aprovechando la computación distribuida.

02. YARN actúa como el gestor de recursos y aplicaciones de Hadoop, permitiendo ejecutar múltiples frameworks (no solo MapReduce) en el mismo clúster.

03. Los componentes de YARN (Resource Manager, Node Managers, Application Master y Containers) trabajan de forma coordinada para asignar recursos y ejecutar aplicaciones de manera eficiente.

## Slide 37

Slide de cierre (decorativa): logo UTEC sobre fondo cian con patrón de flechas hexagonales. Sin contenido textual.
