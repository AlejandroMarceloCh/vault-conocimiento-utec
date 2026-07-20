---
curso: BD2
titulo: 12 BD Distribuidas - Fragmentación Horizontal
slides: 79
fuente: 12 BD Distribuidas - Fragmentación Horizontal.pdf
---

# 12 BD Distribuidas - Fragmentación Horizontal

## Índice

- [Crecimiento de los datos y la escala](#crecimiento-de-los-datos-y-la-escala)
- [Sistemas distribuidos](#sistemas-distribuidos)
- [Base de Datos Distribuidas](#base-de-datos-distribuidas)
- [Diseño de BDD](#diseño-de-bdd)
- [Fragmentación](#fragmentación)
- [Fragmentación Horizontal](#fragmentación-horizontal)
- [Fragmentación Horizontal Derivada](#fragmentación-horizontal-derivada)
- [Base de Datos Distribuida en PostgreSQL](#base-de-datos-distribuida-en-postgresql)
- [Ejercicio](#ejercicio)
- [Glosario](#glosario)

## Crecimiento de los datos y la escala

### Crecimiento de los datos

Crecimiento de los datos

Internet Traffic
≈ 2,417 PB / day
≈ 47,000,000 Wiki / day
(2014, Cisco estimates)

**Figura (slide 3):** Globo terráqueo digital azul brillante sobre fondo negro, representando redes interconectadas. Banda horizontal blanca semitransparente superpuesta en el centro del globo con las estadísticas de tráfico de Internet. Fondo amarillo detrás de la imagen central, con borde blanco grueso arriba y abajo.

Crecimiento de los datos

ChatGTP
≈ 100 million users within 2 months
≈ 1 trillion parameters
(*Estimated, V4)

https://www.stylefactoryproductions.com/blog/chatgpt-statistics

Texto superpuesto sobre el elemento central con las estadísticas de ChatGTP. Fondo amarillo claro con franja horizontal blanca en el centro y barra azul delgada en la parte inferior. URL de fuente en la sección amarilla inferior.

Crecimiento de los datos

Un moderno cuello de botella ☺

**Figura (slide 5):** Fotografía aérea de un atasco de tráfico extremo. Autopista de múltiples carriles (decenas de carriles) completamente saturada con cientos o miles de autos densamente empaquetados, moviéndose hacia una estructura de peaje o punto de control visible en el lado derecho del encuadre. Los carriles convergen al acercarse a la estructura, creando una analogía visual de «cuello de botella».

Crecimiento de los datos ... muchas soluciones

**Figura (slide 6):** Infografía completa del ecosistema Big Data titulada «Crecimiento de los datos ... Organizada en secciones principales:

- **Infrastructure:** subcategorías incluyendo NoSQL Databases (MongoDB, Cassandra, Couchbase, Redis, MarkLogic), NewSQL Databases (SAP HANA, Clustrix, MemSQL, VoltDB, Cockroach Labs), MPP Databases (Teradata, Vertica, Greenplum, Netezza), Cloud EDW (Amazon Redshift, Google BigQuery, Microsoft Azure, Snowflake), Hadoop On-Premise & Cloud (Cloudera, MapR, AWS, Azure, Google Cloud), Spark, Cluster Services, Graph Databases (Neo4j), Data Transformation/Integration (Talend, Informatica), Storage y Security.

- **Analytics:** plataformas de Data Science (Domino, DataRobot), BI Platforms (Power BI, Tableau, MicroStrategy), Visualization (Qlik, Chartio), Log Analytics (Splunk, Loggly), Machine Learning, Speech & NLP.

- **Applications:** organizadas por industria o función: Sales & Marketing (Salesforce), Customer Service, Finance, Health, Vertical AI Applications.

- **Cross-Infrastructure/Analytics:** banda horizontal con conglomerados tecnológicos: Amazon, Google, Microsoft, IBM, SAP, SAS, Oracle, Teradata.

- **Open Source:** Frameworks (YARN, Spark, Mesos), Data Access (Cassandra, HBase, MongoDB, Hive), Coordination (Zookeeper), Real-Time (Kafka, Storm, Flink), Machine Learning (TensorFlow, Caffe).

- **Data Sources & APIs:** origen de datos por campo: Health (Fitbit), IoT, Financial & Economic Data (Bloomberg, Dow Jones), Location/People/Entities.

Cada sección contiene logos de empresas y herramientas organizados en filas y columnas dentro de recuadros de colores.

(slides 3–6)

### Cada aplicación es diferente

Cada aplicación es diferente ...
● Los Datos pueden ser

     ○   (Semi-)Structured data

          ■   (Relational DBs, JSON, XML, CSV, HTML form data)

     ○   Unstructured data

          ■   (text document, comments, images, videos)

     ○   Y cualquier cosa entre ellos!!

Título «Cada aplicación es diferente ...» en la parte superior. Lista jerárquica de bullets con sub-bullets. Ejemplos en texto azul claro entre paréntesis. Punto final en cursiva: «Y cualquier cosa entre ellos!!».

Cada aplicación es diferente ...
● El Procesamiento puede implicar:
     ○   Database Management/Analytics
          ■   (indexing, querying, joins, aggregation)
     ○   Natural Language Processing
          ■   (keyword search, topic extraction, entity recognition, machine translation,
              sentiment analysis, etc.)
     ○   Data Mining and Statistics
          ■   (pattern recognition, classification, event detection, recommendations, etc.)
     ○   O algo mas / una mezcla

Título «Cada aplicación es diferente ...». Lista jerárquica bajo «El Procesamiento puede implicar:» con cuatro categorías principales y sus ejemplos en texto azul entre paréntesis. Elementos decorativos triangulares azules en la esquina superior izquierda. Elemento de diseño gris angulado en el borde derecho.

(slides 7–8)

### La escala es un factor común

La escala es un factor común ...

Tengo un algoritmo.

Tengo una máquina que
puede procesar 1000
elementos de entrada en una
hora.

Si compro una máquina que
es $n$ veces más potente,
¿cuántos elementos puedo
procesar en una hora?

Depende de lo que hace el
algoritmo !!

**Figura (slide 9):** Lado izquierdo: recuadro gris con el problema planteado en español. Debajo, recuadro verde con la respuesta «Depende de lo que hace el algoritmo !!». Lado derecho: gráfico de líneas con eje X titulado «power of machinery ($\times$ instructions per second)» con valores de 1 a 10, y eje Y titulado «input size handled per second» con valores de 0 a 10,000. Todas las curvas parten del punto $(1, 1000)$. Series de datos:
- $O(n)$ (círculos verde oscuro): línea diagonal recta; a potencia 10x maneja 10,000 elementos.
- $O(n^2)$ (cuadrados naranja): curva con rendimientos decrecientes; a 10x potencia maneja aproximadamente 3,162 elementos ($\sqrt{10} \times 1000$).
- $O(n^3)$ (círculos azul): crece aún más lento; a 10x potencia maneja poco más de 2,000 elementos.
- $O(n^4)$ (estrellas rojas): crece muy lentamente, menos de 2,000 elementos a 10x potencia.
- $O(2^n)$ (diamantes verde claro): línea horizontal plana en el nivel 1,000, mostrando que aumentar la potencia del hardware casi no proporciona ganancia para algoritmos exponenciales.

(slide 9)

## Sistemas distribuidos

### Motivación: más de una máquina

Sistemas distribuidos
● Se requiere más de una máquina!

     ○   Google ca. 1998:

**Figura (slide 10):** Encabezado «Sistemas distribuidos» en la parte superior izquierda. Logo de Google estilo 1998 (letras 3D en rojo, amarillo, verde y azul) centrado sobre la foto principal. Foto central: colección de hardware informático de finales de los 90 sobre un escritorio largo, incluyendo cuatro monitores CRT beige de distintos tamaños, múltiples teclados y ratones, varias torres de computadora de escritorio color blanco roto sobre el escritorio y debajo en el piso. Pila de dispositivos periféricos blancos más pequeños en la esquina inferior derecha. Imagen lateral izquierda: foto del famoso case de servidor temprano de Google construido con bloques LEGO de colores (azul, rojo, amarillo y verde), con un pequeño cartel informativo en un soporte. Barra azul claro en la parte inferior y acento triangular azul en la esquina superior izquierda.

Sistemas distribuidos
● Se requiere más de una máquina!

     ○   Google ca. 2014:

**Figura (slide 11):** Encabezado «Sistemas distribuidos» en la parte superior izquierda. Fotografía de un centro de datos masivo con pasillos largos de racks de servidores con luces brillantes y cableado complejo en el techo. La palabra «Google» superpuesta en el centro de la foto con su tipografía multicolor estilo 3D.

(slides 10–11)

### Sistemas monolíticos vs. distribuidos

Sistemas monolíticos vs. distribuidos

 • ¿Una máquina que es $n$    • ¿$n$ máquinas que son
   veces más poderosa?        igual de poderosas?

**Figura (slide 12):** Slide dividida en dos mitades verticales.

Lado izquierdo (fondo melocotón/naranja claro): bullet «¿Una máquina que es $n$ veces más poderosa?». Fotografía de un gabinete de computadora grande de alto rendimiento, torre negra con pantalla azul pequeña y marca «CRAY» visible en el frente, representando escalado vertical.

Lado derecho (fondo azul claro): bullet «¿$n$ máquinas que son igual de poderosas?». Fotografía de un rack de servidores con varios blade servers interconectados, con muchos cables de red azul claro/teal agrupados conectados al frente de los componentes, representando escalado horizontal.

(slide 12)

### Sistemas paralelos vs. distribuidos

Sistemas paralelos vs. distribuidos

• Sistema paralelo                   • Sistema distribuido
Generalmente memoria compartida      Generalmente no comparte memoria
                                                        Processor

 Processor   Processor   Processor                      Memory
                                         Processor

             Memory                       Memory
                                                        Processor

                                                        Memory

**Figura (slide 13):** Slide dividida en dos secciones verticales.

Sección izquierda (fondo naranja claro): texto «Sistema paralelo» y «Generalmente memoria compartida». Diagrama: un rectángulo azul grande contiene tres cajas naranjas etiquetadas «Processor» en la parte superior y una caja verde horizontal larga etiquetada «Memory» en la parte inferior. Cada uno de los tres procesadores está conectado a la memoria compartida por flechas blancas bidireccionales verticales.

Diagrama: tres cajas azules separadas idénticas dispuestas en forma triangular, cada una contiene su propia caja naranja «Processor» y su propia caja verde «Memory» conectadas internamente por flecha bidireccional blanca. Las tres nodos están enlazados entre sí por flechas azules bidireccionales formando una red.

(slide 13)

### Definición

¿Qué es un sistema distribuido?

"Un sistema distribuido es un sistema que permite que una
colección de computadoras independientes se comunique para
resolver un objetivo común."

0010010001011010100

100101110100010001001

**Figura (slide 14):** Encabezado «¿Qué es un sistema distribuido?» en la parte superior. Recuadro rectangular azul oscuro grande en la mitad superior con la definición citada en texto blanco. Las cuatro unidades están interconectadas por líneas curvas azules delgadas formando un anillo. Cada unidad tiene panel frontal con líneas de ventilación y dos luces indicadoras (roja y verde). Dos cadenas de dígitos binarios blancos cerca de los servidores representan transmisión de datos: superior izquierda «0010010001011010100» e inferior derecha «100101110100010001001». Barra azul gruesa horizontal en la parte inferior.

(slide 14)

### Costo de transporte de datos

Costo de transporte de datos
● Se requiere dividir las tareas sobre muchas máquinas

     ○   Las máquinas necesitan comunicación

         … pero no mucho!

     ○   El costo de transporte es (simplificado):

   Main
                              CPU                    Disk   Network
  Memory

                     NECESITAMOS MINIMIZAR EL COSTO DE RED

**Figura (slide 15):** Encabezado «Costo de transporte de datos». Cuatro cajas rectangulares horizontales representando componentes del sistema, donde el ancho de cada caja indica el costo relativo:
1. **Main Memory:** caja verde de ancho medio.
2. **CPU:** caja verde estrecha (menor costo / mayor velocidad).
3. **Disk:** caja verde ligeramente más ancha que CPU.
4. **Network:** caja roja muy ancha, dominando visualmente las demás, indicando que es el factor de costo más significativo.

Texto inferior subrayado en rojo y mayúsculas: «NECESITAMOS MINIMIZAR EL COSTO DE RED».

(slide 15)

### Ventajas y desventajas

Desventajas de los sistemas distribuidos

| (Posibles) Ventajas | (Posibles) Desventajas |
|---|---|
| **Costo** — Mejor desempeño/precio | **Software** — Necesita programas especiales |
| **Extensibilidad** — Agregar otra máquina! | **Redes** — Puede ser lento |
| **Confiabilidad (idealmente)** — No hay punto central de fallo! | **Mantenimiento** — Depurar sw/hw es un dolor … |
| **Carga de trabajo** — Balancea el trabajo automáticamente | **Seguridad** — Multiples usuarios remotos |
| **Compartido** — Acceso remoto a servicios | **Paralelización** — No siempre aplicable |

**Figura (slide 16):** Slide dividida en dos columnas verticales. Columna izquierda con fondo verde claro y texto verde oscuro titulada «(Posibles) Ventajas» con cinco categorías y sus descripciones. Columna derecha con fondo rosa/rojo claro y texto rojo titulada «(Posibles) Desventajas» con cinco categorías y sus descripciones. Cada categoría aparece en negrita seguida de guión y su detalle.

(slide 16)

### Un buen sistema distribuido

#### Transparencia

Un buen sistema distribuido
                     Transparencia
           … dar la impresión de un solo sistema

**Figura (slide 17):** Encabezado «Un buen sistema distribuido» en la parte superior izquierda. Barra horizontal azul oscura en la parte superior de un área rectangular azul claro con la palabra «Transparencia» subrayada y centrada. Debajo, frase centrada en blanco: «… dar la impresión de un solo sistema». Ilustración: a la izquierda, representación estilizada gris de un rack de servidores o chasis de computadora compuesto por varios módulos apilados, con panel frontal con forma ovalada vertical y dos luces de estado (verde y roja). A la derecha, icono simplificado de una persona (mujer con cabello negro y camisa azul) representando un usuario. Cinco flechas azules paralelas apuntan del usuario hacia el lado derecho del rack de servidores, visualizando la interacción del usuario con el sistema.

Un buen sistema distribuido
                              Transparencia
                … dar la impresión de un solo sistema
● Abstracción/oculto:
    ○   Acceso: Cómo se accede a las diferentes máquinas.
    ○   Ubicación: donde se encuentran físicamente las máquinas.
    ○   Heterogeneidad: diferentes software / hardware.
    ○   Concurrencia: acceso para varios usuarios.
    ○   Etc.

● ¿Cómo?
    ○   Empleando direcciones abstractas, APIs, etc..

**Figura (slide 18):** Encabezado «Un buen sistema distribuido». Debajo, dos secciones de bullets: «Abstracción/oculto:» con cinco puntos (Acceso, Ubicación, Heterogeneidad, Concurrencia, Etc.) y «¿Cómo?» con un punto sobre direcciones abstractas y APIs.

(slides 17–18)

#### Flexibilidad

Un buen sistema distribuido
                          Flexibilidad
     …Puede agregar / eliminar máquinas de forma rápida y sencilla

**Figura (slide 19):** Encabezado «Un buen sistema distribuido». Barra azul oscura con «Flexibilidad» subrayada y texto «…Puede agregar / eliminar máquinas de forma rápida y sencilla». A la derecha, icono de persona con cabello negro y camisa azul. En el centro, flecha horizontal azul apuntando de la persona hacia la unidad de servidor, sugiriendo interacción entre usuario/administrador y el hardware del sistema.

Un buen sistema distribuido
                                  Flexibilidad
         …Puede agregar / eliminar máquinas de forma rápida y sencilla

● Evita:
     ○     Tiempo de inactividad: reiniciar el sistema distribuido
     ○     Configuración compleja: 12 administradores trabajando 24/7
     ○     Requisitos específicos: supuestos de OS / HW
     ○     Etc.

● ¿Cómo?
     ○     Empleando: replicación, SW independiente de la plataforma, arranque de
           sistema, heart-beats, equilibrio de carga.

**Figura (slide 20):** Encabezado «Un buen sistema distribuido». Sección «Evita:» con cuatro bullets en rojo (Tiempo de inactividad, Configuración compleja, Requisitos específicos, Etc.). Sección «¿Cómo?» con un bullet en verde listando: replicación, SW independiente de la plataforma, arranque de sistema, heart-beats, equilibrio de carga.

(slides 19–20)

#### Confiabilidad

**Confiabilidad**

… evita fallos / sigue trabajando en caso de fallo

**Figura (slide 21):** La slide presenta el título «Un buen sistema distribuido» en la parte superior izquierda. A la izquierda del recuadro hay una ilustración de un servidor o torre de computadora de color gris con cables y puertos en los laterales; en el borde frontal derecho del servidor se ven dos luces de estado, una verde arriba y una roja abajo. A la derecha hay un avatar de una persona con cabello negro y camisa azul (sin rostro). Una flecha horizontal azul apunta desde la persona hacia el servidor, indicando la interacción del usuario con el sistema.

**Confiabilidad**

… evita fallos / sigue trabajando en caso de fallo

- Evita:
  - Tiempo de inactividad: el sistema se desconecta
  - Inconsistencia: verificar la corrección

- ¿Cómo?
  - Empleando: Replicación, enrutamiento flexible, seguridad, protocolos de consenso.

**Figura (slide 22):** La slide repite el título «Un buen sistema distribuido» y un banner azul con «Confiabilidad» subrayado y el subtítulo «… evita fallos / sigue trabajando en caso de fallo». Debajo, dos bullets principales: «Evita:» con sub-bullets en texto rojo («Tiempo de inactividad: el sistema se desconecta» e «Inconsistencia: verificar la corrección»), y «¿Cómo?» con sub-bullet en texto verde («Empleando: Replicación, enrutamiento flexible, seguridad, protocolos de consenso.»).

(slides 21–22)

#### Desempeño

**Desempeño**

… hace las cosas rápidamente

**Figura (slide 23):** La slide presenta el título «Un buen sistema distribuido» en la parte superior izquierda. En el centro, dentro de un banner azul oscuro, aparece el encabezado subrayado «Desempeño» seguido del texto «… hace las cosas rápidamente». A la izquierda hay una ilustración de un servidor o torre de computadora gris con cables azules conectados al lado izquierdo; en el frente tiene un elemento circular (como una rejilla o ventilador) y dos luces de estado (verde arriba, roja abajo). A la derecha hay un avatar de una persona con cabello negro y camisa azul (sin rostro). Una flecha horizontal azul apunta desde la persona hacia el servidor. Sobre y debajo de la flecha hay dos pequeñas figuras verdes en posición de correr, enfatizando la rapidez.

**Desempeño**

… hace las cosas rápidamente

- Evita:
  - Latencia: tiempo para la respuesta inicial
  - Largo tiempo de ejecución: tiempo para completar la respuesta
  - … básicamente evita

- ¿Cómo?
  - Empleando: Optimización de red, suficientes recursos computacionales, etc.

**Figura (slide 24):** La slide repite el título «Un buen sistema distribuido» y un banner azul con «Desempeño» subrayado y el subtítulo «… hace las cosas rápidamente». Debajo, dos bullets principales: «Evita:» con sub-bullets en texto rojo («Latencia: tiempo para la respuesta inicial», «Largo tiempo de ejecución: tiempo para completar la respuesta» y «… básicamente evita»), y «¿Cómo?» con sub-bullet en texto verde («Empleando: Optimización de red, suficientes recursos computacionales, etc.»).

(slides 23–24)

#### Escalabilidad

**Escalabilidad**

… asegura la escalabilidad de la infraestructura

**Figura (slide 25):** La slide presenta el título «Un buen sistema distribuido» en la parte superior izquierda. En el centro, dentro de un banner azul, aparece el encabezado subrayado «Escalabilidad» seguido del texto «… asegura la escalabilidad de la infraestructura». A la izquierda hay una ilustración de un servidor o hardware de red de color gris con una hendidura circular, ranuras verticales de ventilación y dos luces de estado en el borde derecho (verde arriba, roja abajo). A la derecha hay un grupo de iconos de personas: una silueta grande de cabeza en el fondo y varios iconos más pequeños de personas con cabello oscuro y camisa azul superpuestos delante. Varias flechas horizontales negras apuntan desde el grupo de usuarios hacia el servidor, representando múltiples usuarios accediendo a la infraestructura central.

**Escalabilidad**

… asegura la escalabilidad de la infraestructura

- Evita:
  - Cuellos de botella: confiar demasiado en una parte.
  - Mensajes por pares: crece cuadráticamente $O(n^2)$.

- ¿Cómo?
  - Empleando: peer-to-peer, comunicación directa, índices distribuidos, etc.

**Figura (slide 26):** La slide repite el título «Un buen sistema distribuido» y un banner azul con «Escalabilidad» subrayado y el subtítulo «… asegura la escalabilidad de la infraestructura». Debajo, dos bullets principales: «Evita:» con sub-bullets en texto rojo («Cuellos de botella: confiar demasiado en una parte.» y «Mensajes por pares: crece cuadráticamente $O(n^2)$.»), y «¿Cómo?» con sub-bullet en texto verde («Empleando: peer-to-peer, comunicación directa, índices distribuidos, etc.»).

(slides 25–26)

#### Resumen de propiedades

**Transparencia**

… dar la impresión de un solo sistema

**Flexibilidad**

…Puede agregar / eliminar máquinas de forma rápida y sencilla

**Confiabilidad**

… evita fallos / sigue trabajando en caso de fallo

**Desempeño**

… hace las cosas rápidamente

**Escalabilidad**

… asegura la escalabilidad de la infraestructura

**Figura (slide 27):** La slide presenta el título «Un buen sistema distribuido» en la parte superior izquierda. Debajo, cinco bloques rectangulares horizontales de color azul apilados verticalmente, cada uno con texto en blanco. Cada bloque contiene un término subrayado seguido de su descripción: «Transparencia» con «… dar la impresión de un solo sistema», «Flexibilidad» con «…Puede agregar / eliminar máquinas de forma rápida y sencilla», «Confiabilidad» con «… evita fallos / sigue trabajando en caso de fallo», «Desempeño» con «… hace las cosas rápidamente», y «Escalabilidad» con «… asegura la escalabilidad de la infraestructura».

(slide 27)

## Base de Datos Distribuidas

- BD distribuida:
  - Son varias BD interrelacionadas lógicamente y situadas en diferentes nodos de una red de ordenadores
- SGBD distribuido:
  - Es el software que gestiona las BD distribuidas de forma transparente para el usuario. El usuario ve a las BD como si fuera una sola BD centralizada.
- Ventajas:
  - Localización transparente de los datos
  - Transparencia en los nombres
  - Transparencia de fragmentación

**Figura (slide 28):** La slide presenta el título «Base de Datos Distribuidos» en fuente grande negra en la parte superior. Debajo, tres bullets principales con sub-bullets: «BD distribuida:», «SGBD distribuido:» y «Ventajas:» con sus respectivos puntos.

(slide 28)

**Tópicos del curso:**

1. Diseño de base de datos distribuidas
   - Fragmentación Horizontal
   - Fragmentación Vertical
2. Procesamiento de consultas
   - Descomposición
   - Localización
   - Optimización
3. NoSQL
   - MongoDB
   - Cassandra
   - Redis

**Figura (slide 29):** Slide de agenda con fotografía de fondo de dos personas en un entorno de laboratorio o ingeniería trabajando con maquinaria compleja, cubierta por un degradado azul. El título «Tópicos» aparece en blanco en el centro-izquierda. En la parte inferior, un elemento decorativo de líneas punteadas y sólidas en amarillo y azul que simula un circuito o ruta de datos. La lista numerada de tres secciones con sus sub-tópicos aparece superpuesta sobre el fondo.

(slides 28–29)

## Diseño de BDD

### Enfoques de fragmentación

- Fragmentar: decidir dónde situar las partes de la BDD
  - Se puede plantear dos enfoques
    - Bottom-up
      - Ya existen múltiples base de datos (en diferentes sitios)
      - A uno individual
      - No hay problemas de diseño!!
    - Top-down
      - Comience con una pizarra en blanco (desde cero)
      - Similar al diseño centralizado de DB
      - Se presentan problemas de diseño!!

**Figura (slide 31):** La slide presenta el título «Diseño de BDD» en la parte superior. Debajo, un bullet principal «Fragmentar: decidir dónde situar las partes de la BDD» con sub-bullets anidados que describen los dos enfoques Bottom-up y Top-down con sus respectivos puntos.

(slide 31)

### Bottom-up

- Bottom-up

**Figura (slide 32):** La slide presenta el título «Diseño de BDD» y el bullet «Bottom-up» subrayado. Debajo, un diagrama de arquitectura en cinco niveles horizontales que ilustra la integración bottom-up de bases de datos locales:

1. **Nivel inferior (Local DB):** Tres iconos de cilindros de base de datos en la base, cada uno etiquetado «Local DB», representando bases de datos locales autónomas.
2. **Nivel Local Conceptual Schema:** Desde cada «Local DB» sube una flecha a un rectángulo etiquetado «Local Conceptual Schema», representando el esquema conceptual de cada BD local.
3. **Nivel Export Schema:** Flechas desde los esquemas conceptuales locales hacia rectángulos «Export Schema». El esquema conceptual izquierdo apunta a dos Export Schemas distintos; el del centro apunta a uno; el de la derecha apunta a dos Export Schemas distintos. Estos esquemas definen qué partes de los datos locales son visibles al sistema distribuido.
4. **Nivel Schema Integration:** Óvalos etiquetados «Schema Integration» actúan como puntos de convergencia. El óvalo izquierdo recibe flechas de los dos primeros Export Schemas; el óvalo central recibe flechas del segundo y tercer Export Schema (mostrando solapamiento); el óvalo derecho recibe flechas del cuarto y quinto Export Schema.
5. **Nivel superior (Unified Schema):** Desde cada óvalo de Schema Integration sube una flecha a un rectángulo «Unified Schema» en la parte superior. Hay tres Unified Schemas, representando las vistas globales integradas del sistema distribuido.

El diagrama es un dibujo lineal en blanco y negro.

(slide 32)

### Top-down

- Top-down

**Figura (slide 33):** La slide presenta el título «Diseño de BDD» y el bullet «Top-down» subrayado. Debajo, un diagrama de flujo que detalla las etapas del diseño top-down de una base de datos distribuida:

- En la parte superior, el nodo «Requirements» (Requisitos) es el punto de partida.
- Desde «Requirements» el proceso se bifurca en dos vías paralelas:
  - **Vía izquierda:** «Conceptual design» → «Global schema»
  - **Vía derecha:** «View design» → «External schema»
  - Entre «Conceptual design» y «View design» hay una flecha bidireccional horizontal, indicando interdependencia.
- Tanto «Global schema» como «External schema» alimentan con flechas hacia abajo un recuadro central en negrita «Distribution design» (diseño de distribución), etapa central donde se toman decisiones de fragmentación y asignación.
- Desde «Distribution design» el flujo continúa hacia abajo a través de: «Local schemas» → «Physical design» → «Monitoring».
- Una flecha etiquetada «feedback» va desde «Monitoring» de vuelta hacia «Requirements», indicando un ciclo iterativo de diseño.

(slide 33)

### Nuevos problemas

- Nuevos Problemas!!

  - ¿Cómo dividimos los datos? (fragmentación)
  - ¿En donde debe ir cada fragmento? (Asignación)

  →No son independiente, pero los cubriremos por separado!!

**Figura (slide 34):** La slide presenta el título «Diseño de BDD» y el bullet «Nuevos Problemas!!» seguido de dos sub-bullets con las preguntas sobre fragmentación y asignación, y una flecha (→) con la nota de que no son independientes pero se cubrirán por separado.

(slide 34)

### Ejemplo: relación Empleado

- Ejemplo:

  - Sea la relación Empleado
    - $E(id, name, salary, location, …)$
    - $Q_A$ – 40 % de consultas:

```sql
select * from E where location = A and ...
```

    - $Q_B$ – 40 % de consultas:

```sql
select * from E where location = B and ...
```

    - Motivación: dos sitos A, B

**Figura (slide 35):** La slide presenta el título «Diseño de BDD» y el bullet «Ejemplo:» con sub-bullets que definen la relación Empleado $E(id, name, salary, location, …)$, las consultas $Q_A$ y $Q_B$ (cada una con 40 % de consultas y su respectiva sentencia SQL), y la motivación «dos sitos A, B». En la parte inferior, un diagrama simple: una flecha desde la etiqueta «$Q_A$» apunta hacia un recuadro con la letra «A»; otra flecha desde la etiqueta «$Q_B$» apunta hacia un recuadro con la letra «B».

(slide 35)

## Fragmentación

### Ejemplo: tabla E

- Dividir los datos de la tabla E …

Tabla **E** (datos originales):

| id | name | location | salary |
|---|---|---|---|
| 1 | Tom | A | 15 |
| 2 | Ann | B | 23 |
| 3 | Ben | A | 21 |

**Figura (slide 36):** La slide presenta el título «Fragmentación» y el bullet «Dividir los datos de la tabla E …». Debajo, la tabla E con cuatro columnas (id, name, location, salary) y tres filas de datos (Tom/A/15, Ann/B/23, Ben/A/21). En el centro del diagrama, un icono etiquetado «F» con dos flechas divergentes hacia abajo indica el proceso de fragmentación. El resultado son dos tablas fragmentadas:

- **Fragmento A** (etiquetado con recuadro «A»): contiene las filas donde location = A.

| id | name | location | salary |
|---|---|---|---|
| 1 | Tom | A | 15 |
| 3 | Ben | A | 21 |

- **Fragmento B** (etiquetado con recuadro «B»): contiene la fila donde location = B.

| id | name | location | salary |
|---|---|---|---|
| 2 | Ann | B | 23 |

El esquema (id, name, location, salary) se mantiene idéntico en la tabla original y en ambos fragmentos.

- Dividir los datos de la tabla E …

$$F = \{F_1, F_2\}$$

$$F_1 = \sigma_{location=A}\, E$$

$$F_2 = \sigma_{location=B}\, E$$

→ Fragmentación horizontal primaria

**Figura (slide 37):** La slide presenta el título «Fragmentación» y el bullet «Dividir los datos de la tabla E …». En el centro aparecen las fórmulas de álgebra relacional: el conjunto de fragmentos $F = \{F_1, F_2\}$, el fragmento $F_1$ definido como la selección $\sigma_{location=A}\, E$ (filas de E donde location = A), y el fragmento $F_2$ definido como $\sigma_{location=B}\, E$ (filas de E donde location = B). En la parte inferior, una flecha (→) apunta al texto «Fragmentación horizontal primaria».

(slides 36–37)

### Tipos de fragmentación

**Horizontal**

Primaria:
- Usando predicados solo en E

Derivada:
- Usando predicados de relaciones foráneas
- $F_i = E \Join S_i$, $1 \leq i \leq n$

**Vertical**

**Figura (slide 38):** La slide presenta el título «Fragmentación» dividido en dos secciones separadas por una línea horizontal azul.

**Sección superior — Horizontal:** A la izquierda, un diagrama de un rectángulo (tabla) dividido en dos cajas apiladas horizontalmente (una arriba, otra abajo); una flecha apunta hacia la derecha desde la caja superior y otra hacia la izquierda desde la caja inferior, ilustrando la división por filas. A la derecha del diagrama, el texto «Primaria:» con bullet «Usando predicados solo en E», y «Derivada:» con bullets «Usando predicados de relaciones foráneas» y la fórmula $F_i = E \Join S_i$, $1 \leq i \leq n$.

**Sección inferior — Vertical:** A la izquierda, un diagrama de un rectángulo (tabla) dividido en dos cajas colocadas lado a lado (una a la izquierda, otra a la derecha); una flecha apunta hacia arriba desde la caja derecha y otra hacia abajo desde la caja izquierda, ilustrando la división por columnas. A la derecha aparece únicamente el encabezado «Vertical» sin texto adicional.

(slide 38)

## Fragmentación Horizontal

### Técnicas de particionamiento

- Técnicas de particionamiento

  - Round robin
  - Hash (atributos discretos)
  - Range (atributos discretos, continuos)
  - List (atributos categóricos)

**Figura (slide 40):** La slide presenta el título «Fragmentación Horizontal» en la parte superior izquierda. Debajo, un bullet principal «Técnicas de particionamiento» con cuatro sub-bullets anidados: «Round robin», «Hash (atributos discretos)», «Range (atributos discretos, continuos)» y «List (atributos categóricos)».

(slide 40)

### Particionamiento Round robin

- **Particionamiento Round robin**

  - Distribuye los datos de manera uniforme.
  - Bueno para escanear una relación completa
  - No es bueno para consultas puntuales o por rango

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Particionamiento Round robin». Tres viñetas a la derecha con las características del método. En el centro, diagrama con cuatro columnas verticales: a la izquierda la relación $R$ con tuplas $t_1, t_2, t_3, t_4, t_5, \dots$; a la derecha tres fragmentos $F_1$, $F_2$ y $F_3$, cada uno como rectángulo vertical. Flechas muestran la distribución cíclica: $t_1 \rightarrow F_1$, $t_2 \rightarrow F_2$, $t_3 \rightarrow F_3$, $t_4 \rightarrow F_1$, $t_5 \rightarrow F_2$, y puntos suspensivos indican que el patrón continúa.

(slide 41)

### Particionamiento Hash

- **Particionamiento Hash**

  - Distribuye los datos uniformemente si la función hash es buena.
  - Bueno para consultas puntuales sobre claves y uniones.
  - No es bueno para consultas por rango y consultas puntuales que no están en clave.

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Particionamiento Hash». Tres viñetas a la derecha con las características del método. En el centro, diagrama con la relación $R$ a la izquierda conteniendo tuplas $t_1, t_2, t_3, t_4, t_5, \dots$. Cada tupla se asocia a una clave $k_n$ y se aplica la función hash $h(k_n)$: $t_1 \rightarrow h(k_1) = 2 \rightarrow F_2$; $t_2 \rightarrow h(k_2) = 1 \rightarrow F_1$; $t_3 \rightarrow h(k_3) = 3 \rightarrow F_3$; $t_4 \rightarrow h(k_4) = 3 \rightarrow F_3$; $t_5 \rightarrow h(k_5) = 2 \rightarrow F_2$. A la derecha, tres fragmentos $F_1$ (contiene $t_2$), $F_2$ (contiene $t_1$ y $t_5$) y $F_3$ (contiene $t_3$ y $t_4$).

(slide 42)

### Particionamiento Range

- **Particionamiento Range**

  - Bueno para consultas por rango en el atributo de partición.
  - Necesidad de seleccionar un buen vector para evitar sesgo de datos / ejecución.

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Particionamiento Range». Dos viñetas a la derecha. En el centro, diagrama con la relación $R$ a la izquierda con tuplas $t_1$ ($a_1 = 5$), $t_2$ ($a_2 = 2$), $t_3$ ($a_3 = 9$), $t_4$ ($a_4 = 8$), $t_5$ ($a_5 = 4$). Arriba, un «Partition vector» con valores $[4, 7]$. Líneas punteadas desde el vector definen tres fragmentos: $F_1$ recibe tuplas con $a < 4$ ($t_2$, $a=2$); $F_2$ recibe tuplas con $4 \le a \le 7$ ($t_1$, $a=5$ y $t_5$, $a=4$); $F_3$ recibe tuplas con $a > 7$ ($t_3$, $a=9$ y $t_4$, $a=8$).

(slide 43)

### ¿Buena fragmentación?

- **¿Buena fragmentación?**
  - **Ejemplo 1:**

$$F = \{F_1, F_2\}$$

$$F_1 = \sigma_{\text{salary} < 10} E$$

$$F_2 = \sigma_{\text{salary} > 20} E$$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «¿Buena fragmentación?» con sub-viñeta «Ejemplo 1:». Tres fórmulas en notación de álgebra relacional: el conjunto de fragmentos $F = \{F_1, F_2\}$, el fragmento $F_1$ como selección de $E$ donde salary es menor que 10, y el fragmento $F_2$ como selección de $E$ donde salary es mayor que 20.

- **¿Buena fragmentación?**
  - **Ejemplo 1:**

$$F = \{F_1, F_2\}$$

$$F_1 = \sigma_{\text{salary} < 10} E$$

$$F_2 = \sigma_{\text{salary} > 20} E$$

→ Problema: algunas tuplas se pierden ($10 \le \text{salary} < 20$)

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «¿Buena fragmentación?» con sub-viñeta «Ejemplo 1:». Mismas tres fórmulas de fragmentación que en la slide anterior. Debajo, texto con flecha indicando el problema: «Problema: algunas tuplas se pierden ($10 \le \text{salary} < 20$)».

- **¿Buena fragmentación?**
  - **Ejemplo 2:**

$$F = \{F_3, F_4\}$$

$$F_3 = \sigma_{\text{salary} < 10} E$$

$$F_4 = \sigma_{\text{salary} > 5} E$$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «¿Buena fragmentación?» con sub-viñeta «Ejemplo 2:». Tres fórmulas en notación de álgebra relacional: el conjunto de fragmentos $F = \{F_3, F_4\}$, el fragmento $F_3$ como selección de $E$ donde salary es menor que 10, y el fragmento $F_4$ como selección de $E$ donde salary es mayor que 5.

- **¿Buena fragmentación?**
  - **Ejemplo 2:**

$$F = \{F_3, F_4\}$$

$$F_3 = \sigma_{\text{salary} < 10} E$$

$$F_4 = \sigma_{\text{salary} > 5} E$$

→ Problema: algunas tuplas duplicadas ($5 < \text{salary} < 10$)

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «¿Buena fragmentación?» con sub-viñeta «Ejemplo 2:». Mismas tres fórmulas de fragmentación que en la slide anterior. Debajo, texto con flecha indicando el problema: «Problema: algunas tuplas duplicadas ($5 < \text{salary} < 10$)».

(slides 44–47)

### Propiedades de la fragmentación

- **Propiedades de la fragmentación:**

  - Sea $R$ una relación que se fragmenta en un conjunto de fragmentos $\mathbf{F} = \{F_1, F_2, \dots\}$
  - Las propiedades deseadas para una fragmentación horizontal son:
    - **Completitud**

$$\forall t \in R, \exists F_i \in \mathbf{F} : t \in F_i$$

    - **Desarticulación**

$$\forall t \in F_i, \neg \exists F_j : t \in F_j, \; i \neq j, \; \{F_i, F_j\} \subset \mathbf{F}$$

    - **Reconstrucción**

$$R = \bigcup_{F_i \in \mathbf{F}} F_i$$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Propiedades de la fragmentación:». Sub-viñeta «Sea $R$ una relación que se fragmenta en un conjunto de fragmentos $\mathbf{F} = \{F_1, F_2, \dots\}$». Sub-viñeta «Las propiedades deseadas para una fragmentación horizontal son:» seguida de tres sub-viñetas con negrita: «Completitud», «Desarticulación» y «Reconstrucción», cada una con su fórmula en LaTeX debajo.

(slide 48)

### Cómo asegurar completitud y desarticulación

- **¿Cómo asegurar la completitud y la desarticulación?**

  1. Verificación manual

$$F_1 = \sigma_{\text{salary} \le 5} E \quad \checkmark$$

$$F_2 = \sigma_{\text{salary} > 5} E \quad \checkmark$$

  2. Genera automáticamente fragmentos que cumplan dichas propiedades.

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «¿Cómo asegurar la completitud y la desarticulación?». Numeración «1. Verificación manual» seguida de dos ecuaciones con operador de selección: $F_1 = \sigma_{\text{salary} \le 5} E$ y $F_2 = \sigma_{\text{salary} > 5} E$, cada una con un checkmark ($\checkmark$) a la derecha. Numeración «2. Genera automáticamente fragmentos que cumplan dichas propiedades.»

(slide 49)

### Predicados Minterm (Términos Mínimos)

- **Predicados Minterm (Términos Mínimos)**

  1. Considerar los predicados simples utilizados en las consultas.
     - Ej.: `salary < 10`, `salary > 5`, `location = A`, `location = B`
  2. Generar todos predicados minterm posibles
  3. Eliminar los inútiles

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm (Términos Mínimos)». Tres pasos numerados: el primero con sub-viñeta de ejemplo con cuatro predicados simples (`salary < 10`, `salary > 5`, `location = A`, `location = B`); el segundo «Generar todos predicados minterm posibles»; el tercero «Eliminar los inútiles».

(slide 50)

### Generación de predicados minterm

- **Predicados Minterm**

  - (1) $\text{sal} < 10 \land \text{sal} > 5 \land \text{loc} = A \land \text{loc} = B$
  - (2) $\text{sal} < 10 \land \text{sal} > 5 \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (3) $\text{sal} < 10 \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (4) $\text{sal} < 10 \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$
  - (5) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \text{loc} = A \land \text{loc} = B$
  - (6) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (7) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (8) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Lista numerada del (1) al (8) con ocho expresiones lógicas, cada una con cuatro términos unidos por el operador $\land$, combinando condiciones sobre `sal` (salary) y `loc` (location) con sus negaciones $\neg$.

- **Predicados Minterm**

  - (1) $\text{sal} < 10 \land \text{sal} > 5 \land \text{loc} = A \land \text{loc} = B$
  - (2) $\text{sal} < 10 \land \text{sal} > 5 \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (3) $\text{sal} < 10 \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (4) $\text{sal} < 10 \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$
  - (5) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \text{loc} = A \land \text{loc} = B$
  - (6) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (7) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (8) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Misma lista de ocho predicados minterm del (1) al (8) que en la slide anterior, con líneas horizontales rojas de tachado: las filas (1), (4), (5) y (8) están completamente tachadas; en las filas (2) y (6) solo se tacha el término $\neg(\text{loc} = B)$; en las filas (3) y (7) solo se tacha el término $\neg(\text{loc} = A)$.

- **Predicados Minterm**

  - (1) $\text{sal} < 10 \land \text{sal} > 5 \land \text{loc} = A \land \text{loc} = B$
  - (2) $\text{sal} < 10 \land \text{sal} > 5 \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (3) $\text{sal} < 10 \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (4) $\text{sal} < 10 \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$
  - (5) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \text{loc} = A \land \text{loc} = B$
  - (6) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (7) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (8) $\text{sal} < 10 \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$
  - $5 < \text{sal} < 10$
  - $\text{sal} \le 5$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Misma lista de ocho predicados del (1) al (8) con tachados rojos como en la slide anterior. En las filas (2) y (3), un recuadro azul redondeado agrupa $\text{sal} < 10 \land \text{sal} > 5$ con nota manuscrita en azul «$5 < \text{sal} < 10$» encima; el término $\neg(\text{loc} = B)$ está tachado en rojo en la fila (2) y el término $\neg(\text{loc} = A)$ en la fila (3). En las filas (6) y (7), un recuadro azul agrupa $\text{sal} < 10 \land \neg(\text{sal} > 5)$ con nota manuscrita en azul «$\text{sal} \le 5$» debajo; el término $\neg(\text{loc} = B)$ está tachado en rojo en la fila (6) y el término $\neg(\text{loc} = A)$ en la fila (7). Las filas (1), (4), (5) y (8) permanecen completamente tachadas en rojo.

- **Predicados Minterm**

  - (9) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \text{loc} = A \land \text{loc} = B$
  - (10) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (11) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (12) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$
  - (13) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \text{loc} = A \land \text{loc} = B$
  - (14) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (15) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (16) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Lista numerada del (9) al (16) con ocho expresiones lógicas, cada una comenzando con $\neg(\text{sal} < 10)$ y combinando condiciones sobre `sal` y `loc` con el operador $\land$ y negaciones $\neg$, siguiendo un patrón de tabla de verdad para los tres últimos términos.

- **Predicados Minterm**

  - (9) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \text{loc} = A \land \text{loc} = B$
  - (10) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (11) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (12) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$
  - (13) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \text{loc} = A \land \text{loc} = B$
  - (14) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (15) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (16) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Lista de predicados minterm del (9) al (16) con líneas horizontales rojas de tachado en las filas (9), (12), (13), (14), (15) y (16). Las filas (10) y (11) permanecen sin tachar.

- **Predicados Minterm**

  - (9) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \text{loc} = A \land \text{loc} = B$
  - (10) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (11) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (12) $\neg(\text{sal} < 10) \land \text{sal} > 5 \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$
  - (13) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \text{loc} = A \land \text{loc} = B$
  - (14) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \text{loc} = A \land \neg(\text{loc} = B)$
  - (15) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \text{loc} = B$
  - (16) $\neg(\text{sal} < 10) \land \neg(\text{sal} > 5) \land \neg(\text{loc} = A) \land \neg(\text{loc} = B)$
  - $\text{sal} \ge 10$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Misma lista de predicados del (9) al (16) con tachados rojos en las filas (9), (12), (13), (14), (15) y (16). En las filas (10) y (11), un recuadro azul redondeado agrupa el prefijo $\neg(\text{sal} < 10) \land \text{sal} > 5$ con nota manuscrita en azul «$\text{sal} \ge 10$» encima apuntando al recuadro.

(slides 51–56)

### Fragmentos finales

- **Predicados Minterm**

  - **Fragmentos finales**

    - $F_2$: $5 < \text{salary} < 10 \land \text{location} = A$
    - $F_3$: $5 < \text{salary} < 10 \land \text{location} = B$
    - $F_6$: $\text{salary} \le 5 \land \text{location} = A$
    - $F_7$: $\text{salary} \le 5 \land \text{location} = B$
    - $F_{10}$: $\text{salary} \ge 10 \land \text{location} = A$
    - $F_{11}$: $\text{salary} \ge 10 \land \text{location} = B$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm» con sub-viñeta «Fragmentos finales». Seis fragmentos listados con sus predicados: $F_2$, $F_3$, $F_6$, $F_7$, $F_{10}$ y $F_{11}$, cada uno definido por una combinación de condiciones sobre `salary` y `location` unidas por $\land$.

(slide 57)

### Semántica de la aplicación y fragmentos adicionales

- **Predicados Minterm**

  - La eliminación de fragmentos inútiles depende de la ***semántica de la aplicación***.
  - Ejercicio: si la ubicación podría ser distinta de A o B, ¿Qué fragmentos se debería agregar?:

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Sub-viñeta «La eliminación de fragmentos inútiles depende de la semántica de la aplicación.» (con «semántica de la aplicación» en cursiva/negrita). Sub-viñeta con el ejercicio: «si la ubicación podría ser distinta de A o B, ¿Qué fragmentos se debería agregar?:»

- **Predicados Minterm**

  - La eliminación de fragmentos inútiles depende de la ***semántica de la aplicación***.
  - Ejercicio: si la ubicación podría ser distinta de A o B, ¿Qué fragmentos se debería agregar?:

    - $F_4$: $5 < \text{salary} < 10 \land \text{location} \neq A \land \text{location} \neq B$
    - $F_8$: $\text{salary} \le 5 \land \text{location} \neq A \land \text{location} \neq B$
    - $F_{12}$: $\text{salary} \ge 10 \land \text{location} \neq A \land \text{location} \neq B$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Mismas dos sub-viñetas que en la slide anterior (semántica de la aplicación y enunciado del ejercicio). Debajo, tres fragmentos adicionales: $F_4$, $F_8$ y $F_{12}$, cada uno con predicado que incluye $\text{location} \neq A \land \text{location} \neq B$ combinado con un rango de `salary`.

(slides 58–59)

### Por qué funciona la técnica de minterms

- **Predicados Minterm**

  - ¿Por qué funciona esta técnica?
  - Para ilustrar, consideremos las predicados simples $p_1, p_2, p_3, p_4$
  - Predicados Minterm:

$$p_1 \land p_2 \land p_3 \land p_4$$

$$p_1 \land p_2 \land p_3 \land \neg p_4$$

$$\vdots$$

$$\neg p_1 \land \neg p_2 \land \neg p_3 \land \neg p_4$$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm». Sub-viñeta «¿Por qué funciona esta técnica?». Sub-viñeta «Para ilustrar, consideremos las predicados simples $p_1, p_2, p_3, p_4$». Sub-viñeta «Predicados Minterm:» seguida de cuatro expresiones lógicas alineadas en columnas: la primera $p_1 \land p_2 \land p_3 \land p_4$, la segunda $p_1 \land p_2 \land p_3 \land \neg p_4$, puntos suspensivos verticales ($\vdots$) en el centro, y la última $\neg p_1 \land \neg p_2 \land \neg p_3 \land \neg p_4$.

(slide 60)

### Completitud y desarticulación con minterms

- **Predicados Minterm**

  - **(1) ¿Completitud?**
    - $\forall t \in R: p_i(t)$ es verdadero o falso
    - Digamos que, $p_1(t)$ y $p_2(t)$ son verdaderos, $p_3(t)$ y $p_4(t)$ son falsos
    - Entonces $t$ está en el fragmento con predicado

$$p_1 \wedge p_2 \wedge \neg p_3 \wedge \neg p_4$$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm» en negrita. Sub-viñeta «(1) ¿Completitud?» en negrita, seguida de tres sub-viñetas indentadas. La primera contiene la fórmula $\forall t \in R: p_i(t)$ es verdadero o falso. La segunda describe el ejemplo con $p_1(t)$ y $p_2(t)$ verdaderos y $p_3(t)$ y $p_4(t)$ falsos. La tercera concluye «Entonces $t$ está en el fragmento con predicado» seguida de la fórmula en bloque: $p_1 \wedge p_2 \wedge \neg p_3 \wedge \neg p_4$.

- **Predicados Minterm**

  - **(1) ¿Desarticulación?**
    - Digamos que $t$ está en el fragmento con predicado $p_1 \land p_2 \land \neg p_3 \land \neg p_4$
    - Entonces $p_1(t)$ y $p_2(t)$ son verdaderas; $p_3(t)$ y $p_4(t)$ son falsas
    - No hay otro fragmento en el que pueda estar $t$.

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm» en negrita. Sub-viñeta «(1) ¿Desarticulación?» en negrita, seguida de tres sub-viñetas indentadas. La primera indica que $t$ está en el fragmento con predicado $p_1 \land p_2 \land \neg p_3 \land \neg p_4$. La segunda establece que entonces $p_1(t)$ y $p_2(t)$ son verdaderas y $p_3(t)$ y $p_4(t)$ son falsas. La tercera concluye que no hay otro fragmento en el que pueda estar $t$.

(slides 61–62)

### Resumen de predicados minterm

- **Predicados Minterm: Resumen**

  - Dado un conjunto de predicados simples $P = \{ p_1, p_2, \dots, p_n \}$,
    - Los predicados minterms son:
    - En donde $p_k^*$ es o bien $p_k$ o $\neg p_k$

$$M = \{ m \mid m = \bigwedge_{1 \leq k \leq n} p_k^* \}$$

- Los fragmentos $\sigma_m R$ para todo $m \in M$ son completos y desarticulados.

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Predicados Minterm: Resumen» en negrita. Sub-viñeta con el conjunto de predicados simples $P = \{ p_1, p_2, \dots, p_n \}$, seguida de dos sub-viñetas indentadas: «Los predicados minterms son:» y «En donde $p_k^*$ es o bien $p_k$ o $\neg p_k$». Fórmula en bloque centrada: $M = \{ m \mid m = \bigwedge_{1 \leq k \leq n} p_k^* \}$. Viñeta final: «Los fragmentos $\sigma_m R$ para todo $m \in M$ son completos y desarticulados.»

(slide 63)

### Patrones de Acceso Coincidentes

- **Patrones de Acceso Coincidentes**

  - Otra propiedad de fragmentación deseada.

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Patrones de Acceso Coincidentes» en negrita, seguida de la sub-viñeta «Otra propiedad de fragmentación deseada.» En el centro, tres rectángulos apilados verticalmente etiquetados «Data A», «Data B» y «Data C». A la izquierda, una llave vertical agrupa los tres rectángulos con el texto «Frecuentemente son accedidos de manera conjunta.» A la derecha, otra llave vertical agrupa los mismos tres rectángulos con el texto «Entonces tratar de colocarlos en el mismo fragmento.»

- **Patrones de Acceso Coincidentes**

  - Tomemos el ejemplo definido anteriormente:

$E(id, name, salary, location, \dots)$

- $Q_A$ (40% de las consultas):

```sql
select *
from E
where location = A and ...
```

- $Q_B$ (40% de las consultas):

```sql
select *
from E
where location = B and ...
```

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Patrones de Acceso Coincidentes» en negrita. Sub-viñeta «Tomemos el ejemplo definido anteriormente:». Esquema de relación $E(id, name, salary, location, \dots)$. Dos consultas etiquetadas $Q_A$ y $Q_B$, cada una indicando «40% de las consultas», con bloques SQL correspondientes que filtran por `location = A` y `location = B` respectivamente.

(slides 64–65)

### Opciones de fragmentación y consultas

- **Patrones de Acceso Coincidentes**

  - Consideremos las siguientes opciones de fragmentación:

    - **(1)** $P = \{ \}$, $F_1 = \{ E \}$
    - **(2)** $P = \{ \text{location} = A, \text{location} = B \}$, $F_2 = \{ \sigma_{\text{location}=A}E, \sigma_{\text{location}=B}E \}$
    - **(3)** $P = \{ \text{location} = A, \text{location} = B, \text{salary} < 10 \}$, $F_3 = \{ \sigma_{\text{location}=A \land \text{salary}<10}E, \sigma_{\text{location}=A \land \text{salary}\ge10}E, \sigma_{\text{location}=B \land \text{salary}<10}E, \sigma_{\text{location}=B \land \text{salary}\ge10}E \}$

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Patrones de Acceso Coincidentes» en negrita. Sub-viñeta «Consideremos las siguientes opciones de fragmentación:» seguida de tres opciones numeradas (1), (2) y (3), cada una definiendo un conjunto de predicados $P$ y el conjunto de fragmentos resultante $F_1$, $F_2$ o $F_3$ con operaciones de selección $\sigma$ sobre la relación $E$.

- **Patrones de Acceso Coincidentes**

  - Consideremos las siguientes opciones de fragmentación:

Título «Fragmentación Horizontal» en la parte superior. Viñeta principal «Patrones de Acceso Coincidentes» en negrita. Sub-viñeta «Consideremos las siguientes opciones de fragmentación:». En el centro-izquierda, cuatro cajas rectangulares apiladas verticalmente con los predicados: `location = A ∧ salary < 10`, `location = A ∧ salary ≥ 10`, `location = B ∧ salary < 10`, `location = B ∧ salary ≥ 10`. Tres esquemas de fragmentación con llaves:

- **$F_1$:** cada caja es un fragmento individual (cuatro fragmentos).
- **$F_2$:** las dos primeras cajas agrupadas en un fragmento (`location = A`) y las dos últimas en otro (`location = B`).
- **$F_3$:** las cuatro cajas agrupadas en un solo fragmento.

A la derecha, dos consultas:

- $Q_A$ = `select ... location = A ...`
- $Q_B$ = `select ... location = B ...`

Flecha desde las consultas hacia la conclusión: **$F_2$ is good (not $F_1$ and $F_3$)**.

(slides 66–67)

## Fragmentación Horizontal Derivada

### Contexto y relaciones

- Sean las relaciones:

$E(id, name, salary, location, \dots)$

$F = \{F_1, F_2\}$ by location

$T(id, task, \dots)$

- Una consulta común para tareas:
  - Dado el nombre del empleado, listar las tareas en las que trabaja.

Título «Fragmentación Horizontal Derivada» en la parte superior. Viñeta «Sean las relaciones:» seguida de las definiciones de $E(id, name, salary, location, \dots)$, $F = \{F_1, F_2\}$ by location, y $T(id, task, \dots)$. Viñeta «Una consulta común para tareas:» con sub-viñeta «Dado el nombre del empleado, listar las tareas en las que trabaja.»

(slide 68)

### Ejemplo con semijoin

**Tabla $E_1$:**

| id | name | location | salary |
|----|------|----------|--------|
| 1  | Tom  | A        | 15     |
| 3  | Ben  | A        | 21     |

**Tabla $E_2$:**

| id | name | location | salary |
|----|------|----------|--------|
| 2  | Ann  | B        | 23     |
| 4  | Max  | B        | 17     |

**Tabla $T$:**

| id | task      |
|----|-----------|
| 1  | design    |
| 1  | build     |
| 2  | advertise |
| 4  | sell      |

Título «Fragmentación Horizontal Derivada» en la parte superior. Tres tablas dispuestas horizontalmente: $E_1$ (fragmento con empleados en location A), $E_2$ (fragmento con empleados en location B), y $T$ (tabla de tareas con referencias por id). Las tablas $E_1$ y $E_2$ tienen columnas `id`, `name`, `location`, `salary`. La tabla $T$ tiene columnas `id` y `task`.

**Tabla $E_1$:**

| id | name | location | salary |
|----|------|----------|--------|
| 1  | Tom  | A        | 15     |
| 3  | Ben  | A        | 21     |

**Tabla $E_2$:**

| id | name | location | salary |
|----|------|----------|--------|
| 2  | Ann  | B        | 23     |
| 4  | Max  | B        | 17     |

**Tabla $T_1$:**

| id | task   |
|----|--------|
| 1  | design |
| 1  | build  |

**Tabla $T_2$:**

| id | task      |
|----|-----------|
| 2  | advertise |
| 4  | sell      |

$$T_1 = T \ltimes E_1$$

$$T_2 = T \ltimes E_2$$

Título «Fragmentación Horizontal Derivada» en la parte superior. Cuatro tablas en dos pares: arriba $E_1$ y $E_2$ (fragmentos de empleados), abajo $T_1$ y $T_2$ (fragmentos derivados de tareas). $T_1$ contiene las tareas de los empleados con id en $E_1$ (id 1: design, build). $T_2$ contiene las tareas de los empleados con id en $E_2$ (id 2: advertise, id 4: sell). En la parte inferior, las fórmulas $T_1 = T \ltimes E_1$ y $T_2 = T \ltimes E_2$.

**Tabla $E_1$:**

| id | name | location | salary |
|----|------|----------|--------|
| 1  | Tom  | A        | 15     |
| 3  | Ben  | A        | 21     |

**Tabla $E_2$:**

| id | name | location | salary |
|----|------|----------|--------|
| 2  | Ann  | B        | 23     |
| 4  | Max  | B        | 17     |

**Tabla $T_1$:**

| id | task   |
|----|--------|
| 1  | design |
| 1  | build  |

**Tabla $T_2$:**

| id | task      |
|----|-----------|
| 2  | advertise |
| 4  | sell      |

$$T_1 = T \ltimes E_1$$

$$T_2 = T \ltimes E_2$$

$$R \ltimes S = \{ t : t \in R \wedge \exists s \in S(Fun (t \cup s)) \}$$

where $Fun(r)$ is as in the definition of natural join.

¿Cómo es el semijoin $\ltimes$ en SQL?

Título «Fragmentación Horizontal Derivada» en la parte superior. Mismas cuatro tablas que en la slide anterior ($E_1$, $E_2$, $T_1$, $T_2$) con las fórmulas $T_1 = T \ltimes E_1$ y $T_2 = T \ltimes E_2$. Definición formal del semijoin: $R \ltimes S = \{ t : t \in R \wedge \exists s \in S(Fun (t \cup s)) \}$, con nota «where $Fun(r)$ is as in the definition of natural join.» Pregunta en rojo al pie: «¿Cómo es el semijoin $\ltimes$ en SQL?»

(slides 69–71)

### Convención: relación dueña y miembro

$$R, \mathbf{F} = \{ F_1, F_2, \dots \}$$

F podría ser primaria o derivada

$$\Downarrow$$

$$S, \mathbf{G} = \{ G_1, G_2, \dots \}, \quad G_i = S \ltimes F_i$$

**Convención:**

- R es dueño
- S es miembro

Título «Fragmentación Horizontal Derivada» en la parte superior. Notación de relación dueña: $R, \mathbf{F} = \{ F_1, F_2, \dots \}$, con anotación lateral «F podría ser primaria o derivada». Flecha doble hacia abajo ($\Downarrow$) indicando derivación. Notación de relación miembro: $S, \mathbf{G} = \{ G_1, G_2, \dots \}, G_i = S \ltimes F_i$. Sección «Convención:» con dos viñetas: «R es dueño» y «S es miembro».

(slide 72)

### Comprobación de completitud, desarticulación y reconstrucción

- Comprobación de completitud, desarticulación y reconstrucción.

**Tabla $T$:**

| id | task |
|----|------|
| …  | …    |
| 6  | test |
| …  | …    |

Si esta tupla no esta presente ni en $T_1$ ni en $T_2$ entonces la fragmentación no está completa.

id = 6 debe estar presente en $E_1$ o $E_2$.

Título «Fragmentación Horizontal Derivada» en la parte superior. Viñeta «Comprobación de completitud, desarticulación y reconstrucción.» Tabla $T$ con columnas `id` y `task`, mostrando filas con puntos suspensivos y una fila destacada con id = 6 y task = test. Flecha desde la fila destacada hacia el texto «Si esta tupla no esta presente ni en $T_1$ ni en $T_2$ entonces la fragmentación no está completa.» Recuadro con borde rojo en la parte inferior derecha con el texto «id = 6 debe estar presente en $E_1$ o $E_2$.»

(slide 73)

### Integridad referencial

- Para garantizar la completitud y reconstrucción necesariamente debemos hacer cumplir la integridad referencial:

El atributo Join de la relación miembro

↓ Cada valor debe estar presente

El atributo Join de la relación dueño

Título «Fragmentación Horizontal Derivada» en la parte superior. Viñeta «Para garantizar la completitud y reconstrucción necesariamente debemos hacer cumplir la integridad referencial:» Diagrama vertical con etiqueta superior «El atributo Join de la relación miembro», flecha hacia abajo con anotación «Cada valor debe estar presente», y etiqueta inferior «El atributo Join de la relación dueño».

(slide 74)

### Violación de desarticulación

- Sea el siguiente ejemplo de fragmentación:

**Tabla $E_1$:**

| id | name | location | salary |
|----|------|----------|--------|
| 1  | Tom  | A        | 15     |

**Tabla $E_2$:**

| id | name | location | salary |
|----|------|----------|--------|
| 1  | Ann  | B        | 23     |

**Tabla $T$:**

| id | task |
|----|------|
| 1  | test |

→ Fragmentación viola la desarticulación

**Tabla $T_1$:**

| id | task |
|----|------|
| 1  | test |

**Tabla $T_2$:**

| id | task |
|----|------|
| 1  | test |

Título «Fragmentación Horizontal Derivada» en la parte superior. Viñeta «Sea el siguiente ejemplo de fragmentación:» Tablas $E_1$ (id=1, Tom, A, 15) y $E_2$ (id=1, Ann, B, 23) en la parte superior — ambas contienen id=1. Tabla $T$ (id=1, test) en el centro. Flecha bifurcada desde $T$ hacia $T_1$ y $T_2$, con anotación «Fragmentación viola la desarticulación». Ambos fragmentos $T_1$ y $T_2$ contienen la misma tupla (1, test), violando la desarticulación.

(slide 75)

### Garantizar desarticulación

- Para garantizar la desarticulación :

  - El atributo join debe ser la **llave** de la relación dueño.

¿Qué hay con las tuplas falsas y tuplas perdidas en la fragmentación?

Título «Fragmentación Horizontal Derivada» en la parte superior. Viñeta «Para garantizar la desarticulación :» con sub-viñeta «El atributo join debe ser la **llave** de la relación dueño.» (la palabra «llave» en negrita). Pregunta en rojo e itálica al pie: «¿Qué hay con las tuplas falsas y tuplas perdidas en la fragmentación?»

(slide 76)

## Base de Datos Distribuida en PostgreSQL

- **Extensiones para PostgreSQL**

  - Distributed Computing on PostgreSQL.pdf

- **CITUS**

  - Why the RDBMS is the future of distributed databases, ft. Postgres and Citus (citusdata.com)

- **YSQL**

  - Distributed PostgreSQL on a Google Spanner Architecture - Query Layer - The Distributed SQL Blog (yugabyte.com)

Título «Base de Datos Distribuida en PostgreSQL» en la parte superior. Tres viñetas principales en negrita: «Extensiones para PostgreSQL», «CITUS» y «YSQL», cada una con una sub-viñeta con referencia a documento o enlace.

(slide 77)

## Ejercicio

Dado el siguiente esquema de BD:

**Libro** (Código, Autor, Tema, TotalExistencias, Precio)

**Almacén** (Código, Ciudad, Provincia, CodPostal, ValorInventario)

**Existencias** (Libro, Almacén, Cantidad)

(Libro y Almacén en Existencias son claves foráneas que referencian a Libro.Código y Almacén.Código respectivamente.)

1. Realizar la fragmentación horizontal de Libro sobre el atributo Precio [20,50,100]
2. Realizar la fragmentación horizontal de Almacén sobre el atributo CodPostal [3500,70000]
3. Realizar la fragmentación horizontal derivada de Existencias respecto a Almacén.
4. Si se tiene tres servidores disponibles, asigne a criterio los fragmentos resultantes en cada servidor.
5. En base a la asignación anterior. Qué subconsultas genera la ejecución de la siguiente consulta en cada servidor:

```sql
select Código, TotalExistencias
from Libro
where Precio>15 and Precio<55
```

Título «Ejercicio» en la parte superior. Texto «Dado el siguiente esquema de BD:» seguido de tres esquemas relacionales: Libro con atributos Código (subrayado como PK), Autor, Tema, TotalExistencias, Precio; Almacén con Código (PK), Ciudad, Provincia, CodPostal, ValorInventario; Existencias con Libro, Almacén, Cantidad, con líneas indicando claves foráneas hacia Libro y Almacén. Cinco tareas numeradas (1–5) sobre fragmentación horizontal, derivada, asignación a servidores y análisis de subconsultas. Recuadro al pie con la consulta SQL indicada.

(slide 78)

## Glosario

- **Sistema distribuido:** «Un sistema distribuido es un sistema que permite que una colección de computadoras independientes se comunique para resolver un objetivo común.»

- **BD distribuida:** Son varias BD interrelacionadas lógicamente y situadas en diferentes nodos de una red de ordenadores.

- **SGBD distribuido:** Es el software que gestiona las BD distribuidas de forma transparente para el usuario. El usuario ve a las BD como si fuera una sola BD centralizada.

- **Transparencia:** … dar la impresión de un solo sistema.

- **Flexibilidad:** …Puede agregar / eliminar máquinas de forma rápida y sencilla.

- **Confiabilidad:** … evita fallos / sigue trabajando en caso de fallo.

- **Desempeño:** … hace las cosas rápidamente.

- **Escalabilidad:** … asegura la escalabilidad de la infraestructura.

- **Fragmentación horizontal primaria:** Fragmentación usando predicados solo en la relación dueña (E).

- **Fragmentación horizontal derivada:** Fragmentación usando predicados de relaciones foráneas; $F_i = E \Join S_i$, $1 \leq i \leq n$.

- **Completitud:** $\forall t \in R, \exists F_i \in \mathbf{F} : t \in F_i$

- **Desarticulación:** $\forall t \in F_i, \neg \exists F_j : t \in F_j, \; i \neq j, \; \{F_i, F_j\} \subset \mathbf{F}$

- **Reconstrucción:** $R = \bigcup_{F_i \in \mathbf{F}} F_i$

- **Predicados Minterm (Términos Mínimos):** Dado un conjunto de predicados simples $P = \{ p_1, p_2, \dots, p_n \}$, los predicados minterms son $M = \{ m \mid m = \bigwedge_{1 \leq k \leq n} p_k^* \}$, en donde $p_k^*$ es o bien $p_k$ o $\neg p_k$.

- **Patrones de Acceso Coincidentes:** Otra propiedad de fragmentación deseada; datos frecuentemente accedidos de manera conjunta deben colocarse en el mismo fragmento.

- **Semijoin ($\ltimes$):** $R \ltimes S = \{ t : t \in R \wedge \exists s \in S(Fun (t \cup s)) \}$, where $Fun(r)$ is as in the definition of natural join.

- **Relación dueño (R):** Relación cuya fragmentación (primaria o derivada) determina la fragmentación de la relación miembro.

- **Relación miembro (S):** Relación cuyos fragmentos se obtienen mediante semijoin con los fragmentos de la relación dueño: $G_i = S \ltimes F_i$.
