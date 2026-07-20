---
curso: BIGDATA
titulo: 08 - Semana 6/Actividad 06.1 Spark Carga Archivos
slides: 0
fuente: 08 - Semana 6/Actividad 06.1 Spark Carga Archivos.ipynb
---

<div class="cell markdown" id="SZCJ4ZZoSm61">

## **Funciones de Spark**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="mF7GjDRTBhQV">

``` python
!pip install pyspark
```

</div>

<div class="cell code" id="EScD1Y4C-Oq6">

``` python
import pyspark
from pyspark.sql import DataFrame, SparkSession
from typing import List
import pyspark.sql.types as T
import pyspark.sql.functions as F
```

</div>

<div class="cell code" id="JpIuu_FbB6az">

``` python
spark= SparkSession.builder.appName("Funciones de Spark").getOrCreate()
spark
```

</div>

<div class="cell code" id="qjs67K_u910S">

``` python
from google.colab import drive
drive.mount('/content/drive')
```

</div>

<div class="cell code" id="U0yZHBl7B6d_">

``` python
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext
from pyspark.sql import SQLContext
```

</div>

<div class="cell markdown" id="m8sWwyyFN6Hl">

### **Carga de variedad de archivos en spark.read:**

------------------------------------------------------------------------

</div>

<div class="cell code" id="cCmexecPEQJO">

``` python
[m for m in dir(spark.read) if not m.startswith("_")]
```

</div>

<div class="cell markdown" id="Hn_rGw05Nxf6">

### **Carga de Archivo CSV**

------------------------------------------------------------------------

</div>

<div class="cell code" id="TOMGqq9qB6i-">

``` python
df_csv =spark.read.csv("/content/drive/MyDrive/Datasets Semana 6/salaries.csv")
```

</div>

<div class="cell code" id="JZPEYUQ-B6lb">

``` python
df_csv.show(5,False)
```

</div>

<div class="cell code" id="vglY7A3fFFJI">

``` python
df_csv =spark.read.csv("/content/drive/MyDrive/Datasets Semana 6/salaries.csv",header=True)
```

</div>

<div class="cell code" id="4Fx-srkOFI9Q">

``` python
df_csv.show(5)
```

</div>

<div class="cell markdown" id="rqDY0mVoNt4l">

### **Carga de Archivo JSON**

------------------------------------------------------------------------

</div>

<div class="cell code" id="B0nir6pFB6gZ">

``` python
df_json =spark.read.json("/content/drive/MyDrive/Datasets Semana 6/adults.json")
```

</div>

<div class="cell code" id="mLeHD1d9DxNh">

``` python
df_json.show(5,False)
```

</div>

<div class="cell markdown" id="4ru2mIYwNgS0">

### **Carga de Archivo Parquet**

------------------------------------------------------------------------

</div>

<div class="cell code" id="vjl52OUED0DT">

``` python
df_parquet =spark.read.parquet("/content/drive/MyDrive/Datasets Semana 6/titanic.parquet")
```

</div>

<div class="cell code" id="hwL_nl_QEBck">

``` python
df_parquet.show(5)
```

</div>

<div class="cell markdown" id="doIsVRxgNXSd">

### **Estructura del dataframe**

------------------------------------------------------------------------

</div>

<div class="cell code" id="qiT91tc8EHY-">

``` python
df_csv.printSchema()
```

</div>

<div class="cell markdown" id="UaQV6xoqMd_E">

### **Definir Estructura**

</div>

<div class="cell code" id="2VP3Yi63Maeh">

``` python
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
```

</div>

<div class="cell code" id="X8hGv1-TMmtJ">

``` python
# Definir el esquema
schema = StructType([
    StructField("work_year", IntegerType(), True),
    StructField("experience_level", StringType(), True),
    StructField("employment_type", StringType(), True),
    StructField("job_title", StringType(), True),
    StructField("salary", IntegerType(), True),
    StructField("salary_currency", StringType(), True),
    StructField("salary_in_usd", IntegerType(), True),
    StructField("employee_residence", StringType(), True),
    StructField("remote_ratio", IntegerType(), True),
    StructField("company_location", StringType(), True),
    StructField("company_size", StringType(), True)
])
```

</div>

<div class="cell code" id="gxzAyMskMr5l">

``` python
df_csv = spark.read.csv("/content/drive/MyDrive/Datasets Semana 6/salaries.csv",
    header=True,
    schema=schema
)
```

</div>

<div class="cell code" id="JgYSGyEbM09h">

``` python
df_csv.printSchema()
```

</div>

<div class="cell markdown" id="GLaWvCKuNPNR">

