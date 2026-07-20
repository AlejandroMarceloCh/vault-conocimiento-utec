---
curso: BIGDATA
titulo: 09 - Semana 7/Actividad 06.5 MLlib Clustering
slides: 0
fuente: 09 - Semana 7/Actividad 06.5 MLlib Clustering.ipynb
---

<div class="cell markdown" id="B3p4Zj4s4G9Z">

## **Machine Learning con Spark**

**Clustering**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="CjFaIspj4LwA">

``` python
# 1. Instalar pyspark
!pip install pyspark
```

</div>

<div class="cell code" id="Iva_3M2G4Lzk">

``` python
# 2. Crear SparkSession
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("KMeans").getOrCreate()
```

</div>

<div class="cell code" id="geyMd-ki4jBU">

``` python
from google.colab import drive
drive.mount('/content/drive')
```

</div>

<div class="cell code" id="FCIsnJP-4j_G">

``` python
# 4. Leer el archivo parquet (asegúrate de subir iris.parquet a Colab)
df = spark.read.parquet("/content/drive/MyDrive/Datasets Semana 7/iris.parquet")
```

</div>

<div class="cell code" id="3ol2L6ct4kCI">

``` python
# 5. Renombrar columnas: cambiar "." por "_"
for c in df.columns:
    df = df.withColumnRenamed(c, c.replace(".", "_"))
```

</div>

<div class="cell code" id="MBNgT1905C4A">

``` python
# 6. VectorAssembler para features

from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
    inputCols=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    outputCol="features"
)
df_features = assembler.transform(df)
```

</div>

<div class="cell markdown" id="ZGVLlN1t5VBs">

**Algoritmos de clustering**

------------------------------------------------------------------------

</div>

<div class="cell markdown" id="qxMYyVYB5TPQ">

| Algoritmo | Clase PySpark | Descripción | Uso típico |
|----|----|----|----|
| K-Means | `KMeans` | Agrupa datos en K clusters usando centroides. | Segmentación de clientes, agrupamiento de productos. |
| Bisecting K-Means | `BisectingKMeans` | Variante jerárquica de K-Means que divide clusters recursivamente. | Clustering jerárquico escalable. |
| Gaussian Mixture Model | `GaussianMixture` | Modelo probabilístico basado en mezclas gaussianas. | Segmentación con clusters superpuestos. |
| Latent Dirichlet Allocation | `LDA` | Modelo de tópicos para texto/documentos. | Topic modeling y NLP. |
| Power Iteration Clustering | `PowerIterationClustering` | Clustering basado en grafos y similitud. | Redes, grafos y relaciones complejas. |

</div>

<div class="cell code" id="fVPZY1Vi4kE1">

``` python
# 7. Entrenar KMeans (3 clusters)
from pyspark.ml.clustering import KMeans
kmeans = KMeans(k=3, seed=42, featuresCol="features", predictionCol="cluster")
model = kmeans.fit(df_features)
```

</div>

<div class="cell code" id="SVIZIhpi4L2E">

``` python
# 8. Mostrar centroides
print("Centroides de los clusters:")
for idx, center in enumerate(model.clusterCenters()):
    print(f"Cluster {idx}: {center}")
```

</div>

<div class="cell code" id="OxNnMgkT4L5M">

``` python
# 9. Predicciones: asignar cluster a cada fila
predictions = model.transform(df_features)
predictions.select("sepal_length", "sepal_width", "petal_length", "petal_width", "cluster").show(10)
```

</div>

<div class="cell markdown" id="2fV3dak26bxU">

**WSSSE** calcula qué tan lejos están los puntos respecto a su centroide.

Si los puntos están muy cerca → WSSSE pequeño → buen clustering.

Si están muy dispersos → WSSSE grande → clustering deficiente.

</div>

<div class="cell code" id="WOBULDVP4L79">

``` python
# 10. Métrica WSSSSE
print("WSSSE:", model.summary.trainingCost)
```

</div>
