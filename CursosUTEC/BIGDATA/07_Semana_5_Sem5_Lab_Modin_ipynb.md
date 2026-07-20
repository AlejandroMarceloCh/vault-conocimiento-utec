---
curso: BIGDATA
titulo: 07 - Semana 5/Sem5_Lab Modin
slides: 0
fuente: 07 - Semana 5/Sem5_Lab Modin.ipynb
---

<div id="8d3a3609-a049-4deb-abf7-a64cc06cecff" class="cell code" execution_count="1" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:42:02.742887Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:42:02.742555Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:42:02.746971Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:42:02.746463Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:42:02.742868Z&quot;}" tags="[]">

``` python
# !pip install "modin[dask]"
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

</div>

<div id="481d57aa-3a9a-4287-a574-72554fc7b34f" class="cell code" execution_count="2" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:42:10.625054Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:42:10.624810Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:42:10.751071Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:42:10.750457Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:42:10.625038Z&quot;}" tags="[]">

``` python
import modin.pandas as pd
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

</div>

<div id="5d84c985-6669-44db-86be-b396a33b9556" class="cell code" execution_count="3" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:43:06.144455Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:43:06.144172Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:43:58.117745Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:43:58.117112Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:43:06.144435Z&quot;}" tags="[]">

``` python
df=pd.read_parquet('gs://bucket-utec-2026-v7/data/spotify_parquet')
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output stream stderr">

    2026-04-24 02:43:15,160	INFO worker.py:2012 -- Started a local Ray instance.
    FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enable this behavior and turn off this error message, set RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO=0

</div>

</div>

<div id="4fb0bd38-5a7d-49f0-8d86-fab26d7da892" class="cell code" execution_count="4" execution="{&quot;iopub.execute_input&quot;:&quot;2026-04-24T02:44:00.598598Z&quot;,&quot;iopub.status.busy&quot;:&quot;2026-04-24T02:44:00.597954Z&quot;,&quot;iopub.status.idle&quot;:&quot;2026-04-24T02:44:00.669970Z&quot;,&quot;shell.execute_reply&quot;:&quot;2026-04-24T02:44:00.669313Z&quot;,&quot;shell.execute_reply.started&quot;:&quot;2026-04-24T02:44:00.598563Z&quot;}" tags="[]">

``` python
df.head()
```

<div class="output display_data">

``` json
{"msg":"{\"msgtype\": \"sparkMonitorInit\"}","msgtype":"fromscala"}
```

</div>

<div class="output execute_result" execution_count="4">

                                             id                         name  \
    __null_dask_index__                                                        
    0                    2fASnKww9WIi2YMp8s7sDi                        Sueño   
    1                    2j7mtIlWmFfvodCFAAYd3E                   Confiésame   
    2                    2lGNHYGWS80iu0EJDyqsHw  Pulkstens deviņus jau zvana   
    3                    1BI6ciDl653mn2Oip8KUID        Melanholiskais valsis   
    4                    7oVJpmVnFYtNZA0TQmF2OX       Sobrenatural - Ao Vivo   

                         popularity  duration_ms  explicit            artists  \
    __null_dask_index__                                                         
    0                            37       251480         0        ['Fonseca']   
    1                            39       243000         0        ['Fonseca']   
    2                            17       173907         0          ['Prego']   
    3                            13       234493         0          ['Prego']   
    4                            45       219133         0  ['Jeito Moleque']   

                                     release_date  danceability key  acousticness  \
    __null_dask_index__                                                             
    0                   2005-01-02 00:00:00+00:00         0.511   F        0.0841   
    1                   2005-01-02 00:00:00+00:00         0.700  F#        0.0813   
    2                   2005-01-02 00:00:00+00:00         0.381   F        0.9530   
    3                   2005-01-02 00:00:00+00:00         0.535   A        0.3330   
    4                   2005-01-03 00:00:00+00:00         0.475   A        0.3660   

                         instrumentalness    tempo  
    __null_dask_index__                             
    0                            0.000028  114.025  
    1                            0.000000  112.038  
    2                            0.000000  120.822  
    3                            0.000012  169.968  
    4                            0.000000  159.799  

</div>

</div>
