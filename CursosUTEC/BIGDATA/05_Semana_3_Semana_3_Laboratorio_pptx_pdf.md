---
curso: BIGDATA
titulo: 05 - Semana 3/Semana 3 - Laboratorio__pptx
slides: 34
fuente: 05 - Semana 3/Semana 3 - Laboratorio__pptx.pdf
---

## Slide 1

Portada. Título grande "HDFS en GCP" y subtítulo "Semana 2". Imagen decorativa del edificio UTEC.

## Slide 2

**Objetivo de la sesión**

- **Comprender** cómo se gestiona el almacenamiento en Google Cloud Platform (GCP) y su integración con Hadoop.
- **Aprender** a crear y configurar un clúster Hadoop en GCP utilizando Dataproc.
- **Desarrollar** habilidades prácticas en el uso de comandos básicos de Linux y HDFS para interactuar con clústeres y sistemas distribuidos.

## Slide 3

**Contenido de la sesión** — tres bloques numerados:

- **01.** Almacenamiento en GCP
- **02.** Clúster Hadoop en GCP
- **03.** Comandos útiles

## Slide 4

Divisor de sección. **01. Almacenamiento en GCP** (icono de portapapeles).

## Slide 5

**Cloud Storage**

Captura de la consola de Google Cloud → Cloud Storage → Buckets, en el proyecto "My First Project". El panel lateral muestra: Descripción general, Buckets (seleccionado), Supervisión, Configuración, y bajo "Storage Intelligence": Conjuntos de datos de estadísticas y Configuración.

La tabla de buckets tiene columnas: Nombre, Fecha de creación, Tipo de ubicación, Ubicación, Clase de almacenamiento predeterminada, Última modificación, Acceso público, Control de acceso. El mensaje indica "No hay filas para mostrar."

En el centro hay una ilustración (marco con nube punteada) con el texto "Almacena y recupera tus datos / Para empezar, crea un bucket, un contenedor en el que puedes organizar y controlar el acceso a tus datos y archivos en Cloud Storage." con botones **Crear bucket** (azul) y "Seguir la guía de inicio rápido".

## Slide 6

**Cloud Storage: Comenzar**

Captura del formulario "Crear un bucket", panel "Comenzar":

- Campo de nombre del bucket con valor `bucket-utec-bigdata-2025-v1` ("Selecciona un nombre permanente globalmente único"). Sugerencia: No incluyas información sensible.
- Etiquetas (opcional). Botón **Continuar**.
- Resumen de secciones colapsadas:
  - **Elige dónde almacenar tus datos** → Ubicación: us (múltiples regiones en Estados Unidos); Tipo de ubicación: Multi-region.
  - **Elige cómo almacenar tus datos** → Clase de almacenamiento predeterminada: Standard; Espacio de nombres jerárquico: Inhabilitado.
  - **Elige cómo controlar el acceso a los objetos** → Prevención del acceso público: Sí; Control de acceso: Uniforme.
  - **Elige cómo proteger los datos de objeto** → Política de eliminación no definitiva: Predeterminada; Controles de versiones de objetos: Inhabilitado; Política de retención del bucket: Inhabilitado; Retención de objetos: Inhabilitado; Tipo de encriptación: Administrada por Google.

Panel derecho "Información útil → Precios de ubicación", tabla:

| Elemento | Costo |
|----------|-------|
| us (múltiples regiones en Estados Unidos) | $0.026 por GB al mes |
| Con replicación predeterminada | $0.020 por GB escrito |

Configuración actual: Multi-region/Standard. Botones **Crear** / Cancelar.

## Slide 7

**Cloud Storage: Dónde**

Captura del paso "Elige dónde almacenar tus datos" (Comenzar ya validado ✓, Nombre: bucket-utec-bigdata-2025-v1). Texto: "Esta opción define la ubicación geográfica de tus datos y afecta el costo, el rendimiento y la disponibilidad. No se puede cambiar más adelante."

**Tipo de ubicación** (radios):
- Multi-region — Máxima disponibilidad en el área más amplia.
- Dual-region — Alta disponibilidad y baja latencia en 2 regiones.
- **Region** (seleccionado) — Latencia mínima dentro de una sola región. Dropdown: `us-east1 (Carolina del Sur)`.
- Checkbox "Agregar replicación entre buckets a través del Servicio de transferencia de almacenamiento".

