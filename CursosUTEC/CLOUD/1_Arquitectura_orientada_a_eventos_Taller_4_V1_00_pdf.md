---
curso: CLOUD
titulo: 1. Arquitectura orientada a eventos - Taller 4 - V1.00
slides: 18
fuente: 1. Arquitectura orientada a eventos - Taller 4 - V1.00.pdf
---

## Slide 1

Portada del curso. Texto: "CS2032 - Cloud Computing (Ciclo 2024-1)", "Event-driven architecture", "Semana 11 - Taller 4: SQS - Simple Queue Service". Elaborado por: Geraldo Colchado. Logo UTEC en esquina superior derecha (decorativo).

## Slide 2

Slide de índice "Contenido" (franja lateral izquierda naranja con título "Contenido" / "Event-driven architecture"). Lista numerada de contenidos, con el ítem 1 resaltado en negrita/subrayado (indica sección actual):
1. **Objetivo del taller 4** (resaltado)
2. Ejercicio 1: Evento Nueva Lectura Sensor IoT
3. Ejercicio 2: Ejercicio propuesto
4. Cierre

## Slide 3

Título: "Event-driven architecture / Objetivo del Taller 4". Texto:
- Diseño e implementación de una Arquitectura de Solución basada en eventos con el servicio "SNS - Simple Notification Service" y "SQS - Simple Queue Service".

## Slide 4

Slide de índice "Contenido" (misma plantilla lateral naranja que slide 2), ahora con el ítem 2 resaltado en negrita/subrayado:
1. Objetivo del taller 4
2. **Ejercicio 1: Evento Nueva Lectura Sensor IoT** (resaltado)
3. Ejercicio 2: Ejercicio propuesto
4. Cierre

## Slide 5

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT". Texto: "Implemente la siguiente arquitectura para procesar el evento 'Nuevo Lectura Sensor IoT'".

Diagrama de arquitectura AWS (título dentro de la imagen: "Diagrama de Arquitectura de Solución - Simulación de Nuevo Evento Lectura Sensor IoT"), flujo de izquierda a derecha:
- **EventBridge** (regla "SimuladorSensorIoT", disparada cada 1 min) → invoca lambda
- **GenerarEventoSensorIoT** (Lambda) → produce JSON "Medición Sensor IoT"
- → **Amazon SNS "TemaSensorIoT"** (tópico), que se ramifica en dos salidas:
  - Rama superior (correo, filtro): condición `tenant_id = "FAB1" y sensor_id = "CO2" y medición > 800 PPM` → ícono de sobre de correo (notificación por email)
  - Rama inferior (filtro `tenant_id = "FAB1"`) → **Amazon SQS "ColaSensorIoTFAB1"** → **InsertarEventoSensorIoT** (Lambda) → **Amazon DynamoDB "t_sensor_iot_FAB1"**

## Slide 6

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT".

Paso 1: Crear tema SNS "TemaSensorIoT".
Paso 2: Crear lambda "GenerarEventoSensorIoT" con el código fuente (reemplazar lo resaltado en amarillo) que simula sensor de CO2 con lectura aleatoria entre 400 y 1000 PPM.

Icono pequeño de flujo: Lambda "GenerarEventoSensorIoT" → JSON "Medición Sensor IoT" → Amazon SNS "TemaSensorIoT".

Código fuente (Python, Lambda):
```python
import json
import random
from datetime import datetime
import boto3

def lambda_handler(event, context):
  # TODO implement
  tenant_id = "FAB1"
  sensor_id = "CO2"
  now = datetime.now()
  fecha_hora = str(now.date()) + "." + str(now.time())
  medicion = random.randint(400, 1000) # Desde 400 a 1000 PPM (Nivel de CO2)
  unidad_medida = "PPM"

  lectura_sensor = {
     'tenant_id': tenant_id,
     'lectura_id': sensor_id + "." + fecha_hora,
     'lectura_datos': {
        'medicion': medicion,
        'unidad_medida': unidad_medida
     }
  }

  # Publicar en SNS
  sns_client = boto3.client('sns')
  response_sns = sns_client.publish(
     TopicArn = 'arn:aws:sns:us-east-1:447891120606:TemaSensorIoT',   # resaltado en amarillo (a reemplazar)
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
```

