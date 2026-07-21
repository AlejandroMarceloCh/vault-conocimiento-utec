---
curso: BIGDATA
titulo: 05 - Semana 3/Semana 3 - Laboratorio
slides: 34
fuente: 05 - Semana 3/Semana 3 - Laboratorio.pdf
---

## Slide 1

Portada (decorativa). Título grande: **HDFS en GCP**. Subtítulo: **Semana 2**. Foto del edificio de UTEC a la derecha sobre fondo turquesa.

## Slide 2

**Objetivo de la sesión**

Dentro de un recuadro con esquinas tipo corchete:

- **Comprender** cómo se gestiona el almacenamiento en Google Cloud Platform (GCP) y su integración con Hadoop.
- **Aprender** a crear y configurar un clúster Hadoop en GCP utilizando Dataproc.
- **Desarrollar** habilidades prácticas en el uso de comandos básicos de Linux y HDFS para interactuar con clústeres y sistemas distribuidos.

## Slide 3

**Contenido de la sesión**

Tres bloques numerados, cada uno dentro de corchetes:

- **01.** Almacenamiento en GCP
- **02.** Clúster Hadoop en GCP
- **03.** Comandos útiles

## Slide 4

Portada de sección (divisoria). Número grande **01.** entre corchetes, junto a un ícono de portapapeles y el texto **Almacenamiento en GCP**.

## Slide 5

**Cloud Storage**

Captura de pantalla de la consola de Google Cloud (proyecto "My First Project"), sección **Cloud Storage > Buckets**. El panel izquierdo muestra el menú: Descripción general, Buckets (seleccionado), Supervisión, Configuración, y bajo "Storage Intelligence": Conjuntos de datos de es..., Configuración.

La tabla de buckets tiene columnas: casilla, Nombre, Fecha de creación, Tipo de ubicación, Ubicación, Clase de almacenamiento predeterminada, Última modificación, Acceso público, Control de acceso. El mensaje dice "No hay filas para mostrar."

En el centro, ilustración de un cuadro/marco con una nube punteada y el texto: "Almacena y recupera tus datos. Para empezar, crea un bucket, un contenedor en el que puedes organizar y controlar el acceso a tus datos y archivos en Cloud Storage." Con dos botones: **Crear bucket** (azul) y **Seguir la guía de inicio rápido**.

## Slide 6

**Cloud Storage: Comenzar**

Captura de la consola, pantalla **Crear un bucket**. Sección "Comenzar":
- "Selecciona un nombre permanente globalmente único" con link "Lineamientos para asignar nombre".
- Campo de texto con el nombre: `bucket-utec-bigdata-2025-v1`. Nota: "No incluyas información sensible."
- Etiquetas (opcional). Botón **Continuar**.

Resumen de las siguientes secciones colapsadas:
- **Elige dónde almacenar tus datos**: Ubicación: us (múltiples regiones en Estados Unidos); Tipo de ubicación: Multi-region.
- **Elige cómo almacenar tus datos**: Clase de almacenamiento predeterminada: Standard; Espacio de nombres jerárquico: Inhabilitado.
- **Elige cómo controlar el acceso a los objetos**: Prevención del acceso público: Sí; Control de acceso: Uniforme.
- **Elige cómo proteger los datos de objeto**: Política de eliminación no definitiva: Predeterminada; Controles de versiones de objetos: Inhabilitado; Política de retención del bucket: Inhabilitado; Retención de objetos: Inhabilitado; Tipo de encriptación: Administrada por Google.
- Botones **Crear** / Cancelar.

Panel derecho "Información útil" — Precios de ubicación. Configuración actual: Multi-region/Standard. Tabla:

| Elemento | Costo |
|----------|-------|
| us (múltiples regiones en Estados Unidos) | $0.026 por GB al mes |
| Con replicación predeterminada | $0.020 por GB escrito |

## Slide 7

**Cloud Storage: Dónde**