Panel derecho: Configuración actual: Region/Standard. Tabla: us-east1 (Carolina del Sur) → $0.020 por GB al mes.

## Slide 8

**Cloud Storage: Cómo**

Captura del paso "Elige cómo almacenar tus datos". Explica que la clase de almacenamiento determina costos, recuperación y operaciones.

Opciones (radios):
- Autoclass — transición automática entre clases Estándar/Nearline según actividad. Recomendado si la frecuencia de uso es impredecible.
- **Configurar una clase predeterminada** (seleccionado), con sub-opciones:
  - **Standard** (seleccionado) — mejor para almacenamiento a corto plazo y datos de acceso frecuente.
  - Nearline — copias de seguridad, acceso menos de una vez al mes.
  - Coldline — recuperación ante desastres, acceso menos de una vez por trimestre.
  - Archive — conservación digital a largo plazo, acceso menos de una vez al año.
- Checkbox "Habilita el espacio de nombres jerárquico en este bucket" (para IA/AA y estadísticas).

Botón **Continuar**.

## Slide 9

**Cloud Storage: Controlar**

Captura del paso "Elige cómo controlar el acceso a los objetos".

- **Impedir el acceso público** — "Restringe el acceso público a los datos a través de Internet. Esto evitará que el bucket se use para el hosting web." Checkbox marcado: "Aplicar la prevención de acceso público a este bucket".
- **Control de acceso** (radios):
  - **Uniforme** (seleccionado) — acceso uniforme a todos los objetos mediante permisos a nivel de bucket (IAM). Se aplica de forma permanente después de 90 días.
  - Preciso — acceso a objetos individuales mediante permisos a nivel de objeto (LCA) además de IAM.

Debajo, resumen de "Elige cómo proteger los datos de objeto" y botón **Crear**.

## Slide 10

**Cloud Storage: Proteger**

Captura del paso "Elige cómo proteger los datos de objeto". "Tus datos siempre están protegidos con Cloud Storage, pero también puedes elegir entre estas opciones adicionales."

**Protección de datos**:
- Checkbox marcado: **Política de eliminación no definitiva (para la recuperación de datos)** — el bucket y objetos se conservan un período tras borrarse. Sub-opciones:
  - **Usar la duración de retención predeterminada** (seleccionado) — 7 días por defecto.
  - Establecer duración de retención personalizada.
- Checkbox: Control de versiones de objetos (para el control de versión).
- Checkbox: Retención (para el cumplimiento).
- Enlace desplegable "Encriptación de datos".

## Slide 11

**Cloud Storage**

Captura con diálogo modal emergente "**Se impedirá el acceso público**": "Este bucket está configurado para evitar la exposición de tus datos en la Internet pública. Mantén habilitado este parámetro de configuración, a menos que tengas un caso de uso que requiera acceso público (como el alojamiento estático de un sitio web)." Checkbox marcado "Aplicar la prevención de acceso público a este bucket" y "No volver a mostrar este mensaje". Botones Cancelar / **Confirmar**.

Al fondo, el resumen del bucket con todos los pasos validados (✓) y estado "Procesando...".

## Slide 12

**Cloud Storage**

Captura de la lista de Buckets ya con el bucket creado. Fila:

| Nombre | Fecha de creación | Tipo de ubicación | Ubicación | Clase | Última modificación | Acceso público | Control de acceso |
|--------|-------------------|-------------------|-----------|-------|--------------------|----------------|-------------------|
| bucket-utec-bigdata-2025-v1 | 29 ago 2025 16:11:32 | Region | us-east1 | Standard | 29 ago 2025 16:11:32 | No público | Uniforme |

Toast inferior: "Se creó el bucket bucket-utec-bigdata-2025-v1".

## Slide 13

Divisor de sección. **02. Clúster Hadoop en GCP** (icono de portapapeles).

## Slide 14

**Creación de Clúster con Dataproc**

Captura de la consola Dataproc → Clústeres. Panel lateral: Descripción general; Notebooks/IDE (BigQuery Studio, Workbench); Clústeres (Clústeres, Trabajos, Flujos de trabajo, Políticas de escalado automático); Sin servidores (Lotes, Sesiones interactivas, Plantillas de sesión); Servicios de Metastore (Metastore, Federación); Servicios públicos (Intercambio de componentes).

