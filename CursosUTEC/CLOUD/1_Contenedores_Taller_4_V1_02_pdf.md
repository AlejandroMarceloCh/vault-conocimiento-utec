---
curso: CLOUD
titulo: 1. Contenedores - Taller 4 - V1.02
slides: 20
fuente: 1. Contenedores - Taller 4 - V1.02.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Virtualización con contenedores
Semana 4 - Taller 4: Contenedores

                      ELABORADO POR: GERALDO COLCHADO
               1. Objetivo del taller 4
               2. Ejercicio 1: Subir imágenes de Aplicación Multi
                  Contenedor a hub.docker.com
               3. Ejercicio 2: Desplegar Aplicación Multi
Contenido         Contenedor en otras computadoras
Contenedores
               4. Ejercicio 3: Diagramar Arquitectura de
                  Solución de Aplicación Multi Contenedor
               5. Ejercicio 4: Catálogo de Apis
               6. Cierre
Objetivo del taller 4:
Contenedores
•   Aprender a subir imágenes de Aplicación Multi Contenedor a
    hub.docker.com
•   Aprender a desplegar Aplicación Multi Contenedor en otras
    computadoras
•   Aprender a diagramar Arquitectura de Solución de Aplicación
    Multi Contenedor
•   Aprender a documentar Apis en un Catálogo de Apis
               1. Objetivo del taller 4
               2. Ejercicio 1: Subir imágenes de Aplicación
                  Multi Contenedor a hub.docker.com
               3. Ejercicio 2: Desplegar Aplicación Multi
Contenido         Contenedor en otras computadoras
Contenedores
               4. Ejercicio 3: Diagramar Arquitectura de
                  Solución de Aplicación Multi Contenedor
               5. Ejercicio 4: Catálogo de Apis
               6. Cierre
      Ejercicio 1:
      Subir imágenes de Aplicación Multi Contenedor a
      hub.docker.com
•   Paso 1: Cree dos repositorios públicos en hub.docker.com para las imágenes
      Ejercicio 1:
      Subir imágenes de Aplicación Multi Contenedor a
      hub.docker.com
•   Paso 2: Modifique el archivo docker-compose.yml en “MV Desarrollo”
Ejercicio 1:
Subir imágenes de Aplicación Multi Contenedor a
hub.docker.com
•   Paso 3: Ejecute la aplicación multi contenedor
    $ docker-compose up -d               (Ejecuta en segundo plano)
•   Paso 5: Analice las imágenes creadas y los contenedores
    $ docker images
    $ docker ps -a
•   Paso 6: Ingrese a hub docker (Docker Registry) con este comando:
    $ docker login -u gcolchado                          (Reemplace amarillo)
•   Paso 7: Suba sus imágenes a los repositorios públicos creados:
    $ docker-compose push
•   Paso 8: Salga del hub docker (Docker Registry)
    $ docker logout
•   Paso 9: Detenga la aplicación multi contenedor
    $ docker-compose down
               1. Objetivo del taller 4
               2. Ejercicio 1: Subir imágenes de Aplicación Multi
                  Contenedor a hub.docker.com
               3. Ejercicio 2: Desplegar Aplicación Multi
Contenido         Contenedor en otras computadoras
Contenedores
               4. Ejercicio 3: Diagramar Arquitectura de
                  Solución de Aplicación Multi Contenedor
               5. Ejercicio 4: Catálogo de Apis
               6. Cierre
Ejercicio 2:
Desplegar Aplicación Multi Contenedor en otras
computadoras
• Paso 1: Ingrese por ssh a la máquina virtual “MV Pruebas”
• Paso 2: Cree el directorio /home/ubuntu/app-multi-conte e ingrese
• Paso 3: Copie por sftp o WinSCP el archivo docker-compose.yml
Ejercicio 2:
Desplegar Aplicación Multi Contenedor en otras
computadoras
• Paso 4: Ejecute la aplicación Multi Contenedor:
   $ docker-compose up -d

• Paso 5: Analice las imágenes creadas y los contenedores
   $ docker images
   $ docker ps -a

• Paso 6: Pruebe en navegador y con postman

• Paso 7: Detenga la aplicación multi contenedor
   $ docker-compose down
               1. Objetivo del taller 4
               2. Ejercicio 1: Subir imágenes de Aplicación Multi
                  Contenedor a hub.docker.com
               3. Ejercicio 2: Desplegar Aplicación Multi
Contenido         Contenedor en otras computadoras
Contenedores
               4. Ejercicio 3: Diagramar Arquitectura de
                  Solución de Aplicación Multi Contenedor
               5. Ejercicio 4: Catálogo de Apis
               6. Cierre
Ejercicio 3:
Diagramar Arquitectura de Solución de Aplicación Multi
Contenedor

•   Paso 1: Ingrese a https://draw.io/ y siga las indicaciones del docente
    para elaborar el Diagrama de Arquitectura de Solución de Aplicación
    Multi Contenedor
               1. Objetivo del taller 4
               2. Ejercicio 1: Subir imágenes de Aplicación Multi
                  Contenedor a hub.docker.com
               3. Ejercicio 2: Desplegar Aplicación Multi
Contenido         Contenedor en otras computadoras
Contenedores
               4. Ejercicio 3: Diagramar Arquitectura de
                  Solución de Aplicación Multi Contenedor
               5. Ejercicio 4: Catálogo de Apis
               6. Cierre
Ejercicio 4:
Catálogo de Apis
•   Paso 1: Cree un repositorio en github con los 2 archivos del directorio catalog
Ejercicio 4:
Catálogo de Apis
•     Paso 2: Descargue el repositorio de github en la MV Pruebas con git clone




•     Paso 3: Ejecute el contenedor de swagger ui (Analice el parámetro -e y -v que explique el
      docente)

$ docker run -d -p 8080:8080 -e SWAGGER_JSON=/catalog/api-students.yaml -v /home/ubuntu/catalog:/catalog swaggerapi/swagger-ui
Ejercicio 4:
Catálogo de Apis
•   Paso 4: Visualice el Catálogo de Apis para api-students
Ejercicio 4:
Catálogo de Apis
•   Paso 5: Visualice el Catálogo de Apis para apis-pet-store
               1. Objetivo del taller 4
               2. Ejercicio 1: Subir imágenes de Aplicación Multi
                  Contenedor a hub.docker.com
               3. Ejercicio 2: Desplegar Aplicación Multi
Contenido         Contenedor en otras computadoras
Contenedores
               4. Ejercicio 3: Diagramar Arquitectura de
                  Solución de Aplicación Multi Contenedor
               5. Ejercicio 4: Catálogo de Apis
               6. Cierre
Cierre:
Contenedores - Qué aprendimos?
•   Subir imágenes de Aplicación Multi Contenedor a
    hub.docker.com
•   Desplegar Aplicación Multi Contenedor en otras computadoras
•   Diagramar Arquitectura de Solución de Aplicación Multi
    Contenedor
•   Documentar Apis en un Catálogo de Apis
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
