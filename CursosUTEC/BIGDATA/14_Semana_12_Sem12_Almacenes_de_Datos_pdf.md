---
curso: BIGDATA
titulo: 14 - Semana 12/Sem12_Almacenes de Datos
slides: 34
fuente: 14 - Semana 12/Sem12_Almacenes de Datos.pdf
---

## Slide 1

Portada (decorativa: fondo celeste con edificio UTEC, logo UTEC, "Reinventa el mundo").

Título: **Almacenes de Datos**
Mg. Aldo Lezama Benavides
Semana 12

## Slide 2

**Objetivo de la sesión**

1. **Comprender** las diferencias conceptuales y funcionales entre Data Warehouse, Data Lake y Data Lakehouse, identificando sus arquitecturas y casos de uso en entornos empresariales modernos.
2. **Analizar** las ventajas y desventajas de cada enfoque de almacenamiento de datos, considerando aspectos como estructura, gobernanza, rendimiento y costos.
3. **Evaluar** cómo las nuevas arquitecturas híbridas (Data Lakehouse) integran los beneficios del Data Warehouse y del Data Lake para optimizar el análisis avanzado y la inteligencia de negocios.

## Slide 3

**Contenido de la sesión** — índice visual de 5 bloques numerados entre corchetes:

- **01.** ¿Por qué surgieron?
- **02.** Datawarehouse
- **03.** DataLake
- **04.** DataLakeHouse
- **05.** Principales servicios en la nube

## Slide 4

Divisor de sección. Número grande **01.** con ícono de portapapeles/checklist y título **¿Por qué surgieron?**

## Slide 5

**¿Por qué surgieron estas arquitecturas?**

Diagrama de infografía de 3 columnas conectadas por flechas grises (izquierda → derecha):

**Columna 1 — FUENTES DE DATOS** (encabezado azul). Lista con íconos:
- Sistemas Transaccionales (ERP, Core Bancario)
- CRM
- Aplicaciones Móviles y Web
- Sensores IoT
- Redes Sociales
- APIs Externas
- Archivos, Logs, Correos, Audios, Videos

**Columna 2 — EL PROBLEMA** (encabezado rojo). Cuatro ítems con íconos:
- **VOLUMEN**: Cada día se genera una enorme cantidad de datos.
- **VARIEDAD**: Existen datos estructurados, semiestructurados y no estructurados.
- **VELOCIDAD**: Los datos se generan y cambian en tiempo real.
- **CALIDAD Y GOBERNANZA**: Los datos vienen dispersos, duplicados e inconsistentes.

**Columna 3 — NECESIDAD / SOLUCIÓN** (encabezado verde): **CENTRALIZAR, ALMACENAR, ORGANIZAR Y ANALIZAR LOS DATOS**. Checklist verde:
- Tener una única fuente de verdad.
- Facilitar la toma de decisiones.
- Obtener información para el negocio.
- Cumplir con regulaciones y políticas de datos.
- Habilitar analítica avanzada e Inteligencia Artificial.

Recuadro inferior (bombilla): "Surgen así nuevas arquitecturas de datos (Data Warehouse, Data Lake y Data Lakehouse) para afrontar estos desafíos y convertir los datos en valor para el negocio."

Encabezado superior del gráfico: "Las organizaciones generan grandes volúmenes de datos desde múltiples fuentes, con distintos formatos, estructuras y velocidades."

## Slide 6

**¿Por qué surgieron estas arquitecturas?** (slide de texto)

A medida que las organizaciones crecieron y se digitalizaron, comenzaron a generar enormes cantidades de información proveniente de múltiples fuentes: sistemas transaccionales, aplicaciones móviles, páginas web, sensores IoT, redes sociales y APIs externas.

En un inicio, cada área almacenaba sus propios datos de forma independiente, lo que provocaba problemas de inconsistencia, duplicidad y dificultad para obtener una visión integral del negocio.

