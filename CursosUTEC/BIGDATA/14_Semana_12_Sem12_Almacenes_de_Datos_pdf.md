---
curso: BIGDATA
titulo: 14 - Semana 12/Sem12_Almacenes de Datos
slides: 34
fuente: 14 - Semana 12/Sem12_Almacenes de Datos.pdf
---

Almacenes de Datos
Mg. Aldo Lezama Benavides


Semana 12
       Objetivo de la sesión

1. Comprender las diferencias conceptuales y funcionales entre Data
   Warehouse,       Data   Lake   y   Data   Lakehouse,    identificando   sus
   arquitecturas y casos de uso en entornos empresariales modernos.
2. Analizar   las    ventajas     y   desventajas   de    cada   enfoque   de
   almacenamiento de datos, considerando aspectos como estructura,
   gobernanza, rendimiento y costos.
3. Evaluar cómo las nuevas arquitecturas híbridas (Data Lakehouse)
   integran los beneficios del Data Warehouse y del Data Lake para
   optimizar el análisis avanzado y la inteligencia de negocios.
                     Contenido de la sesión

  01.           02.           03.          04.              05.

                                                         Principales
 ¿Por qué
             Datawarehouse   DataLake   DataLakeHouse   servicios en la
surgieron?
                                                             nube
01.   ¿Por qué surgieron?
¿Por qué surgieron estas arquitecturas?
               ¿Por qué surgieron estas arquitecturas?
A medida que las organizaciones crecieron y se digitalizaron, comenzaron a generar enormes cantidades de
información proveniente de múltiples fuentes: sistemas transaccionales, aplicaciones móviles, páginas web,
sensores IoT, redes sociales y APIs externas.
En un inicio, cada área almacenaba sus propios datos de forma independiente, lo que provocaba problemas
de inconsistencia, duplicidad y dificultad para obtener una visión integral del negocio.


Además, aparecieron los llamados “5Vs del Big Data“


Frente a estos desafíos, las empresas necesitaban una forma de centralizar, almacenar, organizar y analizar
toda esa información para apoyar la toma de decisiones.De esta necesidad surgieron distintas arquitecturas,
cada una respondiendo a un problema específico: DW → LAKE → DATA LAKEHOUSE


Finalmente, el crecimiento exponencial de los datos hizo que estas soluciones migraran hacia la computación
en la nube, aprovechando infraestructura prácticamente ilimitada, costos más bajos y alta escalabilidad.
02.   Datawarehouse
                                       Datawarehouse


• Un datawarehouse guarda información estructurada y
  procesada para facilitar consultas y análisis rápidos.
  Siguiendo con el ejemplo de la empresa minorista, un
  almacén de datos guardaría información procesada
  sobre ventas, registros de clientes y niveles de
  inventario. Posteriormente, el almacén de datos limpia,
  transforma y organiza la información en esquemas, lo
  que facilita la generación de informes y la realización de
  tareas de inteligencia empresarial (BI).
                           Ventajas del Datawarehouse

1. Optimizado para el rendimiento de las consultas
• Los datawarehouses ofrecen un alto rendimiento en
  consultas   y   recuperación    de   datos.    Los   datos
  almacenados se preprocesan y organizan en esquemas
  bien definidos, lo que reduce significativamente el tiempo
  necesario para realizar consultas complejas.
• Esto hace que los datawarehouses sean ideales para
  tareas de inteligencia empresarial (BI), como la generación
  de informes, paneles de control y visualizaciones. Las
  empresas confían en ellos para la toma de decisiones en
  tiempo real, lo que les permite responder con rapidez a los
  cambios del mercado.
                            Ventajas del Datawarehouse

2. Consistencia de los datos
• Uno de los pilares de un almacén de datos es la
  coherencia de los datos en toda la organización. Antes de
  ingresar al almacén, los datos se someten a rigurosos
  procesos de limpieza, transformación y validación.
• Como resultado, los distintos departamentos de la
  organización pueden confiar en la precisión y coherencia
  de   los   datos,   lo   que   permite   tomar   decisiones
  empresariales más fiables. Esto también reduce los
  errores que se producen cuando diferentes equipos
  utilizan fuentes de datos dispares.
                           Ventajas del Datawarehouse

