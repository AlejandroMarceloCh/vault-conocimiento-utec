---
curso: BIGDATA
titulo: 15 - Semana 13/Sem13_Procesamiento Batch y Stream
slides: 41
fuente: 15 - Semana 13/Sem13_Procesamiento Batch y Stream.pdf
---

## Slide 1

Portada (decorativa: fondo cian con foto del edificio UTEC y marca "Reinventa el mundo").

**Procesamiento en batch y stream**
Mg. Aldo Lezama Benavides
Semana 13

## Slide 2

**Objetivo de la sesión**

Lista numerada dentro de un marco de corchetes blancos:

1. **Comprender** de manera integral las diferencias entre el procesamiento por lotes, el procesamiento basado en eventos y el streaming, analizando cómo cada enfoque responde a distintas necesidades operativas y niveles de inmediatez en el manejo de datos.
2. **Identificar** los principios que sustentan a los sistemas modernos orientados a flujos de datos, incluyendo el rol de los logs, las colas y el procesamiento continuo, y cómo estos elementos permiten construir aplicaciones que reaccionan en tiempo real.
3. **Reconocer** la arquitectura y funcionamiento de Apache Kafka como plataforma central para la transmisión, almacenamiento y distribución de eventos, evaluando su capacidad de escalamiento, tolerancia a fallos y paralelismo.

## Slide 3

**Contenido de la sesión**

Tres bloques en corchetes blancos, uno al lado del otro:

| # | Tema |
|---|------|
| 01. | Procesamiento en batch |
| 02. | Computación basada en eventos |
| 03. | Introducción a Kafka |

## Slide 4

Portada de sección: **01. Procesamiento en lotes (batch)** — número grande "01." entre corchetes blancos, icono de portapapeles con checklist junto al título.

## Slide 5

**Introducción**

- El procesamiento de datos ha evolucionado desde modelos tradicionales basados en lotes (batch) hacia arquitecturas de transmisión continua en tiempo real. Vamos a ver una comprensión progresiva de estos conceptos, comenzando por el procesamiento batch y avanzando hacia el streaming moderno.

**Visual:** diagrama estilo pizarra dividido por una línea vertical azul en dos mitades.
- Izquierda, **"Batch Processing"**: una rejilla de 6 cajas rotuladas "Source" cuyas flechas convergen en una caja verde "Batch Processor"; debajo de esta, la nota "Delay: Mins, hours, days"; desde el procesador una flecha va a una caja rosada "Destination".
- Derecha, **"Streaming"**: una caja azul "Source" conecta con una cinta horizontal formada por muchas cajitas pequeñas (el flujo continuo), rotulada abajo "Almost - Real-time", y una flecha llega a la caja rosada "Destination". No hay procesador intermedio con demora.

## Slide 6

**Qué es el procesamiento por lotes**

- El procesamiento por lotes consiste en acumular datos durante un intervalo de tiempo para procesarlos de manera agrupada. Este método fue diseñado en una época donde el hardware era costoso, por lo que procesar grandes volúmenes juntos resultaba más eficiente. Sin embargo, este enfoque implica una espera obligatoria antes de obtener resultados, ya que el sistema solo inicia cuando el lote está completo.

**Visual:** diagrama gris de arquitectura. Un grupo de figuras de usuarios emite "Request" hacia un cilindro (canal), con un archivo "config" y una base de datos adjuntos. El request llega a un bloque "Batch Processing Component", que se conecta bidireccionalmente con una pila de "Processing Components" (icono de engranaje) y, hacia abajo, con un cilindro "Request Store".

## Slide 7

**Escenarios donde se usa batch**

- El procesamiento batch continúa siendo útil en situaciones donde la inmediatez no es un requisito. Es común en tareas programadas como la generación de reportes nocturnos, la lectura periódica de archivos, la automatización de correos y la emisión de documentos. Su valor radica en su estabilidad, su predictibilidad y la facilidad con la que puede ejecutarse de manera recurrente.