Además, aparecieron los llamados **"5Vs del Big Data"**.

Frente a estos desafíos, las empresas necesitaban una forma de centralizar, almacenar, organizar y analizar toda esa información para apoyar la toma de decisiones. De esta necesidad surgieron distintas arquitecturas, cada una respondiendo a un problema específico: **DW → LAKE → DATA LAKEHOUSE**.

Finalmente, el crecimiento exponencial de los datos hizo que estas soluciones migraran hacia la computación en la nube, aprovechando infraestructura prácticamente ilimitada, costos más bajos y alta escalabilidad.

## Slide 7

Divisor de sección. **02.** con ícono checklist y título **Datawarehouse**.

## Slide 8

**Datawarehouse**

Texto: Un datawarehouse guarda información estructurada y procesada para facilitar consultas y análisis rápidos. Siguiendo con el ejemplo de la empresa minorista, un almacén de datos guardaría información procesada sobre ventas, registros de clientes y niveles de inventario. Posteriormente, el almacén de datos limpia, transforma y organiza la información en esquemas, lo que facilita la generación de informes y la realización de tareas de inteligencia empresarial (BI).

Diagrama de flujo (izquierda → derecha) de una arquitectura Data Warehouse:
- Fuentes agrupadas en tres bloques: **SISTEMAS INTERNOS** (íconos de fábrica/robot, carrito, usuarios, dinero), **APLICACIONES** (Facebook, Google, Salesforce, SAP) y **OTROS ORÍGENES** (Microsoft, nube/BD, mapa/ubicación, caja).
- Todas las fuentes convergen mediante flechas en un bloque de engranajes etiquetado **ETL**.
- ETL alimenta un cilindro de base de datos naranja etiquetado **DATA WAREHOUSE**.
- Del Data Warehouse salen dos ramas: hacia **BUSINESS INTELLIGENCE** (ícono de gráfico de barras) y hacia **DATA SCIENCE** (ícono de nodos conectados).
- Ambas ramas convergen en una bombilla amarilla etiquetada **TOMA DE DECISIONES**.

## Slide 9

**Ventajas del Datawarehouse**

**1. Optimizado para el rendimiento de las consultas**
- Los datawarehouses ofrecen un alto rendimiento en consultas y recuperación de datos. Los datos almacenados se preprocesan y organizan en esquemas bien definidos, lo que reduce significativamente el tiempo necesario para realizar consultas complejas.
- Esto hace que los datawarehouses sean ideales para tareas de inteligencia empresarial (BI), como la generación de informes, paneles de control y visualizaciones. Las empresas confían en ellos para la toma de decisiones en tiempo real, lo que les permite responder con rapidez a los cambios del mercado.

Imagen decorativa a la derecha: la palabra "OPTIMIZACIÓN" sobre una composición de engranajes, íconos de negocio y una flecha verde ascendente.

## Slide 10

**Ventajas del Datawarehouse**

**2. Consistencia de los datos**
- Uno de los pilares de un almacén de datos es la coherencia de los datos en toda la organización. Antes de ingresar al almacén, los datos se someten a rigurosos procesos de limpieza, transformación y validación.
- Como resultado, los distintos departamentos de la organización pueden confiar en la precisión y coherencia de los datos, lo que permite tomar decisiones empresariales más fiables. Esto también reduce los errores que se producen cuando diferentes equipos utilizan fuentes de datos dispares.

Imagen decorativa a la derecha: la palabra "CONSISTENCY" escrita a mano con un marcador azul.

## Slide 11

**Ventajas del Datawarehouse**

**3. Gobernanza sólida**
- La gobernanza de datos es fundamental para cualquier estrategia de datos; los almacenes de datos destacan en este ámbito. Utilizan marcos integrales de gobernanza de datos, que incluyen estrictos controles de acceso, mecanismos de auditoría y seguimiento del linaje de datos. Estas características garantizan la seguridad de los datos y su cumplimiento normativo.
- Además, una gobernanza sólida permite que los almacenes de datos apliquen políticas sobre la calidad y el uso de los datos, lo que garantiza su integridad. Esto es especialmente importante en sectores de servicios como las finanzas y la sanidad, donde la seguridad y el cumplimiento normativo de los datos son fundamentales.

