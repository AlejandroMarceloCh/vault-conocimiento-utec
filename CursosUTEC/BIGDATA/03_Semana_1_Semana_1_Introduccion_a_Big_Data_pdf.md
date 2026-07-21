---
curso: BIGDATA
titulo: 03 - Semana 1/Semana 1 Introducción a Big Data
slides: 46
fuente: 03 - Semana 1/Semana 1 Introducción a Big Data.pdf
---

## Slide 1

Portada (decorativa). Fondo cian con render de un edificio de concreto de UTEC.

**INTRODUCCIÓN A BIG DATA**

Mg. Aldo Lezama Benavides
Semana 1

## Slide 2

### Objetivo de la sesión

(Texto dentro de un recuadro con esquinas tipo corchete.)

- **Comprender** el concepto de Big Data y su relevancia en la era digital, identificando sus principales fuentes y aplicaciones en distintos sectores.
- **Analizar** los retos del Big Data, incluyendo almacenamiento, procesamiento, complejidad de datos y comunicación de resultados.
- **Explicar** las características clave del Big Data (5 Vs) y cómo estas dimensiones determinan la forma en que los datos deben ser gestionados y analizados.
- **Entender** la arquitectura de Big Data, reconociendo las distintas capas del flujo de datos desde su origen hasta la generación de valor.

## Slide 3

### Contenido

Cinco bloques numerados en fila, cada uno dentro de corchetes:

| 01. | 02. | 03. | 04. | 05. |
|-----|-----|-----|-----|-----|
| Concepto | Necesidad | Características | Tipología | Arquitectura |

## Slide 4

Divisor de sección. Número grande **01.** dentro de corchetes, icono de portapapeles, y título **Concepto**.

## Slide 5

### Concepto

El término Big Data hace referencia a la gestión y análisis de conjuntos de datos tan grandes, variados y complejos que no pueden ser tratados con los métodos tradicionales de bases de datos y análisis. Estos datos provienen de fuentes muy diversas: registros transaccionales, redes sociales, sensores, imágenes, videos, audios, dispositivos móviles, entre otros. La importancia de este campo radica en que, al procesar correctamente estos datos, es posible obtener conocimiento valioso para la toma de decisiones, el diseño de estrategias de negocio, el desarrollo científico y la innovación tecnológica.

**Visual (captura de dashboard):** A la derecha, screenshot de un dashboard analítico de Netflix (fondo oscuro, marca NETFLIX en rojo). Muestra paneles tipo Power BI: tablas "Watching Type" y "Year Analysis" (Episodes 1321, Movies 655, Total 1976; años 2018=396, 2017=1063, 2016=517), gráficos de barras "Watching over Years / Weeks / Months", un gráfico de dona "Count of Type by Type" (0.66K 33.15% / 1.32K 66.85%), tabla "Seasons Analysis", y medidores circulares (gauges) "Movies Watched 655", "Season Watched 789", "Sub Series Watched 11", "Episode Watched 1,321".

*Pie:* Netflix utiliza Big Data para recomendar películas y series personalizadas según el historial de visualización de cada usuario.

## Slide 6

### Retos

Trabajar con Big Data implica desafíos técnicos y conceptuales. El primero es el **almacenamiento**, ya que un solo dispositivo no es suficiente para guardar la magnitud de información generada cada segundo. A ello se suma la **complejidad**, pues los datos no siempre vienen en un formato uniforme: algunos son estructurados, otros no tienen estructura y muchos son semi-estructurados. Además, el **procesamiento** requiere gran poder computacional, dado que limpiar, integrar y analizar datos en tal escala demanda eficiencia. Finalmente, la **visualización** y **comunicación** se convierten en un reto clave: no basta con obtener resultados, también hay que expresarlos de manera comprensible para quienes no son expertos.

**Visual:** Foto de una mujer embarazada (vestido azul) junto al logo circular rojo de TARGET.

*Pie:* En 2013, Target predijo que una adolescente estaba embarazada a partir de patrones de compra (vitaminas, cremas sin perfume). Esto generó polémica porque la familia aún no lo sabía, muestra lo complejo y sensible de manejar datos.