**Visual:** infografía "BATCH PROCESSING". Cuatro personas rotuladas USER, cada una con su JOB (documento de color), y todas las flechas convergen en un monitor central rotulado OPERATOR. Desde el operador salen dos ramas: cada una pasa por "JOBS" (grupo de documentos) → "BATCH" (icono de base de datos naranja) → y ambas confluyen en un rack rotulado COMPUTER, junto al que hay una persona.

## Slide 8

**Escalamiento vertical en batch**

- El **escalamiento vertical** se basa en aumentar la capacidad de un solo servidor agregando más CPU, más memoria RAM o almacenamiento más rápido. Aunque esta estrategia es sencilla de implementar, se enfrenta rápidamente a limitaciones físicas y económicas. El incremento de potencia en un único servidor tiende a volverse costoso y, eventualmente, insuficiente para manejar volúmenes crecientes de datos.

**Visual:** recuadro con una flecha azul ascendente de izquierda a derecha; debajo, tres pares de cajas "Odoo / Filestore" de tamaño creciente (pequeño gris claro → mediano → grande azul intenso). Leyenda: "Escalamiento Vertical".

## Slide 9

**Escalamiento horizontal en batch**

- El **escalamiento horizontal** divide un proceso en tareas más pequeñas que se distribuyen entre varias máquinas. Esto permite paralelizar el trabajo y obtener mejoras significativas en tiempos de ejecución. Sin embargo, requiere tecnologías de distribución como Spark y una coordinación más compleja entre nodos, aunque ofrece una capacidad de expansión mucho mayor que el escalamiento vertical.

**Visual:** recuadro con una flecha azul horizontal en la parte superior; debajo, cuatro servidores azules idénticos rotulados "Odoo" en fila, y debajo de ellos dos cajas: "PostgresSQL" y "Filestore". Leyenda: "Escalamiento Horizontal".

## Slide 10

**Limitaciones del procesamiento batch**

- El procesamiento por lotes introduce demoras en cada etapa del ciclo de datos. Antes de generar información útil, es necesario esperar la recolección, acumulación y ejecución del lote completo. Estas demoras se vuelven problemáticas cuando se necesitan respuestas inmediatas, especialmente en contextos donde los eventos cambian rápidamente.

**Visual:** esquema **"Batch ETL"** con una línea de tiempo punteada arriba ("Time stream ->") marcada por cuatro relojes. Dos paneles:
- **Unscheduled ETL Batch Job**: un administrador con laptop; texto "At 7:00 AM, Admin extracts and process last night's server logs for analysis"; flujo `Server logs → (engranajes) → Data Warehouse`.
- **Scheduled/Unattended ETL Batch Job**: "At 12:00 AM every 1st of the month, extract and process posted accounting entries of the previous month"; flujo `Accounting entries → (engranajes) → Data Warehouse`; abajo un bloque azul "Covered Period" con "Friday JULY 1" **to** "Sunday JULY 31".

## Slide 11

Portada de sección: **02. Computación basada en eventos** (número "02." entre corchetes, icono de portapapeles).

## Slide 12

**De sistemas batch a sistemas basados en eventos**

- Los sistemas modernos comenzaron a abandonar el enfoque clásico de procesamiento por lotes cuando surgió la necesidad de reaccionar a los datos a medida que ocurren. En lugar de esperar a que un volumen suficiente de información esté disponible, los sistemas basados en eventos ejecutan acciones tan pronto como un suceso es detectado. Este cambio conceptual permite una capacidad de respuesta mucho mayor y da forma a las aplicaciones interactivas y en tiempo real que se utilizan ampliamente hoy en día.

**Visual:** diagrama de tres bloques de color.
- **EVENT PRODUCER** (morado, icono de engranaje con `</>`), del que salen dos flechas etiquetadas "EVENT".
- **EVENT BROKER** (rojo/coral) que contiene "TOPIC 01", "TOPIC 02", "TOPIC…".
- **EVENT CONSUMER(S)** (celeste) con tres iconos de nodos circulares. Entre broker y consumidores, por cada tópico hay una flecha azul de vuelta "SUBSCRIBE TOPIC 01 / 02 / …" y una flecha naranja de ida etiquetada "EVENT".

