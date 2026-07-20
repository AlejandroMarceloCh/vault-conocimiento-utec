---
curso: BIGDATA
titulo: 12 - Semana 10/Sem10_Base de Datos NoSQL
slides: 31
fuente: 12 - Semana 10/Sem10_Base de Datos NoSQL.pdf
---

Base de datos NoSQL
Mg. Aldo Lezama Benavides


Semana 10
      Objetivo de la sesión

•   Comprender los fundamentos de las bases de datos NoSQL, su origen,

    propósito y diferencias clave frente a los sistemas relacionales

    tradicionales (SQL).

•   Identificar los principales tipos de bases de datos NoSQL (documento,

    clave-valor, columna-familia y grafos), sus características, ventajas y

    limitaciones.

•   Reconocer las aplicaciones prácticas de NoSQL en la nube (GCP),

    explorando ejemplos como Cassandra, MongoDB Atlas y Neo4j para

    distintos casos de uso empresariales.
  Contenido de la sesión

   01.             02.              03.

Base de Datos   Introducción a   Soluciones en
    SQL             NoSQL            GCP
01.   Base de Datos SQL
                                    Base de datos SQL


• En 1970, el Dr. Edgar Codd presentó el modelo
  relacional de bases de datos en su histórico artículo “Un
  modelo relacional de datos para grandes bancos de
  datos compartidos”. Este modelo proponía una forma
  eficiente de organizar y almacenar información en tablas
  estructuradas por filas y columnas.
• Cuatro años más tarde, en 1974, IBM desarrolló el
  Sistema R, el primer proyecto que implementó el modelo
  relacional, y creó SQL como lenguaje estándar para
  interactuar con este tipo de bases de datos.
                                    Base de datos SQL


• Con el tiempo, se establecieron nuevos estándares para
  SQL, y compañías como Oracle, IBM y Microsoft
  desarrollaron sus propios sistemas de gestión de bases
  de datos relacionales (RDBMS), enfocados en ofrecer
  entornos más seguros, eficientes y fáciles de usar.
• Posteriormente, surgieron alternativas de código abierto,
  como MySQL, que democratizaron el acceso a SQL y a
  las bases de datos relacionales. Hoy en día, SQL es una
  tecnología    ampliamente      disponible     tanto   en
  infraestructuras locales como en plataformas en la nube
  como AWS, Azure y Google Cloud.
                  Características de las bases de datos SQL

Las bases de datos SQL se basan en el modelo relacional, el cual
organiza la información en tablas estructuradas e interconectadas
para facilitar el almacenamiento y la consulta de datos. Estas bases
están conformadas principalmente por esquemas y tablas:


• Esquema: define la estructura general de la base de datos,
  especificando las tablas, sus campos, los tipos de datos, los
  valores permitidos y las relaciones entre ellas.
• Tablas: son las unidades fundamentales de una base de datos.
  Cada tabla representa una entidad (por ejemplo, clientes,
  productos o transacciones) y se compone de filas que almacenan
  registros individuales (como un cliente específico) y columnas que
  describen los atributos de esa entidad (como el nombre o el
  correo electrónico).
                                       Ventajas de SQL

SQL proporciona un conjunto estándar de comandos para definir,
consultar, actualizar y administrar datos en un sistema de gestión
de bases de datos relacionales (RDBMS). Las operaciones SQL
clave son SELECT (consulta de datos), INSERT (adición de
nuevos registros), UPDATE (modificación de registros existentes)
y DELETE (eliminación de registros).


Al utilizar estos comandos, SQL se asegura de que se mantienen
las propiedades ACID (Atomicidad, Consistencia, Aislamiento y
Durabilidad). Esto garantiza la fiabilidad y coherencia de los
cambios en la base de datos.
                Características de las bases de datos SQL

El modelo relacional garantiza la integridad y coherencia de los
datos mediante el uso de dos tipos de claves:


• Claves primarias, que identifican de forma única cada registro.
• Claves foráneas, que permiten establecer relaciones entre
  diferentes tablas.


Estas características hacen que las bases de datos SQL sean
ideales para manejar información estructurada de manera
consistente, segura y organizada.
                                           Propiedades ACID

