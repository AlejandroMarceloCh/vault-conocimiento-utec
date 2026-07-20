---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.1
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.1.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.1.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.1.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 8751 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 8751 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
3unIjdxPBJ27WvDSHOqaDn,Say It Right,39,223080,0,['Nelly Furtado'],2006-01-01 00:00:00+00:00,0.872,C#,0.0476,0.00112,116.948
7HCAJNB9VcFMvcwjYPh7pH,Écoute-moi camarade,45,405080,0,['Rachid Taha'],2006-01-01 00:00:00+00:00,0.5589999999999999,D#,0.524,0.00285,149.691
7FRdqCCoPxQuPT0wEuzmZw,Je regrette pas,38,247956,1,['Lim'],2006-01-01 00:00:00+00:00,0.494,G,0.0204,0.0,90.523
7zVjhnfcf8wXzBNcr4NRCG,Gabriel,42,213707,0,['Najoua Belyzel'],2006-01-01 00:00:00+00:00,0.69,F,0.00213,1.26e-06,120.02
6hdsNoZWIjPSjxcOnsjIxj,One Woman Man,48,272053,1,['Dave Hollister'],2006-01-01 00:00:00+00:00,0.627,B,0.0457,0.0,91.015
0bAM9qivrntXnHyklRRx39,World Spins Madly On,58,165133,0,"['The Weepies', 'Deb Talan', 'Steve Tannen']",2006-01-01 00:00:00+00:00,0.502,C#,0.617,4.3200000000000007e-05,107.61200000000001
26kF6FArQt20IFu3pdgYF6,Breakin' My Heart (Pretty Brown Eyes),41,355573,0,['Mint Condition'],2006-01-01 00:00:00+00:00,0.6459999999999999,G,0.131,3.39e-06,137.156
3SIE9pI55Qu4QE1eEyOZgO,Brand Suid-Afrika,21,200200,1,['Fokofpolisiekar'],2006-01-01 00:00:00+00:00,0.614,E,0.0271,0.0,140.055
3AZmrNo4aKNcBFQa67aSu0,Amor Combate,32,290093,0,['Linda Martini'],2006-01-01 00:00:00+00:00,0.424,A,8.669999999999999e-05,0.638,144.033
41sLy8IQUSgvjjeW2CN0vc,That's That Shit,57,257640,1,"['Snoop Dogg', 'R. Kelly']",2006-01-01 00:00:00+00:00,0.866,A,0.0199,0.0,82.044
0iYoK9q0WCueRWjdlVkjkN,No Tomorrow,47,167493,0,['Orson'],2006-01-01 00:00:00+00:00,0.6559999999999999,D#,0.0065,0.0,124.08200000000001
01PzTq42bzQBrEoNyYfsSo,Dansen,29,199133,0,['Spring'],2006-01-01 00:00:00+00:00,0.6729999999999999,D,0.0506,0.0,120.01
1UpUrh85poGgna4yamzSjl,"Vida Loka, Pt. 1 (Ao Vivo)",41,202173,0,"[""Racionais MC's""]",2006-01-01 00:00:00+00:00,0.461,A,0.498,0.0,79.163
58K761llMSSlZHvDMi1AYs,Nascer Outra Vez,30,196027,0,['Ritual Tejo'],2006-01-01 00:00:00+00:00,0.693,C#,0.0525,0.0,129.717
2HwQeoD5TPQvakAJ4uSN06,La ceinture - Radio Edit,48,213533,0,['Élodie Frégé'],2006-01-01 00:00:00+00:00,0.451,A,0.613,6.38e-06,95.25299999999999
4GGOc2urRBawIxSMrIqGGn,Premier Love,40,212347,0,"['Tony Parker', 'Rickwel']",2006-01-01 00:00:00+00:00,0.584,B,0.185,0.0,90.055
6tuiDRFaXOBqFLpeTBjAAn,Gold Lion,55,187133,0,['Yeah Yeah Yeahs'],2006-01-01 00:00:00+00:00,0.521,A,0.0223,5.54e-06,158.744
1IO7WmbmHJu4tJX1mZ1GTH,Chopis Centis - Live,41,146267,0,['Mamonas Assassinas'],2006-01-01 00:00:00+00:00,0.43200000000000005,D,0.00155,0.0,135.665
10hnzFqOkWifT35HfvbaNc,Le Mambo Du Décalco,41,214400,1,['Richard Gotainer'],2006-01-01 00:00:00+00:00,0.8540000000000001,B,0.322,0.0,124.74700000000001
3iOy5zzNirhedBMT715TDS,Here (In Your Arms),46,240614,0,['Hellogoodbye'],2006-01-01 00:00:00+00:00,0.705,F,0.193,0.00183,126.038
7tawDKBYV9059X92D6dr7R,Clumsy,57,240427,0,['Fergie'],2006-01-01 00:00:00+00:00,0.731,D,0.191,0.00042,184.00900000000001
2R4KCSHfWuYiCMSu9f0nuc,Conceited (There's Something About Remy),58,219560,1,['Remy Ma'],2006-01-01 00:00:00+00:00,0.7040000000000001,B,0.21600000000000003,0.0,123.855
4mv628DTPrlRfEbCx8VOjX,Mbulali Wami,22,331373,0,['Brenda Fassie'],2006-01-01 00:00:00+00:00,0.46299999999999997,G#,0.8640000000000001,0.0,147.86
2rwwGHau31uBDv18ehgWtT,Le misérable,44,280293,0,['Singuila'],2006-01-01 00:00:00+00:00,0.708,G#,0.355,0.0,82.969
7m8PDR3PRg5lPhWMdYrktc,Trouble Sleeping,56,208733,0,['Corinne Bailey Rae'],2006-01-01 00:00:00+00:00,0.636,F,0.14,0.0,90.97
5gvGLgjq8qnOkSSjF6t7Jm,Swanesang,21,208787,1,['Fokofpolisiekar'],2006-01-01 00:00:00+00:00,0.539,B,0.0532,2.4e-05,150.091
41Z1gnggllzvu7qOWTaSTE,Let Me Down Easy,55,175027,0,['Dennis Brown'],2006-01-01 00:00:00+00:00,0.743,G,0.049,1.25e-05,84.15899999999999
0Ek44VdlLSiO5MLWISwP5H,Higher And Higher ('93 Dance),20,262067,0,['Brenda Fassie'],2006-01-01 00:00:00+00:00,0.772,G,0.161,0.0002,105.34200000000001
7LgLKjsjGiTSevLhoB2JE3,We on Fire (feat. Bongz & Maggz),19,248120,1,"['Da Les', 'Bongz', 'Maggz']",2006-01-01 00:00:00+00:00,0.327,C#,0.00581,0.0,61.092
1nrIaUgk4D5gI1yqQcsu3W,Don't Look Any Further - Single Version,48,243480,0,"['Dennis Edwards', 'Siedah Garrett']",2006-01-01 00:00:00+00:00,0.753,A,0.0426,0.0037,95.14399999999999
3moelwvWkm8rliDyjywgA1,Les voisines,47,215813,0,['Renan Luce'],2006-01-01 00:00:00+00:00,0.855,C#,0.139,5.13e-06,127.031
5A0FBlAHem8zIi4XF7Mjnz,Ma nature,39,279893,0,['Singuila'],2006-01-01 00:00:00+00:00,0.64,B,0.0882,0.0,83.023
4rino0wsmUcK36Ro4CCrke,Boten Anna - Radio edit,49,207067,0,['Basshunter'],2006-01-01 00:00:00+00:00,0.46399999999999997,A,0.0635,0.00010800000000000001,140.179
0FNPiAAdWdWaGr7JOnlKmi,Imagine,58,282187,1,"['Snoop Dogg', 'Dr. Dre', ""D'Angelo""]",2006-01-01 00:00:00+00:00,0.8029999999999999,F#,0.28600000000000003,0.0,87.105
2sY0M3k69oAYz7EOPVRFjo,Big Girl (You Are Beautiful),53,248000,0,['MIKA'],2006-01-01 00:00:00+00:00,0.797,B,0.0384,0.0,116.005
5as4m1rmKAmL2jbECYkZKB,Het Is Een Nacht,42,279387,0,['Guus Meeuwis'],2006-01-01 00:00:00+00:00,0.361,G,0.0997,0.0,140.495
0DLjcGTmH2NV9AjzecAGT6,Breathe Into Me,54,214373,0,['Red'],2006-01-01 00:00:00+00:00,0.32,A,0.000997,0.0,165.94299999999998
3g6SuyjGaGyAXmjvdNI1IU,4 Minutes,47,240320,0,['Avant'],2006-01-01 00:00:00+00:00,0.828,A#,0.0942,0.0,119.969
0Kt0khTz1EzjtaQI8A339S,Starz In Their Eyes,53,295933,0,['Just Jack'],2006-01-01 00:00:00+00:00,0.67,D#,0.0018399999999999998,0.000356,123.802
6KQ7dIdBJnpLQg9HZfNP1s,"Morning Star, Durbanville",20,236307,1,['Fokofpolisiekar'],2006-01-01 00:00:00+00:00,0.529,E,0.128,0.000121,130.058

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  8751.000000  8.751000e+03  8751.000000   8751.000000   8751.000000       8751.000000  8751.000000
mean     37.707576  2.402309e+05     0.050851      0.591191      0.306093          0.050078   121.663809
std      14.341718  8.843522e+04     0.219707      0.157146      0.295423          0.181781    29.401709
min       0.000000  6.373000e+03     0.000000      0.000000      0.000000          0.000000     0.000000
25%      29.000000  2.013665e+05     0.000000      0.488000      0.039600          0.000000    97.418000
50%      38.000000  2.335730e+05     0.000000      0.595000      0.210000          0.000002   120.054000
75%      47.000000  2.700600e+05     0.000000      0.705500      0.526000          0.000308   139.996500
max      82.000000  4.368000e+06     1.000000      0.973000      0.995000          0.988000   215.680000