Barra de acciones: Create cluster, Actualizar, Iniciar, Detener, Borrar, Regiones, "+5 alertas recomendadas".

Tarjeta central "Clúster / **Cloud Dataproc**": "Google Cloud Dataproc te permite aprovisionar clústeres de Apache Hadoop y conectarte a almacenes de datos de análisis subyacentes. No hay clústeres en las regiones de Cloud Dataproc seleccionadas actualmente. Crea un clúster para comenzar." Botón **Create cluster**.

## Slide 15

**Clúster: Configuración**

Captura de "Crea un clúster de Dataproc en Compute Engine". Wizard lateral con pasos: Configura el clúster (activo), Configura los nodos (opcional), Personaliza el clúster (opcional), Administrar seguridad (opcional). Botones **Crear** / Cancelar; enlaces "Línea de comandos equivalente" y "REST equivalente".

- **Nombre** → Nombre del clúster: `cluster-ec8d`.
- **Ubicación** → Región: `us-central1`; Zona: `Cualquiera`.
- **Tipo de clúster** (radios):
  - **Estándar (1 principal, N trabajadores)** (seleccionado).
  - Un solo nodo (1 principal, 0 trabajadores) — nodo que funciona como principal y trabajador; ideal para pequeña escala o prueba de concepto.
  - Alta disponibilidad (3 principales, N trabajadores) — operaciones YARN y HDFS ininterrumpidas ante fallas.
- **Control de versiones** → Tipo de imagen y versión: `2.2-debian12`; Fecha de lanzamiento; botón Cambiar.
- Comienza sección "Mejoras en el rendimiento de Spark".

## Slide 16

**Configuración: Control de Versiones**

Captura (scroll dentro del mismo wizard):

- **Control de versiones** → Tipo de imagen y versión: `2.2-debian12`; Fecha de lanzamiento (Lanzamiento de la primera); botón Cambiar.
- **Mejoras en el rendimiento de Spark** (checkboxes, todos sin marcar):
  - Enable advanced optimizations
  - Enable advanced execution layer
  - Enable Google Cloud Storage caching
- **Ajuste de escala automático** → Política: `None`.
- **Modo de flexibilidad mejorada** — EFM administra datos aleatorios para minimizar retrasos al eliminar nodos. Modos: Shuffle de trabajador principal y Shuffle del sistema de archivos compatible con Hadoop (HCFS). Aviso: "An autoscaling policy must be selected to configure EFM."
- Sección colapsable "Configuración de red".

## Slide 17

**Configuración: Red**

Captura de la sección **Configuración de red**: "Establece la conectividad para las instancias de VM en el clúster."

- Radios: **Redes en este proyecto** (seleccionado) / Redes compartidas del proyecto host.
- Red principal: `default`; Subred; Etiquetas de red (network tags para reglas de firewall).
- **Dataproc Metastore** — Proyecto seleccionado: My First Project (botón Explorar); Servicio de almacén de metadatos: `Ninguno`.
- **Componentes** → Puerta de enlace del componente: checkbox marcado "Habilitar puerta de enlace de componentes" (acceso a interfaces web de componentes).
- Componentes opcionales (enlace Más información).

## Slide 18

**Configuración - Componentes**

Captura de la sección **Componentes**, "Componentes opcionales" (checkboxes):

- Hive WebHCat — sin marcar
- **Jupyter Notebook** — marcado ✓
- Zeppelin Notebook — sin marcar
- Trino, ZooKeeper, Ranger, Flink, Docker, Solr, Hudi, Iceberg, Delta — todos sin marcar

Arriba se ve el resto de Dataproc Metastore (Servicio de almacén de metadatos: Ninguno) y "Habilitar puerta de enlace de componentes" marcado.

## Slide 19

**Configuración nodo: principal node**

Captura de la sección **Nodo de administrador**: "Contiene el administrador de recursos YARN, HDFS NameNode y todos los controladores de trabajos."

