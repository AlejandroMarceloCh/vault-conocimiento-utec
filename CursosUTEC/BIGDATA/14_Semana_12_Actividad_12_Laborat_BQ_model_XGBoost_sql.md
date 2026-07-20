---
curso: BIGDATA
titulo: 14 - Semana 12/Actividad_12_Laborat_BQ__model_XGBoost
slides: 0
fuente: 14 - Semana 12/Actividad_12_Laborat_BQ__model_XGBoost.sql
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 14 - Semana 12/Actividad_12_Laborat_BQ__model_XGBoost.sql. -->

<!-- INTERPRETAR: código fuente (14 - Semana 12/Actividad_12_Laborat_BQ__model_XGBoost.sql). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```sql
CREATE OR REPLACE MODEL
  demo_utec.modelo_xgb

OPTIONS(
  MODEL_TYPE='BOOSTED_TREE_CLASSIFIER',
  INPUT_LABEL_COLS=['income_bracket'],
  MAX_ITERATIONS = 5, 
  NUM_PARALLEL_TREE = 1,
  MAX_TREE_DEPTH=6,
  SUBSAMPLE=0.8,
  LEARN_RATE=0.1
) AS

SELECT
  age,
  education_num,
  hours_per_week,
  capital_gain,
  capital_loss,
  income_bracket
FROM demo_utec.adult_train;


SELECT *
FROM ML.EVALUATE(
MODEL demo_utec.modelo_xgb,
(SELECT * FROM demo_utec.adult_test)
);

SELECT *
FROM ML.CONFUSION_MATRIX(
MODEL demo_utec.modelo_xgb,
(
SELECT * FROM demo_utec.adult_test)
);

SELECT *
FROM ML.ROC_CURVE(
MODEL demo_utec.modelo_xgb,
(SELECT * FROM demo_utec.adult_test)
);
```