## Slide 7

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT".

Paso 3: Crear una suscripción de correo electrónico válido al tema SNS "TemaSensorIoT" y colocar la siguiente política de filtro.

Diagrama pequeño: condición de texto `tenant_id = "FAB1" y sensor_id = "CO2" y medición > 800 PPM` con una flecha hacia un ícono de sobre de correo.

Política de filtro (JSON):
```json
{
  "tenant_id": [
    "FAB1"
  ],
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
```

## Slide 8

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT".

Paso 4: Crear regla en EventBridge "SimuladorSensorIoT" que llame al lambda "GenerarEventoSensorIoT" cada 1 minuto.

Captura de pantalla de la consola AWS EventBridge, dos paneles:
- Izquierdo "Definición de detalles de reglas": campo Nombre = "SimuladorSensorIoT" (resaltado amarillo); Descripción vacía; Bus de eventos = "default"; toggle "Habilitar la regla en el bus de eventos seleccionado" activado; Tipo de regla con dos opciones (radio buttons): "Regla con un patrón de eventos" vs "Programar" (seleccionada, resaltada en azul). Botones Cancelar / Siguiente (con check verde).
- Derecho "Definir programación": "Patrón de programación" con dos opciones: "Una programación detallada..." vs "Un horario que se ejecuta con una frecuencia periódica; p. ej., cada 10 minutos." (seleccionada, resaltada amarillo). "Expresión de frecuencia": campo Valor = "1" (resaltado amarillo), Unidad = "Minutos" (resaltado amarillo). Botones Cancelar / Anterior / Siguiente (con check verde).
- Botón naranja superior "Crear regla".

## Slide 9

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT".

Captura de pantalla consola AWS EventBridge, panel "Seleccionar destinos":
- Aviso azul de Permisos: EventBridge configurará automáticamente los permisos correspondientes.
- "Destino 1": Tipos de destino con radio buttons: "Bus de eventos de EventBridge", "Destino de la API de EventBridge", "Servicio de AWS" (seleccionado, resaltado amarillo). "Seleccione un destino" = "Función Lambda" (resaltado amarillo). "Función" = "GenerarEventoSensorIoT" (resaltado amarillo), con botón de refrescar.
- Botones "Añadir otro destino", Cancelar, Anterior, Siguiente (check verde).
- Botón naranja "Crear regla" arriba a la derecha.
- Diagrama pequeño al lado: EventBridge → GenerarEventoSensorIoT (Lambda), con reloj "Cada 1 min SimuladorSensorIoT" debajo de EventBridge.

## Slide 10

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT".

Paso 5: Esperar unos 6 minutos y verificar si le ha llegado algún correo notificando este filtro.

Diagrama pequeño: condición de texto `tenant_id = "FAB1" y sensor_id = "CO2" y medición > 800 PPM` con flecha hacia ícono de sobre de correo.

## Slide 11

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT".

Paso 6: Crear tabla dynamoDB "t_sensor_iot_FAB1".

Ícono DynamoDB con etiqueta "Amazon DynamoDB t_sensor_iot_FAB1". Captura/tabla de consola DynamoDB con columnas: Nombre, Estado, Clave de partición, Clave de ordenación. Fila:
| Nombre | Estado | Clave de partición | Clave de ordenación |
|---|---|---|---|
| t_sensor_iot_FAB1 | Creando | tenant_id (S) | lectura_id (S) |

## Slide 12

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT".

Paso 7: Crear lambda "InsertarEventoSensorIoT" con este código fuente.
Paso 8: Crear cola SQS "ColaSensorIoTFAB1" que **desencadene** el lambda "InsertarEventoSensorIoT" y con **política de acceso** para tema SNS "TemaSensorIoT".
Paso 9: Suscribir la cola SQS "ColaSensorIoTFAB1" al tema SNS "TemaSensorIoT" con política de filtro (JSON abajo).

Diagrama pequeño: filtro `tenant_id = "FAB1"` → Amazon SQS "ColaSensorIoTFAB1" → Lambda "InsertarEventoSensorIoT".

Política de filtro (JSON):
```json
{
  "tenant_id": [
    "FAB1"
  ]
}
```

