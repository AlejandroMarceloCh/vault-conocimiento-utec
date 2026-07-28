---
curso: CLOUD
titulo: 1. Almacenamiento y Bases de Datos - Taller 2 - V1.01
slides: 23
fuente: 1. Almacenamiento y Bases de Datos - Taller 2 - V1.01.pdf
---

## Slide 1

Portada del curso (decorativa: logo UTEC en la esquina).

**CS2032 - Cloud Computing (Ciclo 2024-1)**
**Almacenamiento y Bases de Datos**
Semana 5 - Taller 2: Contenedor MySQL y RDS

Elaborado por: Geraldo Colchado

## Slide 2

Slide de índice "Contenido" (banda lateral izquierda naranja con título "Contenido / Contenedor MySQL y RDS"). Lista numerada de contenido, con el punto 1 "Objetivo del taller 2" resaltado en negrita/subrayado como sección activa:

1. **Objetivo del taller 2** (activo)
2. Ejercicio 1: Contenedor con MySQL
3. Ejercicio 2: Contenedor con Aplicación Web en PHP con acceso a MySQL
4. Ejercicio 3: MySQL en RDS
5. Ejercicio propuesto
6. Cierre

## Slide 3

**Objetivo del taller 2: Contenedor MySQL y RDS**

- Implementar un contenedor con MySQL
- Implementar contenedor con Aplicación Web con acceso a MySQL
- Implementar MySQL en servicio administrado RDS

## Slide 4

Slide de índice "Contenido" (mismo formato que slide 2), ahora con el punto 2 "Ejercicio 1: Contenedor con MySQL" resaltado como sección activa. Resto de puntos igual que slide 2.

## Slide 5

**Ejercicio 1: Contenedor con MySQL**

- Paso 1: Cree una máquina virtual con la AMI pública más reciente de Origen = amazon/Cloud9Ubuntu y nómbrela como "MV Bases de Datos" y un nuevo grupo de seguridad (frase "Origen = amazon/Cloud9Ubuntu" resaltada en azul; "nuevo grupo de seguridad" resaltado en amarillo).
- Paso 2: Asigne una IP fija (IP elástica) a la máquina virtual.

Visual — dos capturas de pantalla de la consola AWS EC2, lado izquierdo, mostrando el flujo de asignación de IP elástica:
1. Panel lateral "Red y seguridad" con opciones: Security Groups, Direcciones IP elásticas (marcada con check ✓ rojo), Grupos de ubicación, Pares de claves, Interfaces de red.
2. Botón "Asignar la dirección IP elástica" (marcado con check ✓ rojo).
3. Menú desplegable "Acciones" con opciones: Ver los detalles, Liberar direcciones IP elásticas, **Asociar la dirección IP elástica** (resaltada con flecha roja apuntando a ella), Desasociar la dirección IP elástica, Actualizar DNS inverso.

Visual — íconos decorativos a la derecha: ícono "IP Fija" (chip de CPU), ícono de "Amazon EC2 MV 1 CPU, 1 GB RAM, 10 GB SSD (Ubuntu)", logo de MySQL (elefante/delfín con contenedor naranja/azul apilado) y logo de Docker (ballena azul con contenedores).

## Slide 6

**Ejercicio 1: Contenedor con MySQL**

- Paso 3: Ingrese a la máquina virtual por ssh a la IP Elástica
- Paso 4: Abra el puerto 3306 u otro no utilizado por encima de 8000 (Ejemplo: 8005)
- Paso 5: Cree un volumen para la persistencia de datos de MySQL
  ```
  $ docker volume create mysql_data
  ```
- Paso 6: Ejecute el contenedor con la imagen de MySQL
  ```
  $ docker run -d --rm --name mysql_c -e MYSQL_ROOT_PASSWORD=utec -p 8005:3306 -v mysql_data:/var/lib/mysql mysql:8.0
  ```
  (En el comando, cada parámetro está resaltado con un color distinto: `--rm` en amarillo, `--name mysql_c` en verde, `-e MYSQL_ROOT_PASSWORD=utec` en celeste, `-v mysql_data:/var/lib/mysql` en magenta.)

Visual — tabla explicando cada parámetro del comando docker run:

| Parámetro | Comentario |
|---|---|
| --rm | Para que se borre ($ docker rm) automáticamente el contenedor luego de un $ docker stop |
| --name mysql_c | Asigna un nombre al contenedor en vez de uno aleatorio |
| -e MYSQL_ROOT_PASSWORD=utec | Variable de entorno para establecer el password del usuario de base de datos root |
| -v mysql_data:/var/lib/mysql | Usa el volumen mysql_data para la persistencia de datos luego que se borre el contenedor |

(Cada fila de la columna "Parámetro" mantiene el mismo color de resaltado que en el comando de arriba.)

## Slide 7

**Ejercicio 1: Contenedor con MySQL**

