---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.13
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.13.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.13.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.13.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 10936 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 10936 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
1Mytkdy3EAWY0TmAiPaFmr,Te Robo,58,157675,0,['Zato DJ'],2018-01-01 00:00:00+00:00,0.907,C,0.631,3.87e-06,101.99799999999999
32fb4e8XjfktfaDUFytLiG,ASAP,34,227480,0,['Mirror'],2018-01-01 00:00:00+00:00,0.779,F#,0.0165,0.0,134.046
43kiDtoYD0nDJYxzQwclpT,Location Unknown ◐ (feat. BEKA) - Brooklyn Session,67,328050,0,"['HONNE', 'BEKA']",2018-01-01 00:00:00+00:00,0.508,F,0.941,0.0,91.509
2wRotarVdI0MtxnC1wrvja,Deus Não Está Morto,56,261120,0,['Fernandinho'],2018-01-01 00:00:00+00:00,0.586,B,0.0050799999999999994,0.00040300000000000004,129.955
0uCskQ9wUuLw72hcG7DFcZ,404,32,210094,0,['Error'],2018-01-01 00:00:00+00:00,0.828,F#,0.0622,0.0,126.04
2HMMxCBemHQY4Qktdtcpwj,Camped,56,220602,0,['RINI'],2018-01-01 00:00:00+00:00,0.632,G#,0.69,1.98e-05,133.009
00ZnitZelCNdD6PgX44Y1s,S'Onireftika,30,181542,0,['Usurum'],2018-01-01 00:00:00+00:00,0.484,C,0.883,0.16699999999999998,136.843
3C21IZG8yOH690SnMVWLuT,Original Sabahan,42,199855,0,"['Atmosfera', 'Floor 88']",2018-01-01 00:00:00+00:00,0.7490000000000001,D,0.6729999999999999,0.0,111.999
2Mh7XNWkAXgEjBXSskgUyD,Hey Hey Baby,40,139186,0,['my little airport'],2018-01-01 00:00:00+00:00,0.581,A,0.38299999999999995,0.0033299999999999996,89.98299999999999
688GnRUTvWWrJDHXsNS9HF,Next Year - 2018 Mix,0,199040,0,['Geddes the Sea'],2018-01-01 00:00:00+00:00,0.578,C,0.22899999999999998,0.0114,121.079
7Lq3MSNnVQ4yN4acrD9DyU,The Chronic 2017,0,178169,0,"['Mike Emilio', 'Modo']",2018-01-01 00:00:00+00:00,0.35200000000000004,F#,0.00375,1.64e-05,192.125
4UpD3qhY3KjmaCLu9f3SlW,Hardbass DAS,48,55838,1,['DJ Joppa'],2018-01-01 00:00:00+00:00,0.669,B,0.303,0.527,160.001
4bpyDBROAFaXmL2roHP3Mp,你叫我譯一首德國歌詞,38,201101,0,['my little airport'],2018-01-01 00:00:00+00:00,0.491,A,0.40399999999999997,0.0426,134.0
5FuYjeizTeAjQEx56F9RfH,ไม่มีเหตุผล,41,244583,0,"['MARINA', 'นายนะ']",2018-01-01 00:00:00+00:00,0.82,F#,0.36700000000000005,0.0,144.003
2Xn4FpumNNzg8ptNNqHB5K,האיש הפשוט,33,193665,0,['Nitan Ben Ari'],2018-01-01 00:00:00+00:00,0.68,E,0.156,0.0,153.998
4LtgkobW7PoVuwSvPjaGuq,P.P.P,48,196989,0,['Mozthaza'],2018-01-01 00:00:00+00:00,0.778,C#,0.09699999999999999,1.79e-06,94.975
4caxvyJdo9BZr0QYH4VuGS,离人愁,44,247125,0,['李袁杰'],2018-01-01 00:00:00+00:00,0.628,F,0.39299999999999996,0.0,75.02600000000001
1YDbuKfUa1gPHz0vu0IPcN,Destiny,1,329492,0,['Stephane Deschezeaux'],2018-01-01 00:00:00+00:00,0.82,G#,0.0104,0.0175,118.001
5op1X8TfWNUmJnwRzCQ3qL,Tsunami,51,198802,0,['DIVOKEJ BILL'],2018-01-01 00:00:00+00:00,0.601,D,0.0273,0.0,92.007
20RzArTj8t5exuBbnszRLz,Summer Sun,53,204410,0,['Cari Cari'],2018-01-01 00:00:00+00:00,0.732,B,0.484,0.218,114.007
2zVeHoUBTLkFMPYDs0M8co,La Noche,25,169535,0,"['Mariano Bermudez', 'La Sandonga']",2018-01-01 00:00:00+00:00,0.662,F,0.27699999999999997,0.0,104.63799999999999
5Fql9FqpykZo4Klz2WDn8u,Lies,0,417829,0,['Tim Lyall'],2018-01-01 00:00:00+00:00,0.7979999999999999,F#,0.000657,0.838,124.99600000000001
2LXCdIeoJJEJdux336Cyeo,Let's Groove On,0,424918,0,['Aad Mouthaan'],2018-01-01 00:00:00+00:00,0.813,A#,0.00405,0.759,121.999
00PWOnO986Qlt0h86XMm3M,Мама вылечи,53,199756,0,['Nurminsky'],2018-01-01 00:00:00+00:00,0.773,C#,0.0398,0.0,90.01299999999999
27RQbXMyZMqOjFvSg5slg4,缺,32,280714,0,['Hins Cheung'],2018-01-01 00:00:00+00:00,0.5660000000000001,A#,0.642,0.0,120.015
0X46CPFsAMAPobzEgEhQAm,"My Money (feat. Bokoesam, Bizzey & Dopebwoy)",49,180687,1,"['$hirak', 'Bizzey', 'Dopebwoy', 'Bokoesam']",2018-01-01 00:00:00+00:00,0.895,G,0.0226,7.64e-06,99.955
4VeOCv5ybM0IyhPkiAMxEt,心,34,152571,0,['my little airport'],2018-01-01 00:00:00+00:00,0.349,C,0.19399999999999998,0.44,105.994
62Ltx0EJu4imX70bx6icRb,再殺一個人,40,212620,0,['my little airport'],2018-01-01 00:00:00+00:00,0.612,A,0.331,0.0033799999999999998,155.95600000000002
77G0k1La0c5Dw8bAFANcyp,Sports,74,164165,0,['Beach Bunny'],2018-01-01 00:00:00+00:00,0.231,A,0.000653,0.026000000000000002,186.142
0vEC5A9cQVRaRl5eh100wo,Párizs,37,184652,0,['Hiro'],2018-01-01 00:00:00+00:00,0.823,F#,0.552,0.00198,114.96
6baeV3RT4kpivo327DC3AM,あなたがいることで,46,316453,0,['Uru'],2018-01-01 00:00:00+00:00,0.535,G,0.6829999999999999,0.0,147.32299999999998
2H3rFJI32usH7nYRKNm9SP,Ég fæ aldrei nóg af þér,22,206893,0,['Stjórnin'],2018-01-01 00:00:00+00:00,0.649,G#,0.00532,0.00434,155.026
77wz2VtAwxAwYOGTJrZBKT,"Miljonair (feat. SBMG, Lil' Kleine, Boef & Ronnie Flex)",57,189514,1,"['$hirak', 'SBMG', 'Boef', 'Lil Kleine', 'Ronnie Flex']",2018-01-01 00:00:00+00:00,0.7040000000000001,G,0.579,0.0,125.17200000000001
3Mh5cDZsYRljE11BQM7u0J,你說之後會找我,37,180907,0,['my little airport'],2018-01-01 00:00:00+00:00,0.5579999999999999,C,0.8490000000000001,0.000901,80.009
4LnRLsKhypMfOqExy6QanW,remember,48,350120,0,['Uru'],2018-01-01 00:00:00+00:00,0.504,C,0.46799999999999997,9.620000000000001e-05,75.02
5Wdfntb6waHHbUiUyPLqp3,Seinni Tíma Vandamál (Áramótaskaupið 2017),31,177661,0,['Daði Freyr'],2018-01-01 00:00:00+00:00,0.826,C#,0.0557,0.00227,127.042
1el6aIrQIu9griumSFkGRl,BOOBO,45,49830,1,"['LeoKBOBO', 'DJ Joppa']",2018-01-01 00:00:00+00:00,0.6809999999999999,E,0.00155,0.0631,130.151
1Lt82WcaNF72QM41Rp4QHw,Самая тёмная ночь,43,148500,0,['снова не успел'],2018-01-01 00:00:00+00:00,0.522,C,0.33399999999999996,7.04e-05,79.983
2Hjk6eQupcpvSl2sAyjQ03,Move It,45,82004,0,['DJ Kool'],2018-01-01 00:00:00+00:00,0.665,G,0.523,0.897,138.92700000000002
1GBSi00dG3vguFNB0S3JAX,Soy R - Acustico,25,245045,0,['RolA RooTs'],2018-01-01 00:00:00+00:00,0.9359999999999999,A,0.341,0.0,129.98

Resumen numérico:
         popularity   duration_ms      explicit  danceability  acousticness  instrumentalness         tempo
count  10936.000000  1.093600e+04  10936.000000  10936.000000  10936.000000      10936.000000  10936.000000
mean      42.139539  2.207754e+05      0.189923      0.634510      0.278446          0.098398    121.684055
std       21.789451  1.497833e+05      0.392258      0.158109      0.282101          0.256858     28.658735
min        0.000000  4.937000e+03      0.000000      0.000000      0.000000          0.000000      0.000000
25%       33.000000  1.817100e+05      0.000000      0.535000      0.036500          0.000000     99.535750
50%       48.000000  2.105470e+05      0.000000      0.652000      0.178000          0.000002    122.829000
75%       57.000000  2.420902e+05      0.000000      0.752000      0.455000          0.001190    139.724000
max       89.000000  4.864333e+06      1.000000      0.984000      0.996000          1.000000    229.862000
