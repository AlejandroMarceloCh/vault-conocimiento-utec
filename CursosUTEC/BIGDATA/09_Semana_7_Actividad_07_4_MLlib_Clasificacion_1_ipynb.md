---
curso: BIGDATA
titulo: 09 - Semana 7/Actividad_07_4_MLlib_Clasificación (1)
slides: 0
fuente: 09 - Semana 7/Actividad_07_4_MLlib_Clasificación (1).ipynb
---

<div class="cell markdown" id="dF7SZCddXAJa">

## **Machine Learning con Spark**

**Clasificación**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="bO0ZINYLWreb">

``` python
!pip install pyspark
```

</div>

<div class="cell code" id="jjdgD2xuW8TY">

``` python
# 1. Inicializar Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Clasificación").getOrCreate()
```

</div>

<div class="cell code" id="1dQAfjSjDRPE">

``` python
#from google.colab import drive
#drive.mount('/content/drive')
```

</div>

<div class="cell code" id="LRJOqMYlXBMn">

``` python
# 2. Cargar dataset
df = spark.read.parquet("/content/drive/MyDrive/Datasets Semana 7/weather.parquet")
df.printSchema()
df.show(5)
```

</div>

<div class="cell code" id="Pyyg6IYoKj0L">

``` python
df = df.drop("RISK_MM")
```

</div>

<div class="cell code" id="WI8M5j6aLQHH">

``` python
df.printSchema()
```

</div>

<div class="cell code" id="QjwkOExqIKiE">

``` python
df = df.replace(["NA", "N/A", "null", ""], None)
```

</div>

<div class="cell code" id="DxzOf1kud4-J">

``` python
# Número de filas
num_filas = df.count()
num_filas
```

</div>

<div class="cell code" id="0wbDWURed7GX">

``` python
# Número de columnas
num_columnas = len(df.columns)
num_columnas
```

</div>

<div class="cell code" id="E0BWILN2IPxE">

``` python
df.printSchema()
```

</div>

<div class="cell code" id="mjUdIKfyXBPu">

``` python
# 3. Variables
from pyspark.sql.functions import col

numeric_cols = ["MinTemp","MaxTemp","Rainfall","Evaporation",
                "WindSpeed9am","WindSpeed3pm",
                "Humidity9am","Humidity3pm",
                "Pressure9am","Pressure3pm",
                "Cloud9am","Cloud3pm",
                "Temp9am","Temp3pm"]

for c in numeric_cols:
    df = df.withColumn(c, col(c).cast("double"))
```

</div>

<div class="cell code" id="0KDj7QS7bSJJ">

``` python
# 4. conteo de nulos

from pyspark.sql.functions import col, sum

df = df.replace( ["NA", "N/A", "null", ""],  None)

from pyspark.sql.functions import col, sum

df.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in df.columns
]).show()
```

</div>

<div class="cell code" id="7wLoKe53YI2G">

``` python
# 5. Manejo de valores nulos

categorical_cols = ["Sunshine","WindGustDir","WindDir9am","WindDir3pm","RainToday"]

# Reemplazar nulos
df = df.fillna(0, subset=numeric_cols)  # numéricas
df = df.fillna("missing", subset=categorical_cols + ["RainTomorrow"])
```

</div>

<div class="cell code" id="3lVnQvK_Zjfm">

``` python
# 6. Codificación de categóricas

from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler

indexers = {}
encoders = {}
for c in categorical_cols:
    indexers[c] = StringIndexer(inputCol=c, outputCol=c+"_idx", handleInvalid="keep")
    df = indexers[c].fit(df).transform(df)
    encoders[c] = OneHotEncoder(inputCol=c+"_idx", outputCol=c+"_vec")
    df = encoders[c].fit(df).transform(df)
```

</div>

<div class="cell code" id="1FjfjhrCZqfd">

``` python
# 7. VectorAssembler

from pyspark.ml.feature import VectorAssembler

feature_cols = numeric_cols + [c+"_vec" for c in categorical_cols]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
df = assembler.transform(df)
```

</div>

<div class="cell code" id="9NQNfmkJZtAz">

``` python
# 8. Indexar target (RainTomorrow)

label_indexer = StringIndexer(inputCol="RainTomorrow", outputCol="label", handleInvalid="keep")
df = label_indexer.fit(df).transform(df)
```

</div>

<div class="cell code" id="6cfccErHZvCm">

``` python
# 9. Train/Test split
train_df, test_df = df.randomSplit([0.7, 0.3], seed=42)
```

</div>

<div class="cell code" id="QcC3sLxnZvTL">

``` python
# 10. Árbol de decisión

from pyspark.ml.classification import DecisionTreeClassifier

dt = DecisionTreeClassifier(featuresCol="features", labelCol="label", maxDepth=4, seed=42 )
model = dt.fit(train_df)
```

</div>

<div class="cell code" id="FMkokGhjZymQ">

``` python
# 11. Predicciones

predictions = model.transform(test_df)
predictions.select("RainTomorrow","label","prediction","probability").show(10, truncate=False)
```

</div>

<div class="cell code" id="ttqWLibCZ0sH">

``` python
# 12. Evaluación

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Accuracy en test:", accuracy)

print("Estructura del Árbol:")
print(model.toDebugString)
```

</div>

<div class="cell code" id="_PRoBShoMISX">

``` python
feature_names = assembler.getInputCols()

importances = model.featureImportances

importance_list = list(zip(feature_names, importances))

importance_list = sorted(
    importance_list,
    key=lambda x: x[1],
    reverse=True
)

for feature, importance in importance_list:
    print(f"{feature}: {importance:.4f}")
```

</div>
