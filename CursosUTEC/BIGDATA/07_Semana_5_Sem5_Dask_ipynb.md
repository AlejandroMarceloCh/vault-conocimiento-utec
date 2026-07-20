---
curso: BIGDATA
titulo: 07 - Semana 5/Sem5_Dask
slides: 0
fuente: 07 - Semana 5/Sem5_Dask.ipynb
---

<div id="02fec7cd-496c-474e-a67b-23a9e2c5b430" class="cell code" execution_count="1" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:24:45.454826Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:24:45.454587Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:24:45.538095Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:24:45.537483Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:24:45.454809Z&quot;}" tags="[]">

``` python
import pandas as pd
import dask
import numpy as np
import time
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

</div>

<div id="e6cf57a4-5a60-4410-a977-bf32758e3695" class="cell code" execution_count="2" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:24:45.776829Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:24:45.776369Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:24:45.786785Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:24:45.785592Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:24:45.776805Z&quot;}" tags="[]">

``` python
print(dask.__version__)
print(pd.__version__)
print(np.__version__)
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output stream stdout">

    2026.3.0
    2.3.3
    1.26.4

</div>

</div>

<div id="3a63bc03-3c79-44f8-829a-c27150145630" class="cell code" tags="[]">

``` python
#!pip install "dask[dataframe]" --upgrade
```

</div>

<div id="92da9237-8ddc-43e0-957b-d888f3b17d9e" class="cell code" execution_count="3" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:24:48.891531Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:24:48.891013Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:24:49.187366Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:24:49.185991Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:24:48.891500Z&quot;}" tags="[]">

``` python
import dask.dataframe as dd
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

</div>

<div id="e38c7502-6fe7-46dc-b608-04d814b34b39" class="cell code" execution_count="4" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:24:49.341228Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:24:49.340642Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:24:49.349408Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:24:49.348629Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:24:49.341199Z&quot;}" tags="[]">

``` python
#!pip install "modin[all]"
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

</div>

<div id="2663df2a-87e2-464e-8a9f-1639374608b7" class="cell code" execution_count="5" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:24:50.732233Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:24:50.731992Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:24:50.742370Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:24:50.741644Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:24:50.732216Z&quot;}" tags="[]">

``` python
import modin
print(modin.__version__)
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output stream stdout">

    0.37.1

</div>

</div>

<div id="75df3014-53b1-4f49-955b-d0ec577d2cf5" class="cell code" execution_count="6" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:24:51.580802Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:24:51.580540Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:24:51.584356Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:24:51.583788Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:24:51.580777Z&quot;}" tags="[]">

``` python
#import modin.pandas as mdf
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

</div>

<div id="a91bdce8-5fcb-485d-87fa-835fed7c4151" class="cell code" execution_count="7" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:24:52.667941Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:24:52.667677Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:24:55.335410Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:24:55.334508Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:24:52.667919Z&quot;}" tags="[]">

``` python
inicio = time.time()
df_dask = dd.read_parquet("gs://bucket-utec-2026-v7/data/spotify_parquet/",engine='pyarrow',ignore_metadata_file=True)
fin = time.time()
print("Tiempo Dask",fin-inicio)
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output stream stdout">

    Tiempo Dask 2.6588964462280273

</div>

</div>

<div id="b0e39fce-5761-432d-90eb-ab57d9c65538" class="cell code" execution_count="8" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:24:55.337567Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:24:55.337181Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:25:12.923112Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:25:12.921990Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:24:55.337545Z&quot;}" tags="[]">

``` python
inicio = time.time()
df_pd=pd.read_parquet("gs://bucket-utec-2026-v7/data/spotify_parquet/",engine='pyarrow')
fin = time.time()
print("Tiempo Pandas",fin-inicio)
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output stream stdout">

    Tiempo Pandas 17.576823711395264

</div>

</div>

<div id="8999b563-3af6-4db0-8cf4-c7b6735b6e2a" class="cell code" execution_count="9" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:25:12.924971Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:25:12.924713Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:25:27.847573Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:25:27.846775Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:25:12.924952Z&quot;}" tags="[]">