## Slide 13

**Evolución hacia interfaces basadas en eventos**

- Antes de la aparición de las interfaces gráficas, los programas funcionaban bajo un modelo cercano al batch: recibían instrucciones, las procesaban y devolvían un resultado. La llegada del GUI impulsó la adopción del procesamiento por eventos, ya que los sistemas comenzaron a "escuchar" acciones como clics, movimientos del mouse o teclas presionadas. Esto marcó una transición fundamental hacia sistemas más dinámicos y centrados en la experiencia del usuario.

Slide solo de texto, sin figura.

## Slide 14

**Qué significa procesar eventos**

- El procesamiento por eventos consiste en ejecutar una acción específica cuando ocurre un suceso particular. Ese suceso puede provenir de una interacción del usuario, un archivo que llega, un mensaje recibido en una cola o un sensor que detecta un cambio en el entorno. En este enfoque, el tiempo no lo dictan intervalos predefinidos, sino los propios eventos, lo que permite una capacidad de reacción inmediata.

**Visual:** arquitectura event-driven en tres columnas (estilo AWS EventBridge).
- **Event Producer**: *Retail website* ("A customer places a new order through the website") emite un rombo rojo "New order"; *Mobile app* ("A customer submits a question about the availability of an item through the app") emite un círculo azul "Question"; *Point-of-Sale* ("A customer returns an item in person at the store") emite una caja verde "Return".
- Centro: **Event Router** (icono de embudo con engranajes) — "Ingests, filters and pushes the events to the appropriate consumers".
- **Event Consumer**: *Management DB* ("Inventory and item availability updates") recibe Return + New order; *Finance System* ("Updates based on the sale and return") recibe New order + Return; *Customer Relations* ("Customer support team responds to the order and inquiry") recibe New order + Question.

## Slide 15

**El click-stream como ejemplo representativo**

- El click-stream, que registra las interacciones que los usuarios realizan en un sitio web, es un ejemplo claro de procesamiento basado en eventos. Cada clic genera un mensaje que puede enviarse inmediatamente para análisis, almacenamiento o personalización de contenido. Gracias a esta captura en tiempo real, las plataformas pueden adaptar la experiencia del usuario y detectar patrones de comportamiento al instante.

**Visual:** infografía "How clickstream data is generated and used", con dos tarjetas:

| Actions that generate clickstream data (azul) | What clickstream data is used to analyze (verde) |
|---|---|
| User login | Ad campaigns |
| Account registration | Marketing campaigns |
| Newsletter sign-up | Campaign tools |
| Search performed | Product performance |
| Product added to cart | A/B testing trials |
| Product purchased | |
| Feedback provided | |

## Slide 16

**Surgimiento de las colas en arquitecturas basadas en eventos**

- Para manejar el flujo de eventos de forma ordenada, muchas arquitecturas incorporan colas. Una cola actúa como un intermediario que recibe mensajes y los entrega a los sistemas encargados de procesarlos. Esta estructura permite desacoplar componentes, manejar picos de carga y garantizar que los mensajes se procesen en el orden en que fueron generados, incluso cuando diferentes partes del sistema evolucionan por separado.

**Visual:** esquema clásico de cola FIFO: un rectángulo azul entra por una flecha rotulada **"Encolar"** hacia el extremo marcado **"Final"** de una fila de cinco rectángulos azules; en el otro extremo, marcado **"Principio"**, sale una flecha rotulada **"Desencolar"** hacia un rectángulo suelto.

## Slide 17

**Función de las colas en el procesamiento moderno**

