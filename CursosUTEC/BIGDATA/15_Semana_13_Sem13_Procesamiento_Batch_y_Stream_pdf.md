---
curso: BIGDATA
titulo: 15 - Semana 13/Sem13_Procesamiento Batch y Stream
slides: 41
fuente: 15 - Semana 13/Sem13_Procesamiento Batch y Stream.pdf
---

Procesamiento en
batch y stream
Mg. Aldo Lezama Benavides


Semana 13
           Objetivo de la sesión

1. Comprender de manera integral las diferencias entre el procesamiento por lotes, el
   procesamiento basado en eventos y el streaming, analizando cómo cada enfoque
   responde a distintas necesidades operativas y niveles de inmediatez en el manejo
   de datos.
2. Identificar los principios que sustentan a los sistemas modernos orientados a flujos
   de datos, incluyendo el rol de los logs, las colas y el procesamiento continuo, y
   cómo estos elementos permiten construir aplicaciones que reaccionan en tiempo
   real.
3. Reconocer la arquitectura y funcionamiento de Apache Kafka como plataforma
   central para la transmisión, almacenamiento y distribución de eventos, evaluando
   su capacidad de escalamiento, tolerancia a fallos y paralelismo.
           Contenido de la sesión

     01.             02.            03.

                   Computación
Procesamiento en                 Introducción a
                    basada en
      batch                          Kafka
                     eventos
01.   Procesamiento en lotes (batch)
                                       Introducción

• El procesamiento de datos ha evolucionado desde modelos tradicionales basados en lotes (batch) hacia
  arquitecturas de transmisión continua en tiempo real. Vamos a ver una comprensión progresiva de estos
  conceptos, comenzando por el procesamiento batch y avanzando hacia el streaming moderno.
                     Qué es el procesamiento por lotes


• El procesamiento por lotes consiste en acumular
  datos   durante   un   intervalo   de   tiempo   para
  procesarlos de manera agrupada. Este método fue
  diseñado en una época donde el hardware era
  costoso, por lo que procesar grandes volúmenes
  juntos resultaba más eficiente. Sin embargo, este
  enfoque implica una espera obligatoria antes de
  obtener resultados, ya que el sistema solo inicia
  cuando el lote está completo.
                         Escenarios donde se usa batch


• El procesamiento batch continúa siendo útil en
  situaciones donde la inmediatez no es un
  requisito. Es común en tareas programadas
  como la generación de reportes nocturnos, la
  lectura periódica de archivos, la automatización
  de correos y la emisión de documentos. Su
  valor radica en su estabilidad, su predictibilidad
  y la facilidad con la que puede ejecutarse de
  manera recurrente.
                        Escalamiento vertical en batch


• El escalamiento vertical se basa en aumentar
  la capacidad de un solo servidor agregando más
  CPU, más memoria RAM o almacenamiento
  más rápido. Aunque esta estrategia es sencilla
  de implementar, se enfrenta rápidamente a
  limitaciones físicas y económicas. El incremento
  de potencia en un único servidor tiende a
  volverse costoso y, eventualmente, insuficiente
  para manejar volúmenes crecientes de datos.
                     Escalamiento horizontal en batch


• El escalamiento horizontal divide un proceso
  en tareas más pequeñas que se distribuyen
  entre varias máquinas. Esto permite paralelizar
  el trabajo y obtener mejoras significativas en
  tiempos de ejecución. Sin embargo, requiere
  tecnologías de distribución como Spark y una
  coordinación más compleja entre nodos, aunque
  ofrece una capacidad de expansión mucho
  mayor que el escalamiento vertical.
                  Limitaciones del procesamiento batch


• El procesamiento por lotes introduce demoras
  en cada etapa del ciclo de datos. Antes de
  generar información útil, es necesario esperar la
  recolección, acumulación y ejecución del lote
  completo.    Estas    demoras      se    vuelven
  problemáticas cuando se necesitan respuestas
  inmediatas, especialmente en contextos donde
  los eventos cambian rápidamente.
02.   Computación basada en
      eventos
        De sistemas batch a sistemas basados en eventos


