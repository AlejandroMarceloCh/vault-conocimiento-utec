---
curso: BD1
titulo: Clase 10 Seguridad.pptx
slides: 42
fuente: Clase 10 Seguridad.pptx.pdf
---

Seguridad en la base de
    datos y acceso
    programático

CS2041- Base de Datos I
         Ciclo 2024-1




       Teófilo Chambilla - tchambilla@utec.edu.pe
          Brenner Ojeda - bojeda@utec.edu.pe
    CS2041 Base de Datos I
    Teófilo Chambilla Aquino




Índice
• Error de Capa 8
• Acceso programático
• SQL Dinámico
• Store procedure
• Caso de uso
CS2041
BASES DE DATOS I
CICLO 2023-1




                                                                                               Seguridad


                                                                                             Transacciones y ACID
Introducción



                      Algebra Relacional &       SQL                       Planificación y                NO
Modelo Relacional
                       Cálculo Relacional                                                             SQL/GRAFOS

 Entidad - Relación                          Actualización, Dependencias   Optimización de
                                             Restricciones funcionales     Consultas
CS2041 - Base de datos I                                          Computer Science




   RESULTADOS DE APRENDIZAJE


    ❏      Podrá explicar la seguridad de la base de datos.
    ❏      Utilizar correctamente los script al momento de
           implementar en la aplicación
    ❏      Prevenir manipulación de datos por usuarios terceros
CS2041- Base de datos I                                              Computer Science


  Las preguntas de hoy




                          ¿Cómo aseguramos la manipulación segura?

                            Y ¿cómo evitar cambios no permitidos?

                                                                               …
CS2041- Base de datos I




   1                      ERROR CAPA 8

                                         Capítulo 6 | Ramakrishnan / Gehrke
https://larepublica.pe/politica/2022/06/05/empres
as-accedian-ilegalmente-a-informacion-de-la-osc
e-para-ganar-millonarios-contratos-del-estado/
CS2041- Base de datos I




   2                      ACCESO PROGRAMÁTICO (JAVA):
                          JAVA DATABASE CONNECTIVITY (JDBC)
                                           Capítulo 6 | Ramakrishnan / Gehrke
Java Database Connectivity (JDBC)




                          Externas
Veremos el ejemplo ApellidoApp.java
Consulta vs. Actualización
● Para hacer consultas (SELECT):




● Para hacer actualizaciones (INSERT; UPDATE,
  …)
Un problema …
System.out.println("Ingrese un apellido paterno:");           def get_clients():
                                                                  conn = None
