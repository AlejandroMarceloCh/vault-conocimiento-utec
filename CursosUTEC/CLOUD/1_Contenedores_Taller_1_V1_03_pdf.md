---
curso: CLOUD
titulo: 1. Contenedores - Taller 1 - V1.03
slides: 25
fuente: 1. Contenedores - Taller 1 - V1.03.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Virtualización con contenedores
Semana 3 - Taller 1: Contenedores

                      ELABORADO POR: GERALDO COLCHADO
               1. Objetivo del taller 1
               2. Ejercicio 1: Instalar docker en Ubuntu
               3. Ejercicio 2: Comandos básicos de docker
Contenido      4. Ejercicio 3: Contenedor de página web
Contenedores   5. Ejercicio 4: Contenedor de Api REST python3
               6. Cierre
Objetivo del taller 1:
Contenedores
•   Aprender a instalar docker en ubuntu Linux
•   Aprender los comandos básicos de docker
•   Aprender a crear una imagen, ejecutar y detener un contenedor
    de página web
•   Aprender a crear una imagen, ejecutar y detener un contenedor
    de Api REST python3
               1. Objetivo del taller 1
               2. Ejercicio 1: Instalar docker en Ubuntu
               3. Ejercicio 2: Comandos básicos de docker
Contenido      4. Ejercicio 3: Contenedor de página web
Contenedores   5. Ejercicio 4: Contenedor de Api REST python3
               6. Cierre
                                              Nota: La Amazon Machine Image (AMI)

Ejercicio 1:                                  “amazon/Cloud9Ubuntu” ya viene con
                                              docker instalado.

Instalar docker en ubuntu
•   Paso 1: Ingresar por ssh a la máquina virtual “MV Desarrollo” con
    ubuntu Linux

•   Paso 2: Verificar si docker ya está instalado:
    $ docker -v
    Docker version 20.10.17, build 100c701

    En caso no tuviera docker instalado puede seguir este manual:
    https://docs.docker.com/engine/install/ubuntu/
               1. Objetivo del taller 1
               2. Ejercicio 1: Instalar docker en Ubuntu
               3. Ejercicio 2: Comandos básicos de docker
Contenido      4. Ejercicio 3: Contenedor de página web
Contenedores   5. Ejercicio 4: Contenedor de Api REST python3
               6. Cierre
Ejercicio 2:
Comandos básicos de docker
Comando                Descripción
$ docker build         Construir una imagen desde un Dockerfile
$ docker run           Ejecuta una imagen en un nuevo contenedor
$ docker images        Lista las imágenes almacenadas
$ docker ps            Lista los contenedores en ejecución
$ docker stop          Detiene la ejecución de un contenedor
$ docker start         Inicia un contenedor detenido
$ docker rm            Elimina un contenedor detenido
$ docker exec          Ejecuta un comando en un contenedor en
                       ejecución
               1. Objetivo del taller 1
               2. Ejercicio 1: Instalar docker en Ubuntu
               3. Ejercicio 2: Comandos básicos de docker
Contenido      4. Ejercicio 3: Contenedor de página web
Contenedores   5. Ejercicio 4: Contenedor de Api REST python3
               6. Cierre
Ejercicio 3:
Contenedor de página web
•   Paso 1: Abrir puerto 8080 en máquina virtual
•   Paso 2: Crear el directorio /home/ubuntu/web/simple
•   Paso 3: Copiar por sftp o WinSCP los archivos de la página web:
    curso.html          (renombrar $ mv curso.html index.html)
    utec_logo.png
•   Paso 4: Crear el archivo Dockerfile en el directorio
    /home/ubuntu/web
     Ejercicio 3:
     Contenedor de página web
                                            Imagen base de apache2 en
Dockerfile                                    https://hub.docker.com/



FROM httpd:2.4
COPY ./simple/ /usr/local/apache2/htdocs/
                                            Copiar todos los archivos de
                                             directorio actual a imagen
Ejercicio 3:
Contenedor de página web
•   Paso 5: En /home/ubuntu/web ejecutar el comando para
    construir la imagen:

    $ docker build -t websimple .

                                       Ejecuta el Dockerfile de directorio
                                                     actual

                                           -t o tag asigna el nombre
                                            websimple a la imagen
 Ejercicio 3:
 Contenedor de página web
 •    Paso 6: Ejecute este comando para ejecutar en un contenedor la
      imagen creada anteriormente:
      $ docker run -d -p 8080:80 websimple


Ejecutar contenedor en segundo                      Nombre de la imagen para
 plano y mostrar el container ID                    ejecutar en un contenedor

                                                   Relaciona el puerto 8080 de la
                                                  máquina virtual con el Puerto 80
       Nota: Para detener la ejecución use este
                                                          del contenedor
       comando: $ docker stop CONTAINER ID
       Obtener CONTAINER ID con $ docker ps