Imagen decorativa a la derecha: manos entrelazadas en círculo (foto B/N) con la palabra "GOBERNANZA".

## Slide 12

**Desventajas del Datawarehouse**

**1. Costos más elevados**
- Si bien los almacenes de datos ofrecen potentes funcionalidades, pueden resultar costosos, sobre todo a medida que aumenta el volumen de datos. Los costes incluyen el hardware y el software necesarios para su funcionamiento. Además, se incurrirá en gastos recurrentes relacionados con el almacenamiento, el procesamiento y la gestión de datos.
- Además, ampliar un almacén de datos para dar cabida a conjuntos de datos más grandes o a más usuarios a menudo requiere inversiones significativas en infraestructura y recursos, lo que puede suponer una gran carga para el presupuesto de una organización, especialmente para las empresas más pequeñas.

Imagen decorativa a la derecha: pasillo de un centro de datos con racks de servidores iluminados en azul.

## Slide 13

**Desventajas del Datawarehouse**

**2. Limitado a datos estructurados**
- Los almacenes de datos están diseñados para gestionar datos estructurados (datos que se ajustan perfectamente a tablas, filas y columnas). Esto resulta excelente para datos transaccionales, registros financieros y otros tipos de datos con un patrón predecible.
- Sin embargo, el enfoque en los datos estructurados implica que los almacenes de datos tienen dificultades para almacenar y procesar datos no estructurados, incluidos correos electrónicos, vídeos, publicaciones en redes sociales o datos de sensores.
- Aunque algunos almacenes de datos modernos han comenzado a incorporar soporte para formatos de datos semiestructurados —como JSON o XML—, no son tan versátiles como los lagos de datos para manejar diversos tipos de datos.

Diagrama a la derecha ("Types of Data"): un nodo raíz "Types of Data" se ramifica en tres categorías:
- **Structured** (resaltado con recuadro rojo): tablas de dígitos binarios 1001/1010/1110...
- **Unstructured**: íconos dispersos de imágenes, notas musicales, documentos, correos.
- **Semi-Structured**: íconos ordenados en columnas de documentos, imágenes, música, correos.

## Slide 14

**Desventajas del Datawarehouse**

**3. Preparación de datos complejos**
- Introducir datos en un almacén de datos es complejo y requiere mucho tiempo. Los datos deben pasar por el proceso ETL (Extracción, Transformación y Carga), donde se extraen de diversas fuentes, se transforman a un formato consistente y se cargan en el almacén. Esto exige intervención manual y puede ser propenso a errores.
- Además, dado que es necesario limpiar y organizar los datos antes de almacenarlos, suele haber un retraso entre la generación de los datos y su análisis. Esta latencia puede resultar una desventaja cuando se requiere un análisis de datos en tiempo real.

Diagrama a la derecha ("The ETL process"), tres pasos horizontales con flechas:
- **Extract**: cilindros de BD apilados. "Extracts data from multiple data sources simultaneously, pulling it into one place."
- **Transform**: cilindro con flechas circulares (proceso de transformación). "All data is standardized, cleaned and organized ready for analysis."
- **Load**: cilindro con ícono de nube. "Data can then be sent to a storage system, E.G. a data warehouse."

## Slide 15

Divisor de sección. **03.** con ícono checklist y título **Data Lake**.

## Slide 16

**Data Lake**

Texto: Un data lake almacena grandes cantidades de datos sin procesar, no estructurados y semiestructurados. Por ejemplo, una empresa minorista almacena registros de transacciones, comentarios de clientes y grabaciones de vídeo de las cámaras de seguridad de sus tiendas en un lago de datos. Posteriormente, se pueden contratar científicos y analistas de datos para procesar esta información y obtener datos valiosos.