Columna izquierda (pasos):
- Paso 7: Conectarse al linux del contenedor
  ```
  $ docker exec -it mysql_c bash
  ```
- Paso 8: Conectarse al MySQL con password utec
  ```
  $ mysql -u root -p
  ```
- Paso 9: Crear base de datos tienda y tabla fabricantes

Columna derecha (código SQL):
```sql
DROP DATABASE IF EXISTS tienda;
CREATE DATABASE tienda CHARSET utf8mb4;
USE tienda;

CREATE TABLE fabricantes (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO fabricantes(nombre) VALUES('Asus');
INSERT INTO fabricantes(nombre) VALUES('Lenovo');
INSERT INTO fabricantes(nombre) VALUES('Hewlett-Packard');
INSERT INTO fabricantes(nombre) VALUES('Samsung');
```

## Slide 8

**Ejercicio 1: Contenedor con MySQL**

- Paso 10: Consultar tablas
  ```sql
  SHOW TABLES;
  ```
- Paso 11: Consultar datos de tabla
  ```sql
  select * from tienda.fabricantes;
  ```
- Paso 12: Salir
  ```
  exit
  exit
  ```

## Slide 9

Slide de índice "Contenido" (mismo formato), ahora con el punto 3 "Ejercicio 2: Contenedor con Aplicación Web en PHP con acceso a MySQL" resaltado como sección activa.

## Slide 10

**Ejercicio 2: Contenedor con Aplicación Web en PHP con acceso a MySQL**

- Paso 1: En la máquina virtual "MV Bases de Datos", abra el puerto 8080 y ejecute:
  ```
  $ docker run -d --rm --name adminer_c -p 8080:8080 adminer
  ```

Visual — captura de la página de Docker Hub de la imagen oficial "adminer": logo Adminer (icono de base de datos con signo de interrogación), texto "adminer" con badge verde "DOCKER OFFICIAL IMAGE" y descripción "Database management in a single PHP file."

## Slide 11

**Ejercicio 2: Contenedor con Aplicación Web en PHP con acceso a MySQL**

- Paso 2: Ingrese desde la aplicación web a la base de datos MySQL con IP Fija de "MV Bases de datos"

Visual — captura de pantalla del navegador mostrando el formulario de login de Adminer 4.8.1 en la URL `52.45.145.63:8080` (resaltada en amarillo). Formulario "Login":
- Motor de base de datos: MySQL
- Servidor: 52.45.145.63:8005 (resaltado en amarillo, IP y puerto correspondiente al contenedor MySQL del Ejercicio 1)
- Usuario: root
- Contraseña: •••• (oculta)
- Base de datos: (vacío)
- Botón "Login" y checkbox "Guardar contraseña"

## Slide 12

**Ejercicio 2: Contenedor con Aplicación Web en PHP con acceso a MySQL**

- Paso 3: Consultar tabla fabricantes

Visual — captura de pantalla de Adminer tras login exitoso, navegador en `52.45.145.63:8080/?server=52.45.145.63%3A8005&username=root&db=tienda&sql=select%20*%20from...`:
- Ruta de navegación: MySQL » 52.45.145.63:8005 » tienda » Comando SQL
- Panel izquierdo: DB: tienda (dropdown), menú con "Comando SQL" (resaltado en amarillo), Importar, Exportar, Crear tabla, enlace "registros fabricantes"
- Panel derecho, título "Comando SQL", caja con la consulta resaltada en amarillo: `select * from fabricantes`
- Resultado en tabla:

| id | nombre |
|---|---|
| 1 | Asus |
| 2 | Lenovo |
| 3 | Hewlett-Packard |
| 4 | Samsung |

- Pie: "4 registros (0.002 s)" con enlaces Modificar, Explain, Exportar
- Debajo, caja de comando repetida: `select * from fabricantes;`

## Slide 13

Slide de índice "Contenido" (mismo formato), ahora con el punto 4 "Ejercicio 3: MySQL en RDS" resaltado como sección activa.

## Slide 14

**Ejercicio 3: MySQL en RDS (Servicio administrado)**

- Paso 1: Cree una base de datos MySQL en RDS

Visual — captura de la consola AWS RDS, pantalla "Crear base de datos" (RDS > Create database):
- "Elegir un método de creación de base de datos": dos opciones tipo radio: "Creación estándar" (no seleccionada) vs "Creación sencilla" (seleccionada, con descripción "Utilice las configuraciones recomendadas...").
- Sección "Configuración" > "Tipo de motor": tres opciones con logos — Amazon Aurora, **MySQL** (seleccionado, ícono elefante/delfín naranja-azul), MariaDB (logo foca).
- Panel derecho: recuadro "Capa gratuita" seleccionado, con specs: db.t3.micro, 2 vCPUs, 1 GiB RAM, 20 GiB, 0.020 USD/hora.
- Campo "Identificador de instancias de bases de datos": `database-1` (resaltado en amarillo).
- Campo "Nombre de usuario maestro": `admin`.
- Checkbox marcado: "Generación automática de contraseña" (Amazon RDS puede generar una contraseña).

