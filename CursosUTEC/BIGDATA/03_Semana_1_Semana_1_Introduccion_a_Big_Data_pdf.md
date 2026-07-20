---
curso: BIGDATA
titulo: 03 - Semana 1/Semana 1 Introducción a Big Data
slides: 46
fuente: 03 - Semana 1/Semana 1 Introducción a Big Data.pdf
---

INTRODUCCIÓN A
BIG DATA
Mg. Aldo Lezama Benavides

Semana 1
   Objetivo de la sesión

Comprender el concepto de Big Data y su relevancia en la era
digital, identificando sus principales fuentes y aplicaciones en
distintos sectores.
Analizar los retos del Big Data, incluyendo almacenamiento,
procesamiento, complejidad de datos y comunicación de
resultados.
Explicar las características clave del Big Data (5 Vs) y cómo
estas dimensiones determinan la forma en que los datos deben
ser gestionados y analizados.
Entender la arquitectura de Big Data, reconociendo las distintas
capas del flujo de datos desde su origen hasta la generación de
valor.
                       Contenido

 01.        02.               03.            04.          05.

Concepto   Necesidad      Características   Tipología   Arquitectura
01.   Concepto
Concepto
El término Big Data hace referencia a la gestión y análisis de
conjuntos de datos tan grandes, variados y complejos que no
pueden ser tratados con los métodos tradicionales de bases de
datos y análisis. Estos datos provienen de fuentes muy diversas:
registros transaccionales, redes sociales, sensores, imágenes,
videos, audios, dispositivos móviles, entre otros. La importancia de
este campo radica en que, al procesar correctamente estos datos,
es posible obtener conocimiento valioso para la toma de decisiones,    Netflix utiliza Big Data para recomendar películas y series
                                                                       personalizadas según el historial de visualización de cada usuario.
el diseño de estrategias de negocio, el desarrollo científico y la
innovación tecnológica.
Retos
Trabajar con Big Data implica desafíos técnicos y conceptuales. El
primero es el almacenamiento, ya que un solo dispositivo no es
suficiente para guardar la magnitud de información generada cada
segundo. A ello se suma la complejidad, pues los datos no siempre
vienen en un formato uniforme: algunos son estructurados, otros no
tienen estructura y muchos son semi-estructurados. Además, el
procesamiento requiere gran poder computacional, dado que
limpiar, integrar y analizar datos en tal escala demanda eficiencia.
Finalmente, la visualización y comunicación se convierten en un        En 2013, Target predijo que una adolescente estaba embarazada a partir
                                                                       de patrones de compra (vitaminas, cremas sin perfume). Esto generó
                                                                       polémica porque la familia aún no lo sabía, muestra lo complejo y sensible
reto clave: no basta con obtener resultados, también hay que           de manejar datos

expresarlos de manera comprensible para quienes no son expertos.
02.   Necesidad
    Necesidad
La necesidad de Big Data surge a partir de fenómenos característicos
de la era digital:
•   Exponencial crecimiento de los datos: cada segundo se generan
    millones de registros provenientes de redes sociales, sensores,
    transacciones    financieras,   dispositivos   móviles   y   sistemas
    corporativos.
•   Limitaciones de la tecnología tradicional: las bases de datos
    relacionales (SQL) no pueden manejar eficientemente datos no
    estructurados ni volúmenes a escala de petabytes.
    Necesidad

•   Requerimiento de inmediatez: hoy no basta con almacenar la
    información, es necesario procesarla en tiempo real para reaccionar al
    instante (ejemplo: detectar un fraude bancario en segundos).
•   Competitividad empresarial: las organizaciones que aprovechan los
    datos masivos obtienen ventajas en personalización, eficiencia y
    desarrollo de nuevos productos.
En este contexto, Big Data no es una opción, sino una necesidad
estratégica para empresas y gobiernos.
La era digital
Actualmente, ya no se habla de un futuro digital, sino de una
realidad digital en la que vivimos. La producción de datos se da en
actividades cotidianas: al tomar y compartir fotos, comprar en línea,
firmar documentos digitalmente, enviar mensajes, asistir a clases
virtuales o mirar contenido en streaming. Según estadísticas de
2021, existían 4.66 mil millones de usuarios activos en internet, lo
que equivale al 59,5% de la población mundial, y más del 90%
accedía a la red a través de dispositivos móviles. Las redes sociales
son   un   ejemplo   claro:   generan   millones   de publicaciones,
comentarios y archivos compartidos cada día, convirtiéndose en una
                                                                        TikTok genera millones de videos al día. En 2024 se estimaba que los
                                                                        usuarios pasaban más de 95 minutos diarios en la app, lo que se traduce
