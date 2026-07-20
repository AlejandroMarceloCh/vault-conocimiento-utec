---
curso: BIGDATA
titulo: 14 - Semana 12/Actividad_12_Laborat_BQ__p01_Data_Modelo
slides: 0
fuente: 14 - Semana 12/Actividad_12_Laborat_BQ__p01_Data_Modelo.sql
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 14 - Semana 12/Actividad_12_Laborat_BQ__p01_Data_Modelo.sql. -->

<!-- INTERPRETAR: código fuente (14 - Semana 12/Actividad_12_Laborat_BQ__p01_Data_Modelo.sql). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```sql
-- SELECT * FROM `bigquery-public-data.ml_datasets.census_adult_income` LIMIT 10;

-- SELECT income_bracket,COUNT(*) cantidad FROM `bigquery-public-data.ml_datasets.census_adult_income` GROUP BY income_bracket;

-- SELECT AVG(age) edad_promedio, MIN(age) edad_min, MAX(age) edad_max FROM `bigquery-public-data.ml_datasets.census_adult_income`;

-- CREATE OR REPLACE TABLE demo_utec.adult_train AS SELECT * FROM `bigquery-public-data.ml_datasets.census_adult_income` WHERE RAND() < 0.8;

-- CREATE OR REPLACE TABLE demo_utec.adult_test AS SELECT * FROM `bigquery-public-data.ml_datasets.census_adult_income` WHERE RAND() >= 0.8;












```