``` python
result_p2=df_dask.nlargest(n=2,columns='popularity')
result_p2.compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="9">

                               id             name  popularity  duration_ms  \
    2257   5QO79kh1waicV47BqGRL3g  Save Your Tears          97       215627   
    11698  6tDDoYIxWvMLTdKpjFkc1B        telepatía          97       160191   

           explicit         artists              release_date  danceability key  \
    2257          1  ['The Weeknd'] 2020-03-20 00:00:00+00:00         0.680   C   
    11698         0  ['Kali Uchis'] 2020-12-04 00:00:00+00:00         0.653   B   

           acousticness  instrumentalness    tempo  
    2257         0.0212          0.000012  118.051  
    11698        0.1120          0.000000   83.970  

</div>

</div>

<div id="caeb0ff6-c8fb-4e44-ad67-79b7b1717c45" class="cell code" execution_count="10" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:25:27.850878Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:25:27.850520Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:25:42.906054Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:25:42.905288Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:25:27.850858Z&quot;}" tags="[]">

``` python
df_dask["artist"]=df_dask["artists"].str.strip("[]").str.replace("'","")
result_p3=df_dask[df_dask['artist'].str.contains("Bad Bunny")]
result_p3.compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="10">

                               id  \
    6116   6C1RD7YQVvt3YQj0CmuTeu   
    7107   6NSMQFKgjpQb0KkjMDYIK0   
    8572   3LgtCt7CVhMvNSMGoQD9i1   
    8947   01vHGJRvJ6EZW9KO8NtZpi   
    9782   1JxhrUWZjuI8AOjDJ1JpMN   
    ...                       ...   
    11234  23XjN1s3DZC8Q9ZwuorYY4   
    11238  2XIc1pqjXV3Cr2BQUGNBck   
    11241  4MzXwWMhyBbmu6hOcLVD49   
    11253  5RubKOuDoPn5Kj5TLVxSxY   
    11306  0tjZv2hChdHZCW1zFXpy1J   

                                                        name  popularity  \
    6116                                               Diles          76   
    7107       Tu No Vive Asi (feat. Mambo Kingz & DJ Luian)          72   
    8572                                           Me Llamas          55   
    8947   Un Polvo (feat. Bad Bunny, Arcángel, Ñengo Flo...          62   
    9782                                            Soy Peor          74   
    ...                                                  ...         ...   
    11234                                  TE DESEO LO MEJOR          76   
    11238                                 LA NOCHE DE ANOCHE          93   
    11241                                             DÁKITI          90   
    11253                                         TE MUDASTE          88   
    11306                                          HOY COBRÉ          77   

           duration_ms  explicit  \
    6116        286041         1   
    7107        264000         1   
    8572        328000         1   
    8947        306373         1   
    9782        257384         1   
    ...            ...       ...   
    11234       139576         1   
    11238       203201         0   
    11241       205090         1   
    11253       130014         1   
    11306       162151         1   

                                                     artists  \
    6116   ['Bad Bunny', 'Ozuna', 'Farruko', 'Arcangel', ...   
    7107   ['Arcangel', 'Bad Bunny', 'Mambo Kingz', 'DJ L...   
    8572   ['Arcangel', 'Mark B.', 'De La Ghetto', 'Bad B...   
    8947   ['Maluma', 'Bad Bunny', 'Arcangel', 'Ñengo Flo...   
    9782                                       ['Bad Bunny']   
    ...                                                  ...   
    11234                                      ['Bad Bunny']   
    11238                           ['Bad Bunny', 'ROSALÍA']   
    11241                       ['Bad Bunny', 'Jhay Cortez']   
    11253                                      ['Bad Bunny']   
    11306                                      ['Bad Bunny']   

                       release_date  danceability key  acousticness  \
    6116  2016-08-26 00:00:00+00:00         0.813   D        0.1080   
    7107  2016-09-30 00:00:00+00:00         0.815  F#        0.5400   
    8572  2016-11-09 00:00:00+00:00         0.799   D        0.2590   
    8947  2016-11-16 00:00:00+00:00         0.811  F#        0.6730   
    9782  2016-12-08 00:00:00+00:00         0.808   C        0.6830   
    ...                         ...           ...  ..           ...   
    11234 2020-11-27 00:00:00+00:00         0.763  C#        0.1580   
    11238 2020-11-27 00:00:00+00:00         0.856   G        0.0303   
    11241 2020-11-27 00:00:00+00:00         0.731   E        0.4010   
    11253 2020-11-27 00:00:00+00:00         0.811  A#        0.2340   
    11306 2020-11-27 00:00:00+00:00         0.860   B        0.0464   

           instrumentalness    tempo  \
    6116           0.000000  118.033   
    7107           0.000000  120.054   
    8572           0.000000  120.060   
    8947           0.000000  134.062   
    9782           0.006380  116.011   
    ...                 ...      ...   
    11234          0.000018  126.054   
    11238          0.000000   81.993   
    11241          0.000052  109.928   
    11253          0.000572   92.025   
    11306          0.000091  145.001   

                                                      artist  
    6116   Bad Bunny, Ozuna, Farruko, Arcangel, Ñengo Flo...  
    7107          Arcangel, Bad Bunny, Mambo Kingz, DJ Luian  
    8572   Arcangel, Mark B., De La Ghetto, Bad Bunny, Am...  
    8947   Maluma, Bad Bunny, Arcangel, Ñengo Flow, De La...  
    9782                                           Bad Bunny  
    ...                                                  ...  
    11234                                          Bad Bunny  
    11238                                 Bad Bunny, ROSALÍA  
    11241                             Bad Bunny, Jhay Cortez  
    11253                                          Bad Bunny  
    11306                                          Bad Bunny  

    [154 rows x 13 columns]

</div>

</div>

<div id="82709a3a-160a-471e-b5bb-a5f760e1936d" class="cell code" execution_count="11" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:25:42.908006Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:25:42.907529Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:25:58.033403Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:25:58.032345Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:25:42.907976Z&quot;}" tags="[]">

``` python
result_p4=df_dask[df_dask['popularity'].between(50,60)]
result_p4.compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="11">

                               id                            name  popularity  \
    7      6MoyiRPmFwVnkhaZhkyksG             Pickin' Wildflowers          52   
    28     70SEB2Lmmkpo5oRtyHksrY          You're the Inspiration          54   
    29     1uybEGNH2GIvNdzGB7L2Qj  (I Wanna Take) Forever Tonight          58   
    153    4dcUque6026WExzwJYWG7H                   The Suffering          56   
    158    2tUhCTpGeEfssyYTeu0chm                         Wake Up          52   
    ...                       ...                             ...         ...   
    13869  0uk9sQ7MjK0CdAUinD4xBV                    Ek Din Pyaar          56   
    13871  0LgIHffVhGleMeHORs7dUl                        Lockdown          56   
    13880  2nzteZ9E7H8r31cS9lM5IS                            『存在』          56   
    13904  6fKCqK8OB2MVnYCHD9moHj               Tiranosaurius Rex          59   
    13906  1IJNIMSX8kFLymE5P9PuHd                         Inumaga          50   

           duration_ms  explicit                                     artists  \
    7           185920         0                          ['Keith Anderson']   
    28          246880         0                            ['Peter Cetera']   
    29          274453         0                            ['Peter Cetera']   
    153         223653         0                      ['Coheed and Cambria']   
    158         215947         1                      ['Coheed and Cambria']   
    ...            ...       ...                                         ...   
    13869       186600         1                                 ['MC STAN']   
    13871       225000         1                             ['Mef', 'SNIK']   
    13880       243409         0                                 ['TENSONG']   
    13904       184323         0  ['Kase.O', 'Harto', 'Escandaloso Xpósito']   
    13906       318796         0                 ['Omar Baliw', '1096 Gang']   

                       release_date  danceability key  acousticness  \
    7     2005-01-03 00:00:00+00:00         0.561  G#        0.0353   
    28    2005-01-04 00:00:00+00:00         0.645  A#        0.0834   
    29    2005-01-04 00:00:00+00:00         0.601  C#        0.6010   
    153   2005-01-15 00:00:00+00:00         0.550   B        0.0114   
    158   2005-01-15 00:00:00+00:00         0.559   B        0.5930   
    ...                         ...           ...  ..           ...   
    13869 2020-12-31 00:00:00+00:00         0.717   F        0.2230   
    13871 2020-12-31 00:00:00+00:00         0.838  A#        0.6170   
    13880 2020-12-31 00:00:00+00:00         0.522   D        0.0626   
    13904 2020-12-31 00:00:00+00:00         0.842   F        0.0600   
    13906 2020-12-31 00:00:00+00:00         0.817   F        0.0811   

           instrumentalness    tempo                              artist  
    7              0.000000  152.089                      Keith Anderson  
    28             0.000000  143.480                        Peter Cetera  
    29             0.000966  105.953                        Peter Cetera  
    153            0.000000  156.958                  Coheed and Cambria  
    158            0.000004   72.015                  Coheed and Cambria  
    ...                 ...      ...                                 ...  
    13869          0.000000  100.147                             MC STAN  
    13871          0.000107  127.998                           Mef, SNIK  
    13880          0.000000   87.879                             TENSONG  
    13904          0.000000  111.938  Kase.O, Harto, Escandaloso Xpósito  
    13906          0.000010   92.492               Omar Baliw, 1096 Gang  

    [32381 rows x 13 columns]

</div>

</div>

<div id="c764ffbf-09e5-44ec-b97d-308e47064055" class="cell code" execution_count="12" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:25:58.037152Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:25:58.036871Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:26:13.230927Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:26:13.230326Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:25:58.037133Z&quot;}" tags="[]">

``` python
result_p6=df_dask[df_dask['acousticness']>0.5]
result_p6.compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="12">

                               id                         name  popularity  \
    2      2lGNHYGWS80iu0EJDyqsHw  Pulkstens deviņus jau zvana          17   
    6      65ZJCO6yTbxqU98xXJhEHT  Meu Jeito Moleque - Ao Vivo          44   
    9      0AktIva3815qwp5QTmo6g3            יש לנו את כל הזמן          20   
    15     52qZx4Y33kGfQrbO4BzoQd   Pali monos mou milo - Live          18   
    19     0q7x5rssXSdckcZMXt77fX                       את שקט          33   
    ...                       ...                          ...         ...   
    13923  0ll7CXRXFWmij9TSMCHJnw                     KENTRIKA          40   
    13924  2OZfDhjvN3Jqbvk2BwyyTV              MAYRES SAKOYLES          41   
    13926  5OVi4TsDFY8swBMwWrH3oT                     PARANOIA          41   
    13928  3sUNHFHqhhwA61cr4GhUV4                         Team          41   
    13933  7G2lz6En32ncbkpE6VmUdu                      TAHAMOU          42   

           duration_ms  explicit                             artists  \
    2           173907         0                           ['Prego']   
    6           162880         0                   ['Jeito Moleque']   
    9           233347         0                   ['Eviatar Banai']   
    15          127853         0                 ['Giorgos Alkaios']   
    19          349000         0                   ['Eviatar Banai']   
    ...            ...       ...                                 ...   
    13923       193058         1                           ['RICTA']   
    13924       166857         1  ['RICTA', 'Savv', 'Koas', 'Ortiz']   
    13926       294290         1                           ['RICTA']   
    13928       184320         1              ['Thug Slime', 'Scar']   
    13933       240527         1            ['RICTA', 'Leaderbrain']   

                       release_date  danceability key  acousticness  \
    2     2005-01-02 00:00:00+00:00         0.381   F         0.953   
    6     2005-01-03 00:00:00+00:00         0.486   C         0.539   
    9     2005-01-03 00:00:00+00:00         0.434   C         0.800   
    15    2005-01-03 00:00:00+00:00         0.504   A         0.592   
    19    2005-01-03 00:00:00+00:00         0.670   D         0.539   
    ...                         ...           ...  ..           ...   
    13923 2020-12-31 00:00:00+00:00         0.679  A#         0.694   
    13924 2020-12-31 00:00:00+00:00         0.742  C#         0.517   
    13926 2020-12-31 00:00:00+00:00         0.640   B         0.639   
    13928 2020-12-31 00:00:00+00:00         0.908   E         0.507   
    13933 2020-12-31 00:00:00+00:00         0.854   D         0.558   

           instrumentalness    tempo                    artist  
    2              0.000000  120.822                     Prego  
    6              0.000000   83.260             Jeito Moleque  
    9              0.005930  107.535             Eviatar Banai  
    15             0.001100   97.633           Giorgos Alkaios  
    19             0.079300  124.018             Eviatar Banai  
    ...                 ...      ...                       ...  
    13923          0.026700   95.247                     RICTA  
    13924          0.000000   71.635  RICTA, Savv, Koas, Ortiz  
    13926          0.000009  139.120                     RICTA  
    13928          0.000000  125.056          Thug Slime, Scar  
    13933          0.000000  140.051        RICTA, Leaderbrain  

    [40475 rows x 13 columns]

</div>

</div>

<div id="17ac77c3-7738-4bbc-a1f7-d944e1161d2c" class="cell code" execution_count="13" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:26:13.232192Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:26:13.231904Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:26:13.241956Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:26:13.241374Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:26:13.232169Z&quot;}" tags="[]">

``` python
df_dask['anio lanzamiento']=df_dask['release_date'].dt.year
df_dask['mes lanzamiento']=df_dask['release_date'].dt.month
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

</div>

<div id="1ceb19d2-1957-43fb-a5f9-11fca35f8bf6" class="cell code" execution_count="14" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:26:17.601978Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:26:17.601681Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:26:30.792723Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:26:30.791717Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:26:17.601956Z&quot;}" tags="[]">

``` python
df_dask['duration_ms'].mean().compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="14">

    232712.66002423674

</div>

</div>

<div id="8d8ab8c0-4051-49ff-87ec-d127ea22b76e" class="cell code" execution_count="15" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:26:30.796577Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:26:30.796110Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:26:51.076345Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:26:51.075720Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:26:30.796549Z&quot;}" tags="[]">

``` python
result_p9=df_dask[df_dask['artist'].str.contains("Fonseca")]
(result_p9['duration_ms']/6000).mean().compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="15">

    38.30361695906433

</div>

</div>

<div id="a12ec64b-7c1f-4137-bc2b-62dc7e61a3eb" class="cell code" execution_count="16" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:26:51.077701Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:26:51.077456Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:27:03.730308Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:27:03.729398Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:26:51.077679Z&quot;}" tags="[]">

``` python
conteo_id=df_dask.groupby("id").size()
result_p10=conteo_id[conteo_id>1]
result_p10.compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="16">

    Series([], dtype: int64)

</div>

</div>

<div id="69e15bb5-df34-45ae-9afa-57329f05a004" class="cell code" execution_count="17" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:27:03.737505Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:27:03.734757Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:27:19.292912Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:27:19.292163Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:27:03.737472Z&quot;}" tags="[]">

``` python
result_p11=df_dask.isnull().sum()
result_p11.compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="17">

    id                  0
    name                0
    popularity          0
    duration_ms         0
    explicit            0
    artists             0
    release_date        0
    danceability        0
    key                 0
    acousticness        0
    instrumentalness    0
    tempo               0
    artist              0
    anio lanzamiento    0
    mes lanzamiento     0
    dtype: int64

</div>

</div>

<div id="95d817c6-fa67-4fa2-bb64-3d78a265ea51" class="cell code" execution_count="18" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:27:19.294770Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:27:19.294195Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:27:41.697378Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:27:41.695907Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:27:19.294738Z&quot;}" tags="[]">

``` python
df_dask[['popularity','tempo','danceability']].std().compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="18">

    popularity      18.834524
    tempo           28.786926
    danceability     0.157910
    dtype: float64

</div>

</div>

<div id="abb994c8-f337-41f8-82e8-fc74535a2761" class="cell code" execution_count="20" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:28:08.188723Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:28:08.188461Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:28:30.233902Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:28:30.233090Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:28:08.188698Z&quot;}" tags="[]">

