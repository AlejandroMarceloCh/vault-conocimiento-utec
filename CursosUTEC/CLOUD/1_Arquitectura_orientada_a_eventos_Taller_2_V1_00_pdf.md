---
curso: CLOUD
titulo: 1. Arquitectura orientada a eventos - Taller 2 - V1.00
slides: 16
fuente: 1. Arquitectura orientada a eventos - Taller 2 - V1.00.pdf
---

## Slide 1

Portada (decorativa: logo UTEC). Texto:
- CS2032 - Cloud Computing (Ciclo 2024-1)
- Event-driven architecture
- Semana 10 - Taller 2: SNS - Simple Notification Service
- Elaborado por: Geraldo Colchado

## Slide 2

Slide de índice "Contenido" (barra lateral naranja con título "Event-driven architecture"). Lista numerada, ítem 1 resaltado en negrita/subrayado como sección actual:
1. **Objetivo del taller 2**
2. Ejercicio 1: Evento Nuevo Archivo en UTEC
3. Ejercicio 2: Ejercicio propuesto
4. Cierre

## Slide 3

Título: "Event-driven architecture / Objetivo del Taller 2".
Texto: Diseño e implementación de una Arquitectura de Solución basada en eventos con el servicio "SNS - Simple Notification Service".

## Slide 4

Slide de índice "Contenido" (mismo layout que slide 2), ítem 2 resaltado como sección actual:
1. Objetivo del taller 1
2. **Ejercicio 1: Evento Nuevo Archivo en UTEC**
3. Ejercicio 2: Ejercicio propuesto
4. Cierre

## Slide 5

Título: "Event-driven architecture / Ejercicio 1 - Evento Nuevo Archivo en UTEC".
Texto: "Implemente la siguiente arquitectura para procesar el evento 'Nuevo Archivo en UTEC'".

Diagrama de arquitectura (título dentro de la imagen: "Diagrama de Arquitectura de Solución basada en eventos - Nuevo Archivo en UTEC"), flujo de izquierda a derecha:
- **Bucket S3** (ícono balde rojo, etiqueta "Evento Nuevo Archivo") → emite `{JSON}` "datos nuevo archivo" →
- **Lambda "LeerMetadataArchivo"** (ícono λ) → emite `{JSON}` "datos nuevo archivo con Metadata" →
- **Amazon SNS** (ícono embudo/tema) → se bifurca en dos filtros, ambos con condición `tenant_id = 'UTEC'`:
  - Rama superior (ícono embudo azul) → **e-mail a docente** (ícono @ sobre)
  - Rama inferior (ícono embudo azul) → **Lambda "CrearArchivo_UTEC"** (ícono λ) → **Amazon DynamoDB** tabla `t_archivos_UTEC`

## Slide 6

Título: "Event-driven architecture / Ejercicio 1 - Evento Nuevo Archivo en UTEC".
Paso 1: Crear un bucket S3 con nombre único con la siguiente estructura de carpetas.

Captura de pantalla consola S3 (breadcrumb: Amazon S3 > Buckets > `gcolchado3` resaltado en amarillo). Tabla de contenido del bucket:

| Nombre | Tipo |
|---|---|
| universidades/ | Carpeta |
| ├ UNIV2/ | Carpeta |
| ├ UNIV3/ | Carpeta |
| └ UTEC/ | Carpeta |

## Slide 7

Título: "Event-driven architecture / Ejercicio 1 - Evento Nuevo Archivo en UTEC".

Paso 2 (columna izquierda): Crear un lambda "LeerMetadataArchivo" con este código fuente:
```python
import json

def lambda_handler(event, context):
  print(event) # Revisar en Cloud Watch
  # TODO implement
  return {
     'statusCode': 200,
     'body': json.dumps('Hello from Lambda!')
  }
```

Paso 3 (columna derecha): Configure en bucket una notificación de evento hacia el lambda.

