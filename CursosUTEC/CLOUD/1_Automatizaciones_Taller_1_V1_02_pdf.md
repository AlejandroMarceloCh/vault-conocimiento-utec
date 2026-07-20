---
curso: CLOUD
titulo: 1. Automatizaciones - Taller 1 - V1.02
slides: 20
fuente: 1. Automatizaciones - Taller 1 - V1.02.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Automatizaciones
Semana 7 - Taller 1: Automatizar comandos en Linux

                      ELABORADO POR: GERALDO COLCHADO
                   1. Objetivo del taller 1
                   2. Ejercicio 1: Shell script con comandos linux
                   3. Ejercicio 2: Shell script con comandos
                      docker para iniciar Bases de Datos
Contenido
                   4. Ejercicio 3: Shell script con comandos
Automatizaciones
                      docker para detener Bases de Datos
                   5. Ejercicio 4: Automatizar ejecución de
                      contenedores de BD al iniciar Linux
                   6. Ejercicio 5: Automatizar ejecución de
                      contenedores en 2 MV de Producción
                   7. Cierre
Objetivo del taller 1:
Automatizaciones
• Aprender a automatizar comandos en Linux
• Aprender a ejecutar comandos automáticamente en el inicio de
  Linux
                   1. Objetivo del taller 1
                   2. Ejercicio 1: Shell script con comandos linux
                   3. Ejercicio 2: Shell script con comandos
                      docker para iniciar Bases de Datos
Contenido
                   4. Ejercicio 3: Shell script con comandos
Automatizaciones
                      docker para detener Bases de Datos
                   5. Ejercicio 4: Automatizar ejecución de
                      contenedores de BD al iniciar Linux
                   6. Ejercicio 5: Automatizar ejecución de
                      contenedores en 2 MV de Producción
                   7. Cierre
Ejercicio 1:
Shell script con comandos linux

Un shell script es un archivo que contiene comandos Linux y que
permite automatizar su ejecución. El intérprete de comandos más
conocido en Linux es bash que tiene funcionalidades también de
lenguaje de programación estructurado y se pueden declarar
variables, hacer lectura de datos, imprimir en pantalla y utilizar
estructuras selectivas y repetitivas.
Ejercicio 1:
Shell script con comandos linux
• Paso 1: Ingrese por ssh a MV “MV Pruebas”
• Paso 2: Cree el directorio /home/ubuntu/automatizar
• Paso 3: Cree el archivo script1.sh con este contenido
echo "Mi primer shell script"
echo "----------------------"
echo "--- Soy el usuario: "
whoami
echo "--- Pertenezco a estos grupos: "
id
echo "--- Me encuentro en este directorio: "
pwd
echo "--- Tengo instalada esta version de docker: "
docker -v
Ejercicio 1:
Shell script con comandos linux
• Paso 4: Adicione permisos de ejecución al archivo.
$ chmod +x script1.sh

• Paso 5: Ejecute el script.
$ ./script1.sh
                   1. Objetivo del taller 1
                   2. Ejercicio 1: Shell script con comandos linux
                   3. Ejercicio 2: Shell script con comandos
                      docker para iniciar Bases de Datos
Contenido
                   4. Ejercicio 3: Shell script con comandos
Automatizaciones
                      docker para detener Bases de Datos
                   5. Ejercicio 4: Automatizar ejecución de
                      contenedores de BD al iniciar Linux
                   6. Ejercicio 5: Automatizar ejecución de
                      contenedores en 2 MV de Producción
                   7. Cierre
     Ejercicio 2:
     Shell script con comandos docker para iniciar Bases de
     Datos
•    Paso 1: Ingrese por ssh a MV “MV Bases de Datos”
•    Paso 2: Cree el directorio /home/ubuntu/automatizar
•    Paso 3: Cree el archivo bd-start.sh con este contenido
echo "Iniciando contenedores para MySQL"
echo "---------------------------------"
docker run -d --rm --name mysql_c -e MYSQL_ROOT_PASSWORD=utec -p 8005:3306 -v mysql_data:/var/lib/mysql mysql:8.0
docker run -d --rm --name adminer_c -p 8080:8080 adminer

echo ""
echo "Iniciando contenedor de MongoDB"
echo "-------------------------------"
docker run -d --rm --name mongo_c -p 27017:27017 -v mongo_data:/data/db mongo:latest

echo ""
echo "Contenedores en ejecución"
echo "-------------------------"
docker ps
Ejercicio 2:
Shell script con comandos docker para iniciar Bases de
Datos

• Paso 4: Adicione permisos de ejecución al archivo.
$ chmod +x bd-start.sh

