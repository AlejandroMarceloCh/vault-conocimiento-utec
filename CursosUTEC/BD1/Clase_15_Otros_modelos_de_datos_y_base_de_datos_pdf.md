---
curso: BD1
titulo: Clase 15 Otros modelos de datos y base de datos
slides: 36
fuente: Clase 15 Otros modelos de datos y base de datos.pdf
---

OTROS MODELOS DE DATOS
    Y BASE DE DATOS

 CS2041- Base de Datos I
                 Ciclo 2024 - 1



  Teófilo Chambilla - tchambilla@utec.edu.pe
     Brenner Ojeda - bojeda@utec.edu.pe
CS2041 - Base de datos I                        Computer Science



   Agenda
   ❏      Bases de datos, recuperación de la
          información y bases de conocimiento
   ❏      Volúmenes de Datos (datos grandes)
   ❏      Modelos y formatos de datos (texto,
          imágenes, video)
   ❏      Ciclo de los datos
   ❏      Bases de datos No SQL
   ❏      Introducción a MongoDB
Nuestro mundo de los datos
Proceso de base de datos relacional
      Bases de datos
Recuperación de información
   Bases de conocimiento
   Capas de procesamiento de datos


         APIs                 Aplicaciones             Servicios




Estructura de datos: Tablas, Grafos        Lenguaje de consultas




Almacenamiento nativo           Archivos                RDBMS
   Capas de procesamiento de datos


         APIs                 Aplicaciones             Servicios




Estructura de datos: Tablas, Grafos        Lenguaje de consultas

                                                                   Base de datos
                                                                   relacionales

Almacenamiento nativo           Archivos                RDBMS
               Tres niveles de abstracción de datos


                                                                                 Confianza
                                                                  Demostraciones



                                                                                             Firma Digital
                          KR - Lógica           Lógicas + Ontologías
                                                (conceptos + Conocimiento)


                                         Datos + esquemas
                 Bases de datos          (entidades + relaciones)


                                  Sintaxis + formatos
Recuperación de información       (Texto + Links + Lenguajes de codificación)



                                  Unicode                                       URI
     Tres niveles de acceso a datos


    Conceptos + Conocimientos         Inteligencia Artificial
(cuerpo organizado de afirmaciones)



                                         Bases de Datos
       Objetos (entidades)
                +
           relaciones

                                      Recuperación de la información




         Texto + Enlaces
                              Tres enfoques / tres áreas

1.       Recuperación de información
 -       recuperar información a partir de fuentes
 -       Aproximación / cobertura / escalabilidad
 -       Ojalá precisión

                                                     2.       Bases de datos
                                                          -    Administrar y organizar datos limpios con
                                                               precisión
                                                          -    Separación de modelamiento e
                                                               implementación
                                                          -    Ojalá razonamiento/ deducción sobre ellos
3.       Representación del Conocimiento

     -   Razonar sobre datos organizados
     -   Preocupación por la expresividad
¿QUÉ SON GRANDES DATOS?
   VOLUMEN DE DATOS
            Tamaño de datos

Nombre          Estándar SI   Uso Binario

Kilobyte          10 e 3        2 e 10

Megabyte          10 e 6        2 e 20

Gigabyte          10 e 9        2 e 30

Terabyte          10 e 12       2 e 40

Petabyte          10 e 15       2 e 50

Exabyte           10 e 18       2 e 60

Zettabyte         10 e 21       2 e 70
             Modelos y formatos de datos

KILO 10^3 (2^10)
   Texto (email, documento)



MEGA 10^6 (2^20)
   Libro, fotografía



GIGA 10^9 (2^30)
    Memoria RAM, buen video



(Este es nuestro mundo...)
      Volumen de datos I: poniéndose serios

TERA 10^12      2^ {40}


-- Tráfico Global de Internet (20 TB p. sec)

-- Biblioteca del Congreso (USA): 200 TB

-- Discos de 1TB (2007)

-- Wikipedia: 10 Terabyte dump (2015)                                                  lquier
                                                                               j a cua
                                                                             e
-- 3-D movie Monsters Vs Aliens (necesitó                             l o man pete
                                                                    ,        s
   100 TB disco)                                            a . Pero e se re
                                                     h u man ento qu
                                                 ala       im
                                            o esc / exper
                                          N
                                               resa
                                           emp
              Modelos y formatos de datos