### **Inferir Esquema**

</div>

<div class="cell code" id="FvflADmVEHbd">

``` python
df_csv =spark.read.csv("/content/drive/MyDrive/Datasets Semana 6/salaries.csv",header=True, inferSchema=True)
df_csv.printSchema()
```

</div>

<div class="cell code" id="DJuloaRqEHeK">

``` python
df_csv.count()
```

</div>

<div class="cell code" id="OOE2GsH2EHgw">

``` python
df_csv.show(5)
```

</div>

<div class="cell markdown" id="O5Sd6HyNHozJ">

### **Lista de todas las funciones de pyspark.sql.functions**

------------------------------------------------------------------------

</div>

<div class="cell code" id="DndBF-PlHbUN">

``` python
import pyspark.sql.functions as F
[f for f in dir(F) if not f.startswith("_")]
```

</div>

<div class="cell markdown" id="EfxU3YrDF1Tx">

### Funciones básicas de agregación

- `count(col)` → número de filas no nulas.\

- `countDistinct(col1, col2, ...)` → valores distintos.\

- `approx_count_distinct(col, rsd)` → conteo aproximado (más rápido).

- `sum(col)` → suma de valores.\

- `sumDistinct(col)` → suma de valores distintos.

- `avg(col)` o `mean(col)` → promedio.

- `min(col)` → valor mínimo.\

- `max(col)` → valor máximo.

- `first(col)` → primer valor encontrado.\

- `last(col)` → último valor encontrado.

</div>

<div class="cell code" id="LeGgfX8jH7Yl">

``` python
import pyspark.sql.functions as F
```

</div>

<div class="cell code" id="BlrSpir8H9If">

``` python
df_csv.printSchema()
```

</div>

<div class="cell code" id="0gdTTQLRF0DD">

``` python
# Conteo de numero de filas
df_csv.agg(F.count("*")).show()
```

</div>

<div class="cell code" id="oudD7_AbIERI">

``` python
# Conteo distintos
df_csv.agg(F.count_distinct("work_year")).show()
```

</div>

<div class="cell code" id="epvXPGBfIxq5">

``` python
# Suma
df_csv.agg(F.sum("salary")).show()
```

</div>

<div class="cell code" id="EFlHNq8DIxty">

``` python
# Promedio
df_csv.agg(F.avg("salary")).show()
```

</div>

<div class="cell code" id="Gok7uvt-IxwH">

``` python
# Máximo
df_csv.agg(F.max("salary")).show()
```

</div>

<div class="cell code" id="HFbAYFqLIxyX">

``` python
# Mínimo
df_csv.agg(F.min("salary")).show()
```

</div>

<div class="cell code" id="iVG7qynuIx00">

``` python
# Primer valor
df_csv.groupBy("work_year").agg(F.first("employment_type")).show()
```

</div>

<div class="cell code" id="i7dzfc-KIx3I">

``` python
# Último valor
df_csv.groupBy("work_year").agg(F.last("employment_type")).show()
```

</div>

<div class="cell markdown" id="nYjiLeEbJ7Hr">

### **Funciones estadísticas**

------------------------------------------------------------------------

- `variance(col)` o `var_samp(col)` → varianza muestral.\
- `var_pop(col)` → varianza poblacional.\
- `stddev(col)` o `stddev_samp(col)` → desviación estándar muestral.\
- `stddev_pop(col)` → desviación estándar poblacional.\
- `skewness(col)` → sesgo.\
- `kurtosis(col)` → curtosis.

</div>

<div class="cell code" id="NA8wWWeLKDEf">

``` python
# Varianza muestral
df_csv.agg(F.variance("salary_in_usd")).show()
```

</div>

<div class="cell code" id="Rw4JXgY4KeS6">

``` python
# Varianza poblacional
df_csv.agg(F.var_pop("salary_in_usd")).show()
```

</div>

<div class="cell code" id="he8zH0KoKgqx">

``` python
# Desviación estándar muestral
df_csv.agg(F.stddev("salary_in_usd")).show()
```

</div>

<div class="cell code" id="GqJaXpsIKgtu">

``` python
# Desviación estándar poblacional
df_csv.agg(F.stddev_pop("salary_in_usd")).show()
```

</div>

<div class="cell code" id="SpE1EQR7KgwW">

``` python
# Asimetria / Sesgo
df_csv.agg(F.skewness("salary_in_usd")).show()
```

</div>

<div class="cell code" id="TMTKMuRxKgy2">

``` python
# Curtosis / Apuntalamiento
df_csv.agg(F.kurtosis("salary_in_usd")).show()
```

</div>

