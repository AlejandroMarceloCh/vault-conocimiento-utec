---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.8
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.8.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.8.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.8.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 10557 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 10557 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
11qPEHhP5IdSl0lRkLy6Cs,Bláu augun þin,28,185017,0,['Hljómar'],2013-01-01 00:00:00+00:00,0.33799999999999997,D,0.76,0.0,173.447
7Kv9Lxent75sA3OaG78s93,Going Home,17,292893,0,['Ásgeir'],2013-01-01 00:00:00+00:00,0.5920000000000001,G#,0.723,0.551,180.08599999999998
7FZTYY0QStoZeDKPaQuf6h,Kæri vinur,17,224258,0,"['Jón Jónsson', 'Björgvin Halldórsson']",2013-01-01 00:00:00+00:00,0.628,F,0.382,0.0,85.02799999999999
0493JEOPHEvR91vbkzkcBx,Samferða,16,245992,0,['Mannakorn'],2013-01-01 00:00:00+00:00,0.389,D,0.42200000000000004,6.72e-06,175.77
4iQslTaYr5Z90kq7YUJmSI,Resistiré,40,250600,0,['David Bolzoni'],2013-01-01 00:00:00+00:00,0.447,F,0.13699999999999998,0.0,184.018
2ClinwPLpa9NOmytCGeKTo,Otpusti I zabud,38,222547,0,['Anna Buturlina'],2013-01-01 00:00:00+00:00,0.42100000000000004,F,0.81,2.34e-06,136.925
0SK9wxN40P6jlcMfTSAe0V,Glory And Gore,62,210738,0,['Lorde'],2013-01-01 00:00:00+00:00,0.6890000000000001,C#,0.285,0.0,143.946
0ujjgOP4F3fqAX8oycq68r,Pretty Boy Floyd,16,227370,0,['KALEO'],2013-01-01 00:00:00+00:00,0.49200000000000005,A#,0.0206,1.01e-05,126.469
46FcSuBfzsRKrVuk4kWU6N,Belle Hélène - Rapversie,40,185760,0,['The Opposites'],2013-01-01 00:00:00+00:00,0.579,F#,0.0204,0.6509999999999999,139.958
2Hy2SeWdfoA597eoRBNWbN,Mamma þarf að djamma,31,194119,0,"['Jóhanna Guðrún', 'Baggalútur']",2013-01-01 00:00:00+00:00,0.742,D,0.396,0.0005740000000000001,129.983
0eehHRQY2nlimtLjCI9xRf,We Come Running,57,247507,0,['Youngblood Hawke'],2013-01-01 00:00:00+00:00,0.55,A#,0.000323,0.00391,124.97
5C2piF5AjMt4pCh0sgpeUB,Nunca Voy A Olvidarte,52,300640,0,['Cristian Castro'],2013-01-01 00:00:00+00:00,0.546,D#,0.258,1.4000000000000001e-05,156.121
1vSEwZtoQA0sJxkOgF7MtG,Falling,52,257813,0,['HAIM'],2013-01-01 00:00:00+00:00,0.743,D,0.0792,7.75e-05,111.98
7MbcAQi7NN5ZYqpBHhyEBv,Νous Ithinon,23,232307,1,"['Anser', 'Eversor']",2013-01-01 00:00:00+00:00,0.657,C#,0.22699999999999998,0.0,93.009
4ORLwG8RZWVRyGU68EEALc,Anemodarmena Ipsi,31,241384,0,['Katy Garbi'],2013-01-01 00:00:00+00:00,0.5589999999999999,C#,0.46299999999999997,0.0,83.001
5Gbc4h1rpPQgBT3kywWkTG,小城故事,39,158360,0,['Teresa Teng'],2013-01-01 00:00:00+00:00,0.47700000000000004,C,0.72,0.00349,80.032
5NIVxqYr8oWZnb9hJf8VtR,For Første Gang på Lenge 2,35,149827,0,"['Lisa Stokke', 'May Kristin Kaspersen']",2013-01-01 00:00:00+00:00,0.47700000000000004,A,0.912,0.0,98.962
5a3EgPtbUrbmutCu3xlBWq,Hokksund,34,202293,0,['Broiler'],2013-01-01 00:00:00+00:00,0.736,G,0.11599999999999999,0.0365,135.059
3tzM7quInY8UcM9bxp67yC,Samhradh Samhradh,35,356253,0,['The Gloaming'],2013-01-01 00:00:00+00:00,0.522,A#,0.977,0.00279,74.538
1JpM0DYtVF2YKeEJ1D6rIG,Het Is Een Nacht / Love You More - Live @ PSV Stadion Eindhoven June 2013,39,239200,0,"['Guus Meeuwis', 'Racoon']",2013-01-01 00:00:00+00:00,0.266,C#,0.8390000000000001,0.0,77.586
2xannpLNAjth1Hfzp3Qwtq,Ástardúett,16,180094,0,"['Guðrún Gunnarsdóttir', 'Egill Ólafsson']",2013-01-01 00:00:00+00:00,0.6659999999999999,D,0.809,0.0,82.822
6q6Y2okPnlQsgom2212dd5,Glass House,15,254491,0,['KALEO'],2013-01-01 00:00:00+00:00,0.40399999999999997,C,0.00249,0.0104,97.95700000000001
5O3CHdJL1LsVpjv9mUTcyS,Það styttir alltaf upp,27,288867,0,['Ragnar Bjarnason'],2013-01-01 00:00:00+00:00,0.742,E,0.716,0.000204,92.965
3Ip9paW5KZ3xy1l1tpor63,Slapeloze Nachten,41,212224,0,['The Opposites'],2013-01-01 00:00:00+00:00,0.8170000000000001,G#,0.39299999999999996,0.0005009999999999999,111.98899999999999
5cBx2v7XJSErfesDmgNtr2,Liebe,62,195416,0,['Sido'],2013-01-01 00:00:00+00:00,0.522,F#,0.0574,0.0,171.965
6rpAHfcP5vLAbqnSXUcp76,On That Day,16,227853,0,['Ásgeir'],2013-01-01 00:00:00+00:00,0.586,G,0.904,0.0095,99.986
3Mdwx1F4O7LtvG9e1lspvM,少女的祈禱,29,248360,0,['Hins Cheung'],2013-01-01 00:00:00+00:00,0.5820000000000001,A#,0.927,3.78e-05,114.434
3KZw9g7PNBBx66sHNqme6Z,What Are You Listening To?,62,245920,0,['Chris Stapleton'],2013-01-01 00:00:00+00:00,0.563,A#,0.19,4.71e-05,161.893
3B0irDyS69y5eAz15xV2Ee,Wake Me Up,51,247427,0,['Avicii'],2013-01-01 00:00:00+00:00,0.532,D,0.00375,0.00123,124.084
17uERbe9k05hhocvXfTuux,Taxidi Stin Vrochi,31,184293,0,['Eleftheria Eleftheriou'],2013-01-01 00:00:00+00:00,0.535,E,0.457,0.0,112.118
48ubkDBO9GAFRkn3hXFHVt,Sergels torg,54,226520,0,['Veronica Maggio'],2013-01-01 00:00:00+00:00,0.483,C,0.00889,0.0374,138.986
4NVNapccSX7E5JLiW0uQEy,Pound Cake / Paris Morton Music 2,63,432853,1,"['Drake', 'JAY-Z']",2013-01-01 00:00:00+00:00,0.52,D,0.139,1.13e-05,164.083
2cYEzAVCmq5jfsxTX9OoJO,Til eru fræ,14,226813,0,['Helgi Björnsson'],2013-01-01 00:00:00+00:00,0.18,G,0.943,0.353,89.17299999999999
5ngydCLbzCEdtu8SEOXhPU,All Me,62,271573,1,"['Drake', '2 Chainz', 'Big Sean']",2013-01-01 00:00:00+00:00,0.6679999999999999,C#,0.0703,0.0,122.014
5q4X8V0KO9rBQYcjT7oyri,Tankstation,39,246356,0,['Ronnie Flex'],2013-01-01 00:00:00+00:00,0.5589999999999999,D,0.0092,0.0,155.041
512qrQeDm8pY39QVKJrwyZ,"Let It Go - From ""Frozen / Single Version",35,224373,0,['Demi Lovato'],2013-01-01 00:00:00+00:00,0.504,G,0.0188,0.0,139.915
31xVuaxFElzKPIp6Z9HT5N,La Melodía de Dios,56,285307,0,['Tan Bionica'],2013-01-01 00:00:00+00:00,0.67,C,0.00936,0.00018600000000000002,116.064
4yTeQK2XThWYeEW8D72XmU,Dear Boy,57,479333,0,['Avicii'],2013-01-01 00:00:00+00:00,0.6859999999999999,A,0.000276,0.1,124.995
6uygLd3EFY2x3FQqNfoATn,I Sommer,35,111187,0,['Gustav Nilsen'],2013-01-01 00:00:00+00:00,0.648,F#,0.695,0.0,107.074
6p6AMtWxEt4W2jc3HmpqdB,"In Summer - From ""Frozen""/Soundtrack Version",49,110987,0,['Josh Gad'],2013-01-01 00:00:00+00:00,0.5,G,0.536,0.0,77.124

Resumen numérico:
         popularity   duration_ms      explicit  danceability  acousticness  instrumentalness         tempo
count  10557.000000  1.055700e+04  10557.000000  10557.000000  10557.000000      10557.000000  10557.000000
mean      36.071706  2.417162e+05      0.072464      0.591019      0.272938          0.113894    123.151528
std       18.846508  1.622200e+05      0.259267      0.150041      0.297186          0.271724     28.267860
min        0.000000  3.002300e+04      0.000000      0.000000      0.000001          0.000000      0.000000
25%       27.000000  1.962580e+05      0.000000      0.497000      0.020200          0.000000    100.008000
50%       39.000000  2.279740e+05      0.000000      0.597000      0.143000          0.000004    125.984000
75%       49.000000  2.669470e+05      0.000000      0.698000      0.479000          0.003880    139.433000
max       90.000000  5.403500e+06      1.000000      0.979000      0.996000          0.998000    213.870000
