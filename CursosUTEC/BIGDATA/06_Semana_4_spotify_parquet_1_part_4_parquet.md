---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.4
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.4.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.4.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.4.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 9593 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 9593 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
1le5KVGTF1xWf2aUj7ruLy,Fallin' For You,60,215547,0,['Colbie Caillat'],2009-01-01 00:00:00+00:00,0.644,E,0.156,0.0,117.04299999999999
7jvp8DZy7FtHeXdN1k8w2s,Belle Of The Boulevard,42,242453,0,['Dashboard Confessional'],2009-01-01 00:00:00+00:00,0.485,E,0.0453,1.01e-06,89.75399999999999
5CijCh8uOTWZO9DQpYwAXw,The Mess I Made,47,230613,0,['Parachute'],2009-01-01 00:00:00+00:00,0.423,F#,0.0158,0.0,165.394
1V4jC0vJ5525lEF1bFgPX2,Shots,70,222133,1,"['LMFAO', 'Lil Jon']",2009-01-01 00:00:00+00:00,0.825,C#,0.00851,1.4e-06,128.016
1PknFWeSYaeCiHHUShL5ZJ,Angelo,47,210360,0,['Francesco Renga'],2009-01-01 00:00:00+00:00,0.358,B,0.5870000000000001,1.09e-05,81.993
5jOb9snt3PcgxsKsf6ZGOk,I Just Don't Want to Be Lonely,34,250854,0,['Regine Velasquez'],2009-01-01 00:00:00+00:00,0.629,F#,0.355,3.24e-05,146.172
5KWXi2eCYsC6ofIILjvG4V,Signs,52,241693,0,['Five Man Electrical Band'],2009-01-01 00:00:00+00:00,0.446,D,0.243,0.0,153.672
5MtwDBbXBr1eu7LrdyoZ3l,Amakakeru Ryu No Hirameki,33,207667,0,['Silent Sanctuary'],2009-01-01 00:00:00+00:00,0.456,C,0.21600000000000003,1.3500000000000001e-05,113.58200000000001
7eshzPtkSCj122TtU3RLfC,Dekada 90,33,353013,0,['Silent Sanctuary'],2009-01-01 00:00:00+00:00,0.451,D,0.0376,0.00038199999999999996,75.016
0xDdTPs5B1DKuh36PMnSGH,Sa Buhay Na'to,34,296107,0,['Silent Sanctuary'],2009-01-01 00:00:00+00:00,0.647,E,0.122,1.42e-06,112.406
1ax4ZAVsA2k1WmlAEiknCH,Love Me,43,191573,0,['Justin Bieber'],2009-01-01 00:00:00+00:00,0.7290000000000001,D#,0.00939,0.0,124.95700000000001
7dQbXl1DHzsD8AXtiKC9Qt,Lalayo,33,228173,0,['Silent Sanctuary'],2009-01-01 00:00:00+00:00,0.573,A,0.00647,3.37e-05,105.065
5KvpIAORCusSooNFDpcPbI,Can't Help Falling in Love,46,132480,0,['Steven C'],2009-01-01 00:00:00+00:00,0.436,F,0.987,0.9109999999999999,115.46600000000001
0MzzUbsxedRyso4TQnTtXW,Rich Girl$,47,220560,0,['Down With Webster'],2009-01-01 00:00:00+00:00,0.633,F,0.00863,0.0,89.54700000000001
0vBpyfpW2lARGh3AZFtWRi,Heads Will Roll - A-Trak Remix Radio Edit,58,203920,0,"['Yeah Yeah Yeahs', 'A-Trak']",2009-01-01 00:00:00+00:00,0.6709999999999999,G#,0.0134,0.0547,132.05100000000002
1aIKdzKu2xGh6e0D7qPUnB,"Na, na, naaa",16,223813,0,"['No Name', 'Chinaski']",2009-01-01 00:00:00+00:00,0.626,F,0.49200000000000005,0.0,120.863
3MYR3iFoD0e90PgRbRoCru,Seasons,33,236333,0,['FRANCO'],2009-01-01 00:00:00+00:00,0.435,D#,0.00062,0.00155,164.80200000000002
6yVA14oVXpXNxTKbzO4YAj,Tuloy Pa Rin,35,263640,0,['Noel Cabangon'],2009-01-01 00:00:00+00:00,0.7170000000000001,G,0.7240000000000001,3.06e-06,110.057
7uBzUOwWQp6pLQEt7TdlGV,Провода (feat. МиГ29),30,222080,1,"['GUF', 'МиГ29']",2009-01-01 00:00:00+00:00,0.563,C,0.35,0.00121,90.27799999999999
5Bo9qEkAyr6y98pHHoKdie,The Saddest V. 2,34,277747,0,['Silent Sanctuary'],2009-01-01 00:00:00+00:00,0.39899999999999997,G,0.588,0.03,80.063
4WiIscpBgQFm5qIyjoH7M4,Heads Will Roll,56,221000,0,['Yeah Yeah Yeahs'],2009-01-01 00:00:00+00:00,0.562,G#,0.00018700000000000002,0.0939,132.009
78T9DulqSBWqkaxczcGBfk,Man On The Moon,60,210893,1,['Kid Cudi'],2009-01-01 00:00:00+00:00,0.649,C,0.638,2.71e-05,90.991
04vGO36ZMrGzqNjTVdopHL,Stroke Me,55,166480,1,['Mickey Avalon'],2009-01-01 00:00:00+00:00,0.736,C,0.0337,0.0,91.978
0JL71LVViWsdZ7ku5iLVHa,Rakovina,26,346307,0,['Karel Kryl'],2009-01-01 00:00:00+00:00,0.645,E,0.9670000000000001,0.00316,133.764
1h3FBdXNOjZEPPMZAR9p1h,Vítr,32,262747,0,['Lucie Vondrackova'],2009-01-01 00:00:00+00:00,0.475,G,0.0256,0.0,146.05
0fNCLvSVUEK7NTwhu5vk5B,Consider Me Gone,57,218053,0,['Reba McEntire'],2009-01-01 00:00:00+00:00,0.5870000000000001,G#,0.098,0.0,97.031
2gb31QyfSG3j2QBYPjmRMx,When I'm Small,44,249067,0,['Phantogram'],2009-01-01 00:00:00+00:00,0.643,A#,0.195,0.114,91.992
5K5LbSTVuKKe1KGMNfBgIW,Rock That Body,58,268840,0,['Black Eyed Peas'],2009-01-01 00:00:00+00:00,0.715,G,0.0172,8.39e-05,124.992
2fdMAIsNH4wY7RRda8aCfL,You and I,55,205240,0,['Wilco'],2009-01-01 00:00:00+00:00,0.71,G#,0.285,2.8699999999999996e-05,122.189
0rFpcfF0YfvFUYsl99Bw9d,Soundtrack 2 My Life,59,235627,1,['Kid Cudi'],2009-01-01 00:00:00+00:00,0.46399999999999997,A,0.465,1.57e-05,86.501
2rJWnAqSuLMls0KOv416Io,I Never Told You,58,233200,0,['Colbie Caillat'],2009-01-01 00:00:00+00:00,0.506,D#,0.171,0.0,144.07299999999998
6c6t0aQOtVUZTxRQTlEkZQ,If My Heart Was a House,46,245720,0,['Owl City'],2009-01-01 00:00:00+00:00,0.532,D#,0.00451,0.0,124.98100000000001
16XNk3bVCSHXN1rlwbXtHb,Birthday Sex,71,226507,0,['Jeremih'],2009-01-01 00:00:00+00:00,0.677,G,0.295,0.0,60.019
4CdPRndNTd010qP8vR0QrB,Here I Am To Worship - Be Still & Know: Instrumental Songs Of Worship Album Version,46,226627,0,['Worship Ensemble'],2009-01-01 00:00:00+00:00,0.72,D#,0.9390000000000001,0.9279999999999999,76.006
0mBREiw4ppCXccM7rsk2RC,Wavin' Flag,51,220520,0,"[""K'NAAN""]",2009-01-01 00:00:00+00:00,0.63,C,0.124,0.0,75.992
56jz6JfJcpY6NM3NdGafje,"This Is Me - From ""Camp Rock""",50,187733,0,"['Demi Lovato', 'Joe Jonas']",2009-01-01 00:00:00+00:00,0.465,C#,0.008740000000000001,0.0,90.95100000000001
7xoBJ4hih949Jeu5ZfzBai,Gimmie That Girl,58,185453,0,['Joe Nichols'],2009-01-01 00:00:00+00:00,0.5,D,0.205,0.000251,162.249
0DunM81kVGQ4RLKUiITwr0,Skladanka - Live,27,137653,0,"['Frantisek Nedved', 'Honza Nedved St.']",2009-01-01 00:00:00+00:00,0.502,A,0.922,0.0,121.102
76IvPzg39GSx9EIgujQgZn,I Could Sing Of Your Love Forever - Be Still & Know: Instrumental Songs Of Worship Album Version,45,231840,0,['Worship Ensemble'],2009-01-01 00:00:00+00:00,0.626,D,0.958,0.71,83.031
7eM88DF4yL4hpNnB6oJLnD,Catch Me,54,190000,0,['Demi Lovato'],2009-01-01 00:00:00+00:00,0.289,E,0.491,0.0,185.425

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  9593.000000  9.593000e+03  9593.000000   9593.000000   9593.000000       9593.000000  9593.000000
mean     37.585323  2.389363e+05     0.058689      0.593954      0.307853          0.058635   122.624547
std      14.385721  8.991326e+04     0.235053      0.153031      0.296956          0.195232    28.706294
min       0.000000  2.865600e+04     0.000000      0.000000      0.000002          0.000000     0.000000
25%      29.000000  1.980530e+05     0.000000      0.496000      0.037600          0.000000    99.977000
50%      38.000000  2.305070e+05     0.000000      0.603000      0.211000          0.000002   123.081000
75%      47.000000  2.686000e+05     0.000000      0.705000      0.538000          0.000440   139.979000
max      83.000000  4.696690e+06     1.000000      0.975000      0.996000          1.000000   216.618000