Captura de la consola, sección "Elige dónde almacenar tus datos" (paso "Comenzar" ya marcado, Nombre: bucket-utec-bigdata-2025-v1). Texto: "Esta opción define la ubicación geográfica de tus datos y afecta el costo, el rendimiento y la disponibilidad. No se puede cambiar más adelante."

**Tipo de ubicación** (radio buttons):
- Multi-region — "Máxima disponibilidad en el área más amplia"
- Dual-region — "Alta disponibilidad y baja latencia en 2 regiones"
- **Region** (seleccionado) — "Latencia mínima dentro de una sola región"

Dropdown seleccionado: `us-east1 (Carolina del Sur)`. Checkbox sin marcar: "Agregar replicación entre buckets a través del Servicio de transferencia de almacenamiento". Botón **Continuar**.

Panel derecho: Configuración actual: Region/Standard.

| Elemento | Costo |
|----------|-------|
| us-east1 (Carolina del Sur) | $0.020 por GB al mes |

## Slide 8

**Cloud Storage: Cómo**

Captura de la consola, sección "Elige cómo almacenar tus datos". Explica que la clase de almacenamiento determina costos de almacenamiento, recuperación y operaciones.

Opciones (radio buttons):
- **Autoclass** — "Realiza la transición automáticamente de cada objeto a las clases Estándar o Nearline según la actividad a nivel de objeto para optimizar el costo y la latencia..."
- **Configurar una clase predeterminada** (seleccionado) — "Se aplica a todos los objetos del bucket... Se recomienda cuando el uso es muy predecible." Con sub-opciones:
  - **Standard** (seleccionado) — "La mejor opción para el almacenamiento a corto plazo y los datos de acceso frecuente"
  - Nearline — "Ideal para copias de seguridad y datos a los que se accede menos de una vez al mes"
  - Coldline — "Ideal para recuperación ante desastres y datos a los que se accede menos de una vez por trimestre"
  - Archive — "La mejor opción para la conservación digital a largo plazo de los datos a los que se accede menos de una vez al año"

Abajo: "Optimiza el almacenamiento para cargas de trabajo con uso intensivo de datos" con checkbox sin marcar "Habilita el espacio de nombres jerárquico en este bucket". Botón **Continuar**.

## Slide 9

**Cloud Storage: Controlar**

Captura de la consola. Pasos "Elige dónde almacenar tus datos" (us-east1, Region) y "Elige cómo almacenar tus datos" (Standard) ya marcados con check.

Sección "Elige cómo controlar el acceso a los objetos":
- **Impedir el acceso público** — "Restringe el acceso público a los datos a través de Internet. Esto evitará que el bucket se use para el hosting web." Checkbox **marcado**: "Aplicar la prevención de acceso público a este bucket".
- **Control de acceso** (radio buttons):
  - **Uniforme** (seleccionado) — "Garantiza el acceso uniforme a todos los objetos del bucket mediante el uso exclusivo de permisos a nivel de bucket (IAM). Esta opción se aplicará de manera permanente después de 90 días."
  - Preciso — "Especifica el acceso a objetos individuales mediante el uso de permisos a nivel de objeto (LCA) además de los permisos a nivel de bucket (IAM)."

Botón **Continuar**. Abajo resumen "Elige cómo proteger los datos de objeto" con valores por defecto. Botones **Crear** / Cancelar.

## Slide 10

**Cloud Storage: Proteger**

Captura de la consola. Sección "Elige cómo proteger los datos de objeto": "Tus datos siempre están protegidos con Cloud Storage, pero también puedes elegir entre estas opciones adicionales de protección de datos..."

**Protección de datos**:
- Checkbox **marcado**: "Política de eliminación no definitiva (para la recuperación de datos)" — el bucket y sus objetos se conservan durante un período tras borrarlos. Sub-opciones (radio):
  - **Usar la duración de retención predeterminada** (seleccionado) — "Todos los buckets tienen una duración de eliminación no definitiva de 7 días de forma predeterminada..."
  - Establecer duración de retención personalizada — "...Si estableces una duración de '0', se inhabilitará la eliminación no definitiva..."
