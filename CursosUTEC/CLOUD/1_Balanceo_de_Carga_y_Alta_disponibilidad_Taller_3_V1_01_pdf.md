---
curso: CLOUD
titulo: 1. Balanceo de Carga y Alta disponibilidad - Taller 3 - V1.01
slides: 23
fuente: 1. Balanceo de Carga y Alta disponibilidad - Taller 3 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Balanceo de Carga y Alta disponibilidad
Semana 7 - Taller 3: Balanceador de Carga

                       ELABORADO POR: GERALDO COLCHADO
                       1. Objetivo del taller 3
                       2. Ejercicio 1: Crear contenedor de MongoDB
                          en MV Bases de datos
                       3. Ejercicio 2: Crear contenedor de api-fruits
Contenido                 con acceso a MongoDB en MV Desarrollo
Balanceador de Carga   4. Ejercicio 3: Desplegar contenedor api-fruits
                          en 2 MV de producción
                       5. Ejercicio 4: Configurar y probar Balanceador
                          de Carga
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
Objetivo del taller 3:
Balanceador de Carga
• Probar Balanceo de Carga y Alta disponibilidad con Api REST con
  acceso a base de datos MongoDB (NoSQL)
                       1. Objetivo del taller 3
                       2. Ejercicio 1: Crear contenedor de MongoDB
                          en MV Bases de datos
                       3. Ejercicio 2: Crear contenedor de api-fruits
Contenido                 con acceso a MongoDB en MV Desarrollo
Balanceador de Carga   4. Ejercicio 3: Desplegar contenedor api-fruits
                          en 2 MV de producción
                       5. Ejercicio 4: Configurar y probar Balanceador
                          de Carga
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
          Ejercicio 1:
          Crear contenedor de MongoDB en MV Bases de datos
•   Paso 1: Ingrese a la máquina virtual “MV Bases de datos” por ssh a la IP Elástica
•   Paso 2: Ejecute el contenedor de MongoDB:
    $ docker run -d --rm --name mongo_c -p 27017:27017 -v mongo_data:/data/db mongo:latest
•   Paso 3: Dado que el MongoDB se está ejecutando sin usuario y password (no tiene seguridad), sólo debe ser
    accedido por máquinas virtuales de la misma red local y no de internet por lo que en el grupo de seguridad de
    la máquina virtual “MV Bases de datos” abra el puerto 27017 tanto para el mismo grupo de seguridad como
    para el grupo de seguridad de MV Desarrollo y MV Pruebas y para el grupo de seguridad de producción “GS-
    Prod”
        Ejercicio 1:
        Crear contenedor de MongoDB en MV Bases de datos
                                                  use food
•   Paso 4: Conectarse al linux del contenedor
    $ docker exec -it mongo_c bash                db.createCollection("fruits")

