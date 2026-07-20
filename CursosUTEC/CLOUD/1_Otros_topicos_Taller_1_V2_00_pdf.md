---
curso: CLOUD
titulo: 1. Otros tópicos - Taller 1 - V2.00
slides: 20
fuente: 1. Otros tópicos - Taller 1 - V2.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Otros tópicos
Semana 13 - Taller 1: Enfoque aplicaciones serverless

                       ELABORADO POR: GERALDO COLCHADO
                                Con apoyo de Asistentes de Cátedra y Laboratorio:
                                • Ana Accilio (ana.accilio@utec.edu.pe)
                                • Sofía García (sofia.garcia@utec.edu.pe)
                       1. Objetivo del taller 1
                       2. Conocimientos Previos
                       3. Ejercicio 1: Sistema de Seguridad
Contenido              4. Ejercicio 2: Ejercicio Propuesto
Enfoque aplicaciones   5. Cierre
serverless
Enfoque aplicaciones serverless
Objetivo del Taller 1
• Implementar un Sistema de Seguridad Serverless para proteger el
  acceso a las apis
                       1. Objetivo del taller 1
                       2. Conocimientos Previos
                       3. Ejercicio 1: Sistema de Seguridad
Contenido              4. Ejercicio 2: Ejercicio Propuesto
Enfoque aplicaciones   5. Cierre
serverless
           AWS Well-Architected
           Enfoque: Aplicaciones Serverless - Escenarios




Fuente: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html
                       1. Objetivo del taller 1
                       2. Conocimientos Previos
                       3. Ejercicio 1: Sistema de Seguridad
Contenido              4. Ejercicio 2: Ejercicio Propuesto
Enfoque aplicaciones   5. Cierre
serverless
         Enfoque aplicaciones serverless
         Ejercicio 1: Sistema de Seguridad


Implementar este
Sistema de Seguridad
para proteger la
ejecución de apis con
un token con
expiración
       Enfoque aplicaciones serverless
       Ejercicio 1: Sistema de Seguridad
Paso 1: Crear tablas en DynamoDB: t_usuarios, t_tokens_acceso, t_productos
       Enfoque aplicaciones serverless
       Ejercicio 1: Sistema de Seguridad
Paso 2: Crear lambdas: CrearUsuario, LoginUsuario, ValidarTokenAcceso, CrearProducto
       Enfoque aplicaciones serverless
       Ejercicio 1: Sistema de Seguridad
Paso 3: Crear Api Gateway usuarios
       Enfoque aplicaciones serverless
       Ejercicio 1: Sistema de Seguridad
Paso 4: Probar api usuarios: Crear un usuario

                                                t_usuarios
       Enfoque aplicaciones serverless
       Ejercicio 1: Sistema de Seguridad
Paso 5: Probar api usuarios: Login usuario


                                             t_tokens_acceso
      Enfoque aplicaciones serverless
      Ejercicio 1: Sistema de Seguridad
Paso 6: Crear Api Gateway productos
       Enfoque aplicaciones serverless
       Ejercicio 1: Sistema de Seguridad
Paso 7: Probar api productos: Crear Producto
       Enfoque aplicaciones serverless
       Ejercicio 1: Sistema de Seguridad
Paso 7: Probar api productos: Crear Producto


                                               t_tokens_acceso




                                                    t_productos
                       1. Objetivo del taller 1
                       2. Conocimientos Previos
                       3. Ejercicio 1: Sistema de Seguridad
Contenido              4. Ejercicio 2: Ejercicio Propuesto
Enfoque aplicaciones   5. Cierre
serverless
Enfoque aplicaciones serverless
Ejercicio 2: Ejercicio propuesto
• Completar el api productos (protegida) con los lambdas siguientes y
  enviando un token para poder ejecutarlos:
   •   ListarProductos (POST) - Enviar tenant_id
   •   BuscarProducto (POST) - Enviar tenant_id y producto_id
   •   ModificarProducto (PUT)
   •   EliminarProducto (DELETE)
                       1. Objetivo del taller 1
                       2. Conocimientos Previos
                       3. Ejercicio 1: Sistema de Seguridad
Contenido              4. Ejercicio 2: Ejercicio Propuesto
Enfoque aplicaciones   5. Cierre
serverless
Cierre:
Enfoque aplicaciones serverless - Qué aprendimos?
• Proteger el acceso a las apis
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
