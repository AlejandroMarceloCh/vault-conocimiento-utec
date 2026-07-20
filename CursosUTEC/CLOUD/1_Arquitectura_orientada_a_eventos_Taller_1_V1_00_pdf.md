---
curso: CLOUD
titulo: 1. Arquitectura orientada a eventos - Taller 1 - V1.00
slides: 23
fuente: 1. Arquitectura orientada a eventos - Taller 1 - V1.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Event-driven architecture
Semana 10 - Taller 1: SNS - Simple Notification Service

                        ELABORADO POR: GERALDO COLCHADO
                            1. Objetivo del taller 1
                            2. SNS - Simple Notification Service
                            3. Ejercicio 1: Evento Nuevo Alumno en UTEC
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cierre
Event-driven architecture
Objetivo del Taller 1
• Diseño e implementación de una Arquitectura de Solución
  basada en eventos con el servicio “SNS - Simple Notification
  Service”
                            1. Objetivo del taller 1
                            2. SNS - Simple Notification Service
                            3. Ejercicio 1: Evento Nuevo Alumno en UTEC
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cierre
          Event-driven architecture
          SNS - Simple Notification Service




Fuente: https://aws.amazon.com/es/sns
          Event-driven architecture
          SNS - Simple Notification Service




Fuente: https://aws.amazon.com/es/sns
          Event-driven architecture
          SNS - Simple Notification Service




Fuente: https://aws.amazon.com/es/sns
          Event-driven architecture
          SNS - Simple Notification Service




Fuente: https://aws.amazon.com/es/sns
          Event-driven architecture
          SNS - Simple Notification Service




Fuente: https://aws.amazon.com/es/sns
          Event-driven architecture
          SNS - Simple Notification Service




Fuente: https://aws.amazon.com/es/sns
                            1. Objetivo del taller 1
                            2. SNS - Simple Notification Service
                            3. Ejercicio 1: Evento Nuevo Alumno en UTEC
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cierre
      Event-driven architecture
      Ejercicio 1 - Evento Nuevo Alumno en UTEC


Implemente la
siguiente arquitectura
para procesar el
evento “Nuevo
Alumno en UTEC”
        Event-driven architecture
        Ejercicio 1 - Evento Nuevo Alumno en UTEC
Paso 1: Crear un tema “NuevoAlumno” en SNS   Paso 2: Modificar lambda “CrearAlumno” para que
                                             escriba en tema “NuevoAlumno”
                                             import json
                                             import boto3

                                             def lambda_handler(event, context):
                                             …
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
        Event-driven architecture
        Ejercicio 1 - Evento Nuevo Alumno en UTEC
Paso 3: Crear una suscripción al tema “NuevoAlumno” con un correo electrónico (de preferencia de
@gmail) y agregar un filtro para tenant_id = ‘UTEC’. Ingrese a su correo y confirme el enlace.
        Event-driven architecture
        Ejercicio 1 - Evento Nuevo Alumno en UTEC
                                             import json
Paso 4: Crear en DynamoDB una tabla          import boto3

“t_alumnos_canvas” con campos tenant_id      def lambda_handler(event, context):
(clave de partición), alumno_id (clave de      # Entrada (json)
                                               print(event) # Revisar en CloudWatch
ordenación), ambos campos de tipo string o     alumno_json = json.loads(event['Records'][0]['Sns']['Message'])
cadena.                                        # Proceso
                                               dynamodb = boto3.resource('dynamodb')
                                               table = dynamodb.Table('t_alumnos_canvas')
Paso 5: Crear un lambda                        alumno = {
“CrearAlumno_Canvas” que reciba un json           'tenant_id': alumno_json['tenant_id'],
                                                  'alumno_id': alumno_json['alumno_id'],
con los datos del nuevo alumno y los grabe        'alumno_nombre': alumno_json['alumno_datos']['nombre']
en la tabla “t_alumnos_canvas”                 }
                                               print(alumno) # Revisar en CloudWatch
                                               response = table.put_item(Item=alumno)
                                               # Salida (json)
                                               return {
                                                  'statusCode': 200,
                                                  'response': response
                                               }
        Event-driven architecture
        Ejercicio 1 - Evento Nuevo Alumno en UTEC
Paso 6: Crear una suscripción al tema SNS “NuevoAlumno” con el lambda “CrearAlumno_Canvas” y agregue el
filtro tenant_id = ‘UTEC’
              Event-driven architecture
              Ejercicio 1 - Evento Nuevo Alumno en UTEC
Paso 7: Probar el lambda “CrearAlumno” y verificar que se envíe un correo electrónico y que se grabe un
registro en la tabla t_alumnos_canvas
{
  "tenant_id": "UTEC",
  "alumno_id": "202199991",
  "alumno_datos": {
    "nombre": “Juan Colchado",
    "sexo": "M",
    "fecha_nac": "2000-09-01",
    "celular": "999736332",
    "domicilio": {
      "direcc": "Av. Javier Prado
158",
      "distrito": "San Isidro",
      "provincia": "Lima",
      "departamento": "Lima",
      "pais": "Perú"
    }
  }
}
              Event-driven architecture
              Ejercicio 1 - Evento Nuevo Alumno en UTEC
Paso 8: Probar el lambda “CrearAlumno” y verificar que no se envíe un correo electrónico y que no se grabe un
registro en la tabla t_alumnos_canvas por ser de tenant_id = ‘UNIV2’
{
  "tenant_id": “UNIV2",
  "alumno_id": "2021G64747",
  "alumno_datos": {
    "nombre": “Juan Carrasco",
    "sexo": "M",
    "fecha_nac": "2000-09-01",
    "celular": "999736332",
    "domicilio": {
      "direcc": "Av. Javier Prado
158",
      "distrito": "San Isidro",
      "provincia": "Lima",
      "departamento": "Lima",
      "pais": "Perú"
    }
  }
}
                            1. Objetivo del taller 1
                            2. SNS - Simple Notification Service
                            3. Ejercicio 1: Evento Nuevo Alumno en UTEC
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cierre
      Event-driven architecture
      Propuesto - Evento Nuevo Alumno en UTEC


Adicione un subscriber
para notificar al
sistema de seguridad
de UTEC.

Suba su evidencia al
padlet indicado por el
docente.

                            1. Objetivo del taller 1
                            2. SNS - Simple Notification Service
                            3. Ejercicio 1: Evento Nuevo Alumno en UTEC
Contenido                   4. Ejercicio 2: Ejercicio propuesto
Event-driven architecture   5. Cierre
Cierre:
Event-driven architecture - Qué aprendimos?
• Diseño e implementación de una Arquitectura de Solución
  basada en eventos con el servicio “SNS - Simple Notification
  Service”
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