Diagrama a la derecha (flujo de arquitectura Data Lake):
- Entrada a la izquierda: íconos de fuentes de datos (cilindros de BD, imágenes, video/play, audio, documento) etiquetados **Structured, Semi-Structured and Unstructured Data**.
- Flecha hacia un gran círculo con ondas (el "lago de datos").
- Del lago salen dos ramas hacia la derecha:
  - Rama superior: **Data Prep and Validation** (engranajes) → **Data Science** → **Machine Learning**.
  - Rama media: bloque **ETL** → **Real-Time Database** (cilindro) → **Reports** → **BI**.
  - Rama inferior: **Data Marts** (cilindros pequeños).

## Slide 17

**Ventajas de los Data Lakes**

**1. Escalabilidad y asequibilidad**
- Los lagos de datos ofrecen un almacenamiento escalable y rentable para grandes volúmenes de datos estructurados y no estructurados sin necesidad de esquemas predefinidos, lo que los hace ideales para la gestión de datos a gran escala.

Imagen decorativa a la derecha: persona de traje sosteniendo una tablet de la que emerge un gráfico de barras ascendente con flecha (crecimiento).

## Slide 18

**Ventajas de los Data Lakes**

**2. Flexibilidad**
- Almacenan los datos sin procesar en su formato nativo, lo que permite múltiples casos de uso y un análisis flexible, garantizando la versatilidad en el procesamiento de datos.

**3. Prepararse para el futuro**
- Conservar los datos sin procesar permite a las organizaciones analizar datos históricos a medida que surgen nuevas tecnologías y casos de uso, manteniendo la relevancia de los datos a lo largo del tiempo. Los lagos de datos almacenan la información completa, sin extraer ningún dato. Esto permite consultar y utilizar la información para cualquier necesidad.

## Slide 19

**Desventajas de los Data Lakes**

**1. Falta de organización**
- Una de las principales desventajas de los lagos de datos es la falta de organización. Si bien algunos lagos de datos han evolucionado y están mejor organizados, el modelo aún dista mucho de alcanzar el nivel de organización de los almacenes de datos.

**2. Redundancia de datos**
- Los lagos de datos almacenan mucha información redundante. Los datos redundantes pueden aumentar los costos de almacenamiento y complicar la administración.

## Slide 20

**Desventajas de los Data Lakes**

**3. Rendimiento de consultas más lento**
- La consulta de datos no procesados puede ser más lenta en comparación con los sistemas estructurados, lo que dificulta la toma de decisiones en tiempo real.

## Slide 21

Divisor de sección. **04.** con ícono checklist y título **Data LakeHouse**.

## Slide 22

**Data LakeHouse**

Texto:
- Las organizaciones de todo el mundo buscan soluciones de almacenamiento para administrar los requisitos de volumen, latencia, resiliencia y acceso a los macrodatos. Inicialmente, las empresas usaron sus pilas tecnológicas existentes e intentaron que sus data lakes entregaran las mismas capacidades que un almacén, ajustando sus almacenes de datos para manejar grandes cantidades de estructuras semiestructuradas o mantuvieron los datos en ambos.
- En última instancia, estos enfoques dieron como resultado costos elevados, usuarios insatisfechos y datos duplicados en toda la empresa. El data lakehouse surgió como una nueva arquitectura de datos híbrida que busca ofrecer los mejores beneficios de los almacenes de datos y los data lakes, a la vez que elimina las debilidades de ambos sistemas.

Diagrama de ecuación a la derecha (íconos verdes): **Data Warehouse** (cilindro) **+** **Data Lake** (cilindro con ondas) **=** **Data Lakehouse** (casa con ondas de agua). Ilustra la fusión de ambos conceptos.

## Slide 23

**Data LakeHouse**

- Un data lakehouse combina tecnología y herramientas previamente dispares en una solución holística. Una arquitectura típica de lakehouse incluye estas capas:

