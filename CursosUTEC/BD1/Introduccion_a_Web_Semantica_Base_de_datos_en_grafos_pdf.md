---
curso: BD1
titulo: Introducción a Web Semantica “Base de datos en grafos”
slides: 165
fuente: Introducción a Web Semantica “Base de datos en grafos”.pdf
---

Introducción a Web
Semántica
“Base de datos de
grafos”


 CS2041
 Bases de Datos I
 Ciclo 2023-2




                    Teófilo Chambilla - tchambilla@utec.edu.pe
                       Brenner Ojeda - bojeda@utec.edu.pe
CS2041
BASES DE DATOS I
CICLO 2023-2




                                                                                                               NO SQL/GRAFOS
Introducción



Modelo Relacional     Algebra Relacional &       SQL                       Planificación y   Transacciones y
                                                         Formas Normales
                       Cálculo Relacional

 Entidad - Relación                          Actualización, Dependencias   Optimización de ACID
                                             Restricciones funcionales     Consultas
CS2041 - Base de datos I                         Computer Science




   Agenda
   ❏      Motivación
   ❏      La web clásica
   ❏      Nociones básica y el modelo de datos
          RDF
   ❏      La Web semántica
   ❏      Nociones de URI
   ❏      Nociones de Literal y Triple RDF
   ❏      Grafo RDF
   ❏      SPARQL
   ❏      WikiData
   ❏      LinKed Data
      MOTIVACIÓN
Jugadores de fútbol que nacen
en un país con más de 10
millones de habitantes, que
jugaron como portero de un club
que tiene un estadio con más de
30,000 asientos y el país del club
es diferente al país de
nacimiento.
Otro Ejemplo
Muestre la lista de personajes educados en
Universidades Peruanas. se desea conocer el
nombre de la persona y el de la universidad




        https://query.wikidata.org/
        .
  La web clásica es una red
      de documentos,
interpretable por humanos,
 donde las relaciones entre
 documentos no tienen un
        significado.
 La web de datos es una red
de afirmaciones, interpretable
  por humanos y máquinas,
  donde las afirmaciones se
    relacionan y tienen un
          significado.




                                 Tim_Berners-Lee
NOCIONES BÁSICAS Y
       EL MODELO DE DATOS RDF
 ¡La Web es magnífica!




¿Pero puede ser mejor?   … a veces es difícil encontrar información relevante.
¡Pero Google es magnífico!
Se pueden encontrar respuestas directas
Haciendo una tarea para su clase …

                 Quiere encontrar cada:
                     –   Ganadores del Premio Nobel en Literatura
                     –   Que han luchado en una guerra
                     –   El año que ganaron el premio
                     –   Y el año que comenzó la guerra




                           ¿Cómo se puede encontrar esta
                           información con la Web actual?
Muchas pestañas de Wikipedia …




                   …
La Web actual

                La Web actual es un conjunto de
                documentos, en general páginas
                web escritas en HTML.
La Web actual

  Esas páginas Web HTML están
  formadas por contenido y por
  enlaces.



                                   Contenido           Enlaces

                                El contenido son   Los enlaces nos
                                texto, imágenes,    redirigen a otro
                                 videos, audios,     documento(a
                                        etc.       otra página web)
Un ejemplo de la Web actual
Enlaces en una página Web
Desafíos de la Web Actual

                               Múltiples organizaciones
           Heterogénea         generan datos, de forma
                                   independiente.

             Masiva           La cantidad de información
                                 existente es enorme.


           Cambia muy          Cada día son publicados y
             rápido         borrados enormes volúmenes de
                                     información.

                              En general, sólo una persona
         Hecha para
                            puede interpretar la información
         humano
                                 de la una página Web.
La Web actual es heterogénea
La Web actual es masiva




                     = 5.9 TB de datos
                           (aprox)

La Web actual es masiva




                                = 235 TB de datos
                                = 40 Wikipedias
          (Biblioteca del Congreso de EEUU incluye Web Archive)
La Web actual es muy rápida




                            = 160 TB/s transferidos
                            = 27 Wikipedias/segundo
         (fuente: Cisco).