- Checkbox sin marcar: "Control de versiones de objetos (para el control de versión)".
- Checkbox sin marcar: "Retención (para el cumplimiento)".

Link desplegable "Encriptación de datos". Botones **Crear** / Cancelar.

## Slide 11

**Cloud Storage**

Captura de la consola con un cuadro de diálogo modal superpuesto: **"Se impedirá el acceso público"**. Texto: "Este bucket está configurado para evitar la exposición de tus datos en la Internet pública. Mantén habilitado este parámetro de configuración, a menos que tengas un caso de uso que requiera acceso público (como el alojamiento estático de un sitio web). Puedes cambiarlo ahora o más adelante."
- Checkbox marcado: "Aplicar la prevención de acceso público a este bucket".
- Checkbox sin marcar: "No volver a mostrar este mensaje".
- Botones: Cancelar / **Confirmar**.

Al fondo el resumen del bucket con todos los pasos marcados y "Procesando..." en la parte inferior.

## Slide 12

**Cloud Storage**

Captura de la consola, lista de Buckets ya con el bucket creado. La tabla muestra una fila:

| Nombre | Fecha de creación | Tipo de ubicación | Ubicación | Clase de almacenamiento predeterminada | Última modificación | Acceso público | Control de acceso |
|--------|-------------------|-------------------|-----------|----------------------------------------|---------------------|----------------|-------------------|
| bucket-utec-bigdata-2025-v1 | 29 ago 2025 16:11:32 | Region | us-east1 | Standard | 29 ago 2025 16:11:32 | No público | Uniforme |

Notificación toast negra abajo: "Se creó el bucket bucket-utec-bigdata-2025-v1".

## Slide 13

Portada de sección (divisoria). Número grande **02.** entre corchetes, ícono de portapapeles y texto **Clúster Hadoop en GCP**.

## Slide 14

**Creación de Clúster con Dataproc**

Captura de la consola, ruta Dataproc / Clústeres. Barra de acciones: Create cluster, Actualizar, Iniciar, Detener, Borrar, Regiones, "+ 5 alertas recomendadas". Menú lateral con: Descripción general; Notebooks/IDE (BigQuery Studio, Workbench); Clústeres (Clústeres, Trabajos, Flujos de trabajo, Políticas de escalado automático); Sin servidores (Lotes, Sesiones interactivas, Plantillas de sesión); Servicios de Metastore (Metastore, Federación); Servicios públicos (Intercambio de componentes).

Tarjeta central "Clúster — Cloud Dataproc": "Google Cloud Dataproc te permite aprovisionar clústeres de Apache Hadoop y conectarte a almacenes de datos de análisis subyacentes. No hay clústeres en las regiones de Cloud Dataproc seleccionadas actualmente. Crea un clúster para comenzar." Botón azul **Create cluster**.

## Slide 15

**Clúster: Configuración**

Captura de "Crea un clúster de Dataproc en Compute Engine". Pasos a la izquierda: Configura el clúster, Configura los nodos (opcional), Personaliza el clúster (opcional), Administrar seguridad (opcional). Botones Crear/Cancelar; links "Línea de comandos equivalente" y "REST equivalente".

Sección **Nombre**: campo "Nombre del clúster" = `cluster-ec8d`.

Sección **Ubicación**: Región = `us-central1`; Zona = `Cualquiera`.

Sección **Tipo de clúster** (radio):
- **Estándar (1 principal, N trabajadores)** (seleccionado)
- Un solo nodo (1 principal, 0 trabajadores) — "Ideal para procesamiento de pequeña escala o prueba de concepto"
- Alta disponibilidad (3 principales, N trabajadores) — "operaciones YARN y HDFS ininterrumpidas a pesar de las fallas o reinicios del nodo único"

