---
curso: CLOUD
titulo: 1. Arquitectura orientada a eventos - Taller 4 - V1.00
slides: 18
fuente: 1. Arquitectura orientada a eventos - Taller 4 - V1.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Event-driven architecture
Semana 11 - Taller 4: SQS - Simple Queue Service

                       ELABORADO POR: GERALDO COLCHADO
                            1. Objetivo del taller 4
                            2. Ejercicio 1: Evento Nueva Lectura Sensor IoT
                            3. Ejercicio 2: Ejercicio propuesto
Contenido                   4. Cierre
Event-driven architecture
Event-driven architecture
Objetivo del Taller 4
• Diseño e implementación de una Arquitectura de Solución
  basada en eventos con el servicio “SNS - Simple Notification
  Service” y “SQS - Simple Queue Service”.
                            1. Objetivo del taller 4
                            2. Ejercicio 1: Evento Nueva Lectura Sensor IoT
                            3. Ejercicio 2: Ejercicio propuesto
Contenido                   4. Cierre
Event-driven architecture
       Event-driven architecture
       Ejercicio 1 - Evento Nueva Lectura Sensor IoT

Implemente
la siguiente
arquitectura
para procesar
el evento
“Nuevo
Lectura
Sensor IoT”
         Event-driven architecture
         Ejercicio 1 - Evento Nueva Lectura Sensor IoT
                                          import json
                                          import random
                                          from datetime import datetime
Paso 1: Crear tema SNS                    import boto3


“TemaSensorIoT”                           def lambda_handler(event, context):
                                            # TODO implement
                                            tenant_id = "FAB1"
                                            sensor_id = "CO2"
                                            now = datetime.now()
Paso 2: Crear lambda                        fecha_hora = str(now.date()) + "." + str(now.time())
                                            medicion = random.randint(400, 1000) # Desde 400 a 1000 PPM (Nivel de CO2)
                                            unidad_medida = "PPM"
“GenerarEventoSensorIoT” con este
                                            lectura_sensor = {
código fuente (reemplazar amarillo) que        'tenant_id': tenant_id,
                                               'lectura_id': sensor_id + "." + fecha_hora,
simula sensor de CO2 con lectura               'lectura_datos': {
                                                  'medicion': medicion,
                                                  'unidad_medida': unidad_medida
aleatoria entre 400 y 1000 PPM              }
                                               }

                                            # Publicar en SNS
                                            sns_client = boto3.client('sns')
                                            response_sns = sns_client.publish(
                                               TopicArn = 'arn:aws:sns:us-east-1:447891120606:TemaSensorIoT',
                                               Subject = 'Nueva Lectura Sensor',
                                               Message = json.dumps(lectura_sensor),
                                               MessageAttributes = {
                                                  'tenant_id': {'DataType': 'String', 'StringValue': tenant_id },
                                                  'sensor_id': {'DataType': 'String', 'StringValue': sensor_id },
                                                  'medicion': {'DataType': 'Number', 'StringValue': str(medicion) }
                                               }
                                            )
                                            # TODO implement
                                            return {
                                               'statusCode': 200,
                                               'body': response_sns
                                            }
Event-driven architecture
Ejercicio 1 - Evento Nueva Lectura Sensor IoT
Paso 3: Crear una suscripción de correo   {
electrónico válido al tema SNS                "tenant_id": [
“TemaSensorIoT” y colocar la siguiente          "FAB1"
                                              ],
política de filtro
                                              "sensor_id": [
                                                "CO2"
                                              ],
                                              "medicion": [
                                                {
                                                  "numeric": [
                                                    ">",
                                                    800
                                                  ]
                                                }
                                              ]
                                          }
        Event-driven architecture
        Ejercicio 1 - Evento Nueva Lectura Sensor IoT
Paso 4: Crear regla en EventBridge “SimuladorSensorIoT” que llame al lambda “GenerarEventoSensorIoT” cada 1 minuto
Event-driven architecture
Ejercicio 1 - Evento Nueva Lectura Sensor IoT
         Event-driven architecture
         Ejercicio 1 - Evento Nueva Lectura Sensor IoT
Paso 5: Esperar unos 6 minutos y verificar si le ha llegado algún correo notificando este filtro
        Event-driven architecture
        Ejercicio 1 - Evento Nueva Lectura Sensor IoT
Paso 6: Crear tabla dynamoDB “t_sensor_iot_FAB1”
         Event-driven architecture
         Ejercicio 1 - Evento Nueva Lectura Sensor IoT
Paso 7: Crear lambda “InsertarEventoSensorIoT” con este           import json
                                                                  import boto3
código fuente
                                                                  def lambda_handler(event, context):
Paso 8: Crear cola SQS “ColaSensorIoTFAB1” que desencadene          # Entrada (json)
el lambda “InsertarEventoSensorIoT” y con política de acceso        body = json.loads(event['Records'][0]['body'])
                                                                    lectura_sensor = json.loads(body['Message'])
para tema SNS “TemaSensorIoT”                                       # Proceso
                                                                    dynamodb = boto3.resource('dynamodb')
Paso 9: Suscribir la cola SQS “ColaSensorIoTFAB1” al tema SNS       table = dynamodb.Table('t_sensor_iot_FAB1’)
“TemaSensorIoT” con política de filtro                              response = table.put_item(Item=lectura_sensor)
                                               {
                                                                    # Salida (json)
                                                 "tenant_id": [     return {
                                                   "FAB1"             'statusCode': 200,
                                                 ]                    'response': response
                                                                    }
                                               }
         Event-driven architecture
         Ejercicio 1 - Evento Nueva Lectura Sensor IoT
Paso 10: Valide que se registren lecturas del sensor de CO2 en la tabla dynamoDB “t_sensor_iot_FAB1”
                            1. Objetivo del taller 4
                            2. Ejercicio 1: Evento Nueva Lectura Sensor IoT
                            3. Ejercicio 2: Ejercicio propuesto
Contenido                   4. Cierre
Event-driven architecture
              Event-driven architecture
              Ejercicio 2 - Propuesto
•   En lambda “GenerarEventoSensorIoT”
    agregue para tenant_id = “FAB1” un
    nuevo sensor_id = “TEMP” que genere
    aleatoriamente lectura entre 10 y 60 °C
    (grados Celsius) y utilice como
    unidad_medida = “CELSIUS”

•   Agregue una suscripción de correo
    electrónico con el filtro indicado en
    amarillo

•   Verifique que se inserten las lecturas del
    nuevo sensor en tabla dynamoDB y que
    llegue el correo cuando se cumpla el
    filtro

•   Muestre evidencia de correo y registros
    en tabla en padlet indicado por docente
                            1. Objetivo del taller 4
                            2. Ejercicio 1: Evento Nueva Lectura Sensor IoT
                            3. Ejercicio 2: Ejercicio propuesto
Contenido                   4. Cierre
Event-driven architecture
Cierre:
Event-driven architecture - Qué aprendimos?
• Diseño e implementación de una Arquitectura de Solución
  basada en eventos con el servicio “SNS - Simple Notification
  Service” y “SQS - Simple Queue Service”.
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
