---
curso: BD1
titulo: Clase 3_ Modelo Relacional
slides: 86
fuente: Clase 3_ Modelo Relacional.pdf
---

        CLASE 3: MODELO
          RELACIONAL
      CS2041- Bases de Datos I

                                   Ciclo 2024-1




                Brenner Ojeda - bojeda@utec.edu.pe
             Teófilo Chambilla - tchambilla@utec.edu.pe

En colaboración Aidan Hogan de la Universidad de Chile (https://aidanhogan.com/)
Base de Datos I
Ciclo 2024-1




                                 Modelo Relacional

Introducción Modelo Relacional    Algebra Relacional


            Entidad - Relación
CS2041 Bases de Datos I              Teófilo Chambilla Aquino




         Índice


         •    Resumen clase 2.
         •    Transformación de ER
         •    Modelo Relacional
         •    Ejemplos
Resumen: Clase ...2

            Entidad Relación
Resumen clase anterior
Conceptos



• Entidades:

• Atributos de entidades:

• Relaciones entre entidades:
Otros tipos de atributos:
¿PARA QUÉ NECESITAMOS E–R?
¿Para qué necesitamos E–R?
• Modelar los requerimientos de una aplicación
  – En una forma menos técnica que usar tablas

• Evitar redundancia / lograr un modelo conciso

• Documentar restricciones conceptuales

• Evitar problemas (p.ej. con llaves)
Modelo Relacional



Formalizado por
   Edgar F. Codd (IBM)
       en 1969
Modelo Relacional: Conceptos
          Cervezas
          nombre            tipo        grados   ciudad-Origen

          Abraxas           Ale Ultra   7,0      Lima
          Pilsen Trujillo   Lager       4,6      Trujillo
          Pilsen Callao     Lager       4,8      Lima
          Cristal           Lager       4,8      Lima
          Cusqueña Dorada   Lager       4,8      Cusco
          Backus Ice        Lager       4,25     Lima
          Arequipeña        Pilsener    4,6      Arequipa
          San juan          Pilsener    4,6      Pucallpa

• Relación: A cada tabla, la llamamos una relación
   – En este caso: Cervezas
• Atributo: A cada columna, la llamamos un atributo
   – En este caso: nombre, tipo, grados, ciudad-origen
• Tupla: A cada fila, la llamamos una tupla
   – En este caso, p.ej.,
Modelo Relacional: Esquema
       Cervezas
       nombre            tipo        grados   ciudad-Origen

       Abraxas           Ale Ultra   7,0      Lima
       Pilsen Trujillo   Lager       4,6      Trujillo
       Pilsen Callao     Lager       4,8      Lima
       Cristal           Lager       4,8      Lima
       Cusqueña Dorada   Lager       4,8      Cusco
       Backus Ice        Lager       4,25     Lima
       Arequipeña        Pilsener    4,6      Arequipa
       San juan          Pilsener    4,6      Pucallpa


• Para denominar una relación con sus atributos …

• Un esquema es un conjunto de relaciones:
Modelo Relacional: Esquema




         ¿La repetición de los nombres de atributos
                     … es un problema?

   No, pero si fuera, podríamos desambiguar (implícitamente) cada
               atributo usando el nombre de la relación:
Modelo Relacional: Dominio
       Cervezas
       nombre            tipo        grados   ciudad-Origen

       Abraxas           Ale Ultra   7,0      Lima
       Pilsen Trujillo   Lager       4,6      Trujillo
       Pilsen Callao     Lager       4,8      Lima
       Cristal           Lager       4,8      Lima
       Cusqueña Dorada   Lager       4,8      Cusco
       Backus Ice        Lager       4,25     Lima
       Arequipeña        Pilsener    4,6      Arequipa
       San juan          Pilsener    4,6      Pucallpa


• Asumimos que cada atributo tiene un dominio:
    Modelo Relacional: Instancia
     • Una instancia de un esquema es un conjunto
       de tuplas para cada relación de ese esquema




Cervezas
nombre            tipo        grados ciudad-Origen
Abraxas           Ale Ultra    7,0   Lima
Pilsen Trujillo   Lager        4,6   Trujillo
Pilsen Callao     Lager        4,8   Lima
Cristal           Lager        4,8   Lima
Arequipeña        Pilsener     4,6   Arequipa
San juan          Pilsener     4,6   Pucallpa
    Modelo Relacional: Instancia




Cervezas
nombre            tipo       grados ciudad-Origen
Abraxas           Ale Ultra 7,0     Lima
Pilsen Trujillo   Lager       4,6   Trujillo
Pilsen Callao     Lager       4,8   Lima
Cristal           Lager       4,8   Lima
Arequipeña        Pilsener    4,6   Arequipa
San juan          Pilsener    4,6   Pucallpa

                                                    el conjunto puede ser vacío
Modelo Relacional: Instancia
• Una instancia de un esquema es un conjunto
  de tuplas para cada relación de ese esquema


  ¿Cuáles son las consecuencias de esta definición?


          1. No hay orden en las filas
       2. No se puede tener filas duplicadas



                                       (SQL hace algo diferente)
Modelo Relacional: Instancia



      Cervezas
      nombre            tipo        grados   ciudad-Origen

      Abraxas           Ale Ultra   7,0      Lima
      Pilsen Trujillo   Lager       4,6      Trujillo
      Cusqueña Dorada   Lager       4,8      Cusco
      Backus Ice        Lager       4,25     Lima
      Arequipeña        Pilsener    4,6      Arequipa
      San juan          Pilsener    4,6      Pucallpa
Modelo Relacional: Restricciones


Restricciones (de integridad):
  son restricciones formales
     que imponemos a un esquema
        que todas sus instancias
           deben satisfacer

Modelo Relacional: Restricciones (Llaves)
Modelo Relacional: Restricciones (Llaves)


Un conjunto de atributos de una relación
  forma una súper llave
    si no permitimos que existan
      dos (o más) tuplas para esa relación
     con los mismos valores
       en todos los atributos de la llave
Modelo Relacional: Restricciones (Llaves)
      Cervezas
      nombre            tipo        grados   ciudad-Origen

      Abraxas           Ale Ultra   7,0      Lima
      Pilsen Trujillo   Lager       4,6      Trujillo
      Pilsen Callao     Lager       4,8      Lima
      Cristal           Lager       4,8      Lima
      Cusqueña Dorada   Lager       4,8      Cusco
      Backus Ice        Lager       4,25     Lima
      Arequipeña        Pilsener    4,6      Arequipa
      San juan          Pilsener    4,6      Pucallpa



                    ¿Una súper llave?
Modelo Relacional: Restricciones (Llaves)
      Cervezas
      nombre            tipo        grados   ciudad-Origen

      Abraxas           Ale Ultra   7,0      Lima
      Pilsen Trujillo   Lager       4,6      Trujillo
      Pilsen Callao     Lager       4,8      Lima
      Cristal           Lager       4,8      Lima
      Cusqueña Dorada   Lager       4,8      Cusco
      Backus Ice        Lager       4,25     Lima
      Arequipeña        Pilsener    4,6      Arequipa
      San juan          Pilsener    4,6      Pucallpa




                  ¿Entonces la siguiente es
                      una súper llave?

                                    Sí.
Modelo Relacional: Restricciones (Llaves)
      Cervezas
      nombre            tipo grados       ciudad-Origen

      Abraxas           Ale Ultra   7,0 Lima
      Pilsen Trujillo   Lager       4,6 Trujillo
      Pilsen Callao     Lager       4,8 Lima
      Cristal           Lager       4,8 Lima
      Cusqueña Dorada   Lager       4,8 Cusco
      Backus Ice        Lager       4,25 Lima
      Arequipeña        Pilsener    4,6 Arequipa
      San juan          Pilsener    4,6 Pucallpa




                 ¿Ok, entonces la siguiente es
                       una súper llave?

                                    No.
Modelo Relacional: Restricciones (Llaves)


Un conjunto de atributos de una relación
  forma una llave candidata
    si es una súper llave
      y no hay un subconjunto propio de esos atributos
      que es una súper llave
Modelo Relacional: Restricciones (Llaves)
      Cervezas
      nombre            tipo grados     ciudad-Origen

      Abraxas           Ale Ultra   7,0 Lima
      Pilsen Trujillo   Lager       4,6 Trujillo
      Pilsen Callao     Lager       4,8 Lima
      Cristal           Lager       4,8 Lima
      Cusqueña Dorada   Lager       4,8 Cusco
      Backus Ice        Lager       4,25 Lima
      Arequipeña        Pilsener    4,6 Arequipa
      San juan          Pilsener    4,6 Pucallpa




               ¿Cuál es la llave candidata
                  más natural aquí?
Modelo Relacional: Restricciones (Llaves)
      Cervezas
      nombre            tipo grados     ciudad-Origen

      Abraxas           Ale Ultra   7,0 Lima
      Pilsen Trujillo   Lager       4,6 Trujillo
      Pilsen Callao     Lager       4,8 Lima
      Cristal           Lager       4,8 Lima
      Cusqueña Dorada   Lager       4,8 Cusco
      Backus Ice        Lager       4,25 Lima
      Arequipeña        Pilsener    4,6 Arequipa
      San juan          Pilsener    4,6 Pucallpa




                  ¿Entonces la siguiente es
                    una llave candidata?

               ¡No! Es una súper llave pero hay un
            subconjunto propio que es una súper llave.
               Entonces no es una llave candidata.
Modelo Relacional: Restricciones (Llaves)
      Cervezas
      nombre            tipo grados     ciudad-Origen

      Abraxas           Ale Ultra   7,0 Lima
      Pilsen Trujillo   Lager       4,6 Trujillo
      Pilsen Callao     Lager       4,8 Lima
      Cristal           Lager       4,8 Lima
      Cusqueña Dorada   Lager       4,8 Cusco
      Backus Ice        Lager       4,25 Lima
      Arequipeña        Pilsener    4,6 Arequipa
      San juan          Pilsener    4,6 Pucallpa




                ¿Hay otra llave candidata?
                            No.

               … no es una llave candidata.
Modelo Relacional: Restricciones (Llaves)




         ¿Cuál es la llave candidata aquí?




                               ¿Algún problema aquí?
Modelo Relacional: Restricciones (Llaves)




         ¿Cuál es la llave candidata aquí?

          La llave candidata podría ser también …

           ¡Una llave es una restricción definida,
          no una descripción de los datos actuales!
Modelo Relacional: Restricciones (Llaves)




         ¿Es una instancia del esquema?
                      No.
Modelo Relacional: Restricciones (Llaves)

   Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)



      ¿Intuitivamente, hay otra llave candidata?

                      Probablemente …
    Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)


                       … o puede ser …
   Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)
                (si no tenemos un tipo como Gengis Kan)
