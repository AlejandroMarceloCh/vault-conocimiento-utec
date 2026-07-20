---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.14
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.14.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.14.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.14.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 11907 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 11907 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
6DD5RDAyLBdGc1NC9Pju3E,Aldrig (feat. Carmon),42,247869,0,"['Jamaika', 'Carmon']",2019-01-01 00:00:00+00:00,0.6759999999999999,E,0.27,0.0,140.595
6xwqSwpDiTFi8vVAfiIHix,מפיות,37,155000,0,['Stephane Legar'],2019-01-01 00:00:00+00:00,0.782,B,0.387,0.0,74.959
4s4Uf0n0bHWVt4Jkce27Ji,2019 - The Year to Build,0,288105,0,['M C Rev'],2019-01-01 00:00:00+00:00,0.8079999999999999,D,0.546,0.000244,100.98299999999999
2D3YPhWaJaxdfCOD53Eyu0,私の思春期へ,47,226973,0,['BOL4'],2019-01-01 00:00:00+00:00,0.451,A,0.787,0.0,174.18400000000003
0lO61CZzLPbMbwOFu7wGkl,נחכה לך,35,207443,0,"['Nathan Goshen', 'Ishay Ribo']",2019-01-01 00:00:00+00:00,0.542,D,0.491,0.0,74.911
2wI3clxRtiMlPdYTYxw2cC,Na zawsze,49,186812,1,"['Bryan', 'PIT']",2019-01-01 00:00:00+00:00,0.659,B,0.586,0.0,99.602
6J9V3EgYR2Kw0XZUaLcoID,Humo en la Trampa,63,258354,1,"['Aleman', 'Yoga Fire', 'Cozy Cuz', 'Fntxy', 'Dee']",2019-01-01 00:00:00+00:00,0.917,B,0.142,0.0,129.011
24s3bFXbw8rKOXSVcJp1fG,Au Au,53,176000,0,['Filatov & Karas'],2019-01-01 00:00:00+00:00,0.8009999999999999,A,0.0158,6.52e-05,119.941
20hvKL8W9wjVyyVBZ6McNf,เจ็บจนพอ,51,277500,0,['Wanyai'],2019-01-01 00:00:00+00:00,0.445,C#,0.22899999999999998,0.0,173.938
3H1bMJUuqvhXLxNQECfkK7,Jeden Buziak,52,169993,1,['TKM'],2019-01-01 00:00:00+00:00,0.488,A#,0.172,0.0,104.714
5OvGwE0DKVSAOuSuxYDVol,MASNO FEST,47,147470,1,"['Masno', 'Dycha']",2019-01-01 00:00:00+00:00,0.747,D,0.29600000000000004,0.0,124.055
2e6ATMiu9S4t9hFNOByjJE,Niña Bien,59,259500,0,['Revolver Cannabis'],2019-01-01 00:00:00+00:00,0.9229999999999999,G,0.225,0.0,119.994
1YCgD357tcgqVJq05MEZyx,Banalne,49,204907,1,"['Wiatr', 'Tymek']",2019-01-01 00:00:00+00:00,0.637,C,0.858,0.0,106.015
6nkRcMY1BweFKCE8JTMBCb,Selamanya,40,258049,0,['Usop'],2019-01-01 00:00:00+00:00,0.479,C#,0.0441,0.0,148.024
4rBu4nVFX76Y0DGbhQtB3j,6 Rano,49,262003,1,"['Sobota', 'Kabe']",2019-01-01 00:00:00+00:00,0.8009999999999999,C,0.555,0.0,130.03
1sOxcTCGLYUe1gLLp4UODs,Mundur Alon-Alon,48,233143,0,"['Nella Kharisma', 'Ilux']",2019-01-01 00:00:00+00:00,0.665,F,0.134,0.00295,139.995
0XMX8i8IY19Lo6cMJaNxIy,Where Am I?,47,47530,0,['Ruttle Ronny'],2019-01-01 00:00:00+00:00,0.43700000000000006,A#,0.0461,0.815,105.07700000000001
79cyY33irbHnS93VEmzJCX,Skiety & Klapki - Skiety & Klapki,54,185518,1,"['Kabe', 'Kizo']",2019-01-01 00:00:00+00:00,0.972,D#,0.14300000000000002,0.0,121.92200000000001
0cYpavgvIgO51TSaco1tTZ,A Que Jugamos,30,337345,0,['Jhonathan Chávez y Los Triunfadores'],2019-01-01 00:00:00+00:00,0.47600000000000003,G#,0.16,2e-06,192.104
46doqU89HXCjtvNJnC7P5v,Year: 2018,0,230400,1,"['VixEnt', 'Armbreaker21', 'BUSTANUT', 'Fly To Die', 'Tron']",2019-01-01 00:00:00+00:00,0.46299999999999997,C#,0.000342,0.0868,150.097
2IlLQcASGHJjJGyZnKjRAN,Dynamite,41,231573,0,['Sigrid'],2019-01-01 00:00:00+00:00,0.552,C#,0.961,0.000169,114.094
25BaMxOBYkpnPy8IhTI7qk,Klubowa Suka,56,121836,1,"['C0PIK', 'Tymek']",2019-01-01 00:00:00+00:00,0.733,D,0.265,0.0,133.94899999999998
3eohASCbotGVSsLNlulEgE,Ona'e,55,151890,0,"['Jala Brat', 'Buba Corelli', 'Coby']",2019-01-01 00:00:00+00:00,0.7509999999999999,C#,0.287,0.000157,130.02100000000002
2YiR3wOMKM5A0bvZn4Qspx,New Year 2019,0,216173,0,['Dj Blaz3'],2019-01-01 00:00:00+00:00,0.647,B,0.163,0.807,132.985
4znjPaMnY2qOi3WkiBieTw,Kamikaza,53,157931,0,"['Jala Brat', 'Buba Corelli', 'Senidah']",2019-01-01 00:00:00+00:00,0.6709999999999999,F,0.386,0.0,173.99400000000003
3fLQygEvPGElJyAUGeNqQ9,Jagodzianki (prod.by Abel de Jong),56,160630,0,"['Abel de Jong', 'Mr. Polska', 'Malik Montana']",2019-01-01 00:00:00+00:00,0.9570000000000001,A,0.295,2.41e-06,126.985
0gziJFlbSrZDAWgznQB7ZD,Nema bolje,52,139592,0,"['Jala Brat', 'Buba Corelli', 'RAF Camora']",2019-01-01 00:00:00+00:00,0.805,D#,0.0953,0.0,98.069
5vwnGfnh0zrjbKKRNFiSMg,Førsterekka 2020,58,162694,0,"['Ringnes-Ronny', 'DJ FITTE']",2019-01-01 00:00:00+00:00,0.78,B,0.0483,1.55e-05,154.99200000000002
08rTawsConP932IiqH9mQg,Strangers,46,233726,0,['Sigrid'],2019-01-01 00:00:00+00:00,0.758,E,0.00569,0.00119,115.042
738YzJ5CjBrlyUhY2mnuHf,หัวหิน - Huahin Loop,48,223845,0,['Wanyai'],2019-01-01 00:00:00+00:00,0.718,A,0.18,0.0,85.007
4NyIRtMv7VlOhGNdbUIPgM,80's,55,138600,0,['Tymek'],2019-01-01 00:00:00+00:00,0.773,C#,0.799,0.0155,100.01700000000001
6QuDHK5FwGn4wmzCZhQzA7,Don't Kill My Vibe,48,184320,0,['Sigrid'],2019-01-01 00:00:00+00:00,0.5479999999999999,A#,0.271,0.00013700000000000002,149.98
2zfkF4W0wfyzVeDcEGMdZE,A Través del Vaso,49,229630,0,['Los Pincheira del Sur'],2019-01-01 00:00:00+00:00,0.655,F,0.10800000000000001,0.0,131.881
01hQQr1vfQiz4LPpQnDGiO,Tummilla teillä,42,231867,0,['Vesterinen yhtyeineen'],2019-01-01 00:00:00+00:00,0.542,B,0.0067599999999999995,0.0147,148.015
1N4jTBZnj2M3SOTLB8FXPs,Happy New Year 2019,0,12000,1,['Corey-G'],2019-01-01 00:00:00+00:00,0.0,F,0.22699999999999998,0.0,0.0
7nMB9ZYve3sCcjWKyu0IpI,Anklage,46,209432,0,['Jamaika'],2019-01-01 00:00:00+00:00,0.568,F,0.278,0.0,132.825
31bYiiePY6AeU73uWNncKE,Activate,48,61205,0,['Alec. J'],2019-01-01 00:00:00+00:00,0.688,F,0.000254,0.968,99.971
6pv2VnKMSF5OX90R4p7oRd,Jaga Orang Pu Jodoh Slow,47,260087,0,['Sanza Sabila'],2019-01-01 00:00:00+00:00,0.7190000000000001,E,0.0271,2.48e-05,159.965
0zeNIUj1lHn5puKBaLTOmn,Beba,34,191986,1,['King Monroe'],2019-01-01 00:00:00+00:00,0.7659999999999999,A#,0.0367,0.0,141.849
5izYHw7kEtvIESxCKxfcTq,Mała Życie To Nie Film,47,275110,1,['TKM'],2019-01-01 00:00:00+00:00,0.737,F,0.0172,0.0,100.01100000000001

Resumen numérico:
         popularity   duration_ms      explicit  danceability  acousticness  instrumentalness         tempo
count  11907.000000  1.190700e+04  11907.000000  11907.000000  11907.000000      11907.000000  11907.000000
mean      44.920551  2.168024e+05      0.214916      0.649724      0.293902          0.081428    122.023748
std       20.910637  1.095647e+05      0.410781      0.159258      0.278868          0.235854     29.482622
min        0.000000  6.360000e+03      0.000000      0.000000      0.000000          0.000000      0.000000
25%       37.000000  1.772180e+05      0.000000      0.552000      0.049800          0.000000     98.995000
50%       50.000000  2.057470e+05      0.000000      0.670000      0.204000          0.000002    122.953000
75%       59.000000  2.400000e+05      0.000000      0.765000      0.485000          0.000638    139.990500
max       94.000000  4.775518e+06      1.000000      0.977000      0.996000          1.000000    220.230000