<div class="cell code" id="K9BlEdsaKxvt">

``` python
# Percentiles (aproximación)
df_csv.approxQuantile("salary_in_usd", [0.25, 0.5, 0.75], 0.01)
```

</div>

<div class="cell markdown" id="iXuWMJf4OVxn">

### **Agrupaciones: groupBy**

------------------------------------------------------------------------

</div>

<div class="cell code" id="bmoQOl7TKxy9">

``` python
df_csv.groupBy("work_year").agg(F.avg("salary_in_usd")).show()
```

</div>

<div class="cell code" id="9RJnkg6nKx1A">

``` python
df_csv.groupBy("work_year").agg(F.avg("salary_in_usd").alias("promedio")).show()
```

</div>

<div class="cell code" id="hvwRKyQbKg1K">

``` python
df_csv.groupBy("work_year").agg(
    F.avg("salary_in_usd").alias("promedio"),
    F.variance("salary_in_usd").alias("varianza_muestral"),
    F.var_pop("salary_in_usd").alias("varianza_poblacional")
    ).show()
```

</div>

<div class="cell markdown" id="LsxW7zbIPWfw">

### **Operaciones sobre DataFrames: Selección y filtros**

</div>

<div class="cell markdown" id="-1pNoEpCPe9B">

#### 1. **filter**

`filter` permite seleccionar las filas de un DataFrame que cumplen con una condición lógica.\
Es equivalente a aplicar un `WHERE` en SQL.

</div>

<div class="cell code" id="zYwiVpbyL7MR">

``` python
# Empleados con salario mayor a 750,000 USD
df_csv.filter(df_csv.salary_in_usd > 750000).show()
```

</div>

<div class="cell markdown" id="9EZJMxsSPtOR">

#### 2. **where**

`where` es exactamente lo mismo que `filter`, solo cambia la sintaxis.\
Se usa para aplicar condiciones sobre las filas.

</div>

<div class="cell code" id="VUs_MGnrL7Pt">

``` python
# Empleados que trabajan 100% remoto
df_csv.where(df_csv.remote_ratio == 100).show()
```

</div>

<div class="cell markdown" id="0I_KIe2PP5dN">

#### 3. **select**

`select` permite escoger columnas específicas de un DataFrame.\
También se puede usar para renombrarlas o aplicar funciones sobre ellas.

</div>

<div class="cell code" id="MhByDSoAL7Vb">

``` python
# Mostrar solo puesto, salario en USD y ubicación de la empresa
df_csv.select("job_title", "salary_in_usd", "company_location").show(5)
```

</div>

<div class="cell code" id="_AzdZnpoL7XL">

``` python
# Selección con alias para renombrar columnas
df_csv.select(
    col("job_title").alias("Puesto"),
    col("salary_in_usd").alias("Salario_USD")
).show()
```

</div>

<div class="cell code" id="hQ01Zbh5QciV">

``` python
# Ordenar por salario en USD de forma descendente
df_csv.sort(df_csv.salary_in_usd.desc()).show()
```

</div>

<div class="cell code" id="3pGK8eVeQnvM">

``` python
# Ordenar por año y salario en orden ascendente
df_csv.sort("work_year", "salary_in_usd").show()
```

</div>

<div class="cell markdown" id="_h29eLHFRBg5">

#### 5. **orderby**

El método `.orderBy()` funciona igual que `sort()`.\
Permite ordenar un DataFrame por una o varias columnas.\
La diferencia es principalmente de estilo: ambos (`sort` y `orderBy`) son equivalentes.

</div>

<div class="cell code" id="_LRZJAZxRA5w">

``` python
# Ordenar empleados por salario en USD descendente
df_csv.orderBy(df_csv.salary_in_usd.desc()).show()
```

</div>

<div class="cell code" id="PUHlONOVRA9C">

``` python
# Ordenar por año y salario
df_csv.orderBy("work_year", "salary_in_usd").show()
```

</div>

<div class="cell markdown" id="kahqkhSqROkH">

### 6. **na.drop**

El método `.na.drop()` se usa para eliminar filas que contienen valores nulos (NaN o None).\
Se puede aplicar a todo el DataFrame o solo a columnas específicas.

</div>

<div class="cell code" id="WLpNuIFaRBCP">

``` python
# Eliminar cualquier fila que tenga valores nulos en cualquier columna
df_csv.na.drop().show()
```

</div>

<div class="cell code" id="t91GiUf4RBE_">

``` python
# Eliminar filas solo si tienen nulos en la columna 'salary_in_usd'
df_csv.na.drop(subset=["salary_in_usd"]).show()
```

</div>