de las principales fuentes de datos masivos.                            en miles de terabytes de contenido nuevo constantemente.
          La magnitud del dato en tiempo real”
Cada 60 segundos en internet se generan millones de
interacciones digitales:
• Más de 241 millones de emails
• Cerca de 19 millones de mensajes de texto
• 2.4 millones de búsquedas en Google
• 694,000 horas de video vistas en YouTube
• Millones de eventos en redes sociales y apps como Instagram,
  Snapchat y Twitter
03.   Características
 5 Vs de Big Data
La comunidad académica y profesional define el Big Data a partir de una
serie de características conocidas como los “Vs”. Aunque existen versiones
con hasta 10 dimensiones, la base se encuentra en los tres Vs originales. Sin
embargo, con el tiempo se ampliaron las perspectivas y hoy se reconocen al
menos 5 Vs:
• Volumen: la cantidad total de datos generados.
• Variedad: los múltiples formatos y estructuras en los que se presentan.
• Velocidad: la rapidez con que los datos se generan y necesitan ser
  procesados.
• Veracidad: el grado de fiabilidad y calidad de los datos.
• Valor: la utilidad que se obtiene al transformar los datos en conocimiento
  accionable.
- Volumen
El volumen de datos ha crecido a un ritmo exponencial en la última
década. En 2010 la humanidad producía menos de un zettabyte
(ZB) de información. Ocho años después, en 2018, la cifra se
disparó a 33 ZB, y en 2020 alcanzó los 59 ZB, superando con
creces las proyecciones iniciales. Para 2025 se estima superar los
175 ZB, aunque muchos expertos consideran que esta predicción se
quedará   corta.   Este   crecimiento   no   solo   proviene   de   las
interacciones en redes sociales, sino también de la ciencia y la
investigación. Por ejemplo, el Gran Colisionador de Hadrones
(CERN) genera alrededor de 90 petabytes al año, mientras que
telescopios astronómicos producen hasta 20 terabytes por noche de
observación.
- Variedad
La variedad se refiere a los múltiples formatos que adoptan los datos.
Los estructurados se almacenan en bases de datos relacionales, con
tablas y campos claramente definidos. Los semi-estructurados, como
XML o RDF, permiten cierto orden y son útiles para aplicaciones
específicas como el web semántico. Por otro lado, la mayoría de la
información existente es no estructurada: textos libres, correos
electrónicos, imágenes, audios, videos, mensajes de voz, manuscritos
digitalizados, entre otros. Esta diversidad obliga a diseñar sistemas    Un hospital maneja:
                                                                         • Datos estructurados: historias clínicas, resultados de laboratorio.
capaces de integrar e interpretar datos que no siguen un mismo           • Semi-estructurados: archivos XML de equipos médicos.
                                                                         • No estructurados: radiografías, tomografías, notas escritas a mano por
patrón, lo que aumenta la dificultad de análisis y almacenamiento.          médicos.
- Velocidad
La velocidad indica la rapidez con que los datos se producen y
deben ser tratados. En el ámbito financiero, la Bolsa de Nueva York
genera    aproximadamente      1   terabyte   de   información    de
transacciones cada día. En el mundo digital, Meta (Facebook)
procesa alrededor de 500 terabytes diarios provenientes de fotos,
videos, publicaciones y comentarios. En el sector aeronáutico, un
solo motor de avión puede generar 10 terabytes de datos en apenas
30 minutos de vuelo. Si se consideran todos los vuelos diarios a
nivel mundial, la cantidad de información es gigantesca. El reto está
en procesar los datos a la misma velocidad a la que son generados,      Uber procesa en tiempo real millones de viajes simultáneamente para ajustar precios
                                                                        dinámicamente (tarifas más altas en hora punta o cuando hay más demanda).
