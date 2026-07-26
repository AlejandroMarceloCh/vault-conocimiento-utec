---
curso: ACD
titulo: [2025] U5_T1 Data Engineering
slides: 18
fuente: [2025] U5_T1 Data Engineering.pdf
---

## Slide 1

Portada. Título **Data Engineering** — curso **DS3021 Análisis Computacional de Datos**. Docente: Mg. José Espinoza Melgarejo. Imagen de fondo decorativa.

## Slide 2

**Objetivo de sesión**

> Comprender conceptos y fundamentos de Data Warehouse y cómo están relacionados con data engineering

Slide de solo texto (fondo decorativo).

## Slide 3

Separador de sección: **1. Data Engineering — Fundamentos**. Solo texto.

## Slide 4

**Data Engineering**

Data Engineering es el desarrollo, implementación y mantenimiento de sistemas y procesos que toman datos sin procesar (raw data) y producen información consistente y de alta calidad que respalda casos de uso posteriores, como el análisis y el Machine Learning.

Visual: solo texto sobre plantilla; "Data Engineering" resaltado en celeste. Banda superior con foto de oficina y líneas punteadas decorativas.

## Slide 5

**Data Engineering LifeCycle** — "5 Etapas"

Diagrama de bloques del ciclo de vida (izquierda → derecha):

- Caja amarilla **Generation** → flecha negra → contenedor redondeado que agrupa las etapas centrales.
- Dentro del contenedor, fila superior: **Ingestion** (verde) → flecha blanca → **Transformation** (granate) → flecha blanca → **Serving** (azul).
- Debajo, ocupando todo el ancho del contenedor: barra gris **Storage** (soporta a las tres etapas anteriores).
- Del contenedor salen tres flechas a la derecha hacia cajas grises: **Analytics**, **Machine Learning**, **Reverse ETL**.

Debajo, separada por una línea celeste, la franja **Corriente subterráneas** con seis elementos transversales en fila: Security · Data Management · DataOps · Data Architecture · Orchestration · Software Engineering.

## Slide 6

**Corrientes subterráneas** (tabla, parte 1)

| Corriente | Descripción |
|---|---|
| Security (Seguridad) | Asegura la protección de los datos en todas las fases del ciclo (ingesta, almacenamiento, transformación y entrega), incluyendo accesos, cifrado y cumplimiento normativo. |
| Data Management (Gestión de Datos) | Engloba la gobernanza, calidad, catalogación y políticas de retención de datos. Asegura que los datos sean fiables, consistentes y utilizables. |
| DataOps | Metodología ágil aplicada a pipelines de datos, que promueve la automatización, monitoreo continuo, pruebas y colaboración entre equipos de datos. |

## Slide 7

**Corrientes subterráneas** (tabla, parte 2)

| Corriente | Descripción |
|---|---|
| Data Architecture (Arquitectura de Datos) | Define el diseño estructural de los sistemas de datos (bases, lagos, warehouses) y cómo se conectan entre sí para soportar el flujo de datos. |
| Orchestration (Orquestación) | Coordinación automatizada de tareas y procesos dentro del pipeline de datos (por ejemplo, uso de Apache Airflow o Prefect para agendar jobs de transformación). |
| Software Engineering (Ingeniería de Software) | Aplica buenas prácticas de desarrollo de software (versionado, pruebas, CI/CD, modularidad) al desarrollo de pipelines, scripts y soluciones de datos. |

## Slide 8

**Data Engineering LifeCycle** — build-up del diagrama, paso 1.

Visual: el mismo diagrama del slide 5 pero con **solo la caja amarilla `Generation`** visible; el resto del pipeline (Ingestion/Transformation/Serving/Storage y las salidas Analytics/ML/Reverse ETL) aún no aparece. Abajo, intacta, la franja **Corriente subterráneas** con Security · Data Management · DataOps · Data Architecture · Orchestration · Software Engineering.

## Slide 9

**Generation: Source Systems — Etapa 1**

Source system es el origen de los datos utilizados en el ciclo de vida de Data Engineering. Por ejemplo, podría ser un dispositivo IoT, una base de datos transaccional.

Un ingeniero de datos consume datos de un sistema fuente, pero normalmente no posee ni controla el sistema fuente en sí.