1. Atomicidad: Esta propiedad garantiza que cada conjunto de cambios intentados en una
  base de datos se trate como una unidad de trabajo única e indivisible. O bien se consigna
  toda la unidad en la base de datos, o bien no se consigna ninguna si falla alguna parte de
  la transacción.

  Por ejemplo, una transferencia bancaria:
  María transfiere S/500 a Juan.
  La operación tiene dos pasos:
  • Restar S/500 de la cuenta de María.
  • Sumar S/500 a la cuenta de Juan.
  Si ocurre un error entre los pasos (por ejemplo, se resta el dinero de María, pero no se acredita a Juan), la
  transacción se revierte completamente.
                                         Propiedades ACID

2. Consistencia: Garantiza que una transacción finaliza con la base de datos en un estado
   válido. La base de datos debe satisfacer un conjunto de restricciones de integridad tanto
   antes como después de la transacción.



  Por ejemplo, en la base de datos
  La suma total de saldos del banco debe mantenerse constante después de cualquier transferencia.
  Antes: María (S/1,000) + Juan (S/2,000) = S/3,000
  Después de la transacción: María (S/500) + Juan (S/2,500) = S/3,000
  Si por error el dinero se “duplica” o “pierde” en el proceso, la base de datos violaría la consistencia y
  rechazaría la transacción.
                                          Propiedades ACID

3. Aislamiento: Garantiza que las transacciones simultáneas no provoquen incoherencias
   en la base de datos. Cada transacción parece ejecutarse de forma aislada, sin tener
   conocimiento de otras transacciones en ejecución. El aislamiento evita las interferencias
   entre transacciones y mantiene su integridad.

  Por ejemplo, en la base de datos
  Usuario A consulta el saldo de Juan.
  Usuario B está transfiriendo dinero a Juan en ese mismo momento.
  El sistema garantiza que A vea el saldo final confirmado, no un valor intermedio mientras la transacción de B
  está incompleta.
                                                          Propiedades ACID

4. Durabilidad: La durabilidad garantiza que, una vez consignada una transacción, sus
   efectos persistan incluso en caso de fallo del sistema. Los cambios realizados por la
   transacción se almacenan permanentemente en la base de datos, y sobreviven a las
   caídas del sistema o a los cortes de energía.

  Por ejemplo, en la base de datos
  • María transfiere S/500 a Juan.
  • El sistema se apaga justo después de COMMIT.
  Cuando el sistema se reinicia, la base de datos recordará que la transacción fue completada.
  Esto se logra porque SQL registra cada transacción en el log de transacciones, que se guarda en disco antes
  de confirmarse.



   Estas propiedades fundamentales de las bases de datos SQL garantizan que los sistemas de bases de datos
   sean fiables y coherentes, incluso en caso de sucesos inesperados o fallos del sistema.
                        Sistemas comunes de bases de datos SQL




MySQL es un RDBMS de código abierto, ahora          PostgreSQL es un sistema de base de datos         Un RDBMS propietario de Microsoft, que forma
propiedad de Oracle, conocido por su velocidad,     objeto-relacional   de   código   abierto   con   parte de una suite con ediciones como Express,
fiabilidad y facilidad de uso. MySQL se utiliza a   características avanzadas (por ejemplo, soporte   Standard y Enterprise. Microsoft SQL Server se
menudo en entornos LAMP stack (Linux, Apache,       para funciones y procedimientos personalizados,   integra bien en el ecosistema de Microsoft y es
MySQL, PHP/Python/Perl) para aplicaciones web       así como para consultas complejas, indexación y   adecuado para diversas aplicaciones, desde
pequeñas o medianas.                                transacciones). PostgreSQL es el mejor para       pequeñas empresas hasta grandes compañías.
                                                    aplicaciones a gran escala, almacenamiento de
                                                    datos y datos geoespaciales.
02.   Introducción    a  las
      bases de Datos NoSQL
                     Introducción a las Bases de Datos NoSQL
En la actualidad, las organizaciones y sistemas digitales
generan grandes volúmenes de datos a una velocidad sin
precedentes. Este crecimiento continuo desafía los
modelos       tradicionales   y   exige   nuevas   formas   de
gestionar, almacenar y consultar información. Las bases
de datos NoSQL (“Not Only SQL”) emergen como una
alternativa     a   los   modelos     relacionales   clásicos,
ofreciendo flexibilidad, escalabilidad y adaptabilidad en
contextos que requieren manejar datos variados y de alta
velocidad. NoSQL no significa estrictamente “sin SQL”,
sino “no solo SQL”, refiriendo a una filosofía abierta a
diversos modelos estructurales y lenguajes de consulta
        Motivaciones y Necesidades que Impulsan NoSQL