Sección **Control de versiones**: Tipo de imagen y versión = `2.2-debian12`; Fecha de lanzamiento = "Lanzamiento de la primer..."; botón Cambiar. Al final aparece "Mejoras en el rendimiento de Spark".

## Slide 16

**Configuración: Control de Versiones**

Captura del mismo formulario, con foco en:

Sección **Control de versiones**: Tipo de imagen y versión = `2.2-debian12`; Fecha de lanzamiento = "Lanzamiento de la primer..."; botón Cambiar.

Sección **Mejoras en el rendimiento de Spark** (checkboxes sin marcar):
- Enable advanced optimizations
- Enable advanced execution layer
- Enable Google Cloud Storage caching

Sección **Ajuste de escala automático**: Política = `None`.

Sección **Modo de flexibilidad mejorada**: descripción del EFM de Dataproc (Shuffle de trabajador principal y Shuffle del sistema de archivos compatible con Hadoop / HCFS). Aviso: "An autoscaling policy must be selected to configure EFM."

Al final: "Configuración de red".

## Slide 17

**Configuración: Red**

Captura del formulario, sección **Configuración de red**: "Establece la conectividad para las instancias de VM en el clúster."
- Radio **Redes en este proyecto** (seleccionado)
- Radio "Redes compartidas del proyecto host"
- Red principal = `default`; Subred = (Subred, dropdown).
- Campo "Etiquetas de red" con nota sobre network tags para reglas de firewall.

Sección **Dataproc Metastore**: "Configura Dataproc para usar Dataproc Metastore como su almacén de metadatos de Hive." Proyecto seleccionado = My First Project (botón Explorar). Servicio de almacén de metadatos = `Ninguno`.

Sección **Componentes**: "Puerta de enlace del componente" — checkbox marcado "Habilitar puerta de enlace de componentes". "Componentes opcionales — Selecciona uno o varios componentes."

## Slide 18

**Configuración - Componentes**

Captura del formulario, sección **Componentes**.
- **Puerta de enlace del componente**: checkbox marcado "Habilitar puerta de enlace de componentes".
- **Componentes opcionales** (checkboxes):
  - Hive WebHCat (sin marcar)
  - **Jupyter Notebook** (marcado)
  - Zeppelin Notebook (sin marcar)
  - Trino (sin marcar)
  - ZooKeeper (sin marcar)
  - Ranger (sin marcar)
  - Flink (sin marcar)
  - Docker (sin marcar)
  - Solr (sin marcar)
  - Hudi (sin marcar)
  - Iceberg (sin marcar)
  - Delta (sin marcar)

## Slide 19

**Configuración nodo: principal node**

Captura del formulario, paso "Configura los nodos". Sección **Nodo de administrador**: "Contiene el administrador de recursos YARN, HDFS NameNode y todos los controladores de trabajos."
- Toggle "De uso general" (seleccionado) / "Con optimización de memoria".
- Serie = `N4` ("Con la tecnología de la plataforma de CPU Emerald Rapids de Intel").
- Tipo de máquina = `n4-standard-2 (2 CPU virtuales, 1 núcleos, 8 GB de memoria)`.
- Resumen: **vCPU** 2, **Memory** 8 GB.
- "Plataforma de CPU y GPU".
- Tamaño del disco principal = `100 GB`; Primary disk type = `Hyperdisk Balanced Disk`.
- IOPS, Throughput (vacíos). Cantidad de SSD locales = `0 x 375GB`; Interfaz de SSD local = `SCSI`.

Al final comienza sección **Nodos trabajadores**: "Cada uno contiene un NodeManager de YARN y un DataNode de HDFS. El factor de replicación de HDFS es 2."

## Slide 20

**Configuración nodo: workers nodes**

