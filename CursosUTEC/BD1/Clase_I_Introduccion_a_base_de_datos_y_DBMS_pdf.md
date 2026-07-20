---
curso: BD1
titulo: Clase I - Introducción a base de datos y DBMS
slides: 94
fuente: Clase I - Introducción a base de datos y DBMS.pdf
---

                 CLASE 1: INTRODUCCIÓN

                   CS2041- Bases de Datos I

                                               Ciclo 2024-1



                                                Brenner Ojeda bojeda@utec.edu.pe
                                             Teófilo Chambilla - tchambilla@utec.edu.pe

Server Discord
                 En colaboración Aidan Hogan de la Universidad de Chile (https://aidanhogan.com/)
                                                   Agenda

                                                                                    4               ¿Por      qué   se


                                                   1.
                                                                                                    necesitan sistemas
                                                               Metodología    del
                                                                                                    de       “bases de

                                                                                     .
                                                               curso
                                                                                                    datos”?




                                                  2.                                5.
                                                                                                    ¿Una base de datos
                                                               ¿Por qué necesitan
                                                                                                    siempre      modela
                                                               este curso?
                                                                                                    datos como tablas?




                                                  3.                                6.
                                                                                                    ¿Qué    vamos    a
                                                               ¿Qué es una “base
                                                                                                    aprender?
                                                               de datos”?




                                             Teófilo Chambilla - tchambilla@utec.edu.pe
                                               Brenner Ojeda bojeda@utec.edu.pe

Server Discord
                 En colaboración Aidan Hogan de la Universidad de Chile (https://aidanhogan.com/)
1.
     Acerca del curso
     CS2041-Base de datos I
CS2041 Bases de Datos I                                                  Computer Science




    Los resultados del aprendizaje


    ❏ Aplicar conceptos de álgebra relacional y teoría de grafos para
      generar y optimizar las consultas SQL en la recuperación de
      información.

    ❏ Demostrar la optimización de consultas, indexación y transacción
      en las bases de datos mediante motores de bases de datos de
      código abierto (PostgreSQL, MongoDB, Casandra).

    ❏ Construir Base de Datos a través de modelos como
      Entidad-Relación, Modelo Relacional, optimización, transacciones
      y recuperación de la información.

    ❏ Utilizar algoritmos de optimización de consultas SQL, como
      Hash-Join, Nested-Loop, Merge-Join, mediante índices Hash y
      Árboles B+.
2.
 Metodología del
 curso
Se dicta en:




             +                 +


   2 horas         2 horas           2 horas
  teoría
                 Laboratorio       Laboratorio
“Semi-flipped classroom”
• Una cátedra
“Semi-flipped classroom”
• Dos sesiones laboratorio
  – Ejercicios escritos o laboratorios con
    computadoras
Sesiones prácticas
❏   Sesiones prácticas
    – Nuestro primer laboratorio
        • Tendremos una clase con archivos de texto plano y otros


❏   En algunos Lab. trabajarán en grupos de tres o
    cuatro
    – ¡Sólo se puede trabajar en grupo en el lab!
        • Si no asistes físicamente al lab, hay que trabajar sólo


❏   A veces, necesitaremos computador
    – Tendremos computadores en el laboratorio
      507/603/301
    – Se pueden usar notebooks personales también
Material
❏   Subiremos todas las diapositivas
    antes de cada cátedra:
    – Canvas

❏   Las diapositivas servirán como
    el material canónico del curso
    – Pero si quieren leer más, se
      recomienda:
       • “Database Management Systems”
          – Ramakrishnan / Gehrke, Third Edition
Política sobre Tareas y Copias
Las tareas son individuales. Toda entrega debe ser enteramente fruto de su trabajo
y no puede ser derivada del trabajo de otros, ya sea de fuentes publicadas como no
publicadas, la web, otro estudiante, libros, materia de otros cursos (incluyendo
semestres anteriores de este curso), o cualquier otra persona o programa. Se
prohíbe copiar, examinar, o alterar la tarea de otra persona, o usar un programa para
transcribir, modificar o copiar los archivos de otro alumno.

Para facilitar el aprendizaje cooperativo, está autorizado conversar de una tarea con
otros estudiantes, siempre y cuando se respete la siguiente política de “pizarra”: Una
conversación puede tener lugar en una pizarra (o sobre papel, etc.), y debe cumplir
las siguientes reglas:

    ●   Nadie tiene permiso de tomar notas, grabar la conversación, copiar o
        fotografiar lo que esté escrito en la pizarra. La pizarra debe borrarse
        después de la discusión.
    ●   Se debe respetar un lapso de cuatro horas después de cualquier
        conversación antes de empezar a trabajar en la tarea.

El hecho de que pueda recrear la solución de memoria se considera como prueba de
que se entendió efectivamente.

Toda violación podrá ser reportada a las autoridades correspondiente, solicitando un
sumario.
Si todo sale bien….




El profesor pone la pizza
Sistema de Evaluación:
     El promedio final del curso se calcula a través de la siguiente fórmula:




                           TEORÍA (T)                    LABORATORIO (L)

  EVALUACIÓN
                     Práctica Calificada PC1 (12%)    Evaluación Continua C1 ( 7% )
 *La ponderación     Práctica Calificada PC2 (14%)    Evaluación Continua C2 ( 8% )
 de la evaluación    Práctica Calificada PC3 (14%)             Proyecto P1 ( 10% )
 se hará si ambas                Examen E1 (20%)               Proyecto P2 ( 15% )
 partes están
 aprobadas
                               60%                               40%
                                               100%
Práctica Calificada (Tentativa)




Práctica Calificada 1       Práctica Calificada 2         Práctica Calificada 3



                        5                           9                             13
                                                                                       Semana

                   12%                              14%                       14%
Proyecto del Curso



                         Hito 2: 15%
       Hito 1: 10%


   1                 7                      15


                                       Semana
Evaluación Continua
                                          • Tareas
                                          • Ejercicios
                                          • Laboratorio

           Desempeño en clase 15%



       7                                                  15


                                                     Semana



-   No está permitido subir archivos
    ZIP, no se revisará y es como si no
    hubiese entregado su nota es 0.
3.
 ¿Por qué necesitan
 este curso?
Un día cualquiera:
Un día cualquiera: 09:00
Despierto




                           (Bostezo.)
Un día cualquiera: 09:35
Reviso el avance del COVID-19




   Fuente: https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6

Un día cualquiera: 09:40
Reviso el correo




                           Nada urgente, ¡uf!
Un día cualquiera: 09:50
Café: pago con tarjeta




                           Es debito.
Un día cualquiera: 10:15
Me meto al banco (¿me pagaron?)




                             Sí. Me pagaron.
Un día cualquiera: 10:20
Reviso canvas (¿alguna tarea ?)




                                  No, salvo ...
Un día cualquiera: 10:30
IMDb (The Leftovers … ¿es bueno?)




                                    Sí.
Un día cualquiera: 10:35
Amazon (The Leftovers … ¿cuánto cuesta?)




                                 Demasiado.
Un día cualquiera: 10:36
ThePirateBay (me pagaron pero …)




                 Listo. Pero tengo hambre …
Un día cualquiera: 10:52
Al supermercado (¿cuánto cuesta?)




                                    Luca.
Un día cualquiera: 10:55
Al supermercado (esperando en la fila …)




                                   ¿Cero likes?
Un día cualquiera: 10:57
Al supermercado (uso mi tarjeta OH!)




                        ¿Acumulas puntos? Sí.
Un día cualquiera: 11:00
Desayuno




                           …
Un día cualquiera: antes de las 11:00
¿Estas actividades tienen algo en común?
Bases de datos:
Interactuamos con bases de datos
   todo el tiempo, todos los días

• Especialmente con la Web:
  – Búsqueda (Google, Bing, Yahoo!, …)
  – Tiendas (Amazon, eBay, …)
  – Redes sociales (Facebook, Twitter, …)
  – Enciclopedias (Wikipedia, IMDb, …)
  – Bancos
  – Aerolíneas
  – Canvas/EDU
  …
Un buen mercado laboral
“Data Scientist”:
  Ofertas de Trabajo




  http://visit.crowdflower.com/rs/416-ZBE-142/images/CrowdFlower_DataScienceReport_2016.pdf
¿Cúal es la tendencia?
En 2020, cada persona generó 1,7 megabytes de datos en solo un segundo
4.
 ¿Qué es una “base de
 datos”?
¿Una base de datos?




             Un ejemplo de una
              base de datos?

¿Una base de datos?
¿Una base de datos?
¿Una base de datos?
¿Una base de datos?
¿Una base de datos?
¿QUÉ ES UNA “BASE DE DATOS”?


                           DEPENDE ...
Aquí, una base de datos es:


• Una colección de datos
  (típicamente datos estructurados)
  (típicamente datos electrónicos)
   organizada en alguna forma
    para facilitar hacer consultas
     de una forma eficiente
¿Una base de datos?




  (hablando de los datos, no la aplicación …)   Aquí, sí!
¿Una base de datos?




    (es un sistema de base de datos entonces …)   Aquí,
                                                   no!
Un sistema de bases de datos es:
• Un sistema (de software) general
  para manejar
   bases de datos …
• Facilitan (en una forma general):
      • representar datos,
      • cargar datos,
      • organizar datos,
      • definir datos,
      • actualizar datos,
      • consultar datos,
      •…
• DBMS: (DataBase Management System)
Un sistema general implica que podamos
resolver un problema general …
¿Una base de datos?




 (es una aplicación de base de datos entonces …)   Aquí,
                                                    no!
  ¿Una base de datos?




(es una aplicación de base de datos entonces …)   Aquí, no!
¿Una base de datos?




                      ???
CS2041 Bases de Datos I                           Teófilo Chambilla Aquino




                          ¿POR QUÉ SE NECESITAN
                          SISTEMAS DE “BASES DE
                          DATOS”?
Sé programar en C++, sé programar en Python,
   … ¡puedo programar algo sin problema!
Intentemos implementar una aplicación sin un
   sistema de bases de datos (p.ej., en C++)
  Tenemos información de profesores, auxiliares,
    alumnos y notas parciales en cada curso
                                     profesores.csv
        Dni               Nombre                 Curso
       …
      40142153    Ernesto Cuadros Vargas         CS1100
      42440124    Teóﬁlo Chambilla Aquino        CS2701
      45142154    Heider Sanchez Enriquez        CS1102
      45142154    Maria Hilda Bermejo Rios       CS2701
       ...
                                                                                                   auxiliares.csv
                                                                Código             Nombre              Curso
                                 alumnos.csv                   …
  Código          Nombre                Curso                 201710001      Peña Mendoza Alejandro    CS1100
 ...                                                          201710033      Quesada Velarde Luis      CS2701
201710042   Molina Orellana Diego       CS1100                201710066      Quispe Roldan Enrique     CS1102
201710043   Paredes Sanchez Bruno       CS2701                201710077      Peña Cordova Diana        CS2701
201710044   Perez Fu Luis Adrian        CS1102                 ...
201710044   Perez Fu Luis Adrian        CS2701
 ...


                                                                                                          notas.csv
                                                 cursos.csv        Código       Nombre      Eval         Nota
                 Código       Nombre                              …
                  …                                              201710043      CS2701      Lab 1        17
                 CS2701    Base de datos I                       201710043      CS2701      Lab 2        18
                 CS1102    Programación Orientada a O            201710044      CS1102      Examen       11
                 CS1100    Introducción a ciencia de la C.       201710045      CS2701      Proyecto     15
                  ...                                             ...
Queremos saber todos los códigos del cursos
que toma el alumno “201710044”

                                                   alumnos.csv
                     Código          Nombre            Curso
                    ...
                   201710042   Molina Orellana Diego   CS1100
                   201710043   Paredes Sanchez Bruno   CS2701
                   201710044   Perez Fu Luis Adrian    CS1102
                   201710044   Perez Fu Luis Adrian    CS2701
                    ...




• En C++, podemos leer todo el archivo, filtrar todas las filas con
  otros códigos y entregar sola la información relevante

                       ¿Algún problema aquí?
Bueno, si los usuarios son impacientes y los
archivos grandes …


                              Mapa en memoria principal de alumnos.csv
            Clave     Valor
           ...        ...
          201710042   { (Molina Orellana Diego, CS1100) }
          201710043   { (Paredes Sanchez Bruno, CS2701) }
          201710044   { (Perez Fu Luis Adrian, CS1102),(Perez Fu Luis Adrian,CS2701) }
           ...        ...




• En C++, podemos cargar los datos en memoria principal, y
  utilizar un índice con códigos como claves (p.e., un “map”)

                      ¿Algún problema aquí?

Bueno, si los usuarios son impacientes y los
archivos no caben en memoria …

                                                                     alumnos.csv
                                    Código          Nombre              Curso
       Indíce (m. principal)       ...
                                  201710042   Molina Orellana Diego     CS1100
       Código       Bloque        201710043   Paredes Sanchez Bruno     CS2701
      ...                         ...
     201710042      1
     201710044      2             201710044   Perez Fu Luis Adrian      CS1102
      ...                         201710044   Perez Fu Luis Adrian      CS2701
                                   ...




• En C++, podemos crear bloques de datos ordenados por Código,
  y utilizar un índice con el primer Código en cada bloque

                             ¿Algún problema aquí?
Bueno, si tenemos que actualizar la tabla con
datos nuevos …
                                                                                   alumnos.csv
                                    Código                Nombre             Curso     Del?
       Indíce (m. principal)       ...
       Código       Bloque        201710042      Molina Orellana Diego       CS1100    x
      ...                         201710043      Paredes Sanchez Bruno       CS2701
     201710042      1             ...
     201710044      2
      ...                         201710044      Perez Fu Luis Adrian        CS1102    x
                                  201710044      Perez Fu Luis Adrian        CS2701
                                   ...




                                                               Inserciones (m. principal)
                                               Código              Nombre             Curso

                                              201710044     Perez Fu Luis Adrian      CS2804
                                               ...



• En C++, podemos crear un bloque en memoria principal, o
  podemos dejar espacio en los bloques para datos nuevos o …

                             ¿Algún problema aquí?
Bien, si a veces hay que consultar por el nombre
   del alumno entonces …
                                                                                   alumnos.csv
                                         Código           Nombre               Curso     Del?
   Indíce (m. principal)                ...
   Código           Bloque             201710042    Molina Orellana Diego      CS1100    x
  ...                                  201710043    Paredes Sanchez Bruno      CS2701
                                       ...
 201710042          1                                                                           alumnos.csv
 201710044          2
  ...                                  201710044    Perez Fu Luis Adrian       CS1102    x
                                       201710044     Código
                                                    Perez Fu Luis AdrianNombreCS2701      Curso     Del?
               Indíce (m. principal)    ...         ...
               Nombre        Bloque                201710042     Molina Orellana Diego    CS1100
              ...                                  201710042     Molina Orellana Diego    CS2701
             Molina Diego    1                     ...
             Paredes Bruno   2
              ...                                  201710043    Paredes Sanchez Bruno     CS2701
                                                   201710044    Perez Fu Luis Adrian      CS1102    x
                                                   201710044    Perez Fu Luis Adrian      CS2701
                                                    ...




• En C++, podemos crear otro índice ordenado por nombre …


                                 ¿Algún problema aquí?
ok ok, si a veces hay que consultar por el nombre
    de los cursos del alumno entonces …

                           alumnos.csv
        (indexado por Código y Nombre)                                     cursos.csv
   Código          Nombre             Curso
                                                                (indexado por Código)
  ...                                              Código      Nombre
 201710042   Molina Orellana Diego    CS1100        …
 201710043   Paredes Sanchez Bruno    CS2701       CS2701   Base de datos I
 201710044   Perez Fu Luis Adrian     CS1102       CS1102   Programación Orientada a O
 201710044   Perez Fu Luis Adrian     CS2701       CS1100   Introducción a ciencia de la C.
  ...                                               ...




• En C++, podemos crear otro índice para cursos.csv e
  implementar “joins” entre ambos índices

                                     ¿Algún problema aquí?
… uum, si hay que verificar que los alumnos solo
    tengan cursos que aparecen en cursos.csv …
                          alumnos.csv
       (indexado por Código y Nombre)                                                  cursos.csv
   Código          Nombre             Curso
                                                                            (indexado por Código)
  ...                                                          Código      Nombre
 201710042   Molina Orellana Diego    CS1100                    …
 201710043   Paredes Sanchez Bruno    CS2701                   CS2701   Base de datos I
 201710044   Perez Fu Luis Adrian     CS1102                   CS1102   Programación Orientada a O
 201710044   Perez Fu Luis Adrian     CS2701                   CS1100   Introducción a ciencia de la C.
  ...                                                           ...




              INSERT alumnos.csv               (201710044,Perez Fu Luis Adrian, CS1100)
              INSERT alumnos.csv               (201710044,Perez Fu Luis Adrian, CS2801)




• En C++, antes de hacer una inserción a alumnos.csv, podemos
  consultar a cursos.csv para verificar que el curso exista.

                                     ¿Algún problema aquí?
…   pues, si hay que permitir quitar cursos …
                          alumnos.csv
       (indexado por Código y Nombre)                                                  cursos.csv
   Código          Nombre             Curso
                                                                            (indexado por Código)
  ...                                                          Código      Nombre
 201710042   Molina Orellana Diego    CS1100                    …
 201710043   Paredes Sanchez Bruno    CS2701                   CS2701   Base de datos I
 201710044   Perez Fu Luis Adrian     CS1102                   CS1102   Programación Orientada a O
 201710044   Perez Fu Luis Adrian     CS2701                   CS1100   Introducción a ciencia de la C.
  ...                                                           ...




              DELETE alumnos.csv               (201710044,Perez Fu Luis Adrian, CS1100)
              DELETE cursos.csv                (CS2701, Base de datos I)




• En C++, podemos agrupar inserciones y/o borrados para
  mantener la consistencia de los datos (transacciones)

                                     ¿Algún problema aquí?
     …    si hay múltiplos usuarios actualizando la base
           de datos al mismo tiempo …
                                 alumnos.csv
              (indexado por Código y Nombre)                                                 cursos.csv
          Código           Nombre              Curso
                                                                                  (indexado por Código)
         ...                                                        Código       Nombre
        201710042    Molina Orellana Diego     CS1100                …
        201710043    Paredes Sanchez Bruno     CS2701               CS2701    Base de datos I
        201710044    Perez Fu Luis Adrian      CS1102               CS1102    Programación Orientada a O
        201710044    Perez Fu Luis Adrian      CS2701               CS1100    Introducción a ciencia de la C.
         ...                                                         ...




DELETE alumnos.csv (201710044,Perez Fu Luis Adrian, CS1100)   INSERT alumnos.csv (201710044,Perez Fu Luis Adrian, CS1100)
DELETE cursos.csv (CS2701, Base de datos I)




     • En C++, hay que aislar transacciones para evitar este tipo de
       situación (y otras similares)

                                             ¿Algún problema aquí?
… si hay que contar el número de cursos que
cada alumno toma u otra formas de consultas
…
                          alumnos.csv
       (indexado por Código y Nombre)                                         cursos.csv
   Código            Nombre             Curso
                                                                   (indexado por Código)
  ...                                                 Código      Nombre
 201710042     Molina Orellana Diego    CS1100         …
 201710043     Paredes Sanchez Bruno    CS2701        CS2701   Base de datos I
 201710044     Perez Fu Luis Adrian     CS1102        CS1102   Programación Orientada a O
 201710044     Perez Fu Luis Adrian     CS2701        CS1100   Introducción a ciencia de la C.
  ...                                                  ...




             SELECT codigo, COUNT(curso) FROM alumnos GROUP BY codigo




• En C++, podemos implementar un lenguaje de consulta
  general que cubre los rasgos más necesitados

                                       ¿Algún problema aquí?
… si el rendimiento de consultas no basta para
los usuarios, podemos optimizar …
                          alumnos.csv
       (indexado por Código y Nombre)                                         cursos.csv
   Código            Nombre             Curso
                                                                   (indexado por Código)
  ...                                                 Código      Nombre
 201710042     Molina Orellana Diego    CS1100         …
 201710043     Paredes Sanchez Bruno    CS2701        CS2701   Base de datos I
 201710044     Perez Fu Luis Adrian     CS1102        CS1102   Programación Orientada a O
 201710044     Perez Fu Luis Adrian     CS2701        CS1100   Introducción a ciencia de la C.
  ...                                                  ...




             SELECT codigo, COUNT(curso) FROM alumnos GROUP BY codigo




• En C++, podemos implementar varias optimizaciones en un
  planificador de ejecución

                                       ¿Algún problema aquí?
(╯°□°）╯︵ ┻━┻
¡Sí!                                           'utf-8' codec can't decode byte 0xed
                                               in position 417: invalid continuation
                                               byte
• A veces, faltan valores en las tablas
• Cursos pueden tener más que un nombre
• Tenemos valores como fechas, booleanos, etc., que queremos comparar,
  ordenar, manipular, sumar …
• El rendimiento de algunas consultas todavía es terrible
• La carga de datos todavía es demasiado lento
• No hay suficiente memoria para mantener los índices
• Los administradores quieren agregar columnas nuevas como la carrera de
  los alumnos
• Los alumnos no deberían tener acceso para cambiar sus notas
• Hay l33t h4cker$ que quieren pwnear nuestra base de datos para cambiar
  sus notas
• Tenemos que mantener respaldos en una forma segura
• You won’t see this so I can write it in English.
… y si pudiéramos solucionar estos problemas
deuna forma general …




                … habríamos implementado
                un sistema de bases de datos
Estos son problemas generales que se
encuentran en muchas aplicaciones
… muchas aplicaciones importantes
Un sistema de bases de datos es:
• Un sistema (de software) general
  para manejar
   bases de datos …
• Facilitan (en una forma general):
      • representar datos,
      • cargar datos,
      • organizar datos,
      • definir datos,
      • actualizar datos,
      • consultar datos,
      •…
• DBMS: (DataBase Management System)
Con un DBMS …
Los usuarios se encargan de:

• diseñar la estructura de la base de datos,
• escribir consultas,
• actualizar los datos,
•…

… solo las cosas específicas en el contexto de la
aplicación específica.
Con un DBMS …
Por debajo, el DBMS se encarga de:
• Almacenaje optimizado
• Indexación
• Procesamiento de consultas
• Optimización de consultas
• Manejo de transacciones
• Manejo de acceso concurrente
• Seguridad
• ¡y mucho más!

… las cosas generales que se necesitan en muchas aplicaciones.
Hay implementaciones con décadas de
desarrollo por miles de expertos
Pero DBMS están siempre evolucionando:
  tecnología cambia
Pero DBMS están siempre evolucionando:
  los requisitos de las aplicaciones cambian
5.
 ¿Una base de datos
 siempre modela
 datos como tablas?

  … ¿son siempre modelados así?
                                     profesores.csv
        Dni               Nombre                 Curso
       …
      40142153    Ernesto Cuadros Vargas         CS1100
      42440124    Teóﬁlo Chambilla Aquino        CS2701
      45142154    Heider Sanchez Enriquez        CS1102
      45142154    Maria Hilda Bermejo Rios       CS2701
       ...
                                                                                                   auxiliares.csv
                                                                Código             Nombre              Curso
                                 alumnos.csv                   …
  Código          Nombre                Curso                 201710001      Peña Mendoza Alejandro    CS1100
 ...                                                          201710033      Quesada Velarde Luis      CS2701
201710042   Molina Orellana Diego       CS1100                201710066      Quispe Roldan Enrique     CS1102
201710043   Paredes Sanchez Bruno       CS2701                201710077      Peña Cordova Diana        CS2701
201710044   Perez Fu Luis Adrian        CS1102                 ...
201710044   Perez Fu Luis Adrian        CS2701
 ...


                                                                                                          notas.csv
                                                 cursos.csv        Código       Nombre      Eval         Nota
                 Código       Nombre                              …
                  …                                              201710043      CS2701      Lab 1        17
                 CS2701    Base de datos I                       201710043      CS2701      Lab 2        18
                 CS1102    Programación Orientada a O            201710044      CS1102      Examen       11
                 CS1100    Introducción a ciencia de la C.       201710045      CS2701      Proyecto     15
                  ...                                             ...
       ¿Se puede modelar una base de datos
         como un mapa?



  Clave            Valor
 ...               ...
201710042          { (Molina Orellana Diego, CS1100) }
201710043          { (Paredes Sanchez Bruno, CS2701) }
201710044          { (Perez Fu Luis Adrian, CS1102),(Perez Fu Luis
Adrian,CS2701) }
 ...               ...




                                                                     ¡Sí!
¿Se puede modelar una base de datos
  como un árbol?




                                      ¡Sí!
¿Se puede modelar una base de datos
  como un grafo?




                                      ¡Sí!
Bases de Datos Relacional
              profesores.csv
• Tablas = Un modelo       de bases de datos
  – Bases de datos relacionales

                                               auxiliares.csv
• El modelo más establecido
             alumnos.csv


• El enfoque del curso

• Pero hablaremoscursos.csv
                  brevemente de otros                notas.csv

  modelos
6.
 Una diversidad de
 tipos de (sistemas
 de) bases de datos
Los sistemas más utilizados en la práctica
…




                            http://db-engines.com/en/ranking
7.
 ¿Qué vamos a
 aprender?
Una introducción a bases de datos:
• Hay tres tipos típicos de “usuarios” para un
  sistema de bases de datos:

  1.   Usuarios finales
  2.   Administradores del sistema
  3.   Desarrolladores de un sistema

• Enfocaremos en el primer tipo
  –    Incluye desarrolladores de aplicaciones de bases
       de datos
• Hablaremos un poco también de tipos dos y
  tres
En este curso, aprenderán
• Como se puede generalizar una consulta, la
  indexación, la gestión, etcétera, de datos

• Modelos de bases de datos
  – Con énfasis en el modelo relacional
  – Otros modelos: grafos, árboles, NoSQL …

• Usar y manejar sistemas de bases de datos
  – Cargar datos, escribir consultas, actualizar datos
No aprenderán (específicamente)
• Rasgos específicos de todos los sistemas
• Como se puede implementar un sistema de
  bases de datos (en detalle)
• Minería de datos
• Sistemas distribuidos (en detalle)
• Datalog / lógica / teoría (en detalle)
• Big data (en detalle)
La estructura del curso
• Introducción / Motivación
• Entidades/Relaciones
• El Modelo Relacional
• El Álgebra Relacional
• SQL (consultas)
• Indexación / Optimización
• SQL (actualizaciones)
• Formas Normales
• Transacciones
• Otros Modelos:
  Base de datos no relacional: JSON
  Base de datos en Grafos: SPARQL
¿Preguntas?
                                 GRACIAS


                                                Brenner Ojeda bojeda@utec.edu.pe
                                             Teófilo Chambilla - tchambilla@utec.edu.pe

Server Discord
                 En colaboración Aidan Hogan de la Universidad de Chile (https://aidanhogan.com/)

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
