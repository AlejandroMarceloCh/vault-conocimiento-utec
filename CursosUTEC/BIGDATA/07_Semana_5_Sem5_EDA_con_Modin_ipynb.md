---
curso: BIGDATA
titulo: 07 - Semana 5/Sem5_EDA con Modin
slides: 0
fuente: 07 - Semana 5/Sem5_EDA con Modin.ipynb
---

<div class="cell markdown" id="5MeDJBbAV3Tc">

# **Modin**

</div>

<div class="cell markdown" id="IBadwyvQV4KV">

Curso: Big Data

Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="leREIMS5QE-w">

``` python
!pip install "modin[all]" dask distributed gcsfs
```

</div>

<div class="cell code" id="Gu1JC9JtQIle">

``` python
from google.colab import drive
drive.mount('/content/drive')
```

</div>

<div class="cell code" id="sYQbpgGC7Goj">

``` python
import modin.pandas as mpd
import pandas
```

</div>

<div class="cell code" id="QaoYZ6fjRJb3">

``` python
import modin
print(modin.config.NPartitions.get())
```

</div>

<div class="cell code" id="1qQJblnTQMxE">

``` python
import os
os.environ["MODIN_ENGINE"] = "dask"
```

</div>

<div class="cell code" id="01spUaYUQOHk">

``` python
from dask.distributed import Client
client = Client()  # cluster local automático
client
```

</div>

<div class="cell code" id="UKj-BLko7Gr4">

``` python
mdf = mpd.read_csv('/content/drive/MyDrive/Datasets/yellow_tripdata_2016-01.csv',parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"])
```

</div>

<div class="cell markdown" id="l_OZAuHWa46h">

#### Visualización de los 5 primeros registros

</div>

<div class="cell code" id="rNIwymuo7Guv">

``` python
mdf.head()
```

</div>

<div class="cell markdown" id="2WiLbuDDa-z-">

#### Dimensiones del dataset

</div>

<div class="cell code" id="H6yX8y2L7GxY">

``` python
mdf.shape  # 10.9M
```

</div>

<div class="cell markdown" id="MM9xMZfubJ2R">

#### Estructura del dataset

</div>

<div class="cell code" id="UHFoCOWk-hhi">

``` python
mdf.info()
```

</div>

<div class="cell markdown" id="mUOlTOl7-OHJ">

¿Cuántos viajes se realizaron en el 2016?

</div>

<div class="cell code" id="YcY_20cT7G2w">

``` python
mdf.shape[0]
```

</div>

<div class="cell markdown" id="Z_y7hh_n-ddp">

¿Cuántos pasajeros en total se atendió en el 2016?

</div>

<div class="cell code" id="y6-eV3CZ-fHe">

``` python
mdf['passenger_count'].sum()
```

</div>

<div class="cell markdown" id="lVBhy60v-vOB">

¿Cuánto es la tarifa promedio por viaje?

</div>

<div class="cell code" id="6Fh22dm6-xOC">

``` python
mdf['fare_amount'].mean()
```

</div>

<div class="cell markdown" id="dMftGqvUcQDV">

#### Distancia promedio de los viajes

</div>

<div class="cell code" id="LcuYtroVcQf1">

``` python
mdf["trip_distance"].mean()
```

</div>

<div class="cell markdown" id="fA9CpAMO_G0f">

¿Cuánto es la propina promedio por viaje?

</div>

<div class="cell code" id="3U3mn_0m-_ey">

``` python
mdf['tip_amount'].mean()
```

</div>

<div class="cell markdown" id="_XEsmsas_Ip2">

¿Qué porcentaje de los viajes se pagan en efectivo vs tarjeta?

</div>

<div class="cell code" id="feTnASq3_9Jd">

``` python
mdf['payment_type'].value_counts(normalize=True).iloc[1]*100 # Cash
```

</div>

<div class="cell code" id="jCs-bXDl_OOQ">

``` python
mdf['payment_type'].value_counts(normalize=True).iloc[0]*100  # Credit Card
```

</div>

<div class="cell markdown" id="rEjZIMYdbkXp">

##### Viajes con tarifa negativa o cero (posibles errores

</div>

<div class="cell code" id="6mW9oLLpbmuO">

``` python
errores_tarifa = mdf[mdf["fare_amount"] <= 0]
errores_tarifa.head()
```

</div>

<div class="cell markdown" id="STMdadcBNJOQ">

#### Calcular la duración del viaje en minutos

</div>

<div class="cell code" id="MRyvgEg4NJkk">

``` python
mdf["duracion_min"] = (mdf["tpep_dropoff_datetime"] - mdf["tpep_pickup_datetime"]).dt.total_seconds() / 60
mdf.head()
```

</div>

<div class="cell markdown" id="jO6qSUDMdikH">

#### Exportar un subconjunto del dataset

</div>

<div class="cell code" id="PkrBzA65dhmI">

``` python
df_filtrado = mdf[mdf["trip_distance"] > 10]
df_filtrado.head()
```

</div>

<div class="cell markdown" id="7xMLapjWNJ84">

¿Cada viaje es corto (\< 2 millas), mediano (2–10 millas) o largo (\> 10 millas)? (Clasificación personalizada).

</div>

<div class="cell code" id="JuLgMGFNNKEj">

``` python
def clasificar_distancia(millas):
    if millas < 2:
        return "Corto"
    elif millas <= 10:
        return "Medio"
    else:
        return "Largo"

mdf["trip_category"] = mdf["trip_distance"].apply(clasificar_distancia)
mdf.head()
```

</div>
