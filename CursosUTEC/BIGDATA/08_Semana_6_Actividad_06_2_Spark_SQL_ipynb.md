---
curso: BIGDATA
titulo: 08 - Semana 6/Actividad 06.2 Spark SQL
slides: 0
fuente: 08 - Semana 6/Actividad 06.2 Spark SQL.ipynb
---

<div class="cell markdown" id="bzf9sWQ8YBP7">

## **Funciones de Spark**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="lgOYCLxp8Z0v">

``` python
!pip install pyspark
```

</div>

<div class="cell code" id="EiZaBKlC8bA9">

``` python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SparkApp").master("local").getOrCreate()
```

</div>

<div class="cell code" id="DqaB7eSz8tPl">

``` python
import pyspark
from pyspark.sql import DataFrame, SparkSession
from typing import List
import pyspark.sql.types as T
import pyspark.sql.functions as F
```

</div>

<div class="cell code" id="QeINw7ZS8xeG">

``` python
from google.colab import drive
drive.mount('/content/drive')
```

</div>

<div class="cell code" id="rJIbgkOTYHw1">

``` python
df_csv =spark.read.csv("/content/drive/MyDrive/Datasets Semana 6/salaries.csv",header=True, inferSchema=True)
df_csv.printSchema()
```

</div>

<div class="cell markdown" id="E84oVu0edUKm">

#### **Crear vista temporal**

------------------------------------------------------------------------

</div>

<div class="cell code" id="jdaCpeNGYHz0">

``` python
df_csv.createOrReplaceTempView("empleados")
```

</div>

<div class="cell markdown" id="AbmRFJTkdrQj">

#### **Ver todos los datos**

------------------------------------------------------------------------

</div>

<div class="cell code" id="oKUORLdKYH2p">

``` python
# Consulta que selecciona todas las columnas y filas de la tabla empleados
spark.sql("SELECT * FROM empleados").show(5, False)
```

</div>

<div class="cell markdown" id="P5veT8qrd-gC">

**Explicación:**

**SELECT** \* selecciona todas las columnas.

**FROM** empleados indica la vista temporal (como una tabla en SQL).

</div>

<div class="cell markdown" id="rJxBSmseeIUK">

#### **Seleccionar columnas específicas**

------------------------------------------------------------------------

</div>

<div class="cell code" id="AaL2nKOPYH5J">

``` python
# Seleccionar solo ciertas columnas
spark.sql("SELECT job_title, salary, salary_currency FROM empleados").show(5, False)
```

</div>

<div class="cell markdown" id="exM7weaqeWK3">

#### **Filtrar filas con WHERE**

------------------------------------------------------------------------

</div>

<div class="cell code" id="xI6aekGxYH79">

``` python
# Mostrar empleados con salario en USD superior a 100000
spark.sql("""SELECT * FROM empleados WHERE salary_in_usd > 100000""").show(5, False)
```

</div>

<div class="cell markdown" id="wXzhsRkqelGf">

**Explicación:**

**WHERE** se usa para filtrar filas que cumplen una condición.

salary_in_usd \> 100000 filtra por salario alto.

</div>

<div class="cell markdown" id="Cznx4ZgNetVy">

#### **Filtro con múltiples condiciones (AND, OR)**

------------------------------------------------------------------------

</div>

<div class="cell code" id="uoyDvWJxYH-f">

``` python
# Mostrar expertos que trabajan 100% remoto
spark.sql("""SELECT *  FROM empleados WHERE experience_level = 'EX' AND remote_ratio = 100""").show(5, False)
```

</div>

<div class="cell markdown" id="yO08GF-je-EH">

**Explicación:**

Puedes usar operadores lógicos como AND y OR.

En este caso, filtras por dos condiciones al mismo tiempo.

</div>

<div class="cell markdown" id="2O-u9FFTfS0n">

#### **Ordenar resultados (ORDER BY)**

------------------------------------------------------------------------

</div>

<div class="cell code" id="n_oqEDf_ax0x">

