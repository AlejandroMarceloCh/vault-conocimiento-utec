---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.2
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.2.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.2.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.2.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 8770 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 8770 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
2z0z5ddJS3K7qvhp4PH0Aa,Dímelo,57,217933,0,['Enrique Iglesias'],2007-01-01 00:00:00+00:00,0.7829999999999999,G#,0.0608,0.0,114.994
5Dw7Va6ij1yIh6tyMRpmLC,This Heart Attack,43,228949,0,['Faker'],2007-01-01 00:00:00+00:00,0.628,C#,0.0236,0.0,122.006
5FKEkZ0pxjgTVKRDCCeI7S,Antara Ada Dan Tiada (Acoustic),43,235173,0,['Utopia'],2007-01-01 00:00:00+00:00,0.573,D#,0.894,0.0,135.1
2QdroWlsR6FSUBPkf0019J,Melankolia,41,316757,0,['Efek Rumah Kaca'],2007-01-01 00:00:00+00:00,0.529,A,0.0909,0.0482,85.064
2a03afRiyAbNAleOByVju4,Get It Shawty - Main,62,209533,0,['Lloyd'],2007-01-01 00:00:00+00:00,0.8220000000000001,F,0.12300000000000001,0.0,128.014
2XNyz6up4JxH6m6xmYX8wr,Cuatro Lagrimas,44,187173,0,['Los Polifaceticos'],2007-01-01 00:00:00+00:00,0.491,A#,0.534,0.0,89.666
2yWWax89EXuozdykv8bkZx,Maafkanlah,35,328867,0,['Chrisye'],2007-01-01 00:00:00+00:00,0.517,A,0.44,0.0,83.785
1SyJOVMjGCY8m9IfD8YErg,Where I Stood,45,259120,0,['Missy Higgins'],2007-01-01 00:00:00+00:00,0.55,A,0.65,0.000475,72.001
7fhtTFiFHbssNu77aD1ttG,Erga'aly,46,230975,0,['Tamer Hosny'],2007-01-01 00:00:00+00:00,0.659,F,0.588,0.0,133.91299999999998
6jd8pQtqvUTPur4ghRTfgV,Bulldoze The Gates,0,243067,0,['Tunghook'],2007-01-01 00:00:00+00:00,0.36200000000000004,F#,9.4e-05,0.133,135.67600000000002
67RXeJMvUPAJWrWjJ6idKy,Lost Without U,27,254587,0,['Robin Thicke'],2007-01-01 00:00:00+00:00,0.8740000000000001,C,0.205,2.58e-06,113.256
539dFCMA8lfEElDPgGpcIB,All My Friends Say,61,242800,0,['Luke Bryan'],2007-01-01 00:00:00+00:00,0.6829999999999999,A,0.0439,0.0,117.036
3xobxzE4YMCWupZWtROkPC,Tunggara,34,322653,0,['Evie Tamala'],2007-01-01 00:00:00+00:00,0.539,C,0.361,0.00634,182.6
6Efh7DYf2U7e6etkdZlnAr,空洞です,43,284827,0,['Yura Yura Teikoku'],2007-01-01 00:00:00+00:00,0.605,C#,0.0371,0.007529999999999999,86.815
5GZimNKDnE8Gf5sL10oTgB,Lost And Running,46,222160,0,['Powderfinger'],2007-01-01 00:00:00+00:00,0.54,F,6.500000000000001e-05,0.0006,120.096
4B1mxA6kbelF6cO7hYbpXH,Podvod,38,227627,0,['Brontosauri'],2007-01-01 00:00:00+00:00,0.595,F#,0.828,9.279999999999999e-05,111.774
1OzSfjFW08DTD51XoNnog7,"That's How You Know - From ""Enchanted""/Soundtrack Version",61,228960,0,['Amy Adams'],2007-01-01 00:00:00+00:00,0.485,D,0.49700000000000005,0.0,174.025
06Vw2ZOhalTwEw4PhoGRSX,Proper Education - Radio Edit,49,198567,0,"['Eric Prydz', 'Floyd']",2007-01-01 00:00:00+00:00,0.537,C,0.0010199999999999999,0.035,124.93799999999999
525sHGS4t4GYsFvD3TDWHZ,Baby Doll,43,208827,0,['Utopia'],2007-01-01 00:00:00+00:00,0.625,G,0.0164,0.00625,140.049
1MErjfceWn1tHKLRUtrAoW,Tersesal,35,270680,0,['J-Rocks'],2007-01-01 00:00:00+00:00,0.20600000000000002,A,0.0466,0.0014,179.995
1rOlTL4pKQ9Y1fURua4AJR,My Body Is a Cage,61,287240,0,['Arcade Fire'],2007-01-01 00:00:00+00:00,0.29600000000000004,C,0.315,0.0551,81.045
0IEPZKXzr9GU0yTHVBJhSQ,I Want Your Soul,27,399547,0,['Armand Van Helden'],2007-01-01 00:00:00+00:00,0.742,F#,0.00441,0.135,127.985
3PvXKOAq4pUJSF6pAaNIDU,Королевна,41,319253,0,['Мельница'],2007-01-01 00:00:00+00:00,0.62,A,0.8859999999999999,0.0,89.99799999999999
7kyga1JSeqifKDmZvGPqkk,Евпатория,43,262973,0,['Lyapis Trubetskoy'],2007-01-01 00:00:00+00:00,0.5660000000000001,C,0.106,0.0,143.05100000000002
2kwUv2q1sTjHLJWRRHU4ZL,"Ну, вот и все",41,244960,0,['Stas Mikhaylov'],2007-01-01 00:00:00+00:00,0.616,F#,0.0577,0.0,96.001
665hS472Z8rbt2GOUD40LN,"I Don't Feel Like Dancin' - Live At The O2, London, UK / 2007",2,319227,0,['Scissor Sisters'],2007-01-01 00:00:00+00:00,0.552,G,0.0207,0.0,108.104
2OikDCslmF1Y04Szgbc8Hl,"Sol, Playa Y Arena",61,188320,0,"['Tito ""El Bambino""']",2007-01-01 00:00:00+00:00,0.8220000000000001,F,0.254,0.0,94.039
12hNVeWLSUXzOySe86H2KI,Le Festin,50,170787,0,"['Camille', 'Michael Giacchino']",2007-01-01 00:00:00+00:00,0.43799999999999994,D#,0.861,0.0,138.327
064NEtcV4JQqGxAtfqvRfI,Beautiful Girls,61,241933,0,['Sean Kingston'],2007-01-01 00:00:00+00:00,0.745,A,0.159,0.0,129.995
3reoq3Kp45545OlqZBk93X,Destination Calabria - Radio Edit,36,226000,0,"['Alex Gaudino', 'Crystal Waters']",2007-01-01 00:00:00+00:00,0.616,D,0.0015199999999999999,0.00074,128.017
6NBYhdjusY35KqDYsRbWiq,Juwita,43,321347,0,['Chrisye'],2007-01-01 00:00:00+00:00,0.5479999999999999,E,0.309,3.45e-05,118.975
6emutKYT46P70CyE4GSUlg,Hey Gadis,34,237253,0,['SAMSONS'],2007-01-01 00:00:00+00:00,0.605,F#,0.0556,2.3e-06,161.971
1rzbw9C6dfXwsikiMFFGiC,Mentiras,61,237293,0,['Daniela Romo'],2007-01-01 00:00:00+00:00,0.728,G,0.34600000000000003,0.0,140.705
4DWpMoergobRbp0B0UKkBB,"Kiss You Off - Live At The O2, London, UK / 2007",0,289187,0,['Scissor Sisters'],2007-01-01 00:00:00+00:00,0.517,D,0.000275,0.00024700000000000004,133.497
4GydCOsiJbCmUZJuMpOMrn,Город Сочи,47,181440,0,['Sergey Trofimov'],2007-01-01 00:00:00+00:00,0.792,D,0.113,0.0,125.97
4bEvavgsQbygAflrqeh5eE,Cumantel Bae,34,371107,0,['Evie Tamala'],2007-01-01 00:00:00+00:00,0.6579999999999999,A,0.423,0.0354,98.14399999999999
6e9LlPpmqVo68bc0GdU9oT,Eras Una Niña,61,182187,0,"['Nigga', 'Japanesse']",2007-01-01 00:00:00+00:00,0.7490000000000001,G,0.22699999999999998,0.0,89.399
0Qzkm9CSXwK2Fk3Gm0ioDA,Historias De Danzón Y De Arrabal,61,326798,0,['Aleks Syntek'],2007-01-01 00:00:00+00:00,0.76,C,0.397,0.000399,115.01799999999999
5nvS1vouQkX0HxOohfqCoS,Tren Al Sur,63,338253,0,['Los Prisioneros'],2007-01-01 00:00:00+00:00,0.585,A,0.00418,0.0229,180.503
6aesfC1W4QKbg56BH5bz5S,Pero la Recuerdo,48,229304,0,['Pancho Barraza'],2007-01-01 00:00:00+00:00,0.654,F,0.0408,2.12e-05,189.649

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  8770.000000  8.770000e+03  8770.000000   8770.000000   8770.000000       8770.000000  8770.000000
mean     38.077879  2.425776e+05     0.039681      0.590611      0.310254          0.052330   121.781046
std      13.985028  9.492847e+04     0.195219      0.155011      0.299126          0.184447    29.310103
min       0.000000  3.027900e+04     0.000000      0.075400      0.000002          0.000000    36.690000
25%      30.000000  2.020832e+05     0.000000      0.491000      0.036200          0.000000    97.927000
50%      39.000000  2.331470e+05     0.000000      0.598500      0.213000          0.000003   120.975000
75%      47.000000  2.701838e+05     0.000000      0.700000      0.541750          0.000413   140.005500
max      83.000000  3.600120e+06     1.000000      0.983000      0.996000          0.989000   216.674000
