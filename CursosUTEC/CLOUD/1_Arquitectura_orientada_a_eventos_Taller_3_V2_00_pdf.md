---
curso: CLOUD
titulo: 1. Arquitectura orientada a eventos - Taller 3 - V2.00
slides: 28
fuente: 1. Arquitectura orientada a eventos - Taller 3 - V2.00.pdf
---

## Slide 1

Portada del curso (decorativa: logo UTEC en esquina superior derecha, barra naranja inferior).

Texto:
- "CS2032 - Cloud Computing (Ciclo 2024-1)"
- "Event-driven architecture"
- "Semana 11 - Taller 3: SQS - Simple Queue Service"
- "ELABORADO POR: GERALDO COLCHADO"
- "Con apoyo de Asistentes de Cátedra y Laboratorio:
  - Sofía García (sofia.garcia@utec.edu.pe)
  - Rubén Aaron Coorahua (ruben.coorahua@utec.edu.pe)"

## Slide 2

Slide "Contenido" (tabla de contenido, franja lateral izquierda naranja con título "Contenido" / "Event-driven architecture"). Ítem 1 resaltado en negrita/subrayado indicando la sección actual.

Lista numerada del contenido del taller:
1. **Objetivo del taller 3** (resaltado, sección activa)
2. SQS - Simple Queue Service
3. Ejercicio 1: Despacho de pedidos
4. Ejercicio 2: Ejercicio propuesto
5. Cola de Mensajes Fallidos (DLQ)
6. Ejercicio 3: DLQ
7. Cierre

## Slide 3

Título: "Event-driven architecture / Objetivo del Taller 3"

Texto: "Diseño e implementación de una Arquitectura de Solución basada en eventos con el servicio "SQS - Simple Queue Service"."

## Slide 4

Slide de tabla de contenido (igual estructura que slide 2), ahora con el ítem 2 resaltado en negrita/subrayado: "SQS - Simple Queue Service".

## Slide 5

Título: "Event-driven architecture / SQS - Simple Queue Service"

Captura de pantalla de la página oficial de AWS SQS (aws.amazon.com/es/sqs/). Recuadro oscuro superior con el título "Amazon Simple Queue Service" y subtítulo "Colas de mensajes completamente administradas para microservicios, sistemas distribuidos y aplicaciones sin servidor".

Debajo, texto descriptivo (con fragmento resaltado en amarillo): "Amazon Simple Queue Service (Amazon SQS) es un **servicio de colas de mensajes completamente administrado que permite desacoplar y** ajustar la escala de microservicios, sistemas distribuidos y aplicaciones sin servidor. SQS elimina la complejidad y los gastos generales asociados con la administración y el funcionamiento del middleware orientado a mensajes, y permite a los desarrolladores centrarse en la diferenciación del trabajo. Con SQS, puede enviar, almacenar y recibir mensajes entre componentes de software de cualquier volumen, sin pérdida de mensajes ni la necesidad de que otros servicios estén disponibles. Comience a usar SQS en minutos con la consola de administración de AWS, la interfaz de línea de comandos o el SDK de AWS de su elección, y tres comandos simples."

"SQS ofrece dos tipos de colas de mensajes. Las colas estándar ofrecen una capacidad de procesamiento máxima, un ordenamiento de mejor esfuerzo y una entrega al menos una vez. Las colas FIFO de SQS están diseñadas para garantizar que los mensajes se procesen exactamente una vez, en el orden exacto en el que se enviaron."

Pie de página: "Fuente: https://aws.amazon.com/es/sqs/"

## Slide 6

Slide de tabla de contenido, ítem 3 resaltado en negrita/subrayado: "Ejercicio 1: Despacho de pedidos".

## Slide 7

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Diagrama de arquitectura titulado "Diagrama de Arquitectura de Solución de Despacho de Pedidos (Desacoplada y Asíncrona)". Descripción del flujo (de izquierda a derecha):
- Icono "Cliente (Registrar Pedido)" (persona) conecta hacia abajo con "Amazon API Gateway - Microservicio pedidos", que tiene dos rutas: `/pedidos/registrar` y `/pedidos/procesar`.
- `/pedidos/registrar` invoca el lambda **RegistrarPedido** (icono λ naranja), que emite un evento JSON "Evento Nuevo Pedido" hacia **Amazon SQS - Cola Pedidos** (icono SQS).
- La cola SQS conecta con el lambda **ProcesarPedido** (icono λ naranja), el cual escribe en la tabla DynamoDB **t_pedidos_procesados** (icono morado de rayo/base de datos).
- `/pedidos/procesar` también conecta con ProcesarPedido.
- A la derecha, ProcesarPedido conecta con tres actores humanos: "Despachador 1", "Despachador 2", "Despachador 3", cada uno asociado a un ícono de camión de reparto.