``` python
# Mostrar salarios ordenados de mayor a menor
spark.sql("""SELECT job_title, salary_in_usd FROM empleados ORDER BY salary_in_usd DESC""").show(5, False)
```

</div>

<div class="cell markdown" id="8JmWdIbRfgrd">

**Explicación:**

**ORDER BY** organiza los resultados.

**DESC** = descendente (de mayor a menor).

</div>

<div class="cell markdown" id="XpZEOpOffgPi">

#### **Limitar resultados (LIMIT)**

------------------------------------------------------------------------

</div>

<div class="cell code" id="nO0NP0esa7k-">

``` python
# Mostrar los 3 trabajos mejor pagados
spark.sql("""SELECT job_title, salary_in_usd FROM empleados ORDER BY salary_in_usd DESC LIMIT 5""").show()
```

</div>

<div class="cell markdown" id="q-wp7wTHgRNI">

**Explicación:**

**LIMIT** restringe el número de filas mostradas.

Muy útil para "Top N" resultados.

</div>

<div class="cell markdown" id="53vxa2IhgUzv">

#### \*\*Contar filas (COUNT(\*))\*\*

------------------------------------------------------------------------

</div>

<div class="cell code" id="App1sBE1a7oJ">

``` python
# Contar cuántos empleados hay en total
spark.sql("""SELECT COUNT(*) AS total_empleados FROM empleados""").show()
```

</div>

<div class="cell markdown" id="ohWNHwFGg2Da">

**Explicación:**

**COUNT**(\*) cuenta todas las filas.

Puedes renombrar el resultado usando AS nombre_columna.

</div>

<div class="cell markdown" id="YDCnlmDZg_Pu">

#### **Agrupar datos (GROUP BY) + funciones de agregación**

------------------------------------------------------------------------

</div>

<div class="cell code" id="iFP51oR7ax3p">

``` python
# Ver el salario promedio por nivel de experiencia
spark.sql("""SELECT experience_level,
            COUNT(*) AS total,
            AVG(salary_in_usd) AS promedio_sueldo,
            MAX(salary_in_usd) AS max_sueldo
            FROM empleados GROUP BY experience_level""").show()
```

</div>

<div class="cell markdown" id="SyMpamwahX6M">

**Explicación:**

**GROUP BY** agrupa las filas por una o más columnas.

Puedes aplicar funciones como **AVG**, **MAX**, **MIN**, **SUM**, **COUNT**.

</div>

<div class="cell markdown" id="sB8d_zxohQ83">

#### **Filtro después de agrupar (HAVING)**

------------------------------------------------------------------------

</div>

<div class="cell code" id="lw4L2u3eax6n">

``` python
# Mostrar países con salario promedio mayor a 100000
spark.sql("""SELECT company_location,
          AVG(salary_in_usd) AS salario_promedio
          FROM empleados
          GROUP BY company_location
          HAVING salario_promedio > 100000""").show()
```

</div>

<div class="cell markdown" id="fnRG4KL5hnLK">

**Explicación:**

**HAVING** se usa después de GROUP BY, para filtrar los grupos.

Es como **WHERE**, pero para agregaciones.

</div>

<div class="cell markdown" id="dmZz-Ygdhve6">

#### **Crear columna calculada con CASE WHEN**

------------------------------------------------------------------------

</div>

<div class="cell code" id="0q6cM_RTax9b">

``` python
spark.sql("""SELECT job_title,
           salary_in_usd,
           CASE
               WHEN salary_in_usd >= 150000 THEN 'Alto'
               WHEN salary_in_usd >= 70000 THEN 'Medio'
               ELSE 'Bajo'
           END AS categoria_salarial
    FROM empleados""").show()
```

</div>

<div class="cell markdown" id="DFyLxyr9h9Je">

**Explicación:**

**CASE WHEN** es como una estructura if-else para SQL.

Se usa para crear columnas condicionales o etiquetas.

</div>

<div class="cell markdown" id="BYVY-U2niDqk">