- Las colas ofrecen un mecanismo natural para regular el flujo de datos entre componentes que producen información y componentes que la consumen. Al almacenar temporalmente los eventos, permiten que el procesamiento se realice sin perder datos, incluso si la demanda fluctúa. Además, facilitan el aumento de consumidores en caso de que el volumen de eventos crezca, lo cual brinda una forma sencilla de escalar.

**Visual:** dos "contenedores" azules verticales. En el izquierdo entra por arriba (flecha roja rotulada "Entra") una caja verde "Nuevo 5", sobre una pila que ya tiene Elemento 4, 3, 2, 1 (de arriba abajo). Una flecha roja vertical central rotulada "Orden" apunta hacia abajo. El contenedor derecho muestra el resultado: Nuevo 5, Elemento 4, Elemento 3, Elemento 2, Elemento 1.

## Slide 18

**Limitaciones y desafíos en el uso de colas**

- Aunque las colas resultan útiles, no están libres de desafíos. Los mensajes pueden llegar con errores, pueden variar drásticamente en tamaño o pueden acumularse en exceso cuando el sistema no procesa a la misma velocidad a la que recibe. Además, estimar la longitud real de la cola puede ser complejo, lo cual dificulta la planificación de recursos y la prevención de cuellos de botella.

**Visual:** el mismo contenedor azul lleno con Elemento 4, 3, 2, 1 y una línea punteada roja rotulada **"Capacidad Máxima"**. La caja verde "Nuevo 5" intenta entrar (flecha roja "Entra") pero choca con un icono de prohibido y sale rebotada por una flecha roja diagonal rotulada **"Rechazada"**.

## Slide 19

**Introducción al concepto de streaming**

El streaming surge como una respuesta a las limitaciones del batch y a la necesidad de disminuir la latencia. En un sistema de streaming, los datos se procesan en cuanto llegan, sin esperar a que se acumulen. Este enfoque permite manejar información continua de manera fluida y es especialmente útil cuando el comportamiento del sistema depende del flujo constante de eventos.

Slide solo de texto, sin figura.

## Slide 20

**Los logs como base del streaming**

- Los logs, entendidos como registros secuenciales de eventos, constituyen el pilar fundamental de muchos sistemas de streaming. Cada evento queda almacenado con detalle, lo que permite analizarlos posteriormente o procesarlos en tiempo real. Desde archivos simples hasta plataformas avanzadas como Kafka, los logs actúan como una fuente confiable de verdad sobre lo que ocurre en un sistema.

**Visual:** captura de pantalla de un visor web de logs. Arriba: caja de búsqueda, checkbox "Mostrar solo resultado que cumplan el criterio de búsqueda" y checkbox marcado "Aplicar colores a la visualización". Un desplegable "Datos a visualizar: Todas las líneas de Log" está abierto (resaltado en rojo) con las opciones:
- Todas las líneas de Log (seleccionada, azul)
- Solo líneas resultado OK - (Status 200)
- Solo líneas resultado Redirect - (Status 300)
- Solo líneas resultado Client Error - (Status 400)
- Solo líneas resultado Server Error - (Status 500)

Debajo, tabla numerada (1..18) con líneas de log de Apache en formato combinado, p. ej. `swmanuales.com - [07/Dec/2024 09:45:57 +0100] "GET /wordpress HTTP/1.0" 404 196 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"`. Las filas 404 aparecen coloreadas en rosado; algunas son 200.

## Slide 21

**Registros del sistema operativo como fuente de eventos**

- Todos los sistemas operativos generan logs que describen fallos, accesos, instalaciones y múltiples acciones internas. Estos registros son esenciales para auditorías, monitoreo y seguridad. Los sistemas de streaming suelen consumir estos eventos para analizarlos en el momento en que ocurren, facilitando la detección temprana de anomalías o comportamientos sospechosos.

Slide solo de texto, sin figura.

## Slide 22

**Diferencias entre batch y streaming**