Captura de consola S3 (izquierda de la columna derecha): breadcrumb Amazon S3 > Buckets > gcolchado3, pestañas Objetos/**Propiedades**(resaltada)/Permisos, botón "Crear notificación de eventos", formulario "Crear notificación de eventos" con "Configuración general" → campo "Nombre del evento" = `NuevoArchivo` (resaltado amarillo).

Captura panel derecho "Tipos de eventos": checkbox marcado "Todos los eventos de creación de objetos" (s3:ObjectCreated:*, resaltado amarillo) bajo "Creación del objeto". Sección "Destino": radio "Función Lambda" seleccionado. "Especificar Función Lambda": radio "Elija uno de los Funciones de Lambda" seleccionado, campo "Función Lambda" = `LeerMetadataArchivo` (resaltado amarillo). Botón naranja "Guardar cambios".

## Slide 8

Título: "Event-driven architecture / Ejercicio 1 - Evento Nuevo Archivo en UTEC".
Paso 4: Suba un archivo al directorio y valide logs del lambda "LeerMetadataArchivo" en Cloud Watch.

Captura consola S3 izquierda: breadcrumb gcolchado3 > universidades/ > UTEC/. Tabla:

| Nombre | Tipo | Última modificación | Tamaño |
|---|---|---|---|
| archivo01.txt | txt | 17 Oct 2022 5:28:41 PM -05 | 6.0 B |

Panel derecho "Cloud Watch" — log del evento (JSON de S3 event notification), campos clave resaltados en amarillo (`eventTime`, `bucket.name`, `object.key`, `object.size`):
```
{'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1',
'eventTime': '2022-10-17T22:28:40.885Z', 'eventName': 'ObjectCreated:Put',
'userIdentity': {'principalId': 'AWS:AROAWQSDEEHPHKPNON4UA:user2087205=Test_Student'},
'requestParameters': {'sourceIPAddress': '148.102.115.41'},
'responseElements': {'x-amz-request-id': 'R8TNAZMC5FZA7MC7', 'x-amz-id-2':
'GjFjKV9/SgpLNzZwVwwaUVp6/Te8waoNX6cWYal1GcekO+KcDTRWcZS2/N1b1GKqHwHlasJEEnxZloIdso769X2koVSL2iv8'},
's3': {'s3SchemaVersion': '1.0', 'configurationId': 'NuevoArchivo',
'bucket': {'name': 'gcolchado3', 'ownerIdentity': {'principalId': 'A24RZ2Q7S369PD'},
'arn': 'arn:aws:s3:::gcolchado3'},
'object': {'key': 'universidades/UTEC/archivo01.txt', 'size': 6,
'eTag': '5bc8c567a89112d5f408a8af4f17970d', 'sequencer': '00634DD718D7C9D664'}}}]}
```

## Slide 9

Título: "Event-driven architecture / Ejercicio 1 - Evento Nuevo Archivo en UTEC".
Paso 5: Modifique lambda "LeerMetadataArchivo" para obtener metadata identificada en Cloud Watch y pruebe con archivo.

Captura consola S3 (izquierda): breadcrumb gcolchado3 > universidades/ > UTEC/. Tabla: archivo01.txt, txt, 17 Oct 2022 6:25:29 PM -05, 6.0 B.

Código lambda (centro):
```python
import json

def lambda_handler(event, context):
  print(event) # Revisar en Cloud Watch
  # Entrada (json)
  archivo_id = event['Records'][0]['s3']['object']['key']
  tenant_id = archivo_id.split('/')[1] # UTEC, UNIV1, etc.
  archivo_last_modified = event['Records'][0]['eventTime']
  archivo_size = event['Records'][0]['s3']['object']['size']
  bucket_name = event['Records'][0]['s3']['bucket']['name']
  archivo = {
     'tenant_id': tenant_id,
     'archivo_id': archivo_id,
     'archivo_datos': {
        'last_modified': archivo_last_modified,
        'size': archivo_size,
        'bucket_name': bucket_name
     }
  }
  print(archivo)
  # TODO implement
  return {
     'statusCode': 200,
     'body': json.dumps('Hello from Lambda!')
  }
```

Panel derecho "Cloud Watch" — salida del `print(archivo)`:
```
{'tenant_id': 'UTEC', 'archivo_id': 'universidades/UTEC/archivo01.txt',
'archivo_datos': {'last_modified': '2022-10-17T23:25:28.543Z', 'size': 6,
'bucket_name': 'gcolchado3'}}
```

## Slide 10

Título: "Event-driven architecture / Ejercicio 1 - Evento Nuevo Archivo en UTEC".

Columna izquierda (pasos de texto):
- Paso 6: Cree un tema "TemaNuevoArchivo"
- Paso 7: Modifique el lambda "LeerMetadataArchivo" para publicar en el tema "TemaNuevoArchivo"
- Paso 8: Cree una suscripción de correo electrónico al tema "TemaNuevoArchivo" con filtro tenant_id = 'UTEC' y confirme el enlace en su correo.
- Paso 9: Suba un archivo al bucket (universidades/UTEC/) y verifique si le llegó el correo electrónico.
- Paso 10: Suba un archivo al bucket (universidades/UNIV2/) y verifique que **no** le llegue correo electrónico.

Columna central — código lambda modificado (resaltado amarillo el bloque de publicación SNS):
```python
import json
import boto3

def lambda_handler(event, context):
  # Entrada (json)
  archivo_id = event['Records'][0]['s3']['object']['key']
  tenant_id = archivo_id.split('/')[1] # UTEC, UNIV1, etc.
  archivo_last_modified = event['Records'][0]['eventTime']
  archivo_size = event['Records'][0]['s3']['object']['size']
  bucket_name = event['Records'][0]['s3']['bucket']['name']
  archivo = {
     'tenant_id': tenant_id,
     'archivo_id': archivo_id,
     'archivo_datos': {
        'last_modified': archivo_last_modified,
        'size': archivo_size,
        'bucket_name': bucket_name
     }
  }
  # Publicar en SNS
  sns_client = boto3.client('sns')
  response_sns = sns_client.publish(
     TopicArn = 'arn:aws:sns:us-east-1:447891120606:TemaNuevoArchivo',
     Subject = 'Nuevo Archivo',
     Message = json.dumps(archivo),
     MessageAttributes = {
        'tenant_id': {'DataType': 'String', 'StringValue': tenant_id }
     }
  )
  # TODO implement
  return {
     'statusCode': 200,
     'body': response_sns
  }
```

Columna derecha — captura de correo Gmail recibido: asunto "Nuevo Archivo" (Recibidos), remitente "AWS Notifications" 18:48, cuerpo:
```
{"tenant_id": "UTEC", "archivo_id": "universidades/UTEC/archivo01.txt", "archivo_datos": {"last_modified": "2022-10-17T23:48:49.916Z", "size": 6, "bucket_name": "gcolchado3"}}
```

## Slide 11

Título: "Event-driven architecture / Ejercicio 1 - Evento Nuevo Archivo en UTEC".

Columna izquierda (pasos de texto):
- Paso 11: Crear tabla DynamoDB "t_archivos_UTEC"
- Paso 12: Crear lambda "CrearArchivo_UTEC"
- Paso 13: Cree una suscripción del lambda "CrearArchivo_UTEC" al tema "TemaNuevoArchivo" con filtro tenant_id = 'UTEC'
- Paso 14: Suba un archivo al bucket (universidades/UTEC/) y verifique si graba registro en tabla.
- Paso 15: Suba un archivo al bucket (universidades/UNIV2/) y verifique que **no** grabe registro en tabla

Captura tabla DynamoDB (bajo el Paso 11):

| Nombre | Estado | Clave de partición | Clave de ordenación |
|---|---|---|---|
| t_archivos_UTEC | ✓ Activo | tenant_id (S) | archivo_id (S) |

Columna derecha — código lambda "CrearArchivo_UTEC":
```python
import json
import boto3

def lambda_handler(event, context):
  # Entrada (json)
  print(event) # Revisar en CloudWatch
  archivo_json = json.loads(event['Records'][0]['Sns']['Message'])
  # Proceso
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('t_archivos_UTEC')
  archivo = {
     'tenant_id': archivo_json['tenant_id'],
     'archivo_id': archivo_json['archivo_id'],
     'archivo_datos': archivo_json['archivo_datos']
  }
  print(archivo) # Revisar en CloudWatch
  response = table.put_item(Item=archivo)
  # Salida (json)
  return {
     'statusCode': 200,
     'response': response
  }
```

Al pie, captura de tabla DynamoDB con registro grabado:

| tenant_id | archivo_id | archivo_datos |
|---|---|---|
| UTEC | universidades/UTEC/archivo02.txt | {"size": {"N": "6"}, "last_modified": {"S": "2022-10-18T01:11:34.552Z"}, "bucket_name": {"S": "gcolchado3"}} |

## Slide 12

Slide de índice "Contenido" (mismo layout), ítem 3 resaltado como sección actual:
1. Objetivo del taller 1
2. Ejercicio 1: Evento Nuevo Archivo en UTEC
3. **Ejercicio 2: Ejercicio propuesto**
4. Cierre

## Slide 13

Título: "Event-driven architecture / Ejercicio 2- Propuesto".
Texto: Se le solicita que pueda identificar en la metadata del archivo el código del curso y el código de alumno. Diseñe e implemente los cambios. Se requiere que se grabe esa metadata en la tabla t_archivos_UTEC. Presente la solución en el padlet indicado por el docente con la evidencia.

Diagrama (idéntico al de la Slide 5, se repite como referencia de la arquitectura base a modificar): "Diagrama de Arquitectura de Solución basada en eventos - Nuevo Archivo en UTEC". Flujo: Bucket S3 ("Evento Nuevo Archivo") → {JSON} datos nuevo archivo → Lambda "LeerMetadataArchivo" → {JSON} datos nuevo archivo con Metadata → Amazon SNS → bifurca en dos filtros `tenant_id = 'UTEC'`: uno hacia e-mail a docente, otro hacia Lambda "CrearArchivo_UTEC" → Amazon DynamoDB tabla `t_archivos_UTEC`.

## Slide 14

Slide de índice "Contenido" (mismo layout), ítem 4 resaltado como sección actual:
1. Objetivo del taller 1
2. Ejercicio 1: Evento Nuevo Archivo en UTEC
3. Ejercicio 2: Ejercicio propuesto
4. **Cierre**

## Slide 15

Título: "Cierre: / Event-driven architecture - Qué aprendimos?".
Texto: Diseño e implementación de una Arquitectura de Solución basada en eventos con el servicio "SNS - Simple Notification Service".

## Slide 16

Slide de cierre (decorativa). Texto: "Gracias" / "Elaborado por docente: Geraldo Colchado".
