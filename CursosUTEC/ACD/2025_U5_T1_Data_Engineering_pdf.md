---
curso: ACD
titulo: [2025] U5_T1 Data Engineering
slides: 18
fuente: [2025] U5_T1 Data Engineering.pdf
---

Data Engineering

DS3021 Análisis Computacional de Datos




                                  Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Comprender conceptos y fundamentos
                     de Data Warehouse y cómo están
                     relacionados con data engineering
1.
     Data Engineering
     Fundamentos
                         Data Engineering
Data Engineering es el desarrollo, implementación y mantenimiento de sistemas y
procesos que toman datos sin procesar (raw data) y producen información consistente y
de alta calidad que respalda casos de uso posteriores, como el análisis y el Machine
Learning.
                         Data Engineering
                             LifeCycle
 5 Etapas


                                                                                 Analytics
                         Ingestion   Transformation    Serving
                                                                                 Machine
 Generation                                                                      Learning
                                        Storage
                                                                            Reverse ETL




                                Corriente subterráneas

Security       Data           DataOps           Data             Orchestration       Software
            Management                       Architecture                           Engineering
             Corrientes subterráness

    Corriente                           Descripción
                     Asegura la protección de los datos en todas las
     Security        fases    del   ciclo   (ingesta,  almacenamiento,
   (Seguridad)       transformación y entrega), incluyendo accesos,
                     cifrado y cumplimiento normativo.
                     Engloba la gobernanza, calidad, catalogación, y
Data Management
                     políticas de retención de datos. Asegura que los
(Gestión de Datos)
                     datos sean fiables, consistentes y utilizables.
                     Metodología ágil aplicada a pipelines de datos, que
    DataOps          promueve la automatización, monitoreo continuo,
                     pruebas y colaboración entre equipos de datos.
            Corrientes subterráness

   Corriente                           Descripción
Data Architecture   Define el diseño estructural de los sistemas de
(Arquitectura de    datos (bases, lagos, warehouses) y cómo se
     Datos)         conectan entre sí para soportar el flujo de datos.
                    Coordinación automatizada de tareas y procesos
  Orchestration     dentro del pipeline de datos (por ejemplo, uso de
 (Orquestación)     Apache Airflow o Prefect para agendar jobs de
                    transformación).
    Software        Aplica buenas prácticas de desarrollo de software
  Engineering       (versionado, pruebas, CI/CD, modularidad) al
 (Ingeniería de     desarrollo de pipelines, scripts y soluciones de
   Software)        datos.
                        Data Engineering
                            LifeCycle



 Generation




                           Corriente subterráneas

Security      Data        DataOps       Data        Orchestration    Software
           Management                Architecture                   Engineering
Generation: Source Systems
Etapa 1

   Source system es el origen de los datos utilizados en el ciclo de vida
   de Data Engineering. Por ejemplo, podría ser un dispositivo IoT, una
   base de datos transaccional.

   Un ingeniero de datos consume datos de un sistema fuente, pero
   normalmente no posee ni controla el sistema fuente en sí.
                        Data Engineering
                            LifeCycle



 Generation
                                    Storage




                           Corriente subterráneas

Security      Data        DataOps          Data        Orchestration    Software
           Management                   Architecture                   Engineering
Storage
Etapa 2

  Se necesita un lugar para almacenar los datos. Elegir una solución de
  almacenamiento es clave para el éxito en el resto del ciclo de vida y
  también es una de las etapas más complicadas del ciclo de vida por
  diversas razones.
    1. Las arquitecturas de datos en la nube suelen aprovechar varias
        soluciones de almacenamiento.
    2. Pocas soluciones de almacenamiento de datos funcionan
        exclusivamente como almacenamiento, y muchas admiten consultas
        de transformación complejas; incluso las soluciones de
        almacenamiento de objetos pueden admitir potentes capacidades
        de consulta, por ejemplo, Amazon S3 Select.
    3. Si bien el almacenamiento es una etapa del ciclo de vida de la
        ingeniería de datos, con frecuencia afecta a otras etapas, como la
        ingesta, la transformación y el servicio.
  .
                        Data Engineering
                            LifeCycle


                                                                          Analytics
                        Ingestion
                                                                          Machine
 Generation                                                               Learning
                                       Storage
                                                                     Reverse ETL




                               Corriente subterráneas

Security      Data           DataOps          Data        Orchestration       Software
           Management                      Architecture                      Engineering
Ingestion
Etapa 3

   Los sistemas de origen normalmente están fuera del control
   directo y pueden dejar de responder aleatoriamente o
   proporcionar datos de mala calidad. O bien, su servicio de ingesta
   de datos podría dejar de funcionar misteriosamente por muchas
   razones. Como resultado, el flujo de datos se detiene o no entrega
   datos suficientes para su almacenamiento, procesamiento y
   servicio.
                        Data Engineering
                            LifeCycle


                                                                           Analytics
                        Ingestion   Transformation
                                                                           Machine
 Generation                                                                Learning
                                       Storage
                                                                      Reverse ETL




                               Corriente subterráneas

Security      Data           DataOps           Data        Orchestration       Software
           Management                       Architecture                      Engineering
Transformation
Etapa 4

   Una vez que haya ingerido y almacenado datos, debe hacer algo
   con ellos. La siguiente etapa del ciclo de vida de Data Engineering
   es la transformación, lo que significa que los datos deben
   cambiarse de su forma original a algo útil para casos de uso
   posteriores.

   Sin las transformaciones adecuadas, los datos permanecerán
   inertes y no tendrán un formato útil para informes, análisis o
   Machine Learning. Normalmente, la etapa de transformación es
   donde los datos comienzan a crear valor para el consumo de los
   usuarios posteriores.
                        Data Engineering
                            LifeCycle


                                                                                Analytics
                        Ingestion   Transformation    Serving
                                                                                Machine
 Generation                                                                     Learning
                                       Storage
                                                                           Reverse ETL




                               Corriente subterráneas

Security      Data           DataOps           Data             Orchestration       Software
           Management                       Architecture                           Engineering
Serving
Etapa 5
  La última etapa. Ahora que los datos han sido ingeridos, almacenados y
  transformados en estructuras coherentes y útiles, es hora de sacarles
  valor. “Obtener valor” de los datos significa cosas diferentes para
  diferentes usuarios.

  Los datos tienen valor cuando se utilizan con fines prácticos. Los datos
  que no se consumen ni se consultan son simplemente inertes.

  Aquí es donde ocurre la magia.
            Aprendizaje Colaborativo

 ●   Cada grupo realizará una presentación
 ●   Al finalizar habrá un test sobre lo aprendido.

Fuente: Fundamentals of Data Engineering
Joe Reis and Matt Housley

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
