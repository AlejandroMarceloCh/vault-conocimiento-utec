---
curso: BIGDATA
titulo: 14 - Semana 12/Actividad_12_Laborat_BQ__p02_CrearModelo
slides: 0
fuente: 14 - Semana 12/Actividad_12_Laborat_BQ__p02_CrearModelo.sql
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 14 - Semana 12/Actividad_12_Laborat_BQ__p02_CrearModelo.sql. -->

<!-- INTERPRETAR: código fuente (14 - Semana 12/Actividad_12_Laborat_BQ__p02_CrearModelo.sql). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```sql
/* 
CREATE OR REPLACE MODEL demo_utec.modelo_logistico

OPTIONS(
  MODEL_TYPE='LOGISTIC_REG',
  INPUT_LABEL_COLS=['income_bracket']
) AS

SELECT age, education_num, hours_per_week, capital_gain, capital_loss, income_bracket FROM demo_utec.adult_train;
*/


-- SELECT * FROM ML.TRAINING_INFO(MODEL demo_utec.modelo_logistico);
```
