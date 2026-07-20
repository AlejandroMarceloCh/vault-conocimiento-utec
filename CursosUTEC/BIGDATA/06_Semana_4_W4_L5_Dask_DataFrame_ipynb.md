---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L5 Dask DataFrame
slides: 0
fuente: 06 - Semana 4/W4 L5 Dask DataFrame.ipynb
---

<div class="cell markdown" id="gO_hiKdtZpiz">

# Análisis Exploratorio con **Dask**

</div>

<div class="cell markdown" id="y6RWCzrgZzgl">

Curso: Big Data - UTEC

</div>

<div class="cell markdown" id="pq0dsmCKZxoK">

Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="WUam_H5eUF2y">

``` python
import dask.dataframe as dd
import matplotlib.pyplot as plt
import os
```

</div>

<div class="cell code" id="FVDrpUCpUfix">

``` python
# Especificamos el tamaño del blocksize
ddf = dd.read_csv("/content/drive/MyDrive/Datasets/yellow_tripdata_2016-02.csv", blocksize="1MB",dtype={'tolls_amount': 'float64'})
```

</div>

<div class="cell code" id="t200uXBAgwtX">

``` python
%whos
```

</div>

<div class="cell code" id="N5f0DaC1UbjB">

``` python
# Visualizamos el número de particiones
print("Número de particiones:", ddf.npartitions)
```

</div>

<div class="cell code" id="X07nRWteUSqp">

``` python
# Dask determina el tamaño del blocksize
ddf = dd.read_csv("/content/drive/MyDrive/Datasets/yellow_tripdata_2016-02.csv",dtype={'tolls_amount': 'float64'})
```

</div>

<div class="cell code" id="H-HYmxKUUnDX">

``` python
# Visualizamos el número de particiones
print("Número de particiones:", ddf.npartitions)
```

</div>

<div class="cell code" id="v5sp9UMBg5ra">

``` python
# Visualizamos los 5 primeros registros de la 1ra partición
ddf.head()
```

</div>

<div class="cell code" id="PSsz-TRNazHN">

``` python
# Visualizamos los 5 primeros registros de la 1ra partición
ddf.partitions[0].head()
```

</div>

<div class="cell code" id="8ECPVNnnbACm">

``` python
# Visualizamos los 5 primeros registros de la última partición
ddf.partitions[26].tail()
```

</div>

<div class="cell code" id="pVDrWAB7Uuzx">

``` python
# Vemos los tipos de datos de las variables
print(ddf.dtypes)
```

</div>

<div class="cell code" id="-EYgqGHVXAsP">

``` python
# Visualizamos las columnas
ddf.columns
```

</div>

<div class="cell code" id="2cpq-84fWv9V">

``` python
# Número de columnas
n_cols = len(ddf.columns)
n_cols
```

</div>

<div class="cell code" id="pgVcZ4VdWwAL">

``` python
# Número de filas
n_filas = ddf["VendorID"].count().compute()
n_filas
```

</div>

<div class="cell code" id="En9wouM0WwCt">

``` python
# Conteo de valores nulos por columna
missing = ddf.isnull().sum().compute()
print("Valores nulos por columna:\n", missing)
```

</div>

<div class="cell code" id="yg_sv4VnWwFZ">

``` python
# Estadísticas numéricas
print(ddf.describe().compute())
```

</div>

<div class="cell code" id="QN84dU74WwNp">

``` python
# Convertir fechas
ddf["tpep_pickup_datetime"] = dd.to_datetime(ddf["tpep_pickup_datetime"])
ddf["tpep_dropoff_datetime"] = dd.to_datetime(ddf["tpep_dropoff_datetime"])
```

</div>

<div class="cell code" id="2E6M-rBBWwQK">

``` python
# Ver el esquema del DataFrame
print(ddf.dtypes)
```

</div>

<div class="cell code" id="E02neVSMWwTe">

``` python
# Crear variable de duración (en minutos)
ddf["trip_duration_min"] = ((ddf["tpep_dropoff_datetime"] - ddf["tpep_pickup_datetime"]).dt.total_seconds() / 60)
ddf["trip_duration_min"].head()
```

</div>

<div class="cell code" id="pdpfTVArWwWG">

