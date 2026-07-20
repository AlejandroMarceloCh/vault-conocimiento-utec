---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.12
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.12.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.12.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.12.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 9889 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 9889 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
6CZhOkTPmFXZSOymIE80Jg,Не забывай,43,193347,0,['T-Fest'],2017-01-01 00:00:00+00:00,0.51,C,0.0875,0.0,116.305
0MIpFpCMXkwi9RTJuDbFxw,Pusula,53,196660,1,"['Gazapizm', 'Cash Flow', 'Esat Bargun']",2017-01-01 00:00:00+00:00,0.665,E,0.013000000000000001,0.0,129.934
1d5hx2nX2Nr87orTqBVR9T,Perreo Musulmán,48,166951,0,['DJ Liendro'],2017-01-01 00:00:00+00:00,0.9109999999999999,G,0.289,5.44e-06,102.148
1S9uBRXAELOLZX0G9iCrCY,Te Amo y Te Amaré,43,391733,0,['Los Rancheros de Plata'],2017-01-01 00:00:00+00:00,0.6629999999999999,F,0.16,0.0,137.985
4pNqETdfhlxuE0b6U7jbEZ,Pięć (prod. Tasty Beats),42,218547,0,"['Donguralesko', 'Dj Cube', 'Shellerini', 'Sitek']",2017-01-01 00:00:00+00:00,0.617,E,0.0127,0.0,87.086
5lrZstHSfDdYFNlHIChCSR,Me Emborracharé,50,253048,0,['Grupo Zúmbale Primo'],2017-01-01 00:00:00+00:00,0.638,D,0.0893,0.0,116.934
5AeVsL9BeifkgUuDbOWXvu,Signo Libra,45,285036,0,['Los Rancheros de Plata'],2017-01-01 00:00:00+00:00,0.669,A,0.0486,0.0,136.078
5O1WpOYbqlbLaAoHNbhqur,Land of Hope and Glory (2017 Version),3,163268,0,"[""Blackmore's Night""]",2017-01-01 00:00:00+00:00,0.452,C,0.0657,0.000368,75.017
1NmC8j2bSFiTitcbqlBZoe,Land of Hope and Glory - 2017 Version,6,163268,0,"[""Blackmore's Night""]",2017-01-01 00:00:00+00:00,0.452,C,0.0657,0.000368,75.017
7bU4S2655LHm3qo1A6Cpuc,Coming Home - 2017 Version,6,189028,0,"[""Blackmore's Night""]",2017-01-01 00:00:00+00:00,0.584,G,0.0221,0.00257,138.058
1YyQ6i603y0FFQGmBNNPBn,Te Pido Perdon,53,186990,0,['Banda XXI'],2017-01-01 00:00:00+00:00,0.6779999999999999,D,0.196,0.0,138.018
24ssF0rQ364s7T3IADEMaA,Writing on the Wall - 2017 Version,7,210594,0,"[""Blackmore's Night""]",2017-01-01 00:00:00+00:00,0.5429999999999999,G#,0.141,0.000128,158.954
1vj0XFI6gF7KDJ28x5kxbp,Satu-satuNya Yang Kuandalkan,46,227972,0,['Angel Pieters'],2017-01-01 00:00:00+00:00,0.379,F,0.615,0.0,135.808
6csAIjpqo5z6OnUq7lmOr9,何になりたくて、,45,212067,0,['LOZAREENA'],2017-01-01 00:00:00+00:00,0.778,D,0.816,0.0,90.014
21y3M2slvLOj1ECjsv8A9j,Warzone,52,210704,0,['Nfx'],2017-01-01 00:00:00+00:00,0.603,C#,0.43,0.000735,90.065
5obrQsY3cohSBpTdJbUyUa,A Song I Wrote When I Was 9,53,47084,1,['Joe Bowley'],2017-01-01 00:00:00+00:00,0.65,A,0.915,0.0329,91.98
2qmsUfTjdSWkE45n1x8WoV,Gökyüzü,56,151551,0,['Perdenin Ardındakiler'],2017-01-01 00:00:00+00:00,0.5920000000000001,C,0.848,0.000258,79.931
42Y5pqnu8iQMPuyJUgbBKx,All Day Everyday (Łee),43,214347,1,['Kaz Bałagane'],2017-01-01 00:00:00+00:00,0.85,A#,0.19899999999999998,0.0,141.996
3qw4ESWTiz1Y8Tl75sSLpI,Moonlight Shadow (2017 Version),3,169361,0,"[""Blackmore's Night""]",2017-01-01 00:00:00+00:00,0.617,D#,0.752,0.0,121.40899999999999
188vCXc4bAejLqGhpEVBGT,Jiyuu no Tsubasa,69,331947,0,['Linked Horizon'],2017-01-01 00:00:00+00:00,0.373,G,0.0619,3.3100000000000005e-05,157.433
2pc6yUv7m1R524Mg1mnxdp,El Final - Remix,39,226685,1,"['Goldy Boy', 'Ozuna']",2017-01-01 00:00:00+00:00,0.745,C#,0.449,0.0,84.971
1EuFr1JA70TaEzlaSM4ulc,366.Gün,58,235078,0,['Sagopa Kajmer'],2017-01-01 00:00:00+00:00,0.55,F,0.121,0.0,82.995
3Hk1TBFRnKOCP144ne8Isp,Одно я знал_выдох,52,279196,1,['T-Fest'],2017-01-01 00:00:00+00:00,0.525,D#,0.154,0.0,146.274
4f7byC0CCA57DiAqImVcwu,Apa Salah Dan Dosaku,44,212360,0,['D. Lloyd'],2017-01-01 00:00:00+00:00,0.43700000000000006,D,0.41100000000000003,7.56e-05,66.991
5sJ9QnkBrTAB4CBcbwOxQT,生僻字,44,216000,0,['陳柯宇'],2017-01-01 00:00:00+00:00,0.595,B,0.601,0.0,139.975
6aF4FPWZOv4Kae5ViFEkWD,Gia Ola Ikanoi (Tzamaika),38,238078,0,['Christos Mastoras'],2017-01-01 00:00:00+00:00,0.695,A,0.036000000000000004,0.0,109.962
0oRkfCO7H4IiGpxK3U0JGS,Ángel O Demonio,52,202850,0,"['Fredy Montoya', 'Luisito Muñoz']",2017-01-01 00:00:00+00:00,0.823,D,0.48100000000000004,0.0,110.99700000000001
0VdfL7wQBI5eLjFvM7Ylam,Chufuku,43,194456,0,"['Emus DJ', 'Tiburon Valdez']",2017-01-01 00:00:00+00:00,0.888,F#,0.0596,1.11e-05,100.04899999999999
2cb1NymMUM9wdRTgXoLFNe,Bergmál,24,267400,0,['DIMMA'],2017-01-01 00:00:00+00:00,0.386,F,0.0141,0.00203,76.062
386bifjqGxhkDsefwG9SZJ,ฟ้าสีจาง,37,250761,0,"['Owlet Lounge', 'UrboyTJ']",2017-01-01 00:00:00+00:00,0.688,B,0.0651,3.55e-06,91.986
6DhNE80UHGTmnagT3rdprD,7 Years,1,226702,0,"['Karizma Duo', 'Josh Franklin']",2017-01-01 00:00:00+00:00,0.757,A#,0.746,0.0,118.79
4eg47ngxYMau5Ce8RBb9qQ,Burn,42,238144,0,['Priscilla Abby'],2017-01-01 00:00:00+00:00,0.522,D,0.306,0.0,89.962
0BFchMxw58nYVMcjVyqmxm,При своём (2017),41,178399,0,['Miyagi & Andy Panda'],2017-01-01 00:00:00+00:00,0.7090000000000001,B,0.6609999999999999,0.0,129.954
6kS5ykFz7MPq673xAzO1JB,2010 Was a Good Year,0,60187,0,['Koolest Kev'],2017-01-01 00:00:00+00:00,0.7140000000000001,C,0.0964,0.895,120.178
4vEarTrAW9KEo3Pbu3vuRw,Mi Habitación,44,213653,0,['Monada'],2017-01-01 00:00:00+00:00,0.609,A#,0.192,0.0,143.92
5AGaFrwi1HLtIyD97WzSGW,Spodenki Do Ćpania,41,180147,1,['Kaz Bałagane'],2017-01-01 00:00:00+00:00,0.602,A#,0.102,0.0,98.036
1krx9aPU8fD9tZdtaHI4mP,Castles Year 2002,0,357850,0,['R2M'],2017-01-01 00:00:00+00:00,0.6,A,0.0138,0.507,142.009
2AnMndnV7XFk3VuuCPy6Zk,Safari - Gritty Remix,51,195516,0,"['Serena', 'Gritty']",2017-01-01 00:00:00+00:00,0.8140000000000001,F,0.635,0.00134,102.971
0WuLJ3tbRap45aO1OtN7vh,talpig feketében,31,181461,1,['gyuris'],2017-01-01 00:00:00+00:00,0.7929999999999999,A#,0.55,4.24e-05,127.014
6y4vLEcQubtiIa0n7DJfX1,100 feat. Sound'n'Grace,42,195267,0,['Filip Lato'],2017-01-01 00:00:00+00:00,0.68,G#,0.0708,0.0,106.98299999999999

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  9889.000000  9.889000e+03  9889.000000   9889.000000   9889.000000       9889.000000  9889.000000
mean     42.236222  2.297585e+05     0.170998      0.624972      0.278547          0.089228   121.335623
std      20.568946  1.313905e+05     0.376526      0.160689      0.283121          0.245042    28.896425
min       0.000000  8.594000e+03     0.000000      0.000000      0.000001          0.000000     0.000000
25%      34.000000  1.900000e+05     0.000000      0.528000      0.034500          0.000000    99.728000
50%      47.000000  2.176670e+05     0.000000      0.644000      0.172000          0.000002   122.022000
75%      56.000000  2.523070e+05     0.000000      0.740000      0.466000          0.001090   138.046000
max      88.000000  4.511716e+06     1.000000      0.979000      0.996000          1.000000   219.978000