3. Gobernanza sólida
• La gobernanza de datos es fundamental para cualquier estrategia
  de datos; los almacenes de datos destacan en este ámbito.
  Utilizan marcos integrales de gobernanza de datos, que incluyen
  estrictos controles de acceso, mecanismos de auditoría y
  seguimiento del linaje de datos. Estas características garantizan la
  seguridad de los datos y su cumplimiento normativo.
• Además, una gobernanza sólida permite que los almacenes de
  datos apliquen políticas sobre la calidad y el uso de los datos, lo
  que garantiza su integridad. Esto es especialmente importante en
  sectores de servicios como las finanzas y la sanidad, donde la
  seguridad y el cumplimiento normativo de los datos son
  fundamentales.
                        Desventajas del Datawarehouse

1. Costos más elevados
• Si   bien   los   almacenes     de    datos     ofrecen   potentes
  funcionalidades, pueden resultar costosos, sobre todo a
  medida que aumenta el volumen de datos. Los costes incluyen
  el hardware y el software necesarios para su funcionamiento.
  Además, se incurrirá en gastos recurrentes relacionados con
  el almacenamiento, el procesamiento y la gestión de datos.
• Además, ampliar un almacén de datos para dar cabida a
  conjuntos de datos más grandes o a más usuarios a menudo
  requiere    inversiones   significativas   en   infraestructura   y
  recursos, lo que puede suponer una gran carga para el
  presupuesto de una organización, especialmente para las
  empresas más pequeñas.
                        Desventajas del Datawarehouse

2. Limitado a datos estructurados
• Los almacenes de datos están diseñados para gestionar datos
  estructurados (datos que se ajustan perfectamente a tablas, filas y
  columnas). Esto resulta excelente para datos transaccionales,
  registros financieros y otros tipos de datos con un patrón predecible.
• Sin embargo, el enfoque en los datos estructurados implica que los
  almacenes de datos tienen dificultades para almacenar y procesar
  datos no estructurados, incluidos correos electrónicos, vídeos,
  publicaciones en redes sociales o datos de sensores.
• Aunque algunos almacenes de datos modernos han comenzado a
  incorporar soporte para formatos de datos semiestructurados —
  como JSON o XML—, no son tan versátiles como los lagos de datos
  para manejar diversos tipos de datos.
                       Desventajas del Datawarehouse

3. Preparación de datos complejos
• Introducir datos en un almacén de datos es complejo y requiere
  mucho tiempo. Los datos deben pasar por el proceso ETL
  (Extracción, Transformación y Carga), donde se extraen de diversas
  fuentes, se transforman a un formato consistente y se cargan en el
  almacén. Esto exige intervención manual y puede ser propenso a
  errores.
• Además, dado que es necesario limpiar y organizar los datos antes
  de almacenarlos, suele haber un retraso entre la generación de los
  datos y su análisis. Esta latencia puede resultar una desventaja
  cuando se requiere un análisis de datos en tiempo real.
03.   Data Lake
                                          Data Lake


• Un data lake almacena grandes cantidades de datos sin
  procesar, no estructurados y semiestructurados. Por
  ejemplo, una empresa minorista almacena registros de
  transacciones, comentarios de clientes y grabaciones de
  vídeo de las cámaras de seguridad de sus tiendas en un
  lago de datos. Posteriormente, se pueden contratar
  científicos y analistas de datos para procesar esta
  información y obtener datos valiosos.
                            Ventajas de los Data Lakes

1. Escalabilidad y asequibilidad
• Los lagos de datos ofrecen un almacenamiento escalable
  y rentable para grandes volúmenes de datos estructurados
  y   no   estructurados   sin   necesidad   de   esquemas
  predefinidos, lo que los hace ideales para la gestión de
  datos a gran escala.
                            Ventajas de los Data Lakes

