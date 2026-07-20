---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.9
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.9.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.9.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.9.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 11252 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 11252 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
1uuyATSrgeVURyWHy68VxX,Just One Day,45,212120,0,['Mighty Oaks'],2014-01-01 00:00:00+00:00,0.602,D#,0.19899999999999998,0.000365,101.934
4oFF5OJrbT4sUyO4mF9PLe,Dicht bij mij,39,254253,0,['Bart Peeters'],2014-01-01 00:00:00+00:00,0.5660000000000001,A,0.8440000000000001,0.0005780000000000001,83.87100000000001
1FQyRDFRpIcUgWTEvICDy6,今生今世,30,105533,0,['Leslie Cheung'],2014-01-01 00:00:00+00:00,0.5529999999999999,C,0.951,5.539999999999999e-05,129.471
3DhD3hWyou0QluBBTSiBC5,No Digas Nada (Déjà Vu),58,213467,0,['Cali Y El Dandee'],2014-01-01 00:00:00+00:00,0.493,B,0.253,0.0,176.063
0OD1Y1Ok71DsXHRUh1HaOF,心內的話,31,221572,0,['玖壹壹'],2014-01-01 00:00:00+00:00,0.639,G,0.13699999999999998,0.0,85.04299999999999
5p5jXve0CXP3Za6xY2fylF,Crazy Stupid Love,51,225150,1,"['Cheryl', 'Tinie Tempah']",2014-01-01 00:00:00+00:00,0.852,B,0.0015400000000000001,0.000908,120.596
6pCxwehCUsSLBwk3DcL5yy,Maja Tanz,53,179760,0,['Die Biene Maja'],2014-01-01 00:00:00+00:00,0.838,G,0.485,0.0,122.99799999999999
1inc0n0zjlx7gopyz8sxWx,Sembilu,44,321733,0,['Ella'],2014-01-01 00:00:00+00:00,0.584,A,0.5379999999999999,0.00403,114.281
7m6QW6B5iT4R1x0f7wVplQ,"下個轉彎是你嗎(電視劇""一見不鍾情""片尾曲)",35,284412,0,['Rainie Yang'],2014-01-01 00:00:00+00:00,0.42200000000000004,C#,0.774,0.0,137.56
0Ci7Ux6qni6sp4p6LZzliI,一比鴨鴨,32,106710,0,['MOMO家族'],2014-01-01 00:00:00+00:00,0.8909999999999999,F,0.39,0.0,134.961
26w9Ok099x8Ov0Dyob7xRJ,從未到過的地方,43,233773,0,['Cyndi Wang'],2014-01-01 00:00:00+00:00,0.52,C,0.75,0.0,125.68299999999999
2LeLfY4Z2ZG5LqmslJBY7K,Tu Muñeca,35,219053,0,['Dulce'],2014-01-01 00:00:00+00:00,0.7290000000000001,E,0.322,0.000127,81.37899999999999
6sXoEfM3EgF3wTN0OOkLw2,天使的指纹,37,245806,0,['Stefanie Sun'],2014-01-01 00:00:00+00:00,0.392,A,0.835,0.0,129.495
5V2oYvfPrbIFeRRFs3qFQN,"Slå Dig Fri - Från ""Frost""/Svenskt Original Soundtrack",52,224040,0,['Annika Herlitz'],2014-01-01 00:00:00+00:00,0.607,G#,0.816,0.0,137.02
7s5M2pUlLri4yxoDOTqXFq,Cuando Te Enamoras,45,211464,0,['Orquesta Candela'],2014-01-01 00:00:00+00:00,0.602,C,0.353,0.0,90.113
5B0qPMGraEoPtDSc0hvZ3d,Najednou - Czech Version,34,222973,0,['Monika Absolonova'],2014-01-01 00:00:00+00:00,0.583,G#,0.7809999999999999,0.0,136.977
7Fbisz5waRkyN0xWeASqQ8,Megbántottak REMIX,29,328160,0,['Hip Hop Boyz'],2014-01-01 00:00:00+00:00,0.8140000000000001,G,0.00048300000000000003,0.00717,133.984
5no8GE6YS8oq79HyJc3GcX,Kötél - Remix,30,336640,1,"['Mr.Busta', 'AK26', 'Beerseewalk', 'Essemm', 'Fura Csé']",2014-01-01 00:00:00+00:00,0.8420000000000001,A#,0.26,0.0,133.931
02qoqHv29LQCBw1mymxlY5,Fakkin fin,49,242533,0,['Labyrint'],2014-01-01 00:00:00+00:00,0.705,F#,0.17,0.0,165.96
58oT9wQPpFfQnq5hGBppbE,La Belle Epoque,49,238000,0,['kent'],2014-01-01 00:00:00+00:00,0.505,F#,0.000472,0.00366,158.034
71PmZqBXH0RUETqxpwlV0w,Style,60,231000,0,['Taylor Swift'],2014-01-01 00:00:00+00:00,0.598,D,0.00256,0.00143,95.021
14ZZR92YmYIIVhOi6h0MOg,Mooie Dag,55,145662,0,['Jayh'],2014-01-01 00:00:00+00:00,0.691,C#,0.10300000000000001,0.0,175.801
6WmLxgA4Qfw5dvZs96TEUh,"Kravy, kravy",26,266093,0,"['Zdeněk Svěrák', 'Jaroslav Uhlír', 'Sedmihlasek']",2014-01-01 00:00:00+00:00,0.599,C,0.752,0.0,111.05799999999999
4P7Nn5zvwXmLMCBOUgeJ3V,Precis som du vill,48,211867,0,['Jens Hult'],2014-01-01 00:00:00+00:00,0.489,D,0.5870000000000001,0.0,136.999
1k7askm0LAgXVquR5EpXL6,給親戚看見我一個人食吉野家,35,155533,0,['my little airport'],2014-01-01 00:00:00+00:00,0.6729999999999999,A,0.7440000000000001,0.00011100000000000001,94.544
27mT3JdR3sRJyiMBFHdhB4,Waiting Game,60,207719,0,['BANKS'],2014-01-01 00:00:00+00:00,0.33399999999999996,F,0.6579999999999999,0.00014,129.127
2Tuyb61K4eKoq0oaFJB7c0,Kruhy,31,255683,0,"['Lipo', 'Yanna']",2014-01-01 00:00:00+00:00,0.38799999999999996,F,0.0295,0.0,179.94799999999998
7nDoBWDvf02SyD8kEQuuPO,Bottoms Up,51,221227,0,['Brantley Gilbert'],2014-01-01 00:00:00+00:00,0.474,G,0.113,0.0,170.00599999999997
4lYf4CJHwbf5QgC8buafrw,January 2014 - Mixed by Sean Jay Dee - Released Every First Day of The Odd Months of The Year - Continuous Mix,0,3543738,0,['Sean Jay Dee'],2014-01-01 00:00:00+00:00,0.7859999999999999,C,0.0014,0.6809999999999999,124.007
0YcR6q80tWpaCl3e218vGz,"不散,不見",35,230696,0,['Karen Mok'],2014-01-01 00:00:00+00:00,0.45899999999999996,D#,0.9690000000000001,1.8100000000000003e-05,75.62
1srMlzGV9Zjdvhfiv53m3b,För Första Gången Nånsin,46,224293,0,"['Annika Herlitz', 'Mimmi Sandén']",2014-01-01 00:00:00+00:00,0.456,C,0.902,0.0,98.462
5CYJB5Md92kvcrZ4lJDALY,The Spark,60,240893,0,"['Afrojack', 'Spree Wilson']",2014-01-01 00:00:00+00:00,0.6509999999999999,B,0.152,0.0,126.051
4Dn7e19E79oYGEyDftdxdq,Cechacek a totacek,27,274750,0,['XINDL X'],2014-01-01 00:00:00+00:00,0.807,G,0.513,0.0,126.051
4cZqNHlTkf6yWJSWDw2da0,Ayat Kursi,48,52533,0,['Syekh Mishary Rasyid'],2014-01-01 00:00:00+00:00,0.289,G#,0.23399999999999999,0.19699999999999998,172.201
2Dz8KeCYs9awlwUJStJlmh,Classic,47,175427,0,['MKTO'],2014-01-01 00:00:00+00:00,0.72,C#,0.0384,0.0,102.071
4ou16rn6sJwL5uwGfEL0IE,Hangover,45,221227,0,['Alestorm'],2014-01-01 00:00:00+00:00,0.634,F#,0.00413,0.0,134.985
0lKNUoW2e07gYBARPe97hw,Surat Al Qiyamah,47,248200,0,['Muhammad Thaha'],2014-01-01 00:00:00+00:00,0.49200000000000005,G#,0.9690000000000001,0.0,128.139
2tKOIBLJ2j384tnunmmKi7,From Eden,52,222427,0,['Hozier'],2014-01-01 00:00:00+00:00,0.479,C,0.43200000000000005,4.0600000000000004e-05,106.90899999999999
5OXwaPptL6NFHFJj48c2QT,Higher,50,198671,0,"['The Saturdays', 'Flo Rida']",2014-01-01 00:00:00+00:00,0.6679999999999999,A#,0.0852,0.0,117.022
1YPJ4wKWLIsAZ6kjkat1zu,I Don't Care,48,240657,1,['Cheryl'],2014-01-01 00:00:00+00:00,0.703,G#,0.00041500000000000006,7.64e-06,117.005

Resumen numérico:
         popularity   duration_ms      explicit  danceability  acousticness  instrumentalness         tempo
count  11252.000000  1.125200e+04  11252.000000  11252.000000  11252.000000      11252.000000  11252.000000
mean      36.800036  2.353230e+05      0.084163      0.598888      0.286852          0.094891    122.583300
std       18.664666  1.352505e+05      0.277644      0.153693      0.297580          0.249370     27.905352
min        0.000000  2.265500e+04      0.000000      0.000000      0.000000          0.000000      0.000000
25%       28.000000  1.939822e+05      0.000000      0.501000      0.025900          0.000000     99.990000
50%       40.000000  2.246335e+05      0.000000      0.608000      0.169000          0.000003    124.978000
75%       49.000000  2.617532e+05      0.000000      0.709000      0.503000          0.001640    139.458000
max       86.000000  5.042185e+06      1.000000      0.985000      0.996000          0.999000    217.648000