``` python
df_dask.groupby(['artist','anio lanzamiento'])['popularity'].mean().compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="20">

    artist                  anio lanzamiento
    "5nizza", [dunkelbunt]  2007                37.0
    "AStudio"               2005                37.0
    "Adolescents Orquesta"  2005                42.0
                            2007                46.0
                            2008                51.0
                                                ... 
    魏嘉瑩 Arrow Wei           2017                37.0
    魏奇奇                     2018                57.0
    麦小兜                     2018                48.0
    黃冠筑, Randy C            2019                52.0
    黃宣                      2019                48.0
    Name: popularity, Length: 86299, dtype: float64

</div>

</div>

<div id="b58a0ce8-139a-4d96-af59-163e2444439e" class="cell code" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:29:43.927863Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:29:43.927615Z&quot;}" tags="[]">

``` python
df_dask[df_dask['duration_ms']>5000000].compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="22">

                               id  \
    5416   7foc25ig7dibxvULPU2kBG   
    10754  6rGikpwOv3LXaHWVCYbMNC   

                                                        name  popularity  \
    5416                            Brown Noise - 90 Minutes          50   
    10754  New Year's Eve 2015 Party Hits - Full DJ Party...           0   

           duration_ms  explicit              artists              release_date  \
    5416       5403500         0    ['Sound Dreamer'] 2013-06-05 00:00:00+00:00   
    10754      5042185         0  ['Various Artists'] 2014-12-19 00:00:00+00:00   

           danceability key  acousticness  instrumentalness    tempo  \
    5416          0.000   D       0.11100           0.39200    0.000   
    10754         0.457   B       0.00467           0.00109  129.516   

                    artist  anio lanzamiento  mes lanzamiento  
    5416     Sound Dreamer              2013                6  
    10754  Various Artists              2014               12  