**Capa de ingesta**
- La capa de ingesta recopila datos de transmisión por lotes y en tiempo real de una variedad de fuentes. Si bien los lakehouses pueden usar procesos ETL para capturar datos, muchos usan extracción, carga y transformación (ELT). El lakehouse puede cargar datos sin procesar en el almacenamiento y transformarlos más tarde cuando sean necesarios para el análisis.

## Slide 24

**Data LakeHouse**

**Capa de almacenamiento**
La capa de almacenamiento suele ser el almacenamiento de objetos en la nube, como en un data lake.

**Capa de metadatos**
La capa de metadatos proporciona un catálogo unificado de metadatos para cada objeto de la capa de almacenamiento. Esta capa de metadatos ayuda a los lakehouses a hacer muchas cosas que los lakes no pueden hacer: indexar datos para consultas más rápidas, hacer cumplir esquemas y aplicar controles de gobernanza y calidad.

## Slide 25

**Data LakeHouse**

**Capa de interfaz de programación de aplicaciones (API)**
La capa de API permite a los usuarios conectar herramientas para analytics avanzados.

**Capa de consumo**
La capa de consumo aloja aplicaciones y herramientas de cliente para BI, ML y otros proyectos de analytics y ciencia de datos.

## Slide 26

**Diferencias entre DWH, DL y DLH** — tabla comparativa de 4 columnas:

| Criterio | Data Warehouse | Data Lake | Data Lakehouse |
|---|---|---|---|
| Tipo de datos | Estructurados (tablas relacionales) | Estructurados, semiestructurados y no estructurados | Todos los tipos de datos |
| Estructura del esquema | Schema-on-write (definido al cargar los datos) | Schema-on-read (definido al consultar) | Combina ambos enfoques |
| Procesamiento | ETL (Extract – Transform – Load) | ELT (Extract – Load – Transform) | Híbrido ETL/ELT |
| Costo de almacenamiento | Alto (infraestructura optimizada pero costosa) | Bajo (usa almacenamiento masivo en la nube) | Moderado |
| Usuarios típicos | Analistas, BI, ejecutivos | Científicos de datos, ingenieros de datos | Ambos perfiles |
| Rendimiento | Alto para consultas analíticas estructuradas | Variable (no optimizado para SQL) | Alto (usa formatos como Delta Lake, Iceberg o Hudi) |
| Governanza y calidad de datos | Alta (reglas, seguridad, control de versiones) | Baja o inexistente | Alta (incorpora metadata, control de versiones, ACID) |
| Ejemplos de tecnología | Google BigQuery, Snowflake, Amazon Redshift, Teradata | Amazon S3, Azure Data Lake Storage, Google Cloud Storage | Databricks Lakehouse, Snowflake Unistore, Delta Lake, Apache Iceberg |
| Escalabilidad | Vertical (añadir más poder a un servidor) | Horizontal (añadir más nodos) | Horizontal |
| Uso principal | Reportería y BI tradicional | Exploración, ciencia de datos, ML | BI + ML + streaming + exploración |

## Slide 27

**Analogía** — infografía ilustrada de 4 columnas: "ALMACÉN, SUPERMERCADO Y ALMACÉN INTELIGENTE EN LA NUBE".

**1. DATA LAKE** (verde) — "Un enorme almacén donde se guardan todas las cajas tal como llegan." Ilustración: almacén/galpón con cajas apiladas (CSV, imágenes, audios, logs) y un montacargas. Puntos:
- Guarda todo en su formato original.
- Datos estructurados y no estructurados.
- Bajo costo.
- Aún no se organiza la información.
- Ideal para Big Data e IA.

