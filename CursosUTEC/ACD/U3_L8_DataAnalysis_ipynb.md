---
curso: ACD
titulo: U3_L8 DataAnalysis
slides: 0
fuente: U3_L8 DataAnalysis.ipynb
---

<div class="cell markdown" id="Op8OQbp172hy">

# **U3_L8 Data Analysis**

## **Objetivo:**

Al finalizar el laboratorio, el estudiante será capaz de poner en práctica las técnicas computacionales de preprocesamiento a casos reales.

</div>

<div class="cell code" execution_count="1" executionInfo="{&quot;elapsed&quot;:4189,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719419768130,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="UarMepXQ7fh7">

``` python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

</div>

<div class="cell markdown" id="w64-UXOm8fwX">

## **MovieLens 1M Dataset**

[GroupLens Research](https://grouplens.org/datasets/movielens/) proporciona una serie de colecciones de datos de clasificación de películas recopilados de usuarios de MovieLens a finales de los años 1990 y principios de los 2000. Los datos proporcionan clasificaciones de películas, metadatos de películas (géneros y año) y datos demográficos sobre los usuarios (edad, código postal, género y ocupación). Estos datos suelen ser de interés en el desarrollo de sistemas de recomendación basados ​​en algoritmos de Machine Learning.

</div>

<div class="cell markdown" id="NMsm1kJq9F9l">

El conjunto de datos MovieLens 1M contiene un millón de calificaciones recopiladas de **seis mil usuarios en cuatro mil películas**. Se distribuye en 3 tablas: *users*, *movies* y *ratings*.

</div>

<div class="cell markdown" id="WFotyDbGZ8Mw">

### **Ejercicio 1:**

Carguemos los datos y observemos con cuidado los atributos de cada dataset.

</div>

<div class="cell code" execution_count="2" id="-ec-GlhCYd5i">

``` python
unames = ["user_id", "gender", "age", "occupation", "zip"]
users = pd.read_table("users.dat", sep="::", header=None, names=unames, engine="python")

rnames = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("ratings.dat", sep="::", header=None, names=rnames, engine="python")

mnames = ["movie_id", "title", "genres"]
movies = pd.read_table("movies.dat", sep="::", header=None, names=mnames, engine="python", encoding="ISO-8859-1")
```

</div>

<div class="cell code" execution_count="3" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:352,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719167912587,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="PEQQgBIvZHBW" outputId="e22acca5-2165-400c-a7ec-c121c90107d1">

``` python
users.head()
```

<div class="output execute_result" execution_count="3">

       user_id gender  age  occupation    zip
    0        1      F    1          10  48067
    1        2      M   56          16  70072
    2        3      M   25          15  55117
    3        4      M   45           7  02460
    4        5      M   25          20  55455

</div>

</div>

<div class="cell code" execution_count="4" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:357,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719168239339,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="R1Qt3f5taV5l" outputId="d92678ea-b7d7-46cd-b6e2-9281a774554d">

``` python
users.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6040 entries, 0 to 6039
    Data columns (total 5 columns):
     #   Column      Non-Null Count  Dtype 
    ---  ------      --------------  ----- 
     0   user_id     6040 non-null   int64 
     1   gender      6040 non-null   object
     2   age         6040 non-null   int64 
     3   occupation  6040 non-null   int64 
     4   zip         6040 non-null   object
    dtypes: int64(3), object(2)
    memory usage: 236.1+ KB

</div>

</div>

<div class="cell code" execution_count="5" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:343,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719167939343,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="kmkRTzofZLaF" outputId="3ffbd1e8-8151-48e6-a73a-e0af7fa1ed94">

``` python
ratings.head()
```

<div class="output execute_result" execution_count="5">

       user_id  movie_id  rating  timestamp
    0        1      1193       5  978300760
    1        1       661       3  978302109
    2        1       914       3  978301968
    3        1      3408       4  978300275
    4        1      2355       5  978824291

</div>

</div>

<div class="cell code" execution_count="6" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:316,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719168283298,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="eDtz6OGBahIE" outputId="4774b429-e8c7-42f7-d103-e1d63301a467">

