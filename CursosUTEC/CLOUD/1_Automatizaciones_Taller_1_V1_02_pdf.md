---
curso: CLOUD
titulo: 1. Automatizaciones - Taller 1 - V1.02
slides: 20
fuente: 1. Automatizaciones - Taller 1 - V1.02.pdf
---

## Slide 1

Portada del taller. Texto: "CS2032 - Cloud Computing (Ciclo 2024-1) / Automatizaciones / Semana 7 - Taller 1: Automatizar comandos en Linux". Autoría: "Elaborado por: Geraldo Colchado". Logo UTEC en esquina superior derecha (decorativo). Franja naranja horizontal decorativa en el borde inferior.

## Slide 2

Slide de agenda "Contenido - Automatizaciones", con panel lateral izquierdo naranja/marrón. Lista numerada de 7 puntos (ítem 1 resaltado en negrita/naranja para indicar que es la sección actual):
1. **Objetivo del taller 1** (resaltado)
2. Ejercicio 1: Shell script con comandos linux
3. Ejercicio 2: Shell script con comandos docker para iniciar Bases de Datos
4. Ejercicio 3: Shell script con comandos docker para detener Bases de Datos
5. Ejercicio 4: Automatizar ejecución de contenedores de BD al iniciar Linux
6. Ejercicio 5: Automatizar ejecución de contenedores en 2 MV de Producción
7. Cierre

## Slide 3

Título "Objetivo del taller 1: Automatizaciones". Lista con 2 bullets:
- Aprender a automatizar comandos en Linux
- Aprender a ejecutar comandos automáticamente en el inicio de Linux

## Slide 4

Misma slide de agenda "Contenido" que la slide 2, pero ahora resaltado el ítem 2: **Ejercicio 1: Shell script con comandos linux**.

## Slide 5

Título "Ejercicio 1: Shell script con comandos linux". Párrafo explicativo (con palabras clave resaltadas en azul: "automatizar su ejecución", "bash", "lenguaje de programación"): un shell script es un archivo que contiene comandos Linux y permite automatizar su ejecución; el intérprete más conocido en Linux es bash, que también tiene funcionalidades de lenguaje de programación estructurado (variables, lectura de datos, impresión en pantalla, estructuras selectivas y repetitivas).

## Slide 6

Título "Ejercicio 1: Shell script con comandos linux". Instrucciones paso a paso:
- Paso 1: Ingrese por ssh a MV "MV Pruebas"
- Paso 2: Cree el directorio /home/ubuntu/automatizar
- Paso 3: Cree el archivo script1.sh con este contenido (bloque de código, comandos linux en negrita):

```bash
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
```

## Slide 7

Título "Ejercicio 1: Shell script con comandos linux". Continuación:
- Paso 4: Adicione permisos de ejecución al archivo.
```bash
$ chmod +x script1.sh
```
- Paso 5: Ejecute el script.
```bash
$ ./script1.sh
```

## Slide 8

Misma slide de agenda "Contenido", ahora resaltado el ítem 3: **Ejercicio 2: Shell script con comandos docker para iniciar Bases de Datos**.

## Slide 9

Título "Ejercicio 2: Shell script con comandos docker para iniciar Bases de Datos". Pasos:
- Paso 1: Ingrese por ssh a MV "MV Bases de Datos"
- Paso 2: Cree el directorio /home/ubuntu/automatizar
- Paso 3: Cree el archivo **bd-start.sh** con este contenido (comandos docker en negrita):

```bash
echo "Iniciando contenedores para MySQL"
echo "----------------------------------"
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
```

## Slide 10

Título "Ejercicio 2: Shell script con comandos docker para iniciar Bases de Datos". Continuación:
- Paso 4: Adicione permisos de ejecución al archivo.
```bash
$ chmod +x bd-start.sh
```
- Paso 5: Ejecute el script.
```bash
$ ./bd-start.sh
```

## Slide 11

Misma slide de agenda "Contenido", ahora resaltado el ítem 4: **Ejercicio 3: Shell script con comandos docker para detener Bases de Datos**.

## Slide 12

Título "Ejercicio 3: Shell script con comandos docker para detener Bases de Datos". Pasos:
- Paso 1: Ingrese por ssh a MV "MV Bases de Datos"
- Paso 2: Cree el directorio /home/ubuntu/automatizar
- Paso 3: Cree el archivo **bd-stop.sh** con este contenido (comandos docker en negrita):

```bash
echo "Deteniendo contenedores para MySQL"
echo "-----------------------------------"
docker stop mysql_c
docker stop adminer_c

echo ""
echo "Deteniendo contenedor de MongoDB"
echo "---------------------------------"
docker stop mongo_c

echo ""
echo "Contenedores en ejecución"
echo "-------------------------"
docker ps -a
```

## Slide 13

Título "Ejercicio 3: Shell script con comandos docker para detener Bases de Datos". Continuación:
- Paso 4: Adicione permisos de ejecución al archivo.
```bash
$ chmod +x bd-stop.sh
```
- Paso 5: Ejecute el script.
```bash
$ ./bd-stop.sh
```

## Slide 14

Misma slide de agenda "Contenido", ahora resaltado el ítem 5: **Ejercicio 4: Automatizar ejecución de contenedores de BD al iniciar Linux**.

## Slide 15

Título "Ejercicio 4: Automatizar ejecución de contenedores de BD al iniciar Linux". Pasos:
- Paso 1: En "MV Bases de Datos", ejecute este comando:
```bash
sudo crontab -e
```
- Paso 2: Agregue esta línea al final del archivo:
```
@reboot /home/ubuntu/automatizar/bd-start.sh
```
- Paso 3: "Detener" y luego "Iniciar" la MV "MV Bases de Datos" o "Reiniciar", y luego ingrese por ssh y ejecute este comando para ver si se han ejecutado automáticamente los 3 contenedores:
```bash
docker ps
```

## Slide 16

Misma slide de agenda "Contenido", ahora resaltado el ítem 6: **Ejercicio 5: Automatizar ejecución de contenedores en 2 MV de Producción**.

## Slide 17

Título "Ejercicio 5: Automatizar ejecución de contenedores en 2 MV de Producción". Pasos:
- Paso 1: Elabore un script para iniciar y otro para detener estos contenedores en sus 2 MV de Producción (nombres de imagen docker con el prefijo "gcolchado" resaltado en amarillo, indicando que debe reemplazarse por el usuario del alumno):

| Imagen docker | Nota |
|---|---|
| gcolchado/websimple | (Reemplace amarillo por su usuario) |
| gcolchado/api-employees | (Reemplace amarillo por su usuario) |
| gcolchado/api-fruits | (Reemplace amarillo por su usuario) |

- Paso 2: Automatice con crontab el inicio de los 3 contenedores al iniciar Linux
- Paso 3: Suba su evidencia (script, foto, enlace para probar) en el padlet indicado por el profesor.

## Slide 18

Misma slide de agenda "Contenido", ahora resaltado el ítem 7: **Cierre**.

## Slide 19

Título "Cierre: Automatizaciones - Qué aprendimos?". Lista con 2 bullets:
- Automatizar comandos en Linux
- Ejecutar comandos automáticamente en el inicio de Linux

## Slide 20

Slide de cierre. Texto centrado "Gracias" y debajo "Elaborado por docente: Geraldo Colchado". Sin elementos visuales adicionales (decorativa).