Captura del formulario, sección **Nodos trabajadores**: "Cada uno contiene un NodeManager de YARN y un DataNode de HDFS. El factor de replicación de HDFS es 2."
- Toggle "De uso general" (seleccionado) / "Con optimización de memoria".
- Serie = `N4`.
- Tipo de máquina = `n4-standard-2 (2 CPU virtuales, 1 núcleos, 8 GB de memoria)`.
- Resumen: **vCPU** 2, **Memory** 8 GB.
- **Number of worker nodes** = `2`.
- Tamaño del disco principal = `50 GB`; Primary disk type = `Hyperdisk Balanced Disk`.
- IOPS, Throughput (vacíos). Cantidad de SSD locales = `0 x 375GB`; Interfaz de SSD local = `SCSI`.

Al final comienza sección **Nodos trabajadores secundarios**: "Cada uno contiene un NodeManager de YARN. HDFS no se puede ejecutar en nodos trabajadores secundarios..."

## Slide 21

**Configuración nodo: secondary nodes**

Captura del formulario, sección **Nodos trabajadores secundarios**: "Cada uno contiene un NodeManager de YARN. HDFS no se puede ejecutar en nodos trabajadores secundarios. Las VM de trabajador secundarias son interrumpibles de forma predeterminada. Las VMs interrumpibles y spot cuestan menos, pero se pueden cerrar en cualquier momento..."

Sección **Usuario único**: "Habilita esta opción para crear este clúster en nodos de usuario único, lo que otorga acceso exclusivo a un servidor físico de Compute Engine..." Toggle "Habilitar" (desactivado).

Sección **VM protegida**: "Activa todos los ajustes para lograr la configuración más segura." Checkboxes sin marcar:
- Activa el arranque seguro
- Activa vTPM
- Activar la supervisión de integridad

Sección **Uso total de YARN**:

| Núcleos YARN | Memoria YARN |
|--------------|--------------|
| 4 | 13.74 GB |

## Slide 22

**Personalizar: IP internas**

Captura del formulario, paso "Personaliza el clúster".

Sección **Solo IP internas**: checkbox **marcado** "Configurar todas las instancias para tener solo direcciones IP internas".

Sección **Etiquetas**: "Una lista de pares clave-valor que se adjuntarán al clúster para realizar el seguimiento." Botón **+ Agregar etiquetas**.

Sección **Propiedades del clúster**: "Usa las propiedades del clúster para agregar o modificar archivos de configuración cuando creas un clúster." Botón **+ Agregar propiedades**.

Sección **Acciones de inicialización**: "Utiliza acciones de inicialización para personalizar la configuración, instalar aplicaciones o realizar otras modificaciones en tu clúster..." Botón **+ Agregar acción de inicialización**.

Sección **Metadatos personalizados del clúster**: botón **+ Agregar metadatos**.

## Slide 23

**Personalizar: Acciones de inicialización**

Captura del formulario, continúa la sección "Personaliza el clúster".
- **Propiedades del clúster** con botón **+ Agregar propiedades**.
- **Acciones de inicialización** con botón **+ Agregar acción de inicialización**.
- **Metadatos personalizados del clúster** con botón **+ Agregar metadatos**.
- **Eliminación programada**: "Usa la eliminación programada para evitar que se generen cobros de Google Cloud por un clúster inactivo." Checkboxes sin marcar: "Borrar según el cronograma de fechas establecido", "Borrar luego de un tiempo de inactividad del clúster sin trabajos enviados".
- **Bucket de etapa de pruebas de Cloud Storage**: campo "Bucket de etapa de pruebas de almacenamiento" (vacío) con botón Explorar. Nota: "El bucket de etapa de pruebas de Cloud Storage que se usará para almacenar las dependencias de trabajos clústeres, los resultados del controlador de trabajos y los archivos de configuración de clústeres."

## Slide 24

**Personalizar: Selección de bucket**

Misma pantalla que la anterior con un panel modal a la derecha: **"Seleccionar bucket"**. Navegador de buckets (ruta "Buckets") mostrando una fila seleccionada (resaltada en azul): `bucket-utec-bigdata-2025-v1` con una flecha ">". Botones abajo: **Seleccionar** (azul) / Cancelar.