``` python
ratings.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 1000209 entries, 0 to 1000208
    Data columns (total 4 columns):
     #   Column     Non-Null Count    Dtype
    ---  ------     --------------    -----
     0   user_id    1000209 non-null  int64
     1   movie_id   1000209 non-null  int64
     2   rating     1000209 non-null  int64
     3   timestamp  1000209 non-null  int64
    dtypes: int64(4)
    memory usage: 30.5 MB

</div>

</div>

<div class="cell code" execution_count="7" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" executionInfo="{&quot;elapsed&quot;:318,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719167953705,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="S4FvH7O3ZPxh" outputId="6c85cbe1-66b9-4420-8a05-c40158dc121d">

``` python
movies.head()
```

<div class="output execute_result" execution_count="7">

       movie_id                               title                        genres
    0         1                    Toy Story (1995)   Animation|Children's|Comedy
    1         2                      Jumanji (1995)  Adventure|Children's|Fantasy
    2         3             Grumpier Old Men (1995)                Comedy|Romance
    3         4            Waiting to Exhale (1995)                  Comedy|Drama
    4         5  Father of the Bride Part II (1995)                        Comedy

</div>

</div>

<div class="cell code" execution_count="8" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:346,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719168299215,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="FS1J34A5alD3" outputId="fc4e8980-48c9-4dbe-fc0b-e1845dfde4af">

``` python
movies.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3883 entries, 0 to 3882
    Data columns (total 3 columns):
     #   Column    Non-Null Count  Dtype 
    ---  ------    --------------  ----- 
     0   movie_id  3883 non-null   int64 
     1   title     3883 non-null   object
     2   genres    3883 non-null   object
    dtypes: int64(1), object(2)
    memory usage: 91.1+ KB

</div>

</div>

<div class="cell markdown" id="8gSChabqaqbW">

### **Ejercicio 2:**

Calcule el rating promedio de cada pelicula en base al genéro del usuario.

</div>