**2. DATA WAREHOUSE** (azul) — "Un supermercado donde los productos ya están ordenados por categorías para que sean fáciles de encontrar." Ilustración: supermercado con estanterías rotuladas (Lácteos, Bebidas, Frutas, Carnes) y un carrito. Puntos:
- Datos ya procesados y organizados.
- Estructura definida.
- Altísimo rendimiento en consultas (SQL).
- Ideal para reportes y dashboards (BI).
- Costo medio.

**3. DATA LAKEHOUSE** (morado) — "Un almacén inteligente que guarda las cajas originales, pero además puede organizarlas automáticamente cuando alguien necesita encontrarlas." Ilustración: almacén inteligente con Zona Raw (datos originales), Procesamiento y Gobierno de Datos, Datos Limpios (Curated), Datos Listos (Gold) y dashboards. Puntos:
- Guarda todo y también organiza.
- Soporta SQL, ACID, versiones y gobierno.
- Sirve para BI, Machine Learning e IA.
- Alto rendimiento con gran flexibilidad.
- Costo bajo a medio.

**4. CLOUD (LA NUBE)** (celeste) — "El terreno y el edificio alquilado donde funciona todo el sistema, sin que la empresa tenga que construirlo ni mantenerlo." Ilustración: nube AWS/AZURE/GCP conectada a Data Lake, Data Lakehouse, Data Warehouse y a BI/Reportes y Machine Learning. Puntos:
- Infraestructura elástica y escalable.
- Pagas solo por lo que usas.
- Alta disponibilidad y seguridad.
- Servicios administrados.
- Permite innovar más rápido.

Resumen inferior: "La nube es el lugar donde construyes tu almacén (Data Lake), tu supermercado (Data Warehouse) o tu almacén inteligente (Data Lakehouse) para convertir todos los datos en información valiosa."

## Slide 28

**Caso aplicado: Plataforma de Datos de un Banco** — diagrama de arquitectura end-to-end.

Encabezado: "El banco necesita integrar datos de múltiples fuentes para analizar el negocio, mejorar la experiencia del cliente, gestionar riesgos y cumplir con regulaciones."

Flujo horizontal de bloques (izquierda → derecha, unidos por flechas):

**Fuentes de Datos**: Sistemas Transaccionales (Core Bancario), Aplicación Móvil, Banca en Línea, Cajeros Automáticos, Call Center, Redes Sociales, Buró de Crédito, Entidades Externas.

**1. Data Lake (Datos Crudos)** — Almacenamiento en la Nube (Amazon S3 / Azure Data Lake / GCS). Carpetas: /transacciones (CSV, Parquet), /logs_app (JSON, TXT), /clickstream (JSON), /audios_callcenter (MP3, WAV), /imagenes_dni (JPG, PNG), /documentos (PDF), /datos_buro (CSV, XML), /otros (…). Nota: "Guarda todo tipo de datos sin estructura definida. Bajo costo y alta escalabilidad."

**2. Lakehouse (Procesamiento y Gobierno)** — Plataforma: Databricks / Microsoft Fabric / BigLake. Arquitectura medallion:
- **Bronze (Raw)**: Datos en su formato original; ingesta automática y particionada.
- **Silver (Limpios)**: Limpieza, deduplicación y validación; estandarización de formatos; reglas de calidad de datos.
- **Gold (Curados)**: Datos modelados por dominio; métricas y agregaciones; listos para análisis y reportes.
- Barra inferior de gobierno: Gobernanza y Seguridad, Catálogo de Datos, Trazabilidad (Lineage), Calidad de Datos.

**3. Data Warehouse (Datos Curados para Negocio)** — Modelo Dimensional:
- **Hechos**: Ventas y Transacciones, Pagos, Interacciones, Mora y Riesgo.
- **Dimensiones**: Cliente, Producto, Tiempo, Canal, Sucursal / Agencia, Geografía.
- Nota: "Optimizado para consultas SQL rápidas y reportes de negocio."