#### **Concatenar columnas (CONCAT)**

------------------------------------------------------------------------

</div>

<div class="cell code" id="ZOyXNJrIYIC5">

``` python
# Unir el cargo con el país en una sola columna
spark.sql("""SELECT
        CONCAT(job_title, ' (', company_location, ')') AS descripcion,
        salary_in_usd
    FROM empleados""").show(truncate=False)
```

</div>

<div class="cell markdown" id="ST_gmbYNi7-b">

**Explicación:**

CONCAT une múltiples cadenas o columnas.

Ideal para generar descripciones personalizadas.

</div>

<div class="cell markdown" id="oe8uAWDgia7g">

#### **Subconsulta en WHERE**

------------------------------------------------------------------------

</div>

<div class="cell code" id="s3iJi-8Ob884">

``` python
# Mostrar empleados que ganan más que el salario promedio
spark.sql("""SELECT *
    FROM empleados
    WHERE salary_in_usd > (
        SELECT AVG(salary_in_usd) FROM empleados)""").show(5)
```

</div>

<div class="cell markdown" id="gaEkFzuGimmE">

**Explicación:**

Puedes usar subconsultas dentro de WHERE para hacer comparaciones dinámicas.

En este caso, solo muestra los que ganan más que el promedio global.

</div>

<div class="cell markdown" id="3_y_2DA7im-I">

**Agrupación jerárquica con ROLLUP**

------------------------------------------------------------------------

</div>

<div class="cell code" id="w6kNdI6cb8_q">

``` python
# Agrupar por país y experiencia, con subtotales y totales
spark.sql("""SELECT company_location, experience_level,
           AVG(salary_in_usd) AS salario_promedio
    FROM empleados
    GROUP BY ROLLUP(company_location, experience_level)""").show(5)
```

</div>

<div class="cell markdown" id="Sa8w_uNMjDAr">

**Explicación:**

**ROLLUP** genera subtotales y totales jerárquicos.

Muy útil para reportes.

</div>

<div class="cell markdown" id="R1jIO-bfjDGl">

**Ranking con funciones de ventana (RANK())**

------------------------------------------------------------------------

</div>

<div class="cell code" id="Joog2P75b9DU">

``` python
# Ver ranking de salario por país
spark.sql("""SELECT
        job_title,
        employee_residence,
        salary_in_usd,
        RANK() OVER (
            PARTITION BY employee_residence
            ORDER BY salary_in_usd DESC
        ) AS ranking
    FROM empleados""").show()
```

</div>

<div class="cell markdown" id="67mGLZOzjTIR">

**Explicación:**

**RANK**() es una función de ventana que asigna un número de orden.

**PARTITION** BY agrupa por país y ordena dentro del grupo.

</div>

<div class="cell markdown" id="52LGSQy2Ksna">

**Subconsulta con WITH**

------------------------------------------------------------------------

</div>

<div class="cell code" id="RAi9otVGKsyM">

``` python
# Mostrar empleados cuyo salario esté por encima del promedio de su país
spark.sql("""
    WITH promedio_pais AS (
        SELECT employee_residence, AVG(salary_in_usd) AS salario_promedio
        FROM empleados
        GROUP BY employee_residence
    )

    SELECT e.*, p.salario_promedio
    FROM empleados e
    JOIN promedio_pais p
    ON e.employee_residence = p.employee_residence
    WHERE e.salary_in_usd > p.salario_promedio
""").show()
```

</div>

<div class="cell markdown" id="6GqxHg9dPmpV">

**Explicación:**

**WITH** permite definir subconsultas reutilizables.

Útil para dividir lógica compleja en partes legibles.

</div>

<div class="cell markdown" id="VF41Vk0RONJo">

#### **JOIN entre dos vistas**

</div>

<div class="cell code" id="mWbm_iLcK6Vb">

