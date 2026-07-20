---
curso: BIGDATA
titulo: 14 - Semana 12/Actividad_12_Laborat_BQ__model_KMeans
slides: 0
fuente: 14 - Semana 12/Actividad_12_Laborat_BQ__model_KMeans.sql
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 14 - Semana 12/Actividad_12_Laborat_BQ__model_KMeans.sql. -->

<!-- INTERPRETAR: código fuente (14 - Semana 12/Actividad_12_Laborat_BQ__model_KMeans.sql). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```sql
CREATE OR REPLACE MODEL
demo_utec.segmentacion

OPTIONS(
  MODEL_TYPE='KMEANS',
  NUM_CLUSTERS=4
) AS

SELECT
  age,
  education_num,
  hours_per_week
FROM demo_utec.adult_train;


SELECT *
FROM ML.CENTROIDS(
MODEL demo_utec.segmentacion
);

SELECT *
FROM ML.PREDICT(
MODEL demo_utec.segmentacion,
(
SELECT
  age,
  education_num,
  hours_per_week
FROM demo_utec.adult_test
)
);
```