- Pestañas: **De uso general** (seleccionado) / Con optimización de memoria.
- Serie: `N4` (tecnología CPU Emerald Rapids de Intel).
- Tipo de máquina: `n4-standard-2 (2 CPU virtuales, 1 núcleos, 8 GB de memoria)` → vCPU: 2, Memory: 8 GB.
- Enlace "Plataforma de CPU y GPU".
- Tamaño del disco principal: `100` GB; Primary disk type: `Hyperdisk Balanced Disk`.
- IOPS; Throughput; Cantidad de SSD locales: `0` x 375GB; Interfaz de SSD local: `SCSI`.

Debajo comienza sección **Nodos trabajadores**: "Cada uno contiene un NodeManager de YARN y un DataNode de HDFS. El factor de replicación de HDFS es 2."

## Slide 20

**Configuración nodo: workers nodes**

Captura de la sección **Nodos trabajadores** (factor de replicación HDFS = 2):

- Pestañas: **De uso general** (seleccionado) / Con optimización de memoria.
- Serie: `N4`.
- Tipo de máquina: `n4-standard-2 (2 CPU virtuales, 1 núcleos, 8 GB de memoria)` → vCPU: 2, Memory: 8 GB.
- **Number of worker nodes**: `2`.
- Tamaño del disco principal: `50` GB (campo resaltado en azul); Primary disk type: `Hyperdisk Balanced Disk`.
- IOPS; Throughput; Cantidad de SSD locales: `0` x 375GB; Interfaz de SSD local: `SCSI`.

Debajo comienza **Nodos trabajadores secundarios**: "Cada uno contiene un NodeManager de YARN. HDFS no se puede ejecutar en nodos trabajadores secundarios."

## Slide 21

**Configuración nodo: secondary nodes**

Captura de secciones:

- **Nodos trabajadores secundarios** — "Cada uno contiene un NodeManager de YARN. HDFS no se puede ejecutar en nodos trabajadores secundarios. Las VM de trabajador secundarias son interrumpibles de forma predeterminada. Las VMs interrumpibles y spot cuestan menos, pero se pueden cerrar en cualquier momento."
- **Usuario único** — crea el clúster en nodos de usuario único (acceso exclusivo a un servidor físico). Toggle "Habilitar" (desactivado).
- **VM protegida** — "Activa todos los ajustes para lograr la configuración más segura." Checkboxes (sin marcar): Activa el arranque seguro; Activa vTPM; Activar la supervisión de integridad.
- **Uso total de YARN** — tabla: Núcleos YARN: `4`; Memoria YARN: `13.74 GB`.

## Slide 22

**Personalizar: IP internas**

Captura del paso "Personaliza el clúster":

- **Solo IP internas** — checkbox marcado: "Configurar todas las instancias para tener solo direcciones IP internas."
- **Etiquetas** — pares clave-valor adjuntados al clúster para seguimiento. Botón "+ Agregar etiquetas".
- **Propiedades del clúster** — para agregar o modificar archivos de configuración al crear el clúster. Botón "+ Agregar propiedades".
- **Acciones de inicialización** — secuencias de comandos/ejecutables que Dataproc ejecuta al aprovisionar el clúster. Botón "+ Agregar acción de inicialización".
- **Metadatos personalizados del clúster** — botón "+ Agregar metadatos".

## Slide 23

**Personalizar: Acciones de inicialización**

Captura (scroll) del mismo paso:

- **Propiedades del clúster** → botón "+ Agregar propiedades".
- **Acciones de inicialización** → botón "+ Agregar acción de inicialización".
- **Metadatos personalizados del clúster** → botón "+ Agregar metadatos".
- **Eliminación programada** — evita cobros por clúster inactivo. Checkboxes (sin marcar): "Borrar según el cronograma de fechas establecido"; "Borrar luego de un tiempo de inactividad del clúster sin trabajos enviados".
- **Bucket de etapa de pruebas de Cloud Storage** — campo vacío + botón Explorar; se usará para almacenar dependencias de trabajos, resultados del controlador y archivos de configuración de clústeres.

## Slide 24

**Personalizar: Selección de bucket**

Igual que la anterior pero con un panel modal lateral derecho "**Seleccionar bucket**" abierto. Muestra el breadcrumb "Buckets" y una fila seleccionada (resaltada en azul): `bucket-utec-bigdata-2025-v1`. Botones **Seleccionar** / Cancelar.