- El procesamiento por lotes y el procesamiento en streaming responden a necesidades distintas. En el enfoque batch, los datos se almacenan y se procesan en grupos definidos, lo que implica una espera obligatoria antes de obtener resultados. En el streaming, los datos fluyen continuamente y el sistema los procesa apenas llegan, lo que reduce significativamente la latencia. Ambas aproximaciones pueden coexistir, pero la elección depende de los requisitos de inmediatez, volumen y naturaleza del problema.

**Visual:** ilustración de un balde gris con agua y una gota cayendo, rotulado **BUCKET**, frente a **VS.**, y un grifo con manguera verde soltando un chorro continuo de agua, rotulado **HOSE**. Pie de figura: "Analogía la cubeta y la manguera".

## Slide 23

**Qué significa operar en tiempo real**

- Operar en tiempo real no implica necesariamente actuar en milisegundos, sino garantizar una respuesta dentro de un límite temporal establecido. Ese límite varía según el contexto: en un sistema financiero puede ser crítico responder en segundos, mientras que en logística una actualización cada minuto puede ser suficiente. Lo esencial es que el sistema sea predecible y cumpla con su ventana de respuesta.

**Visual:** logotipo/banner con la palabra "Real" sobre fondo verde azulado y "Time" sobre fondo magenta.

## Slide 24

**Relación entre streaming y tiempo real**

- El streaming suele ser la base de los sistemas en tiempo real porque procesa los datos en el momento en que se producen. Su capacidad para evitar acumulaciones hace que los sistemas puedan reaccionar a eventos rápidamente. La combinación adecuada de velocidad de transporte, capacidad de cómputo y baja latencia convierte al streaming en un componente esencial de aplicaciones modernas que requieren respuesta inmediata.

**Visual:** diagrama radial. En el centro un rectángulo redondeado con marco de cuatro colores (verde, rojo, amarillo, azul oscuro) rotulado **"Real-Time Data Streaming Applications"**; conectadas por líneas punteadas, cuatro tarjetas con icono:
- Forex/Trading apps (engranaje con monedas $)
- Digital media (monitor con botón play)
- Real estate apps (móvil con ficha de casa)
- Online games (globo terráqueo con gamepad)

## Slide 25

**Recursos y limitaciones en tiempo real**

- Los sistemas en tiempo real dependen de múltiples variables: el rendimiento de la red, la velocidad del almacenamiento, la capacidad de cómputo y el costo de operación. Aunque un sistema pueda ofrecer respuestas muy rápidas, esto no siempre es sostenible si los recursos que demanda son demasiado costosos. Por ello, equilibrar velocidad y eficiencia es fundamental al diseñar arquitecturas orientadas al tiempo real.

Slide solo de texto, sin figura.

## Slide 26

**Frameworks de streaming**

- Para implementar sistemas basados en flujos continuos existen plataformas especializadas que facilitan la ingestión, el transporte y el procesamiento en tiempo real. Herramientas como Kafka, Spark Streaming y Flink proporcionan componentes ya optimizados para manejar grandes volúmenes de datos con baja latencia. Estas plataformas se han convertido en pilares fundamentales en arquitecturas orientadas a eventos.

**Visual:** fila con cuatro logotipos: **kafka** (nodos negros), **Spark Streaming** (estrella naranja), **Apache Flink** (ardilla colorida) y **Celery** (tallo verde).

## Slide 27

**Frameworks de streaming**

Logo de **kafka** a la izquierda; a la derecha el texto:

Kafka permite enviar millones de eventos entre productores y consumidores. Su arquitectura distribuida lo convierte en una herramienta esencial para sistemas de alta demanda. Permite escalamiento horizontal, tolerancia a fallos y persistencia eficiente.

## Slide 28

**Frameworks de streaming**

Logo de **Spark Streaming** a la izquierda; a la derecha el texto:

Spark Streaming extiende el poder de Spark al mundo del tiempo real. Aprovecha micro-lotes para equilibrar rendimiento y simplicidad. Es especialmente útil para modelos de machine learning que procesan flujos de datos en constante actualización.

## Slide 29

**Frameworks de streaming**