<div class="cell code" execution_count="9" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:528}" executionInfo="{&quot;elapsed&quot;:747,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719168751954,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="cCVsDy6fbUd_" outputId="910869bb-4971-4837-e915-623daca37e1e">

``` python
#mezclamos las tres tablas en 1
data = pd.merge(pd.merge(ratings, users), movies)
data
```

<div class="output execute_result" execution_count="9">

             user_id  movie_id  rating  timestamp gender  age  occupation    zip  \
    0              1      1193       5  978300760      F    1          10  48067   
    1              1       661       3  978302109      F    1          10  48067   
    2              1       914       3  978301968      F    1          10  48067   
    3              1      3408       4  978300275      F    1          10  48067   
    4              1      2355       5  978824291      F    1          10  48067   
    ...          ...       ...     ...        ...    ...  ...         ...    ...   
    1000204     6040      1091       1  956716541      M   25           6  11106   
    1000205     6040      1094       5  956704887      M   25           6  11106   
    1000206     6040       562       5  956704746      M   25           6  11106   
    1000207     6040      1096       4  956715648      M   25           6  11106   
    1000208     6040      1097       4  956715569      M   25           6  11106   

                                              title  \
    0        One Flew Over the Cuckoo's Nest (1975)   
    1              James and the Giant Peach (1996)   
    2                           My Fair Lady (1964)   
    3                        Erin Brockovich (2000)   
    4                          Bug's Life, A (1998)   
    ...                                         ...   
    1000204              Weekend at Bernie's (1989)   
    1000205                 Crying Game, The (1992)   
    1000206         Welcome to the Dollhouse (1995)   
    1000207                  Sophie's Choice (1982)   
    1000208       E.T. the Extra-Terrestrial (1982)   

                                      genres  
    0                                  Drama  
    1           Animation|Children's|Musical  
    2                        Musical|Romance  
    3                                  Drama  
    4            Animation|Children's|Comedy  
    ...                                  ...  
    1000204                           Comedy  
    1000205                Drama|Romance|War  
    1000206                     Comedy|Drama  
    1000207                            Drama  
    1000208  Children's|Drama|Fantasy|Sci-Fi  

    [1000209 rows x 10 columns]

</div>

</div>

<div class="cell code" execution_count="10" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:455}" executionInfo="{&quot;elapsed&quot;:320,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719169751794,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="NTwjstzCcfxh" outputId="8ed75f06-963f-436e-e347-53bec53cbb73">

``` python
#para conseguir el rating promedio usamos pivot_table
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
mean_ratings
```

<div class="output execute_result" execution_count="10">

    gender                                             F         M
    title                                                         
    $1,000,000 Duck (1971)                      3.375000  2.761905
    'Night Mother (1986)                        3.388889  3.352941
    'Til There Was You (1997)                   2.675676  2.733333
    'burbs, The (1989)                          2.793478  2.962085
    ...And Justice for All (1979)               3.828571  3.689024
    ...                                              ...       ...
    Zed & Two Noughts, A (1985)                 3.500000  3.380952
    Zero Effect (1998)                          3.864407  3.723140
    Zero Kelvin (Kjærlighetens kjøtere) (1995)       NaN  3.500000
    Zeus and Roxanne (1997)                     2.777778  2.357143
    eXistenZ (1999)                             3.098592  3.289086

    [3706 rows x 2 columns]

</div>

</div>

<div class="cell markdown" id="k8cxaqXMfrYh">

### **Ejercicio 3:**

¿Cuáles son las top 5 peliculas del género femenino? Considere que para una pelicula este en el top como mínimo ha recibido 250 ratings.

Hints. Puede usar el dataframe del ejercicio anterior.

</div>

<div class="cell code" execution_count="11" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:309,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719170926216,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="fxMrOHhckQsY" outputId="d805b8f0-8c63-4e4e-8f13-0072e67070b0">

``` python
#agrupo la data en base a la pelicula
ratings_by_title = data.groupby("title").size()
ratings_by_title
```

<div class="output execute_result" execution_count="11">

    title
    $1,000,000 Duck (1971)                         37
    'Night Mother (1986)                           70
    'Til There Was You (1997)                      52
    'burbs, The (1989)                            303
    ...And Justice for All (1979)                 199
                                                 ... 
    Zed & Two Noughts, A (1985)                    29
    Zero Effect (1998)                            301
    Zero Kelvin (Kjærlighetens kjøtere) (1995)      2
    Zeus and Roxanne (1997)                        23
    eXistenZ (1999)                               410
    Length: 3706, dtype: int64

</div>

</div>

<div class="cell code" execution_count="12" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:396,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719171348083,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="r3RE_CnMmLCX" outputId="1758d62b-2777-49e8-e176-6ff16f748ccc">

``` python
#filtro > 250
tmp_df = ratings_by_title[ratings_by_title >= 250]
tmp_df
```

<div class="output execute_result" execution_count="12">

    title
    'burbs, The (1989)                   303
    10 Things I Hate About You (1999)    700
    101 Dalmatians (1961)                565
    101 Dalmatians (1996)                364
    12 Angry Men (1957)                  616
                                        ... 
    Young Guns (1988)                    562
    Young Guns II (1990)                 369
    Young Sherlock Holmes (1985)         379
    Zero Effect (1998)                   301
    eXistenZ (1999)                      410
    Length: 1216, dtype: int64

</div>

</div>

<div class="cell code" execution_count="13" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:455}" executionInfo="{&quot;elapsed&quot;:307,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719171473691,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="JskuYMmhmgeu" outputId="832d453a-087c-4dbb-df55-4b6dea521fef">

``` python
#filtro mean_ratings en base a index de tmp_df
mean_ratings = mean_ratings.loc[tmp_df.index]
mean_ratings
```

<div class="output execute_result" execution_count="13">

    gender                                    F         M
    title                                                
    'burbs, The (1989)                 2.793478  2.962085
    10 Things I Hate About You (1999)  3.646552  3.311966
    101 Dalmatians (1961)              3.791444  3.500000
    101 Dalmatians (1996)              3.240000  2.911215
    12 Angry Men (1957)                4.184397  4.328421
    ...                                     ...       ...
    Young Guns (1988)                  3.371795  3.425620
    Young Guns II (1990)               2.934783  2.904025
    Young Sherlock Holmes (1985)       3.514706  3.363344
    Zero Effect (1998)                 3.864407  3.723140
    eXistenZ (1999)                    3.098592  3.289086

    [1216 rows x 2 columns]

</div>

</div>

<div class="cell code" execution_count="14" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:336,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719171503978,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="lJAml7Jlmwd_" outputId="fd9af0b9-1c0e-41d5-b848-6493333d21f5">

``` python
#ordeno F
mean_ratings['F'].sort_values(ascending=False)[:5]
```

<div class="output execute_result" execution_count="14">

    title
    Close Shave, A (1995)                                     4.644444
    Wrong Trousers, The (1993)                                4.588235
    Sunset Blvd. (a.k.a. Sunset Boulevard) (1950)             4.572650
    Wallace & Gromit: The Best of Aardman Animation (1996)    4.563107
    Schindler's List (1993)                                   4.562602
    Name: F, dtype: float64

</div>

</div>

<div class="cell markdown" id="d3yjTKlXnAj2">

### **Ejercicio 4:**

Con base a sus cálculos del ejercicio anterior, ¿cuáles son las películas que generan más división entre los espectadores masculinos y femeninos?

</div>

<div class="cell code" execution_count="15" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" executionInfo="{&quot;elapsed&quot;:325,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719171706908,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="s9rfIdrXnkwk" outputId="d5177fb3-e27a-4100-f823-e38b37941d62">

``` python
mean_ratings.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    Index: 1216 entries, 'burbs, The (1989) to eXistenZ (1999)
    Data columns (total 2 columns):
     #   Column  Non-Null Count  Dtype  
    ---  ------  --------------  -----  
     0   F       1216 non-null   float64
     1   M       1216 non-null   float64
    dtypes: float64(2)
    memory usage: 28.5+ KB

</div>

</div>

<div class="cell code" execution_count="16" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:455}" executionInfo="{&quot;elapsed&quot;:326,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719171773533,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="--A_XSaWntKE" outputId="1ddab516-3480-4b94-9a93-d45f4582e664">

``` python
mean_ratings["diff"] = mean_ratings["M"] - mean_ratings["F"]
mean_ratings
```

<div class="output execute_result" execution_count="16">

    gender                                    F         M      diff
    title                                                          
    'burbs, The (1989)                 2.793478  2.962085  0.168607
    10 Things I Hate About You (1999)  3.646552  3.311966 -0.334586
    101 Dalmatians (1961)              3.791444  3.500000 -0.291444
    101 Dalmatians (1996)              3.240000  2.911215 -0.328785
    12 Angry Men (1957)                4.184397  4.328421  0.144024
    ...                                     ...       ...       ...
    Young Guns (1988)                  3.371795  3.425620  0.053825
    Young Guns II (1990)               2.934783  2.904025 -0.030758
    Young Sherlock Holmes (1985)       3.514706  3.363344 -0.151362
    Zero Effect (1998)                 3.864407  3.723140 -0.141266
    eXistenZ (1999)                    3.098592  3.289086  0.190494

    [1216 rows x 3 columns]

</div>

</div>

<div class="cell code" execution_count="17" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:455}" executionInfo="{&quot;elapsed&quot;:303,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719171830678,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="6mnkGO9Qn-xo" outputId="93e5faca-efba-411e-8325-c6c091498ef1">

``` python
#Ordenar diff
sorted_by_diff = mean_ratings.sort_values(by="diff")
sorted_by_diff
```

<div class="output execute_result" execution_count="17">

    gender                                         F         M      diff
    title                                                               
    Dirty Dancing (1987)                    3.790378  2.959596 -0.830782
    Jumpin' Jack Flash (1986)               3.254717  2.578358 -0.676359
    Grease (1978)                           3.975265  3.367041 -0.608224
    Little Women (1994)                     3.870588  3.321739 -0.548849
    Steel Magnolias (1989)                  3.901734  3.365957 -0.535777
    ...                                          ...       ...       ...
    Cable Guy, The (1996)                   2.250000  2.863787  0.613787
    Longest Day, The (1962)                 3.411765  4.031447  0.619682
    Dumb & Dumber (1994)                    2.697987  3.336595  0.638608
    Kentucky Fried Movie, The (1977)        2.878788  3.555147  0.676359
    Good, The Bad and The Ugly, The (1966)  3.494949  4.221300  0.726351

    [1216 rows x 3 columns]

</div>

</div>

<div class="cell code" execution_count="18" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:238}" executionInfo="{&quot;elapsed&quot;:308,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719171921395,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="Pq-BfgsWoURf" outputId="219cc681-e53e-4065-e7f3-9eea662871e8">

``` python
#las que prefieren los hombres
sorted_by_diff[::-1].head()
```

<div class="output execute_result" execution_count="18">

    gender                                         F         M      diff
    title                                                               
    Good, The Bad and The Ugly, The (1966)  3.494949  4.221300  0.726351
    Kentucky Fried Movie, The (1977)        2.878788  3.555147  0.676359
    Dumb & Dumber (1994)                    2.697987  3.336595  0.638608
    Longest Day, The (1962)                 3.411765  4.031447  0.619682
    Cable Guy, The (1996)                   2.250000  2.863787  0.613787

</div>

</div>

<div class="cell code">

``` python
```

</div>

<div class="cell code">

``` python
```

</div>

<div class="cell code" execution_count="19" executionInfo="{&quot;elapsed&quot;:324,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719419786737,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="wF6yYv7lpinY">

``` python
#Librerias para acceder a Google Drive
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
```

<div class="output error" ename="ModuleNotFoundError" evalue="No module named 'pydrive2'">

    ---------------------------------------------------------------------------
    ModuleNotFoundError                       Traceback (most recent call last)
    Cell In[19], line 2
          1 #Librerias para acceder a Google Drive
    ----> 2 from pydrive2.auth import GoogleAuth
          3 from pydrive2.drive import GoogleDrive
          4 from google.colab import auth

    ModuleNotFoundError: No module named 'pydrive2'

</div>

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:15434,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719419803911,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="hj92BRqK_r0Z">

``` python
#Autenticación
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
```

</div>

<div class="cell markdown" id="7xfZ9iL5LRmZ">

### **Ejercicio 1:**

Compilar todos los archivos en un solo DataFrame que tenga como atributos:

- **name**: nombre del bebé
- **sex**: femenino o masculino
- **number**: número de ocurrencia del nombre
- **year**: año al que corresponde

</div>

<div class="cell code" executionInfo="{&quot;elapsed&quot;:1773,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719419808313,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="IWKeNDLo_7EA">

``` python
#Get Lista de Documentos
fileList = drive.ListFile({'q': "'1E6EDoWXq10LEIjbTwEo6DHPaM34x9pmq' in parents and trashed=false"}).GetList()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:424}" executionInfo="{&quot;elapsed&quot;:154151,&quot;status&quot;:&quot;ok&quot;,&quot;timestamp&quot;:1719419964204,&quot;user&quot;:{&quot;displayName&quot;:&quot;Yamilet Serrano LL&quot;,&quot;userId&quot;:&quot;02422272653784538191&quot;},&quot;user_tz&quot;:300}" id="mLEu_BD5JUs-" outputId="622ce17e-3725-4a51-919d-a724708efc2e">

``` python
dfList = []

for file in fileList:

  #Extraer título y id
  file_name = file['title']
  file_id = file['id']

  #Descargar el contenido
  fileDownloaded = drive.CreateFile({'id':file_id})
  fileDownloaded.GetContentFile(file_name)

  #Convertir a dataframe
  df = pd.read_csv(file_name, names=["name", "sex", "number"])

  #extraer el año
  df['year'] = file_name.split('.')[0][3:]

  #agregar a la lista de dataframes
  dfList.append(df)

#Concatenar todos los dataframes
names = pd.concat(dfList, ignore_index=True)
names
```

</div>