## Slide 25

**Personalizar: Selección de bucket**

Captura tras seleccionar el bucket. El campo "Bucket de etapa de pruebas de Cloud Storage" ahora muestra `bucket-utec-bigdata-2025-v1` (con ícono verde de validación) + botón Explorar. Se mantienen visibles las secciones Acciones de inicialización, Metadatos personalizados, Eliminación programada.

## Slide 26

**Seguridad: Acceso y Encriptación**

Captura del paso "Administrar seguridad":

- **Acceso al proyecto** — checkbox marcado: "Habilita el alcance de la plataforma de nube para este clúster."
- **Encriptación** — "Encrypt cluster persistent disk data and optionally job argument data." Radios:
  - **Clave de encriptación administrada por Google** (seleccionado) — Claves propiedad de Google.
  - Clave de Cloud KMS — Claves propiedad de los clientes.
  - Toggle (desactivado): "Encrypt job argument data in addition to cluster persistent disk data."
  - Checkbox: Habilitar Confidential Computing (solo si todos los nodos usan tipo de máquina N2D).
- **Autenticación personal del clúster** — toggle "Habilitar" (desactivado).
- **Multiusuario seguro** — toggle "Habilitar" (desactivado).
- **Modo seguro de Kerberos y Hadoop** — autenticación, aislamiento y encriptación.

## Slide 27

**Terminal: Usando código en GCP**

Captura de la consola Dataproc con **Cloud Shell** abierto en la parte inferior (terminal negra, proyecto `infra-voyage-469707-g8`). Aviso "Gemini CLI está disponible en la terminal de Cloud Shell."

En la terminal se ejecuta el comando de creación del clúster y aparece la salida:

```
Welcome to Cloud Shell! Type "help" to get started...
Your Cloud Platform project in this session is set to infra-voyage-469707-g8.
a_lezamabenavides@cloudshell:~ (infra-voyage-469707-g8)$ gcloud dataproc clusters create cluster-14e6 --enable-component-gateway --bucket bucket-utec-bigdata-2025-v1 --region us-east1 --no-address --master-machine-type n4-standard-2 --master-boot-disk-type hyperdisk-balanced --master-boot-disk-size 100 --num-workers 2 --worker-machine-type n4-standard-2 --worker-boot-disk-type hyperdisk-balanced --worker-boot-disk-size 50 --image-version 2.2-debian12 --optional-components JUPYTER --scopes 'https://www.googleapis.com/auth/cloud-platform' --project infra-voyage-469707-g8
Waiting on operation [projects/infra-voyage-469707-g8/regions/us-east1/operations/0d73a881-2a3b-36e3-89a2-70e78de8f0a3].
Waiting for cluster creation operation...
WARNING: Failed to validate permissions required for default service account: '670104136254-compute@developer.gserviceaccount.com'. Cluster creation could still be successful if required permissions have been granted... Enable Cloud Resource Manager API...
WARNING: The firewall rules for specified network or subnetwork would allow ingress traffic from 0.0.0.0/0, which could be a security risk.
Waiting for cluster creation operation...working...
```

## Slide 28

**Terminal: Usando código en GCP**

Diagrama que desglosa el comando `gcloud dataproc clusters create` línea por línea, con flechas a etiquetas explicativas y recuadros de colores:

```
gcloud dataproc clusters create cluster-14e6      → Nombre del clúster
--enable-component-gateway
--bucket bucket-utec-bigdata-2025-v1
--region us-east1                                 → Ubicación del cluster
--public-ip-address                                 IP Pública
--master-machine-type n4-standard-2               → Características del Nodo administrador
--master-boot-disk-type hyperdisk-balanced
--master-boot-disk-size 100 --num-workers 2
--worker-machine-type n4-standard-2               → Características de los nodos trabajadores
--worker-boot-disk-type hyperdisk-balanced
--worker-boot-disk-size 50
--image-version 2.2-debian12                       → Características de la imagen
--optional-components JUPYTER                      → Componentes adicionales
--scopes 'https://www.googleapis.com/auth/cloud-platform'
--project infra-voyage-469707-g8
```

Recuadro derecho **"Copia y pega esto en el terminal"** con el comando en una sola línea:

