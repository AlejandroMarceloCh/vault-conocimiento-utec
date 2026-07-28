---
curso: CLOUD
titulo: 1. Arquitectura orientada a eventos - Taller 1 - V1.00
slides: 23
fuente: 1. Arquitectura orientada a eventos - Taller 1 - V1.00.pdf
---

## Slide 1

Portada (decorativa: logo UTEC). Texto: "CS2032 - Cloud Computing (Ciclo 2024-1) / Event-driven architecture / Semana 10 - Taller 1: SNS - Simple Notification Service". Elaborado por: Geraldo Colchado.

## Slide 2

Slide de tabla de contenido (barra lateral naranja "Contenido / Event-driven architecture"). Lista numerada, ítem 1 en negrita/subrayado (resaltando la sección actual):
1. **Objetivo del taller 1**
2. SNS - Simple Notification Service
3. Ejercicio 1: Evento Nuevo Alumno en UTEC
4. Ejercicio 2: Ejercicio propuesto
5. Cierre

## Slide 3

Título "Event-driven architecture / Objetivo del Taller 1". Texto: "Diseño e implementación de una Arquitectura de Solución basada en eventos con el servicio 'SNS - Simple Notification Service'".

## Slide 4

Slide de contenido (repetida), ahora resalta el ítem 2 en negrita/subrayado:
1. Objetivo del taller 1
2. **SNS - Simple Notification Service**
3. Ejercicio 1: Evento Nuevo Alumno en UTEC
4. Ejercicio 2: Ejercicio propuesto
5. Cierre

## Slide 5

Título "Event-driven architecture / SNS - Simple Notification Service". Captura de pantalla de la página de AWS (banner oscuro con red de nodos decorativa): "Amazon Simple Notification Service — Notificaciones push móviles, correo electrónico, SMS y mensajería de publicación/suscripción completamente administrada", con botón naranja "Introducción a Amazon SNS". Debajo, texto explicativo: Amazon SNS es un servicio de mensajería completamente administrado para la comunicación aplicación a aplicación (A2A) y aplicación a persona (A2P) (resaltado en amarillo). Explica que A2A brinda temas pub/sub de alto rendimiento, muchos a muchos, entre sistemas distribuidos, microservicios y apps serverless, distribuyendo a SQS, Lambda, HTTPS y Kinesis Data Firehose; A2P permite enviar mensajes a escala vía SMS, push móvil y correo. Fuente: https://aws.amazon.com/es/sns.

## Slide 6

Título igual. Captura de pantalla de consola/doc AWS con pestañas "Publicación/suscripción" (activa, resaltada en amarillo) | SMS | Notificaciones push móviles. Diagrama de flujo dentro del recuadro:
`Publisher (Publish messages from distributed systems, microservices, and other AWS services)` → `Amazon SNS (Fully-managed pub/sub messaging and event-driven computing service)` → `SNS Topic (Decouple message publishers from subscribers with topics)` → `Message Filtering & Fanout (Filter messages according to subscription filter policies, and deliver them to subscribers)` → lista de destinos suscriptores: `AWS Lambda`, `Amazon SQS`, `Amazon Kinesis Data Firehose`, `HTTP/S`, `Email` → `Subscribers (Receive messages in subscribing serverless functions, queues, microservices, delivery streams and more)`. Además, una rama superior desde SNS Topic muestra `Dead-letter Queue (If an endpoint is unavailable, messages can be held in a dead-letter queue for analysis or reprocessing)`. Fuente: https://aws.amazon.com/es/sns.

## Slide 7

Título igual. Captura con pestaña "SMS" activa (resaltada en amarillo, recuadro azul). Diagrama: `Amazon SNS` → `Publish text messages (You can send SMS messages to millions of users via a topic or directly to their devices)` → `SNS Topic` → 4 iconos de persona con celular (destinatarios). Fuente: https://aws.amazon.com/es/sns.

## Slide 8

