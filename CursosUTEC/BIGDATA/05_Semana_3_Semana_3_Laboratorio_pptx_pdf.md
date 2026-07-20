---
curso: BIGDATA
titulo: 05 - Semana 3/Semana 3 - Laboratorio__pptx
slides: 34
fuente: 05 - Semana 3/Semana 3 - Laboratorio__pptx.pdf
---

HDFS en GCP

Semana 2
Objetivo de la sesión


Comprender cómo se gestiona el almacenamiento en Google Cloud
Platform (GCP) y su integración con Hadoop.
Aprender a crear y configurar un clúster Hadoop en GCP utilizando
Dataproc.
Desarrollar habilidades prácticas en el uso de comandos básicos de
Linux y HDFS para interactuar con clústeres y sistemas distribuidos.
    Contenido de la sesión
    01                02                 03
      .                 .                  .
Almacenamiento   Clúster Hadoop en
                                     Comandos útiles
   en GCP               GCP
01.   Almacenamiento en
      GCP
Cloud Storage
Cloud Storage: Comenzar
Cloud Storage: Dónde
Cloud Storage: Cómo
Cloud Storage: Controlar
Cloud Storage: Proteger
Cloud Storage
Cloud Storage
02.   Clúster Hadoop en GCP
Creación de Clúster con Dataproc
Clúster: Configuración
Configuración: Control de Versiones
Configuración: Red
Configuración - Componentes
Configuración nodo: principal node
Configuración nodo: workers nodes

Configuración nodo: secondary nodes
Personalizar: IP internas
Personalizar: Acciones de inicialización
Personalizar: Selección de bucket
Personalizar: Selección de bucket
Seguridad: Acceso y Encriptación
Terminal: Usando código en GCP
                                   Terminal: Usando código en GCP
gcloud dataproc clusters create cluster-14e6                Nombre del clúster

--enable-component-gateway
--bucket bucket-utec-bigdata-2025-v1
--region us-east1                                 Ubicación del cluster
                                                       IP Pública                                  Copia y pega esto en el terminal
--public-ip-address
                                                                                     gcloud dataproc clusters create cluster-14e6 --enable-component-gateway --
--master-machine-type n4-standard-2                                                  bucket bucket-utec-bigdata-2025-v1 --region us-east1 --public-ip-address --
                                                    Características del              master-machine-type n4-standard-2 --master-boot-disk-type hyperdisk-balanced
--master-boot-disk-type hyperdisk-balanced          Nodo administrador               --master-boot-disk-size 100 --num-workers 2 --worker-machine-type n4-
                                                                                     standard-2 --worker-boot-disk-type hyperdisk-balanced --worker-boot-disk-size
--master-boot-disk-size 100 --num-workers 2                                          50 --image-version 2.2-debian12 --optional-components JUPYTER --scopes
                                                                                     'https://www.googleapis.com/auth/cloud-platform' --project infra-voyage-469707-
--worker-machine-type n4-standard-2                 Características de los           g8
--worker-boot-disk-type hyperdisk-balanced           nodos trabajadores

--worker-boot-disk-size 50
                                                     Características de la
--image-version 2.2-debian12                               imagen
                                                                             Componentes
--optional-components JUPYTER                                                 adicionales
--scopes 'https://www.googleapis.com/auth/cloud-platform’
--project infra-voyage-469707-g8
Creación de Clúster: Terminado
03.   Comandos Útiles
                                                    Comandos Básicos con Linux
                                           Comando                                    Explicación
                                               pwd                      Muestra en qué carpeta estás (ruta actual).

                                               ls -lh            Lista archivos en la carpeta actual (con tamaños legibles).

                                            cd carpeta/                             Entra a una carpeta.

                                               cd ..                             Sube un nivel de carpeta.

                                          mkdir practica                    Crea una carpeta llamada practica.
interactuamos con la VM del clúster
                                          rm archivo.txt                             Elimina un archivo.

                                          rm -r carpeta/                Elimina una carpeta con todo su contenido.

                                      cp archivo.txt copia.txt                        Copia un archivo.

                                         mv archivo.txt ../      Mueve un archivo a otra ruta (ejemplo: al directorio padre).

                                        head archivo.csv               Muestra las primeras 10 líneas de un archivo.

                                          tail archivo.csv                     Muestra las últimas 10 líneas.

                                         wc -l archivo.csv                 Cuenta cuántas líneas tiene el archivo.

                                            wget URL                          Descarga un archivo de internet.

                                        unzip archivo.zip                           unzip archivo.zip
                                           Comandos Básicos de HFDS
                                                   Comando                               Explicación

                                                hdfs dfs -ls /ruta                   Lista archivos en HDFS


                                              hdfs dfs -mkdir /ruta                 Crea una carpeta en HDFS


                                            hdfs dfs -put archivo /ruta           Sube archivo de Linux a HDFS


interactuamos con el sistema     de            hdfs dfs -get /ruta ./           Descarga archivo de HDFS a Linux
archivos distribuido de Hadoop

                                      hdfs dfs -copyFromLocal archivo /ruta   Copia de Linux → HDFS (igual que -put)


                                          hdfs dfs -copyToLocal /ruta ./      Copia de HDFS → Linux (igual que -get)


                                            hdfs dfs -cat /ruta/archivo       Muestra contenido del archivo en HDFS


                                            hdfs dfs -rm /ruta/archivo                Borra archivo en HDFS


                                           hdfs dfs -rm -r /ruta/carpeta         Borra carpeta completa en HDFS
                    Conclusiones
01    GCP proporciona una infraestructura flexible y escalable para implementar Hadoop y

  .
      trabajar con HDFS en la nube.



02    La creación y configuración de un clúster en Dataproc requiere entender parámetros

  .
      clave como nodos maestros, workers, red, seguridad y almacenamiento



03    El dominio de los comandos básicos de Linux y HDFS es esencial para administrar

  .
      eficientemente los recursos y gestionar datos en entornos Big Data.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