para poder obtener valor inmediato y no quedar rezagados frente al
flujo de información.
Veracidad
La veracidad en Big Data se refiere al nivel de confianza que se
puede tener en los datos que se recopilan y analizan. A diferencia
de otras dimensiones, no trata de la cantidad ni de la rapidez, sino
de la calidad intrínseca de la información. En entornos masivos, los
datos pueden estar incompletos, duplicados, mal registrados o
incluso ser contradictorios. La gestión de la veracidad implica
establecer procesos de depuración, estandarización y validación
que permitan garantizar que los resultados obtenidos reflejen la
realidad con la mayor precisión posible. Una baja veracidad
compromete la utilidad de cualquier análisis, ya que decisiones        En redes sociales circulan noticias falsas (fake news). Si una empresa de
                                                                       análisis político usara estos datos sin verificar, obtendría conclusiones
críticas podrían basarse en información defectuosa.                    equivocadas.
- Valor
El valor representa la dimensión más estratégica del Big Data, ya
que está vinculada con la capacidad de transformar los datos en un
recurso con impacto práctico y beneficios tangibles. No basta con
recolectar,   almacenar   y   procesar   grandes    volúmenes    de
información: es necesario que esa información, una vez analizada,
aporte beneficios reales, ya sea en términos de eficiencia,
innovación, reducción de riesgos o generación de nuevas
oportunidades. En este sentido, el valor constituye la justificación
principal para invertir en tecnologías y procesos de Big Data, pues
determina si los esfuerzos realizados se traducen efectivamente en
                                                                       Waze transforma la información enviada por
ventajas competitivas o mejoras en la toma de decisiones.              conductores en tiempo real en mapas de tráfico útiles
                                                                       para los usuarios.
Síntesis de los 5 Vs
Los 5 Vs —volumen, variedad, velocidad, veracidad y valor— explican la
naturaleza única del Big Data. No se trata únicamente de manejar
grandes volúmenes o diversidad de formatos, sino también de asegurar
que la información sea confiable y que su análisis produzca beneficios
concretos.   Estas   cinco   dimensiones    hacen   que    los   enfoques
tradicionales sean insuficientes y justifican el uso de nuevas tecnologías
como Hadoop, Spark y bases de datos NoSQL.
04.   Tipologías de Big Data

Tipologías

El Big Data se alimenta de diversas tipologías de datos, que
requieren técnicas diferenciadas de tratamiento:
Datos estructurados: organizados en filas y columnas,
fácilmente     almacenados   en   bases    relacionales   (ej.
transacciones bancarias).
Datos semiestructurados: tienen cierta organización, pero
no cumplen un esquema rígido (ej. XML, JSON, logs de
servidores).
Tipologías

Datos no estructurados: carecen de un formato definido,
representan la mayor parte del Big Data (ej. imágenes,
videos, audios, texto libre en redes sociales).
Datos en streaming: información que fluye en tiempo
real desde sensores, IoT o sistemas de monitoreo.La
tipología determina qué herramientas y arquitecturas se
deben utilizar para almacenarlos y analizarlos.
Datos Estructurados

Definición: Tienen un formato rígido, organizado en filas y
columnas. Se almacenan en bases de datos relacionales
(SQL).
Ejemplos:
•   Registros de ventas en un supermercado (fecha,
    producto, cantidad, precio).
•   Operaciones bancarias (N° de cuenta, monto, fecha, tipo
    de transacción).
•   Inventarios en un ERP.
En la práctica: Una hoja de Excel con 10,000 facturas.
Datos Semiestructurados

Definición: Tienen cierta organización, pero no siguen un
esquema fijo como las tablas.
Ejemplos:
•   Archivos en formato JSON o XML (muy usados en APIs).
•   Logs de servidores web (ej. registros de acceso a una
    página).
•   Correos electrónicos (con campos como remitente,
    asunto, cuerpo del mensaje).
En la práctica: Un archivo JSON de pedidos online con
información diferente según el cliente.
Datos no estructurados

Definición: No siguen un formato definido, difíciles de
almacenar en bases tradicionales. Representan más del
80% de los datos actuales.
Ejemplos:
•   Publicaciones en Twitter, Facebook o TikTok (texto,
    imagen, video).
•   Imágenes médicas (rayos X, resonancias).Grabaciones
    de audio de un call center.
•   Videos de cámaras de seguridad.
En la práctica: Analizar millones de comentarios en redes
sociales para conocer la opinión sobre una marca.
Datos en streaming
Definición: Se generan de manera continua y deben
procesarse casi instantáneamente para ser útiles.
Ejemplos:
•   Sensores de IoT en fábricas o autos (temperatura,
    velocidad, vibración).