Título igual. Captura con pestaña "Notificaciones push móviles" activa (resaltada, recuadro azul). Diagrama de 3 pasos: `Amazon SNS` → `1) Create a platform application (A platform application represents a push notification service from a provider like Apple, Google, Amazon or Microsoft)` → `2) Add endpoints (A platform endpoint can be a mobile device, such as an iPhone or Android phone)` → `3) Publish messages (You can send push notifications to millions of users via a topic or directly to their devices)` → `SNS Topic` → 4 iconos de persona con celular. Fuente: https://aws.amazon.com/es/sns.

## Slide 9

Título igual. Sección "Aplicación a aplicación (A2A)" (resaltada en amarillo). Texto: Amazon SNS permite desacoplar publicadores de suscriptores, útil para mensajería entre microservicios, sistemas distribuidos y apps serverless (con enlace "Más información"). Diagrama en español: `Publicador (Los publicadores envían mensajes desde sistemas distribuidos, microservicios y otros servicios de AWS)` → `Amazon SNS` → `Tema de SNS (Los temas desacoplan los publicadores de los mensajes de los suscriptores)` → destinos: `AWS Lambda`, `Amazon SQS`, `HTTP/S` → `Suscriptores (Los suscriptores pueden ser funciones de Lambda, colas de SQS y puntos de enlace HTTP(S))`. Fuente: https://aws.amazon.com/es/sns.

## Slide 10

Título igual. Sección "Aplicación a persona (A2P)" (resaltada en amarillo). Texto: Amazon SNS permite enviar notificaciones de inserción a apps móviles, SMS a teléfonos y correos a direcciones de email; puede distribuir por tema o publicar directamente en endpoints móviles. Diagrama en español: `Publicador` → `Amazon SNS` → `Tema de SNS` → destinos: `Notificaciones de inserción`, `Mensajes de texto`, `Correo electrónico` → `Suscriptores (aplicaciones móviles, números de teléfono móvil y direcciones de correo electrónico)`. Fuente: https://aws.amazon.com/es/sns.

## Slide 11

Slide de contenido (repetida), resalta ítem 3 en negrita/subrayado:
1. Objetivo del taller 1
2. SNS - Simple Notification Service
3. **Ejercicio 1: Evento Nuevo Alumno en UTEC**
4. Ejercicio 2: Ejercicio propuesto
5. Cierre

## Slide 12

Título "Event-driven architecture / Ejercicio 1 - Evento Nuevo Alumno en UTEC". Texto: "Implemente la siguiente arquitectura para procesar el evento 'Nuevo Alumno en UTEC'". Diagrama principal del taller, titulado "Diagrama de Arquitectura de solución basada en eventos - Nuevo Alumno en UTEC":
- Icono Lambda `CrearAlumno` → flecha con etiqueta `{JSON} datos nuevo alumno` → icono `Amazon SNS`.
- Desde Amazon SNS salen dos ramas, cada una con un filtro (embudo azul) `tenant_id = "UTEC"`:
  - Rama superior: filtro → icono `@` (sobre de correo) etiquetado `e-mail a empresa de Merchandising`, junto a una foto decorativa de productos de merchandising (polos, gorras, tazas, sombrillas con logo "LOREM").
  - Rama inferior: filtro → icono Lambda `CrearAlumno_Canvas` → icono de base de datos `t_alumnos_canvas`.

## Slide 13

Título "Event-driven architecture / Ejercicio 1 - Evento Nuevo Alumno en UTEC". Dos columnas:
- **Paso 1:** Crear un tema "NuevoAlumno" en SNS. Captura de consola AWS: botón "Crear un tema", formulario "Crear un tema" con sección "Detalles": Tipo = FIFO vs **Estándar** (seleccionado, resaltado en amarillo, con sus características: clasificación de mejor esfuerzo, entrega al menos una vez, mayor rendimiento, protocolos SQS/Lambda/HTTP/SMS/correo/apps); Nombre = "NuevoAlumno" (resaltado); botón "Crear un tema".
- **Paso 2:** Modificar lambda "CrearAlumno" para que escriba en tema "NuevoAlumno". Código Python (resaltado en amarillo/celeste las líneas clave):
```python
import json
import boto3

def lambda_handler(event, context):
...
  # Publicar en SNS
  sns_client = boto3.client('sns')
  response_sns = sns_client.publish(
     TopicArn = 'arn:aws:sns:us-east-1:447891120606:NuevoAlumno',
     Subject = 'Nuevo Alumno',
     Message = json.dumps(alumno),
     MessageAttributes = {
        'tenant_id': {'DataType': 'String', 'StringValue': tenant_id }
     }
  )
  print(response_sns)
  # Salida (json)
  return {
     'statusCode': 200,
     'response': response
  }
```
Al costado, mini-diagrama: `Evento Nuevo Alumno` → icono Lambda `CrearAlumno` → `{JSON} datos nuevo alumno` → icono `Amazon SNS`.