String input = br.readLine().trim();                              try:
if(input.equals(KILL)) break;                                          conn = psycopg2.connect(database=‘x', user=‘x',
                                                              password=x')
// crear un statement en blanco                                        cur = conn.cursor()
st = conn.createStatement();                                           cur.execute('select * from clientes;')
                                                                      for row in cur.fetchall():
                                                                           print(row[0], row[1], row[2])
// crear la consulta                                                   cur.close()
String consulta = "SELECT * FROM estudiante "                          conn.close()
               + "WHERE apellido='"+ input +"’                    except (Exception, psycopg2.DatabaseError) as error:
                   + "ORDER BY nota DESC LIMIT 100";                  print(error)
                                                                  finally:
                                                                      if conn is not None:
// ejecutar una consulta
                                                                           conn.close()
ResultSet rs = st.executeQuery(consulta);




       ¿Hay algún problema aquí?                       … no hemos “verificado” el input.
Inyección SQL
● Un usuario malintencionado puede ingresar un
  string de entrada para hacer algo inesperado
Inyección SQL
● Un usuario malintencionado puede ingresar un
  string de entrada para hacer algo inesperado




¿Qué hace el ejemplo?   ¡Devolverá toda la tabla!
Parece estúpido pero …
Parece estúpido pero ...




              OWASP: Open Web Application Security Project
    https://sucuri.net/guides/owasp-top-10-security-vulnerabilities-2020/
Más ejemplos …
          https://en.wikipedia.org/wiki/SQL_injection

Más ejemplos …
          https://en.wikipedia.org/wiki/SQL_injection
  La historia de HBGary y Anonymous




● 2010/12/08: Anonymous empiezan un
  “DDoS” (denegación de servicio
  distribuido) contra MasterCard, Visa, etc.,
  por no aceptar donaciones a Wikileaks

● 2011/02/05: Aaron Barr (CEO de HBGary
  Federal, una empresa de ciberseguridad)
  dice al Financial Times que ha logrado
  obtener información sobre las identidades
  de miembros de Anonymous

● 2011/02/05-06: Anonymous usa
  inyecciones SQL para obtener todos los
  datos de usuarios de HBGary, incluyendo
  hashes de contraseñas, con los cuales (y
  una tabla arcoíris) pueden hackear las
  cuentas sociales de Aaron Barr …
La historia de HBGary y Anonymous
Inyección SQL




         ¿Cómo podemos resolver el problema?
Inyección SQL: ¿escapar los strings?




                       ¿Cómo podemos resolver el problema?




   Mejor, pero sería complicado implementar la función escapar en un lenguaje de
programación general y garantizar que prevente cada tipo de inyección en cada versión
      (futura) de cada sistema de BdD dado cualquier tipo de consulta y entrada!
CS2041- Base de datos I




   3                      SQL DINÁMICO

                                         Capítulo 6 | Ramakrishnan / Gehrke
Inyección SQL: ¡sentencias pre-compiladas!




 Mandamos la consulta al sistema de bases de datos y después se reemplazarán los
                     parámetros con la entrada del usuario
Inyección SQL: ¡sentencias pre-compiladas!




                                                      El sistema de base de datos


       La consulta es compilada por el sistema sin la entrada
Inyección SQL: ¡sentencias pre-compiladas!




                                                      El sistema de base de datos

       Se reemplaza el parámetro en la sentencia pre-compilada
              (que es un plan en memoria, no un string)
Inyección SQL: ¡sentencias pre-compiladas!




                              El sistema de base de datos
Sentencias pre-compiladas




        Se puede reutilizar el PreparedStatement varias veces
    (es más eficiente también: se compila la sentencia sólo una vez)


          Se puede tener varios parámetros con varios tipos
CS2041- Base de datos I




   4                      PROCEDIMIENTO ALMACENADO

                                          Capítulo 6 | Ramakrishnan / Gehrke
CS2041- Base de datos I




   5                      RESPALDOS
Tipos de respaldo
Respaldos EXTERNOS
Respaldos EXTERNOS

             ●   Usar métodos estándares de respaldar archivos

                 ✓Algo simple

                  ○   Solo hay protección ante errores de hardware
                      si se usa otro disco para respaldar la
                      información
                  ○   × En sí, no provee protección ante errores
                      humanos o de software (solo respaldará el
                      estado actual)
                  ○   × En general, habría que detener el sistema
                      de base de datos para hacer un respaldo
                      “coherente”
                  ○   × No podemos consultar los respaldos
Respaldos EXTERNOS

             ●   Replicar el disco (p.ej., RAID-1) o la máquina

                  ○   ✓Protección ante errores de hardware
                  ○   ✓Podemos consultar el respaldo (más
                      lecturas)
                  ○   ✓No es necesario desactivar el sistema de
                      base de datos
                  ○   × Mantener la réplica actualizada puede tener
                      un costo (en particular en el caso de usar otra
                      máquina)
                  ○   × En sí, no provee protección ante errores
                      humanos o de software (solo respaldará el
                      estado actual)
                  ○   × Existe el costo de comprar y mantener el
                      hardware adicional
Respaldos Internos - Completos

                ●   Respaldar todos los datos dentro del sistema de
                    base de datos cada vez (por ejemplo, cada
                    noche)

                         ✓No hay que parar el sistema de base de
                         datos
                         ✓Más fácil de cargar de nuevo
                         × Mantener una historia de copias completas
                         puede ocupar mucho espacio
                         × No podemos consultar los respaldos
Preguntas?

                                                               Computer Science
CS2041 Base de datos I




        Resumen
        ➔ Es importante el uso correctos de los scripts SQL
        ➔ El uso de buenas prácticas es fundamental al
          momento de implementar las aplicaciones
        ➔ Velar la integridad de datos es crucial y es
          responsabilidad del DBA y el Oficial de Seguridad.
        ➔ Siempre usar store procedure o consultas
          precompiladas
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