•   Transacciones financieras en la bolsa de valores.
•   Señales de GPS en aplicaciones como Uber o Waze.
•   Datos de un smartwatch que mide pulso y pasos cada
    segundo.
En la práctica: Detectar un intento de fraude con tarjeta en
el momento exacto de la compra.
Aplicaciones de Big Data
El Big Data se ha convertido en un eje transformador en múltiples
industrias y sectores. La gran promesa radica en su capacidad para
convertir cantidades masivas de información en inteligencia práctica y
decisiones estratégicas.


• En el sector financiero, se aplica en análisis de riesgo crediticio,
  detección de fraudes en tiempo real y gestión de inversiones
  mediante modelos predictivos.


• En marketing, permite diseñar campañas altamente personalizadas,
  identificando patrones de consumo y preferencias ocultas en millones
  de interacciones.
• En salud, su impacto es revolucionario: análisis de imágenes
  médicas, estudios genómicos y apoyo en diagnósticos complejos
  gracias a modelos de inteligencia artificial entrenados con datos
  clínicos.


• La manufactura lo utiliza para predecir fallas en máquinas,
  reducir tiempos de inactividad y mejorar la calidad de los
  productos.


El Big Data no se limita a un sector en particular, sino que se ha
convertido en una infraestructura transversal de valor para todas
las organizaciones que buscan ser competitivas en la era digital..
05.   Arquitectura de Big Data
Introducción a la arquitectura de Big Data
La arquitectura de Big Data puede entenderse como el mapa que
describe cómo circulan los datos desde que se generan hasta que
producen conocimiento útil. Cada capa u etapa del proceso cumple
una función específica: algunas se encargan de recolectar y
transformar la información, otras de almacenarla y procesarla, y
finalmente existen fases que permiten consultarla y visualizarla de
manera comprensible. Además, a lo largo de todo este flujo existen
dos capas transversales —la seguridad y la monitorización— que
garantizan el correcto funcionamiento y la confiabilidad del sistema.
Flujo general del proceso
El proceso de Big Data no ocurre de manera desordenada, sino                            Arquitectura de Big Data

siguiendo un flujo lógico. Primero, la información nace en las fuentes
                                                                                                                   Capa de visualización
de datos, que pueden ser diversas y heterogéneas. Luego, se
ingiere, se valida y se organiza para asegurar su calidad inicial.                                           Capa de consulta y análisis
                                                                         Capa de    Capa de       Capa de
Posteriormente, atraviesa la capa de conexión, que permite que los       fuentes   Ingestión     Conexión
                                                                                                               Capa de Procesamiento
datos viajen de forma estandarizada hacia los repositorios de
almacenamiento. Una vez guardados, se procesan y analizan para                                                Capa de Almacenamiento

extraer patrones o correlaciones. A partir de allí, los usuarios
                                                                                               Capa de Seguridad
pueden realizar consultas específicas y finalmente recibir la
                                                                                               Capa de Monitoreo
información en forma de visualizaciones, que cierran el ciclo
transformando los datos en conocimiento accesible.
Capa de fuente de datos
                                                                                         Arquitectura de Big Data
Las fuentes de datos son el punto de partida de toda arquitectura de
Big Data. Se trata de los orígenes donde la información es                                                          Capa de visualización

generada, recolectada o registrada antes de entrar en el sistema de
                                                                                                               Capa de consulta y análisis
ingestión. Estas fuentes pueden ser extremadamente heterogéneas:          Capa de    Capa de      Capa de
                                                                          fuentes   Ingestión    Conexión
desde sensores que capturan datos en tiempo real hasta bases de                                                 Capa de Procesamiento

datos   tradicionales   con   registros   históricos.   Comprender   la
                                                                                                               Capa de Almacenamiento
diversidad de estas fuentes resulta esencial, pues determina la
complejidad de los procesos posteriores y las herramientas que se                               Capa de Seguridad

deben utilizar para      gestionarlas. Además, la calidad y          la
                                                                                                Capa de Monitoreo
confiabilidad de los datos dependen en gran medida de la manera
en que estas fuentes están diseñadas y mantenidas.
fuente de datos




                          Redes sociales   Multimedia   E-mail y paginas web
        DBMS relacional
