---
curso: CLOUD
titulo: 1. Otros tópicos - Taller 4 - V1.10
slides: 21
fuente: 1. Otros tópicos - Taller 4 - V1.10.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Otros tópicos
Semana 14 - Taller 4: Optimización de Lambdas

                      ELABORADO POR: GERALDO COLCHADO
                          1. Objetivo del taller 4
                          2. Ejercicio 1: Configuración de memoria RAM
                          3. Ejercicio 2: Stage o Etapa del Lambda/Api G.
Contenido                 4. Ejercicio 3: Ejecutar api rest desde Linux
Optimización de Lambdas   5. Ejercicio 4: Ejercicio propuesto
                          6. Cierre
Optimización de Lambdas
Objetivo del Taller 4
• Aprender a optimizar tiempos de ejecución de Lambdas
• Aprender a desplegar lambdas/Api G. en diferentes etapas
• Aprender a ejecutar un Api Rest desde Linux
                          1. Objetivo del taller 4
                          2. Ejercicio 1: Configuración de memoria RAM
                          3. Ejercicio 2: Stage o Etapa del Lambda/Api G.
Contenido                 4. Ejercicio 3: Ejecutar api rest desde Linux
Optimización de Lambdas   5. Ejercicio 4: Ejercicio propuesto
                          6. Cierre
          Optimización de Lambdas
          Ejercicio 1: Configuración de memoria RAM
Paso 1: Implementar un lambda que liste todos los buckets y otro lambda que liste todos los objetos de un bucket. Ambos
lambdas los debe publicar en un mismo API Rest en Api Gateway.

Adicionalmente debe automatizar el despliegue con serverless framework: $ serverless deploy

Utilice el código fuente en python entregado por el docente. Nota: No olvide actualizar el archivo credentials, el org y el role
    Optimización de Lambdas
    Ejercicio 1: Configuración de memoria RAM
Paso 2: Pruebe en
postman
    Optimización de Lambdas
    Ejercicio 1: Configuración de memoria RAM
Paso 2: Pruebe en
postman
    Optimización de Lambdas
    Ejercicio 1: Configuración de memoria RAM
Paso 3: Analice lambda y api gateway creados
                          1. Objetivo del taller 4
                          2. Ejercicio 1: Configuración de memoria RAM
                          3. Ejercicio 2: Stage o Etapa del Lambda/Api G.
Contenido                 4. Ejercicio 3: Ejecutar api rest desde Linux
Optimización de Lambdas   5. Ejercicio 4: Ejercicio propuesto
                          6. Cierre
    Optimización de Lambdas
    Ejercicio 2: Stage o Etapa del Lambda/Api G.
Paso 1: La implementación del Api Rest “api-s3” en el stage “dev” (desarrollo) ha sido satisfactoria.
Realice el despliegue automático en el entorno de pruebas.

$ serverless deploy --stage test
    Optimización de Lambdas
    Ejercicio 2: Stage o Etapa del Lambda/Api G.
Paso 2: Pruebe en postman
Paso 3: Analice lambda y api gateway creados. Note que son lambdas diferentes y el api gateway
también es diferente al de stage = “dev”
    Optimización de Lambdas
    Ejercicio 2: Stage o Etapa del Lambda/Api G.
Paso 4: La implementación del Api Rest “api-s3” en el stage “test” (pruebas) ha sido satisfactoria y el
equipo de QA ha dado el OK. Realice el despliegue automático en el entorno de producción.

$ serverless deploy --stage prod
    Optimización de Lambdas
    Ejercicio 2: Stage o Etapa del Lambda/Api G.
Paso 5: Pruebe en postman
Paso 6: Analice lambda y api gateway creados. Note que son lambdas diferentes y api gateway
diferentes en los 3 stages.
                          1. Objetivo del taller 4
                          2. Ejercicio 1: Configuración de memoria RAM
                          3. Ejercicio 2: Stage o Etapa del Lambda/Api G.
Contenido                 4. Ejercicio 3: Ejecutar api rest desde Linux
Optimización de Lambdas   5. Ejercicio 4: Ejercicio propuesto
                          6. Cierre
              Optimización de Lambdas
              Ejercicio 3: Ejecutar api rest desde Linux
        Paso 1: Ejecutar el api rest de Listar buckets (GET)

        $ curl https://v6fak03vga.execute-api.us-east-1.amazonaws.com/dev/s3/lista-buckets




Fuentes: https://reqbin.com/req/c-1n4ljxb9/curl-get-request-example
              Optimización de Lambdas
              Ejercicio 3: Ejecutar api rest desde Linux
        Paso 2: Ejecutar el api listar objetos de bucket (POST)

        $ curl -X POST https://v6fak03vga.execute-api.us-east-1.amazonaws.com/dev/s3/bucket/lista-objetos -
        H 'Content-Type: application/json' -d '{"bucket":"gcolchado-sec1"}'




Fuentes: https://reqbin.com/req/c-dwjszac0/curl-post-json-example
                          1. Objetivo del taller 4
                          2. Ejercicio 1: Configuración de memoria RAM
                          3. Ejercicio 2: Stage o Etapa del Lambda/Api G.
Contenido                 4. Ejercicio 3: Ejecutar api rest desde Linux
Optimización de Lambdas   5. Ejercicio 4: Ejercicio propuesto
                          6. Cierre
      Optimización de Lambdas
      Ejercicio 4: Ejercicio propuesto
• Modifique el api-s3 para agregar una función que cree una carpeta o directorio en un
  bucket y otra función para crear un nuevo bucket.

• Realice el despliegue en el stage de test

• Pruebe el api rest desde Linux con curl.

• Muestre la evidencia de la carpeta creada en el bucket de S3.

• Coloque toda la evidencia en un archivo word, excel o power point y súbalo al padlet
  indicado por el profesor.
                          1. Objetivo del taller 4
                          2. Ejercicio 1: Configuración de memoria RAM
                          3. Ejercicio 2: Stage o Etapa del Lambda/Api G.
Contenido                 4. Ejercicio 3: Ejecutar api rest desde Linux
Optimización de Lambdas   5. Ejercicio 4: Ejercicio propuesto
                          6. Cierre
Cierre:
Optimización de Lambdas - Qué aprendimos?
• Optimizar tiempos de ejecución de Lambdas
• Desplegar lambdas/Api G. en diferentes etapas
• Ejecutar un Api Rest desde Linux

              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