## Slide 8

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Texto: "Paso 1: Crear Cola de Pedidos (sqs-pedidos)"

Captura de pantalla de la consola AWS SQS, formulario "Crear una cola":
- Breadcrumb: Amazon SQS > Colas > Crear una cola
- Sección "Detalles" > "Tipo": dos opciones de radio button:
  - **Estándar** (seleccionada): "No se conserva el orden de los mensajes donde se entrega al menos una vez" — "Entrega al menos una vez", "Orden de mejor esfuerzo"
  - **FIFO**: "Se conserva el orden de mensajes en donde el primero que en entrar, es el primero en salir" — "Entrega primero en entrar/primero en salir", "Procesamiento único"
- Aviso: "No puede cambiar el tipo de cola después de crear una cola."
- Campo "Nombre": `sqs-pedidos` (resaltado en amarillo)

## Slide 9

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Texto:
- "Paso 2: Crear Lambda RegistrarPedido con tiempo de espera de 10 segundos y reemplace el `queue_url`"
- "Paso 3: Crear Api Gateway `pedidos` con recurso `/pedidos/registrar` con un método `POST` que ejecute el lambda anterior y habilite `CORS`"

Captura de pantalla: formulario "Habilitar CORS" de API Gateway, sección "Configuración de CORS":
- "Respuestas de puerta de enlace": checkboxes marcados "Default 4XX" y "Default 5XX" (resaltados en amarillo)
- "Access-Control-Allow-Methods": checkbox "OPTIONS" (no marcado), checkbox "POST" marcado (resaltado en amarillo)

## Slide 10

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Texto: "Paso 4: Pruebe con postman registrar un pedido"

Captura de pantalla de Postman:
- Método `POST` (resaltado) a URL `https://h8dg6269x6.execute-api.us-east-1.amazonaws.com/prod/pedidos/registrar` (con `/pedidos/registrar` resaltado)
- Tab "Body" seleccionada, tipo "raw" con formato "JSON"
- JSON del body:
```json
{
  "tenant_id": "PLAZA_VEA",
  "pedido_id": 1,
  "pedido_datos": {
    "cliente_id": "jperez@gmail.com",
    "fecha_compra": "2024-06-01T14:30:00Z",
    "items": [
      {
        "item_id": "001",
        "product_name": "Detergente",
        "quantity": 2,
        "price": "60.99"
      },
      ...
```
- Respuesta abajo: Status "200 OK", Time "2.95 s", Size "827 B". Body de respuesta (tab Pretty/JSON): `{ "statusCode": 200, ...` (resaltado en amarillo)

## Slide 11

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Texto: "Paso 5: Verifique en la cola sqs-pedidos si llegó el mensaje"

Captura de pantalla de consola SQS:
- Tabla de colas: columnas Nombre, Tipo, Creado, Mensajes disponibles, Mensajes en tránsito
  | Nombre | Tipo | Creado | Mensajes disponibles | Mensajes en tránsito |
  |---|---|---|---|---|
  | sqs-pedidos | Estándar | 2024-06-02T17:33-05:00 | 1 (resaltado) | 0 |

- Panel inferior "Mensaje: 78ce5045-ba71-4b9f-ac66-457bd2ca3474" con tabs Cuerpo/Atributos/Detalles. Contenido del cuerpo del mensaje (JSON):
```json
{"tenant_id": "PLAZA_VEA", "pedido_id": 1, "pedido_datos": {"cliente_id": "jperez@gmail.com", "fecha_compra": "2024-06-01T14:30:00Z", "items": [{"item_id": "001", "product_name": "Detergente", "quantity": 2, "price": "60.99"}, {"item_id": "002", "product_name": "Lavavajilla", "quantity": 1, "price": "10.35"}], "direccion_entrega": {"calle": "Avenida Los Frutales 123", "distrito": "La Molina", "provincia": "Lima", "pais": "Perú"}}}
```

## Slide 12

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Texto: "Paso 6: Registre los otros 4 mensajes por postman"

Captura de pantalla de tabla de colas SQS (misma estructura que slide 11), mostrando ahora:
| Nombre | Tipo | Creado | Mensajes disponibles | Mensajes en tránsito |
|---|---|---|---|---|
| sqs-pedidos | Estándar | 2024-06-02T17:33-05:00 | 5 (resaltado en amarillo) | 0 |

## Slide 13

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Texto:
- "Paso 7: Crear tabla DynamoDB `t_pedidos_procesados`"
- "Paso 8: Crear lambda ProcesarPedido con tiempo de espera de 10 segundos"
- "Paso 9: En Api Gateway `pedidos` crear recurso `/pedidos/procesar` con un método `GET` que ejecute el lambda anterior y habilite `CORS`"