## Slide 25

**Personalizar: Selección de bucket**

Captura del formulario tras seleccionar el bucket. En la sección **Bucket de etapa de pruebas de Cloud Storage** el campo ahora muestra `bucket-utec-bigdata-2025-v1` (con ícono verde de validado) y botón Explorar. Resto de secciones igual (Acciones de inicialización, Metadatos personalizados, Eliminación programada).

## Slide 26

**Seguridad: Acceso y Encriptación**

Captura del formulario, paso "Administrar seguridad".

Sección **Acceso al proyecto**: checkbox marcado "Habilita el alcance de la plataforma de nube para este clúster".

Sección **Encriptación**: "Encrypt cluster persistent disk data and optionally job argument data." Radio:
- **Clave de encriptación administrada por Google** (seleccionado) — "Claves propiedad de Google"
- Clave de Cloud KMS — "Claves propiedad de los clientes"
Toggle "Encrypt job argument data in addition to cluster persistent disk data" (desactivado). Checkbox sin marcar "Habilitar Confidential Computing" (nota: solo con máquinas N2D).

Sección **Autenticación personal del clúster**: toggle "Habilitar" (desactivado).

Sección **Multiusuario seguro**: toggle "Habilitar" (desactivado).

Sección **Modo seguro de Kerberos y Hadoop**: descripción para habilitar autenticación de usuario, aislamiento y encriptación en el clúster.

## Slide 27

**Terminal: Usando código en GCP**

Captura de la consola Dataproc/Clústeres con la **Cloud Shell** abierta en la parte inferior (terminal negra, proyecto `infra-voyage-469707-g8`). Aviso: "Gemini CLI está disponible en la terminal de Cloud Shell."

En la terminal se ejecuta el comando de creación del clúster:

```bash
gcloud dataproc clusters create cluster-14e6 --enable-component-gateway --bucket bucket-utec-bigdata-2025-v1 --region us-east1 --no-address --master-machine-type n4-standard-2 --master-boot-disk-type hyperdisk-balanced --master-boot-disk-size 100 --num-workers 2 --worker-machine-type n4-standard-2 --worker-boot-disk-type hyperdisk-balanced --worker-boot-disk-size 50 --image-version 2.2-debian12 --optional-components JUPYTER --scopes 'https://www.googleapis.com/auth/cloud-platform' --project infra-voyage-469707-g8
```

Salida:
```
Waiting on operation [projects/infra-voyage-469707-g8/regions/us-east1/operations/0d73a881-2a3b-36e3-89a2-70e78de8f0a3].
Waiting for cluster creation operation...
WARNING: Failed to validate permissions required for default service account: '670104136254-compute@developer.gserviceaccount.com'. Cluster creation could still be successful if required permissions have been granted... Enable it by visiting 'https://console.developers.google.com/apis/api/cloudresourcemanager.googleapis.com/overview?project=670104136254' before or it is disabled.
WARNING: The firewall rules for specified network or subnetwork would allow ingress traffic from 0.0.0.0/0, which could be a security risk.
Waiting for cluster creation operation...working...
```

## Slide 28

**Terminal: Usando código en GCP**

Diagrama que desglosa el comando `gcloud dataproc clusters create` línea por línea, con flechas que conectan cada bloque de flags a su significado (los bloques están resaltados con cuadros de colores y bordes rojos):

- `gcloud dataproc clusters create` **cluster-14e6** → **Nombre del clúster**
- `--enable-component-gateway`
- `--bucket bucket-utec-bigdata-2025-v1`
- `--region us-east1` / `--public-ip-address` → **Ubicación del cluster / IP Pública**
- `--master-machine-type n4-standard-2` / `--master-boot-disk-type hyperdisk-balanced` / `--master-boot-disk-size 100 --num-workers 2` → **Características del Nodo administrador**
- `--worker-machine-type n4-standard-2` / `--worker-boot-disk-type hyperdisk-balanced` / `--worker-boot-disk-size 50` → **Características de los nodos trabajadores**
- `--image-version 2.2-debian12` → **Características de la imagen**
- `--optional-components JUPYTER` → **Componentes adicionales**
- `--scopes 'https://www.googleapis.com/auth/cloud-platform'`
- `--project infra-voyage-469707-g8`