**Consumo de Datos**:
- Inteligencia de Negocio: Power BI / Tableau / Looker.
- Analítica Avanzada: Segmentación de clientes, Predicción de Mora, Detección de Fraude, Next Best Offer.
- Operaciones: Reportes regulatorios, Monitoreo en tiempo real, Alertas y tableros.
- Usuarios: Gerencia, Analistas, Científicos de Datos, Regulador.

**Barra transversal — Gobernanza y Seguridad (Transversal)**: Control de Accesos (Roles y Permisos), Encriptación de Datos, Cumplimiento (Normativas), Monitoreo y Auditoría.

**Beneficios para el Negocio**: Decisiones más rápidas y basadas en datos; Mejor experiencia para el cliente; Reducción de riesgos y fraude; Aumento de eficiencia operativa; Optimización de costos y recursos.

## Slide 29

Divisor de sección. **05.** con ícono checklist y título **Principales Servicios de la nube**.

## Slide 30

**Principales servicios en la nube para arquitecturas de datos**
Arquitectura: **Data Warehouse**

Fila de 3 servicios (con logos):
- **Amazon Redshift**: Servicio de almacenamiento analítico de AWS diseñado para consultas SQL de gran volumen. Permite crear dashboards y reportes empresariales con alta velocidad.
- **(Microsoft — logo Azure Synapse/hexágono azul)**: Plataforma analítica de Microsoft que integra Data Warehouse, procesamiento Big Data y herramientas de integración de datos en un solo servicio.
- **BigQuery** (Google): Data Warehouse serverless de Google. No requiere administrar servidores y permite consultar grandes volúmenes de datos usando SQL estándar.

## Slide 31

**Principales servicios en la nube para arquitecturas de datos**
Arquitectura: **Data Lake**

Fila de 3 servicios (con logos):
- **Amazon S3**: Servicio de almacenamiento de objetos altamente escalable. Se utiliza como repositorio central para almacenar cualquier tipo de archivo: CSV, JSON, imágenes, videos, logs, etc.
- **Azure Data Lake**: Solución de almacenamiento masivo optimizada para análisis de Big Data. Integra capacidades de seguridad y gobierno de datos de Azure.
- **Google Cloud Storage**: Servicio de almacenamiento de objetos de Google Cloud, utilizado frecuentemente como Data Lake para proyectos de analítica e inteligencia artificial.

## Slide 32

**Principales servicios en la nube para arquitecturas de datos**
Arquitectura: **Data LakeHouse**

Fila de 3 servicios (con logos):
- **Databricks**: Plataforma que combina las ventajas de un Data Lake y un Data Warehouse. Facilita el procesamiento distribuido con Apache Spark, Machine Learning y analítica SQL sobre los mismos datos.
- **Microsoft Fabric**: Plataforma unificada de analítica de Microsoft que integra ingeniería de datos, Data Science, Data Warehouse, BI y Lakehouse bajo una arquitectura SaaS.
- **(Google BigLake — logo lupa con ondas azules)**: Solución de Google para administrar datos almacenados en Data Lakes con capacidades de gobierno, seguridad y consultas analíticas similares a un Data Warehouse.

## Slide 33

**Conclusiones**

**01.** El Data Warehouse se caracteriza por su alta estructuración, gobernanza sólida y velocidad en consultas, siendo ideal para análisis empresariales tradicionales.

**02.** El Data Lake ofrece flexibilidad y escalabilidad para almacenar datos sin procesar, pero enfrenta retos de organización y rendimiento en consultas.

**03.** El Data Lakehouse surge como una evolución natural que combina lo mejor de ambos mundos: la estructura y gobernanza del Data Warehouse con la flexibilidad y escalabilidad del Data Lake, impulsando la analítica moderna y el machine learning.

**04.** Cada una responde a una necesidad distinta. El Data Warehouse prioriza el análisis estructurado, el Data Lake la flexibilidad y el Data Lakehouse busca integrar ambos enfoques.

## Slide 34

Cierre. Decorativa: logo UTEC — Universidad de Ingeniería y Tecnología, sobre fondo celeste.