Captura de pantalla de consola DynamoDB (tabla de tablas):
| Nombre | Estado | Clave de partición | Clave de ordenación |
|---|---|---|---|
| t_pedidos_procesados | ✅ Activo | tenant_id (S) (resaltado) | pedido_id (N) (resaltado) |

Captura adicional (recorte a la derecha) de configuración CORS de API Gateway: checkboxes "Default 4XX", "Default 5XX", "GET" marcados.

## Slide 14

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Texto: "Paso 10: Ejecute el api en postman simulando que es el Despachador 1"

Captura de pantalla de Postman:
- Método `GET` a URL `https://h8dg6269x6.execute-api.us-east-1.amazonaws.com/prod/pedidos/procesar`
- Tabs Params/Authorization/Headers, sección "Query Params" vacía
- Respuesta (Status 200 OK), body JSON:
```json
{
  "statusCode": 200,
  "pedidos_procesados": [
    {
      "tenant_id": "PLAZA_VEA",
      "pedido_id": 1,
      "pedido_datos": {
        "cliente_id": "jperez@gmail.com",
        "fecha_compra": "2024-06-01T14:30:00Z",
    },
    {
      "tenant_id": "PLAZA_VEA",
      "pedido_id": 4,
      "pedido_datos": {
        "cliente_id": "pontaneda@gmail.com",
        "fecha_compra": "2024-06-01T17:35:15Z",
```

## Slide 15

Título: "Event-driven architecture / Ejercicio 1 - Despacho de Pedidos"

Texto: "Paso 11: Verifique si se grabaron los pedidos en tabla"