La Web actual está hecha para humanos




                   ¿Cómo puede un computador
                   entender esta Web?
La Web actual está hecha para humanos




                   ¿Leyendo el texto disponible ?

                   ¿Cómo sabe una aplicación
                   computacional qué texto leer?
La Web actual está hecha para humanos




                  ¿Mirando el código HTML?

                  ¿Es posible Identificar el
                  nombre de una persona en el
                  código HTML ?
¿Cómo podemos aprovechar estos datos?




                 Los   Computadores   tiene   la
                 capacidad para poder analizar
                 estos datos.
¿Cómo podemos aprovechar estos datos?




                 Pero actualmente no son capaces
                 de interpretarlos correctamente ...
                 (Las páginas que mostramos están
                 pensadas para personas )
¿Cómo podemos aprovechar estos datos?




                 Hay que permitir que las
                 aplicaciones     computacionales
                 entiendan los datos …
                     ¿Cómo hacemos esto?
Requisitos para una Web de datos efectiva

     Primero, es necesario tener una lenguaje que
     permita especificar recursos en la Web y las
               relaciones entre ellos.



                               Un requisito fundamental: este lenguaje
                               debe ser procesable por un computador
Requisitos para una Web de datos efectiva

    Segundo, necesitamos poder consultar estos datos
         mediante aplicaciones computacionales.




                        Dos requisitos fundamentales:

                         ●   Debemos tener un lenguaje para escribir
                             consulta que sean procesable por un
                             computador.
                         ●   Debemos ser capaces de sacar conclusiones
                             de los datos de manera automática.
La Web de Datos / La Web Semántica
La Web Semántica



                   “La Web Semántica es una extensión
                    de la Web actual en la cual se da un
                        significado bien definido a la
                   información, permitiendo mejorar la
                      colaboración entre personas y
                         computadores en la Web”

                              Tim Berners-Lee 2001
La Web Semántica en la práctica

   Es un conjunto de recomendaciones desarrolladas por el
    World Wide Web Consortium, cuyo objetivo es
     que los computadores sean capaces de entender los
                      datos en la Web



                          ●   Una recomendaciones es un descripción
                              formal de una tecnología que debería ser
                              utilizadas por todos. Es decir, un lenguaje
                              común para todos.

                          ●   El w3c es el organismos regular de la Web
Los estándares para Web Semántica
LA NOCIÓN DE URI
¿Qué es la Web Semántica?



                “Es una extensión de la Web
                actual en la cual se da un
                significado bien definido a la
                información, permitiendo mejorar
                la colaboración entre personas y
                computadores en la Web”

                      Tim Berners-Lee 2001
¿Cómo realizar la Web Semántica?

                                                              Debe ser
                      </>                      Requisito      lenguaje
                                                             procesable
                     Construir                                 por un
                     Lenguaje                                computador




             que permita especificar                       Propuesta actual




 Recursos                         Relaciones
                                                              Lenguaje
 en la Web                           entre
                                                                RDF
                                 recurso Web
Características básicas de RDF
RDF es la propuesta del World
Wide Web Consortium (W3C)
para representar información
sobre recursos en la Web




                                 1                 2                  3
                                                                        Las piezas
                                RDF está basada          Una
                                                                       básicas para
                                  en el uso de      especificación
                                                                      construir una
                                grafos dirigidos    RDF puede ser
                                                                      especificación
                                 y etiquetados     procesada por un
                                                                       RDF son los
                                                      computador
                                                                        URIs y los
                                                                         literales
Figura: Ejemplo de un grafo

  URI (Uniform Resource Identifier)
    Un URI es un identificador
    de un recurso en la WEB


                                       Recurso

                           Recurso
                                                 Un recurso corresponde a
                                                 un elemento mencionado en
                                                 la Web por ejemplo:
                                                   ● Un página Web
   URI                Recurso
                                     Web           ● una persona
                                                   ● un libro
                                                   ● una ciudad
                                                   ● un gen
Identificador             Recurso                  ● una película


                                     Recurso
