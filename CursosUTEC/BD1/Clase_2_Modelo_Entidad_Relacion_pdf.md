---
curso: BD1
titulo: Clase_2_Modelo_Entidad_Relación
slides: 111
fuente: Clase_2_Modelo_Entidad_Relación.pdf
---

                CLASE 2:
           ENTIDAD-RELACIÓN

        CS2041- Base de Datos I

                                   Ciclo 2024-1




                Brenner Ojeda bojeda@utec.edu.pe
             Teófilo Chambilla - tchambilla@utec.edu.pe

En colaboración Aidan Hogan de la Universidad de Chile (https://aidanhogan.com/)
       CS2041 Base de Datos I
       Teófilo Chambilla Aquino




   Índice
• Resumen clase I.
• Enfoque de la base de datos
• Diseño conceptual: Diagrama Entidad Relación
• Diagrama Entidad - Relación :Relaciones múltiples
• Diagrama Entidad - Relación :Jerarquías de clases
• Restricciones avanzadas
• Entidad Débil
• Entidad Virtual
CS2041
BASE DE DATOS I
CICLO 2024-1


               Entidad Relación

Introducción      Modelo relacional
Resumen: Clase 1

Introducción a base de datos
y DBMS
Componentes
  SISTEMA DE BASE DE DATOS                Usuarios / Programadores


                                    Programas de Aplicación / Consultas

         SOFTWARE DEL SGBD

                                 Software para procesar
                                 Consultas / Programas


                               Software para tener acceso a
                                  los datos almacenados




         Definición de la BD                              Base de Datos
            (Metadatos)                                       almacenada
Modelo
de Datos




           Sección 1.5 | Ramakrishnan / Gehrke
Modelos de cervezas
     Modelo de datos (árbol/jerarquía)
                                               Cervezas


tipo: Ale Ultra                    tipo: Lager                  tipo: Pilsener   tipo: Dark

origen: Lima      origen: Lima origen: Cusco origen: Trujillo origen: Arequipa   origen: Cusco

  Abraxas              Cristal   Cusqueña           Pilsen         Arequipeña     Cusqueña
                   Pilsen Callao Dorada             Trujillo        San Juan       Negra
                    Backus ICE     Roja

grados: 7,0        grados: 4,6   grados: 4,8      grados: 4,6      grados: 4,6   grados: 5,5
Modelo de datos (árbol/jerarquía)
Modelo de datos (grafo)
Modelo de datos (grafo)
Modelo de datos (tabla)
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
Modelo de datos (tabla)
Diferentes modelos de datos tienen
   diferentes fortalezas y debilidades
Pero el modelo (formal) más establecido es
  el del modelo relacional
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
Enfoque
   de
 Base
   de
 Datos



          Capítulo 2 | Ramakrishnan / Gehrke
               Enfoque de base de datos
                                            Obtención y análisis de
                                               requerimientos

                                                 requerimientos
                                                   funcionales


                       Análisis funcional                             Diseño Conceptual


                                                                       Esquema conceptual

Independiente del DBMS

                                                                        Diseño Lógico
Dependiente del DBMS
                 Diseño de programa de
                       aplicación
                                                                       Esquema lógico




                   Implementación de
                                                                        Diseño Físico
                     transacciones             Esquema interno




                  Programas de aplicación
DISEÑO CONCEPTUAL:

      El diagrama
        Entidad
        Relación




                     Capítulo 2 | Ramakrishnan / Gehrke
Una pregunta más general:
Conceptualmente: ¿qué estamos describiendo?
• Caso:
  ○ Una base de datos de una empresa de marketing
    necesita almacenar información de cada compañía
    asociada (identificada por nombre y su valor-acción
    en el mercado), y los productos que fabrica cada
    compañía (identificado por nombre, precio y
    categoría).
Una pregunta más general:
Conceptualmente: ¿qué estamos describiendo?

• Entidades:

• Atributos de entidades:

• Relaciones entre entidades:

Diagramas: Entidad–Relación (ER)
ER: Llaves
(son obligatorias para cada entidad)
ER: Relaciones Binarias
(Dos entidades relacionadas)
ER: Relaciones Binarias
(Dos entidades relacionadas)
ER: Relaciones Binarias
Atributos de Relaciones




                    Relaciones tienen
                 atributos descriptivos
                  (no se pueden usar
                como parte de una llave)
       ER: Relaciones Binarias:
       Multiplicidad de relaciones


• n a n:
    n significa 0 o más

• n a 0 o 1:

• 0 o 1 a n:

• 0 o 1 a 0 o 1:
De hecho,
hay muchas convenciones

• Según Wikipedia:
Pero sólo utilizaremos esta convención:




• Un Producto se fabrica por como máximo una Compañía
• Una Compañía puede fabricar varios Productos


               No significa que hay solo 0 o 1 Compañía.
       Significa que un Producto se fabrica por 0 o 1 Compañía.
Las flechas son difíciles de recordar, pero ...




       Dice que un ciudadano puede tener al máximo un presidente
      (Si consideráramos personas con dos ciudadanías, no aplicaría)
   ER: Relaciones Binarias
   (Dos entidades relacionadas)




                           dni     Siempre a 1
                                   1 a 1 (e.g., dni)
¿Multiplicidad de atributos?     n a 1 (e.g., categoría)
DIAGRAMA ENTIDAD–RELACIÓN:
  RELACIONES MÚLTIPLES




                         Capítulo 2 | Ramakrishnan / Gehrke
ER: Relaciones

¿Cómo se puede modelar un alquiler que involucra
    Personas, Películas y Locales de Videos?
ER: Relaciones Múltiples

¿Cómo se puede modelar un alquiler que involucra
    Personas, Películas y Locales de Videos?
     ER: Relaciones Múltiples

                    ¿Por qué no un atributo?




    Relaciones tienen
 atributos descriptivos
(no se puede usar como
   parte de una llave)



    Si Película no es un “valor simple” (tiene varios atributos)
        y/o si se necesita Película en la llave de la relación
ER: Relaciones Múltiples




        ¿Las multiplicidades?
                                …
ER: Relaciones Múltiples
      ER: Relaciones Múltiples


            ¿Qué significa ésta (exactamente)?




Persona es “una llave”
    de la relación



  Una Persona puede arrendar una sola Película en un solo Local de videos.
    Puede ser que haya varias Locales de videos con varias Películas, etc.
ER: Relaciones Múltiples




  ¿Si quisiéramos decir que una Persona puede alquilar
       varias Películas de varios Locales de videos?     …
ER: Relaciones Múltiples




¿Si quisiéramos decir que una Persona puede alquilar varias
          Películas pero de un solo Local de videos?    Regresaremos.
ER: Relaciones Múltiples

              ¿Es un diagrama ER?




Formalmente no. No tenemos llaves de entidades.
 (Pero a menudo, se omiten los atributos para ser conciso)

   ER: Relaciones Múltiples




¿Se puede hacerlo usando relaciones binarias?
                                                …
ER: Relaciones Múltiples
  ER: Relaciones Múltiples

                    ¿Cuál es preferible?




    Más flexible
                                       Mucho más conciso
(p.ej., restricciones)
ER: Relaciones Múltiples

¿Si quisiéramos decir que una Persona puede alquilar varias
          Películas pero de un solo Local de videos?          …
DER: Relaciones Múltiples:
Arcos Etiquetados (Roles)
DIAGRAMA ENTIDAD–RELACIÓN:
  JERARQUÍAS DE CLASES


                        Capítulo 2 | Ramakrishnan / Gehrke
E–R: Jerarquías de clases
  IsA: es Un(a) en inglés




              … los atributos origen, nombre y tipo
                     se heredan por Vino y Cerveza
E–R: Jerarquías de clases
  Superclases y subclases




                     … Bebida es una superclase
                   … Vino y Cerveza son subclases
                    E–R: Jerarquías de clases
                      Generalización y especialización




Bebida generaliza                                          Vino y Cerveza


 Vino y Cerveza
                                                         especializan Bebida
     DER: Jerarquías de clases
     Restricciones: Solapamiento




• Solapamiento (Overlap): ¿se permite que dos
  subclases contengan la misma entidad?

 ¿Hay Solapamiento aquí?           No (con suerte).
    DER: Jerarquías de clases
    Restricciones: Solapamiento




• Solapamiento (dicho de otra manera)
  – ¿Se puede tener una entidad en A y B o B y C o A y C?
      • ¿Sí? entonces se permite Solapamiento [por defecto]
      • ¿No? entonces no se permite Solapamiento
     DER: Jerarquías de clases
     Restricciones: Solapamiento

                      No Solapamiento.




• No Solapamiento (dicho de manera más matemática) significa que:
       DER: Jerarquías de clases
       Restricciones: Cobertura




• Cobertura (Covering): ¿todas las subclases cubren
  la superclase?

  ¿Hay Cobertura aquí?               No (con suerte).
      DER: Jerarquías de clases
      Restricciones: Cobertura




• Cobertura (dicho de otra manera):
  – ¿Se puede tener una entidad en Z que no está en A, ni B, ni C?
      • ¿Sí? entonces no se puede afirmar cobertura [por defecto]
      • ¿No? entonces se puede afirmar cobertura
       DER: Jerarquías de clases
       Restricciones: Cobertura




• Cobertura (dicho de manera más matemática) significa que:
   DER: Jerarquías de clases
   Restricciones




¿Hay Solapamiento aquí?        Depende (¿datos históricos?)

 ¿Hay Cobertura aquí?           Sí (de alumnos universitarios)
     DER: Jerarquías de clases
     Restricciones




¿Hay Solapamiento aquí?          Sí (p.ej., auxiliar ->TAs)

 ¿Hay Cobertura aquí?            Depende (¿visitantes?)
DIAGRAMA ENTIDAD–RELACIÓN


     Restricciones
      avanzadas




                        Capítulo 2 |Ramakrishnan / Gehrke
ER: Restricciones
(Hemos visto) Multiplicidad de relaciones




                      O?




                                            …
ER: Restricciones
(Hemos visto) Multiplicidad de relaciones

              N                          1




                  Hace referencia a la
                   MULTIPLICIDAD

 ER: Restricciones
 Participación


                                 (1 , )




               Hace referencia a una
               PARTICIPACIÓN TOTAL



… cada profesor trabaja en al menos una universidad
  ER: Restricciones
  Participación + Multiplicidad
                                       MULTIPLICIDAD




                             (1, N)




                     PARTICIPACIÓN




… cada profesor trabaja en al menos una universidad
  ER: Restricciones
  Participación + Multiplicidad


             (0,N)          (1,N)




… cada profesor trabaja en al menos una universidad
ER: Restricciones
Participación + Multiplicidad


          (0,N)          (1,1)




… cada profesor trabaja en una (sola) universidad
ER: Restricciones
Participación + Multiplicidad
          (0,N)          (0,1)



    … cada profesor trabaja en 0 o 1 universidad

          (0,N)          (1,N)



… cada profesor trabaja en 1 o más universidades

          (0,N)          (1,1)



  … cada profesor trabaja en 1 (sola) universidad
DIAGRAMA ENTIDAD–RELACIÓN


      Entidades
       Débiles




                        Capítulo 2 |Ramakrishnan / Gehrke
E–R: Entidades débiles




            ¡No se puede compartir llaves así!
E–R: Entidades débiles




         ¡Se llama una llave parcial!

                   … entidades cuya llave dependa
                        de la llave de otra entidad
E–R: Entidades débiles
  ¿Cuándo se usan? Tres características
     (2) Varias (débiles) a una
       (3) Participación total




                   (1) Dependencia de llave


                          … entidades cuya llave dependa
                               de la llave de otra entidad
 E–R: Entidades débiles
   Un ejemplo más complejo




¿Ahora, si queremos modelar notas de alumnos?
                                           …
        E–R: Entidades débiles
          Una cadena de entidades débiles




dni_alumno




      ¿Y si queremos guardar el nombre del alumno?
                                                 …
        E–R: Entidades débiles
          Una cadena de entidades débiles
                    ¡Repeticiones del nombre del alumno para cada nota!
                                  (Redundante con el DNI)




dni_alumno




                ¿Algún problema aquí?
                                                               …
E–R: Entidades débiles
  Varias dependencias
  ¡No hay llave parcial!




        dni




    ¿Podemos simplificar el modelo?
                                      …
      E–R: Entidades débiles
        Relación con una entidad débil




dni




         ¿Si tenemos notas por pregunta?
                                           …
      E–R: Entidades débiles
        Relación con una entidad débil
                    ¡Un alumno puede tener varias notas para varias
                           preguntas en la misma evaluación!




dni




             ¿Algún problema aquí?
                                                           …
E–R: Entidades débiles
  Varias dependencias y una cadena




      dni




            ¿Algún problema aquí?
                               ¡Todo bien! ☺
DIAGRAMA ENTIDAD–RELACIÓN


      Agregación




                        Capítulo 2 |Ramakrishnan / Gehrke
      E–R: Agregación
        ¿Cuándo se necesita agregación?

            dni




dni




¿Cómo se puede conectar Auxiliar (TA) y Curso?

                                             …
      E–R: Agregación
        ¿Cuándo se necesita agregación?

            dni




dni




 ¿Cómo se puede conectar Profesor y Curso?

                                             …
    E–R: Agregación
      ¿Cuándo se necesita agregación?

            dni




  dni




¿Cómo se puede conectar Auxiliar(TA) y Profesor?

 ¿Están implícitamente conectados por Curso?

      E–R: Agregación
        ¿Cuándo se necesita agregación?

              dni




dni




      ¿Si hay varios Profesores en cada Curso
          con sus propios Auxiliares(TAs)?
                                                …
       E–R: Agregación
         ¿Cuándo se necesita agregación?

              dni




 dni




¿Si queremos decir cuántas horas el Auxiliar(TA)
     trabaja con cada Profesor en el Curso?
                                               …
           E–R: Agregación
             ¿Cuándo se necesita agregación?

                  dni




     dni




¿Si queremos decir el sueldo total del Auxiliar(TA) en el
    Curso (independientemente de los Profesores)?
                                                      …
             E–R: Agregación
               ¿Cuándo se necesita agregación?

                   dni




       dni



… se puede tener relaciones entre relaciones?
                   No directamente, pero …
E–R: Agregación: crear una entidad virtual
  encapsulando una relación
              dni




    dni
   E–R: Agregación:
     ¿Cuándo se usa? Un caso típico
                  dni




                             (1) (1) (0,n) a (0,n)
                                Dependencia    de llave




dni




o(2)
  (2)Atributos
      Atributosdiferentes
                diferentes
E–R: Agregación:
  Mejor ejemplo




                     La relación no está entre
                    relaciones (hay un hueco).
                   La relación conecta Persona
                       y una entidad virtual.

     dni
          E–R: Agregación:
            Mejor ejemplo




                  dni


¿Todavía tiene sentido sin hasta?
      ¡Sí! (Si un local puede tener películas no arrendadas)
         E–R: Agregación:
           Mejor ejemplo




                 dni


¿Todavía tiene sentido sin precio-por-noche?
     ¡Sí! (Si un local puede tener películas no arriendadas)
        E–R: Agregación:
          Mejor ejemplo




                dni


¿Todavía tiene sentido sin ambos atributos?
    ¡Sí! (Si un local puede tener películas no arriendadas)
        E–R: Agregación:
          Mejor ejemplo




               dni


¿Todavía tiene sentido con participación?
                                            ¡No!
       E–R: Agregación:
         Mejor ejemplo




                 dni



¿Todavía tiene sentido con participación?
         ... más conciso con una relación ternaria!
E–R: Relaciones:
  Binaria vs. Agregación vs. Ternaria

             Más flexible




             Más conciso

         ¡Es importante intentar ser tan conciso
       como sea posible (pero no muy conciso)!
       E–R: Relaciones:
          Agregación vs. Binaria + Ternaria




 dni                                 dni




                        Una persona podría arrendar una película de
                              cualquier local, incluso un local
                                  que no tenga la película


¿Cuál es la diferencia entre las dos opciones aquí?
¿PARA QUÉ NECESITAMOS E–R?
       ¿Para qué necesitamos E–R?
• Modelar los requerimientos de un aplicación
  – En una forma menos técnica que usar tablas

• Evitar redundancia / lograr un modelo conciso

• Documentar restricciones conceptuales

• Evitar problemas (p.ej. con llaves)
EJEMPLO:
   VINO, CERVEZA
Modelando vinos y cervezas




    Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
cervezas tienen un precio unitario y una cantidad “en stock” cada día.
    Modelando vinos y cervezas




    Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
cervezas tienen un precio unitario y una cantidad “en stock” cada día.

                                              No tenemos llaves …

    Modelando vinos y cervezas
     (con llaves)




    Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
cervezas tienen un precio unitario y una cantidad “en stock” cada día.

                               ¿Repeticiones de atributos? […]
    Modelando vinos y cervezas
     (con jerarquía de clases)




    Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
cervezas tienen un precio unitario y una cantidad “en stock” cada día.

                                          ¿La llave del Stock? […]
    Modelando vinos y cervezas
     (con entidades débiles)




    Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
cervezas tienen un precio unitario y una cantidad “en stock” cada día.

                ¿Multiplicidades y otras restricciones? […]
       Modelando vinos y cervezas
        (con restricciones)




       Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
   ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
   cervezas tienen un precio unitario y una cantidad “en stock” cada día.

¿Pero cada Bebida tiene que tener un valor de Stock? […]
    Modelando vinos y cervezas
     (con restricciones)




    Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
cervezas tienen un precio unitario y una cantidad “en stock” cada día.

                                                                     Listo.
        Modelando vinos y cervezas
         (pero …)




        Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
    ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
     cervezas tienen un precio unitario y una cantidad “en stock” actual.

¿Qué pasa si quito la fecha (si guardo sólo el stock actual)?
    Modelando vinos y cervezas
     (pero …)                 ¡No hay una llave parcial!




    Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
 cervezas tienen un precio unitario y una cantidad “en stock” actual.

                                                                  ¿Listo?
     Modelando vinos y cervezas
      (ser más conciso)




    Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y
ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y
 cervezas tienen un precio unitario y una cantidad “en stock” actual.
Ejercicio: cadena de pizzerías.
●   Tienen varios locales, los cuales se identifican por su dirección. También se
    registra su número telefónico.
●   Algunos locales son exclusivamente delivery (entrega a domicilio), otros son
    exclusivamente restaurantes (para servir allí mismo), otros cuentan con ambas
    modalidades de servicio.
●   Los locales que ofrecen entrega a domicilio cuentan con un costo fijo de despacho.
●   Los restaurantes cuentan con una capacidad máxima de ocupantes.
●   Un tipo de pizza (margerita, pepperoni, etc.) se identifica por su nombre y
    tamaño (individual, mediana, familiar, etc.).
●   Un tipo de pizza tiene además un booleano que indica si es vegetariano o no.
●   Un tipo de pizza se vende en uno o más locales, cada uno a un precio particular
    (es decir, Dos locales pueden vender la misma pizza a distintos precios.
●   Un local de pizza debe vender uno o más tipos de pizza.
●   Una oferta tiene un código único y un porcentaje de descuento.
●   Cada oferta es válida para un tipo de pizza en un local.
La próxima vez, continuaremos con:
DEL MODELO ENTIDAD–RELACIÓN:
  AL MODELO RELACIONAL


                             Capítulo 3.5 | Ramakrishnan / Gehrke
¿Preguntas?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
