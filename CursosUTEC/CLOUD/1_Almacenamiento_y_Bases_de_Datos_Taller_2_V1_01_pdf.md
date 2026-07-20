---
curso: CLOUD
titulo: 1. Almacenamiento y Bases de Datos - Taller 2 - V1.01
slides: 23
fuente: 1. Almacenamiento y Bases de Datos - Taller 2 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Almacenamiento y Bases de Datos
Semana 5 - Taller 2: Contenedor MySQL y RDS

                      ELABORADO POR: GERALDO COLCHADO
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Contenedor con MySQL
                         3. Ejercicio 2: Contenedor con Aplicación Web
                            en PHP con acceso a MySQL
Contenido
                         4. Ejercicio 3: MySQL en RDS
Contenedor MySQL y RDS
                         5. Ejercicio propuesto
                         6. Cierre
Objetivo del taller 2:
Contenedor MySQL y RDS
•   Implementar un contenedor con MySQL
•   Implementar contenedor con Aplicación Web con acceso a
    MySQL
•   Implementar MySQL en servicio administrado RDS
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Contenedor con MySQL
                         3. Ejercicio 2: Contenedor con Aplicación Web
                            en PHP con acceso a MySQL
Contenido
                         4. Ejercicio 3: MySQL en RDS
Contenedor MySQL y RDS
                         5. Ejercicio propuesto
                         6. Cierre
        Ejercicio 1:
        Contenedor con MySQL
•   Paso 1: Cree una máquina virtual con la AMI pública más
    reciente de Origen = amazon/Cloud9Ubuntu y nómbrela
    como “MV Bases de Datos” y un nuevo grupo de
    seguridad
•   Paso 2: Asigne una IP fija (IP elástica) a la máquina virtual
            Ejercicio 1:
            Contenedor con MySQL
•   Paso 3: Ingrese a la máquina virtual por ssh a la IP Elástica
•   Paso 4: Abra el puerto 3306 u otro no utilizado por encima de 8000 (Ejemplo: 8005)
•   Paso 5: Cree un volumen para la persistencia de datos de MySQL
    $ docker volume create mysql_data
•   Paso 6: Ejecute el contenedor con la imagen de MySQL
    $ docker run -d --rm --name mysql_c -e MYSQL_ROOT_PASSWORD=utec -p 8005:3306 -v mysql_data:/var/lib/mysql mysql:8.0

     Parámetro                             Comentario
     --rm                                  Para que se borre ($ docker rm) automáticamente el contenedor luego de un $ docker stop

     --name mysql_c                        Asigna un nombre al contenedor en vez de uno aleatorio

     -e MYSQL_ROOT_PASSWORD=utec           Variable de entorno para establecer el password del usuario de base de datos root

     -v mysql_data:/var/lib/mysql          Usa el volumen mysql_data para la persistencia de datos luego que se borre el contenedor
        Ejercicio 1:
        Contenedor con MySQL
•   Paso 7: Conectarse al linux del contenedor   DROP DATABASE IF EXISTS tienda;
    $ docker exec -it mysql_c bash               CREATE DATABASE tienda CHARSET utf8mb4;
                                                 USE tienda;

•   Paso 8: Conectarse al MySQL con password     CREATE TABLE fabricantes (
    utec                                             id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    $ mysql -u root -p                               nombre VARCHAR(100) NOT NULL
                                                 );

•   Paso 9: Crear base de datos tienda y tabla   INSERT INTO fabricantes(nombre) VALUES('Asus');
    fabricantes                                  INSERT INTO fabricantes(nombre) VALUES('Lenovo');
                                                 INSERT INTO fabricantes(nombre) VALUES('Hewlett-Packard');
                                                 INSERT INTO fabricantes(nombre) VALUES('Samsung');
        Ejercicio 1:
        Contenedor con MySQL
•   Paso 10: Consultar tablas

    SHOW TABLES;

•   Paso 11: Consultar datos de tabla

    select * from tienda.fabricantes;

•   Paso 12: Salir
    exit
    exit
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Contenedor con MySQL
                         3. Ejercicio 2: Contenedor con Aplicación Web
                            en PHP con acceso a MySQL
Contenido
                         4. Ejercicio 3: MySQL en RDS
Contenedor MySQL y RDS
                         5. Ejercicio propuesto
                         6. Cierre
       Ejercicio 2:
       Contenedor con Aplicación Web en PHP con acceso a
       MySQL
•   Paso 1: En la máquina virtual “MV Bases de Datos”, abra el puerto 8080 y ejecute:

    $ docker run -d --rm --name adminer_c -p 8080:8080 adminer
        Ejercicio 2:
        Contenedor con Aplicación Web en PHP con acceso a
        MySQL
•   Paso 2: Ingrese desde la aplicación web a la base de datos MySQL con IP Fija de “MV Bases de datos”
       Ejercicio 2:
       Contenedor con Aplicación Web en PHP con acceso a
       MySQL
•   Paso 3: Consultar tabla fabricantes
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Contenedor con MySQL
                         3. Ejercicio 2: Contenedor con Aplicación Web
                            en PHP con acceso a MySQL
Contenido
                         4. Ejercicio 3: MySQL en RDS
Contenedor MySQL y RDS
                         5. Ejercicio propuesto
                         6. Cierre
       Ejercicio 3:
       MySQL en RDS (Servicio administrado)
•   Paso 1: Cree una base de datos MySQL en RDS
       Ejercicio 3:
       MySQL en RDS (Servicio administrado)
•   Paso 2: Obtener password de acceso
       Ejercicio 3:
       MySQL en RDS (Servicio administrado)
•   Paso 3: Habilitar acceso público de la base de datos MySQL
       Ejercicio 3:
       MySQL en RDS (Servicio administrado)
•   Paso 4: Abrir acceso a cualquier origen en regla de entrada de grupo de seguridad
       Ejercicio 3:
       MySQL en RDS (Servicio administrado)
•   Paso 5: Acceda a la base de datos MySQL en RDS desde Adminer
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Contenedor con MySQL
                         3. Ejercicio 2: Contenedor con Aplicación Web
                            en PHP con acceso a MySQL
Contenido
                         4. Ejercicio 3: MySQL en RDS
Contenedor MySQL y RDS
                         5. Ejercicio propuesto
                         6. Cierre
   Ejercicio propuesto (opcional para casa)
a) Investigue e implemente un contenedor con PostgreSQL y acceda con
   Adminer. Suba un archivo con las evidencias en el padlet.

b) Instale en su laptop un SW cliente gráfico de acceso a BD como
   https://dbeaver.io/, https://www.heidisql.com/ u otro de su preferencia y
   acceda a la BD MySQL en contenedor, MySQL en RDS y PostgreSQL en
   contenedor. Suba un archivo con las evidencias en el padlet. Nota: En caso
   tenga problemas de acceso con la red wifi de UTEC pruebe con un acceso
   a internet externo o desde su casa.

                         1. Objetivo del taller 2
                         2. Ejercicio 1: Contenedor con MySQL
                         3. Ejercicio 2: Contenedor con Aplicación Web
                            en PHP con acceso a MySQL
Contenido
                         4. Ejercicio 3: MySQL en RDS
Contenedor MySQL y RDS
                         5. Ejercicio propuesto
                         6. Cierre
Cierre:
Contenedor MySQL y RDS - Qué aprendimos?
•   Implementar un contenedor con MySQL
•   Implementar contenedor con Aplicación Web con acceso a
    MySQL
•   Implementar MySQL en servicio administrado RDS
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