</div>

</div>

<div id="e472fd47-4020-40e9-8c9c-fe13853bf36f" class="cell code" execution_count="23" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:31:12.868843Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:31:12.868586Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:31:39.719741Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:31:39.718997Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:31:12.868823Z&quot;}" tags="[]">

``` python
df_dask[['popularity','tempo','danceability','acousticness']].corr().compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="23">

                  popularity     tempo  danceability  acousticness
    popularity      1.000000 -0.026500      0.151833      0.043779
    tempo          -0.026500  1.000000     -0.112013     -0.142594
    danceability    0.151833 -0.112013      1.000000     -0.156032
    acousticness    0.043779 -0.142594     -0.156032      1.000000

</div>

</div>

<div id="885db147-5e33-4828-ae1b-767ddc233b5e" class="cell code" execution_count="24" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:32:57.325732Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:32:57.325452Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:33:14.438328Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:33:14.437699Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:32:57.325713Z&quot;}" tags="[]">

``` python
result_p16=df_dask[df_dask['artist'].str.contains("Bad Bunny|J Balvin")]
result_p16.compute()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="24">

                               id                                   name  \
    4770   0gHSFpCQZmZ1LwPHQpzn6T  Sin Compromiso (feat. Jowell Y Randy)   
    9264   3TllzYD3T3VSy1Mg3m7vyG                 Si Tú No Estás - Remix   
    1304   3yoO9jbPHRxAsoUuyx4gG3                         Sin Compromiso   
    6228   7mPwkbaoiQ5bf8FPbRJzUr                                   6 AM   
    6234   6klAm7Z2oR2FM7lozc7agF                              Tranquila   
    ...                       ...                                    ...   
    11241  4MzXwWMhyBbmu6hOcLVD49                                 DÁKITI   
    11253  5RubKOuDoPn5Kj5TLVxSxY                             TE MUDASTE   
    11306  0tjZv2hChdHZCW1zFXpy1J                              HOY COBRÉ   
    11555  2XghxCSGfhpGR2B3ahQXVr                                  Lento   
    12883  3eblNP3Zd5b5J3JaOckl8Y                   Baby (with J Balvin)   

           popularity  duration_ms  explicit  \
    4770           41       245555         0   
    9264           43       227653         0   
    1304           43       189027         0   
    6228           62       243227         0   
    6234           54       199933         0   
    ...           ...          ...       ...   
    11241          90       205090         1   
    11253          88       130014         1   
    11306          77       162151         1   
    11555          71       188910         0   
    12883          74       193555         1   

                                                     artists  \
    4770                                        ['J Balvin']   
    9264   ['Cosculluela', 'J Balvin', 'Ñejo & Dalmata', ...   
    1304                                        ['J Balvin']   
    6228                             ['J Balvin', 'Farruko']   
    6234                                        ['J Balvin']   
    ...                                                  ...   
    11241                       ['Bad Bunny', 'Jhay Cortez']   
    11253                                      ['Bad Bunny']   
    11306                                      ['Bad Bunny']   
    11555                            ['Mr Eazi', 'J Balvin']   
    12883                      ['Sfera Ebbasta', 'J Balvin']   

                       release_date  danceability key  acousticness  \
    4770  2011-05-09 00:00:00+00:00         0.755   C        0.1130   
    9264  2011-12-13 00:00:00+00:00         0.640   D        0.3760   
    1304  2012-01-01 00:00:00+00:00         0.775   G        0.1930   
    6228  2013-07-15 00:00:00+00:00         0.747   F        0.1420   
    6234  2013-07-15 00:00:00+00:00         0.731   E        0.0278   
    ...                         ...           ...  ..           ...   
    11241 2020-11-27 00:00:00+00:00         0.731   E        0.4010   
    11253 2020-11-27 00:00:00+00:00         0.811  A#        0.2340   
    11306 2020-11-27 00:00:00+00:00         0.860   B        0.0464   
    11555 2020-12-04 00:00:00+00:00         0.870  A#        0.5220   
    12883 2020-12-18 00:00:00+00:00         0.755  A#        0.1250   

           instrumentalness    tempo  \
    4770           0.000000   97.986   
    9264           0.000000  170.018   
    1304           0.000000   98.031   
    6228           0.000000  175.978   
    6234           0.000000  175.944   
    ...                 ...      ...   
    11241          0.000052  109.928   
    11253          0.000572   92.025   
    11306          0.000091  145.001   
    11555          0.648000   92.025   
    12883          0.001420   99.984   

                                                   artist  anio lanzamiento  \
    4770                                         J Balvin              2011   
    9264   Cosculluela, J Balvin, Ñejo & Dalmata, Farruko              2011   
    1304                                         J Balvin              2012   
    6228                                J Balvin, Farruko              2013   
    6234                                         J Balvin              2013   
    ...                                               ...               ...   
    11241                          Bad Bunny, Jhay Cortez              2020   
    11253                                       Bad Bunny              2020   
    11306                                       Bad Bunny              2020   
    11555                               Mr Eazi, J Balvin              2020   
    12883                         Sfera Ebbasta, J Balvin              2020   

           mes lanzamiento  
    4770                 5  
    9264                12  
    1304                 1  
    6228                 7  
    6234                 7  
    ...                ...  
    11241               11  
    11253               11  
    11306               11  
    11555               12  
    12883               12  

    [274 rows x 15 columns]

</div>

</div>
