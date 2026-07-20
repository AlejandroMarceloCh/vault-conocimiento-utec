---
curso: CLOUD
titulo: 1. Otros tópicos - Taller 5 - V1.10
slides: 21
fuente: 1. Otros tópicos - Taller 5 - V1.10.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Otros tópicos
Semana 15 - Taller 5: UUID. Environment y Resources
en framework serverless

                         ELABORADO POR: GERALDO COLCHADO
                         1. Objetivo del taller 5
                         2. Ejercicio 1: UUID
                         3. Ejercicio 2: Environment variables
Contenido                4. Ejercicio 3: Resources (DynamoDB) por stage
UUID. Environment y      5. Ejercicio 4: Eliminar lo desplegado
Resources en framework
serverless               6. Cierre
UUID. Environment y Resources
Objetivo del Taller 5
•   Aprender a utilizar UUID
•   Aprender a utilizar variables de entorno
•   Aprender a crear recursos (DynamoDB) por stage
•   Aprender a eliminar lo desplegado
                         1. Objetivo del taller 5
                         2. Ejercicio 1: UUID
                         3. Ejercicio 2: Environment variables
Contenido                4. Ejercicio 3: Resources (DynamoDB) por stage
UUID. Environment y      5. Ejercicio 4: Eliminar lo desplegado
Resources en framework
serverless               6. Cierre
             UUID. Environment y Resources
             Ejercicio 1: UUID
                                        “What
                                        What
                                        A Version
                                              isisaa1
                                                    version
                                                    4Version4
                                                      UUID  is1a
                                                               UUID?
                                                                UUID?
                                                                 universally unique identifier that is generated using arandom
                                                                                                                          timestamp
                                                                                                                                numbers.”
                                                                                                                                    and the MAC address of the computer on which it was generated.




                                                                       “What is a Version 1 UUID?
                                                                       A Version 1 UUID is a universally unique
                                                                       identifier that is generated using a
                                                                       timestamp and the MAC address of the
                                                                       computer on which it was generated.

                                                                       What is a version 4 UUID?
                                                                       A Version 4 UUID is a universally unique
                                                                       identifier that is generated using random
                                                                       numbers.”


Fuentes: https://youtu.be/MUK5qZxlWFg
https://www.uuidgenerator.net/
             UUID. Environment y Resources
             Ejercicio 1: UUID
             • Paso 1: Ingrese a la máquina virtual “MV para serverless”
             • Paso 2: Cree un directorio /home/ubuntu/python
             • Paso 3: Cree y ejecute el archivo generar-uuid.py
             import uuid
             uuidv1 = str(uuid.uuid1())
             uuidv4 = str(uuid.uuid4())
             print("UUID en V1: ", uuidv1)
             print("UUID en V4: ", uuidv4)


Fuentes: https://youtu.be/MUK5qZxlWFg
https://www.uuidgenerator.net/
             UUID. Environment y Resources
             Ejercicio 1: UUID
             • Paso 4: Ejecutar el programa




Fuentes: https://youtu.be/MUK5qZxlWFg
https://www.uuidgenerator.net/
                         1. Objetivo del taller 5
                         2. Ejercicio 1: UUID
                         3. Ejercicio 2: Environment variables
Contenido                4. Ejercicio 3: Resources (DynamoDB) por stage
UUID. Environment y      5. Ejercicio 4: Eliminar lo desplegado
Resources en framework
serverless               6. Cierre
              UUID. Environment y Resources
              Ejercicio 2: Environment variables
             • Paso 1: Visualice las variables de entorno de Linux
             $ printenv

             • Paso 2: Cree las siguientes variables de entorno
             $ NOMBRE_ALUMNO="Geraldo Colchado Ruiz"
             $ NOMBRE_EMPRESA="UTEC"
             $ export NOMBRE_ALUMNO
             $ export NOMBRE_EMPRESA


