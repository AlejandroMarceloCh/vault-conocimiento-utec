---
curso: BIGDATA
titulo: 05 - Semana 3/Semana 3 Laboratorio Google Cloud
slides: 34
fuente: 05 - Semana 3/Semana 3 Laboratorio Google Cloud.pdf
---

## Slide 1

Portada. Título grande "Laboratorio" con subtítulo "Semana 3". Fondo cian corporativo UTEC con foto decorativa del edificio UTEC en concreto. Logo UTEC y lema "Reinventa el mundo" (chrome decorativo).

## Slide 2

**Objetivo de la sesión**

Lista dentro de un marco tipo corchetes:

1. **Comprender** las principales soluciones de almacenamiento y analítica en la nube de Google Cloud.
2. **Identificar** cuándo usar cada servicio dentro de una arquitectura de datos.
3. **Aplicar** los conceptos mediante la creación de un bucket y un clúster.

## Slide 3

**Contenido de la sesión**

Cuatro bloques numerados en cajas con corchetes:

| # | Tema |
|----|------|
| 01. | Soluciones de Almacenamiento |
| 02. | Soluciones de Analítica |
| 03. | Creación de un bucket |
| 04. | Creación de un clúster |

## Slide 4

Slide divisoria de sección. Número grande "01." dentro de corchetes junto a un ícono de portapapeles con checklist. Título: **Soluciones de Almacenamiento**.

## Slide 5

Captura de la consola de Google Cloud, panel **Storage** ("Store long-term, short-term, VM, and Filestore securely"). Tabla con columnas Name / Description. Fila **Cloud Storage** resaltada con recuadro naranja (marcada con estrella azul = favorito).

Tabla de servicios de Storage mostrados:

| Name | Description |
|------|-------------|
| Cloud Storage (★) | Enterprise-ready object storage |
| Filestore | Fully managed NFS server |
| Backup and DR | Simplified backup administration |
| Storage Transfer | Secure and flexible way to move data |
| Parallelstore | Managed parallel file system |
| Managed Lustre | Parallel file system for AI/ML and HPC |
| NetApp Volumes | Fully Managed File and Block Storage |

Cuadro lateral naranja (explicación del servicio resaltado, Cloud Storage):
- **Almacenamiento de archivos en la nube (tipo data lake).**
- Función: Guardar y acceder a datos masivos desde cualquier servicio.
- Cuando usarlo: Para analítica, backups y datos de entrada/salida.

## Slide 6

Misma captura de la tabla Storage; ahora la fila resaltada en naranja es **Filestore** (Fully managed NFS server).

Cuadro lateral naranja:
- **Disco compartido tipo red (NFS)**
- Función: Permitir que varias máquinas accedan a los mismos archivos.
- Cuando usarlo: Apps que necesitan filesystem tradicional.

## Slide 7

Misma tabla Storage; fila resaltada **Backup and DR** (Simplified backup administration).

Cuadro lateral naranja:
- **Backup and DR**
- Función: Crear copias y restaurar sistemas ante fallas.
- Cuando usarlo: Continuidad del negocio y cumplimiento.

## Slide 8

Misma tabla Storage; fila resaltada **Storage Transfer** (Secure and flexible way to move data).

Cuadro lateral naranja:
- **Herramienta de transferencia de datos**
- Función: Mover datos desde on-premise u otras nubes.
- Cuando usarlo: Migraciones o cargas masivas programadas.

## Slide 9

Misma tabla Storage; fila resaltada **Parallelstore** (Managed parallel file system).

Cuadro lateral naranja:
- **Sistema de archivos de alto rendimiento**
- Función: Procesar grandes volúmenes de datos en paralelo.
- Cuando usarlo: Simulaciones o cargas intensivas (HPC).

## Slide 10

Misma tabla Storage; fila resaltada **Managed Lustre** (Parallel file system for AI/ML and HPC).

Cuadro lateral naranja:
- **Filesystem HPC ultra rápido**
- Función: Soportar cargas pesadas de IA/ML y cómputo.
- Cuando usarlo: Entrenamiento ML o procesamiento intensivo.