## Slide 7

Divisor de sección. Número grande **02.** dentro de corchetes, icono de portapapeles, y título **Necesidad**.

## Slide 8

### Necesidad

La necesidad de Big Data surge a partir de fenómenos característicos de la era digital:

- **Exponencial crecimiento de los datos:** cada segundo se generan millones de registros provenientes de redes sociales, sensores, transacciones financieras, dispositivos móviles y sistemas corporativos.
- **Limitaciones de la tecnología tradicional:** las bases de datos relacionales (SQL) no pueden manejar eficientemente datos no estructurados ni volúmenes a escala de petabytes.

**Visual:** Foto de un circuito impreso/placa electrónica azul con un chip central rotulado "BIG DATA".

## Slide 9

### Necesidad (cont.)

- **Requerimiento de inmediatez:** hoy no basta con almacenar la información, es necesario procesarla en tiempo real para reaccionar al instante (ejemplo: detectar un fraude bancario en segundos).
- **Competitividad empresarial:** las organizaciones que aprovechan los datos masivos obtienen ventajas en personalización, eficiencia y desarrollo de nuevos productos.

En este contexto, Big Data no es una opción, sino una necesidad estratégica para empresas y gobiernos.

**Visual:** Misma foto del circuito azul con chip "BIG DATA".

## Slide 10

### La era digital

Actualmente, ya no se habla de un futuro digital, sino de una realidad digital en la que vivimos. La producción de datos se da en actividades cotidianas: al tomar y compartir fotos, comprar en línea, firmar documentos digitalmente, enviar mensajes, asistir a clases virtuales o mirar contenido en streaming. Según estadísticas de 2021, existían 4.66 mil millones de usuarios activos en internet, lo que equivale al 59,5% de la población mundial, y más del 90% accedía a la red a través de dispositivos móviles. Las redes sociales son un ejemplo claro: generan millones de publicaciones, comentarios y archivos compartidos cada día, convirtiéndose en una de las principales fuentes de datos masivos.

**Visual:** Foto de una pantalla de smartphone con iconos de apps (Instagram, Messenger, Twitter, Facebook, Google), con una lupa que amplía el icono de **TikTok**.

*Pie:* TikTok genera millones de videos al día. En 2024 se estimaba que los usuarios pasaban más de 95 minutos diarios en la app, lo que se traduce en miles de terabytes de contenido nuevo constantemente.

## Slide 11

### La magnitud del dato en tiempo real"

**Visual (infografía):** Gráfico circular tipo rueda "THE INTERNET IN 2023 EVERY MINUTE" con un cronómetro "60 SECONDS" al centro (creado por eDiscovery Today & LTMG). Cada segmento = una plataforma en 60 s:
- App Store: 22,831 visits to ChatGPT
- 271,309 iOS & Android app downloads
- 3.02M photos created with smartphones
- 6.94M emoji sent
- 11,834 chats on Microsoft Teams
- 34,247 Slack messages
- 6.3M total Zoom meeting minutes
- 11,035 fake accounts removed (Facebook)
- 10.4M viewing minutes (Instagram)
- 3.47M snaps created (Snapchat)
- 347,222 tweets
- 694,000 video hours viewed (YouTube)
- 2.4M Google searches
- 18.8M text messages sent
- 241.2M emails sent

Texto lateral:

Cada 60 segundos en internet se generan millones de interacciones digitales:
- Más de 241 millones de emails
- Cerca de 19 millones de mensajes de texto
- 2.4 millones de búsquedas en Google
- 694,000 horas de video vistas en YouTube
- Millones de eventos en redes sociales y apps como Instagram, Snapchat y Twitter

## Slide 12

Divisor de sección. Número grande **03.** dentro de corchetes, icono de portapapeles, y título **Características**.

## Slide 13

### 5 Vs de Big Data

La comunidad académica y profesional define el Big Data a partir de una serie de características conocidas como los "Vs". Aunque existen versiones con hasta 10 dimensiones, la base se encuentra en los tres Vs originales. Sin embargo, con el tiempo se ampliaron las perspectivas y hoy se reconocen al menos **5 Vs**:

- **Volumen:** la cantidad total de datos generados.
- **Variedad:** los múltiples formatos y estructuras en los que se presentan.
- **Velocidad:** la rapidez con que los datos se generan y necesitan ser procesados.
- **Veracidad:** el grado de fiabilidad y calidad de los datos.
- **Valor:** la utilidad que se obtiene al transformar los datos en conocimiento accionable.

**Visual (diagrama):** Infografía en abanico "5 V's OF DATA" con iconos, distribuidos alrededor de un centro:
- VOLUME – Amount of Data
- VARIETY – Diversity of Data
- VELOCITY – Speed of Data Generation
- VERACITY – Accuracy of Data
- VALUE – Worth of Data

## Slide 14

### - Volumen

El volumen de datos ha crecido a un ritmo exponencial en la última década. En 2010 la humanidad producía menos de un zettabyte (ZB) de información. Ocho años después, en 2018, la cifra se disparó a 33 ZB, y en 2020 alcanzó los 59 ZB, superando con creces las proyecciones iniciales. Para 2025 se estima superar los 175 ZB, aunque muchos expertos consideran que esta predicción se quedará corta. Este crecimiento no solo proviene de las interacciones en redes sociales, sino también de la ciencia y la investigación. Por ejemplo, el Gran Colisionador de Hadrones (CERN) genera alrededor de 90 petabytes al año, mientras que telescopios astronómicos producen hasta 20 terabytes por noche de observación.

**Visual:** Ilustración futurista de una persona de espaldas frente a un panel/muro digital lleno de gráficos, dashboards y visualizaciones azules.

## Slide 15

### - Variedad

La variedad se refiere a los múltiples formatos que adoptan los datos. Los estructurados se almacenan en bases de datos relacionales, con tablas y campos claramente definidos. Los semi-estructurados, como XML o RDF, permiten cierto orden y son útiles para aplicaciones específicas como el web semántico. Por otro lado, la mayoría de la información existente es no estructurada: textos libres, correos electrónicos, imágenes, audios, videos, mensajes de voz, manuscritos digitalizados, entre otros. Esta diversidad obliga a diseñar sistemas capaces de integrar e interpretar datos que no siguen un mismo patrón, lo que aumenta la dificultad de análisis y almacenamiento.

**Visual (diagrama):** Infografía azul "Solución Hospitalaria Virtual" en el centro, conectada por flechas a nodos con iconos: Dispositivos médicos inteligentes conectados (signos vitales del paciente, datos de consumo de medicamentos), Registros electrónicos de salud (síntomas, signos vitales, consultas en línea; historial de salud del paciente), Sistema de gestión de consultorios (chequeos programados; horarios del equipo médico, facturas), Software de imágenes médicas (imágenes de diagnóstico), Sistema de información del laboratorio (resultados de pruebas).

*Pie:* Un hospital maneja:
- Datos estructurados: historias clínicas, resultados de laboratorio.
- Semi-estructurados: archivos XML de equipos médicos.
- No estructurados: radiografías, tomografías, notas escritas a mano por médicos.

## Slide 16

### - Velocidad

La velocidad indica la rapidez con que los datos se producen y deben ser tratados. En el ámbito financiero, la Bolsa de Nueva York genera aproximadamente 1 terabyte de información de transacciones cada día. En el mundo digital, Meta (Facebook) procesa alrededor de 500 terabytes diarios provenientes de fotos, videos, publicaciones y comentarios. En el sector aeronáutico, un solo motor de avión puede generar 10 terabytes de datos en apenas 30 minutos de vuelo. Si se consideran todos los vuelos diarios a nivel mundial, la cantidad de información es gigantesca. El reto está en procesar los datos a la misma velocidad a la que son generados, para poder obtener valor inmediato y no quedar rezagados frente al flujo de información.

**Visual:** Foto de una persona conduciendo (manos en el volante de un Volkswagen) sosteniendo un smartphone con la app **Uber** abierta.