Slide idéntica a la anterior (duplicada en el PDF): logo de **Spark Streaming** y el mismo párrafo sobre micro-lotes y machine learning.

## Slide 30

Portada de sección: **03. Introducción a Kafka** (número "03." entre corchetes, icono de portapapeles).

## Slide 31

**Introducción a Apache Kafka**

- Apache Kafka es una plataforma distribuida diseñada para manejar flujos de eventos a gran escala. Su arquitectura permite transmitir, almacenar y distribuir millones de mensajes por segundo con baja latencia. Kafka se ha convertido en un componente central en organizaciones que necesitan integrar datos en tiempo real, coordinar microservicios o ejecutar análisis continuos.

**Visual:** logotipo de kafka a la derecha.

## Slide 32

**Por qué Kafka es tan relevante**

- Kafka aborda limitaciones que otros sistemas de mensajería no pueden resolver fácilmente. Ofrece alta escalabilidad, múltiples consumidores simultáneos y una política de retención que permite conservar los mensajes durante el tiempo necesario. Estas características lo hacen útil para registrar eventos, integrar aplicaciones, alimentar pipelines de análisis y soportar sistemas de machine learning en tiempo real.

**Visual:** logotipo de kafka a la derecha.

## Slide 33

**Arquitectura general de Kafka**

- Kafka se compone de productores que envían mensajes, consumidores que los leen y brokers que actúan como servidores distribuidores de los datos. Los mensajes se organizan en tópicos, que funcionan como canales lógicos. Esta estructura permite un diseño simple pero sumamente escalable, capaz de soportar miles de clientes trabajando en simultáneo.

**Visual:** diagrama publicador/suscriptor con clipart. Un **Publicador** "Genera" (flecha azul) un **Mensaje** hacia **Topic 1** (caja naranja) y otro Mensaje hacia **Topic 2**. Desde cada tópico sale una flecha roja "Entrega" con un Mensaje hacia **Suscriptor 1** y **Suscriptor 2** respectivamente; en sentido inverso, cada suscriptor tiene una flecha roja "Suscribe" apuntando a su tópico.

## Slide 34

**Los tópicos como eje central**

- Los tópicos son contenedores lógicos donde los eventos son almacenados de manera secuencial. Kafka no elimina los mensajes cuando un consumidor los lee; en su lugar, los conserva según una política de tiempo. Esto facilita que diferentes aplicaciones procesen el mismo flujo sin interferencias, ofreciendo una enorme flexibilidad en escenarios complejos.

**Visual:** tres cajas turquesa **Producer** a la izquierda (con icono de sobre y rótulo "send message") cuyas flechas convergen en un bloque central **KAFKA** que contiene una franja rotulada **topic**; desde ahí salen tres flechas hacia tres cajas **Consumer** a la derecha (icono de sobre, "receive message").

## Slide 35

**Particiones y paralelismo**

- Un tópico se divide en particiones, y cada partición mantiene un orden estricto de llegada. Esta división permite que múltiples consumidores procesen datos en paralelo sin perder coherencia. A medida que aumenta la carga, se pueden añadir particiones adicionales para distribuir el trabajo, lo que hace que Kafka escale horizontalmente de forma natural.

**Visual:** recuadro rotulado **TOPIC KAFKA** que contiene tres "tubos" rosados horizontales: **PARTICIÓN 1**, **PARTICIÓN 2**, **PARTICIÓN 3**; cada uno con una fila de celdas rotulada MENSAJES en su extremo izquierdo. De cada partición sale una flecha negra gruesa hacia una caja verde: CONSUMIDOR 1, CONSUMIDOR 2 y CONSUMIDOR 3 respectivamente (mapeo 1:1 partición-consumidor).

## Slide 36

**Brokers y el clúster de Kafka**

- Cada broker es un servidor que almacena datos y coordina la comunicación. Un conjunto de brokers forma un clúster capaz de distribuir las particiones y ofrecer tolerancia a fallos. Si un nodo falla, el clúster continúa operando gracias a las copias replicadas en otros servidores, evitando la pérdida de mensajes y manteniendo el sistema operativo.