## Slide 11

Misma tabla Storage; fila resaltada **NetApp Volumes** (Fully Managed File and Block Storage).

Cuadro lateral naranja:
- **Almacenamiento empresarial avanzado.**
- Función: Ofrecer features como snapshots y replicación.
- Cuando usarlo: Sistemas legacy o aplicaciones corporativas.

## Slide 12

Slide divisoria de sección. Número grande "02." dentro de corchetes con ícono de portapapeles. Título: **Soluciones de Analítica**.

## Slide 13

Captura de la consola GCP, panel **Analytics** ("Collect, store, process, and analyze large amounts of data"). Tabla con columnas Name / Description. Fila **Pub/Sub** resaltada en naranja. (En esta lista, Managed Apache Spark aparece marcado con estrella azul como favorito.)

Tabla de servicios de Analytics:

| Name | Description |
|------|-------------|
| Pub/Sub | Global real-time messaging |
| Dataflow | Streaming analytics service |
| Composer | Managed workflow orchestration service |
| Managed Apache Spark (★) | Managed Apache Spark and other OSS components |
| Alteryx Designer Cloud | Visual data wrangling |
| Data Fusion | Data pipeline management |
| Looker | Enterprise BI and Analytics |
| Healthcare | Healthcare data storage and processing |
| Elastic Cloud (P) | Data power to uncover actionable intelligence |
| Databricks (P) | Platform for data, analytics, and AI workloads |
| Earth Engine | Planetary-scale platform for Earth science |

Cuadro lateral naranja (Pub/Sub):
- **Servicio de mensajería en tiempo real**
- Función: Enviar y recibir eventos entre sistemas.
- Cuando usarlo: Streaming, eventos, arquitecturas desacopladas.

## Slide 14

Misma tabla Analytics; fila resaltada **Dataflow** (Streaming analytics service).

Cuadro lateral naranja:
- **Procesamiento de datos en tiempo real o Batch**
- Función: Transformar y procesar grandes volúmenes de datos.
- Cuando usarlo: ETL/ELT y pipelines de streaming.

## Slide 15

Misma tabla Analytics; fila resaltada **Composer** (Managed workflow orchestration service).

Cuadro lateral naranja:
- **Orquestador de workflows (basado en Airflow)**
- Función: Automatizar y programar pipelines de datos.
- Cuando usarlo: Coordinar procesos ETL complejos.

## Slide 16

Misma tabla Analytics; fila resaltada **Managed Apache Spark** (Managed Apache Spark and other OSS components).

Cuadro lateral naranja:
- **Servicio gestionado de Spark**
- Función: Procesar datos distribuidos a gran escala.
- Cuando usarlo: Big Data, ML y procesamiento masivo.

## Slide 17

Misma tabla Analytics; fila resaltada **Alteryx Designer Cloud** (Visual data wrangling).

Cuadro lateral naranja:
- **Herramienta visual de preparación de datos**
- Función: Limpiar y transformar datos sin programar.
- Cuando usarlo: Usuarios de negocio (low-code).

## Slide 18

Misma tabla Analytics; fila resaltada **Data Fusion** (Data pipeline management).

Cuadro lateral naranja:
- **Plataforma para construir pipelines de datos**
- Función: Integrar y mover datos entre sistemas.
- Cuando usarlo: Integración sin mucho código (ETL visual).

## Slide 19

Misma tabla Analytics; fila resaltada **Looker** (Enterprise BI and Analytics).

Cuadro lateral naranja:
- **Plataforma de BI y analítica.**
- Función: Crear dashboard y explorar datos.
- Cuando usarlo: Reportes y toma de decisiones.

## Slide 20

Misma tabla Analytics; fila resaltada **Healthcare** (Healthcare data storage and processing).

Cuadro lateral naranja:
- **Plataforma para datos de salud**
- Función: Almacenar y procesar datos médicos.
- Cuando usarlo: Soluciones del sector salud.

## Slide 21

Slide divisoria de sección. Número grande "03." dentro de corchetes con ícono de portapapeles. Título: **Creación de un bucket en GCS**.