*Pie:* Uber procesa en tiempo real millones de viajes simultáneamente para ajustar precios dinámicamente (tarifas más altas en hora punta o cuando hay más demanda).

## Slide 17

### Veracidad

La veracidad en Big Data se refiere al nivel de confianza que se puede tener en los datos que se recopilan y analizan. A diferencia de otras dimensiones, no trata de la cantidad ni de la rapidez, sino de la calidad intrínseca de la información. En entornos masivos, los datos pueden estar incompletos, duplicados, mal registrados o incluso ser contradictorios. La gestión de la veracidad implica establecer procesos de depuración, estandarización y validación que permitan garantizar que los resultados obtenidos reflejen la realidad con la mayor precisión posible. Una baja veracidad compromete la utilidad de cualquier análisis, ya que decisiones críticas podrían basarse en información defectuosa.

**Visual:** Foto conceptual: una mano maneja como marioneta a un maniquí de madera dentro de un televisor antiguo, con un cartel "FAKE NEWS".

*Pie:* En redes sociales circulan noticias falsas (fake news). Si una empresa de análisis político usara estos datos sin verificar, obtendría conclusiones equivocadas.

## Slide 18

### - Valor

El valor representa la dimensión más estratégica del Big Data, ya que está vinculada con la capacidad de transformar los datos en un recurso con impacto práctico y beneficios tangibles. No basta con recolectar, almacenar y procesar grandes volúmenes de información: es necesario que esa información, una vez analizada, aporte beneficios reales, ya sea en términos de eficiencia, innovación, reducción de riesgos o generación de nuevas oportunidades. En este sentido, el valor constituye la justificación principal para invertir en tecnologías y procesos de Big Data, pues determina si los esfuerzos realizados se traducen efectivamente en ventajas competitivas o mejoras en la toma de decisiones.

**Visual:** Captura de la app **Waze** (mapa de Buenos Aires con barra "¿A dónde vamos?", iconos de tráfico, alertas y rutas rojas sobre las calles).

*Pie:* Waze transforma la información enviada por conductores en tiempo real en mapas de tráfico útiles para los usuarios.

## Slide 19

### Síntesis de los 5 Vs

Los 5 Vs —volumen, variedad, velocidad, veracidad y valor— explican la naturaleza única del Big Data. No se trata únicamente de manejar grandes volúmenes o diversidad de formatos, sino también de asegurar que la información sea confiable y que su análisis produzca beneficios concretos. Estas cinco dimensiones hacen que los enfoques tradicionales sean insuficientes y justifican el uso de nuevas tecnologías como Hadoop, Spark y bases de datos NoSQL.

**Visual:** Icono circular amarillo con un engranaje azul central rodeado de 4 nodos morados y flechas hacia el centro.

## Slide 20

Divisor de sección. Número grande **04.** dentro de corchetes, icono de portapapeles, y título **Tipologías de Big Data**.

## Slide 21

### Tipologías

El Big Data se alimenta de diversas tipologías de datos, que requieren técnicas diferenciadas de tratamiento:

- **Datos estructurados:** organizados en filas y columnas, fácilmente almacenados en bases relacionales (ej. transacciones bancarias).
- **Datos semiestructurados:** tienen cierta organización, pero no cumplen un esquema rígido (ej. XML, JSON, logs de servidores).

**Visual:** Diagrama radial (fondo azul oscuro) con la silueta de un usuario al centro conectada por líneas punteadas a iconos de fuentes: Facebook, EMAIL, Twitter, Búsquedas en Internet, Blogger, Documentos (Google Drive), YouTube e Instagram.

## Slide 22

### Tipologías (cont.)

- **Datos no estructurados:** carecen de un formato definido, representan la mayor parte del Big Data (ej. imágenes, videos, audios, texto libre en redes sociales).
- **Datos en streaming:** información que fluye en tiempo real desde sensores, IoT o sistemas de monitoreo.

La tipología determina qué herramientas y arquitecturas se deben utilizar para almacenarlos y analizarlos.

**Visual:** Mismo diagrama radial de fuentes (Facebook, Email, Twitter, Búsquedas, Blogger, Documentos, YouTube, Instagram) alrededor de un usuario central.

