---
curso: BIGDATA
titulo: 09 - Semana 7/Actividad 06.4 MLlib Regresión
slides: 0
fuente: 09 - Semana 7/Actividad 06.4 MLlib Regresión.ipynb
---

<div class="cell markdown" id="lPceLu6qulFA">

## **Machine Learning con Spark**

**Regresión**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="ojX2jtC4tfHE">

``` python
!pip install pyspark
```

</div>

<div class="cell code" id="15fd5xeduq6n">

``` python
# 1. Inicializar Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Regression").getOrCreate()
```

</div>

<div class="cell code" id="uldY3tepvb_y">

``` python
from google.colab import drive
drive.mount('/content/drive')
```

</div>

<div class="cell code" id="XazmHj8ouq9n">

``` python
# 2. Cargar dataset
df = spark.read.parquet("/content/drive/MyDrive/Datasets Semana 7/house-price.parquet")
df.printSchema()
df.show(5)
```

</div>

<div class="cell code" id="4FNTCsiFurAX">

``` python
# 3. Variables categóricas y numéricas
categorical_cols = ["mainroad", "guestroom", "basement",
                    "hotwaterheating", "airconditioning",
                    "prefarea", "furnishingstatus"]

numeric_cols = ["area", "bedrooms", "bathrooms", "stories", "parking"]
```

</div>

<div class="cell code" id="S0aHzJbhurDA">

``` python
# 4. Indexar y codificar categóricas
from pyspark.ml.feature import StringIndexer, OneHotEncoder

for col in categorical_cols:
    indexer = StringIndexer(inputCol=col, outputCol=col+"_index", handleInvalid="keep")
    df = indexer.fit(df).transform(df)

    encoder = OneHotEncoder(inputCol=col+"_index", outputCol=col+"_vec")
    df = encoder.fit(df).transform(df)
```

</div>

<div class="cell code" id="lQoHX8H5vFAL">

``` python
df.show(5)
```

</div>

<div class="cell code" id="pD6H7_F8vFDi">

``` python
# 5. VectorAssembler para juntar numéricas + categóricas codificadas
from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
    inputCols=numeric_cols + [col+"_vec" for col in categorical_cols],
    outputCol="features"
)
df = assembler.transform(df).select("features", df["price"].alias("label"))
```

</div>

<div class="cell code" id="3ejn-8tRvFFu">

``` python
# 6. Train/Test split
train_df, test_df = df.randomSplit([0.7, 0.3], seed=42)
```

</div>

<div class="cell markdown" id="VxMl3nxF3avi">

**Algoritmos de Regresión en PySpark**

------------------------------------------------------------------------

</div>

<div class="cell markdown" id="QRdjcCBP3dxs">

| Modelo | Clase PySpark | Descripción | Uso típico |
|----|----|----|----|
| Regresión Lineal | `LinearRegression` | Modelo lineal clásico para predecir valores continuos. | Predicción de ventas, precios, demanda, riesgo. |
| Regresión Lineal Generalizada | `GeneralizedLinearRegression` | Extiende regresión lineal usando distintas distribuciones y funciones link. | Seguros, salud, conteos, modelos actuariales. |
| Árbol de Decisión para Regresión | `DecisionTreeRegressor` | Modelo basado en reglas y divisiones jerárquicas. | Modelos interpretables y no lineales. |
| Random Forest Regressor | `RandomForestRegressor` | Conjunto de múltiples árboles de decisión. | Alta precisión y reducción de overfitting. |
| Gradient Boosted Trees Regressor | `GBTRegressor` | Ensamble secuencial de árboles optimizando errores previos. | Modelos predictivos avanzados y competiciones ML. |
| Regresión Isotónica | `IsotonicRegression` | Ajusta una relación monótona entre variables. | Scorecards, calibración de probabilidades. |
| Factorization Machines Regressor | `FMRegressor` | Modelo que captura interacciones entre variables sparse. | Sistemas de recomendación y datasets de alta dimensión. |
| Survival Regression | `AFTSurvivalRegression` | Modelo Accelerated Failure Time para análisis de supervivencia. | Riesgo de churn, tiempo hasta incumplimiento o falla. |