El crecimiento de internet, las redes sociales y los sistemas distribuidos expuso varias limitaciones de los modelos
relacionales:
• Escalabilidad limitada verticalmente: Los RDBMS suelen escalar incrementando la capacidad de un solo servidor
  (RAM, CPU), un proceso costoso y finalmente limitado.
• Esquemas rígidos: Requieren definir previamente la estructura de los datos; cualquier cambio impone migraciones
  costosas.
• Baja tolerancia a datos no estructurados: Dificultad para manejar imágenes, videos, documentos, logs, sensores.
• Transacciones y ACID imponen overhead: Asegurar atomicidad y consistencia puede penalizar el rendimiento y
  dificultar la escalabilidad.
• Limitantes en alto rendimiento y baja latencia en grandes volúmenes.


NoSQL surge así para abordar necesidades más flexibles, eficientes y escalables ante el auge de Big Data, aplicaciones
web/móviles, IoT y servicios que requieren adaptación rápida ante cambios constantes en los datos.
                                                  Ventajas de NoSQL
Las bases de datos NoSQL ofrecen varias ventajas, con notables puntos
fuertes en escalabilidad, flexibilidad y rendimiento cuando se trata de datos
no estructurados.
Las bases de datos NoSQL ofrecen escalabilidad en forma de escalabilidad
horizontal y elasticidad. Están diseñados para escalar horizontalmente, lo
que permite a las organizaciones manejar cantidades crecientes de datos
añadiendo más servidores a un sistema distribuido. Esto las hace muy
adecuadas para aplicaciones con cargas de trabajo crecientes o
impredecibles.
Muchas bases de datos NoSQL también proporcionan fragmentación
automática y equilibrio de carga, distribuyendo los datos entre varios nodos
para garantizar una utilización eficiente de los recursos y un mejor
rendimiento. Esta capacidad permite que los sistemas se amplíen o
reduzcan dinámicamente en función de la demanda y se conoce como
elasticidad.
                                                  Ventajas de NoSQL

También proporcionan flexibilidad de esquema. Las bases de
datos NoSQL utilizan esquemas dinámicos, lo que permite
flexibilidad en la representación de los datos. Esto significa que los
campos de un registro pueden variar entre distintos documentos,
dando cabida a las diversas y cambiantes estructuras de datos que
suelen encontrarse en las aplicaciones modernas.


También funcionan bien con tipos de datos no estructurados y
semiestructurados, como JSON y XML. Hoy en día, los datos
suelen ser impredecibles, sobre todo cuando son generados por
los usuarios, y NoSQL gestiona bien el almacenamiento de estos
datos.
                                       Tipos de bases de datos NoSQL
                                                   Ventajas de las bases de datos de documentos

                                                   ❖ Sin esquema : no existen limitaciones en cuanto al formato y la estructura del almacenamiento

                                                     de datos. Esto resulta beneficioso, especialmente cuando la base de datos se transforma

                                                     continuamente.

                                                   ❖ Fácil de actualizar : se puede agregar o eliminar información nueva sin cambiar el resto de los

                                                     campos existentes de ese documento específico.
Almacenes de documentos: Utiliza una estructura
                                                   ❖ Rendimiento mejorado : toda la información de un documento se encuentra en ese mismo
flexible, similar a JSON, para almacenar datos
                                                     documento. No es necesario consultar información externa, lo que podría no ser el caso de una
como documentos. Son útiles para manejar datos
complejos y jerárquicos, y admiten esquemas          base de datos relacional, donde el usuario podría tener que solicitar otras tablas.
dinámicos. Se utilizan sobre todo en sistemas de
                                                   Limitaciones de la base de datos de documentos
gestión de contenidos, plataformas de comercio
                                                   ❖ Problemas de comprobación de coherencia : porque los documentos no necesariamente tienen
electrónico y aplicaciones en tiempo real.
                                                     que tener una relación entre sí y dos documentos pueden tener campos diferentes.

                                                   ❖ Problemas de atomicidad : si tenemos que cambiar dos colecciones de documentos,

                                                     necesitaremos ejecutar una consulta separada para cada documento.

                                  Tipos de bases de datos NoSQL
                                                  Ventajas de las bases de datos de clave-valor

                                                  ❖ Simplicidad : la estructura clave-valor es sencilla. La ausencia de tipo de dato facilita

                                                    su uso.

                                                  ❖ Velocidad : el formato de datos simple hace que las operaciones de lectura y escritura

                                                    sean más rápidas.

                                                  Limitaciones de las bases de datos de clave-valor