Código fuente (Python, Lambda):
```python
import json
import boto3

def lambda_handler(event, context):
  # Entrada (json)
  body = json.loads(event['Records'][0]['body'])
  lectura_sensor = json.loads(body['Message'])
  # Proceso
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('t_sensor_iot_FAB1')

  response = table.put_item(Item=lectura_sensor)
  # Salida (json)
  return {
     'statusCode': 200,
     'response': response
  }
```

## Slide 13

Título: "Event-driven architecture / Ejercicio 1 - Evento Nueva Lectura Sensor IoT".

Paso 10: Valide que se registren lecturas del sensor de CO2 en la tabla dynamoDB "t_sensor_iot_FAB1".

Captura/tabla de consola DynamoDB con columnas: tenant_id, lectura_id, lectura_datos. Filas de ejemplo:
| tenant_id | lectura_id | lectura_datos |
|---|---|---|
| FAB1 | CO2.2022-10-26.01:45:48.591414 | {"unidad_medida":{"S":"PPM"},"medicion":{"N":"807"}} |
| FAB1 | CO2.2022-10-26.01:46:48.060123 | {"unidad_medida":{"S":"PPM"},"medicion":{"N":"948"}} |
| FAB1 | CO2.2022-10-26.01:47:48.047735 | {"unidad_medida":{"S":"PPM"},"medicion":{"N":"785"}} |

## Slide 14

Slide de índice "Contenido" (misma plantilla lateral naranja), ahora con el ítem 3 resaltado en negrita/subrayado:
1. Objetivo del taller 4
2. Ejercicio 1: Evento Nueva Lectura Sensor IoT
3. **Ejercicio 2: Ejercicio propuesto** (resaltado)
4. Cierre

## Slide 15

Título: "Event-driven architecture / Ejercicio 2 - Propuesto". Lista de instrucciones del ejercicio propuesto:
- En lambda "GenerarEventoSensorIoT" agregue para tenant_id = "FAB1" un nuevo sensor_id = "TEMP" que genere aleatoriamente lectura entre 10 y 60 °C (grados Celsius) y utilice como unidad_medida = "CELSIUS".
- Agregue una suscripción de correo electrónico con el filtro indicado en amarillo.
- Verifique que se inserten las lecturas del nuevo sensor en tabla dynamoDB y que llegue el correo cuando se cumpla el filtro.
- Muestre evidencia de correo y registros en tabla en padlet indicado por docente.

Diagrama de arquitectura (mismo diagrama base del slide 5, ampliado con nueva rama resaltada en amarillo):
- **EventBridge** (cada 1 min, "SimuladorSensorIoT") → **GenerarEventoSensorIoT** (Lambda) → JSON "Medición Sensor IoT" → **Amazon SNS "TemaSensorIoT"**, con tres ramas:
  - Rama superior (correo, filtro CO2 existente): `tenant_id = "FAB1" y sensor_id = "CO2" y medición > 800 PPM` → sobre de correo
  - Rama media (filtro `tenant_id = "FAB1"`) → **Amazon SQS "ColaSensorIoTFAB1"** → **InsertarEventoSensorIoT** (Lambda) → **Amazon DynamoDB "t_sensor_iot_FAB1"**
  - Rama inferior nueva (resaltada en amarillo, correo): `tenant_id = "FAB1" y sensor_id = "TEMP" y medición > 40 CELSIUS` → sobre de correo

## Slide 16

Slide de índice "Contenido" (misma plantilla lateral naranja), ahora con el ítem 4 resaltado en negrita/subrayado:
1. Objetivo del taller 4
2. Ejercicio 1: Evento Nueva Lectura Sensor IoT
3. Ejercicio 2: Ejercicio propuesto
4. **Cierre** (resaltado)

## Slide 17

Título: "Cierre: / Event-driven architecture - Qué aprendimos?". Texto:
- Diseño e implementación de una Arquitectura de Solución basada en eventos con el servicio "SNS - Simple Notification Service" y "SQS - Simple Queue Service".

## Slide 18

Slide final de cierre. Texto: "Gracias" / "Elaborado por docente: Geraldo Colchado" (decorativa/cierre).