## Slide 15

**Ejercicio 3: MySQL en RDS (Servicio administrado)**

- Paso 2: Obtener password de acceso

Visual — captura de la consola AWS RDS tras crear la BD:
- Banner verde de éxito: "Se ha creado correctamente la base de datos database-1. We have generated your database master password during the database creation and it will be displayed in the connection details. This is the only time you will be able to view this password..." con botón "View connection details" (check verde).
- Panel "Detalles de conexión a la base de datos database-1" con aviso de que la contraseña solo se muestra una vez:
  - Nombre de usuario maestro: admin
  - Contraseña maestra: `BgGb2L553R9MHinDp5he` (con botón Copy) — valor de ejemplo generado automáticamente por AWS para la demo del taller.
  - Punto de enlace (endpoint): `database-1.clkq26zjxpyk.us-east-1.rds.amazonaws.com` (con botón Copy)

## Slide 16

**Ejercicio 3: MySQL en RDS (Servicio administrado)**

- Paso 3: Habilitar acceso público de la base de datos MySQL

Visual — captura de consola AWS RDS, sección "Configuración adicional" > "Acceso público":
- Opción seleccionada (radio button azul): **"Accesible públicamente"** (resaltado en amarillo) — con descripción "RDS asigna una dirección IP pública a la base de datos. Las instancias de Amazon EC2 y otros recursos fuera de la VPC pueden conectarse a la base de datos..."
- Opción no seleccionada: "No accesible públicamente"
- Campo "Puerto de la base de datos": `3306` (resaltado en amarillo)
- Panel lateral derecho: "Estado ▽ / ✓ Disponible" (indicador verde de que la instancia RDS ya está activa)

## Slide 17

**Ejercicio 3: MySQL en RDS (Servicio administrado)**

- Paso 4: Abrir acceso a cualquier origen en regla de entrada de grupo de seguridad

Visual — captura de consola AWS EC2, pantalla "Editar reglas de entrada" del grupo de seguridad `sg-0257470dae2a3e82b - bd`:
- Tabla "Reglas de entrada" con columnas: ID de la regla, Tipo, Protocolo, Intervalo de puertos, Origen, Descripción.
- Fila: ID `sgr-089317957cbf66bc1`, Tipo `MYSQL/Aurora` (dropdown), Protocolo `TCP`, Intervalo de puertos `3306` (resaltado en amarillo), Origen `Anywh...` con valor `0.0.0.0/0` (resaltado en amarillo/celeste) — es decir, acceso abierto desde cualquier IP.
- Botones: "Agregar regla", y al pie "Cancelar", "Previsualizar los cambios", "Guardar reglas" (marcado con check verde).

## Slide 18

**Ejercicio 3: MySQL en RDS (Servicio administrado)**

- Paso 5: Acceda a la base de datos MySQL en RDS desde Adminer

Visual — captura del navegador con el formulario de login de Adminer 4.8.1 en `52.45.145.63:8080`. Formulario "Login":
- Motor de base de datos: MySQL
- Servidor: `database-1.clkq26zjxpyk.us...` (resaltado en amarillo, truncado — es el endpoint de RDS)
- Usuario: `admin` (resaltado en amarillo)
- Contraseña: •••••••••••••••••• (oculta, resaltada en amarillo)
- Base de datos: (vacío)
- Botón "Login" y checkbox "Guardar contraseña"

## Slide 19

Slide de índice "Contenido" (mismo formato), ahora con el punto 5 "Ejercicio propuesto" resaltado como sección activa.

## Slide 20

**Ejercicio propuesto (opcional para casa)**

a) Investigue e implemente un contenedor con PostgreSQL y acceda con Adminer. Suba un archivo con las evidencias en el padlet.

b) Instale en su laptop un SW cliente gráfico de acceso a BD como https://dbeaver.io/, https://www.heidisql.com/ u otro de su preferencia y acceda a la BD MySQL en contenedor, MySQL en RDS y PostgreSQL en contenedor. Suba un archivo con las evidencias en el padlet. Nota: En caso tenga problemas de acceso con la red wifi de UTEC pruebe con un acceso a internet externo o desde su casa.

## Slide 21

Slide de índice "Contenido" (mismo formato), ahora con el punto 6 "Cierre" resaltado como sección activa.

## Slide 22

**Cierre: Contenedor MySQL y RDS - ¿Qué aprendimos?**

- Implementar un contenedor con MySQL
- Implementar contenedor con Aplicación Web con acceso a MySQL
- Implementar MySQL en servicio administrado RDS

## Slide 23

Slide de cierre (decorativa): texto centrado "Gracias" y debajo "Elaborado por docente: Geraldo Colchado".
