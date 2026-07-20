---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.5
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.5.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.5.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.5.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 9597 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 9597 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
2ctPEKEZTumjgcJPmkXo4R,憑著愛,27,274200,0,['George Lam'],2010-01-01 00:00:00+00:00,0.527,A,0.867,1.4300000000000002e-05,99.036
4BFYZbGJXZvU4iXbKg7Piq,Каникулы,38,216137,0,['Турбомода'],2010-01-01 00:00:00+00:00,0.857,C,0.0686,0.0021,139.059
5gXMdkIRNEuSFCNAjRbBGH,You've Made Me Stronger,45,245840,0,['Regine Velasquez'],2010-01-01 00:00:00+00:00,0.65,E,0.0464,2.34e-05,94.947
2QA6KBF9kV88NhWDj2SdBl,Skruzdėlinė Elektrinė,12,165240,0,['Tele Bim Bam'],2010-01-01 00:00:00+00:00,0.7040000000000001,D,0.465,6.65e-05,102.04
30NGAHZMP0iBpRT491bi1f,我的快樂時代,24,218173,0,['Eason Chan'],2010-01-01 00:00:00+00:00,0.233,C,0.499,3.62e-06,180.84400000000002
09I4gCrXABIV7YdNtWGXoi,Morning Sun,46,218462,0,['Dave Bixby'],2010-01-01 00:00:00+00:00,0.409,E,0.847,0.0036,48.875
5RNtyseiyt5dNH0P8E3M3D,Kalėdų Stebuklas,14,313627,0,['Tele Bim Bam'],2010-01-01 00:00:00+00:00,0.586,D,0.368,0.0,83.02
2cjS444xQfSRbQDp0lNLs4,"Pupa, Pupa",13,177587,0,['Tele Bim Bam'],2010-01-01 00:00:00+00:00,0.899,D,0.0776,8.22e-06,127.009
5Nc5Ovx5QUscOOV3nRhTMm,Būsim Draugais,13,237587,0,['Tele Bim Bam'],2010-01-01 00:00:00+00:00,0.695,D#,0.303,0.0,115.99600000000001
5fp6m6Zo4LetiWaMMrPjy5,Dreamscape,51,277489,0,['009 Sound System'],2010-01-01 00:00:00+00:00,0.5489999999999999,D#,0.00481,0.00038199999999999996,123.02799999999999
6ZNVfDrLagBycP58Dl94kg,Balta Lopšinė,15,218187,0,['Tele Bim Bam'],2010-01-01 00:00:00+00:00,0.521,F,0.49700000000000005,0.000479,105.898
79aUUZchoCbggPNH7dmytr,落花流水,26,246840,0,['Eason Chan'],2010-01-01 00:00:00+00:00,0.41200000000000003,C#,0.644,0.000196,75.702
5kZbRCbMUbbbSmrQxSVkLp,信口開河,24,258040,0,['Justin Lo'],2010-01-01 00:00:00+00:00,0.5660000000000001,F#,0.561,0.0,127.73200000000001
2Z2dTiPJYuYHrP9vdgszBj,童話,30,257307,0,['Miriam Yeung'],2010-01-01 00:00:00+00:00,0.48700000000000004,B,0.91,0.0,135.799
2zu3dpbWHgIfSPIdp8qZyg,Небеса,45,236192,0,['Valery Meladze'],2010-01-01 00:00:00+00:00,0.753,A#,0.429,0.0,130.034
48rJQa3TdMfnPJxh1oPxsZ,El Prostipirugolfo,59,186413,0,['Los Titanes De Durango'],2010-01-01 00:00:00+00:00,0.757,F,0.289,1.08e-06,127.47
5GZ2bQIzvLXgZpjgxSKP4l,等,26,255880,0,['Eason Chan'],2010-01-01 00:00:00+00:00,0.276,C,0.8759999999999999,7.390000000000001e-05,67.635
2UZoSuDO0D6y9bW9Z3Hkng,Niña De Mi Corazón,57,188413,0,['La Arrolladora Banda El Limón De Rene Camacho'],2010-01-01 00:00:00+00:00,0.7020000000000001,D#,0.52,0.0,114.037
3e00xrTJ3zwRf4Ayr6MH2s,兩隻老虎,45,72200,0,['風格童星組合'],2010-01-01 00:00:00+00:00,0.841,D#,0.72,0.0,135.088
0ZKgaQUvQvd4C5ADKNtBk8,忘記他,36,175467,0,['Teresa Teng'],2010-01-01 00:00:00+00:00,0.311,F,0.373,0.0014,103.275
2iYL1ecHzwZsvvnPduIXb6,CLICK,45,270573,0,['ClariS'],2010-01-01 00:00:00+00:00,0.588,A#,0.0265,0.00585,134.915
1mivlo7KSaJfye1hzp0MhV,沙龍,25,276413,0,['Eason Chan'],2010-01-01 00:00:00+00:00,0.406,E,0.267,6.37e-06,140.444
0X5Ras26dWvagYaQ58VnBC,Wie ich heiß,37,236840,0,['Schwefelgelb'],2010-01-01 00:00:00+00:00,0.7829999999999999,C,0.000146,0.465,123.954
0MqhXAFU5rnOtskcRkllYG,Just Tonight,55,168400,0,['The Pretty Reckless'],2010-01-01 00:00:00+00:00,0.278,F#,0.0012,0.0174,163.877
0q1GXKAZABZOhNXRApqT4R,Sfyrixa....Ki Elixes,37,199133,0,['Panos Kiamos'],2010-01-01 00:00:00+00:00,0.593,B,0.008320000000000001,0.0,180.083
5FpUEdxB0w4RBvxkDG5osd,Pupa,14,189133,0,['Tele Bim Bam'],2010-01-01 00:00:00+00:00,0.856,A,0.452,2.44e-05,123.993
5ElBbDAlqAyAnDcgQUjhlm,Geloven In Het Leven,43,242907,0,['3JS'],2010-01-01 00:00:00+00:00,0.564,C,0.235,0.000557,140.968
4tstfcVBKsqYNd1EPt3vCH,最緊要好玩,29,184253,0,['Sam Hui'],2010-01-01 00:00:00+00:00,0.735,C#,0.122,0.0,144.93
1rdBJvTlDHHH82HUPbxDLd,Tu Y Yo Somos Uno Mismo,34,255467,0,['Timbiriche'],2010-01-01 00:00:00+00:00,0.727,C#,0.24,0.0,125.359
5Xfrz26D1llsmmwoDB0gnI,大熱,24,217507,0,['Leslie Cheung'],2010-01-01 00:00:00+00:00,0.5329999999999999,G,0.462,0.0,160.053
5GUJ3zBhqMuyTLKU7nV74H,雌雄同體,24,234053,0,['Juno Mak'],2010-01-01 00:00:00+00:00,0.629,G#,0.146,0.0010199999999999999,177.968
4G8I2gh90zpYrEXbQlenWR,無人之境,27,252920,0,['Eason Chan'],2010-01-01 00:00:00+00:00,0.348,D,0.43200000000000005,0.0,125.745
78AQlcD4vmJap3xJKAFb9t,左右手,31,255507,0,['Leslie Cheung'],2010-01-01 00:00:00+00:00,0.44,F,0.716,0.000299,131.705
2nleIsDVspaCnDomR43APV,你怎麼說,39,204413,0,['Teresa Teng'],2010-01-01 00:00:00+00:00,0.6509999999999999,F,0.637,1.9699999999999998e-05,82.87299999999999
7dGR0CfXH0pmTICRXRy2cJ,Jungle,40,193112,1,"['Professor Green', 'Maverick Sabre']",2010-01-01 00:00:00+00:00,0.47600000000000003,F,0.222,0.0,72.77600000000001
7BvYZlVpLX48WN2GUlXSpz,Ku-Kū!,14,231427,0,['Tele Bim Bam'],2010-01-01 00:00:00+00:00,0.725,E,0.138,4.87e-06,142.05100000000002
4buvG5Kmstm8UMjSgUrv2X,Who Owns My Heart,57,214853,0,['Miley Cyrus'],2010-01-01 00:00:00+00:00,0.5710000000000001,A,0.0106,0.0,135.908
21HXNdJEfwiFZwwGFI0XLO,In Moments Like These,50,229827,0,['Maranatha! Music'],2010-01-01 00:00:00+00:00,0.341,D,0.9059999999999999,0.0132,93.288
4vzr8ZjVHFH3Yv2pAkEU4N,黑色狂迷,24,206347,0,['Mr.'],2010-01-01 00:00:00+00:00,0.44799999999999995,A#,0.00048600000000000005,0.0,122.075
6yd8jIHRyFNEO6QBRQCdw3,Do Re Mi,15,162120,0,['Tele Bim Bam'],2010-01-01 00:00:00+00:00,0.42,A#,0.195,0.0,128.46200000000002

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  9597.000000  9.597000e+03  9597.000000   9597.000000   9597.000000       9597.000000  9597.000000
mean     37.364176  2.505258e+05     0.060748      0.598078      0.305220          0.057111   121.847336
std      16.360212  1.955304e+05     0.238880      0.153116      0.300604          0.191216    28.766440
min       0.000000  3.040000e+04     0.000000      0.000000      0.000003          0.000000     0.000000
25%      29.000000  1.990000e+05     0.000000      0.500000      0.035400          0.000000    98.499000
50%      39.000000  2.311070e+05     0.000000      0.608000      0.198000          0.000002   122.969000
75%      48.000000  2.700000e+05     0.000000      0.707000      0.529000          0.000455   139.414000
max      84.000000  4.995083e+06     1.000000      0.985000      0.996000          0.998000   210.140000
