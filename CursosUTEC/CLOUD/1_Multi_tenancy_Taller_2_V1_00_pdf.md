---
curso: CLOUD
titulo: 1. Multi-tenancy - Taller 2 - V1.00
slides: 35
fuente: 1. Multi-tenancy - Taller 2 - V1.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Multi-tenancy
Semana 9 - Taller 2: Microservicio Multi-tenancy

                       ELABORADO POR: GERALDO COLCHADO
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD
                                 con servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
Objetivo del taller 2:
Microservicio Multi-tenancy
• Diseñar e implementar un Microservicio Multi-tenancy con
  servicio Lambda (Serverless) y Api Gateway (Serverless)
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD
                                 con servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
           Function as a Service (FaaS)
           Lambda (Serverless)




Fuente: https://aws.amazon.com/es/lambda/
        Ejercicio 1:
        Crear una función Lambda - ListarAlumnos
•   Paso 1: Requisito: Tener creada
    la tabla DynamoDB t_alumnos

•   Paso 2: Crear la función lambda
         Ejercicio 1:
         Crear una función Lambda - ListarAlumnos
•   Paso 3: Escribir el siguiente código fuente y “Deploy”
                                                             import boto3 # import Boto3
                                                             from boto3.dynamodb.conditions import Key # import Boto3 conditions

                                                             def lambda_handler(event, context):
                                                               # Entrada (json)
                                                               tenant_id = event['tenant_id']
                                                               # Proceso
                                                               dynamodb = boto3.resource('dynamodb')
                                                               table = dynamodb.Table('t_alumnos')
                                                               response = table.query(
                                                                  KeyConditionExpression=Key('tenant_id').eq(tenant_id)
                                                               )
                                                               items = response['Items']
                                                               num_reg = response['Count']
                                                               # Salida (json)
                                                               return {
                                                                  'statusCode': 200,
                                                                  'tenant_id':tenant_id,
                                                                  'num_reg': num_reg,
                                                                  'alumnos': items
                                                               }
            Ejercicio 1:
            Crear una función Lambda - ListarAlumnos
•   Paso 4: Probar el lambda
    con esta entrada

    {
        "tenant_id": "UTEC"
    }
Ejercicio 1:
Crear una función Lambda - ListarAlumnos
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD
                                 con servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
                Ejercicio 2:
                Crear una función Lambda - CrearAlumno
                                                            import boto3
•   Paso 1: Escribir el siguiente                           def lambda_handler(event, context):
    código fuente y “Deploy”                                  # Entrada (json)
                                                              tenant_id = event['tenant_id']
                                                              alumno_id = event['alumno_id']
•   Paso 2: Probar el lambda con                              alumno_datos = event['alumno_datos']
    esta entrada:                                             # Proceso
    {
                                                              dynamodb = boto3.resource('dynamodb')
        "tenant_id": "UTEC",                                  table = dynamodb.Table('t_alumnos')
        "alumno_id": "202099998",                             alumno = {
        "alumno_datos": {
               "nombre": "Geraldo Colchado",                     'tenant_id': tenant_id,
               "sexo": "M",                                      'alumno_id': alumno_id,
               "fecha_nac": "2000-09-01",
               "celular": "999736332",
                                                                 'alumno_datos': alumno_datos
               "domicilio": {                                 }
                        "direcc": "Av. Javier Prado 158",     response = table.put_item(Item=alumno)
                        "distrito": "San Isidro",
                        "provincia": "Lima",                  # Salida (json)
                        "departamento": "Lima",               return {
                        "pais": "Perú"
               }
                                                                 'statusCode': 200,
        }                                                        'response': response
    }                                                         }
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD con
                                 servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
                Ejercicio 3:
                Crear una función Lambda - ModificarAlumno
                                                            import boto3
•   Paso 1: Escribir el siguiente
                                                            def lambda_handler(event, context):
    código fuente y “Deploy”                                  # Entrada (json)
                                                              tenant_id = event['tenant_id']
                                                              alumno_id = event['alumno_id']
•   Paso 2: Probar el lambda con                              alumno_datos = event['alumno_datos']
                                                              # Proceso
    esta entrada:                                             dynamodb = boto3.resource('dynamodb')
                                                              table = dynamodb.Table('t_alumnos')
    {                                                         response = table.update_item(
        "tenant_id": "UTEC",                                     Key={
        "alumno_id": "202099998",                                   'tenant_id': tenant_id,
        "alumno_datos": {                                           'alumno_id': alumno_id
               "nombre": "Geraldo Colchado Ruiz",                },
               "sexo": "M",
                                                                 UpdateExpression="set alumno_datos=:alumno_datos",
               "fecha_nac": "2000-09-01",
               "celular": "999736332",
                                                                 ExpressionAttributeValues={
               "domicilio": {                                       ':alumno_datos': alumno_datos
                        "direcc": "Av. Javier Prado 158",        },
                        "distrito": "San Borja",                 ReturnValues="UPDATED_NEW"
                        "provincia": "Lima",                  )
                        "departamento": "Lima",               # Salida (json)
                        "pais": "Perú"                        return {
               }                                                 'statusCode': 200,
        }                                                        'response': response
    }
                                                              }
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD con
                                 servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
            Ejercicio 4:
            Crear una función Lambda - BuscarAlumno
                                    import boto3