• Los sistemas modernos comenzaron a abandonar el
  enfoque clásico de procesamiento por lotes cuando
  surgió la necesidad de reaccionar a los datos a
  medida que ocurren. En lugar de esperar a que un
  volumen suficiente de información esté disponible, los
  sistemas basados en eventos ejecutan acciones tan
  pronto como un suceso es detectado. Este cambio
  conceptual permite una capacidad de respuesta
  mucho    mayor     y    da   forma   a   las   aplicaciones
  interactivas   y   en   tiempo   real    que   se   utilizan
  ampliamente hoy en día.
          Evolución hacia interfaces basadas en eventos


• Antes de la aparición de las interfaces gráficas, los programas funcionaban bajo un modelo cercano al batch:
  recibían instrucciones, las procesaban y devolvían un resultado. La llegada del GUI impulsó la adopción del
  procesamiento por eventos, ya que los sistemas comenzaron a “escuchar” acciones como clics, movimientos
  del mouse o teclas presionadas. Esto marcó una transición fundamental hacia sistemas más dinámicos y
  centrados en la experiencia del usuario.
                        Qué significa procesar eventos


• El procesamiento por eventos consiste en
  ejecutar una acción específica cuando ocurre
  un suceso particular. Ese suceso puede
  provenir de una interacción del usuario, un
  archivo que llega, un mensaje recibido en una
  cola o un sensor que detecta un cambio en el
  entorno. En este enfoque, el tiempo no lo
  dictan intervalos predefinidos, sino los propios
  eventos, lo que permite una capacidad de
  reacción inmediata.
            El click-stream como ejemplo representativo


• El click-stream, que registra las interacciones que los
  usuarios realizan en un sitio web, es un ejemplo claro
  de procesamiento basado en eventos. Cada clic
  genera     un    mensaje      que   puede     enviarse
  inmediatamente para análisis, almacenamiento o
  personalización de contenido. Gracias a esta captura
  en tiempo real, las plataformas pueden adaptar la
  experiencia del usuario y detectar patrones de
  comportamiento al instante.
                           Surgimiento de las colas
                     en arquitecturas basadas en eventos

• Para manejar el flujo de eventos de forma ordenada,
  muchas arquitecturas incorporan colas. Una cola
  actúa como un intermediario que recibe mensajes y
  los entrega a los sistemas encargados de procesarlos.
  Esta estructura permite desacoplar componentes,
  manejar picos de carga y garantizar que los mensajes
  se procesen en el orden en que fueron generados,
  incluso   cuando    diferentes   partes   del   sistema
  evolucionan por separado.
                               Función de las colas
                          en el procesamiento moderno

• Las colas ofrecen un mecanismo natural para regular
  el flujo de datos entre componentes que producen
  información y componentes que la consumen. Al
  almacenar temporalmente los eventos, permiten que
  el procesamiento se realice sin perder datos, incluso si
  la demanda fluctúa. Además, facilitan el aumento de
  consumidores en caso de que el volumen de eventos
  crezca, lo cual brinda una forma sencilla de escalar.
               Limitaciones y desafíos en el uso de colas


• Aunque las colas resultan útiles, no están libres de
  desafíos. Los mensajes pueden llegar con errores,
  pueden variar drásticamente en tamaño o pueden
  acumularse en exceso cuando el sistema no procesa
  a la misma velocidad a la que recibe. Además, estimar
  la longitud real de la cola puede ser complejo, lo cual
  dificulta la planificación de recursos y la prevención de
  cuellos de botella.
                  Introducción al concepto de streaming



El streaming surge como una respuesta a las limitaciones del batch y a la necesidad de disminuir la latencia. En un
sistema de streaming, los datos se procesan en cuanto llegan, sin esperar a que se acumulen. Este enfoque permite
manejar información continua de manera fluida y es especialmente útil cuando el comportamiento del sistema
depende del flujo constante de eventos.
                     Los logs como base del streaming


• Los logs, entendidos como registros secuenciales de
  eventos, constituyen el pilar fundamental de muchos
  sistemas   de   streaming.   Cada    evento   queda
  almacenado con detalle, lo que permite analizarlos
  posteriormente o procesarlos en tiempo real. Desde
  archivos simples hasta plataformas avanzadas como
  Kafka, los logs actúan como una fuente confiable de
  verdad sobre lo que ocurre en un sistema.

                       Registros del sistema operativo
                          como fuente de eventos