Base de datos clave-valor: Es la forma más
                                                  ❖ No pueden realizar ningún filtrado en la columna de valor porque el valor devuelto es
sencilla de base de datos NoSQL, en la que cada
                                                    toda la información almacenada en el campo de valor.
unidad de datos se almacena como un par clave-
valor. Estos sistemas son eficaces y útiles en    ❖ Se optimiza únicamente al tener una única clave y valor. Almacenar varios valores
situaciones en las que es necesario acceder
                                                    requeriría un analizador.
rápidamente a muchos datos con tiempos de
                                                  ❖ El valor se actualiza solo en su conjunto, lo que requiere obtener los datos completos,
respuesta rápidos.
                                                    procesarlos y, finalmente, almacenarlos. Esto podría generar problemas de

                                                    rendimiento si el procesamiento requiere mucho tiempo.
                                  Tipos de bases de datos NoSQL

                                                   Ventajas de las bases de datos de gráficos/nodos

                                                   ❖ Son una estructura ágil y flexible.

                                                   ❖ La relación entre los nodos de la base de datos es legible y explícita, por lo que es fácil de

                                                     entender.

                                                   Limitaciones de la base de datos de gráficos/nodos

Base de datos gráfica: Estas bases de datos        ❖ No existe un lenguaje de consulta estandarizado porque cada lenguaje depende de la
representan relaciones entre entidades de datos.     plataforma.
Por tanto, son más útiles en escenarios en los
                                                   ❖ La razón anterior hace que sea difícil encontrar ayuda en línea cuando se enfrenta un
que las relaciones son importantes, como en las
redes sociales o los sistemas de recomendación.      problema.
                                     Tipos de bases de datos NoSQL
                                                      Ventajas de las bases de columnas - familia
                                                      ❖ Alto rendimiento en lecturas y escrituras masivas distribuidas.
                                                      ❖ Escalabilidad horizontal, agregando nodos fácilmente.
                                                      ❖ Esquema flexible, cada fila puede tener distintas columnas.
                                                      ❖ Alta disponibilidad gracias a la replicación entre nodos.
                                                      ❖ Eficientes para series temporales y grandes volúmenes de datos.
                                                      ❖ Soportan consultas rápidas por clave-partición.


Base de datos columna-familia: Las bases de
                                                      Limitaciones de las bases de columnas - familia
datos de la familia de columnas representan los
                                                      ❖ Modelado complejo, requiere diseño cuidadoso de claves.
datos en columnas en lugar de en filas. Son los
                                                      ❖ No garantizan transacciones ACID completas.
mejores para los sistemas distribuidos a gran
                                                      ❖ Usan lenguajes propios (como CQL), no SQL estándar.
escala y los sistemas que leen y escriben a
                                                      ❖ Mayor curva de aprendizaje y administración técnica.
menudo,    como    las   aplicaciones   de   series
                                                      ❖ Mantenimiento complejo en clústeres distribuidos.
temporales y las aplicaciones IoT.
                                                      ❖ No aptas para consultas ad hoc o relaciones complejas.
                                                      ❖ Limitadas para sistemas financieros o críticos
                Cuando se debe usar bases de datos NoSQL
En este entorno competitivo y de rápido crecimiento, las industrias necesitan recopilar la mayor cantidad de datos posible para
alcanzar sus objetivos comerciales. Recopilar datos es una cosa, pero almacenarlos en la infraestructura adecuada es otro
desafío. La dificultad radica en que los datos pueden ser de diferentes tipos, como imágenes, videos, texto y sonido. Usar
bases de datos relacionales para almacenar estos diferentes tipos de datos no siempre es una decisión inteligente. Sin
embargo, la pregunta persiste:
Debería considerar usar NoSQL cuando se encuentre en el siguiente escenario:
• Cambio constante de datos : cuando no sabes cómo crecerá tu sistema o aplicaciones en el futuro, lo que significa que
  es posible que desees agregar nuevos tipos de datos, nuevas funciones, etc.
• Una gran cantidad de datos : cuando su empresa trabaja con grandes cantidades de datos que pueden crecer con el
  tiempo.