Modelo Relacional: Restricciones (Llaves)

• Una súper-llave identifica cada fila; p.ej.:
     Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)
     Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)


• Una llave candidata es una súper llave mínima; p.ej.:
     Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)
     Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)


• Se escogerá una de las llaves candidatas como llave primaria:
      Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)
UN PROBLEMA CON EL VINO
Modelo Relacional: Restricciones


      ¿Cuál es la llave primaria más natural?
                  (Hay que pensar en el futuro también)

          ¿                                               ?
      Cervezas
      nombre              tipo grados     ciudad-Origen

      Abraxas              Ale Ultra 7,0 Lima
      Pilsen Trujillo      Lager     4,6 Trujillo
      Pilsen Callao        Lager     4,8 Lima
      Cusqueña Dorada Lager          4,8 Cusco
      Backus Ice      Lager     4,25 Lima
      Arequipeña      Pilsener 4,6 Arequipa


               ¿Cómo podemos solucionar
                   este problema?
Modelo Relacional: Restricciones


      ¿Cuál es la llave primaria más natural?
             (Hay que pensar en el futuro también)

        ¿                                            ?



    ¿Cómo podemos solucionar este problema?


            ¿Cómo podemos solucionar
                este problema?
Solución 1:
   ¿Un nombre de vino más específico?



        Cervezas
        nombre             tipo grados    ciudad-Origen

        Abraxas            Ale Ultra 7,0 Lima
        Pilsen Trujillo    Lager     4,6 Trujillo
        ...        ... …   …