## Slide 22

**CREACIÓN DE BUCKET PASO A PASO**

Ruta de la solución (recuadro): `Storage – Cloud Storage - Buckets`

Tres capturas de la consola de creación de bucket colocadas de izquierda a derecha:

**PASO 1: NOMBRE ÚNICO CLUSTER** — Panel "Get Started". "Pick a globally unique, permanent name". Campo de nombre con valor `bucket-utec-bigdata-202604`. Tip: "Don't include any sensitive information". Sección "Labels (optional)". Botón Continue.

**PASO 2: TIPO DE LOCACION** — Panel "Choose where to store your data". Location type con opciones de radio:
- Multi-region (Highest availability across largest area)
- Dual-region (High availability and low latency across 2 regions)
- **Region** (seleccionado) — Lowest latency within a single region → desplegable `us-central1 (Iowa)`
  - Checkbox "Add cross-bucket replication via Storage Transfer Service"
- Zone (Lowest latency within a single zone)

**PASO 3: FORMA DE ALMACENAMIENTO** — Panel "Choose how to store your data". Location: us-central1 (Iowa), Location type: Region. Opciones de clase de almacenamiento:
- Autoclass (transición automática de objetos)
- **Set a default class** (seleccionado):
  - Rapid
  - **Standard** (seleccionado) — Best for short-term storage and frequently accessed data
  - Nearline (backups, < 1 vez/mes)
  - Coldline (disaster recovery, < 1 vez/trimestre)
  - Archive (preservación digital a largo plazo, < 1 vez/año)
- Checkbox "Enable Hierarchical namespace on this bucket" (optimizar para AI/ML y analítica, filesystem-like).

## Slide 23

**CREACIÓN DE BUCKET PASO A PASO**

Dos capturas:

**PASO 4: CONTROL DE ACCESO** — Panel "Choose how to control access to objects".
- Prevent public access: checkbox marcado "Enforce public access prevention on this bucket".
- Access control:
  - **Uniform** (seleccionado) — acceso uniforme por permisos a nivel de bucket (IAM), permanente tras 90 días. Nota informativa: "Your organization requires buckets to use the Uniform Bucket Level Access option."
  - Fine-grained (ACLs a nivel de objeto).
- Botón Continue.

**PASO 5: PROTECCIÓN DE DATOS** — Panel "Choose how to protect object data". Data protection:
- Checkbox marcado **Soft delete policy (For data recovery)**:
  - **Use default retention duration** (seleccionado) — 7 días por defecto.
  - Set custom retention duration.
- Object versioning (For version control) — desmarcado.
- Retention (For compliance) — desmarcado.
- Enlace desplegable "Data Encryption".

## Slide 24

**CREACIÓN DE BUCKET PASO A PASO**

**PASO 6: CREATE + FINALIZACIÓN**

Captura superior: lista de Buckets con el bucket creado:

| Name | Created | Location type | Location | Default storage class | Last modified | Public access | Access control | Protection |
|------|---------|---------------|----------|----------------------|---------------|---------------|----------------|------------|
| bucket-utec-bigdata-202604 | Apr 10, 2026, 6:17:11 PM | Region | us-central1 | Standard | Apr 10, 2026, 6:17:11 PM | Not public | Uniform | Soft Delete |

Captura inferior: vista del bucket `bucket-utec-bigdata-202604`. Encabezado con Location: us-central1 (Iowa), Storage class: Standard, Public access: Not public, Protection: Soft Delete. Pestañas: Objects, Configuration, Permissions, Protection, Lifecycle, Observability, Inventory Reports, Operations. Folder browser con el bucket; acciones Create folder / Upload / Transfer data. Mensaje "No rows to display" (bucket vacío).

## Slide 25

**CREACIÓN DE BUCKET MEDIANTE CLOUD SHELL**