Capa de ingestión
                                                                                      Arquitectura de Big Data
La ingestión es la puerta de entrada del Big Data. Aquí los datos,
provenientes de múltiples orígenes, son recolectados y preparados                                                Capa de visualización

para el análisis. No se trata únicamente de copiar información, sino
                                                                                                            Capa de consulta y análisis
de priorizar lo relevante, filtrar lo redundante y verificar su        Capa de    Capa de      Capa de
                                                                       fuentes   Ingestión    Conexión
consistencia. La ingestión debe ser capaz de manejar tanto flujos en                                         Capa de Procesamiento

tiempo real como grandes cargas históricas, y hacerlo de manera
                                                                                                            Capa de Almacenamiento
robusta y eficiente. Una deficiencia en esta etapa comprometería
todo el proceso, pues cualquier error o ruido que se filtre afectará                         Capa de Seguridad

los resultados obtenidos en fases posteriores.
                                                                                             Capa de Monitoreo
Capa de conexión
                                                                                        Arquitectura de Big Data
Una vez recolectados, los datos pasan por la capa de conexión. En
esta fase se transforman y reorganizan para garantizar que lleguen                                                 Capa de visualización

en un formato adecuado al sistema de almacenamiento. El propósito
                                                                                                              Capa de consulta y análisis
principal es desacoplar los componentes del sistema, asegurando          Capa de    Capa de      Capa de
                                                                         fuentes   Ingestión    Conexión
que la información fluya sin depender estrictamente de la forma en                                             Capa de Procesamiento

que fue generada. Esto otorga flexibilidad y evita cuellos de botella,
                                                                                                              Capa de Almacenamiento
permitiendo que diferentes fuentes puedan integrarse de manera
armónica. La capa de conexión actúa, por tanto, como un puente                                 Capa de Seguridad

que da coherencia a un ecosistema diverso de datos.
                                                                                               Capa de Monitoreo
Capa de almacenamiento
                                                                                        Arquitectura de Big Data
El almacenamiento es el núcleo donde se conserva la información
para su uso presente y futuro. En Big Data, este componente debe                                                   Capa de visualización

estar diseñado para manejar enormes volúmenes de datos, de
                                                                                                              Capa de consulta y análisis
distintos tipos y generados a distintas velocidades. Los sistemas de     Capa de    Capa de      Capa de
                                                                         fuentes   Ingestión    Conexión
almacenamiento pueden ser locales, en la nube o distribuidos en                                                Capa de Procesamiento

múltiples nodos, pero siempre deben asegurar escalabilidad,
                                                                                                              Capa de Almacenamiento
accesibilidad y resiliencia. Una arquitectura deficiente en esta etapa
limita gravemente la capacidad de análisis, pues impide aprovechar                             Capa de Seguridad

de manera efectiva el potencial de los datos recolectados.
                                                                                               Capa de Monitoreo
       Capa de almacenamiento




                                                                        Google Cloud Storage es un servicio de que   es una plataforma segura en la nube que
HDFS    en     Hadoop      como   Amazon S3 como almacenamiento en la   permite almacenar y acceder a datos no       proporciona almacenamiento escalable y
almacenamiento distribuido        nube                                  estructurados en la nube a través de         rentable para el análisis de macrodatos.
                                                                        contenedores llamados buckets.
Capa de Procesamiento y análisis
                                                                                          Arquitectura de Big Data
El procesamiento constituye la fase donde los datos dejan de ser
materia prima bruta y se convierten en información significativa.                                                    Capa de visualización

Implica limpiar errores, normalizar formatos, seleccionar variables
                                                                                                                Capa de consulta y análisis
relevantes y aplicar algoritmos de análisis. Existen diferentes estilos    Capa de    Capa de      Capa de
                                                                           fuentes   Ingestión    Conexión
de procesamiento: el procesamiento por lotes (batch) permite                                                     Capa de Procesamiento

examinar    grandes    cantidades    de   información    histórica;   el
                                                                                                                Capa de Almacenamiento
procesamiento en tiempo real brinda respuestas inmediatas a
medida que se generan los datos; y los sistemas híbridos combinan                                Capa de Seguridad

ambas aproximaciones para ofrecer un balance entre velocidad y
                                                                                                 Capa de Monitoreo