Solución 2:
   ¿Un atributo nuevo: id? (¿p.ej., el código de barras?)



            Cervezas
            id      nombre    tipo grados    ciudad-Origen

            CAuL00 Abraxas    Ale Ultra 7,0 Lima
            CAuY00 Trujillo   Lager     4,6 Trujillo
            ... ... ... …     …
  Solución 3:
     ¿Una tabla “En-Stock” para vino y cerveza?




Cervezas
nombre            tipo       grados           ciudad-Origen

Abraxas         Ale Ultra    7,0   Lima
Pilsen Trujillo Lager        4,6   Trujillo
...    ...     ...   ...

Cervezas-En-Stock

nombre            cantidad   precio-unitario

Pilsen Trujillo     600         2000

Solución 4:
   ¿Combinemos las tablas?


Cervezas
nombre         tipo         grados   ciudad-Origen   Cantidad   precio-unitario

Abraxas         Ale Ultra   7,0      Lima            600        2000
Pilsen Trujillo Lager       4,6      Trujillo        0          ?
...              ...        …        …
Solución 5:
   ¿Tomar todo el vino en stock?
DEL MODELO ENTIDAD–RELACIÓN:
  AL MODELO RELACIONAL

                       Capítulo 3.5 | Ramakrishnan / Gehrke