Slide de solo texto.

## Slide 10

**Data Engineering LifeCycle** — build-up, paso 2.

Visual: aparece **Generation** (amarillo) y, a su derecha, la barra gris **Storage** dentro del contenedor redondeado. Aún sin Ingestion, Transformation, Serving ni las salidas. Franja de corrientes subterráneas igual que antes.

## Slide 11

**Storage — Etapa 2**

Se necesita un lugar para almacenar los datos. Elegir una solución de almacenamiento es clave para el éxito en el resto del ciclo de vida y también es una de las etapas más complicadas del ciclo de vida por diversas razones.

1. Las arquitecturas de datos en la nube suelen aprovechar varias soluciones de almacenamiento.
2. Pocas soluciones de almacenamiento de datos funcionan exclusivamente como almacenamiento, y muchas admiten consultas de transformación complejas; incluso las soluciones de almacenamiento de objetos pueden admitir potentes capacidades de consulta, por ejemplo, Amazon S3 Select.
3. Si bien el almacenamiento es una etapa del ciclo de vida de la ingeniería de datos, con frecuencia afecta a otras etapas, como la ingesta, la transformación y el servicio.

Slide de solo texto (lista numerada).

## Slide 12

**Data Engineering LifeCycle** — build-up, paso 3.

Visual: ahora se suma la caja verde **Ingestion** sobre la barra **Storage**, además de **Generation**. También aparecen ya las tres salidas a la derecha: **Analytics**, **Machine Learning**, **Reverse ETL**, conectadas con flechas desde el contenedor. Faltan Transformation y Serving. Franja de corrientes subterráneas abajo.

## Slide 13

**Ingestion — Etapa 3**

Los sistemas de origen normalmente están fuera del control directo y pueden dejar de responder aleatoriamente o proporcionar datos de mala calidad. O bien, su servicio de ingesta de datos podría dejar de funcionar misteriosamente por muchas razones. Como resultado, el flujo de datos se detiene o no entrega datos suficientes para su almacenamiento, procesamiento y servicio.

Slide de solo texto.

## Slide 14

**Data Engineering LifeCycle** — build-up, paso 4.

Visual: se añade la caja granate **Transformation** a la derecha de **Ingestion** (con flecha blanca entre ambas), sobre la barra **Storage**; **Generation** a la izquierda y las salidas Analytics / Machine Learning / Reverse ETL a la derecha. Falta solo **Serving**. Franja de corrientes subterráneas abajo.

## Slide 15

**Transformation — Etapa 4**

Una vez que haya ingerido y almacenado datos, debe hacer algo con ellos. La siguiente etapa del ciclo de vida de Data Engineering es la transformación, lo que significa que los datos deben cambiarse de su forma original a algo útil para casos de uso posteriores.

Sin las transformaciones adecuadas, los datos permanecerán inertes y no tendrán un formato útil para informes, análisis o Machine Learning. Normalmente, la etapa de transformación es donde los datos comienzan a crear valor para el consumo de los usuarios posteriores.

Slide de solo texto.

## Slide 16

**Data Engineering LifeCycle** — diagrama completo (paso 5).

Visual: idéntico al slide 5 — Generation → [Ingestion → Transformation → Serving, sobre Storage] → Analytics / Machine Learning / Reverse ETL, con la franja de corrientes subterráneas (Security, Data Management, DataOps, Data Architecture, Orchestration, Software Engineering).

## Slide 17

**Serving — Etapa 5**

La última etapa. Ahora que los datos han sido ingeridos, almacenados y transformados en estructuras coherentes y útiles, es hora de sacarles valor. "Obtener valor" de los datos significa cosas diferentes para diferentes usuarios.

Los datos tienen valor cuando se utilizan con fines prácticos. Los datos que no se consumen ni se consultan son simplemente inertes.

Aquí es donde ocurre la magia.

Slide de solo texto.

## Slide 18

**Aprendizaje Colaborativo**

- Cada grupo realizará una presentación
- Al finalizar habrá un test sobre lo aprendido.

Fuente: *Fundamentals of Data Engineering* — Joe Reis and Matt Housley

Visual: icono de tres personas (grupo) sobre el texto; a la izquierda, foto decorativa de laboratorio con filtro azul.