## Slide 23

### Datos Estructurados

**Definición:** Tienen un formato rígido, organizado en filas y columnas. Se almacenan en bases de datos relacionales (SQL).

**Ejemplos:**
- Registros de ventas en un supermercado (fecha, producto, cantidad, precio).
- Operaciones bancarias (N° de cuenta, monto, fecha, tipo de transacción).
- Inventarios en un ERP.

**En la práctica:** Una hoja de Excel con 10,000 facturas.

**Visual (diagrama):** Infografía "DATOS" con tres círculos de puntos que ilustran el grado de orden: **Estructurados** (azul, puntos en cuadrícula ordenada), **Semiestructurados** (amarillo, cuadrícula parcial), **No Estructurados** (rojo, puntos dispersos sin orden).

## Slide 24

### Datos Semiestructurados

**Definición:** Tienen cierta organización, pero no siguen un esquema fijo como las tablas.

**Ejemplos:**
- Archivos en formato JSON o XML (muy usados en APIs).
- Logs de servidores web (ej. registros de acceso a una página).
- Correos electrónicos (con campos como remitente, asunto, cuerpo del mensaje).

**En la práctica:** Un archivo JSON de pedidos online con información diferente según el cliente.

**Visual:** Misma infografía "DATOS" de tres círculos (Estructurados / Semiestructurados / No Estructurados).

## Slide 25

### Datos no estructurados

**Definición:** No siguen un formato definido, difíciles de almacenar en bases tradicionales. Representan más del 80% de los datos actuales.

**Ejemplos:**
- Publicaciones en Twitter, Facebook o TikTok (texto, imagen, video).
- Imágenes médicas (rayos X, resonancias). Grabaciones de audio de un call center.
- Videos de cámaras de seguridad.

**En la práctica:** Analizar millones de comentarios en redes sociales para conocer la opinión sobre una marca.

**Visual:** Misma infografía "DATOS" de tres círculos (Estructurados / Semiestructurados / No Estructurados).

## Slide 26

### Datos en streaming

**Definición:** Se generan de manera continua y deben procesarse casi instantáneamente para ser útiles.

**Ejemplos:**
- Sensores de IoT en fábricas o autos (temperatura, velocidad, vibración).
- Transacciones financieras en la bolsa de valores.
- Señales de GPS en aplicaciones como Uber o Waze.
- Datos de un smartwatch que mide pulso y pasos cada segundo.

**En la práctica:** Detectar un intento de fraude con tarjeta en el momento exacto de la compra.

**Visual:** Misma infografía "DATOS" de tres círculos (Estructurados / Semiestructurados / No Estructurados).

## Slide 27

### Aplicaciones de Big Data

El Big Data se ha convertido en un eje transformador en múltiples industrias y sectores. La gran promesa radica en su capacidad para convertir cantidades masivas de información en inteligencia práctica y decisiones estratégicas.

- En el sector **financiero**, se aplica en análisis de riesgo crediticio, detección de fraudes en tiempo real y gestión de inversiones mediante modelos predictivos.
- En **marketing**, permite diseñar campañas altamente personalizadas, identificando patrones de consumo y preferencias ocultas en millones de interacciones.

**Visual:** Tres fotos apiladas a la derecha: personas analizando gráficos financieros en papel; una lupa sobre código binario con la palabra "FRAUD" resaltada en rojo; y una nube de palabras "MARKETING CAMPAIGN" (strategy, plan, promotion, budget, goals...) con una mano marcando con lapicero.

## Slide 28

### Aplicaciones de Big Data (cont.)

- En **salud**, su impacto es revolucionario: análisis de imágenes médicas, estudios genómicos y apoyo en diagnósticos complejos gracias a modelos de inteligencia artificial entrenados con datos clínicos.
- La **manufactura** lo utiliza para predecir fallas en máquinas, reducir tiempos de inactividad y mejorar la calidad de los productos.

El Big Data no se limita a un sector en particular, sino que se ha convertido en una infraestructura transversal de valor para todas las organizaciones que buscan ser competitivas en la era digital.