2. Flexibilidad
• Almacenan los datos sin procesar en su formato nativo, lo
  que permite múltiples casos de uso y un análisis flexible,
  garantizando la versatilidad en el procesamiento de datos.
                                                   3. Prepararse para el futuro
                                                   • Conservar     los   datos   sin   procesar   permite   a   las
                                                      organizaciones analizar datos históricos a medida que
                                                      surgen nuevas tecnologías y casos de uso, manteniendo
                                                      la relevancia de los datos a lo largo del tiempo. Los lagos
                                                      de datos almacenan la información completa, sin extraer
                                                      ningún dato. Esto permite consultar y utilizar la información
                                                      para cualquier necesidad
                         Desventajas de los Data Lakes

1. Falta de organización
• Una de las principales desventajas de los lagos de datos es la
  falta de organización. Si bien algunos lagos de datos han
  evolucionado y están mejor organizados, el modelo aún dista
  mucho de alcanzar el nivel de organización de los almacenes
  de datos.

                                           2. Redundancia de datos
                                           • Los lagos de datos almacenan mucha información redundante. Los
                                             datos redundantes pueden aumentar los costos de almacenamiento
                                             y complicar la administración.
                         Desventajas de los Data Lakes

3. Rendimiento de consultas más lento
• La consulta de datos no procesados ​puede ser más lenta en
  comparación con los sistemas estructurados, lo que dificulta la toma
  de decisiones en tiempo real.

04.   Data LakeHouse
                                    Data LakeHouse

• Las organizaciones de todo el mundo buscan soluciones de
  almacenamiento para administrar los requisitos de volumen,
  latencia, resiliencia y acceso a los macrodatos. Inicialmente, las
  empresas usaron sus pilas tecnológicas existentes e intentaron que
  sus data lakes entregaran las mismas capacidades que un almacén,
  ajustando sus almacenes de datos para manejar grandes cantidades
  de estructuras semiestructuradas o mantuvieron los datos en ambos.
• En última instancia, estos enfoques dieron como resultado costos
  elevados, usuarios insatisfechos y datos duplicados en toda la
  empresa. El data lakehouse surgió como una nueva arquitectura de
  datos híbrida que busca ofrecer los mejores beneficios de los
  almacenes de datos y los data lakes, a la vez que elimina las
  debilidades de ambos sistemas.
                                      Data LakeHouse

• Un data lakehouse combina tecnología y herramientas previamente dispares en una solución holística. Una
  arquitectura típica de lakehouse incluye estas capas:


  Capa de ingesta
• La capa de ingesta recopila datos de transmisión por lotes y en tiempo real de una variedad de fuentes. Si
  bien los lakehouses pueden usar procesos ETL para capturar datos, muchos usan extracción, carga y
  transformación (ELT). El lakehouse puede cargar datos sin procesar en el almacenamiento y transformarlos
  más tarde cuando sean necesarios para el análisis.
                                    Data LakeHouse


Capa de almacenamiento
La capa de almacenamiento suele ser el almacenamiento de objetos en la nube, como en un data lake.




Capa de metadatos
La capa de metadatos proporciona un catálogo unificado de metadatos para cada objeto de la capa de
almacenamiento. Esta capa de metadatos ayuda a los lakehouses a hacer muchas cosas que los lakes no pueden
hacer: indexar datos para consultas más rápidas, hacer cumplir esquemas y aplicar controles de gobernanza y
calidad.
                                  Data LakeHouse


Capa de interfaz de programación de aplicaciones (API)
La capa de API permite a los usuarios conectar herramientas para analytics avanzados.




Capa de consumo
La capa de consumo aloja aplicaciones y herramientas de cliente para BI, ML y otros proyectos de analytics y
ciencia de datos.
                          Diferencias entre DWH, DL y DLH
            Criterio                       Data Warehouse                           Data Lake                            Data Lakehouse

                                                                      Estructurados, semiestructurados y
Tipo de datos                   Estructurados (tablas relacionales)                                         Todos los tipos de datos
                                                                      no estructurados

                                Schema-on-write (definido al cargar   Schema-on-read (definido al
Estructura del esquema                                                                                      Combina ambos enfoques
                                los datos)                            consultar)
