---
curso: CLOUD
titulo: 1. Arquitectura orientada a eventos - Taller 3 - V2.00
slides: 28
fuente: 1. Arquitectura orientada a eventos - Taller 3 - V2.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Event-driven architecture
Semana 11 - Taller 3: SQS - Simple Queue Service

                       ELABORADO POR: GERALDO COLCHADO
                           Con apoyo de Asistentes de Cátedra y Laboratorio:
                           • Sofía García (sofia.garcia@utec.edu.pe)
                           • Rubén Aaron Coorahua (ruben.coorahua@utec.edu.pe)
                            1. Objetivo del taller 3
                            2. SQS - Simple Queue Service
                            3. Ejercicio 1: Despacho de pedidos
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cola de Mensajes Fallidos (DLQ)
                            6. Ejercicio 3: DLQ
                            7. Cierre
Event-driven architecture
Objetivo del Taller 3
• Diseño e implementación de una Arquitectura de Solución
  basada en eventos con el servicio “SQS - Simple Queue Service”.
                            1. Objetivo del taller 3
                            2. SQS - Simple Queue Service
                            3. Ejercicio 1: Despacho de pedidos
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cola de Mensajes Fallidos (DLQ)
                            6. Ejercicio 3: DLQ
                            7. Cierre
          Event-driven architecture
          SQS - Simple Queue Service




Fuente: https://aws.amazon.com/es/sqs/
                            1. Objetivo del taller 3
                            2. SQS - Simple Queue Service
                            3. Ejercicio 1: Despacho de pedidos
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cola de Mensajes Fallidos (DLQ)
                            6. Ejercicio 3: DLQ
                            7. Cierre
Event-driven architecture
Ejercicio 1 - Despacho de Pedidos
Event-driven architecture
Ejercicio 1 - Despacho de Pedidos
Paso 1: Crear Cola de Pedidos (sqs-pedidos)
Event-driven architecture
Ejercicio 1 - Despacho de Pedidos
Paso 2: Crear Lambda RegistrarPedido con tiempo de espera de 10 segundos y reemplace el queue_url

Paso 3: Crear Api Gateway pedidos con recurso /pedidos/registrar con un método POST que ejecute el
lambda anterior y habilite CORS
         Event-driven architecture
         Ejercicio 1 - Despacho de Pedidos
Paso 4: Pruebe con
postman registrar un
pedido
Event-driven architecture
Ejercicio 1 - Despacho de Pedidos
Paso 5: Verifique en la cola sqs-pedidos si llegó el mensaje
Event-driven architecture
Ejercicio 1 - Despacho de Pedidos
Paso 6: Registre los otros 4 mensajes por postman
Event-driven architecture
Ejercicio 1 - Despacho de Pedidos
Paso 7: Crear tabla DynamoDB t_pedidos_procesados




Paso 8: Crear lambda ProcesarPedido con tiempo de espera de 10
segundos

Paso 9: En Api Gateway pedidos crear recurso /pedidos/procesar
con un método GET que ejecute el lambda anterior y habilite CORS
Event-driven architecture
Ejercicio 1 - Despacho de Pedidos
Paso 10: Ejecute el api en postman
simulando que es el Despachador 1
Event-driven architecture
Ejercicio 1 - Despacho de Pedidos
Paso 11: Verifique si se grabaron los pedidos en tabla




 Paso 12: Ejecute el api hasta procesar todos los 5 pedidos simulando que es el Despachador 2 y
 Despachador 3 y analice
                            1. Objetivo del taller 3
                            2. SQS - Simple Queue Service
                            3. Ejercicio 1: Despacho de Pedidos
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cola de Mensajes Fallidos (DLQ)
                            6. Ejercicio 3: DLQ
                            7. Cierre
Event-driven architecture
Ejercicio 2 - Propuesto
• Modifique el lambda ProcesarPedido para que reciba como entrada un despachador_id (“DESP-01”,
  “DESP-02”, “DESP-03”) y este se grabe como campo en la tabla DynamoDB t_pedidos_procesados para
  identificar el despachador que procesó los pedidos. Debe modificar el método a POST en Api Gateway
  en pedidos/procesar.

• En la respuesta del lambda ProcesarPedido agregue un campo con la cantidad de pedidos procesados
                            1. Objetivo del taller 3
                            2. SQS - Simple Queue Service
                            3. Ejercicio 1: Despacho de Pedidos
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cola de Mensajes Fallidos (DLQ)
                            6. Ejercicio 3: DLQ
                            7. Cierre
          Event-driven architecture
          Cola de Mensajes Fallidos (DLQ - Dead Letter Queue)


          “Una cola de mensajes fallidos
          (DLQ) es un tipo especial de cola de
          mensajes que almacena
          temporalmente los mensajes que
          un sistema de software no puede
          procesar debido a errores.”




Fuente: https://aws.amazon.com/es/what-is/dead-letter-queue/, https://siecola.com.br/blogs/aws_sqs_dlq.html
                            1. Objetivo del taller 3
                            2. SQS - Simple Queue Service
                            3. Ejercicio 1: Despacho de Pedidos
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cola de Mensajes Fallidos (DLQ)
                            6. Ejercicio 3: DLQ
                            7. Cierre

      Event-driven architecture
      Ejercicio 3 - DLQ


Agregar una cola de
mensajes fallidos
(DLQ) en caso falle el
registro de nuevo
alumno en canvas
        Event-driven architecture
        Ejercicio 3 - DLQ
• Paso 1: Cree una cola de mensajes fallidos
  sqs-registrar-canvas-dlq

• Paso 2: Cree una cola sqs-registrar-canvas y
  configure la cola de mensajes fallidos para
  que sea enviado el mensaje luego de 2
  reintentos fallidos de procesarlo.
       Event-driven architecture
       Ejercicio 3 - DLQ
• Paso 3: Cree un lambda RegistrarCanvas que
  genene una excepción (simulando que falla)
       Event-driven architecture
       Ejercicio 3 - DLQ
• Paso 4: En la cola sqs-registrar-canvas configure un desencadenador de lambda a RegistrarCanvas para que
  procese el mensaje
        Event-driven architecture
        Ejercicio 3 - DLQ
• Paso 5: Envíe un mensaje en la cola sqs-registrar-canvas y valide los 2 reintentos con error en CloudWatch (cada 30
  segundos) y que se genere un mensaje en cola sqs-registrar-canvas-dlq
                            1. Objetivo del taller 3
                            2. SQS - Simple Queue Service
                            3. Ejercicio 1: Despacho de Pedidos
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cola de Mensajes Fallidos (DLQ)
                            6. Ejercicio 3: DLQ
                            7. Cierre
Cierre:
Event-driven architecture - Qué aprendimos?
• Diseño e implementación de una Arquitectura de Solución
  basada en eventos con el servicio “SQS - Simple Queue Service”.
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