``` python
# Tabla de impuestos por país
df_impuestos = spark.createDataFrame([
    ("US", 0.30),
    ("CA", 0.25),
    ("DE", 0.35),
    ("NG", 0.10),
    ("MU", 0.20)
], ["pais", "tasa_impuesto"])

df_impuestos.createOrReplaceTempView("impuestos")

# Calcular salario neto luego de impuesto
spark.sql("""SELECT
        e.job_title,
        e.company_location,
        e.salary_in_usd,
        i.tasa_impuesto,
        e.salary_in_usd * (1 - i.tasa_impuesto) AS salario_neto
    FROM empleados e
    JOIN impuestos i ON e.company_location = i.pais""").show()
```

</div>

<div class="cell markdown" id="gLL8QUa1OTSo">

**Explicación:**

**JOIN** une datos de dos vistas o tablas.

Se puede hacer INNER, LEFT, RIGHT, etc.

</div>

<div class="cell markdown" id="7i6EAiW4OYU8">

#### **Ranking por grupo con ROW_NUMBER()**

</div>

<div class="cell code" id="oZMCIAv1K6YZ">

``` python
# Obtener el empleado mejor pagado por nivel de experiencia
spark.sql("""SELECT *
    FROM (SELECT *, ROW_NUMBER() OVER (
                   PARTITION BY experience_level
                   ORDER BY salary_in_usd DESC
               ) AS fila
        FROM empleados
    ) WHERE fila = 1""").show()
```

</div>

<div class="cell markdown" id="HNJlsotUOeUO">

**Explicación:**

**ROW_NUMBER()** asigna un número de fila dentro de cada grupo.

**PARTITION BY** define el grupo (por ejemplo, por experiencia).

Solo se conservan los primeros de cada grupo.

</div>

<div class="cell markdown" id="VseXt8PUOjma">

#### **Ventanas móviles (MOVING AVERAGE)**

</div>

<div class="cell code" id="7J4tHSG8K6bD">

``` python
# Calcular promedio móvil de salario en cada país
spark.sql("""SELECT job_title, company_location, salary_in_usd,
        AVG(salary_in_usd) OVER (
            PARTITION BY company_location
            ORDER BY salary_in_usd
            ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
        ) AS promedio_movil
    FROM empleados""").show()
```

</div>

<div class="cell markdown" id="7gaalhIPOop8">

**Explicación:**

Las funciones de ventana permiten cálculos fila por fila.

**ROWS BETWEEN** define cuántas filas anteriores y siguientes incluir.

</div>

<div class="cell markdown" id="g0NZvvcsOvcy">

#### **Crear una columna categórica compleja (CASE anidado)**

</div>

<div class="cell code" id="n9N90gVeK6it">

``` python
# Clasificar salarios y experiencia en etiquetas combinadas
spark.sql("""SELECT *,CASE
               WHEN salary_in_usd > 200000 AND experience_level = 'EX' THEN 'Experto muy bien pagado'
               WHEN salary_in_usd > 100000 THEN 'Buen salario'
               WHEN salary_in_usd BETWEEN 50000 AND 100000 THEN 'Promedio'
               ELSE 'Bajo salario'
           END AS clasificacion FROM empleados""").show()
```

</div>

<div class="cell markdown" id="xIcg25saO4n7">

**Explicación:**

**CASE WHEN** se puede anidar para clasificar condiciones más detalladas.

Muy útil para análisis exploratorio.

</div>

<div class="cell markdown" id="sOAMzidVPCHf">

#### **Concatenación y formato de columnas**

</div>

<div class="cell code" id="McSn2x2uNLgk">

``` python
# Formatear una descripción del empleado
spark.sql(""" SELECT  CONCAT('Rol: ', job_title, ' | País: ', employee_residence, ' | Salario USD: ', CAST(salary_in_usd AS STRING)) AS descripcion
          FROM empleados""").show(truncate=False)
```

</div>

<div class="cell markdown" id="2dTfow9qPF5J">

**Explicación:**

**CONCAT** une columnas y textos.

**CAST(... AS STRING)** convierte números para que puedan concatenarse.

</div>