## Slide 14

**Paso 3:** Crear una suscripción al tema "NuevoAlumno" con un correo electrónico (de preferencia @gmail) y agregar un filtro para tenant_id = 'UTEC'. Ingresar al correo y confirmar el enlace. Tres capturas de pantalla:
- Formulario "Crear una suscripción": ARN del tema = `arn:aws:sns:us-east-1:447891120606:NuevoAlumno` (resaltado); Protocolo = "Correo electrónico" (resaltado); Punto de enlace = dirección de correo (parcialmente tapada/censurada en verde) `...@gmail.com`; nota "Una vez creada la suscripción, debe confirmarla".
- Sección "Política de filtro de suscripciones - opcional": opción "Habilitado" seleccionada (resaltada); "Editor de JSON" con:
```json
{
  "tenant_id": [
    "UTEC"
  ]
}
```
(marcado con llave amarilla a mano). Botón "Crear una suscripción".
- Mini-diagrama: `Amazon SNS` → filtro `tenant_id = "UTEC"` → icono `@` → "e-mail a empresa de Merchandising".

## Slide 15

**Paso 4:** Crear en DynamoDB una tabla "t_alumnos_canvas" con campos tenant_id (clave de partición), alumno_id (clave de ordenación), ambos tipo string. **Paso 5:** Crear un lambda "CrearAlumno_Canvas" que reciba un json con los datos del nuevo alumno y los grabe en la tabla "t_alumnos_canvas". Mini-diagrama: icono Lambda `CrearAlumno_Canvas` → icono BD `t_alumnos_canvas`. Código Python completo:
```python
import json
import boto3

def lambda_handler(event, context):
   # Entrada (json)
   print(event) # Revisar en CloudWatch
   alumno_json = json.loads(event['Records'][0]['Sns']['Message'])
   # Proceso
   dynamodb = boto3.resource('dynamodb')
   table = dynamodb.Table('t_alumnos_canvas')
   alumno = {
      'tenant_id': alumno_json['tenant_id'],
      'alumno_id': alumno_json['alumno_id'],
      'alumno_nombre': alumno_json['alumno_datos']['nombre']
   }
   print(alumno) # Revisar en CloudWatch
   response = table.put_item(Item=alumno)
   # Salida (json)
   return {
      'statusCode': 200,
      'response': response
   }
```

## Slide 16

**Paso 6:** Crear una suscripción al tema SNS "NuevoAlumno" con el lambda "CrearAlumno_Canvas" y agregar el filtro tenant_id = 'UTEC'. Capturas:
- Formulario "Crear una suscripción": ARN del tema = `arn:aws:sns:us-east-1:447891120606:NuevoAlumno` (resaltado); Protocolo = "AWS Lambda" (resaltado); Punto de enlace = `arn:aws:lambda:us-east-1:447891120606:function:CrearAlumno_Canvas` (resaltado).
- Política de filtro: "Habilitado" (resaltado); Editor de JSON igual que antes: `{ "tenant_id": ["UTEC"] }` (marcado con llave amarilla).
- Mini-diagrama: `Amazon SNS` → filtro `tenant_id = "UTEC"` → icono Lambda `CrearAlumno_Canvas`.

## Slide 17

