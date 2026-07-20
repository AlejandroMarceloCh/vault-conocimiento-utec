---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.11
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.11.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.11.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.11.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 11083 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 11083 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
5MgBUUjbkQ27Kd9CbeZFLo,Roses (feat. ROZES) - Zaxx Remix,54,190267,0,"['The Chainsmokers', 'ROZES', 'Zaxx']",2016-01-01 00:00:00+00:00,0.677,C#,0.00445,0.0146,128.121
5FXehnLmh6kweglLXHkOJ5,The Way It Goes,24,188287,0,['Púr Múdd'],2016-01-01 00:00:00+00:00,0.728,C#,0.0857,0.000266,115.94
0xFU2rL97jyengK90bcfJI,Hea Tuju Laul,23,235755,0,['Anne Veski'],2016-01-01 00:00:00+00:00,0.7240000000000001,F#,0.0528,0.0,133.004
3Q06XfNgOjBQAyPV4GbYaR,Allt jag behöver,53,163657,0,['Miriam Bryant'],2016-01-01 00:00:00+00:00,0.6940000000000001,A#,0.0441,6.41e-06,151.96
2MRKc0dryJdSlrbFj0KV9I,Who's To Say? - Live,24,374413,0,['Moon Taxi'],2016-01-01 00:00:00+00:00,0.512,A#,0.00385,0.00011,92.057
5DrikCrFK2V1F7NtEBqSXO,La Verdad,49,157964,0,['Siloé'],2016-01-01 00:00:00+00:00,0.611,A,0.7340000000000001,0.0,117.14299999999999
6pUGdsOjgVXf5ulbQRZtRy,Vi Lovar (Besvärjelse),43,250667,0,['Eva Weel Skram'],2016-01-01 00:00:00+00:00,0.433,A#,0.9279999999999999,0.0,86.196
010Ovolh5Pixkv3GUDsXFa,Agent Lonely - 2015 Heavy Workout Mix,0,223000,0,['Lightyear'],2016-01-01 00:00:00+00:00,0.619,A#,0.00443,0.878,130.054
0PRX6CXffB3cARlzNCkmR4,Selmas sang (fra Snøfall),44,208427,0,['Eva Weel Skram'],2016-01-01 00:00:00+00:00,0.428,C,0.183,4.8899999999999996e-05,88.323
4IuJtm9P6dXgmR6PpQfaNo,Picturing Love,45,215000,0,['July Talk'],2016-01-01 00:00:00+00:00,0.7,A,0.0299,4.18e-05,116.368
1h2aXTmrgmJ6smdoUGQIPF,Year Zero - Live,13,252293,0,['Moon Taxi'],2016-01-01 00:00:00+00:00,0.289,F,0.000628,0.0,79.023
2Oc2oLhrsqADmYYFos8tPt,Passarinhos (Rdio Sessions) (feat. Xênia França) - Ao Vivo,49,229413,0,"['Emicida', 'Xênia França']",2016-01-01 00:00:00+00:00,0.759,E,0.40700000000000003,0.0,80.149
3de8Tv5oYKCchjv223Wkyh,När kärleken tar slut,40,254573,0,['Lisa Nilsson'],2016-01-01 00:00:00+00:00,0.586,F,0.7020000000000001,0.0,139.937
5DsAYK3STPu8srYNX4SXfU,Balewala,44,311753,0,['Loonie'],2016-01-01 00:00:00+00:00,0.72,A,0.527,1.6899999999999997e-05,97.007
2iGeiOOKZ0GDZG9mNm0QGE,Aphrodite,46,245435,0,['The Ridleys'],2016-01-01 00:00:00+00:00,0.6920000000000001,E,0.8490000000000001,0.0843,113.95299999999999
1VDfQ4Wu5PrcO3mKKC3841,Traces - Nostalgic Mix,28,489091,0,['The Godfathers Of Deep House SA'],2016-01-01 00:00:00+00:00,0.546,D#,0.00746,0.887,118.025
2TKxke3omsD8a3cZoc8wXT,The Only One,39,159822,0,['Miriam Bryant'],2016-01-01 00:00:00+00:00,0.71,D,0.0201,0.00455,111.991
6IOitwRrqNNymujyIZQ3Zn,Life Is A Flower,43,169372,0,['Miriam Bryant'],2016-01-01 00:00:00+00:00,0.627,E,0.188,5.92e-06,86.01700000000001
4BIgpWXnGeTbmQvUrBPGLu,"On the Wings of Love - From ""On the Wings of Love""",45,274628,0,['Kyla'],2016-01-01 00:00:00+00:00,0.302,C#,0.63,1.31e-06,136.805
3qWRmouJQNWR1Fk61PFuwa,Stationen,48,168276,0,['Miriam Bryant'],2016-01-01 00:00:00+00:00,0.387,E,0.13699999999999998,0.0,173.69299999999998
1NJfEOlqun7kEWwtSm06Yn,I Saw Her Standing There - 2004 It Was 40 Years Ago Today Mix,0,154093,0,['Jaimie Vernon'],2016-01-01 00:00:00+00:00,0.742,A,0.792,0.0,123.024
20ozlzv5wZrQVzUupnMeo3,Fight Song,51,204013,0,['Rachel Platten'],2016-01-01 00:00:00+00:00,0.564,G,0.0549,0.0,175.924
3nD5Zyg1zbmlLFcDXZswa0,Vart du än går,49,229067,0,['Lisa Nilsson'],2016-01-01 00:00:00+00:00,0.498,D,0.924,8.13e-06,96.042
7ajeKZVPiTT006vxoCZany,One Last Time,49,159087,0,['Miriam Bryant'],2016-01-01 00:00:00+00:00,0.655,F,0.0247,1.58e-06,85.98
6oagqjixKcQglIjjYQGGkU,Ambon,48,281282,0,['Migz & Maya'],2016-01-01 00:00:00+00:00,0.545,C,0.425,0.0,159.80100000000002
75L2KgB1DNkjY28GVB82nS,Blodskudt,49,347723,0,['Jamaika'],2016-01-01 00:00:00+00:00,0.595,G,0.29,0.0,78.209
49OMed4MSSZ15Ry2qnrHIO,You'll Be Safe Here,49,272187,0,['Elmo Magalona'],2016-01-01 00:00:00+00:00,0.40299999999999997,B,0.24,0.0,79.85300000000001
0qiprdV8xNfehA6G2rDbiP,Verdades Do Tempo,49,259145,0,['Thiago Brado'],2016-01-01 00:00:00+00:00,0.175,E,0.0932,0.0,50.451
4ub59HeXqdYApJtkJqnvXE,I'll Never Go,50,263056,0,['Erik Santos'],2016-01-01 00:00:00+00:00,0.45399999999999996,B,0.723,0.0,139.89
4Ho6xWdM04np96TTgP82NN,Alecrim Dourado,51,104500,0,['Ana Santos'],2016-01-01 00:00:00+00:00,0.795,C,0.96,1.74e-05,120.15
5zfWoufXTAXICVcxgR5fYO,Carinhoso,53,112231,0,"['Marisa Monte', 'Paulinho Da Viola']",2016-01-01 00:00:00+00:00,0.542,G,0.812,4.270000000000001e-05,104.986
3MWkqe3GTNP4cH8np1fDAB,เธอจะเชื่อไหม,29,272573,0,['Kor Notapol Srichomkwan'],2016-01-01 00:00:00+00:00,0.616,A#,0.11699999999999999,0.0111,98.319
5Ew6ieSRFMoGZlF3rWtDNM,Acicálame,56,202053,0,['Tessa Ia'],2016-01-01 00:00:00+00:00,0.675,D,0.0889,6.1e-06,130.983
4gQ3Dg2I22lt13CVny63ri,Run Right Back - Live,14,227400,0,['Moon Taxi'],2016-01-01 00:00:00+00:00,0.349,G#,0.0842,0.0,141.121
30xT5N6yPt840MdnM4GVKA,Michael Jackson through the years,0,324147,0,"['Michael Jackson', 'Sjöbo Ungdomsorkester']",2016-01-01 00:00:00+00:00,0.425,F,0.754,0.636,123.618
7JZUD0GPmCKtY5XJWL0dJl,"Pilgrim - Live in Leipzig, 2015",2,392707,0,['Deine Lakaien'],2016-01-01 00:00:00+00:00,0.18600000000000003,C,0.619,0.00047400000000000003,171.497
3a7ElnG4oDbQiILiCCKduY,Traicionera,49,216000,0,['Américo'],2016-01-01 00:00:00+00:00,0.754,C#,0.40399999999999997,0.0,100.976
3SjvaBA2qyzTU4fJSwZuVT,"Europe - Live in Warsaw, 2015",1,369373,0,['Deine Lakaien'],2016-01-01 00:00:00+00:00,0.634,A#,0.382,0.0028399999999999996,96.025
7KgJC1TRqgvMMAHZlLIY1K,Revolutia,28,184552,0,['Dani Mocanu'],2016-01-01 00:00:00+00:00,0.504,B,0.27899999999999997,0.0,112.039
4e6KOiwokihP4BqOzAtq9M,T.C. Radiation - Original 1979 Version,0,282443,0,['Radiation'],2016-01-01 00:00:00+00:00,0.713,D,0.027999999999999997,0.535,128.82299999999998

Resumen numérico:
         popularity   duration_ms      explicit  danceability  acousticness  instrumentalness         tempo
count  11083.000000  1.108300e+04  11083.000000  11083.000000  11083.000000      11083.000000  11083.000000
mean      39.280339  2.301142e+05      0.124154      0.604140      0.280669          0.086585    121.401084
std       19.779825  1.285592e+05      0.329772      0.160123      0.289881          0.241359     28.852216
min        0.000000  2.821300e+04      0.000000      0.000000      0.000000          0.000000      0.000000
25%       30.000000  1.905625e+05      0.000000      0.502000      0.031300          0.000000     98.992000
50%       43.000000  2.204350e+05      0.000000      0.617000      0.171000          0.000002    122.000000
75%       53.000000  2.556580e+05      0.000000      0.722000      0.479000          0.000830    138.039000
max       88.000000  4.018399e+06      1.000000      0.982000      0.996000          1.000000    219.827000