**Visual:** Dos fotos: brazos robóticos en una línea de ensamblaje automotriz con un operario usando una tablet; y un médico con bata sosteniendo un dispositivo, con un electrocardiograma/corazón dibujado.

## Slide 29

Divisor de sección. Número grande **05.** dentro de corchetes, icono de portapapeles, y título **Arquitectura de Big Data**.

## Slide 30

### Introducción a la arquitectura de Big Data

La arquitectura de Big Data puede entenderse como el mapa que describe cómo circulan los datos desde que se generan hasta que producen conocimiento útil. Cada capa u etapa del proceso cumple una función específica: algunas se encargan de recolectar y transformar la información, otras de almacenarla y procesarla, y finalmente existen fases que permiten consultarla y visualizarla de manera comprensible. Además, a lo largo de todo este flujo existen dos capas transversales —la seguridad y la monitorización— que garantizan el correcto funcionamiento y la confiabilidad del sistema.

**Visual:** Ilustración isométrica en escala de grises: un panel central de dashboards conectado por líneas a varias plataformas/personas trabajando (representa un ecosistema de datos).

## Slide 31

### Flujo general del proceso

El proceso de Big Data no ocurre de manera desordenada, sino siguiendo un flujo lógico. Primero, la información nace en las fuentes de datos, que pueden ser diversas y heterogéneas. Luego, se ingiere, se valida y se organiza para asegurar su calidad inicial. Posteriormente, atraviesa la capa de conexión, que permite que los datos viajen de forma estandarizada hacia los repositorios de almacenamiento. Una vez guardados, se procesan y analizan para extraer patrones o correlaciones. A partir de allí, los usuarios pueden realizar consultas específicas y finalmente recibir la información en forma de visualizaciones, que cierran el ciclo transformando los datos en conocimiento accesible.

**Visual (diagrama de arquitectura):** Diagrama "Arquitectura de Big Data" con bloques naranjas. Tres columnas verticales a la izquierda (**Capa de fuentes → Capa de Ingestión → Capa de Conexión**) con flechas rojas horizontales que avanzan de una a otra. A la derecha, una pila apilada verticalmente con flechas rojas bidireccionales entre niveles: de abajo hacia arriba **Capa de Almacenamiento → Capa de Procesamiento → Capa de consulta y análisis → Capa de visualización**. Abajo, dos bandas horizontales transversales que cruzan todo: **Capa de Seguridad** y **Capa de Monitoreo**.

## Slide 32

### Capa de fuente de datos

Las fuentes de datos son el punto de partida de toda arquitectura de Big Data. Se trata de los orígenes donde la información es generada, recolectada o registrada antes de entrar en el sistema de ingestión. Estas fuentes pueden ser extremadamente heterogéneas: desde sensores que capturan datos en tiempo real hasta bases de datos tradicionales con registros históricos. Comprender la diversidad de estas fuentes resulta esencial, pues determina la complejidad de los procesos posteriores y las herramientas que se deben utilizar para gestionarlas. Además, la calidad y la confiabilidad de los datos dependen en gran medida de la manera en que estas fuentes están diseñadas y mantenidas.

**Visual (diagrama):** Misma "Arquitectura de Big Data", con la **Capa de fuentes** resaltada (naranja con borde rojo) y las demás capas en gris atenuado.

## Slide 33

### fuente de datos

**Visual (galería de iconos):** Cuatro tipos de fuentes ilustradas en fila:
- **DBMS relacional:** diagrama de tablas conectadas por relaciones (Table–Table con "Relationship").
- **Redes sociales:** collage de logos (X/Twitter, YouTube, Facebook, Instagram, TikTok, WhatsApp, LinkedIn, Snapchat, Spotify, Reddit, Pinterest, Telegram, Behance, digg, etc.).
- **Multimedia:** panal hexagonal "Multimedia" con iconos de video, audio, texto (Aa) e imágenes.
- **E-mail y páginas web:** ilustración de un sobre EMAIL con flecha hacia una laptop mostrando una página web.

## Slide 34

### Capa de ingestión