• Todos los sistemas operativos generan logs que describen fallos, accesos, instalaciones y múltiples acciones
  internas. Estos registros son esenciales para auditorías, monitoreo y seguridad. Los sistemas de streaming
  suelen consumir estos eventos para analizarlos en el momento en que ocurren, facilitando la detección
  temprana de anomalías o comportamientos sospechosos.
                   Diferencias entre batch y streaming


• El procesamiento por lotes y el procesamiento en
  streaming responden a necesidades distintas. En el
  enfoque batch, los datos se almacenan y se procesan
  en grupos definidos, lo que implica una espera
  obligatoria antes de obtener resultados. En el
  streaming, los datos fluyen continuamente y el sistema
  los   procesa   apenas    llegan,   lo   que   reduce
  significativamente la latencia. Ambas aproximaciones
  pueden coexistir, pero la elección depende de los
  requisitos de inmediatez, volumen y naturaleza del       Analogía la cubeta y la manguera

  problema.
                   Qué significa operar en tiempo real


• Operar en tiempo real no implica necesariamente
  actuar en milisegundos, sino garantizar una respuesta
  dentro de un límite temporal establecido. Ese límite
  varía según el contexto: en un sistema financiero
  puede ser crítico responder en segundos, mientras
  que en logística una actualización cada minuto puede
  ser suficiente. Lo esencial es que el sistema sea
  predecible y cumpla con su ventana de respuesta.
                  Relación entre streaming y tiempo real


• El streaming suele ser la base de los sistemas en
  tiempo real porque procesa los datos en el momento
  en que se producen. Su capacidad para evitar
  acumulaciones    hace   que   los   sistemas   puedan
  reaccionar a eventos rápidamente. La combinación
  adecuada de velocidad de transporte, capacidad de
  cómputo y baja latencia convierte al streaming en un
  componente esencial de aplicaciones modernas que
  requieren respuesta inmediata.
                 Recursos y limitaciones en tiempo real



• Los sistemas en tiempo real dependen de múltiples variables: el rendimiento de la red, la velocidad del
  almacenamiento, la capacidad de cómputo y el costo de operación. Aunque un sistema pueda ofrecer
  respuestas muy rápidas, esto no siempre es sostenible si los recursos que demanda son demasiado
  costosos. Por ello, equilibrar velocidad y eficiencia es fundamental al diseñar arquitecturas orientadas al
  tiempo real.
                           Frameworks de streaming

• Para implementar sistemas basados en flujos continuos existen plataformas especializadas que facilitan la
  ingestión, el transporte y el procesamiento en tiempo real. Herramientas como Kafka, Spark Streaming y Flink
  proporcionan componentes ya optimizados para manejar grandes volúmenes de datos con baja latencia.
  Estas plataformas se han convertido en pilares fundamentales en arquitecturas orientadas a eventos.




                                                                                                 Celery
Frameworks de streaming



     Kafka permite enviar millones de eventos entre productores y
     consumidores. Su arquitectura distribuida lo convierte en una
     herramienta esencial para sistemas de alta demanda. Permite
     escalamiento horizontal, tolerancia a fallos y persistencia eficiente.
Frameworks de streaming



     Spark Streaming extiende el poder de Spark al mundo del tiempo
     real.   Aprovecha   micro-lotes   para   equilibrar   rendimiento   y
     simplicidad. Es especialmente útil para modelos de machine
     learning que procesan flujos de datos en constante actualización.
Frameworks de streaming



     Spark Streaming extiende el poder de Spark al mundo del tiempo
     real.   Aprovecha   micro-lotes   para   equilibrar   rendimiento   y
     simplicidad. Es especialmente útil para modelos de machine
     learning que procesan flujos de datos en constante actualización.
03.   Introducción a Kafka
                         Introducción a Apache Kafka


• Apache Kafka es una plataforma distribuida diseñada
  para manejar flujos de eventos a gran escala. Su
  arquitectura permite transmitir, almacenar y distribuir
  millones de mensajes por segundo con baja latencia.
  Kafka se ha convertido en un componente central en
  organizaciones que necesitan integrar datos en tiempo
  real, coordinar microservicios o ejecutar análisis
  continuos.
                         Por qué Kafka es tan relevante


