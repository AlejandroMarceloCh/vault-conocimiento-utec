---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.3
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.3.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.3.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.3.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 9714 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 9714 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
0WTm21amOR7KQNh67GA1OP,No Le Temas al Amor,35,257640,0,['Los inquietos del vallenato'],2008-01-01 00:00:00+00:00,0.721,D#,0.0598,0.0,148.55
3CgWfGDdz79tMGq4ddB2Yk,Lukaku,33,258280,0,['D’MASIV'],2008-01-01 00:00:00+00:00,0.40299999999999997,B,0.715,7.33e-06,174.18
6gzqel7GCOe9wmA5fpxwGq,Ultimas Noticias,49,264440,0,['El Poder Del Norte'],2008-01-01 00:00:00+00:00,0.607,G#,0.518,0.0,179.989
5rKNgKpyv0yEHQKygVvyvm,Lene Gia Mena,31,249067,0,"['Master Tempo', 'Hristos Dandis']",2008-01-01 00:00:00+00:00,0.696,F,0.00494,0.0176,94.991
34MgFmh4IiHvR0qEAS3wyZ,Song for the children,39,279760,0,['Oscar Harris'],2008-01-01 00:00:00+00:00,0.623,E,0.27,0.000133,78.185
0nHZaFH16gzcPCa2Q9xtn4,Nada,50,334450,0,['Zoé'],2008-01-01 00:00:00+00:00,0.541,D,0.155,0.0801,133.515
0H3I8PJh0mbJ5tSRleYywg,Kau dan Aku Menuju Ruang Hampa,45,239926,0,['Efek Rumah Kaca'],2008-01-01 00:00:00+00:00,0.368,E,0.105,4.68e-05,132.516
1iZo5ZYjVh9PJw5FrT80EW,Zaterdagavond,34,191507,0,['Mieke'],2008-01-01 00:00:00+00:00,0.809,G,0.303,0.0,122.755
4pcoxvpDtdjRMEUyF7LknZ,เพื่อเธอ,24,279878,0,['Nop Ponchamni'],2008-01-01 00:00:00+00:00,0.5870000000000001,C,0.9390000000000001,9.69e-06,81.675
6sR0gCVYVfKjQzqx1v20bC,ويلاه,37,235827,0,['Rashed Al-Majed'],2008-01-01 00:00:00+00:00,0.40299999999999997,C#,0.302,0.0,87.321
2pZDhsmGRSkRgWNfkDr70S,Ghosts N Goblins,20,106973,0,['Year 200X'],2008-01-01 00:00:00+00:00,0.278,G,4.15e-06,0.9670000000000001,92.99700000000001
3LUStBcxw1gCC2SvuEpeVH,Blijf Je Vanavond,34,200107,0,['Monique Smit'],2008-01-01 00:00:00+00:00,0.6779999999999999,A,0.235,0.0,120.0
4wxuhmjzImWHSfKNdGcqKj,Bila Kau Yang Membuka Pintu,34,215067,0,['Maria Shandi'],2008-01-01 00:00:00+00:00,0.45399999999999996,A#,0.703,2.23e-05,135.887
3tK2JY8quLxkEvmvKDyGo5,Te Juro Que Te Amo,54,208693,0,['Grupo Bryndis'],2008-01-01 00:00:00+00:00,0.7240000000000001,A,0.419,0.0468,92.751
3JOxS04XfwGxJpyKwVeWrx,Que Me Digan Loco,50,221600,0,['La Original Banda El Limón de Salvador Lizárraga'],2008-01-01 00:00:00+00:00,0.628,A#,0.631,2.62e-05,144.017
0nxUIazpTfTZNmoRMugDPe,Bij Ons In De Jordaan,35,205533,0,['Johnny Jordaan'],2008-01-01 00:00:00+00:00,0.7490000000000001,G,0.831,0.0,130.672
7f4wlBeT8vqUDmom4Q676T,Te Sorprenderás,48,288533,0,['Los inquietos del vallenato'],2008-01-01 00:00:00+00:00,0.6990000000000001,G,0.41700000000000004,0.0,136.764
4k4myRYVvF8p1yAXtFJNC9,Emeina Edo,27,260160,0,['Stelios Rokkos'],2008-01-01 00:00:00+00:00,0.33799999999999997,B,0.475,0.0,143.63299999999998
2yBj2PchXHEC8rIde9rgMM,Doe Wat Je Altijd Deed,35,225493,0,['Marco Borsato'],2008-01-01 00:00:00+00:00,0.33,E,0.32799999999999996,0.0,179.922
4mZEwngFtFRTWNWNrVHerV,He Vuelto por Ti,53,280867,0,['Maelo Ruiz'],2008-01-01 00:00:00+00:00,0.515,A#,0.45299999999999996,3.27e-06,177.21599999999998
3skPCcteHhoPV6GkzxVl2p,Into Your Arms,54,239227,0,['The Maine'],2008-01-01 00:00:00+00:00,0.353,G,0.11800000000000001,0.0,179.926
6cwApjDiqBA9WMWNhnOSVY,Gangster for Life,25,235570,0,['Danger Man'],2008-01-01 00:00:00+00:00,0.631,C#,0.37799999999999995,0.0,170.081
56z8EVfBhdmkmzSE8mL15p,Sonora Y Sus Ojos Negros,55,177387,0,['Miguel Y Miguel'],2008-01-01 00:00:00+00:00,0.5820000000000001,G#,0.7929999999999999,0.0,94.39
6pPNepnzBAMdPcE3vgyT3y,Sabes A Chocolate,48,226333,0,"['Kumbia Kings', 'A.B. Quintanilla III', 'Pee Wee Gonzalez']",2008-01-01 00:00:00+00:00,0.7490000000000001,G,0.10300000000000001,0.00033,109.962
6YAfMAyF3V6dhJXkPCu0WB,Necesito una Canción,33,173863,0,['Nano Stern'],2008-01-01 00:00:00+00:00,0.594,G,0.42700000000000005,0.0,129.16
5ucLsalXHFV7vufoGC5LeG,Baraja De Oro,50,203573,0,['Chalino Sanchez'],2008-01-01 00:00:00+00:00,0.47100000000000003,A#,0.723,9.53e-05,169.94099999999997
7280ciFIlOtglgAvxwVWTp,Mikra Veggalika,23,297031,0,['Eleonora Zouganeli'],2008-01-01 00:00:00+00:00,0.535,D,0.198,1.0300000000000001e-05,146.189
1acbmViB11Fnlt4LQ1P3YL,Tiempos Que,25,297493,0,['Danger Man'],2008-01-01 00:00:00+00:00,0.529,C#,0.316,0.0,76.122
5o7obrwZeYCdq1AS5WjVBB,Dan Bila,32,282040,0,['Second Civil'],2008-01-01 00:00:00+00:00,0.223,F#,0.14800000000000002,7.74e-05,140.45
3pJiIxqrptYnXgpCyLtBgy,Menjadi Indonesia,34,277906,0,['Efek Rumah Kaca'],2008-01-01 00:00:00+00:00,0.55,D,0.0997,0.0679,127.96600000000001
2Qv1MpF8JjeT8PQSLT8t0u,Para mis soldados,35,221401,0,['Danger Man'],2008-01-01 00:00:00+00:00,0.71,A,0.179,0.0,76.06
011ojwYah24f0x9nZuRYHP,Latin Dance,34,194581,0,['Massada'],2008-01-01 00:00:00+00:00,0.5429999999999999,B,0.0882,1.26e-05,123.631
78fBP0oLehKiEG7h4ohBIp,Jangan Pernah,32,318187,0,['Speak Up'],2008-01-01 00:00:00+00:00,0.429,D,0.00147,2.71e-05,105.04899999999999
4pmBTtmicaLv7P3pRXnwRe,Pacarku Superstar,50,267240,0,['Project Pop'],2008-01-01 00:00:00+00:00,0.537,C,0.52,0.0,169.735
1TW8loyyFySIb5Ra41sCsn,Malam Terakhir,32,497733,0,"['Agung', 'Dwi Ratna']",2008-01-01 00:00:00+00:00,0.33299999999999996,F,0.36200000000000004,0.253,157.197
3LUCCjAyXpgpH250Fylcpb,Historia de un amor,55,197947,0,['Diego El Cigala'],2008-01-01 00:00:00+00:00,0.588,A,0.7829999999999999,0.0016899999999999999,128.075
4O7Vc8KPNrBiJ1KTIBX3jg,Bakit Nga Ba Mahal Kita,42,297195,0,['Laarni Lozada'],2008-01-01 00:00:00+00:00,0.49,A#,0.764,4.7600000000000005e-05,134.064
3H1t4eL7FSYrbDrkstyTka,เพลงสุดท้าย,24,232053,0,['Tattoo Colour'],2008-01-01 00:00:00+00:00,0.711,A,0.331,0.0,118.04299999999999
1v7RbmAqVN9owqISrwN2jG,เปิดเพลงไหน เปิดเมื่อไหร่ ก็ยังสวยงาม,26,160067,0,['Tattoo Colour'],2008-01-01 00:00:00+00:00,0.637,B,0.13699999999999998,0.0,165.02
1oTjIkOc4yUb3osymxMkq6,Glossa Epikinonias,24,286534,0,['Giannis Tassios'],2008-01-01 00:00:00+00:00,0.8190000000000001,C#,0.14800000000000002,0.0,91.001

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  9714.000000  9.714000e+03  9714.000000   9714.000000   9714.000000       9714.000000  9714.000000
mean     36.055693  2.392139e+05     0.049001      0.589766      0.311432          0.056310   122.234493
std      15.339189  8.658097e+04     0.215882      0.156201      0.298800          0.191350    29.146793
min       0.000000  1.846700e+04     0.000000      0.000000      0.000001          0.000000     0.000000
25%      27.000000  1.980735e+05     0.000000      0.485000      0.039000          0.000000    98.603000
50%      37.000000  2.317400e+05     0.000000      0.599000      0.211000          0.000003   122.123000
75%      46.000000  2.685835e+05     0.000000      0.703000      0.546000          0.000577   139.974750
max      86.000000  2.677054e+06     1.000000      0.985000      0.996000          1.000000   218.320000
