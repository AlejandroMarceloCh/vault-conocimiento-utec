---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.6
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.6.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.6.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.6.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 9689 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 9689 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
2pC8PvCeQLw1AMx9nwA2jc,Ég gef þér allt mitt líf,12,255373,0,"['Ragga Gröndal', 'Helgi Björnsson']",2011-01-01 00:00:00+00:00,0.556,C,0.255,0.0,127.74600000000001
7EA0xZLiXLFuSuwHUeIc3j,Wait for Fate,14,270977,0,['Jón Jónsson'],2011-01-01 00:00:00+00:00,0.584,G#,0.9420000000000001,0.0,112.825
0V4NgZlY77MpROTCPDBLSt,Little Tree,13,246410,0,['Jón Jónsson'],2011-01-01 00:00:00+00:00,0.479,A,0.47700000000000004,2.8600000000000004e-05,154.993
0O3fAQi8dYTtxc3neZFD95,Nærvera,11,503409,0,['Friðrik Karlsson'],2011-01-01 00:00:00+00:00,0.46,E,0.9009999999999999,0.877,120.07700000000001
1QlMpoJNwgTJODvONnHxeL,Sem kóngur ríkti hann,13,187989,0,['Papar'],2011-01-01 00:00:00+00:00,0.56,D,0.0829,0.0,136.013
7BmI4hAj6dXIQgA77ZlOzm,Buzzin Remix,41,224333,1,"['Mann', '50 Cent']",2011-01-01 00:00:00+00:00,0.687,A#,0.0887,0.0,104.029
41KBQ1IMtrIYmE8BA8rHtR,Ég gef þér allt mitt líf,13,223422,0,"['Ragnhildur Gísladóttir', 'Björgvin Halldórsson']",2011-01-01 00:00:00+00:00,0.653,E,0.268,0.000677,127.117
7DJ6zJAl3Z4bgKpH0CdJN1,Irving Berlin-The Early Years,0,389107,0,"['Irving Berlin', 'Coastal Communities Concert Band', 'Dr. Robert C. Fleming']",2011-01-01 00:00:00+00:00,0.217,G,0.122,0.0030800000000000003,130.078
2Yv4ta05XMaTQKeN4vv4e6,Þrek og tár,13,248918,0,"['Sigríður Thorlacius', 'Sigurður Guðmundsson', 'Iceland Symphony Orchestra']",2011-01-01 00:00:00+00:00,0.174,G,0.7609999999999999,0.0153,73.438
4gDQktCvIfPqo18AdHmkR4,Lipstick - Radio Edit,40,175000,0,['Jedward'],2011-01-01 00:00:00+00:00,0.625,G#,0.0109,0.0,138.015
1l8GKUSfTaX2CL0Qe3iPi8,Steinstjarna,13,207911,0,['Emmsjé Gauti'],2011-01-01 00:00:00+00:00,0.626,A,0.00601,0.0,143.672
05a0eWm2Xg3pvDEVuvKm76,I think of angels (feat. Ellen Kristjáns),12,210884,0,"['KK', 'Ellen Kristjánsdóttir']",2011-01-01 00:00:00+00:00,0.621,D,0.946,0.0113,121.99700000000001
47g7906sLoM40c4QO5bIo1,Þjóðsaga,13,173221,0,['Papar'],2011-01-01 00:00:00+00:00,0.6779999999999999,D,0.301,0.000559,98.006
53d6MZiiMSoymGx8MYYdIX,Að sleppa takinu,13,941848,0,['Friðrik Karlsson'],2011-01-01 00:00:00+00:00,0.139,F,0.99,0.826,73.225
1VlEpNSqN4yV7u5jwBMr6J,Síðasti dansinn,12,230249,0,"['Erna Gunnarsdóttir', 'Björgvin Halldórsson']",2011-01-01 00:00:00+00:00,0.385,G,0.552,0.0,135.89
6ZvdB6I9Ocs8rQbvJbTRWS,Dancing In The Moonlight,32,176547,0,['King Harvest'],2011-01-01 00:00:00+00:00,0.63,C,0.161,0.0,136.114
11i5Bnpjquuq7bzDjnS08V,Af álfum,13,187292,0,"['Margrét Eir', 'Friðrik Ómar']",2011-01-01 00:00:00+00:00,0.654,G#,0.47,0.0,101.961
5ARvaT9bPJi5WiRqMaxIDQ,Farin,12,202571,0,['Skítamórall'],2011-01-01 00:00:00+00:00,0.5920000000000001,G,0.147,1.24e-06,95.95100000000001
0XGciH3qBicZzp2HT9Lh9v,Einn ég ríð til fjalla,16,228345,0,['Helgi Björnsson'],2011-01-01 00:00:00+00:00,0.688,C,0.637,0.0,119.132
2GXnvifooVkdvapTF2iqvJ,Lately,13,235590,0,['Jón Jónsson'],2011-01-01 00:00:00+00:00,0.623,D,0.44,5.97e-06,150.08
4VtxZztPlu4AjLhGGYdtt4,When You're Around,17,222540,0,['Jón Jónsson'],2011-01-01 00:00:00+00:00,0.531,G,0.153,0.0,94.78200000000001
28iu6RUQHEr64yIAkAgLgk,Beautiful Girl,53,207453,0,['INXS'],2011-01-01 00:00:00+00:00,0.662,B,0.000766,0.54,120.59100000000001
7wK50ryAnzzKLcw0v3jGwN,Árás,17,366400,0,['Skálmöld'],2011-01-01 00:00:00+00:00,0.415,E,0.00011100000000000001,0.0015,107.861
1bjPavnBwzPrWk3lC5EhaJ,Miss You So,14,306085,0,['Jón Jónsson'],2011-01-01 00:00:00+00:00,0.5529999999999999,C#,0.892,0.0447,120.118
2siwUl90v9WtZECBYlribW,Alltaf á Heimaey,13,220822,0,['Hálft í hvoru'],2011-01-01 00:00:00+00:00,0.58,A,0.705,0.0,91.64
6A8sipwNlvJZ0mwDpqoZoV,Í góðu skapi,13,191750,0,['Steindinn okkar'],2011-01-01 00:00:00+00:00,0.836,C,0.00217,0.0,115.98899999999999
3z0ZTUc20yDpSJBjKxmYsa,Faðir Thug,15,161890,0,['Steindinn okkar'],2011-01-01 00:00:00+00:00,0.273,G#,0.252,0.00235,104.323
4vcH23rUapxgcSyIIGiSal,Brúðkaup Villa kokks,13,136626,0,"['Papar', 'Einar Ágúst']",2011-01-01 00:00:00+00:00,0.626,G,0.456,0.0,112.976
7nOJ0CLKPYmFEgKlTNc73N,Higher And Higher,14,262525,0,['Jet Black Joe'],2011-01-01 00:00:00+00:00,0.48200000000000004,G#,0.0303,0.00935,119.948
5LetylD5rmQWmAeVDWrTEP,Það er komið sumar,14,230040,0,"['Ragga Holm', 'Margrét Rán', 'Emmsjé Gauti']",2011-01-01 00:00:00+00:00,0.688,G,0.0022600000000000003,0.00028,143.006
0Q8BVb82shwHgfe08nVtT3,Draumur um Nínu,14,176239,0,"['Eyjólfur Kristjánsson', 'Stefán Hilmarsson']",2011-01-01 00:00:00+00:00,0.593,D,0.39899999999999997,0.0,75.906
5zwcVFRHq9INNCFtCM1g5x,Changes Come,12,459987,0,['GusGus'],2011-01-01 00:00:00+00:00,0.465,F,0.308,0.9079999999999999,120.896
2EFdXuxXBLeH76aXH05bk6,Alt mulig mand (ásamt Þorsteini Guðmundssyni),12,104954,0,['Steindinn okkar'],2011-01-01 00:00:00+00:00,0.852,G,0.00488,0.0159,95.88600000000001
2Px4PrbPBMeWB1silbjI5H,(Today I Met) The Boy I'm Gonna Marry,54,166053,0,['Darlene Love'],2011-01-01 00:00:00+00:00,0.355,C#,0.54,0.0645,100.87799999999999
0DgwF3FCd3RYdDA2u8gJJ0,Litla sæta ljúfan góða,14,170388,0,['Hljómsveit Ingimars Eydal'],2011-01-01 00:00:00+00:00,0.544,A#,0.8859999999999999,0.0,130.628
6YrP1vpOwcSSSUiM4YO2PJ,Seinna meir,12,195233,0,"['Jóhann Helgason', 'Magnús Þór Sigmundsson']",2011-01-01 00:00:00+00:00,0.669,E,0.821,0.00301,106.31700000000001
4JUdzL0tRKNEMFDnpu4YTx,NAVIDAD 2010 - ORIGINAL MIX,0,327654,0,['YAN KROW'],2011-01-01 00:00:00+00:00,0.73,C,0.0017699999999999999,0.71,126.01100000000001
3D8iGJ3RwyL7shgAZNXEY5,Devil Went Down to Georgia,13,247571,0,['Papar'],2011-01-01 00:00:00+00:00,0.653,G,0.239,0.000131,132.059
40Ql1rH5Tp748yNKXmg4QZ,Tell Me!,16,176147,0,"['Einar Ágúst', 'Telma']",2011-01-01 00:00:00+00:00,0.489,D,0.0021100000000000003,0.0,145.452
3vP0xlW7ib3JEOebUGjz4m,Baseline,24,199181,0,['Quarashi'],2011-01-01 00:00:00+00:00,0.653,D,0.0005099999999999999,0.00374,97.96799999999999

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  9689.000000  9.689000e+03  9689.000000   9689.000000   9689.000000       9689.000000  9689.000000
mean     37.050986  2.447019e+05     0.071731      0.588243      0.304033          0.075009   122.997772
std      16.631041  1.270579e+05     0.258055      0.152910      0.305441          0.222391    28.855725
min       0.000000  3.002700e+04     0.000000      0.000000      0.000000          0.000000     0.000000
25%      29.000000  1.991070e+05     0.000000      0.487000      0.030600          0.000000    99.891000
50%      39.000000  2.304930e+05     0.000000      0.599000      0.189000          0.000002   124.638000
75%      48.000000  2.704000e+05     0.000000      0.699000      0.547000          0.000853   139.963000
max      85.000000  4.792587e+06     1.000000      0.988000      0.996000          0.993000   215.537000