Fuente: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux-es
              UUID. Environment y Resources
              Ejercicio 2: Environment variables
             • Paso 3: Verifique que se hayan creado
             $ printenv
             …
             NOMBRE_ALUMNO=Geraldo Colchado Ruiz
             …
             NOMBRE_EMPRESA=UTEC
             …



Fuente: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux-es
              UUID. Environment y Resources
              Ejercicio 2: Environment variables
             • Paso 4: Cree /home/ubuntu/python/variables-entorno.py
             import os
             alumno = os.environ["NOMBRE_ALUMNO"]
             empresa = os.environ["NOMBRE_EMPRESA"]
             print(alumno)
             print(empresa)

             • Paso 5: Ejecute el programa




Fuente: https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux-es
                         1. Objetivo del taller 5
                         2. Ejercicio 1: UUID
                         3. Ejercicio 2: Environment variables
Contenido                4. Ejercicio 3: Resources (DynamoDB) por stage
UUID. Environment y      5. Ejercicio 4: Eliminar lo desplegado
Resources en framework
serverless               6. Cierre
      UUID. Environment y Resources
      Ejercicio 3: Resources (DynamoDB) por stage
Elabore un lambda que reciba como entrada un tenant_id y un texto y lo almacene
en una tabla DynamoDB. Considere lo siguiente:

•   Publicar como API Rest con Api Gateway
•   Debe usar una tabla con nombre diferente según el stage (Una para desarrollo,
    otra para test y otra para producción). Use variables de entorno.
•   Debe usar el campo tenant_id como clave de partición y el campo uuid como
    clave de ordenamiento (Use UUID V1)
•   Debe automatizar el despliegue con framework serverless (La tabla debe ser
    creada automáticamente desde aquí)
      UUID. Environment y Resources
      Ejercicio 3: Resources (DynamoDB) por stage
•   Paso 1: Actualice el archivo de credenciales /home/ubuntu/.aws/credentials

•   Paso 2: Cree el directorio /home/ubuntu/api-comentario y suba los archivos
    indicados por el docente. Analice el contenido de los archivos

• Paso 3: Realice el despliegue automático en stage de desarrollo
$ serverless login
$ serverless deploy
      UUID. Environment y Resources
      Ejercicio 3: Resources (DynamoDB) por stage
•   Paso 4: Pruebe en postman y verifique la variable de entorno de lambda y tabla
      UUID. Environment y Resources
      Ejercicio 3: Resources (DynamoDB) por stage
• Paso 5: Realice el despliegue automático en stage de test y producción
$ serverless deploy --stage test
$ serverless deploy --stage prod

•   Paso 6: Pruebe en postman y verifique las variables de entorno de lambda y
    tablas de test y producción
                         1. Objetivo del taller 5
                         2. Ejercicio 1: UUID
                         3. Ejercicio 2: Environment variables
Contenido                4. Ejercicio 3: Resources (DynamoDB) por stage
UUID. Environment y      5. Ejercicio 4: Eliminar lo desplegado
Resources en framework
serverless               6. Cierre
      UUID. Environment y Resources
      Ejercicio 4: Eliminar lo desplegado
•   Paso 1: Desde el directorio /home/ubuntu/api-comentario ejecute estos
    comandos para eliminar todo lo desplegado

$ serverless remove
$ serverless remove --stage test
$ serverless remove --stage prod

•   Paso 2: Verifique que se hayan eliminado todos los objetos (Api Gateway,
    Lambdas y DynamoDB) tanto de desarrollo, test y producción.
                         1. Objetivo del taller 5
                         2. Ejercicio 1: UUID
                         3. Ejercicio 2: Environment variables
Contenido                4. Ejercicio 3: Resources (DynamoDB) por stage
UUID. Environment y      5. Ejercicio 4: Eliminar lo desplegado
Resources en framework
serverless               6. Cierre
Cierre:
UUID. Environment y Resources - Qué aprendimos?
•   Utilizar UUID
•   Utilizar variables de entorno
•   Crear recursos (DynamoDB) por stage
•   Eliminar lo desplegado

              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