```
gcloud dataproc clusters create cluster-14e6 --enable-component-gateway --bucket bucket-utec-bigdata-2025-v1 --region us-east1 --public-ip-address --master-machine-type n4-standard-2 --master-boot-disk-type hyperdisk-balanced --master-boot-disk-size 100 --num-workers 2 --worker-machine-type n4-standard-2 --worker-boot-disk-type hyperdisk-balanced --worker-boot-disk-size 50 --image-version 2.2-debian12 --optional-components JUPYTER --scopes 'https://www.googleapis.com/auth/cloud-platform' --project infra-voyage-469707-g8
```

## Slide 29

**Creación de Clúster: Terminado**

Captura de la lista de Clústeres con el clúster creado. Banner rojo "El servidor no pudo completar tu solicitud." La tabla muestra:

| Nombre | Estado | Región | Zona | Base image version | Total de nodos trabajadores | ¿Tiene VMs flexibles? | Eliminación programada | Bucket de etapa de pruebas |
|--------|--------|--------|------|--------------------|-----------------------------|-----------------------|------------------------|----------------------------|
| cluster-14e6 | En ejecución (✓ verde) | us-east1 | us-east1-d | 2.2.64-debian12 | 2 | No | Desactivado | bucket-utec-bigdata-2025-v1 |

## Slide 30

Divisor de sección. **03. Comandos Útiles** (icono de portapapeles).

## Slide 31

**Comandos Básicos con Linux**

Nota lateral: "interactuamos con la VM del clúster".

| Comando | Explicación |
|---------|-------------|
| `pwd` | Muestra en qué carpeta estás (ruta actual). |
| `ls -lh` | Lista archivos en la carpeta actual (con tamaños legibles). |
| `cd carpeta/` | Entra a una carpeta. |
| `cd ..` | Sube un nivel de carpeta. |
| `mkdir practica` | Crea una carpeta llamada practica. |
| `rm archivo.txt` | Elimina un archivo. |
| `rm -r carpeta/` | Elimina una carpeta con todo su contenido. |
| `cp archivo.txt copia.txt` | Copia un archivo. |
| `mv archivo.txt ../` | Mueve un archivo a otra ruta (ejemplo: al directorio padre). |
| `head archivo.csv` | Muestra las primeras 10 líneas de un archivo. |
| `tail archivo.csv` | Muestra las últimas 10 líneas. |
| `wc -l archivo.csv` | Cuenta cuántas líneas tiene el archivo. |
| `wget URL` | Descarga un archivo de internet. |
| `unzip archivo.zip` | Descomprime un archivo .zip. |

## Slide 32

**Comandos Básicos de HFDS** (HDFS)

Nota lateral: "interactuamos con el sistema de archivos distribuido de Hadoop".

| Comando | Explicación |
|---------|-------------|
| `hdfs dfs -ls /ruta` | Lista archivos en HDFS |
| `hdfs dfs -mkdir /ruta` | Crea una carpeta en HDFS |
| `hdfs dfs -put archivo /ruta` | Sube archivo de Linux a HDFS |
| `hdfs dfs -get /ruta ./` | Descarga archivo de HDFS a Linux |
| `hdfs dfs -copyFromLocal archivo /ruta` | Copia de Linux → HDFS (igual que `-put`) |
| `hdfs dfs -copyToLocal /ruta ./` | Copia de HDFS → Linux (igual que `-get`) |
| `hdfs dfs -cat /ruta/archivo` | Muestra contenido del archivo en HDFS |
| `hdfs dfs -rm /ruta/archivo` | Borra archivo en HDFS |
| `hdfs dfs -rm -r /ruta/carpeta` | Borra carpeta completa en HDFS |

## Slide 33

**Conclusiones**

- **01.** GCP proporciona una infraestructura flexible y escalable para implementar Hadoop y trabajar con HDFS en la nube.
- **02.** La creación y configuración de un clúster en Dataproc requiere entender parámetros clave como nodos maestros, workers, red, seguridad y almacenamiento.
- **03.** El dominio de los comandos básicos de Linux y HDFS es esencial para administrar eficientemente los recursos y gestionar datos en entornos Big Data.

## Slide 34

Cierre. Logo UTEC "Universidad de Ingeniería y Tecnología" sobre fondo cian. Decorativa.
