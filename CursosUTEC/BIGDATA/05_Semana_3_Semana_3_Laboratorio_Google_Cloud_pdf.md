---
curso: BIGDATA
titulo: 05 - Semana 3/Semana 3 Laboratorio Google Cloud
slides: 34
fuente: 05 - Semana 3/Semana 3 Laboratorio Google Cloud.pdf
---

Laboratorio

Semana 3
    Objetivo de la sesión


1. Comprender las principales soluciones de almacenamiento y

   analítica en la nube de Google Cloud.
2. Identificar cuándo usar cada servicio dentro de una arquitectura

   de datos.
3. Aplicar los conceptos mediante la creación de un bucket y un

   clúster.
                 Contenido de la sesión

    01.                 02.             03.              04.

 Soluciones de       Soluciones de   Creación de un   Creación de un
Almacenamiento         Analítica         bucket           clúster
01.   Soluciones de
      Almacenamiento
Almacenamiento de archivos en la
nube (tipo data lake).
Función:
•   Guardar y acceder a datos masivos desde
    cualquier servicio
Cuando usarlo:
•   Para   analítica,    backups   y   datos   de
    entrada/salida.
Disco compartido tipo red (NFS)
Función:
•   Permitir que varias máquinas accedan a
    los mismos archivos.
Cuando usarlo:
•   Apps que necesitan filesystem tradicional.
Backup and DR
Función:
•   Crear copias y restaurar sistemas ante
    fallas.
Cuando usarlo:
•   Continuidad del negocio y cumplimiento.
Herramienta de transferencia de datos
Función:
•   Mover datos desde on-premise u otras
    nubes.
Cuando usarlo:
•   Migraciones    o   cargas    masivas
    programadas.
Sistema        de   archivos      de     alto
rendimiento
Función:
•   Procesar grandes volúmenes de datos en
    paralelo
Cuando usarlo:
•   Simulaciones o cargas intensivas (HPC).
Filesystem HPC ultra rápido
Función:
•   Soportar cargas pesadas de IA/ML y
    cómputo
Cuando usarlo:
•   Entrenamiento   ML   o   procesamiento
    intensivo
Almacenamiento                      empresarial
avanzado.
Función:
•   Ofrecer    features      como   snapshots   y
    replicación
Cuando usarlo:
•   Sistemas        legacy     o     aplicaciones
    corporativas.
02.   Soluciones de Analítica
Servicio de mensajería en tiempo real
Función:
•   Enviar y recibir eventos entre sistemas
Cuando usarlo:
•   Streaming,      eventos,      arquitecturas
    desacopladas
Procesamiento de datos en tiempo
real o Batch
Función:
•   Transformar    y     procesar      grandes
    volúmenes de datos
Cuando usarlo:
•   ETL/ELT y pipelines de streaming
Orquestador de workflows (basado en
Airflow)
Función:
•   Automatizar y programar pipelines de
    datos
Cuando usarlo:
•   Coordinar procesos ETL complejos
Servicio gestionado de Spark
Función:
•   Procesar datos distribuidos a gran escala
Cuando usarlo:
•   Big Data, ML y procesamiento masivo
Herramienta visual de preparación de
datos
Función:
•   Limpiar y transformar datos sin programar
Cuando usarlo:
•   Usuarios de negocio (low-code)
Plataforma para construir pipelines de
datos
Función:
•   Integrar y mover datos entre sistemas
Cuando usarlo:
•   Integración sin mucho código (ETL visual)
Plataforma de BI y analítica.
Función:
•   Crear dashboard y explorar datos
Cuando usarlo:
•   Reportes y toma de decisiones
Plataforma para datos de salud
Función:
•   Almacenar y procesar datos médicos
Cuando usarlo:
•   Soluciones del sector salud

03.   Creación de un bucket en GCS
                                 CREACIÓN DE BUCKET PASO A PASO
                                                                        PASO 3: FORMA DE ALMACENAMIENTO
Ruta de la solución

        Storage – Cloud Storage - Buckets




         PASO 1: NOMBRE ÚNICO CLUSTER




                                             PASO 2: TIPO DE LOCACION
CREACIÓN DE BUCKET PASO A PASO
    PASO 4: CONTROL DE ACCESO   PASO 5: PROTECCIÓN DE DATOS
CREACIÓN DE BUCKET PASO A PASO




           PASO 6: CREATE + FINALIZACIÓN
CREACIÓN DE BUCKET MEDIANTE CLOUD SHELL



                            CÓDIGO UTILIZADO
                            gcloud storage buckets create gs://bucket-utec-bigdata-202604 \
                              --default-storage-class=STANDARD \
                              --location=US-CENTRAL1 \
                              --uniform-bucket-level-access \
                              --public-access-prevention
04.   Creación de un clúster en GCP
                               CREACIÓN DE CLÚSTER PASO A PASO
Ruta de la solución

  Analytics - Managed Apache Spark - Clusters
CREACIÓN DE CLÚSTER PASO A PASO
CREACIÓN DE CLÚSTER PASO A PASO
CREACIÓN DE CLÚSTER PASO A PASO
CREACIÓN DE BUCKET PASO A PASO
CREACIÓN DE CLÚSTER MEDIANTE CLOUD SHELL

                             CÓDIGO UTILIZADO
                             gcloud dataproc clusters create cluster-3bcd --enable-
                             component-gateway --bucket bucket-utec-bigdata-202604 --
                             region us-central1 --no-address --zone us-central1-a --master-
                             machine-type n4-standard-2 --master-boot-disk-type hyperdisk-
                             balanced --master-boot-disk-size 100 --num-workers 2 --worker-
                             machine-type n4-standard-2 --worker-boot-disk-type hyperdisk-
                             balanced --worker-boot-disk-size 100 --image-version 2.3-
                             debian12 --properties
                             spark:spark.dataproc.engine=default,spark:spark.dataproc.lightni
                             ngEngine.runtime=default --optional-components
                             JUPYTER,ZOOKEEPER,PIG --max-age 7200s --scopes
                             'https://www.googleapis.com/auth/cloud-platform' --project
                             project-c845ec52-f5b1-4857-9a4
                       Conclusiones

01.   Se presentó una visión general de los servicios de analítica en Google Cloud,
      entendiendo su rol dentro del ecosistema de datos




02.   Se profundizó en soluciones de almacenamiento, clave como base para cualquier
      arquitectura de datos en la nube.




03.   La creación del bucket y clúster permitió llevar la teoría a la práctica, entendiendo
      la implementación real de un entorno de procesamiento

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