PETA 10^15     2^50

 ●   Tráfico Global Internet por hora: 70 PB

 ●   Internet Archive (50 PB) (crece 100 TB por mes)

 ●   Google procesa 100 petabytes de datos cada día

 ●   1/2 PB: filmar la vida de una persona (100 años en alta definición).

 ●   Facebook tiene 60 mil millones de imágenes, esto es 1,5PB.

 ●   Los experimentos del LHC (Large Hadron Collider) producen 30 petabytes
     de datos al
     año.
                              Futuro próximo

EXA 10^18 (2^60)                          Zetta 10^21 (2^70)

 -   Todas las palabras
     que se han hablado                        El universo digital (todos los
      aprox. 5 EXB texto                       datos o archivos
     (digitalizadas)                           almacenados digitalm.)
                                               alcanza 1,2 millones de
 -   Google almacena 15 EB                     petabytes, o 1,2
                                               zettabytes.
 -   Tráfico internet diario 2 EB

 -   El premio del Sultán en el
     ajedrez: 2^64: casi 1 EXP            Tráfico Internet anual: 1 ZB
MODELOS Y FORMATOS
    DE DATOS
  ¿Formato de datos? Depende...



XML, JSON, RSS, Atom, YAML, iCalendar, CSV,
Serialized PHP, HTML, PNG, GeoRSS, vCard,
     Text, RDF, OPML, MediaRSS, VML,
 TV-Anytime, hCalendar, FOAX, XSPF, SQL,
                GML, CDF
                             Modelo =/= Formato

1.   Binario (eficiente, ilegible)


2.   Texto (natural para humanos, ineficiente, poca o nada estructura)


3. Tablas (buena organización, históricamente popular, eficiente, excelente soporte:RDBMS;
versión “reguleque”: CSV)


4. Documentos (natural para humanos, semi – estructurado, formalizado
como XML, JSON, et al.)


5.   Grafos (excelente expresividad, difícil –aún- de procesar, poco soporte. Es lo que viene)
                      Tres modelos básicos




                           Documentos / árboles




Tablas / relaciones                               Grafos / redes

Dos modelos “nuevos” (en base de datos)




  Texto
                             Imágenes y videos
EL CICLO DE LOS DATOS
                                                                               CLAVE DE NIVEL DE RIESGO
                         10.
                                           1.                                      Alto peligro
                     DESTRUCCIÓN
                                       COLECCIÓN                                   Peligro moderado
                                                                                   Poco peligro
         9.
     RETENCIÓN
                                                       2.
                                                   RELEVANCIA


  8.
BACKUP
                     Ciclo de
                    vida de los                             3.
                                                      CLASIFICACIÓN
                       datos
     7.
PUBLICACIÓN
                                                    4.
                                              MANIPULACIÓN Y
                    6.                       ALMACENAMIENTO
              MANIPULACIÓN          5.
              CONVERSIÓN O    TRANSMISIÓN
               ALTERACIÓN     Y TRANSPORTE


                                                                Referecian: SearchSecurity TechTarget
EL MUNDO DE LAS BASES DE DATOS No SQL
                           Formas de accesos a datos




no estructurado
                                   Buscador / expresiones       Técnicas estadísticas
                  Navegación
                                         regulares                   (NLP / AI)




estructurado
                                  Lenguaje de consulta (SQL)
                                                                        API
                  Formulario
                                                               Web Service Endpoints



                   humana                    semi                    automática