Captura de la consola Google Cloud (proyecto "My First Project") con Cloud Storage > Buckets mostrando `bucket-utec-bigdata-202604` (creado Apr 10, 2026, 6:23:52 PM, Region, us-central1, Standard). Abajo, terminal Cloud Shell negro ejecutando el comando; aviso "Gemini CLI is available in Cloud Shell terminal". Salida: "Creating gs://bucket-utec-bigdata-202604/...".

Cuadro lateral naranja **CÓDIGO UTILIZADO**:

```bash
gcloud storage buckets create gs://bucket-utec-bigdata-202604 \
  --default-storage-class=STANDARD \
  --location=US-CENTRAL1 \
  --uniform-bucket-level-access \
  --public-access-prevention
```

## Slide 26

Slide divisoria de sección. Número grande "04." dentro de corchetes con ícono de portapapeles. Título: **Creación de un clúster en GCP**.

## Slide 27

**CREACIÓN DE CLÚSTER PASO A PASO**

Ruta de la solución (recuadro): `Analytics - Managed Apache Spark - Clusters`

Tres capturas:

Izquierda — Tarjeta "Cluster: Managed Service for Apache Spark (formerly known as Dataproc)". "Provision Apache Spark clusters and connect to underlying analytic data stores." "There are no clusters in the currently selected region(s). Create a cluster to get started." Botón **Create cluster**.

Centro — Panel "Define your cluster":
- Cluster Name: `cluster-3bcd`
- Region: `us-central1`, Zone: `us-central1-a`
- Cluster type: `Standard (1 master, N workers)`
- Number of workers: 2
- Checkbox "Enable Lightning Engine" (desmarcado)
- Versioning → Image Type and Version: `2.3-debian12`; Release Date: "First released on 06/09/2025". Botón Change.

Derecha — Panel "Advanced configurations (optional)" con secciones colapsables: Lakehouse and Clusters, Infrastructure, Security, Other. Enlaces "Equivalent command line" / "Equivalent REST" y "Hide configuration options".

## Slide 28

**CREACIÓN DE CLÚSTER PASO A PASO**

Dos capturas de configuración avanzada:

Izquierda — **Lakehouse and Clusters**:
- Autoscaling → Policy: None.
- Enhanced Flexibility Mode (EFM) — descripción; nota "An autoscaling policy must be selected to configure EFM."
- Network Configuration (colapsado).
- Dataproc Metastore → Selected project: My First Project; Metastore service: None.

Derecha — **Components**:
- Component Gateway: checkbox marcado "Enable component gateway".
- Optional components (checkboxes): Iceberg, Delta, Hudi, Docker, Trino, Flink (todos desmarcados); **Jupyter Notebook** (marcado), Hive WebHCat, Ranger (desmarcados); **ZooKeeper** (marcado), Solr, Zeppelin Notebook, Jupyter Kernel Gateway (desmarcados); **Pig** (marcado).

## Slide 29

**CREACIÓN DE CLÚSTER PASO A PASO**

Tres capturas de configuración de infraestructura:

Izquierda — **Infrastructure / Manager node** (YARN Resource Manager, HDFS NameNode, drivers). General purpose. Series: N4. Machine type: `n4-standard-2 (2 vCPU, 1 core, 8 GB memory)`. vCPU 2, Memory 8 GB. Primary disk size: 100 GB. Primary disk type: Hyperdisk Balanced. Number of local SSDs: 0. Local SSD Interface: SCSI.

Centro — **Worker nodes** (cada uno con YARN NodeManager y HDFS DataNode; replication factor = 2). General purpose. Series: N4. Machine type: `n4-standard-2 (2 vCPU, 1 core, 8 GB memory)`. vCPU 2, Memory 8 GB. Number of worker nodes: 2. Primary disk size: 100 GB. Primary disk type: Hyperdisk Balanced. Local SSDs: 0, SCSI.

Derecha — **Security / Project access**:
- Checkbox marcado "Enables the cloud-platform scope for this cluster".
- Encryption: **Google-managed encryption key** (seleccionado); Cloud KMS key.
- Toggles off: "Encrypt job argument data...", "Enable confidential computing".
- Personal Cluster Authentication: Enable (off).
- Secure Multi Tenancy: Enable (off).