Captura de pantalla de tabla DynamoDB `t_pedidos_procesados`:
| tenant_id (Cadena) | pedido_id (Número) | pedido_datos |
|---|---|---|
| PLAZA_VEA | 1 (resaltado) | { "direccion_entrega" : { "M" : { "distrito" : { "S" : "La Molina" }, "provi... |
| PLAZA_VEA | 4 (resaltado) | { "direccion_entrega" : { "M" : { "distrito" : { "S" : "San Isidro" }, "provi... |

Texto: "Paso 12: Ejecute el api hasta procesar todos los 5 pedidos simulando que es el Despachador 2 y Despachador 3 y analice"

## Slide 16

Slide de tabla de contenido, ítem 4 resaltado en negrita/subrayado: "Ejercicio 2: Ejercicio propuesto".

## Slide 17

Título: "Event-driven architecture / Ejercicio 2 - Propuesto"

Texto (enunciado del ejercicio propuesto, sin captura de AWS):
- "Modifique el lambda ProcesarPedido para que reciba como entrada un despachador_id ("DESP-01", "DESP-02", "DESP-03") y este se grabe como campo en la tabla DynamoDB t_pedidos_procesados para identificar el despachador que procesó los pedidos. Debe modificar el método a POST en Api Gateway en pedidos/procesar."
- "En la respuesta del lambda ProcesarPedido agregue un campo con la cantidad de pedidos procesados"

Bloque de código (ejemplo de respuesta JSON esperada, con línea resaltada en amarillo):
```json
{
        "statusCode": 200,
        "cantidad_pedidos_procesados": 3,
        "pedidos_procesados": [
        ...
```

## Slide 18

Slide de tabla de contenido, ítem 5 resaltado en negrita/subrayado: "Cola de Mensajes Fallidos (DLQ)".

## Slide 19

Título: "Event-driven architecture / Cola de Mensajes Fallidos (DLQ - Dead Letter Queue)"

Cita textual: "Una cola de mensajes fallidos (DLQ) es un tipo especial de cola de mensajes que almacena temporalmente los mensajes que un sistema de software no puede procesar debido a errores."

Diagrama conceptual: icono "AWS SQS" (rosa) en la parte superior. Debajo, tres cajas conectadas por flechas: "Publisher" → cola SQS (recuadro verde con mensajes M3, M1, M4, M2) → "Consumer". Un mensaje (M2) dentro de la cola tiene una X roja grande (indicando fallo de procesamiento) y una flecha curva lo redirige hacia abajo a una caja separada rotulada "M2", etiquetada como "Dead Letter Queue - DLQ".

Pie de página: "Fuente: https://aws.amazon.com/es/what-is/dead-letter-queue/, https://siecola.com.br/blogs/aws_sqs_dlq.html"

## Slide 20

Slide de tabla de contenido, ítem 6 resaltado en negrita/subrayado: "Ejercicio 3: DLQ".

## Slide 21

Título: "Event-driven architecture / Ejercicio 3 - DLQ"

Texto lateral izquierdo (en cursiva): "Agregar una cola de mensajes fallidos (DLQ) en caso falle el registro de nuevo alumno en canvas"

Bloque de código JSON de ejemplo (payload del mensaje):
```json
{
  "tenant_id": "UTEC",
  "alumno_id": "202310295",
  "alumno_datos": {
        "nombre": "Claudia Espinoza",
        "sexo": "M",
        "fecha_nac": "2004-12-04",
        "celular": "999736371",
        "domicilio": {
                "direcc": "Av. El Polo 1767",
                "distrito": "Monterrico",
                "provincia": "Lima",
                "departamento": "Lima",
                "pais": "Perú"
        }
  }
}
```

Diagrama de arquitectura titulado "Diagrama de Arquitectura de solución / Registrar Alumno en Canvas con SQS y DLQ": el payload JSON entra a **Amazon SQS - sqs-registrar-canvas**, que desencadena (con etiqueta "Desencadenar Lambda (2 Reintentos)") el lambda **RegistrarCanvas** (icono λ naranja). Si falla el lambda, una flecha etiquetada "Si falla el Lambda, se envía a cola DLQ" lleva a una segunda cola **Amazon SQS - sqs-registrar-canvas-dlq**.

## Slide 22

Título: "Event-driven architecture / Ejercicio 3 - DLQ"

Texto:
- "Paso 1: Cree una cola de mensajes fallidos sqs-registrar-canvas-dlq"
- "Paso 2: Cree una cola sqs-registrar-canvas y configure la cola de mensajes fallidos para que sea enviado el mensaje luego de 2 reintentos fallidos de procesarlo."

Captura de pantalla de consola SQS, sección "Cola de mensajes fallidos - Opcional" (resaltado en amarillo):
- "Establezca esta cola para recibir mensajes que no se puedan entregar."
- Radio buttons: "Deshabilitada" / "Habilitada" (seleccionada)
- Campo "Elegir cola": `arn:aws:sqs:us-east-1:498917627164:sqs-registrar-canvas-dlq` (resaltado en amarillo)
- Campo "Recepciones máximas": `2` (resaltado en amarillo), con nota "Debe estar entre 1 y 1000."

## Slide 23

Título: "Event-driven architecture / Ejercicio 3 - DLQ"

Texto: "Paso 3: Cree un lambda RegistrarCanvas que genene una excepción (simulando que falla)"

Bloque de código Python (captura del editor Lambda):
```python
import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    raise Exception("Error")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
```

## Slide 24

Título: "Event-driven architecture / Ejercicio 3 - DLQ"

Texto: "Paso 4: En la cola sqs-registrar-canvas configure un desencadenador de lambda a RegistrarCanvas para que procese el mensaje"

Captura de pantalla de consola SQS, sección "Desencadenadores de Lambda (1)":
- Tabla con columnas UUID y ARN
  | UUID | ARN |
  |---|---|
  | f93b83e8-6989-4de4-bf83-750d4a3267e8 | arn:aws:lambda:us-east-1:498917627164:function:RegistrarCanvas (resaltado en amarillo) |

## Slide 25

Título: "Event-driven architecture / Ejercicio 3 - DLQ"

Texto: "Paso 5: Envíe un mensaje en la cola sqs-registrar-canvas y valide los 2 reintentos con error en CloudWatch (cada 30 segundos) y que se genere un mensaje en cola sqs-registrar-canvas-dlq"

Captura de pantalla de consola SQS:
- Panel "Enviar y recibir mensajes" para la cola sqs-registrar-canvas, con mensaje de confirmación "El mensaje se ha enviado y está listo para ser recibido." y el body del mensaje (mismo JSON del alumno de la slide 21) parcialmente visible.
- Tabla superior de colas:
  | Nombre | Tipo | Creado | Mensajes disponibles | Mensajes en tránsito |
  |---|---|---|---|---|
  | sqs-registrar-canvas | Estándar | 2024-06-09T17:25-05:00 | 0 | 1 (resaltado) |
  | sqs-registrar-canvas-dlq | Estándar | 2024-06-09T17:25-05:00 | 0 | 0 |
- Tabla inferior (después de los reintentos):
  | Nombre | Tipo | Creado | Mensajes disponibles | Mensajes en tránsito |
  |---|---|---|---|---|
  | sqs-registrar-canvas | Estándar | 2024-06-09T17:25-05:00 | 0 | 0 |
  | sqs-registrar-canvas-dlq | Estándar | 2024-06-09T17:25-05:00 | 1 (resaltado) | 0 |

## Slide 26

Slide de tabla de contenido, ítem 7 resaltado en negrita/subrayado: "Cierre".

## Slide 27

Título: "Cierre: / Event-driven architecture - Qué aprendimos?"

Texto: "Diseño e implementación de una Arquitectura de Solución basada en eventos con el servicio "SQS - Simple Queue Service"."

## Slide 28

Slide de cierre (decorativa, fondo blanco con barra naranja inferior).

Texto: "Gracias" / "Elaborado por docente: Geraldo Colchado"