La ingestión es la puerta de entrada del Big Data. Aquí los datos, provenientes de múltiples orígenes, son recolectados y preparados para el análisis. No se trata únicamente de copiar información, sino de priorizar lo relevante, filtrar lo redundante y verificar su consistencia. La ingestión debe ser capaz de manejar tanto flujos en tiempo real como grandes cargas históricas, y hacerlo de manera robusta y eficiente. Una deficiencia en esta etapa comprometería todo el proceso, pues cualquier error o ruido que se filtre afectará los resultados obtenidos en fases posteriores.

**Visual (diagrama):** "Arquitectura de Big Data" con **Capa de fuentes** y **Capa de Ingestión** resaltadas (naranja/borde rojo); el resto en gris.

## Slide 35

### Capa de conexión

Una vez recolectados, los datos pasan por la capa de conexión. En esta fase se transforman y reorganizan para garantizar que lleguen en un formato adecuado al sistema de almacenamiento. El propósito principal es desacoplar los componentes del sistema, asegurando que la información fluya sin depender estrictamente de la forma en que fue generada. Esto otorga flexibilidad y evita cuellos de botella, permitiendo que diferentes fuentes puedan integrarse de manera armónica. La capa de conexión actúa, por tanto, como un puente que da coherencia a un ecosistema diverso de datos.

**Visual (diagrama):** "Arquitectura de Big Data" con **Capa de fuentes**, **Capa de Ingestión** y **Capa de Conexión** resaltadas; el resto en gris.

## Slide 36

### Capa de almacenamiento

El almacenamiento es el núcleo donde se conserva la información para su uso presente y futuro. En Big Data, este componente debe estar diseñado para manejar enormes volúmenes de datos, de distintos tipos y generados a distintas velocidades. Los sistemas de almacenamiento pueden ser locales, en la nube o distribuidos en múltiples nodos, pero siempre deben asegurar escalabilidad, accesibilidad y resiliencia. Una arquitectura deficiente en esta etapa limita gravemente la capacidad de análisis, pues impide aprovechar de manera efectiva el potencial de los datos recolectados.

**Visual (diagrama):** "Arquitectura de Big Data" con las tres columnas de la izquierda y la **Capa de Almacenamiento** resaltadas; el resto en gris.

## Slide 37

### Capa de almacenamiento (herramientas)

**Visual (galería de logos):** Cuatro tecnologías de almacenamiento:
- **Hadoop HDFS:** HDFS en Hadoop como almacenamiento distribuido.
- **Amazon S3:** Amazon S3 como almacenamiento en la nube.
- **Google Cloud Storage:** servicio que permite almacenar y acceder a datos no estructurados en la nube a través de contenedores llamados buckets.
- **Azure Data Lake:** es una plataforma segura en la nube que proporciona almacenamiento escalable y rentable para el análisis de macrodatos.

## Slide 38

### Capa de Procesamiento y análisis

El procesamiento constituye la fase donde los datos dejan de ser materia prima bruta y se convierten en información significativa. Implica limpiar errores, normalizar formatos, seleccionar variables relevantes y aplicar algoritmos de análisis. Existen diferentes estilos de procesamiento: el procesamiento por lotes (batch) permite examinar grandes cantidades de información histórica; el procesamiento en tiempo real brinda respuestas inmediatas a medida que se generan los datos; y los sistemas híbridos combinan ambas aproximaciones para ofrecer un balance entre velocidad y profundidad. De la calidad del procesamiento depende la solidez de los hallazgos.

**Visual (diagrama):** "Arquitectura de Big Data" con las tres columnas izquierdas, la **Capa de Procesamiento** y la **Capa de Almacenamiento** resaltadas; el resto en gris.

## Slide 39

### Capa de consultas

La capa de consultas brinda la posibilidad de interactuar directamente con los datos. A través de ella, los usuarios pueden formular preguntas específicas que devuelvan métricas, estadísticas o reportes de interés. Se trata de una fase más operativa que el análisis avanzado, pues está pensada para dar soporte inmediato a la toma de decisiones cotidianas. La eficacia de esta capa depende de la organización previa de los datos y de la capacidad del sistema para responder de manera ágil y confiable a los requerimientos planteados.