• Falta de consistencia : cuando la consistencia de los datos y la integridad total no son su prioridad. Por ejemplo, al
  desarrollar una plataforma de redes sociales para su empresa, que todos los empleados vean sus publicaciones a la vez
  podría no ser un problema.
• Escalabilidad y costo : las bases de datos NoSQL permiten una mayor flexibilidad y pueden controlar los costos a medida
  que cambian sus necesidades de datos.
 Comparativa entre Bases de Datos SQL y NoSQL
      Característica               Bases de datos SQL                  Bases de datos NoSQL
                                                                   Documentos, clave-valor, grafos,
      Modelo de datos              Tablas, filas, columnas
                                                                            columnas

         Esquema                       Fijo y riguroso                    Flexible y opcional


       Escalabilidad              Vertical (mejor hardware)           Horizontal (más servidores)


     Relacionamiento               JOINs, claves foráneas          Embedding, referencias manuales


Transacciones y consistencia               ACID                       BASE / eventual (a menudo)

                                                                 Varía según sistema (JSON, APIs, CQL,
   Lenguaje de consulta                     SQL
                                                                              Cypher, etc.)

                               Datos estructurados, relaciones   Volumen, alta velocidad, flexibilidad,
       Casos de uso
                                         complejas                         datos variados

     Soporte y madurez            Muy alto, estandarizado              Variable, en crecimiento
03.   Soluciones en GCP MarketPlace
MongoDB Atlas

            MongoDB Atlas es la plataforma en la nube oficial y totalmente
            administrada de MongoDB, diseñada para que puedas crear,
            desplegar y escalar bases de datos MongoDB sin tener que
            preocuparte por la infraestructura.
            ¿Qué es MongoDB Atlas?
            MongoDB Atlas es un servicio Database-as-a-Service (DBaaS)
            ofrecido por la empresa MongoDB Inc.
            Te permite ejecutar MongoDB directamente en la nube (sin
            instalar ni administrar servidores), en cualquiera de los
            principales proveedores:
            • Google Cloud Platform (GCP)
            • Amazon Web Services (AWS)
            • Microsoft Azure
            Es decir, puedes elegir dónde alojar tu base de datos, pero Atlas
            se encarga de todo el mantenimiento, seguridad, actualizaciones
            y copias de seguridad.
Apache Cassandra

              ¿Qué es Apache Cassandra?
              Apache Cassandra es una base de datos NoSQL distribuida y
              altamente escalable, diseñada para manejar grandes volúmenes
              de datos en muchos servidores, sin un único punto de falla.Es
              ideal cuando necesitas alta disponibilidad, baja latencia y
              tolerancia a fallos.
              En resumen:
              • Modelo de datos: clave-valor / columna ancha.
              • Arquitectura: sin maestro (peer-to-peer).
              • Escalabilidad: horizontal, agregando nodos.
              • Lenguaje de consulta: CQL (Cassandra Query Language),
                 similar a SQL.
              Se usa mucho en:
              • Telecomunicaciones (registros de llamadas).
              • IoT (sensores y datos de tiempo real).
              • Analítica de grandes volúmenes (logs, clics, telemetría)
Neo4j

        ¿Qué es Neo4j?
        Neo4j es una base de datos NoSQL orientada a grafos,
        diseñada para almacenar y analizar relaciones entre datos de
        manera eficiente.
        A diferencia de las bases relacionales (SQL) o de documentos
        (MongoDB), Neo4j modela los datos como nodos (entidades) y
        relaciones (conexiones), lo que permite consultas muy rápidas
        sobre redes complejas.
                       Conclusiones
      Las bases de datos NoSQL surgieron como respuesta a las limitaciones de
01.   escalabilidad y flexibilidad de los sistemas relacionales, ofreciendo soluciones más
      adecuadas para entornos de Big Data y alta disponibilidad.


      Cada tipo de base de datos NoSQL responde a necesidades específicas de modelado
02.   y rendimiento, por lo que la elección depende del tipo de datos, las relaciones y la
      carga de trabajo.

      Las soluciones NoSQL en la nube, como Cassandra, MongoDB Atlas y Neo4j,

03.   permiten a las organizaciones implementar arquitecturas distribuidas, elásticas y
      seguras, integradas con servicios analíticos modernos en plataformas como Google
      Cloud Platform (GCP).

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