Ejemplo y componentes de un URI


  http especifica el              resource/Lionel_Messi es el
  protocolo de acceso al          camino, la parte principal del
  recurso                         URI

    http://dbpedia.org/resource/Lionel_Messi


            dbpedia.org es la autoridad del
            URI, la cual es similar al nombre
            de dominio de una página Web.
Idea: Usar los identificadores de la Web
• URL: Uniform Resource Location
  – La ubicación de un recurso de la Web
  – (p.ej., una página Web)
  – http://ex.org/Dubl%C3%ADn.html

• URI: Uniform Resource Identifier (RDF 1.0)
  – Un identificador de un recurso general
  – (p.ej., una ciudad)
  – http://ex.org/Dubl%C3%ADn
Algunos ejemplos de URIs



         http://dbpedia.org/resource/Lionel_Messi




           https://www.pcm.gob.pe
Usaremos URIs con prefijos


Prefijos comunes:
LAS NOCIONES DE LITERAL
                    Y TRIPLE RDF
Una segunda pieza básica de RDF:Los literales

Un literal representa un valor
concreto en una especificación
RDF




                                 Messi nació en la fecha
                                      “1987-06-24”
Una segunda pieza básica de RDF:Los literales

Un literal es simplemente
una cadena de caracteres




                             “1987-06-24”
                            “Lionel Messi”
                               “157.38”
                              “18:25:00”
Una segunda pieza básica de RDF:Los literales

Un literal puede tener un
tipo asociado




                            - Fecha: “1987-06-24”^^xsd:date
                            - Número Real: “157.38”^^xsd:float
                            - Hora: “18:25:00”^^xsd:time
Un tiple en RDF
En una especificación RDF,                                  Puede ser utilizado para dar
una relación entre dos                                      el valor de un atributo
recursos es dada a través de                                asociado a un recurso.
un triple.




           Sujeto                       Predicado                           Objeto

                                 Está dado por un URI, el cual
                                 representa:
                                   - Una relación entre           Es un recurso identificado por
Es un recurso identificado por
                                       recursos si el objeto es   un URI o un valor dado por un
un URI
                                       un recurso                 literal
                                   - Un atributo si el objeto
                                       es un valor
Abreviación de URis

Usualmente, los URIs son
abreviados      utilizando
prefijos


                       @prefix dbpedia: http://dbpedia.org/resource

                       Entonces:
                       dbpedia:Lionel_Messi

                       Es la abreviación de :

                       http://dbpedia.org/resource/Lionel_Messi
Un primer ejemplo de tiple
El siguiente ejemplo indica
que     Messi   nació    en
argentina




       dbpedia:                  Predicado                dbpedia:
     Lionel_Messi                birthPlace               Argentina



                              Este triple indica una relación entre los
                              recursos:

                              dbpedia:Lionel_Messi y
                              dbpedia:Argentina
Un segundo ejemplo de triple
El siguiente ejemplo indica
que     Messi   juega    en
barcelona




       dbpedia:                  Predicado                dbpedia:
     Lionel_Messi                currentclub            FC_Barcelona



                              Este triple indica una relación entre los
                              recursos:

                              dbpedia:Lionel_Messi y
                              dbpedia:FC_Barcelona
Un tercer ejemplo de triple
El siguiente ejemplo indica
que Messi nació el 24 junio
de 1987.




       dbpedia:                  example:                “1987-06-24”
     Lionel_Messi                 birthday


                              Este triple indica que el valor del atributo
                              example:birthday para el recurso
                              dbpedia:Lionel_Messi es “1987-06-24”
EL CONCEPTO DE GRAFO RDF
Un Grafo RDF




               Un grafo RDF está formado por
               un conjunto de triples RDF
Un primer ejemplo de triple

El siguiente ejemplo indica
que Messi nació en Rosario




        dbpedia:                 dbpprop:                 dbpedia:
      Lionel_Messi               birthPlace                Rosario




                              Un grafo puede tener solo un triple.
Un segundo ejemplo de triple
El siguiente ejemplo indica
que Messi vive en Barcelona




   dbpedia:                   dbpprop:     dbpedia:
 Lionel_Messi                 birthPlace    Rosario




                              dbpprop:     dbpedia:
                              residence    Barcelona