profundidad. De la calidad del procesamiento depende la solidez de
los hallazgos.
Capa de consultas
                                                                                      Arquitectura de Big Data
La capa de consultas brinda la posibilidad de interactuar
directamente con los datos. A través de ella, los usuarios pueden                                                Capa de visualización

formular preguntas específicas que devuelvan métricas, estadísticas
                                                                                                            Capa de consulta y análisis
o reportes de interés. Se trata de una fase más operativa que el       Capa de    Capa de      Capa de
                                                                       fuentes   Ingestión    Conexión
análisis avanzado, pues está pensada para dar soporte inmediato a                                            Capa de Procesamiento

la toma de decisiones cotidianas. La eficacia de esta capa depende
                                                                                                            Capa de Almacenamiento
de la organización previa de los datos y de la capacidad del sistema
para responder de manera ágil y confiable a los requerimientos                               Capa de Seguridad

planteados.
                                                                                             Capa de Monitoreo
Capa de consultas




 Apache Hive para consultas SQL sobre   Presto para consultas interactivas en   Impala como alternativa rápida en
 datos en Hadoop.                       grandes volúmenes.                      entornos Hadoop.

Visualización de resultados
                                                                                           Arquitectura de Big Data
La visualización representa la culminación del proceso de Big Data,
donde la información se traduce en un lenguaje comprensible para                                                      Capa de visualización

las   personas.   Más   allá   de   mostrar   gráficos   atractivos,   la
                                                                                                                 Capa de consulta y análisis
visualización busca transmitir de manera clara patrones, tendencias         Capa de    Capa de      Capa de
                                                                            fuentes   Ingestión    Conexión
y conclusiones que serían imposibles de detectar en el estado                                                     Capa de Procesamiento

original de los datos. Una visualización bien diseñada no solo facilita
                                                                                                                 Capa de Almacenamiento
la interpretación de los resultados, sino que también maximiza el
impacto del análisis al permitir que distintos perfiles de usuarios,                              Capa de Seguridad

técnicos o no técnicos comprendan y utilicen el conocimiento
                                                                                                  Capa de Monitoreo
generado.
Visualización de resultados
Capas transversales
                                                                                     Arquitectura de Big Data
A lo largo de todo el flujo de Big Data operan dos capas
transversales: la seguridad y la monitorización. La seguridad                                                   Capa de visualización

asegura que los datos estén protegidos frente a accesos no
                                                                                                           Capa de consulta y análisis
autorizados, pérdidas o manipulaciones indebidas, garantizando        Capa de    Capa de      Capa de
                                                                      fuentes   Ingestión    Conexión
confidencialidad e integridad. La monitorización, por su parte, se                                          Capa de Procesamiento

ocupa de vigilar la calidad, consistencia y correcto funcionamiento
                                                                                                           Capa de Almacenamiento
de los procesos en cada etapa. Ambas capas no son fases aisladas,
sino dimensiones permanentes que acompañan y sostienen la                                   Capa de Seguridad

arquitectura en su totalidad.
                                                                                            Capa de Monitoreo
Buenas Prácticas
El éxito de un proyecto de Big Data no depende solo de la
tecnología, sino también de la forma en que se gestiona. Es
recomendable definir objetivos claros que guíen el análisis,
implementar la seguridad desde el inicio, y validar constantemente
la calidad de los modelos y los datos. Asimismo, conviene alinear
los resultados con necesidades reales del negocio o de la
organización, de modo que el esfuerzo invertido genere impacto
tangible. Finalmente, las metodologías ágiles permiten mantener
flexibilidad en entornos que cambian rápidamente, lo cual es clave
para aprovechar al máximo el valor del Big Data.
                       Conclusiones

01.   El Big Data es un habilitador estratégico, ya que permite transformar grandes
      volúmenes de datos en conocimiento útil para la toma de decisiones.




02.   La complejidad del Big Data radica en la diversidad y velocidad de los datos, lo que
      exige nuevas tecnologías y enfoques distintos a los tradicionales.




03.   La correcta gestión del ciclo de datos (arquitectura) es fundamental para garantizar
      que la información sea procesada, analizada y utilizada de manera efectiva.




04.   El valor del Big Data no está en los datos en sí, sino en su aplicación, es decir, en
      cómo se traducen en ventajas competitivas, eficiencia operativa e innovación.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