Modelo E–R: Entidad (con atributos y llaves)
→ Modelo Relacional: Tabla



                                  (Hay que agregar el
                                       dominio)
Modelo E–R: Entidad (con atributos y llaves)
→ Modelo Relacional: Tabla
                                           Las llaves de las
Modelo E–R: Relación (con atributos)   entidades juntas forman
                                       (Tenemos
                                        una súper que    elegirla
                                                   llave para
→ Modelo Relacional: Tabla                  el relación
                                              dominio)
                                           Las llaves de las
Modelo E–R: Relación (con atributos)   entidades juntas forman
                                       (Tenemos
                                        una súper que    elegirla
                                                   llave para
→ Modelo Relacional: Tabla                  el relación
                                              dominio)
Modelo E–R: Relación (con valor único)
→ Modelo Relacional: Tabla




                                     Con esta restricción no se
                                        (Tenemos que elegir
                                        necesita c-nombre
                                      para la el dominio)
                                              llave. p-nombre
                                    forma una llave candidata.
 Modelo E–R: Relación (llaves foráneas)
 → Modelo Relacional: Tabla


                               También una llave primaria


       Una llave foránea:                                          Una llave foránea:
Una llave primaria en otra tabla                            Una llave primaria en otra tabla
Modelo E–R: Relación (llaves foráneas)
→ Modelo Relacional: Tabla

                                    Llaves foráneas:
                                  Las escribiremos así
                             (a veces abreviadas como C.)
Modelo E–R: Relación (llaves foráneas)
→ Modelo Relacional: Tabla        ¿Algún problema aquí?
                                  La misma llave, pero ...
                               un producto no tiene que ser
                               fabricado por una compañía?
Modelo E–R: Relación (llaves foráneas)
→ Modelo Relacional: Tabla        ¿Algún problema aquí?
                                  La misma llave, pero ...
                               un producto no tiene que ser
                               fabricado por una compañía?




                                       Si intentáramos combinar las
                                            tablas, tendríamos un
                                                  problema
                                      con productos sin información
                                              de su fabricación
Modelo E–R: Relación (llaves foráneas)
→ Modelo Relacional: Tabla      ¿Hay algún caso que puede
                                        generar una tabla
                                          redundante?       …
Modelo E–R: Relación (con participación)
→ Modelo Relacional: Tabla            ¿Ahora?
Modelo E–R: Relación (con participación)
→ Modelo Relacional: Tabla




                               ¿Hay un problema con el
                                     diagrama?
                               ¿Hay un mejor diagrama?
Modelo E–R: Relación (con participación)
→ Modelo Relacional: Tabla




                                          ¿Hay un problema con el
                                                diagrama?
                                           ¿Hay un mejor diagrama?
                  ¡Sí! Pero no cambia la traducción: a veces, hay que
                 considerar la posibilidad de combinar algunas tablas.
    Modelo E–R: Relaciones Múltiples
    → Modelo Relacional: Tabla
Película(título:string, año:int,categoria:string)     Local de videos(id:int,direccion:string)




                                                    dni




                       Persona(dni:string,nombre:string)



     Arriendo(PI.titulo:string,PI.año:int,Pr.dni:string,L.id:int,fecha:date)
Modelo E–R: Relaciones Múltiples
→ Modelo Relacional: Tabla




                                              dni