Un segundo ejemplo de triple
  El siguiente ejemplo indica
  que Messi vive en Barcelona




  dbpedia:                           dbpedia:    dbppro      dbpedia:
                        dbpprop:
Lionel_Messi                         Rosario     p:
                        birthPlace                           Santa_Fe_Province
                                                 IsPartOf




                                                  dbppro
                        dbpprop:     dbpedia:     p:         dbpedia:
                        residence    Barcelona    IsPartOf   Province_of_Barcelona
Un grado RDF en la Web


           Hemos construido un grafo en base a triples:


            - Messi nació en Rosario
            - Messi vive en Barcelona
            - Rosario es parte de la Provincia de Santa fe
            - Barcelona es parte de la Provincia de Barcelona




               ¿Cómo se almacena este
               grafo en la Web?

 Un grado RDF como archivo


      Un grafo RDF es almacenado como una secuencia de triples



dbpedia:Lionel_Messidbpprop:birthPlace      dbpedia:Rosario.
dbpedia:Lionel_Messidbpedia-owl:residence   dbpedia:Barcelona.
dbpedia:Rosario     dbpedia-owl:isPartOfdbpedia:Santa_Fe_Province.
dbpedia:Barcelona   dbpedia-owl:isPartOfdbpedia:Province_of_Barcelona.
 Uso de prefijos en un grafo RDF
  Para simplificar la escritura
  de URIs en un grafo RDF
  usamos prefijos



       En el grafo RDF anterior usamos los siguiente prefijos


@prefix dbpedia: <http://dbpedia.org/resource>.
@prefix dbpprop: <http://dbpedia.org/property>.
@prefix dbpedia-owl:<http://dbpedia.org.ontology>.
 Un grafo RDF complejo
 Aquí vemos un archivo completo de un grafo RDF:

@prefix dbpedia: <http://dbpedia.org/resource>.
@prefix dbpprop: <http://dbpedia.org/property>.
@prefix dbpedia-owl:<http://dbpedia.org.ontology>.


dbpedia:Lionel_Messidbpprop:birthPlace      dbpedia:Rosario .
dbpedia:Lionel_Messidbpedia-owl:residence   dbpedia:Barcelona .
dbpedia:Rosario     dbpedia-owl:isPartOfdbpedia:Santa_Fe_Province .
dbpedia:Barcelona   dbpedia-owl:isPartOfdbpedia:Province_of_Barcelona.
Entonces: Los triples representan un grafo
Protocolo y Lenguaje de Consulta de RDF:

SPARQL: SPARQL PROTOCOL AND RDF
QUERY LANGAUGE
SPARQL: Consultar Grafos en RDF




     Consulta: “Quién protagoniza en la película ‘Sharknado’?”
SPARQL: Consultar Grafos en RDF




Consulta:                    Soluciones:
SPARQL Prefijos: Abreviaturas de IRIs
SPARQL: cláusula de WHERE
• Donde se produce la magia
• Especifica un grafo de consulta




                              “Patrón triple”
                              (un triple con variables)
SPARQL: cláusula de WHERE
SPARQL: cláusula de WHERE




   Consulta: “¿En cuáles (otras) películas han actuado los actores de
                             Sharknado?”
SPARQL: cláusula de WHERE
SPARQL: cláusula de WHERE




                      “Basic Graph Pattern”
                       (un conjunto de pátrones triples)
SPARQL: Joins




                “Variable de Join”
                (una variable en múltiples lugares)
SPARQL: Unión




Consulta: “¿Cuáles son los títulos de las dos primeras películas en la serie Sharknado?”
SPARQL: Unión
 SPARQL: Left-join (OPTIONAL)




Consulta: “¿Los títulos de películas y (cuando sea disponible) sus fechas de estreno?”
SPARQL: Left-join (OPTIONAL)




                         “Variable UNBOUND”
                      (una variable sin una solución)
SPARQL: Filtros




        Consulta: “¿Cuales películas estrenaron en 2014?”

SPARQL: Filtros




                  Resultados vacíos
SPARQL: Filtros




                  Una abreviatura