Ejercicio 3:
Contenedor de página web
•   Paso 7: Pruebe la página web en un navegador:
    dirección-IP:8080
               1. Objetivo del taller 1
               2. Ejercicio 1: Instalar docker en Ubuntu
               3. Ejercicio 2: Comandos básicos de docker
Contenido      4. Ejercicio 3: Contenedor de página web
Contenedores   5. Ejercicio 4: Contenedor de Api REST python3
               6. Cierre
Ejercicio 4:
Contenedor de Api REST python3
•   Paso 1: Crear directorio en máquina virtual
    /home/ubuntu/api01

•   Paso 2: Copiar por sftp o WinSCP los archivos del Api students:
    app.py
    db.py
    Dockerfile

•   Paso 3: Entender a detalle el archivo Dockerfile que tiene los
    comandos para construir automáticamente la imagen
Ejercicio 4:
Contenedor de Api REST python3
                                  Imagen base de python3 delgada
Dockerfile                          en https://hub.docker.com/

                                     Directorio a crear en imagen
FROM python:3-slim
WORKDIR /programas/api-students        Instalar flask en imagen

RUN pip3 install flask               Copiar todos los archivos de
COPY . .                              directorio actual a imagen

RUN python3 db.py                 Crear la base de datos en imagen
CMD [ "python3", "./app.py" ]
                                  Ejecutar el api REST de estudiantes
                                    cuando se ejecute la imagen en
                                              contenedor
Ejercicio 4:
Contenedor de Api REST python3
•   Paso 4: Ingrese al directorio /home/ubuntu/api01 y ejecute este
    comando para construir la imagen:

    $ docker build -t api-students .

                                          Ejecuta el Dockerfile de directorio
                                                        actual

                                              -t o tag asigna el nombre
                                              api-students a la imagen
Ejercicio 4:
Contenedor de Api REST python3
•   Paso 5: Ejecute este comando para ejecutar en un contenedor la
    imagen creada anteriormente:
    $ docker run -p 8000:8000 api-students


                                           Nombre de la imagen para
                                           ejecutar en un contenedor

                                          Relaciona el puerto 8000 de la
                                          máquina virtual con el Puerto
    Nota: Con CTRL + C podemos detener
                                              8000 del contenedor
    la ejecución de este contenedor
               Ejercicio 4:
               Contenedor de Api REST python3
              •      Paso 6: Ejecute este comando para ejecutar el contenedor en
                     segundo plano:
                     $ docker run -d -p 8000:8000 api-students

            Ejecutar contenedor en segundo
             plano y mostrar el container ID
                                                                               Nombre de la imagen para
Nota: Para detener la ejecución        Nota: Para volver a iniciar use este    ejecutar en un contenedor
use este comando:                      comando:
$ docker stop CONTAINER ID             $ docker start CONTAINER ID            Relaciona el puerto 8000 de la
Obtener CONTAINER ID con               Obtener CONTAINER ID con
$ docker ps                            $ docker ps -a                         máquina virtual con el Puerto
                                                                                  8000 del contenedor
Nota: Para eliminar un contenedor detenido use este comando:
$ docker rm CONTAINER ID       (Obtener CONTAINER ID con $ docker ps -a)
Ejercicio 4:
Contenedor de Api REST python3
•    Paso 7: Abra otra sesión ssh y ejecute este comando para entrar
     al contenedor en modo comando:
     $ docker exec -it bd2d1cd689e2 /bin/bash


       -i es de interactive                   Ejecutar el intérprete de
-t es de Allocate a pseudo-TTY                       comandos

                                           Reemplazar por el CONTAINER ID
                                                   ($ docker ps)

Ejercicio 4:
Contenedor de Api REST python3
Ejercicio 4:
Contenedor de Api REST python3
•   Paso 8: Pruebe el api REST de estudiantes con
    https://www.postman.com/
               1. Objetivo del taller 1
               2. Ejercicio 1: Instalar docker en Ubuntu
               3. Ejercicio 2: Comandos básicos de docker
Contenido      4. Ejercicio 3: Contenedor de página web
Contenedores   5. Ejercicio 4: Contenedor de Api REST python3
               6. Cierre
Cierre:
Contenedores - Qué aprendimos?
•   Instalar docker en ubuntu Linux
•   Comandos básicos de docker
•   Crear una imagen, ejecutar y detener un contenedor de página
    web
•   Crear una imagen, ejecutar y detener un contenedor de Api REST
    python3
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