•   Paso 5: Conectarse al MongoDB                 db.fruits.insertMany([ {name: "apple", origin: "usa", price: 5},
                                                  {name: "orange", origin: "italy", price: 3}, {name: "mango",
    # mongosh                                     origin: "malaysia", price: 3} ])

•   Paso 6: Crear base de datos “food”,           db.fruits.find().pretty()
    colección “fruits”, consultar datos y salir
                                                  exit

                                                  exit
                       1. Objetivo del taller 3
                       2. Ejercicio 1: Crear contenedor de MongoDB
                          en MV Bases de datos
                       3. Ejercicio 2: Crear contenedor de api-fruits
Contenido                 con acceso a MongoDB en MV Desarrollo
Balanceador de Carga   4. Ejercicio 3: Desplegar contenedor api-fruits
                          en 2 MV de producción
                       5. Ejercicio 4: Configurar y probar Balanceador
                          de Carga
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
             Ejercicio 2:
             Crear contenedor de api-fruits con acceso a MongoDB
             en MV Desarrollo
       •     Paso 1: En MV “MV Desarrollo” cree el directorio /home/ubuntu/api-fruits y
             copie por sftp o WinSCP los archivos indicados por el profesor.
       •     Paso 2: Analice el Dockerfile y app.py. En app.py reemplace por IP privada
             de su MV “MV Bases de datos”




       •     Paso 3: Cree la imagen
             $ docker build -t api-fruits .
Referencia del api-fruits: https://ishmeet1995.medium.com/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc
    Ejercicio 2:
    Crear contenedor de api-fruits con acceso a MongoDB
    en MV Desarrollo
•   Paso 4: Suba la imagen a https://hub.docker.com
    Ingrese a https://hub.docker.com con su usuario
    Cree un repositorio público con el nombre api-fruits
    $ docker login -u gcolchado                     (Reemplace amarillo)
    $ docker tag api-fruits gcolchado/api-fruits    (Reemplace amarillo)
    $ docker push gcolchado/api-fruits              (Reemplace amarillo)
    $ docker logout
    Ejercicio 2:
    Crear contenedor de api-fruits con acceso a MongoDB
    en MV Desarrollo
•   Paso 5: Ejecute el contenedor:
    $ docker run -d --rm --name api-fruits_c -p 8001:8001 api-fruits

•   Paso 6: Abra el puerto 8001 en el grupo de seguridad de MV “MV
    Desarrollo”

•   Paso 7: Pruebe en postman o testfully el api-fruits con la IP de la MV “MV
    Desarrollo”
Ejercicio 2:
Crear contenedor de api-fruits con acceso a MongoDB
en MV Desarrollo
    Consultar frutas                Crear fruta
Ejercicio 2:
Crear contenedor de api-fruits con acceso a MongoDB
en MV Desarrollo
     Modificar fruta                 Eliminar fruta
                       1. Objetivo del taller 3
                       2. Ejercicio 1: Crear contenedor de MongoDB
                          en MV Bases de datos
                       3. Ejercicio 2: Crear contenedor de api-fruits
Contenido                 con acceso a MongoDB en MV Desarrollo
Balanceador de Carga   4. Ejercicio 3: Desplegar contenedor api-fruits
                          en 2 MV de producción
                       5. Ejercicio 4: Configurar y probar Balanceador
                          de Carga
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
    Ejercicio 3:
    Desplegar contenedor api-fruits en 2 MV de producción
•   Paso 1: Ingrese por ssh y ejecute el contenedor en las 2 MV de producción
    $ docker run -d --rm --name api-fruits_c -p 8001:8001 gcolchado/api-fruits
                       1. Objetivo del taller 3
                       2. Ejercicio 1: Crear contenedor de MongoDB
                          en MV Bases de datos
                       3. Ejercicio 2: Crear contenedor de api-fruits
Contenido                 con acceso a MongoDB en MV Desarrollo
Balanceador de Carga   4. Ejercicio 3: Desplegar contenedor api-fruits
                          en 2 MV de producción
                       5. Ejercicio 4: Configurar y probar
                          Balanceador de Carga
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
    Ejercicio 4:
    Configurar y probar Balanceador de Carga
•   Paso 1: En grupo de seguridad “GS-Prod”, que usan las 2 MV de producción,
    abra puerto 8001
•   Paso 2: Crear un Target Group con las 2 MV de producción para el puerto
    8001
    Ejercicio 4:
    Configurar y probar Balanceador de Carga
•   Paso 3: Agregue un agente de escucha en el Balanceador de Carga
          Ejercicio 4:
          Configurar y probar Balanceador de Carga

•   Paso 4: Pruebe en postman el balanceador de carga varias veces.
•   Paso 5: Detener la instancia “MV Prod 1” y probar
•   Paso 6: Detener la instancia “MV Prod 2” y probar
•   Paso 7: Iniciar la instancia “MV Prod 1”, ejecutar el contenedor y probar
    $ docker run -d --rm --name api-fruits_c -p 8001:8001 gcolchado/api-fruits
•   Paso 8: Iniciar la instancia “MV Prod 2”, ejecutar el contenedor y probar
    $ docker run -d --rm --name api-fruits_c -p 8001:8001 gcolchado/api-fruits
                       1. Objetivo del taller 3
                       2. Ejercicio 1: Crear contenedor de MongoDB
                          en MV Bases de datos
                       3. Ejercicio 2: Crear contenedor de api-fruits
Contenido                 con acceso a MongoDB en MV Desarrollo
Balanceador de Carga   4. Ejercicio 3: Desplegar contenedor api-fruits
                          en 2 MV de producción
                       5. Ejercicio 4: Configurar y probar Balanceador
                          de Carga
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
    Ejercicio 5:
    Diagrama de Arquitectura de Solución
•   Paso 1: Elabore en draw.io el Diagrama de Arquitectura de Solución del Api
    REST con acceso a base de datos MongoDB balanceada en carga usando el
    puerto 8001. Publique su diagrama en el padlet.

                       1. Objetivo del taller 3
                       2. Ejercicio 1: Crear contenedor de MongoDB
                          en MV Bases de datos
                       3. Ejercicio 2: Crear contenedor de api-fruits
Contenido                 con acceso a MongoDB en MV Desarrollo
Balanceador de Carga   4. Ejercicio 3: Desplegar contenedor api-fruits
                          en 2 MV de producción
                       5. Ejercicio 4: Configurar y probar Balanceador
                          de Carga
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
Cierre:
Balanceador de Carga - Qué aprendimos?
• Balanceo de Carga y Alta disponibilidad con Api REST con acceso
  a base de datos MongoDB (NoSQL)
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