SPARQL: cláusula de WHERE (otro ejemplo)
SPARQL: cláusula de WHERE (otro ejemplo)




                          Como NOT EXISTS/EXCEPT!
SPARQL: SELECT con *
SPARQL: SELECT con proyección




                                 Devuelve
                                duplicados
SPARQL: SELECT con DISTINCT




                              (no hay duplicados)
SPARQL: ASK




              true si hay al menos
                 un resultado,

                  false si no.
SPARQL: CONSTRUCT




                    Devuelve un grafo de RDF
Modificadores: ORDER BY, LIMIT, OFFSET



   Consulta: “La segunda película y la tercera película más recientes”
GOOGLE'S KNOWLEDGE GRAPH
Google: “Info-box”
Google: Búsqueda Semántica
Datos estructurados como grafos …
FACEBOOK: OPEN GRAPH PROTOCOL
 Mientras tanto en Facebook …




  Facebook quiere saber
alguna información de los
 documentos con enlaces
    en los comentarios
Mientras tanto en la Web …




        Facebook quiere saber alguna información sobre las
           cosas que uno puede “Like” en la Web externa
Facebook Open Graph Protocol
LA WIKIPEDIA DE DATOS:
WIKIDATA
¿Qué es Wikidata?

Wikipedia: Varios Idiomas
Wikipedia: Listas, etc.
Farfán marcó un gol …




            Ahora un ejército de personas tienen
                 que actualizar Wikipedia
                (texto, listas, idiomas, etc.)
Una solución: Wikidata
Wikidata: datos estructurados
Servicio de consulta (SPARQL):
Servicio de consulta (SPARQL):
(Hidden slide)
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?laureateName ?awardYear ?warName ?warYear
WHERE {
  ?laureate p:P166 ?award .       # Winner of some prize
  ?award ps:P166 wd:Q37922 .         # Prize is Nobel Pr. in Lit.
  ?award pq:P585 ?awardDate .        # Get the date of the award
  BIND(YEAR(?awardDate) as ?awardYear) # Get the year of the award
  ?laureate wdt:P607 ?war .       # Find war(s) laureate was in
  ?war rdfs:label ?warName .       # Get name(s) of war(s)
  ?war wdt:P580 ?warStart .                         # Get year the war started
  BIND(YEAR(?warStart) as ?warYear)
  ?laureate rdfs:label ?laureateName . # Get name of laureate
  FILTER(lang(?warName)="en"         # Filter for English
   && lang(?laureateName)="en")       # ... names only
} ORDER BY ?awardYear             # Order by year or award
https://query.wikidata.org/
LINKED (OPEN) DATA
Esto también pasa con los datos abiertos y
sus metadatos

   No alcanza con publicarlos en formatos
   abiertos para poder relacionarlos y que su
   significado sea procesable por máquinas


                  Necesitamos algo más ...
Linked Data + Open Data = Linked Open Data


                             ★
                            ★★
                          ★★★
                         ★★ ★★
                         ★★★★
                             ★
    5 ★ Datos Abiertos


    Tim Berners-Lee, el inventor de la Web e
★   iniciador de los Datos Enlazados (Linked
    Data), sugirió un esquema de desarrollo
    de 5 estrellas para Datos Abiertos.


                 A      continuación      veamos
                 ejemplos para cada escalón o
                 nivel de estrellas y veamos los
                 costos y beneficios involucrados
                 en cada caso.
   Las 5 ★’s de Linked Open Data
★       Publicar datos bajo licencia abierta

★★      Hacer los datos "legibles a máquina"
        Por ejemplo, una hoja de cálculo mejor que una tabla PDF.


★★★           Utilizar formatos no propietarios
        Por ejemplo, un archivo de texto CSV mejor que Excel


★★★★Usar URIs para nombrar los objetos (sugerencia: RDF)
        usar identificadores inequívocos que se puedan vincular / buscar


★★★★★ Proporcionar enlaces a otro contenido (sugerencia: Linked
Data)
        Para que los consumidores puedan seguir enlaces para obtener más información




                  Cada estrella mejora la interoperabilidad de los datos.
            ESQUEMA 5 ★ DATOS ABIERTOS
                                                                                 Para que los consumidores