## Slide 30

**CREACIÓN DE CLÚSTER PASO A PASO**

Tres capturas del apartado Other + Metadata + Scheduled stop:

Izquierda — **Other**:
- Internal IP only: checkbox marcado "Configure all instances to have only internal IP addresses".
- Labels: "Add labels".
- Cluster properties: "Add properties".
- Initialization actions: "Add initialization action".

Centro — **Custom cluster metadata** + **Scheduled deletion**:
- Add metadata.
- Scheduled deletion: checkbox marcado "Delete on a fixed time schedule"; opción seleccionada **Delete after elapsed time since creation**; Timeout: 2 Hours. → "The cluster will be deleted 2 hours after creation".
- Scheduled stop (checkboxes desmarcados).

Derecha — **Scheduled stop**:
- Checkbox marcado "Stop on a fixed time schedule"; opción seleccionada **Stop after elapsed time since creation**; Timeout: 1 Hours. → "The cluster will be stopped an hour after creation".
- Cloud Storage staging bucket: `bucket-utec-bigdata-202604`.

## Slide 31

**CREACIÓN DE BUCKET PASO A PASO** (título; realmente muestra el clúster creado)

Captura de la lista de **Clusters**. Barra con acciones Create cluster / Refresh / Start / Stop / Delete / Regions / "5 recommended alerts". Banner de error rojo: "Sorry, the server was not able to fulfill your request."

Tabla:

| Name | Status | Region | Zone | Base image version | Engine | Total worker nodes | Flexible VMs? | Scheduled deletion | Scheduled stop | Cloud Storage staging bucket |
|------|--------|--------|------|--------------------|--------|--------------------|--------------|--------------------|----------------|------------------------------|
| cluster-3bcd | ✅ Running | us-central1 | us-central1-a | 2.3.28-debian12 | Default | 0 | No | On | On | bucket-utec-bigdata-202604 |

## Slide 32

**CREACIÓN DE CLÚSTER MEDIANTE CLOUD SHELL**

Captura de la consola Managed Apache Spark / Clusters con `cluster-3bcd` en estado Running (us-central1, us-central1-a, 2.3.28-debian12, Default, 2 workers, staging bucket bucket-utec-bigdata-202604). Debajo terminal Cloud Shell ejecutando el comando gcloud dataproc; salida con warnings (Auto Zone recommendation, permisos del service account, firewall) y finalmente "Waiting for cluster creation operation...done. Created [.../clusters/cluster-3bcd] Cluster placed in zone [us-central1-a]."

Cuadro lateral naranja **CÓDIGO UTILIZADO**:

```bash
gcloud dataproc clusters create cluster-3bcd --enable-component-gateway \
  --bucket bucket-utec-bigdata-202604 --region us-central1 --no-address \
  --zone us-central1-a --master-machine-type n4-standard-2 \
  --master-boot-disk-type hyperdisk-balanced --master-boot-disk-size 100 \
  --num-workers 2 --worker-machine-type n4-standard-2 \
  --worker-boot-disk-type hyperdisk-balanced --worker-boot-disk-size 100 \
  --image-version 2.3-debian12 \
  --properties spark:spark.dataproc.engine=default,spark:spark.dataproc.lightningEngine.runtime=default \
  --optional-components JUPYTER,ZOOKEEPER,PIG --max-age 7200s \
  --scopes 'https://www.googleapis.com/auth/cloud-platform' \
  --project project-c845ec52-f5b1-4857-9a4
```

## Slide 33

**Conclusiones**

Tres puntos numerados:

01. Se presentó una visión general de los servicios de analítica en Google Cloud, entendiendo su rol dentro del ecosistema de datos.

02. Se profundizó en soluciones de almacenamiento, clave como base para cualquier arquitectura de datos en la nube.

03. La creación del bucket y clúster permitió llevar la teoría a la práctica, entendiendo la implementación real de un entorno de procesamiento.

## Slide 34

Slide de cierre. Logo UTEC centrado sobre fondo cian con patrón geométrico decorativo. Sin contenido textual adicional (decorativa).
