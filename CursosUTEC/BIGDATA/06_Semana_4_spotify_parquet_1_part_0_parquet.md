---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.0
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.0.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.0.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.0.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 5728 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 5728 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
2fASnKww9WIi2YMp8s7sDi,Sueño,37,251480,0,['Fonseca'],2005-01-02 00:00:00+00:00,0.511,F,0.0841,2.8100000000000002e-05,114.025
2j7mtIlWmFfvodCFAAYd3E,Confiésame,39,243000,0,['Fonseca'],2005-01-02 00:00:00+00:00,0.7,F#,0.0813,0.0,112.038
2lGNHYGWS80iu0EJDyqsHw,Pulkstens deviņus jau zvana,17,173907,0,['Prego'],2005-01-02 00:00:00+00:00,0.381,F,0.953,0.0,120.822
1BI6ciDl653mn2Oip8KUID,Melanholiskais valsis,13,234493,0,['Prego'],2005-01-02 00:00:00+00:00,0.535,A,0.33299999999999996,1.15e-05,169.968
7oVJpmVnFYtNZA0TQmF2OX,Sobrenatural - Ao Vivo,45,219133,0,['Jeito Moleque'],2005-01-03 00:00:00+00:00,0.475,A,0.366,0.0,159.799
1r4D2L2VxgmpyQPDyC4iC1,תחרות כלבים,42,277867,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.6459999999999999,F#,0.156,7.42e-05,112.02
65ZJCO6yTbxqU98xXJhEHT,Meu Jeito Moleque - Ao Vivo,44,162880,0,['Jeito Moleque'],2005-01-03 00:00:00+00:00,0.486,C,0.539,0.0,83.26
6MoyiRPmFwVnkhaZhkyksG,Pickin' Wildflowers,52,185920,0,['Keith Anderson'],2005-01-03 00:00:00+00:00,0.561,G#,0.0353,0.0,152.089
6VcsrxdEnAMC4u6u9ssjse,Para Tudo - Ao Vivo,42,275600,0,['Jeito Moleque'],2005-01-03 00:00:00+00:00,0.31,F#,0.41600000000000004,3.9e-06,145.33100000000002
0AktIva3815qwp5QTmo6g3,יש לנו את כל הזמן,20,233347,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.434,C,0.8,0.0059299999999999995,107.535
1DwVWibPBDTBNLCuzV4QlU,Me Faz Feliz - Ao Vivo,45,175280,0,['Jeito Moleque'],2005-01-03 00:00:00+00:00,0.604,C,0.149,0.0,103.71
3nwdXST6RMJd25rM7LpDqX,טיפה של אור,20,266067,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.529,C,0.469,0.0656,150.07399999999998
6ZVk3PvgtXq8UpJNYR0C5t,בבית,17,221333,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.61,G,0.491,0.000798,111.961
19pvG8lf5oY6XGX81Xe3vp,מיתר,17,227067,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.76,F#,0.196,0.00484,105.95299999999999
5psgd9N2kHquqYPy8EgDdg,בשבילך,17,223800,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.6459999999999999,B,0.0949,0.542,114.023
52qZx4Y33kGfQrbO4BzoQd,Pali monos mou milo - Live,18,127853,0,['Giorgos Alkaios'],2005-01-03 00:00:00+00:00,0.504,A,0.5920000000000001,0.0011,97.633
3ncNTFdLjuXOmp1Jdt7xwW,פקק תנועה,22,221107,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.322,E,0.187,0.00022,179.917
56CuqxHdDCQjaQjkunYwO8,Man müsste noch mal 20 sein,42,265253,0,['Brings'],2005-01-03 00:00:00+00:00,0.61,F#,0.11800000000000001,0.0,137.997
1JISGjYOQoiJe6xc7CWnQo,Hoje A Noite É Nossa - Ao Vivo,40,206920,0,['Jeito Moleque'],2005-01-03 00:00:00+00:00,0.455,B,0.19399999999999998,1.86e-05,104.919
0q7x5rssXSdckcZMXt77fX,את שקט,33,349000,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.67,D,0.539,0.0793,124.01799999999999
70wHJTH7M64u5NBrdKBKFl,Eu Nunca Amei Assim - Ao Vivo,42,230160,0,['Jeito Moleque'],2005-01-03 00:00:00+00:00,0.48,G,0.325,0.0,75.80199999999999
0WkKSJiOHumAHleapC5PKt,מתנות,33,211733,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.5660000000000001,A,0.0376,5.9699999999999994e-05,111.95700000000001
2lTrhZa4tJFLizwdob9lYa,המון אנשים,18,219107,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.256,E,0.934,0.095,140.399
0ltdRHucjtDnq8ifRleIEo,שוב אני לבד,20,250467,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.703,A,0.14,0.033,136.03
34nOHhugejZrvZfCqBLsZF,Una Fan Enamorada,14,300213,0,['L´Autentika'],2005-01-03 00:00:00+00:00,0.495,A#,0.344,0.0,183.977
491wIDZNOChYOrX0QYig9z,Amor Eterno - Ao Vivo,42,268160,0,['Jeito Moleque'],2005-01-03 00:00:00+00:00,0.353,F#,0.386,1.85e-05,99.70299999999999
2EifUNgHPoZHa22ZltRHKl,הזאב והאיילה,35,214400,0,['Eviatar Banai'],2005-01-03 00:00:00+00:00,0.565,C,0.589,0.0362,135.96
26W2s4olnidTVYt4UklfqS,Yeşil Ördek Gibi,40,242173,0,['Müslüm Gürses'],2005-01-04 00:00:00+00:00,0.659,E,0.617,0.079,119.976
70SEB2Lmmkpo5oRtyHksrY,You're the Inspiration,54,246880,0,['Peter Cetera'],2005-01-04 00:00:00+00:00,0.645,A#,0.0834,0.0,143.48
1uybEGNH2GIvNdzGB7L2Qj,(I Wanna Take) Forever Tonight,58,274453,0,['Peter Cetera'],2005-01-04 00:00:00+00:00,0.601,C#,0.601,0.0009660000000000001,105.95299999999999
49mm2fTKdGkFAJRAM12UuD,Flower of Scotland,31,224373,0,['The Wolfe Tones'],2005-01-05 00:00:00+00:00,0.312,G,0.161,0.0,163.96
4k4CVH4QLpQHXREFWdidnE,Galtee Mountain Boy,34,180133,0,['The Wolfe Tones'],2005-01-05 00:00:00+00:00,0.501,F,0.612,0.0,157.08100000000002
1SfWhQYidQRzHFGynzSzuR,Pigface,33,221747,0,['Greyhoundz'],2005-01-05 00:00:00+00:00,0.37200000000000005,C,0.0118,0.39899999999999997,104.02
4YVbLto1w4dEKXjuZxlGRQ,雙棲動物,43,275800,0,['Tanya Chua'],2005-01-05 00:00:00+00:00,0.34600000000000003,A#,0.674,0.0,134.66
27doZ3PBRnbEtoI3qRNJv5,原點,35,250147,0,"['Stefanie Sun', 'Tanya Chua']",2005-01-05 00:00:00+00:00,0.47,F#,0.39399999999999996,0.0,129.678
1mnELnVixuWR2nTyUJqaTx,下一次愛情來的時候,35,258840,0,['Tanya Chua'],2005-01-05 00:00:00+00:00,0.485,F,0.34700000000000003,0.0,75.991
2jzdlM8TIb4SSfCjDuWYPf,Arcadia [ASOT 182] - Original Mix,7,174813,0,['Gabriel & Dresden'],2005-01-06 00:00:00+00:00,0.629,B,0.0355,0.902,131.826
2cSG5Wpfvk43fF4VtiZs9G,Mercury [ASOT 182] - Original Mix,5,82813,0,"[""John O'Callaghan"", 'Mannix']",2005-01-06 00:00:00+00:00,0.446,A,9.89e-05,0.932,139.071
7IAoa1fobj9NrK8ikxLG47,Perfect Wave [ASOT 182] - Original Mix,6,155074,0,"['Peter Martin', 'Anthanasia']",2005-01-06 00:00:00+00:00,0.613,D,0.0296,0.914,136.06
6Jy8ZVg25HOdpYeP546lHG,Not Even Winds [ASOT 182] - Original Mix,6,126730,0,"['O.C.', 'Nick Beman']",2005-01-06 00:00:00+00:00,0.6409999999999999,G#,0.000724,0.429,128.776

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  5728.000000  5.728000e+03  5728.000000   5728.000000   5728.000000       5728.000000  5728.000000
mean     36.880936  2.452433e+05     0.043471      0.586198      0.309832          0.060784   122.358014
std      14.140177  8.425781e+04     0.203932      0.160113      0.300644          0.199429    29.319362
min       0.000000  3.158600e+04     0.000000      0.070100      0.000000          0.000000    46.755000
25%      28.000000  2.041132e+05     0.000000      0.479000      0.033975          0.000000    98.581750
50%      37.000000  2.395735e+05     0.000000      0.593000      0.210000          0.000004   121.518000
75%      46.000000  2.789300e+05     0.000000      0.702000      0.542250          0.000669   140.027250
max      87.000000  2.539418e+06     1.000000      0.974000      0.996000          0.980000   218.061000