Película(título:string, año:int,categoria:string)
Local de videos(id:int,direccion:string)
Persona(dni:string,nombre:string)
Arriendo(PI.titulo:string,PI.año:int,Pr.dni:string,L.id:int,fecha:date)
Modelo E–R: Relación (con papeles)
→ Modelo Relacional: Columnas distintas




                                                   dni




Película(título:string, año:int,categoria:string)
Local de videos(id:int,direccion:string)
Persona(dni:string,nombre:string)
Arriendo(PI.titulo:string,PI.año:int,Pr.dni-cli:string,Pr.dni-caj:string,L.id:int,fecha:date)
Modelo E–R: Jerarquías de clases

                                   dni




     ¿Qué vamos
     hacer aquí?

 Modelo E–R: Jerarquías de clases
 → Modelo Relacional:
  Opción 1: Tablas solo para las subclases
                                                                  dni




Empleado(dni:string, nombre:string,género:string,sueldo:string)
Cliente(dni:string, nombre:string,género:string,vip:boolean)
Modelo E–R: Jerarquías de clases
→ Modelo Relacional:
 Opción 2: Tabla para la superclase
                                                     dni




  Persona(dni:string, nombre:string,género:string)
  Empleado(P.dni:string,sueldo:int)
  Cliente(P.dni:string,vip:boolean)
 Modelo E–R: Jerarquías de clases
 → Modelo Relacional:
  Eligiendo una opción
Empleado(dni:string, nombre:string,género:string,sueldo:string)
Cliente(dni:string, nombre:string,género:string,vip:boolean)              1
                         ¿Cuál sea la mejor opción …

   Persona(dni:string, nombre:string,género:string)
   Empleado(P.dni:string,sueldo:int)
   Cliente(P.dni:string,vip:boolean)
                                                                          2
         … con mucho solapamiento entre Cliente y Empleado?

    Mucho solapamiento sugiere 2 (con menos o no solapamiento sugiere 1)
 (Si tuviéramos muchos Empleados que sean Clientes también, con 1, tendríamos
       que repetir los atributos generales de Personas dos veces en cada caso)
 Modelo E–R: Jerarquías de clases
 → Modelo Relacional:
  Eligiendo una opción
Empleado(dni:string, nombre:string,género:string,sueldo:string)
Cliente(dni:string, nombre:string,género:string,vip:boolean)               1
                         ¿Cuál sea la mejor opción …

   Persona(dni:string, nombre:string,género:string)
   Empleado(P.dni:string,sueldo:int)
   Cliente(P.dni:string,vip:boolean)
                                                                           2
    … sin cobertura … si hay Personas que no son Empleados ni Clientes?

                                 Hay que elegir 2
           (Si tuviéramos Personas que no sean ni Empleados ni Clientes,
                    no podríamos representarlas con la opción 1)
 Modelo E–R: Jerarquías de clases
 → Modelo Relacional:
  Eligiendo una opción
Empleado(dni:string, nombre:string,género:string,sueldo:string)
Cliente(dni:string, nombre:string,género:string,vip:boolean)                1
                         ¿Cuál sea la mejor opción …

   Persona(dni:string, nombre:string,género:string)
   Empleado(P.dni:string,sueldo:int)
   Cliente(P.dni:string,vip:boolean)
                                                                            2
 … con muchas consultas para el nombre de una Persona dado el DNI?

                                      Sugiere 2
 (Con muchas de estas consultas, y con 1, tendríamos que consultar a dos tablas,
            pero con 2, tendríamos que consultar a una sola tabla)
 Modelo E–R: Jerarquías de clases
 → Modelo Relacional:
  Eligiendo una opción
Empleado(dni:string, nombre:string,género:string,sueldo:string)
Cliente(dni:string, nombre:string,género:string,vip:boolean)          1
                         ¿Cuál sea la mejor opción …

   Persona(dni:string, nombre:string,género:string)
   Empleado(P.dni:string,sueldo:int)
   Cliente(P.dni:string,vip:boolean)
                                                                      2

                                  En general …
       Hay que considerar las tablas, los atributos, los datos, las
             restricciones, el control de acceso, etcétera,
                     y aplicar algo “prudente”. ☺
Modelo E–R: Jerarquías de clases
→ Modelo Relacional

        dni




        ¿Cuáles son las opciones en este caso? ☺
                                                   …