Procesamiento                   ETL (Extract – Transform – Load)      ELT (Extract – Load – Transform)      Híbrido ETL/ELT
                                Alto (infraestructura optimizada pero Bajo (usa almacenamiento masivo en
Costo de almacenamiento                                                                                  Moderado
                                costosa)                              la nube)
                                                                      Científicos de datos, ingenieros de
Usuarios típicos                Analistas, BI, ejecutivos                                                   Ambos perfiles
                                                                      datos
                                Alto para consultas analíticas                                              Alto (usa formatos como Delta Lake,
Rendimiento                                                           Variable (no optimizado para SQL)
                                estructuradas                                                               Iceberg o Hudi)
                                Alta (reglas, seguridad, control de                                         Alta (incorpora metadata, control de
Governanza y calidad de datos                                         Baja o inexistente
                                versiones)                                                                  versiones, ACID)

                                Google BigQuery, Snowflake, Amazon Amazon S3, Azure Data Lake Storage, Databricks Lakehouse, Snowflake
Ejemplos de tecnología
                                Redshift, Teradata                 Google Cloud Storage                Unistore, Delta Lake, Apache Iceberg

                                Vertical (añadir más poder a un
Escalabilidad                                                         Horizontal (añadir más nodos)         Horizontal
                                servidor)

Uso principal                   Reportería y BI tradicional           Exploración, ciencia de datos, ML     BI + ML + streaming + exploración
Analogía
Caso aplicado: Plataforma de Datos de un Banco
05.   Principales Servicios de la
      nube
                                   Principales servicios en la nube
                                     para arquitecturas de datos

 Arquitectura: Data Warehouse


                                                             Servicio




Servicio de almacenamiento analítico de      Plataforma analítica de Microsoft que       Data Warehouse serverless de Google. No
AWS diseñado para consultas SQL de           integra Data Warehouse, procesamiento       requiere administrar servidores y permite
gran volumen. Permite crear dashboards y     Big Data y herramientas de integración de   consultar grandes volúmenes de datos
reportes empresariales con alta velocidad.   datos en un solo servicio.                  usando SQL estándar.
                                            Principales servicios en la nube
                                              para arquitecturas de datos

 Arquitectura: Data Lake


                                                                       Servicio




Servicio de almacenamiento de objetos                 Solución    de   almacenamiento    masivo     Servicio de almacenamiento de objetos de
altamente     escalable.   Se     utiliza   como      optimizada para análisis de Big Data.         Google Cloud, utilizado frecuentemente
repositorio    central     para      almacenar        Integra    capacidades   de   seguridad   y   como Data        Lake para proyectos de
cualquier tipo de archivo: CSV, JSON,                 gobierno de datos de Azure.                   analítica e inteligencia artificial.
imágenes, videos, logs, etc.
                                  Principales servicios en la nube
                                    para arquitecturas de datos

 Arquitectura: Data LakeHouse


                                                            Servicio




Plataforma que combina las ventajas de      Plataforma   unificada   de   analítica   de   Solución de Google para administrar datos
un Data Lake y un Data Warehouse.           Microsoft que integra ingeniería de datos,     almacenados    en    Data   Lakes    con
Facilita el procesamiento distribuido con   Data Science, Data Warehouse, BI y             capacidades de gobierno, seguridad y
Apache   Spark,   Machine    Learning   y   Lakehouse bajo una arquitectura SaaS.          consultas analíticas similares a un Data
analítica SQL sobre los mismos datos.                                                      Warehouse.
                      Conclusiones

01.   El Data Warehouse se caracteriza por su alta estructuración, gobernanza sólida y
      velocidad en consultas, siendo ideal para análisis empresariales tradicionales.




02.   El Data Lake ofrece flexibilidad y escalabilidad para almacenar datos sin procesar,
      pero enfrenta retos de organización y rendimiento en consultas.


      El Data Lakehouse surge como una evolución natural que combina lo mejor de

03.   ambos mundos: la estructura y gobernanza del Data Warehouse con la flexibilidad
      y escalabilidad del Data Lake, impulsando la analítica moderna y el machine
      learning.


      Cada una responde a una necesidad distinta. El Data Warehouse prioriza el análisis
04.   estructurado, el Data Lake la flexibilidad y el Data Lakehouse busca integrar ambos
      enfoques.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