•   Paso 1: Escribir el siguiente   def lambda_handler(event, context):
    código fuente y “Deploy”          # Entrada (json)
                                      tenant_id = event['tenant_id']
                                      alumno_id = event['alumno_id']
•   Paso 2: Probar el lambda con      # Proceso
    esta entrada:                     dynamodb = boto3.resource('dynamodb')
                                      table = dynamodb.Table('t_alumnos')
                                      response = table.get_item(
                                         Key={
    {
                                            'tenant_id': tenant_id,
        "tenant_id": "UTEC",                'alumno_id': alumno_id
        "alumno_id": "202099998"         }
    }                                 )
                                      # Salida (json)
                                      return {
                                         'statusCode': 200,
                                         'response': response
                                      }
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD con
                                 servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
            Ejercicio 5:
            Crear una función Lambda - EliminarAlumno
                                    import boto3
•   Paso 1: Escribir el siguiente
                                    def lambda_handler(event, context):
    código fuente y “Deploy”          # Entrada (json)
                                      tenant_id = event['tenant_id']
•   Paso 2: Probar el lambda con      alumno_id = event['alumno_id']
                                      # Proceso
    esta entrada:                     dynamodb = boto3.resource('dynamodb')
                                      table = dynamodb.Table('t_alumnos')
                                      response = table.delete_item(
                                         Key={
    {                                       'tenant_id': tenant_id,
        "tenant_id": "UTEC",                'alumno_id': alumno_id
        "alumno_id": "202099998"         }
    }                                 )
                                      # Salida (json)
                                      return {
                                         'statusCode': 200,
                                         'response': response
                                      }
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD
                                 con servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
           Ejercicio 6:
           Servicio Api Gateway (Serverless)




Fuente: https://aws.amazon.com/es/api-gateway/
Ejercicio 6:
Publicar microservicio como API Rest CRUD con servicio
Api Gateway
•   Paso 1: Crear API Rest en
    servicio Api Gateway

       Ejercicio 6:
       Publicar microservicio como API Rest CRUD con servicio
       Api Gateway
•   Paso 2: Crear
    recurso alumnos
        Ejercicio 6:
        Publicar microservicio como API Rest CRUD con servicio
        Api Gateway
•   Paso 3: Crear    •   Paso 4: Crear   •   Paso 5: Asociar a Lambda ListarAlumnos
    recurso listar       método POST
Ejercicio 6:
Publicar microservicio como API Rest CRUD con servicio
Api Gateway
•   Paso 6: Probar
Ejercicio 6:
Publicar microservicio como API Rest CRUD con servicio
Api Gateway
•   Paso 7: Habilitar CORS   •   Paso 8: Implementar la Api
Ejercicio 6:
Publicar microservicio como API Rest CRUD con servicio
Api Gateway
•   Paso 9: Probar la api
    ListarAlumnos en postman
        Ejercicio 6:
        Publicar microservicio como API Rest CRUD con servicio
        Api Gateway
•   Paso 10: Repetir
    Pasos 3 al 8 para el
    resto de recursos
    según esta imagen
        Ejercicio 6:
        Publicar microservicio como API Rest CRUD con servicio
        Api Gateway
•   Paso 11: Probar la
    api CrearAlumno en
    postman
        Ejercicio 6:
        Publicar microservicio como API Rest CRUD con servicio
        Api Gateway
•   Paso 12: Probar la
    api ModificarAlumno
    en postman
        Ejercicio 6:
        Publicar microservicio como API Rest CRUD con servicio
        Api Gateway
•   Paso 13: Probar la
    api EliminarAlumno
    en postman
        Ejercicio 6:
        Publicar microservicio como API Rest CRUD con servicio
        Api Gateway
•   Paso 14: Probar la
    api BuscarAlumno en
    postman
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD
                                 con servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
      Ejercicio 7:
      Ejercicio propuesto para la casa
                                          json de entrada a lambda   Funcionalidad para:
• Implemente una sola función Lambda      {                          Listar alumnos
                                              "tenant_id": "UTEC",
  en Python 3 que reciba un campo             "action": "listar"
  adicional “action” y en base a ello     }
                                          …                          Crear alumno
  ejecute las instrucciones para Listar    "action": "crear"
  Alumnos y para Crear, Modificar,        …
                                          …                          Modificar alumno
  Eliminar y Buscar un alumno.             "action": "modificar"
                                          …

• Publicar como Api REST CRUD usando      …
                                           "action": "eliminar"
                                                                     Eliminar alumno

  Api Gateway                             …
                                          …                          Buscar alumno
                                           "action": "buscar"
                                          …
                              1. Objetivo del taller 2
                              2. Ejercicio 1: Crear una función Lambda - ListarAlumnos
                              3. Ejercicio 2: Crear una función Lambda - CrearAlumno
                              4. Ejercicio 3: Crear una función Lambda - ModificarAlumno
Contenido
Microservicio Multi-tenancy   5. Ejercicio 4: Crear una función Lambda - BuscarAlumno
                              6. Ejercicio 5: Crear una función Lambda - EliminarAlumno
                              7. Ejercicio 6: Publicar microservicio como API Rest CRUD
                                 con servicio Api Gateway
                              8. Ejercicio 7: Ejercicio propuesto
                              9. Cierre
Cierre:
Microservicio Multi-tenancy - Qué aprendimos?
• Diseño e implementación de un Microservicio Multi-tenancy con
  servicio Lambda (Serverless) y Api Gateway (Serverless)
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