**Visual:** diagrama titulado **"Apache Kafka Broker"**. Una barra azul superior a lo ancho rotulada **Zookeeper**, con flechas verticales que suben desde los productores (una punteada), desde el broker y desde los consumidores. En el centro, caja beige **"Single Node-Single Kafka Broker / Kafka-Broker"**; a la izquierda tres cajas **Producer** conectadas hacia el broker, y a la derecha tres cajas **Consumer** que reciben del broker.

## Slide 37

**Replicación y tolerancia a fallos**

- Kafka replica cada partición en varios brokers. Para cada conjunto replicado, uno actúa como líder y los demás como seguidores. El líder maneja la lectura y escritura, mientras que los seguidores mantienen copias exactas. Si el líder falla, uno de los seguidores asume su rol automáticamente, proporcionando un mecanismo robusto de alta disponibilidad.

**Visual:** esquema **APACHE KAFKA**. Una barra azul oscura **BROKER** encabeza un panel gris con tres columnas: **TOPIC 1** (celdas azules), **TOPIC 2** (celdas rojas) y **TOPIC 3** (celdas verdes), cada uno con dos filas de cuatro celdas; abajo la leyenda punteada **PARTITIONS**. A la izquierda, una barra vertical **PRODUCER** con icono de sobre y la nota "Send Record to given Topic & Partition". A la derecha, una barra **CONSUMER** (flecha entrante desde arriba) y un apilado de barras **CONSUMER GROUPS** con la nota "Reads from given Topic & Partition".

## Slide 38

**Función de los productores**

- Los productores son responsables de enviar eventos hacia los tópicos. Pueden decidir en qué partición colocar cada mensaje, ya sea mediante una clave, mediante un reparto automático o mediante reglas personalizadas. Kafka asegura que los eventos lleguen de forma confiable utilizando configuraciones de confirmación que equilibran velocidad y durabilidad.

**Visual:** pipeline de izquierda a derecha. Fuentes: **Mobile Phone**, **Computers**, **IoT Device** → flecha azul **Producer** → caja con el logo **kafka** → tres salidas azules: **Consumer**, **Kafka Streams**, **KSQL** → destinos finales: **Email**, **Phone**, **Database** (icono DB).

## Slide 39

**Cómo operan los consumidores**

- Los consumidores leen los mensajes a su propio ritmo y pueden organizarse en grupos. Cada grupo se divide el trabajo asignando particiones específicas a cada consumidor, lo que permite aprovechar el paralelismo. Diferentes grupos pueden leer el mismo tópico independientemente, lo que facilita construir múltiples aplicaciones a partir de un mismo flujo.

**Visual:** el mismo pipeline de la slide anterior: Mobile Phone / Computers / IoT Device → Producer → kafka → Consumer, Kafka Streams, KSQL → Email, Phone, Database.

## Slide 40

**Conclusiones**

01. El procesamiento por lotes, el procesamiento basado en eventos y el streaming representan etapas complementarias en la evolución de las arquitecturas de datos, y comprender sus diferencias permite seleccionar la estrategia adecuada según los requerimientos de latencia, volumen y frecuencia.

02. Los sistemas de streaming se han convertido en un componente clave para aplicaciones que requieren respuesta inmediata, gracias a su capacidad de procesar datos tan pronto como se generan y a su integración con mecanismos de colas y logs que garantizan un flujo continuo y confiable.

03. Kafka se consolida como una herramienta fundamental para arquitecturas de datos modernas, proporcionando un modelo distribuido que permite manejar grandes volúmenes de eventos con escalabilidad, paralelismo y alta disponibilidad, habilitando múltiples casos de uso en tiempo real.

(Cada bloque va entre corchetes celestes con el número grande a la izquierda.)

## Slide 41

Cierre decorativo: logo UTEC centrado sobre fondo cian. Sin contenido.