Cada estrella mejora la interoperabilidad de los datos.                       puedan seguir los enlaces para
                                                                                             encontrar más.

                                                 Use identificadores inequívocos que
                                                       puedan vincularse / buscarse.

                                  Por ejemplo, un archivo de texto
                                              CSV mejor que Excel

              Por ejemplo, una hoja de cálculo
                     mejor que una tabla PDF




                                    Fuente: http://5stardata.info/en/
   ¿Qué necesitamos para lograr las 5?
RDF Un modelo de datos basado
en triplas que permite representar
relaciones.



            SPARQL El lenguaje de consultas
                       sobre RDF.



                     RDF-S y OWL para representar
                     metadatos y darles significado
                     (ontologías).
Ontología de Escuela Profesionales de Computación
Linked Open DATASETS
Crecimiento de LINKED DATA CLOUD




                                   Oct. 2007
Crecimiento de LINKED DATA CLOUD



                                   Oct. 2007
                                   Nov. 2007
Crecimiento de LINKED DATA CLOUD



                                   Oct. 2007
                                   Nov. 2007
                                   Feb. 2008
                                   Sep. 2008

Crecimiento de LINKED DATA CLOUD



                                   Oct. 2007
                                   Nov. 2007
                                   Feb. 2008
                                   Sep. 2008
                                   Mar. 2009
Crecimiento de LINKED DATA CLOUD



                                   Oct. 2007
                                   Nov. 2007
                                   Feb. 2008
                                   Sep. 2008
                                   Mar. 2009
                                   Jul. 2009
Crecimiento de LINKED DATA CLOUD



                                   Oct. 2007
                                   Nov. 2007
                                   Feb. 2008
                                   Sep. 2008
                                   Mar. 2009
                                   Jul. 2009
                                   Sep. 2010
Crecimiento de LINKED DATA CLOUD



                                   Oct. 2007
                                   Nov. 2007
                                   Feb. 2008
                                   Sep. 2008
                                   Mar. 2009
                                   Jul. 2009
                                   Sep. 2010
                                   Sep. 2011
Crecimiento de LINKED DATA CLOUD



                                   Oct. 2007
                                   Nov. 2007
                                   Feb. 2008
                                   Sep. 2008
                                   Mar. 2009
                                   Jul. 2009
                                   Sep. 2010
                                   Sep. 2011
                                   Sep. 2012
Crecimiento de LINKED DATA CLOUD


                                   Oct. 2007
                                   Nov. 2007
                                   Feb. 2008
                                   Sep. 2008
                                   Mar. 2009
                                   Jul. 2009
                                   Sep. 2010
                                   Sep. 2011
                                   Sep. 2012
                                   Sep. 2013
Crecimiento de LINKED DATA CLOUD

                                   Oct. 2007
                                   Nov. 2007
                                   Feb. 2008
                                   Sep. 2008
                                   Mar.2009
                                   Jul. 2009
                                   Sep. 2010
                                   Sep. 2011
                                   Sep. 2012
                                   Sep. 2013
                                   Ago.2014
                 Linked Open Data hasta
                 2018-08-22

    Publicacio
           nes
                                          Dominio
      Redes                               cruzado
    Sociales
                                            Geografía
Generado
   por el
  usuario                                     Gobierno


                                                Ciencias de la
                                                vida

                                                    Lingüística


                                                        Medios de
                                                        Comunicación


                                          http://lod-cloud.net/
Ejemplos de LINKED OPEN DATA
Ejemplos de LINKED OPEN DATA
                                                                                     Encuentre la causa de muerte más común para las
                                                                                     personas educadas en universidades peruanas.
                                                                                     Retorne el nombre de la causa de muerte y la cuenta

Las universidades que están       La lista de personajes educados en universidades
en Perú                           peruanas. Retorne el nombre de la persona yel
                                                                                     SELECT ?muerte ( count(?muerte) as ?count )
                                  de la universidad.