Modelo E–R: Jerarquías de clases
→ Modelo Relacional

              dni




Pregado(dni:string, nombre:string,género:string,año:int)
Postgrado(dni:string, nombre:string,género:string,año:int)

                    ¿Pero hay otra opción aquí? ☺
                                                             …
Modelo E–R: Jerarquías de clases
→ Modelo Relacional
              dni




                          Pregado(dni:string, nombre:string,género:string,año:int)
                          Postgrado(dni:string, nombre:string,género:string,año:int)




Alumno(dni:string, nombre:string,género:string,año:int)

Pregado(A.dni:string)
                                                             ¿Hay otra opción?
Postgrado(A.dni:string)
                                                                    ☺ …
Modelo E–R: Jerarquías de clases
→ Modelo Relacional:
 Una opción implícita: Quitar la jerarquía
        dni



                                   dni
Modelo E–R: Jerarquías de clases
→ Modelo Relacional:
 Una opción implícita: Quitar la jerarquía


                                                             dni




Alumno(dni:string, nombre:string,género:string,año:int,tipo:string)

 ¿Algún problema aquí?                   Tendremos mucha repetición
                                             en la columna tipo.
                                       (Pero es más sencillo, el sistema
                                        puede comprimirla, etcétera.)
Modelo E–R: Entidades débiles
→ Modelo Relacional: Cuidado con las llaves




                ¿Alguien quiere ”adivinar”? ☺




¿Algún problema aquí?        La tabla De(.,.) es redundante
                               … y es un nombre terrible para una tabla.
Modelo E–R: Entidades débiles
→ Modelo Relacional: No se necesita una tabla para la relación débil




                                        Entonces …



Observación: En el libro de R&G, se mencionan atributos sobre relaciones débiles (p.ej. Figura 3.14) y
  por eso, se necesita una tabla para la relación. No estoy de acuerdo con eso: atributos en tales
        relaciones siempre pueden ser asociados con la entidad débil dado su relación 1:n.
 Modelo E–R: Entidades débiles
 → Modelo Relacional




                                                         ¿Las relaciones?
                          dni


Curso(código:string, nombre:string)

Evaluación(nombre:string, C.código:string, fecha:date)

Nota(pregunta:int, E.nombre:string, C.código:string, A.dni:string valor:float)

Alumno(dni:string, nombre:string)
Modelo E–R: Agregación
→ Modelo Relacional:




                                  dni




                         ¿Alguien quiere ”adivinar”? ☺

Película(año:int, título:string)
Local-de-Video(id:int,dirección:string)
Stock(PI.año:int, PI.título:string, L.id:int, precio-por-noche:int)
Persona(dni:string, nombre:string)
Arriendo(PI.año:int, PI.título:string,L.id:int,Pr.dni:string, fecha:date)
Modelo E–R: Ejercicio→ Modelo Relacional:




            ¿Alguien quiere ”adivinar”? ☺
Modelo E–R: Ejercicio→ Modelo Relacional:




Oferta( código:int ,descuenta:float)
Tipo de Pizza(nombre:string,tamaño:int, vegentariano:int)
Local de Pizza(dirección:string ,teléfono:int)
Restaurante(dirección:string,capacidad:int)
Delivery (dirección:string,tarifa:float)
Vende(LdP.dirección:string ,TdP.nombre:string,TdP.tamaño:int,precio:float)
Rebaja(O.codigo,LdP.direccion,TdP.nombre,TdP.tamaño)
Modelo E–R: Ejercicio→ Modelo Relacional:




            ¿Alguien quiere ”adivinar”? ☺
Modelo E–R: Ejercicio→ Modelo Relacional:

Modelo E–R: Ejercicio→ Modelo Relacional:
Modelo E–R: Ejercicio→ Modelo Relacional:
Modelo E–R: Relación
→ Modelo Relacional: Tabla

• Aparte de jerarquías de clases la traducción es
  más o menos determinística



                ¿Qué piensan ustedes?
                       ¿Cuál es mejor …
 … diseñar tablas directamente o diseñar un modelo E-R antes?
LA PRÓXIMA VEZ, CONTINUAREMOS CON:
   EL ÁLGEBRA RELACIONAL

                                     Capítulo 4 | Ramakrishnan / Gehrke
¿Preguntas?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
