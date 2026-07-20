---
curso: BD1
titulo: Clase 7 Actualizaciones, Restricciones
slides: 54
fuente: Clase 7 Actualizaciones, Restricciones.pdf
---

      CLASE 7:
 ACTUALIZACIONES,
RESTRICCIONES (SQL)

CS2041- Base de Datos I
        Ciclo 2024 - 1




            Teófilo Chambilla - tchambilla@utec.edu.pe
               Brenner Ojeda - bojeda@utec.edu.pe
      CS2041 Base de Datos I
      Teófilo Chambilla Aquino




Índice:
•   Introducción
•   Gestionar y crear tablas
•   Esquema
•   Privilegios
•   Actualizar tablas
•   Restricciones
•   Definir dominios y tipos
CS2041
BASE DE DATOS I
CICLO 2024-1




                                                                SQL II

                                   Algebra Relacional &                  Formas Normales
Introducción Modelo Relacional      Cálculo Relacional    SQL


              Entidad - Relación
Resumen: Clase 6

   STRUCTURED QUERY LANGUAGE (SQL)
 Agregación: GROUP BY y HAVING

 SELECT A,               T1xT2
 FROM T1,T2              A    A2   A3   B    B2   B3

 WHERE C1                a    .    .    b    .    .
                         a1   .    .    b1   .    .
 GROUP BY A,             a2   .    .    b2   .    .
                         a3   .    .    b3   .    .
 HAVING SUM(c) =n;

     A    A2   A3
T1                       A    A2   A3   B    B2   B3
     a    .    .
     a1   .    .         a    .    .    b    .    .
     a2   .    .         a    .    .    b1   .    .
     a3   .    .         a    .    .    b2   .    .
                         a    .    .    b3   .    .

T2   B    B2   B3
                         a1   .    .    b    .    .
     b    .    .         a1   .    .    b1   .    .
     b1   .    .         a1   .    .    b2   .    .
     b2   .    .         a1   .    .    b3   .    .
     b3   .    .
Las preguntas de hoy




           ¿Pero cómo se puede crear y actualizar las tablas?

      ¿Y cómo se puede saber si es un buen diseño relacional o no?

                                                                     …
SQL: GESTIONAR Y CREAR TABLAS

                        Capítulo 3.1.1 | Ramakrishnan / Gehrke
SQL: Base de datos




                     ...
SQL: Base de datos

        CREATE DATABASE name
            [ [ WITH ] [ OWNER [=] user_name ]
                   [ TEMPLATE [=] template ]
                   [ ENCODING [=] encoding ]
                   ...
                   [ CONNECTION LIMIT [=] connlimit ] ]




                       https://www.postgresql.org/docs/9.0/sql-createdatabase.html
SQL: Esquema




                         ¿Para que sirven los esquemas?

          Podemos configurar agrupaciones de tablas usando esquemas …
SQL: Privilegios de Esquema
SQL: Crear tablas
SQL: Borrar tablas




                     ¿Hay que poner el esquema cada vez?
                                                           …
SQL: Camino de esquema


SET search_path = my_schema, "$user", public; -- For current session only

ALTER ROLE your_role SET search_path = my_schema, "$user", public; -- Persistent, for
role




                                        Seleccionará el primer esquema en el camino.
                                    P. ej., si hay SistemaSolar.Aterrizaje y public.Aterrizaje,
                                                     leerá de la primera tabla
SQL: ACTUALIZAR TABLAS

                         Capítulo 3.1.1 | Ramakrishnan / Gehrke
SQL: Insertar tuplas
SQL: Insertar tuplas
SQL: Insertar tuplas
SQL: Insertar tuplas
SQL: Insertar tuplas

SQL: Insertar tuplas
SQL: Editar tuplas
SQL: Borrar tuplas
SQL: Borrar columnas
SQL: Crear columnas
     SQL: Modificar columnas




PSQL: ALTER TABLE AterrizajeEEUU ALTER COLUMN despegue TYPE VARCHAR(255)
Postgres: Cargar datos




                                 Especifico de Postgres
     ¿Algún problema aquí?
                             …   Concatena los datos
(Integrity Constraints)

SQL: RESTRICCIONES

                          Capítulo 5.7 | Ramakrishnan / Gehrke
Abre una cuenta




                  Banco de ABC
SQL: Esquema




    CREATE SCHEMA SistemaBancario;
Y (por supuesto) hay una base de datos
Modelo Relacional: Restricciones


Restricciones (de integridad):
  son restricciones formales
     que imponemos a un esquema
        que todas sus instancias
           deben satisfacer
Restricciones básicas: llaves, nulos, domino
Restricciones básicas: valores por defecto
Restricciones de unicidad




                La llave primaria implica una restricción de
                unicidad. La unicidad representa una llave
                 candidata: se pueden tener varias llaves
                 candidatas pero una sola llave primaria.
Nombrar (y borrar) restricciones




                           Más fácil cambiar restricciones
                                   posteriormente.
                      Si hay una violación, el mensaje de error
                        será más intuitiva si las restricciones
                              tienen nombres intuitivos.
Restricciones de llaves foráneas




                       Cada cuenta en Ingreso tiene que
                          estar en Cuenta.número.
Restricciones de llaves compuestas
Restricciones sobre varias columnas
Restricciones sobre varias tablas

Restricciones sobre varias tablas (!)




                                 ¿Algún problema aquí? …
                            ¿Por qué la ponemos en Ingreso cuando
                               involucra Gasto igualmente? Por
                             ejemplo, si agregáramos la milésima
                             tupla (con la misma cuenta y fecha) a
                             Gasto, ¡no tendríamos una violación!
                                     ¿Alguna solución?
                            Duplicar la restricción en Gasto o …
Asertos: Restricciones independientes




                          Rechazará alguna operación en el
                          esquema que violaría la restricción

                          La restricción no depende de ni una
                                     tabla ni la otra.

                                … pero puede ser más
                                costosa/compleja así.
¡Garantizar integridad con restricciones!
Postgres no permite consultas anidadas en CHECK
                   ni asertos

                 (son caros!)
DEFINIR DOMINIOS Y TIPOS
Crear dominios: VARCHAR
Crear dominios: INTEGER
Dominios: compatibles con el tipo base




                Se puede comparar valores del domino con
                  otros valores como fuera del tipo base
Tipos: son distintos a otros tipos




                   No se pueden comparar valores del nuevo
                 tipo con valores de otros tipos (solo entre sí).
Tipos: son distintos a otros tipos




                  No se pueden usar funciones del tipo base
                         con valores del nuevo tipo.
     Tipos son estándares (en SQL)

Pero Postgres solo suporte tipos compuestos ...
Tipos: un tipo compuesto
Tipos: un tipo compuesto
Preguntas?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