SELECT ?nom                                                                          WHERE {
    WHERE {                                                                          ?pe wdt:P31 wd:Q5.
                                  SELECT ?unom ?pnom WHERE {
        ?uni wdt:P31 wd:Q3918                                                        ?uni wdt:P31 wd:Q3918.
.                                     ?uni wdt:P31 wd:Q3918.
                                                                                     ?pe wdt:P69 ?uni.
        ?uni rdfs:label ?nom .        ?uni rdfs:label ?unom.
                                                                                     ?uni wdt:P17 wd:Q419.
        ?uni wdt:P17 wd:Q419 .        ?uni wdt:P17 wd:Q419.
                                                                                     ?uni rdfs:label ?nomuni .
        FILTER(lang(?nom)="es")       ?person wdt:P69 ?uni.
                                                                                     ?pe rdfs:label ?nom.
    }                                 ?person rdfs:label ?pnom.                      ?pe wdt:P570 ?death.
                                      FILTER((LANG(?unom)) = "es")                   ?pe wdt:P509 ?causa.
                                      FILTER((LANG(?pnom)) = "es")                   ?causa rdfs:label ?muerte
                                  }                                                  FILTER(lang (?nom)="es" )
                                                                                     FILTER(lang (?nomuni)="es" )
                                                                                     FILTER(lang (?muerte)="es" )
                                                                                     }

    https://query.wikidata.org                                                       group by ?muerte
                                                                                     order by desc (?count )
                                                                                     limit 10
Ejemplos de LINKED OPEN DATA
Ejemplos de LINKED OPEN DATA
Ejemplos de LINKED OPEN DATA
Ejemplos de LINKED OPEN DATA
Ejemplos de LINKED OPEN DATA




                           http://www.infolobby.cl/#!/inicio
Ejemplos de LINKED OPEN DATA




                               http://www.infolobby.cl/#!/inicio
Ejemplos de LINKED OPEN DATA




                               http://datos.bcn.cl/es/
Linked Government Data:
Linked Government Data:
Life Sciences

E-Commerce
Ejemplos de LINKED OPEN DATA
Aplicaciones de LINKED
                  DATA
Entonces, ¿quién está utilizando estos conjuntos de datos (y para qué)?




                                                                          Oct. 2007
                                                                          Nov. 2007
                                                                          Feb. 2008
                                                                          Sep. 2008
                                                                          Mar. 2009
                                                                          July 2009
                                                                          Sept. 2010
                                                                          Sept. 2011
                                                                          Sept. 2012
                                                                          Sept. 2013
                                                                          Aug. 2014
                                                                          Nov. 2018
Google’s Knowledge Graph
Apple's Siri
IBM’s
EN CONCLUSIÓN
Una área de investigación aquí …
Datos ≠ Datos Relacionales
SEMANTIC WEB
               AGENTS
Agente Inteligente

          Un agente inteligente (o agente racional)
           es una entidad autónoma. que observa y
           actúa sobre un entorno (es decir, es un
          agente) y dirige su actividad hacia el logro
              de objetivos (es decir, es racional).
Agentes Inteligentes
• Están situados en algún entorno y son capaz de percibir
  este ambiente.
• Son capaces de actuar de manera autónoma dentro de
  ese entorno, es decir, pueden decidir sobre una acción y
  ejecutarla sin intervención humana.
• Tienen algún tipo de tarea u objetivo.
• Pueden interactuar con otros agentes.
• Son un tema clásico de Inteligencia Artificial (IA).
Ejemplo de Agente Inteligente
• Un termostato es un agente reactivo muy simple.
• Un agente tiene una forma de percibir su entorno:
   – Un sensor de temperatura.
• Un agente tiene un conjunto limitado de acciones que puede
  realizar:
   – Enciendo la calefacción.
   – Apago la calefacción o.
• Las acciones tienen condiciones previas:
   – ¡Demasiado frío! -> Calefacción encendida.
   – Temperatura OK! -> Calefacción apagada.
• Las condiciones previas dependen del estado del medio
  ambiente como percibido por el agente a través de sus
  sensores.
Descripción de Agente Termostato
• Activación Cada 5 minutos.
  – query Obtenga temperatura ambiente del sensor.
• Acción 1 if (temperatura ambiente <temperatura deseada)
            and (calentándose)
        -> ! Encienda la calefacción.
