---
curso: CLOUD
titulo: 1. Multi-tenancy - Taller 1 - V1.00
slides: 18
fuente: 1. Multi-tenancy - Taller 1 - V1.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Multi-tenancy
Semana 9 - Taller 1: Base Datos No SQL Multi-tenancy

                      ELABORADO POR: GERALDO COLCHADO
                           1. Objetivo del taller 1
                           2. Ejercicio 1: Patrón 1 en DynamoDB (NoSQL)
                           3. Ejercicio 2: Ejercicio propuesto
Contenido                  4. Cierre
Base Datos No SQL Multi-
tenancy
Objetivo del taller 1:
Base Datos No SQL Multi-tenancy
• Diseñar e implementar Base de Datos NoSQL Multi-tenancy con
  Patrón 1
                           1. Objetivo del taller 1
                           2. Ejercicio 1: Patrón 1 en DynamoDB (NoSQL)
                           3. Ejercicio 2: Ejercicio propuesto
Contenido                  4. Cierre
Base Datos No SQL Multi-
tenancy
               Patrones de diseño BD Multi-tenancy
               Patrón 1: A Single, Shared Database Schema
               Un esquema de base de datos único y compartido




                                                                               Las tablas deben tener un campo “TENANT_ID”
                                                                               para identificar sus registros. Ejemplo de acceso:

                                                                               SELECT * FROM ORDERS WHERE TENANT_ID = ?
Fuentes: https://www.datamation.com/cloud/what-is-multi-tenant-architecture/
https://www.oscarblancarteblog.com/2020/07/12/multi-tenancy-principio-de-arquitectura-de-software/
              Bases de Datos
              No SQL (Conocimientos previos)




Fuente: https://youtu.be/0buKQHokLK8
             Bases de Datos
             No SQL - DynamoDB (Serverless)




                                              Para complementar:
                                              https://aws.amazon.com/es/nosql/



Fuente: https://aws.amazon.com/es/dynamodb
Patrones de diseño BD Multi-tenancy
Patrón 1: En DynamoDB (NoSQL)
                           Ejercicio 1: Diseñe e implemente en
                           DynamoDB una tabla Multi-tenancy para
                           almacenar los alumnos de una universidad.
                           Considerar que el tenant_id es un código por
                           cada universidad en mayúsculas:
          Microservicio
          “alumnos”        tenant_id: UTEC, UNIV2, UNIV3, UNIV4, etc.

          Tabla DynamoDB
          “t_alumnos”
         Ejercicio 1: Diseñe e implemente en DynamoDB una
         tabla Multi-tenancy para almacenar los alumnos de una
         universidad
•   Paso 1: Crear tabla en
    DynamoDB



•   Paso 2: Asignar los
    siguientes valores:
Ejercicio 1: Diseñe e implemente en DynamoDB una
tabla Multi-tenancy para almacenar los alumnos de una
universidad
        Ejercicio 1: Diseñe e implemente en DynamoDB una
        tabla Multi-tenancy para almacenar los alumnos de una
        universidad
                                                {
•   Paso 3: Inserte un                              "tenant_id": "UTEC",
    registro en la tabla.                           "alumno_id": "202010290",
    Previamente convierta                           "alumno_datos": {
    el formato json a                                   "nombre": "Juan Pérez",
                                                        "sexo": "M",
    “formato json de                                    "fecha_nac": "2004-12-04",
    DynamoDB” usando                                    "celular": "999736371“,
    este enlace:                                        "domicilio": {
    https://dynobase.dev/                                     "direcc": "Av. El Polo 1767",
                                                              "distrito": "Monterrico",
    dynamodb-json-                                            "provincia": "Lima",
    converter-tool/                                           "departamento": "Lima“,
                                                              "pais": "Perú"
                                                        }
                                                    }
                                                }
          Ejercicio 1: Diseñe e implemente en DynamoDB una
          tabla Multi-tenancy para almacenar los alumnos de una
          universidad
•   Paso 4: Modifique el json e inserte dos registros adicionales en la tabla. Previamente convierta el formato json a
    “formato json de DynamoDB” usando este enlace: https://dynobase.dev/dynamodb-json-converter-tool/
          Ejercicio 1: Diseñe e implemente en DynamoDB una
          tabla Multi-tenancy para almacenar los alumnos de una
          universidad
•   Paso 5: Inserte 3 registros adicionales en la tabla para UNIV2. Previamente convierta el formato json a “formato
    json de DynamoDB” usando este enlace: https://dynobase.dev/dynamodb-json-converter-tool/
                           1. Objetivo del taller 1
                           2. Ejercicio 1: Patrón 1 en DynamoDB (NoSQL)
                           3. Ejercicio 2: Ejercicio propuesto
Contenido                  4. Cierre
Base Datos No SQL Multi-
tenancy
    Ejercicio 2: Diseñe e implemente en DynamoDB
    una tabla Multi-tenancy de su preferencia

Ejercicio 2:

•   Diseñe e implemente en DynamoDB una tabla Multi-tenancy de su
    preferencia e inserte 6 registros (2 por cada tenant_id).

•   Suba la evidencia en el padlet indicado por el docente incluyendo un json de
    ejemplo y la foto de los 6 registros insertados. Usted tendrá puntos de
    participación activa si lo completa.
                           1. Objetivo del taller 1
                           2. Ejercicio 1: Patrón 1 en DynamoDB (NoSQL)
                           3. Ejercicio 2: Ejercicio propuesto
Contenido                  4. Cierre
Base Datos No SQL Multi-
tenancy
Cierre:
Base Datos No SQL Multi-tenancy - Qué aprendimos?
• Diseño e implementación de Base de Datos NoSQL Multi-tenancy
  con Patrón 1
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
