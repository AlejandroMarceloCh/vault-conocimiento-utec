---
curso: CLOUD
titulo: 1. Contenedores - Taller 2 - V1.01
slides: 13
fuente: 1. Contenedores - Taller 2 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Virtualización con contenedores
Semana 3 - Taller 2: Contenedores

                      ELABORADO POR: GERALDO COLCHADO
               1. Objetivo del taller 2
               2. Ejercicio 1: Subir imagen a hub.docker.com
               3. Ejercicio 2: Desplegar contenedor en otras
                  computadoras
Contenido
               4. Ejercicio propuesto
Contenedores
               5. Cierre
Objetivo del taller 2:
Contenedores
•   Aprender a subir imagen a hub.docker.com
•   Aprender a desplegar un contenedor en otras computadoras
               1. Objetivo del taller 2
               2. Ejercicio 1: Subir imagen a hub.docker.com
               3. Ejercicio 2: Desplegar contenedor en otras
                  computadoras
Contenido
               4. Ejercicio propuesto
Contenedores
               5. Cierre
Ejercicio 1:
Subir imagen a hub.docker.com
• Paso 1: Cree una cuenta o usuario en https://hub.docker.com/ (Docker
  Registry) e ingrese
• Paso 2: Cree un repositorio público con el nombre api-students
• Paso 3: Ingrese a hub docker (Docker Registry) con este comando:
   $ docker login -u gcolchado                         (Reemplace amarillo)
• Paso 4: Asigne nuevo nombre (tag) a la imagen local api-students:
   $ docker tag api-students gcolchado/api-students (Reemplace amarillo)
• Paso 5: Suba su imagen al repositorio público creado
   $ docker push gcolchado/api-students                (Reemplace amarillo)
• Paso 6: Salga del hub docker (Docker Registry)
   $ docker logout
               1. Objetivo del taller 2
               2. Ejercicio 1: Subir imagen a hub.docker.com
               3. Ejercicio 2: Desplegar contenedor en otras
                  computadoras
Contenido
               4. Ejercicio propuesto
Contenedores
               5. Cierre
Ejercicio 2:
Desplegar contenedor en otras computadoras
• Paso 1: Cree otra máquina virtual y nómbrela como “MV Pruebas”, abra el
  puerto 8000 y luego ingrese por ssh

• Paso 2: Ejecute el contenedor de la imagen pública:

   $ docker run -d -p 8000:8000 gcolchado/api-students   (Reemplace amarillo)

• Paso 3: Pruebe con postman
Ejercicio 2 (Opcional para la casa):
Desplegar contenedor en otras computadoras
• Paso 1: En la computadora del laboratorio (Windows) o en su laptop (Windows
  o Mac OS o Linux) verifique si está instalado el docker y en caso no está lo debe
  instalar.

   docker -v

• Paso 2: Ejecute el contenedor de la imagen pública:

   docker run -d -p 8000:8000 gcolchado/api-students (Reemplace amarillo)

• Paso 3: Pruebe con postman
               1. Objetivo del taller 2
               2. Ejercicio 1: Subir imagen a hub.docker.com
               3. Ejercicio 2: Desplegar contenedor en otras
                  computadoras
Contenido
               4. Ejercicio propuesto
Contenedores
               5. Cierre
Ejercicio:
Propuesto
Ejercicio a):
• Suba la imagen websimple a hub.docker.com
• Despliegue el contenedor en otras computadoras puerto 8080

Ejercicio b):
• Cree una imagen webplantilla con dockerfile
• Suba la imagen webplantilla a hub.docker.com
• Despliegue el contenedor en otras computadoras puerto 8081
               1. Objetivo del taller 2
               2. Ejercicio 1: Subir imagen a hub.docker.com
               3. Ejercicio 2: Desplegar contenedor en otras
                  computadoras
Contenido
               4. Ejercicio propuesto
Contenedores
               5. Cierre
Cierre:
Contenedores - Qué aprendimos?
•   Subir imagen a hub.docker.com
•   Desplegar un contenedor en otras computadoras
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