``` python
# Promedio de duración
print("Promedio duración (min):", ddf["trip_duration_min"].mean().compute())
```

</div>

<div class="cell code" id="pv8BHPBVZIN_">

``` python
# Tabla de frecuencias de la variable payment_type
ddf["payment_type"].value_counts().compute()
```

</div>

<div class="cell code" id="b6ivHeZXZISF">

``` python
ddf["payment_type"].unique().compute()
```

</div>

<div class="cell code" id="UmkDBj0wb1FK">

``` python
# Tomar muestra del 1% para graficar
sample = ddf.sample(frac=0.01, random_state=42).compute()
```

</div>

<div class="cell code" id="27AoTi5Mb1Ia">

``` python
# Histograma de duración de viajes
sample["trip_duration_min"].plot(kind="hist", bins=50, figsize=(8,4))
plt.title("Distribución de duración de viajes (muestra 1%)")
plt.xlabel("Minutos")
plt.show()
```

</div>

<div class="cell code" id="2jAQ2Jeab1K7">

``` python
# Relación distancia vs tarifa
sample.plot.scatter(x="trip_distance", y="fare_amount", alpha=0.3, figsize=(8,4))
plt.title("Distancia vs Tarifa (muestra 1%)")
plt.show()
```

</div>

<div class="cell code" id="LPVCaYuWb1Nm">

``` python
# Promedio de duración por tipo de pago
print(ddf.groupby("payment_type")["trip_duration_min"].mean().compute())
```

</div>

<div class="cell code" id="59ygZNwIb1QP">

``` python
# Número de viajes por proveedor
print(ddf.groupby("VendorID").size().compute())
```

</div>

<div class="cell code" id="UuZyGpkrb1S9">

``` python
# Tarifa promedio por día
print(ddf.groupby(ddf["tpep_pickup_datetime"].dt.date)["fare_amount"].mean().compute().head())
```

</div>

<div class="cell code" id="mvb7f0-6b1Vd">

``` python
# Cuantiles
ddf["trip_distance"].quantile([0.25, 0.5, 0.75]).compute()
```

</div>

<div class="cell code" id="3XTIpPIzb1X9">

``` python
# Matriz de Correlación
ddf[["trip_distance", "fare_amount", "tip_amount"]].corr().compute()
```

</div>

<div class="cell code" id="4Mf_hJm6c4kD">

``` python
# Agrupaciones
ddf.groupby("payment_type")["fare_amount"].agg(["mean", "median", "count"]).compute()
```

</div>

<div class="cell code" id="XVRq2Iqic4nP">

``` python
# Ordenar (si el dataset es muy grande va demorar...)
ddf.nlargest(10, "fare_amount").compute()
```

</div>

<div class="cell code" id="RjpMvIUTc4p4">

``` python
# Cambiar número de particiones
ddf2 = ddf.repartition(npartitions=50)
# Visualizamos el número de particiones
print("Número de particiones:", ddf2.npartitions)
```

</div>

<div class="cell code" id="Cc8FW5Lgc4st">

``` python
# Cambiar por tamaño aproximado (p.e 20MB por partición)
ddf3 = ddf.repartition(partition_size="20MB")
# Visualizamos el número de particiones
print("Número de particiones:", ddf3.npartitions)
```

</div>

<div class="cell code" id="lJkVppuQe5lS">

``` python
# Filtro por condicionales
long_trips = ddf[ddf["trip_distance"] > 10]
print(long_trips.head())
```

</div>

<div class="cell code" id="4ivv9eURe8_6">

``` python
# Crear carpeta si no existe
os.makedirs("/content/drive/MyDrive/Output", exist_ok=True)
```

</div>

<div class="cell code" id="nXW5piRne9DC">

``` python
ddf.to_csv("/content/drive/MyDrive/Output/trips-*.csv", index=False)
```

</div>

<div class="cell code" id="H4QWACMRe9FV">

``` python
```

</div>

<div class="cell code" id="Kauqd-4ie9IK">

``` python
```

</div>

<div class="cell code" id="_F1JHQmUe9K4">

``` python
```

</div>

<div class="cell code" id="PhqC--1pe9No">

``` python
```

</div>