• Acción 2 if (temperatura ambiente> = temperatura
            deseada) and (calefacción encendida)
        -> ! Apague la calefacción.
Arquitectura simple de un agente




Los agentes simples actúan sólo en función de sus percepciones
actuales.
 Agentes basados en el conocimiento

• Todo el conocimiento del agente está en la lógica del programa.
• Los agentes basados en el conocimiento pueden beneficiarse del
  conocimiento expresado en formas muy generales (una base de
  conocimiento, KB).
• El conocimiento está separado de la lógica del programa.
• Un agente basado en el conocimiento puede agregar nuevos
  conocimientos a la KB, consulta lo que se sabe y hace inferencia.
• Solo especificamos qué sabe el agente y qué objetivos tiene para
  definir el comportamiento del agente.
 Descripción de un agente de taxi basado en el conocimiento

• Activación Cada vez que un cliente ingresa a un destino.
  – query Obtener ubicación actual.
            Encuentra la ruta entre la ubicación actual y el destino.
  Acción 1 if (ubicación actual! = Destino)
          and (la ruta existe)
         -> ! Manejar. Actualiza la ubicación actual.
  Acción 2 if (ubicación actual == destino)
         -> ! Obtenga dinero del cliente.
  Acción 3 if not (la ruta existe)
         -> ! Dígale al cliente que ingrese un nuevo destino.
Agente web semántico



             Un agente es un programa que
            actúa en nombre de una persona
                    u organización.

                                    [W3C]
Definición visionaria: Agente web semántico
    El verdadero poder de la Web Semántica se hará realidad cuando las
    personas creen muchos programas que recopilan contenido web de
    diversos fuentes, procesar la información e intercambiar los resultados
    con otros programas. La efectividad de dichos agentes de software
    aumentará exponencialmente a medida que más contenido web sea
    legible por máquina y los servicios automatizados (incluidos otros
    agentes).

    La Web Semántica promueve esta sinergia: incluso agentes que no
    fueron diseñado expresamente para trabajar juntos puede transferir
    datos entre ellos mismos cuando los datos vienen con semántica.

                                                   Berners-Lee et al. 2001

    Agentes basados en conocimiento VS
    Agentes Web Semánticos
●   Cómo es el conocimiento       ●   La web semántica proporciona
    representado no es                estándares para representando el
    específico.                       conocimiento.
●   Los agentes usan sus          ●   SW Agentes utilizan su conocimiento
    conocimiento para elegir el       para elegir un conjunto de posibles
    acción que los trae más           acciones, pero el usuario decide qué
    cercano a su objetivo y           acción a tomar.
    realizar esa acción           ●   Los agentes de SW son siempre basado
●   Amplia variedad de agente         en el conocimiento y uso Tecnologías
    tipos y usados tecnologías        SW.
¿Qué necesita un agente Web semántico?
●   Una base de conocimiento.
     - RDF, RDFS, OWL
●   La capacidad de hacer preguntas a la base de conocimiento.
     - SPARQL
●   La capacidad de realizar inferencia sobre este conocimiento.
     - Reglas de inferencia RDFS, Razonadores OWL (por ejemplo, cuadros)
●   La capacidad de activarse en un punto determinado.
●   La capacidad de comunicarse con otros agentes.
●   La capacidad de comunicarse con el usuario.
●   Los marcos de agentes (por ejemplo, JADE) no son un área del SW,
     - Los agentes de software se basan en la tecnología existente para los
        agentes de software mejorado con recomendaciones específicas de
        Web semántica.
¿Qué necesita un agente Web semántico?
●   Un agente de recuperación busca conocimiento en la Web Semántica.
●   Un agente personal que utiliza el conocimiento formal de la Web Semántica.
    para reservar vacaciones o citas médicas.
●   Un sistema de múltiples agentes que es capaz de actuar por sí mismo para
    construir y mantener conjuntos de datos vinculados adicionales, por
    ejemplo, actualizar datos basados en Wikipedia.
Descripción de un Agente de Pizza Web Semántica (incompleto)
¿Preguntas?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
