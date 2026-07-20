---
curso: CLOUD
titulo: 1. Contenedores - Taller 3 - V1.01
slides: 15
fuente: 1. Contenedores - Taller 3 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Virtualización con contenedores
Semana 4 - Taller 3: Contenedores

                      ELABORADO POR: GERALDO COLCHADO
               1. Objetivo del taller 3
               2. Ejercicio 1: Instalar docker compose
               3. Ejercicio 2: Aplicación Multi Contenedor
Contenido      4. Ejercicio propuesto
Contenedores   5. Cierre
Objetivo del taller 3:
Contenedores
•   Aprender a instalar docker compose en ubuntu linux
•   Aprender a crear y ejecutar una aplicación Multi Contenedor
               1. Objetivo del taller 3
               2. Ejercicio 1: Instalar docker compose
               3. Ejercicio 2: Aplicación Multi Contenedor
Contenido      4. Ejercicio propuesto
Contenedores   5. Cierre
             Ejercicio 1:
             Instalar docker compose en Ubuntu Linux
  •      Paso 1: Verifique si tiene instalado docker compose:
         $ docker-compose --version

  •      Paso 2: Si no está instalado ejecute estos comandos:
  $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  $ sudo chmod +x /usr/local/bin/docker-compose
  $ docker-compose --version




Referencia: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-es
               1. Objetivo del taller 3
               2. Ejercicio 1: Instalar docker compose
               3. Ejercicio 2: Aplicación Multi Contenedor
Contenido      4. Ejercicio propuesto
Contenedores   5. Cierre
      Ejercicio 2:
      Aplicación Multi Contenedor
•   Paso 1: Analice la aplicación multi contenedor




•   Paso 2: Copie por sftp o WinSCP el directorio “compose” a su máquina virtual
    “MV Desarrollo” en /home/ubuntu/
      Ejercicio 2:
      Aplicación Multi Contenedor
•   Paso 3: Analice el archivo docker-compose.yml y los 2 Dockerfile
      Ejercicio 2:
      Aplicación Multi Contenedor
•   Paso 4: Ejecute la aplicación multi contenedor
    $ cd /home/ubuntu/compose
    $ docker-compose up -d               (Ejecuta en segundo plano)

•   Paso 5: Analice las imágenes creadas y los contenedores
    $ docker images
    $ docker ps -a

•   Paso 6: Pruebe la página web y el api-students (reemplace IP en amarillo) con postman o
    https://testfully.io/:
    http://54.209.65.66:8080
    http://54.209.65.66:8000/students       (Métodos POST, GET)
      Ejercicio 2:
      Aplicación Multi Contenedor
•   Paso 7: Detenga la aplicación multi contenedor
    $ docker-compose down

•   Paso 8: Analice las imágenes y los contenedores
    $ docker images
    $ docker ps -a
               1. Objetivo del taller 3
               2. Ejercicio 1: Instalar docker compose
               3. Ejercicio 2: Aplicación Multi Contenedor
Contenido      4. Ejercicio propuesto
Contenedores   5. Cierre
Ejercicio:
Propuesto
Ejercicio a):
• Agregue a la aplicación Multi contenedor la página web plantilla
   en el puerto 8081
• Ejecute la aplicación Multi contenedor y pruébela
               1. Objetivo del taller 3
               2. Ejercicio 1: Instalar docker compose
               3. Ejercicio 2: Aplicación Multi Contenedor
Contenido      4. Ejercicio propuesto
Contenedores   5. Cierre
Cierre:
Contenedores - Qué aprendimos?
•   Instalar docker compose en ubuntu linux
•   Crear y ejecutar una aplicación Multi Contenedor
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