• Paso 5: Ejecute el script.
$ ./bd-start.sh
                   1. Objetivo del taller 1
                   2. Ejercicio 1: Shell script con comandos linux
                   3. Ejercicio 2: Shell script con comandos
                      docker para iniciar Bases de Datos
Contenido
                   4. Ejercicio 3: Shell script con comandos
Automatizaciones
                      docker para detener Bases de Datos
                   5. Ejercicio 4: Automatizar ejecución de
                      contenedores de BD al iniciar Linux
                   6. Ejercicio 5: Automatizar ejecución de
                      contenedores en 2 MV de Producción
                   7. Cierre
    Ejercicio 3:
    Shell script con comandos docker para detener Bases
    de Datos
•   Paso 1: Ingrese por ssh a MV “MV Bases de Datos”
•   Paso 2: Cree el directorio /home/ubuntu/automatizar
•   Paso 3: Cree el archivo bd-stop.sh con este contenido
echo "Deteniendo contenedores para MySQL"
echo "----------------------------------"
docker stop mysql_c
docker stop adminer_c

echo ""
echo "Deteniendo contenedor de MongoDB"
echo "--------------------------------"
docker stop mongo_c

echo ""
echo "Contenedores en ejecución"
echo "-------------------------"
docker ps -a
Ejercicio 3:
Shell script con comandos docker para detener Bases
de Datos

• Paso 4: Adicione permisos de ejecución al archivo.
$ chmod +x bd-stop.sh

• Paso 5: Ejecute el script.
$ ./bd-stop.sh
                   1. Objetivo del taller 1
                   2. Ejercicio 1: Shell script con comandos linux
                   3. Ejercicio 2: Shell script con comandos
                      docker para iniciar Bases de Datos
Contenido
                   4. Ejercicio 3: Shell script con comandos
Automatizaciones
                      docker para detener Bases de Datos
                   5. Ejercicio 4: Automatizar ejecución de
                      contenedores de BD al iniciar Linux
                   6. Ejercicio 5: Automatizar ejecución de
                      contenedores en 2 MV de Producción
                   7. Cierre
Ejercicio 4:
Automatizar ejecución de contenedores de BD al iniciar
Linux
• Paso 1: En “MV Bases de Datos”, ejecute este comando:
sudo crontab -e

• Paso 2: Agregue esta línea al final del archivo
@reboot /home/ubuntu/automatizar/bd-start.sh

•  Paso 3: “Detener” y luego “Iniciar” la MV “MV Bases de Datos” o “Reiniciar”
   y luego ingrese por ssh y ejecute este comando para ver si se han ejecutado
   automáticamente los 3 contenedores
docker ps
                   1. Objetivo del taller 1
                   2. Ejercicio 1: Shell script con comandos linux
                   3. Ejercicio 2: Shell script con comandos
                      docker para iniciar Bases de Datos
Contenido
                   4. Ejercicio 3: Shell script con comandos
Automatizaciones
                      docker para detener Bases de Datos
                   5. Ejercicio 4: Automatizar ejecución de
                      contenedores de BD al iniciar Linux
                   6. Ejercicio 5: Automatizar ejecución de
                      contenedores en 2 MV de Producción
                   7. Cierre
Ejercicio 5:
Automatizar ejecución de contenedores en 2 MV de
Producción
•  Paso 1: Elabore un script para iniciar y otro para detener estos contenedores
   en sus 2 MV de Producción:
gcolchado/websimple           (Reemplace amarillo por su usuario)
gcolchado/api-employees       (Reemplace amarillo por su usuario)
gcolchado/api-fruits          (Reemplace amarillo por su usuario)

•   Paso 2: Automatice con crontab el inicio de los 3 contenedores al iniciar
    Linux

•   Paso 3: Suba su evidencia (script, foto, enlace para probar) en el padlet
    indicado por el profesor.
                   1. Objetivo del taller 1
                   2. Ejercicio 1: Shell script con comandos linux
                   3. Ejercicio 2: Shell script con comandos
                      docker para iniciar Bases de Datos
Contenido
                   4. Ejercicio 3: Shell script con comandos
Automatizaciones
                      docker para detener Bases de Datos
                   5. Ejercicio 4: Automatizar ejecución de
                      contenedores de BD al iniciar Linux
                   6. Ejercicio 5: Automatizar ejecución de
                      contenedores en 2 MV de Producción
                   7. Cierre
Cierre:
Automatizaciones - Qué aprendimos?
• Automatizar comandos en Linux
• Ejecutar comandos automáticamente en el inicio de Linux
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