• Kafka aborda limitaciones que otros sistemas de
  mensajería no pueden resolver fácilmente. Ofrece alta
  escalabilidad, múltiples consumidores simultáneos y
  una política de retención que permite conservar los
  mensajes    durante   el   tiempo   necesario.    Estas
  características lo hacen útil para registrar eventos,
  integrar aplicaciones, alimentar pipelines de análisis y
  soportar sistemas de machine learning en tiempo real.
                       Arquitectura general de Kafka



• Kafka se compone de productores que envían
 mensajes, consumidores que los leen y brokers que
 actúan como servidores distribuidores de los datos.
 Los mensajes se organizan en tópicos, que funcionan
 como canales lógicos. Esta estructura permite un
 diseño simple pero sumamente escalable, capaz de
 soportar miles de clientes trabajando en simultáneo.
                          Los tópicos como eje central


• Los tópicos son contenedores lógicos donde
  los eventos son almacenados de manera
  secuencial. Kafka no elimina los mensajes
  cuando un consumidor los lee; en su lugar,
  los conserva según una política de tiempo.
  Esto facilita que diferentes aplicaciones
  procesen el mismo flujo sin interferencias,
  ofreciendo   una   enorme   flexibilidad   en
  escenarios complejos.
                             Particiones y paralelismo


• Un tópico se divide en particiones, y cada partición
  mantiene un orden estricto de llegada. Esta división
  permite que múltiples consumidores procesen datos
  en paralelo sin perder coherencia. A medida que
  aumenta la carga, se pueden añadir particiones
  adicionales para distribuir el trabajo, lo que hace que
  Kafka escale horizontalmente de forma natural.
                          Brokers y el clúster de Kafka


• Cada broker es un servidor que almacena datos y
  coordina la comunicación. Un conjunto de brokers
  forma un clúster capaz de distribuir las particiones y
  ofrecer tolerancia a fallos. Si un nodo falla, el clúster
  continúa operando gracias a las copias replicadas en
  otros servidores, evitando la pérdida de mensajes y
  manteniendo el sistema operativo.
                       Replicación y tolerancia a fallos


• Kafka replica cada partición en varios brokers. Para
  cada conjunto replicado, uno actúa como líder y los
  demás como seguidores. El líder maneja la lectura y
  escritura, mientras que los seguidores mantienen
  copias exactas. Si el líder falla, uno de los seguidores
  asume su rol automáticamente, proporcionando un
  mecanismo robusto de alta disponibilidad.
                           Función de los productores


• Los productores son responsables de enviar eventos
  hacia los tópicos. Pueden decidir en qué partición
  colocar cada mensaje, ya sea mediante una clave,
  mediante un reparto automático o mediante reglas
  personalizadas. Kafka asegura que los eventos
  lleguen de forma confiable utilizando configuraciones
  de confirmación que equilibran velocidad y durabilidad.
                        Cómo operan los consumidores


• Los consumidores leen los mensajes a su propio ritmo
  y pueden organizarse en grupos. Cada grupo se divide
  el trabajo asignando particiones específicas a cada
  consumidor, lo que permite aprovechar el paralelismo.
  Diferentes grupos pueden leer el mismo tópico
  independientemente, lo que facilita construir múltiples
  aplicaciones a partir de un mismo flujo.
                      Conclusiones
      El procesamiento por lotes, el procesamiento basado en eventos y el streaming

01.   representan etapas complementarias en la evolución de las arquitecturas de datos,
      y comprender sus diferencias permite seleccionar la estrategia adecuada según los
      requerimientos de latencia, volumen y frecuencia.

      Los sistemas de streaming se han convertido en un componente clave para

02.   aplicaciones que requieren respuesta inmediata, gracias a su capacidad de procesar
      datos tan pronto como se generan y a su integración con mecanismos de colas y
      logs que garantizan un flujo continuo y confiable.

      Kafka se consolida como una herramienta fundamental para arquitecturas de

03.   datos modernas, proporcionando un modelo distribuido que permite manejar
      grandes volúmenes de eventos con escalabilidad, paralelismo y alta disponibilidad,
      habilitando múltiples casos de uso en tiempo real.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