</div>

<div class="cell code" id="Hh1xXhe3vFIT">

``` python
# 7. Entrenar Regresión Lineal
from pyspark.ml.regression import LinearRegression

lr = LinearRegression(featuresCol="features", labelCol="label")
model = lr.fit(train_df)
```

</div>

<div class="cell markdown" id="c2zT_NFk2nBW">

**Métodos en Regresión (output)**

------------------------------------------------------------------------

</div>

<div class="cell markdown" id="LEt8bkwC1sCa">

| Método | Descripción | Comando |
|----|----|----|
| `coefficients` | Obtiene los coeficientes de la regresión lineal. | `model.coefficients` |
| `intercept` | Obtiene el intercepto del modelo. | `model.intercept` |
| `transform()` | Genera predicciones sobre un DataFrame. | `model.transform(test_df)` |
| `summary` | Muestra el resumen estadístico del modelo. | `model.summary` |
| `summary.r2` | Obtiene el coeficiente de determinación R². | `model.summary.r2` |
| `summary.rmse` | Obtiene el error cuadrático medio raíz. | `model.summary.rmse` |
| `summary.meanAbsoluteError` | Obtiene el error absoluto medio. | `model.summary.meanAbsoluteError` |
| `summary.residuals` | Muestra los residuos o errores del modelo. | `model.summary.residuals.show()` |
| `evaluate()` | Evalúa el modelo con otro dataset. | `model.evaluate(test_df)` |
| `save()` | Guarda el modelo entrenado. | `model.save("modelo_lr")` |
| `load()` | Carga un modelo previamente guardado. | `LinearRegressionModel.load("modelo_lr")` |
| `numFeatures` | Muestra la cantidad de variables predictoras. | `model.numFeatures` |
| `getPredictionCol()` | Obtiene el nombre de la columna de predicción. | `model.getPredictionCol()` |
| `extractParamMap()` | Muestra los parámetros configurados del modelo. | `model.extractParamMap()` |
| `explainParams()` | Describe todos los parámetros del modelo. | `model.explainParams()` |
| `hasSummary` | Indica si el modelo tiene resumen estadístico. | `model.hasSummary` |

</div>

<div class="cell code" id="ah2RjZ4611Up">

``` python
# 8. Resultados del modelo
print("Intercepto:", model.intercept)
print("Coeficientes:", model.coefficients)
```

</div>

<div class="cell code" id="PznUSdHA11YN">

``` python
# 9. Predicciones
predictions = model.transform(test_df)
predictions.select("label", "prediction").show(10, truncate=False)
```

</div>

<div class="cell markdown" id="n3555BWA2bL-">

**Métricas en Regresión**

------------------------------------------------------------------------

</div>

<div class="cell markdown" id="phoSnouG2kfZ">

| metricName | Descripción | Interpretación |
|----|----|----|
| `"rmse"` | Root Mean Squared Error | Penaliza más los errores grandes. Mientras menor, mejor. |
| `"mse"` | Mean Squared Error | Similar al RMSE pero sin raíz cuadrada. |
| `"mae"` | Mean Absolute Error | Error promedio absoluto. Más robusto ante outliers. |
| `"r2"` | Coeficiente de determinación | Mide qué tanto explica el modelo. Más cercano a 1, mejor. |
| `"var"` | Explained Variance | Mide la varianza explicada por el modelo. |

</div>

<div class="cell code" id="N-Vh7kGN11bZ">

``` python
# 10. Evaluación
from pyspark.ml.evaluation import RegressionEvaluator

evaluator = RegressionEvaluator(labelCol="label", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
r2 = evaluator.evaluate(predictions, {evaluator.metricName: "r2"})

print("RMSE en test:", rmse)
print("R² en test:", r2)
```

</div>

<div class="cell code" id="2OHDWnuD11dx">

``` python
```

</div>