**Visual (diagrama):** "Arquitectura de Big Data" con las tres columnas izquierdas y las capas de la derecha (Consulta y análisis, Procesamiento, Almacenamiento) resaltadas.

## Slide 40

### Capa de consultas (herramientas)

**Visual (galería de logos):** Tres motores de consulta:
- **Apache Hive:** para consultas SQL sobre datos en Hadoop.
- **Presto:** para consultas interactivas en grandes volúmenes.
- **Apache Impala:** como alternativa rápida en entornos Hadoop.

## Slide 41

### Visualización de resultados

La visualización representa la culminación del proceso de Big Data, donde la información se traduce en un lenguaje comprensible para las personas. Más allá de mostrar gráficos atractivos, la visualización busca transmitir de manera clara patrones, tendencias y conclusiones que serían imposibles de detectar en el estado original de los datos. Una visualización bien diseñada no solo facilita la interpretación de los resultados, sino que también maximiza el impacto del análisis al permitir que distintos perfiles de usuarios, técnicos o no técnicos comprendan y utilicen el conocimiento generado.

**Visual (diagrama):** "Arquitectura de Big Data" con todas las capas del flujo (fuentes, ingestión, conexión, visualización, consulta, procesamiento, almacenamiento) resaltadas en naranja; solo Seguridad y Monitoreo quedan en gris.

## Slide 42

### Visualización de resultados (herramientas)

**Visual (galería de logos):** Tres herramientas de visualización/BI: **Power BI**, **Tableau** y **Grafana**.

## Slide 43

### Capas transversales

A lo largo de todo el flujo de Big Data operan dos capas transversales: la seguridad y la monitorización. La seguridad asegura que los datos estén protegidos frente a accesos no autorizados, pérdidas o manipulaciones indebidas, garantizando confidencialidad e integridad. La monitorización, por su parte, se ocupa de vigilar la calidad, consistencia y correcto funcionamiento de los procesos en cada etapa. Ambas capas no son fases aisladas, sino dimensiones permanentes que acompañan y sostienen la arquitectura en su totalidad.

**Visual (diagrama):** "Arquitectura de Big Data" con **todas** las capas resaltadas en naranja/borde rojo, incluyendo ahora las bandas transversales **Capa de Seguridad** y **Capa de Monitoreo** (diagrama completo activo).

## Slide 44

### Buenas Prácticas

El éxito de un proyecto de Big Data no depende solo de la tecnología, sino también de la forma en que se gestiona. Es recomendable definir objetivos claros que guíen el análisis, implementar la seguridad desde el inicio, y validar constantemente la calidad de los modelos y los datos. Asimismo, conviene alinear los resultados con necesidades reales del negocio o de la organización, de modo que el esfuerzo invertido genere impacto tangible. Finalmente, las metodologías ágiles permiten mantener flexibilidad en entornos que cambian rápidamente, lo cual es clave para aprovechar al máximo el valor del Big Data.

**Visual:** Título "BUENAS PRÁCTICAS" en rojo con una mano/lapicero marcando con check la cara feliz (verde) entre tres caritas de valoración (triste roja, neutra naranja, feliz verde) con casillas.

## Slide 45

### Conclusiones

Cuatro puntos numerados (cada uno dentro de corchetes):

1. El Big Data es un habilitador estratégico, ya que permite transformar grandes volúmenes de datos en conocimiento útil para la toma de decisiones.
2. La complejidad del Big Data radica en la diversidad y velocidad de los datos, lo que exige nuevas tecnologías y enfoques distintos a los tradicionales.
3. La correcta gestión del ciclo de datos (arquitectura) es fundamental para garantizar que la información sea procesada, analizada y utilizada de manera efectiva.
4. El valor del Big Data no está en los datos en sí, sino en su aplicación, es decir, en cómo se traducen en ventajas competitivas, eficiencia operativa e innovación.

## Slide 46

Cierre (decorativa). Fondo cian con el logo de **UTEC — Universidad de Ingeniería y Tecnología**.
