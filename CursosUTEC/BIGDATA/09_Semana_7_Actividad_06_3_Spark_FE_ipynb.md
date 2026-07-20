---
curso: BIGDATA
titulo: 09 - Semana 7/Actividad 06.3 Spark FE
slides: 0
fuente: 09 - Semana 7/Actividad 06.3 Spark FE.ipynb
---

<div class="cell markdown" id="sos5VjsU5Gkp">

## **Feature Engineering**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="MuApcigR5De8">

``` python
!pip install pyspark
```

</div>

<div class="cell code" id="PTEpiiL35DiK">

``` python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Feature Engineering").master("local").getOrCreate()
```

</div>

<div class="cell code" id="vhDBqJbe5DoG">

``` python
data_1 = [('Jorge','Nores','M',3000, "Seguro"),
        ('Alberto','Huanca','M',7100, None),
        ('Julia','Llacsa','F',5200, None)]

columns = ["nombre","apellido","genero","salario", "empresa"]
df1 = spark.createDataFrame(data=data_1, schema = columns)
df1.show()
```

</div>

<div class="cell code" id="S1h1UmFwrBl5">

``` python
df1 = df1.na.fill("Seguro")
df1.show()
```

</div>

<div class="cell code" id="l27pPu-rj7fr">

``` python
data_2 = [('Tania','Napa','F',7500,"Seguro"),
          ('Juana','Cruz',None,5000,"Seguro"),
          ('Elizabeth','Arroyo',None,6000,"Seguro")]

df_adic = spark.createDataFrame(data=data_2, schema = columns)
df_adic.show()
```

</div>

<div class="cell code" id="ckYw7GoekCyD">

``` python
df_adic = df_adic.na.fill({'genero': 'F'})
df_adic.show()
```

</div>

<div class="cell code" id="ak6jSSj3kJqP">

``` python
df1 = df1.union(df_adic)
df1.show(truncate=False)
```

</div>

<div class="cell code" id="ebtGSl2_5Dqp">

``` python
from pyspark.sql.functions import lit
df2 = df1.withColumn("bono_ext_perc", lit(0.3))
df2.show()
```

</div>

<div class="cell code" id="J66BnNQJ5DtS">

``` python
df3 = df2.withColumn("util_anual", df2.salario*1.1)
df3.show()
```

</div>

<div class="cell code" id="qDdlAvkfh8N7">

``` python
df4 = df3.withColumn("util_anual",df3.util_anual.cast("Integer"))
df4.show()
```

</div>

<div class="cell code" id="yxd9cUWEiUVo">

``` python
from pyspark.sql.functions import col
df4 = df3.withColumn("util_anual",col("util_anual").cast("Integer"))
df4.show()
```

</div>

<div class="cell code" id="ld8h1o8AhpTr">

``` python
from pyspark.sql.functions import concat_ws
df5 = df4.withColumn("nombre_completo", concat_ws(",","nombre",'apellido'))
df5.show()
```

</div>

<div class="cell code" id="yPgQZeqMiz6g">

``` python
df5.show()
```

</div>

<div class="cell code" id="4TgPzBkddlWF">

``` python
df6 = df5.withColumn("salario_anual",col("salario")*12)
df6.show()
```

</div>

<div class="cell code" id="mBigcKmGi-s_">

``` python
df7 = df6.withColumnRenamed("genero","sexo")
df7.show(truncate=False)
```

</div>

<div class="cell code" id="u8ash4ftjHfo">

``` python
from pyspark.sql.functions import when
df8 = df7.withColumn("categoria_genero", when(df7.sexo == "M","Masculino")
                                 .when(df7.sexo == "F","Femenino")
                                 .when(df7.sexo.isNull() ,"")
                                 .otherwise(df7.sexo))
df8.show()
```

</div>

<div class="cell code" id="Ja-CQACtjwmj">

``` python
```

</div>