**Paso 7:** Probar el lambda "CrearAlumno" y verificar que se envíe un correo electrónico y que se grabe un registro en la tabla t_alumnos_canvas. JSON de entrada de prueba (resaltado en partes):
```json
{
  "tenant_id": "UTEC",
  "alumno_id": "202199991",
  "alumno_datos": {
    "nombre": "Juan Colchado",
    "sexo": "M",
    "fecha_nac": "2000-09-01",
    "celular": "999736332",
    "domicilio": {
      "direcc": "Av. Javier Prado 158",
      "distrito": "San Isidro",
      "provincia": "Lima",
      "departamento": "Lima",
      "pais": "Perú"
    }
  }
}
```
Debajo, captura de tabla DynamoDB "t_alumnos_canvas" con resultado esperado — columnas `tenant_id | alumno_id | alumno_nombre`, fila: `UTEC | 202199991 | Juan Colchado`. A la derecha, diagrama completo de arquitectura repetido (igual que slide 12).

## Slide 18

**Paso 8:** Probar el lambda "CrearAlumno" y verificar que **no** se envíe un correo electrónico y que **no** se grabe un registro en la tabla t_alumnos_canvas por ser de tenant_id = 'UNIV2' (resaltados en amarillo "no" y "tenant_id = 'UNIV2'"). JSON de entrada de prueba:
```json
{
  "tenant_id": "UNIV2",
  "alumno_id": "2021G64747",
  "alumno_datos": {
    "nombre": "Juan Carrasco",
    "sexo": "M",
    "fecha_nac": "2000-09-01",
    "celular": "999736332",
    "domicilio": {
      "direcc": "Av. Javier Prado 158",
      "distrito": "San Isidro",
      "provincia": "Lima",
      "departamento": "Lima",
      "pais": "Perú"
    }
  }
}
```
Debajo, misma tabla DynamoDB "t_alumnos_canvas" mostrando que sigue solo con el registro anterior (`UTEC | 202199991 | Juan Colchado`), es decir sin el nuevo registro de UNIV2. A la derecha, mismo diagrama de arquitectura completo.

## Slide 19

Slide de contenido (repetida), resalta ítem 4 en negrita/subrayado:
1. Objetivo del taller 1
2. SNS - Simple Notification Service
3. Ejercicio 1: Evento Nuevo Alumno en UTEC
4. **Ejercicio 2: Ejercicio propuesto**
5. Cierre

## Slide 20

Título "Event-driven architecture / Propuesto - Evento Nuevo Alumno en UTEC". Texto: "Adicione un subscriber para notificar al sistema de seguridad de UTEC. Suba su evidencia al padlet indicado por el docente." Diagrama de arquitectura extendido (mismo diagrama base de la slide 12, ahora con una tercera rama añadida):
- `Evento Nuevo Alumno` → Lambda `CrearAlumno` → `{JSON} datos nuevo alumno` → `Amazon SNS`.
- Rama 1 (filtro `tenant_id = "UTEC"`) → `@` correo → "e-mail a empresa de Merchandising".
- Rama 2 (filtro `tenant_id = "UTEC"`) → Lambda `CrearAlumno_Canvas` → BD `t_alumnos_canvas`.
- Rama 3 (nueva, filtro `tenant_id = "UTEC"`) → Lambda `CrearAlumno_Seguridad` → BD `t_alumnos_seguridad`.

## Slide 21

Slide de contenido (repetida), resalta ítem 5 en negrita/subrayado:
1. Objetivo del taller 1
2. SNS - Simple Notification Service
3. Ejercicio 1: Evento Nuevo Alumno en UTEC
4. Ejercicio 2: Ejercicio propuesto
5. **Cierre**

## Slide 22

Título "Cierre: / Event-driven architecture - Qué aprendimos?". Texto: "Diseño e implementación de una Arquitectura de Solución basada en eventos con el servicio 'SNS - Simple Notification Service'". Repite el objetivo del taller como resumen de cierre.

## Slide 23

Slide final (decorativa, portada de cierre): "Gracias". "Elaborado por docente: Geraldo Colchado".
