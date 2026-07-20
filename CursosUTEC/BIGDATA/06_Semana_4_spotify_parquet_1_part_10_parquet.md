---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.10
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.10.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.10.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.10.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 10591 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 10591 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
5XfHNrdomVBNxUI0iRztic,Будильник,45,204062,0,['Egor Kreed'],2015-01-01 00:00:00+00:00,0.7829999999999999,B,0.0933,0.0,124.03399999999999
4IVgXhwBD357hgHjxVDfzq,Fáum Borgað (feat. Blaz Roca & Joe Frazier),19,237434,0,"['Herra Hnetusmjör', 'Blaz Roca', 'Joe Frazier']",2015-01-01 00:00:00+00:00,0.8009999999999999,G,0.00999,0.0,97.93700000000001
4ArRDOfRo90VHzWrsXi0q6,Океан,39,217500,1,['Scriptonite'],2015-01-01 00:00:00+00:00,0.474,A#,0.815,0.0,89.29
6ofZUiViaPyY57Mv9ZaXiV,Абсолютно всё,44,188571,0,"['Mot', 'Bianka']",2015-01-01 00:00:00+00:00,0.526,C#,0.0958,0.0,153.921
3FTCuGP7OhGdXzfisLEaLK,Þangað Til (feat. Joe Frazier),20,243692,0,"['Herra Hnetusmjör', 'Joe Frazier']",2015-01-01 00:00:00+00:00,0.768,C,0.0306,0.0,130.005
6B0XqIWl17SjUKtln7kuxF,Вниз,39,224167,1,['Scriptonite'],2015-01-01 00:00:00+00:00,0.515,D,0.0905,0.000721,60.577
6WE7yCg72facr7GKQD6CA6,Time Machine,59,255467,0,['Six Part Invention'],2015-01-01 00:00:00+00:00,0.591,C#,0.293,0.0,95.14
0JzwzRDkwZr8s1WRfNgUqA,Till I Met You,59,240065,0,['Angeline Quinto'],2015-01-01 00:00:00+00:00,0.452,D,0.6890000000000001,2.27e-06,139.833
6mE7cjA9svHRq3k63FAvYn,Right Here,51,220160,0,['Jess Glynne'],2015-01-01 00:00:00+00:00,0.8059999999999999,G,0.0294,1.34e-05,120.02799999999999
2MuxsihiTrMMkxsIQSj8gc,Hvítur Bolur Gullkeðja,20,220588,0,['Herra Hnetusmjör'],2015-01-01 00:00:00+00:00,0.802,C#,0.0118,0.0,135.965
5F5n3IuvLFyNx6f5h2jn0E,20ogeitthvað,19,233546,0,['Úlfur Úlfur'],2015-01-01 00:00:00+00:00,0.77,A,0.0854,0.0,149.988
0UqBQNPLy0txwTOfTGZMXS,Бумажки,41,322250,1,"['Scriptonite', 'Юрик Четверг']",2015-01-01 00:00:00+00:00,0.7040000000000001,F#,0.14,5.67e-06,105.92399999999999
5PLbqbPQP42plJ6VBHjMRH,La La,18,193774,0,['Herra Hnetusmjör'],2015-01-01 00:00:00+00:00,0.5479999999999999,A#,0.0573,0.0,96.97200000000001
5mrWGeEdZqgOmsrMw5exJy,Skusme To V Mieri,29,346293,0,['Majk Spirit'],2015-01-01 00:00:00+00:00,0.541,C#,0.652,0.0,140.02700000000002
3BMMHl6h8VkI4lW9jKSuEL,100 поцелуев,40,155729,1,['Scriptonite'],2015-01-01 00:00:00+00:00,0.539,C#,0.19899999999999998,0.00322,119.35799999999999
1CD0XNh1byEW9NKPtpFTAC,Лёд,41,350687,0,"['Basta', 'Smoky Mo', 'Scriptonite']",2015-01-01 00:00:00+00:00,0.606,C#,0.545,0.0,77.498
1F1kllba7qMoii2hswILYw,Оставь это нам,40,100110,1,['Scriptonite'],2015-01-01 00:00:00+00:00,0.742,C#,0.0368,0.0,91.039
1ABGjM1kc8P5Vj7X6TkL40,Ťahal dedko repku,25,1218933,0,"['Mária Podhradská', 'Richard Čanaky', 'Spievankovo']",2015-01-01 00:00:00+00:00,0.6940000000000001,D,0.521,0.0,105.096
5egyjW2qZwEtCLfS0Ci4Nl,Selfie,18,215286,0,['Herra Hnetusmjör'],2015-01-01 00:00:00+00:00,0.815,F#,0.127,0.0,97.958
39PnZjQ73g07oY2NaAOtxZ,Желаю,42,280398,0,['Chestnyi'],2015-01-01 00:00:00+00:00,0.657,E,0.09699999999999999,0.0,149.954
4zDl6nT5P5tPeXxG8LRGtS,Way Down We Go,18,219289,0,['KALEO'],2015-01-01 00:00:00+00:00,0.505,A#,0.625,0.00028700000000000004,162.621
2c2sBxXAj2VXTTFN2EWdMq,Стиль - Другая версия,39,407197,1,"['Scriptonite', 'ATL']",2015-01-01 00:00:00+00:00,0.5489999999999999,C,0.152,2.58e-05,123.96700000000001
7AQLbnuuyPzy22MOEmeetH,暗湧,41,261813,0,['Faye Wong'],2015-01-01 00:00:00+00:00,0.325,A#,0.898,0.0541,181.1
0K2UkduBJxjuNYLOFhpwHB,再見只是陌生人,53,251691,0,['Ada Zhuang'],2015-01-01 00:00:00+00:00,0.625,F,0.0134,0.0,82.00399999999999
50MRAYaWCgWqUcefowkaOV,Rozeznávám,33,249027,0,['Richard Muller'],2015-01-01 00:00:00+00:00,0.249,C,0.664,2.51e-06,52.407
1AVYznIek3SoK9xSAsnAuH,放過自己,50,249041,0,['Ada Zhuang'],2015-01-01 00:00:00+00:00,0.598,C,0.102,0.0,120.001
7G8lsE1TP7zl4stkae3b0V,Надо ли,43,200335,0,['Egor Kreed'],2015-01-01 00:00:00+00:00,0.5589999999999999,A,0.34,0.0,87.959
6rup3MnFORKLyVwn10k2uO,Row Row Your Boat (Merrily),58,52250,0,"[""Children's Music""]",2015-01-01 00:00:00+00:00,0.818,A#,0.573,0.000667,102.24799999999999
4eanIaPbj0SBmvVHrym7E5,Draumahöll,21,166907,0,"['Lára Sóley', 'Stefán Örn Gunnlaugsson']",2015-01-01 00:00:00+00:00,0.34,A,0.96,2.12e-06,92.822
4quGalr9t5YguUgVuXsCJt,Tvær plánetur,23,308779,0,['Úlfur Úlfur'],2015-01-01 00:00:00+00:00,0.703,F#,0.08900000000000001,0.0,140.05200000000002
2dC3kRI8ng4P9LOH9nhdTG,Dagný,23,199088,0,"['Elly Vilhjálms', 'Vilhjálmur Vilhjálmsson']",2015-01-01 00:00:00+00:00,0.276,G,0.667,0.0,105.32700000000001
0jLVhgKWMo0ygckGg50dBR,El R 15,44,183252,0,['Los Reales del Valle'],2015-01-01 00:00:00+00:00,0.7879999999999999,C#,0.409,0.0032600000000000003,122.529
318WVDtjykBxdXTq5nlg0G,Los Sabanales,44,265172,0,['La Banda Tropikal de Vallenar'],2015-01-01 00:00:00+00:00,0.787,B,0.159,1.6e-05,120.055
7tAsEaXdXgCiwUdBZ77Dwq,En un Largo Tour,43,262293,0,['Sol y Lluvia'],2015-01-01 00:00:00+00:00,0.638,B,0.29600000000000004,1.09e-05,110.00399999999999
2lSQEYpE4SizYH6CjkN1SI,За спиной,39,251063,0,['Chestnyi'],2015-01-01 00:00:00+00:00,0.5489999999999999,A,0.000109,0.0,75.959
1THQIMBDAqSqEueweFKWaX,Paloma Blanca,42,239537,0,['La Banda Tropikal de Vallenar'],2015-01-01 00:00:00+00:00,0.8140000000000001,C,0.161,0.0,120.008
49SdPAp9ligptoAMfZHnYc,El Chofer,41,280218,0,['La Banda Tropikal de Vallenar'],2015-01-01 00:00:00+00:00,0.893,F#,0.13699999999999998,1.4499999999999998e-05,120.03
5lM4GgQIX6IHCC7WgNW8XW,La Guitarra y la Mujer,40,191890,0,['La Banda Tropikal de Vallenar'],2015-01-01 00:00:00+00:00,0.8140000000000001,A,0.138,0.0,118.00200000000001
4RYtrtRgTV4BKdGJMgz5ez,Лям,36,276708,1,['Scriptonite'],2015-01-01 00:00:00+00:00,0.493,C#,0.273,0.0,108.417
6RBel04CNvcZhod6VBbvyn,Intro / Outro,42,73718,0,['Damn Whøre'],2015-01-01 00:00:00+00:00,0.424,G,0.522,0.000343,109.845

Resumen numérico:
         popularity   duration_ms      explicit  danceability  acousticness  instrumentalness         tempo
count  10591.000000  1.059100e+04  10591.000000  10591.000000  10591.000000      10591.000000  10591.000000
mean      37.818997  2.306743e+05      0.100085      0.595792      0.300305          0.101745    121.259240
std       20.042966  1.350272e+05      0.300127      0.159397      0.302536          0.262220     28.766055
min        0.000000  3.000000e+04      0.000000      0.000000      0.000000          0.000000      0.000000
25%       28.000000  1.893465e+05      0.000000      0.496000      0.032200          0.000000     98.988500
50%       42.000000  2.208250e+05      0.000000      0.607000      0.187000          0.000003    122.003000
75%       52.000000  2.562515e+05      0.000000      0.710000      0.515000          0.001500    137.991000
max       87.000000  4.737458e+06      1.000000      0.977000      0.996000          0.999000    215.511000