A la derecha, recuadro "**Copia y pega esto en el terminal**" con el comando completo en una sola línea:

```bash
gcloud dataproc clusters create cluster-14e6 --enable-component-gateway --bucket bucket-utec-bigdata-2025-v1 --region us-east1 --public-ip-address --master-machine-type n4-standard-2 --master-boot-disk-type hyperdisk-balanced --master-boot-disk-size 100 --num-workers 2 --worker-machine-type n4-standard-2 --worker-boot-disk-type hyperdisk-balanced --worker-boot-disk-size 50 --image-version 2.2-debian12 --optional-components JUPYTER --scopes 'https://www.googleapis.com/auth/cloud-platform' --project infra-voyage-469707-g8
```

## Slide 29

**Creación de Clúster: Terminado**

Captura de la consola Dataproc/Clústeres con el clúster ya creado. Aparece un aviso rojo "El servidor no pudo completar tu solicitud." La tabla muestra:

| Nombre | Estado | Región | Zona | Base image version | Total de nodos trabajadores | ¿Tiene VMs flexibles? | Eliminación programada | Bucket de etapa de pruebas de Cloud Storage |
|--------|--------|--------|------|--------------------|-----------------------------|-----------------------|------------------------|---------------------------------------------|
| cluster-14e6 | En ejecución (check verde) | us-east1 | us-east1-d | 2.2.64-debian12 | 2 | No | Desactivado | bucket-utec-bigdata-2025-v1 |

## Slide 30

Portada de sección (divisoria). Número grande **03.** entre corchetes, ícono de portapapeles y texto **Comandos Útiles**.

## Slide 31

**Comandos Básicos con Linux**

Nota al margen izquierdo: *"interactuamos con la VM del clúster"*.

Tabla de dos columnas:

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

Nota al margen izquierdo: *"interactuamos con el sistema de archivos distribuido de Hadoop"*.

Tabla de dos columnas:

| Comando | Explicación |
|---------|-------------|
| `hdfs dfs -ls /ruta` | Lista archivos en HDFS |
| `hdfs dfs -mkdir /ruta` | Crea una carpeta en HDFS |
| `hdfs dfs -put archivo /ruta` | Sube archivo de Linux a HDFS |
| `hdfs dfs -get /ruta ./` | Descarga archivo de HDFS a Linux |
| `hdfs dfs -copyFromLocal archivo /ruta` | Copia de Linux → HDFS (igual que -put) |
| `hdfs dfs -copyToLocal /ruta ./` | Copia de HDFS → Linux (igual que -get) |
| `hdfs dfs -cat /ruta/archivo` | Muestra contenido del archivo en HDFS |
| `hdfs dfs -rm /ruta/archivo` | Borra archivo en HDFS |
| `hdfs dfs -rm -r /ruta/carpeta` | Borra carpeta completa en HDFS |

## Slide 33

**Conclusiones**

Tres puntos numerados con estilo de corchetes:

- **01.** GCP proporciona una infraestructura flexible y escalable para implementar Hadoop y trabajar con HDFS en la nube.
- **02.** La creación y configuración de un clúster en Dataproc requiere entender parámetros clave como nodos maestros, workers, red, seguridad y almacenamiento.
- **03.** El dominio de los comandos básicos de Linux y HDFS es esencial para administrar eficientemente los recursos y gestionar datos en entornos Big Data.

## Slide 34

Contraportada (decorativa). Logo grande de **UTEC — Universidad de Ingeniería y Tecnología** centrado sobre fondo turquesa.