Tipo de base de datos NoSQL
                                           Guía visual de sistemas NoSQL
                                                                                                                                               Relacional (comparación
                                       Disponibilidad: Cada                                                                                    Key-Value
                                       cliente siempre puede
                                       leer y escribir.           A                                                              Data Models   Column-Oriented/Tabular
                                                                                                                                               Document-Oriented




                                      CA
                                                                                                     AP
                          RDBMS            Aster Data
                                                                                          Dynamo          Cassandra
                          (MySQL,          Greenplum
                                                                                          Voldemort       SimpleDB
                          Postgres,        Vertica
                                                                                          Tokyo Cabinet   Couch DB
                          etc.)                                Pick two                   KAI             Riak




Consistencia: Todos los
                              C                                   CP
                                                                                                P         Tolerancia de partición:
clientes siempre tienen
la misma vista de los                             BigTable     MongoDB      Berkeley DB                   El sistema funciona bien a
datos.                                            Hypertable   Terrastore   MemcacheDB                    pesar de las particiones
                                                  Hbase        Scalaris     Redis                         físicas de la red.
                               Habilidades de ciencia de los datos
                                                                             La ciencia de datos, dada su naturaleza interdisciplinaria, requiere una
                                  Zona                                       intersección de habilidades: habilidades de piratería informática,
                                peligrosa                                    conocimientos de matemáticas y estadísticas, y experiencia
                                                                             sustancial en un campo de la ciencia.


                                                                             Las habilidades de piratería son necesarias para trabajar con
                                                                             cantidades masivas de datos electrónicos que deben adquirirse,
              Habilidades                      Experiencia                   limpiarse y manipularse.
              de piratería                      sustantiva

                                                                             El conocimiento de las matemáticas y las estadísticas permite a un
                                                                             científico de datos elegir métodos y herramientas adecuados para
                               Ciencia de                                    extraer información de los datos.
                                los datos
                                                                             La experiencia sostenida en un científico apasionado es crucial para
                                                                             generar preguntas e hipótesis motivadoras e interpretar los
                                                                             resultados.


                                                                             La investigación tradicional se encuentra en la intersección del
                                                                             conocimiento de las matemáticas y el conocimiento estadístico con
                                                                             una experiencia sustancial en un campo científico.
Aprendizaje                                                  Investigación
automático                                                    tradicional    El aprendizaje automático surge de combinar habilidades de piratería
                                                                             con conocimientos de matemáticas y estadísticas, pero no requiere
                             Conocimiento de                                 motivación científica.
                              matemáticas y
                               estadísticas                                  ¡Zona peligrosa! Las habilidades de piratería combinadas con la
                                                                             experiencia científica sustantiva sin métodos rigurosos pueden dar
                                                                             lugar a análisis incorrectos.
Introducción a MongoDB
                 Basado en Documentos


● Las bases de datos almacenan y recuperan documentos
   que pueden ser XML,JSON, BSON, etc.

● Los documentos almacenados son similares unos con
   otros pero no necesariamente con la misma estructura.
                         Mongo DB

● Su nombre surge de la palabra en inglés
   “humongous” (que significa enorme).

● MongoDB guarda estructuras de datos en documentos tipo
   JSON (JavaScript Object Notation) con un esquema
   dinámico.

● Internamente MongoDB almacena los datos en formato
   BSON (Binary JavaScript Object Notation).

● BSON está diseñado para tener un almacenamiento y
   velocidad más eficiente.
                                   Basado en Documentos

                                            La empresa 10gen lo desarrolla cuando estaba
                                     2007   desarrollando una Plataforma cómo servicio (PaaS -
                                            Platform as a Service). Similar a Google App Engine.
Bases de Datos
 Documentales

                                            En este año MongoDB es lanzado como Producto. Es
                                     2009
                                            publicado bajo licencia de código abierto AGPL.
                  Bases de Datos
                    De Código
                     Abierto
                                            Se lanza la versión 1.4 considerada como una Base de
                                     2011   Datos lista para producción.

 Bases de Datos
  de Propósitos
   Generales                                Actualmente MongoDB está por la versión 5.x y es la
                                     2021   Base de Datos NoSQL con mayor popularidad.
Terminología RDBMS vs. Document Based (MongoDB)

                 RDBMS                MongoDB

 Database instance       MongoDB instance

 Database / Schema       Database

 Table                   Collection

 Row                     Document

 Rowid                   _id

 Join                    Dbref
           Modelado de Relaciones entre Documentos

Relaciones Uno a Uno                Si la dirección es un dato frecuentemente consultado junto con el
con documentos embebidos            Nombre de la persona, la mejor opción será embeber la dirección
                                    en los datos de la persona.
Modelo Normalizado
                                                Colección Personas
Colección Personas                              { _id: “u0001",
{ _id: “u0001",                                 nombre: “Juan Martín Hernandez" }
nombre: “Juan Martín Hernandez" }

                                                 direccion:{calle: “Malabia 2277",
Colección Direcciones                                           ciudad: “CABA",
{ persona_id: “u0001",                                          provincia: “CABA",
calle: “Malabia 2277",                                          codPostal: "1425" }
                                                 }
ciudad: “CABA",
provincia: “CABA",                  Con una sola consulta podríamos recuperar toda la información de
codPostal: "1425" }                 una persona.
                           En qué casos usarlas ?

Logging de Eventos
 ●   Las bases de datos basadas en documentos puede loguear cualquier clase de eventos y
     almacenarlos con sus diferentes estructuras.

 ●   Pueden funcionar como un repositorio central de logueo de eventos.

CMS, blogging
 ●   Su falta de estructura predefinida hace que funcionen bien para este tipo de aplicaciones.

Web-analytics / Real-Time analytics
 ●   Almacenar cantidad de vistas a una página o visitantes únicos.

Commerce
 ●   A menudo requieren tener esquemas flexibles para los productos y órdenes

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
