---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.7
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.7.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.7.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.7.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 9744 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 9744 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
5z6C7bb9LcJpxE9b4D661s,Infinity - Spectral Emotions Remix,0,289283,0,['Thomas P. Heckmann'],2012-01-01 00:00:00+00:00,0.613,G,0.0016600000000000002,0.0183,152.053
23KtEcRNrUWAtvxNlxuavx,As The Years Go Passing By - 2002 Digital Remaster,9,464400,0,['Gary Moore'],2012-01-01 00:00:00+00:00,0.42700000000000005,F,0.0988,0.198,141.372
2ri0wuEhHwuGC1imOtDDhx,פרחים בקנה,22,285573,0,"['Subliminal', 'The Shadow', 'Sivan', 'Itzik Shamli', 'Gavriel Butler']",2012-01-01 00:00:00+00:00,0.6559999999999999,G#,0.244,0.0,110.04299999999999
2uViVTNHdYYoUzlBfeqbZh,Sleepwalker - Mental Remix,0,434233,0,['Thomas P. Heckmann'],2012-01-01 00:00:00+00:00,0.555,D,3.6099999999999997e-05,0.898,143.481
1JjSDrtYYCBi5yr6lIMppN,La Hora del Juicio,50,232072,0,['Canserbero'],2012-01-01 00:00:00+00:00,0.706,A#,0.146,0.000755,93.431
3q2v8QaTnHLveAQzR6gvYm,"Sing About Me, I'm Dying Of Thirst",61,723573,1,['Kendrick Lamar'],2012-01-01 00:00:00+00:00,0.654,B,0.303,8.08e-05,110.72200000000001
0yzhOPf0iw2qWwcXRRta5L,Rhapsody In Blue,57,890000,0,"['George Gershwin', 'Benjamin Grosvenor', 'Royal Liverpool Philharmonic Orchestra', 'James Judd']",2012-01-01 00:00:00+00:00,0.309,A,0.976,0.69,74.568
03YZ9NzElsztRw1pQasLDS,Brain Waves,0,204595,0,['Thomas P. Heckmann'],2012-01-01 00:00:00+00:00,0.6970000000000001,G,0.00217,0.894,196.398
7K1ZJlEZ2Nw9BrPHLyEmvC,Divina Tú,52,263440,0,['Carlos Macías'],2012-01-01 00:00:00+00:00,0.391,B,0.919,1.08e-06,82.96799999999999
7E4tE303U4LTUAsvzGVfxZ,Wonderland,0,479392,0,['Thomas P. Heckmann'],2012-01-01 00:00:00+00:00,0.563,B,0.000324,0.853,143.556
5v5Kra9bZOVKBXpfLVK2fP,Canção De Engate - Acoustic,44,324733,0,['Tiago Bettencourt'],2012-01-01 00:00:00+00:00,0.289,G#,0.259,0.0351,149.855
6IBpFG2LU2udYofIuROp3w,Lost In The Light,70,236720,0,['Bahamas'],2012-01-01 00:00:00+00:00,0.597,D,0.7929999999999999,0.0014,75.545
03d1qH5qlwuBw6trsfbjkM,The Hungry Years - Live,7,242053,0,['Neil Sedaka'],2012-01-01 00:00:00+00:00,0.379,C,0.9129999999999999,0.000143,78.575
0BEyccSds3Qxz7bCXcKqyy,"Oh, Angeline",2,197693,0,['Shoes'],2012-01-01 00:00:00+00:00,0.5379999999999999,C,0.498,0.000152,126.954
0Ksj1ehwR3eJl6L3bB9VZk,Losha,21,218469,0,['Andrea'],2012-01-01 00:00:00+00:00,0.61,F#,0.467,0.0819,94.985
74tLlkN3rgVzRqQJgPfink,Money Trees,72,386907,1,"['Kendrick Lamar', 'Jay Rock']",2012-01-01 00:00:00+00:00,0.716,G,0.0703,0.0,71.994
6yR4OhiJYiH9YXOgv8MO0A,Donde está el amor,52,225013,0,['Pablo Alborán'],2012-01-01 00:00:00+00:00,0.647,E,0.239,2.14e-06,140.001
2ztQXBIKkXroeSBD69XhOK,Trans-Form,0,429136,0,['Thomas P. Heckmann'],2012-01-01 00:00:00+00:00,0.693,G,0.00183,0.846,131.134
0hb9rwJj53EVIfUcruLsMV,Mujer De Las Mil Batallas,50,212653,0,['Manuel Carrasco'],2012-01-01 00:00:00+00:00,0.521,C,0.0603,0.0,139.78
3wyMwEpzoIWBGqEkHeEvi6,The Promise,54,224111,0,['Girls Aloud'],2012-01-01 00:00:00+00:00,0.575,A,0.008,0.0,90.036
1b5ZowScLd0KJpLBqY6Fon,Age,0,431547,0,['Thomas P. Heckmann'],2012-01-01 00:00:00+00:00,0.688,F,0.00233,0.9059999999999999,131.27
442YgzY4YBcE3UXFRrczJb,Casual Sex,48,193573,0,['My Darkest Days'],2012-01-01 00:00:00+00:00,0.6709999999999999,B,0.00912,0.0,116.04
0d0jsoba88SpOoFxCxA2rZ,The Art of Peer Pressure,58,324533,1,['Kendrick Lamar'],2012-01-01 00:00:00+00:00,0.555,A#,0.28600000000000003,0.00106,94.939
7gQ5c5HY6zMsIck6QLY9dJ,Hurricane,72,243987,0,['Bridgit Mendler'],2012-01-01 00:00:00+00:00,0.757,G,0.0398,2.63e-06,95.01
6M7bXLGi2e3QKHLwZTTmEN,Twilight,55,207952,0,['Cover Drive'],2012-01-01 00:00:00+00:00,0.425,G,0.00821,0.00047999999999999996,89.05799999999999
5UfSMQblqlnvLDlBGp2HPQ,Walkabout - 2012 Remaster,5,431752,0,['Edgar Froese'],2012-01-01 00:00:00+00:00,0.151,A,0.83,0.985,188.55599999999998
2qe6x1RtVj0rUib203guni,Trope III - Unreleased Mix,0,388211,0,['Thomas P. Heckmann'],2012-01-01 00:00:00+00:00,0.627,C,0.0336,0.8079999999999999,135.921
447r2keRxpkINmWYp83MlH,Maquiavélico,69,284709,0,['Canserbero'],2012-01-01 00:00:00+00:00,0.5539999999999999,B,0.544,0.0,92.90700000000001
6Ymvlzom4TQeoKqAWsZRD8,Somethin' 'Bout A Truck,70,213827,0,['Kip Moore'],2012-01-01 00:00:00+00:00,0.5539999999999999,B,0.0697,0.0,176.01
3pfGTMNDUJwj4cBN6op9m6,No Hay 2 Sin 3 (Gol),47,226653,0,"['Cali Y El Dandee', 'David Bisbal']",2012-01-01 00:00:00+00:00,0.642,C,0.0333,0.0,126.07700000000001
50vrx3zL8St5TnrJq3CFMC,אגדת דשא - Live,23,337653,0,"['Shalom Hanoch', 'Moshe Levi']",2012-01-01 00:00:00+00:00,0.423,C#,0.865,3.73e-06,123.132
1zZLRpTzRTqPQ7G7uxYI9Y,Angeleyes,56,262493,0,['ABBA'],2012-01-01 00:00:00+00:00,0.711,B,0.49700000000000005,0.000254,133.157
3l2K1gEKG6wwrguFthojTd,Desfado,38,155520,0,['Ana Moura'],2012-01-01 00:00:00+00:00,0.7040000000000001,D,0.261,0.0,119.874
3tolNJf26RqEWwVwlbJrY3,Tequila Makes Her Clothes Fall Off,37,188587,0,['Nathan Carter'],2012-01-01 00:00:00+00:00,0.628,F,0.0292,0.0,95.008
4hdIORk57S3av6dKI9JRDz,Prefiero Ser Su Amante,69,208000,0,['María José'],2012-01-01 00:00:00+00:00,0.632,C,0.00128,1.4599999999999999e-05,131.988
6rvKR6qk4pEUDR9N38Dsr2,Upland - 2012 Remaster,9,397665,0,['Edgar Froese'],2012-01-01 00:00:00+00:00,0.263,A,0.746,0.9059999999999999,118.12899999999999
7ypaYozVuw2UumW5tw07sy,Louisiana Saturday Night,37,167288,0,['Robert Mizzell'],2012-01-01 00:00:00+00:00,0.536,D,0.66,0.0,175.09799999999998
0YHO4FoviUi3v4q5d81bS1,Lost In Your Love,52,229436,0,['Redlight'],2012-01-01 00:00:00+00:00,0.705,F#,0.0491,0.0063100000000000005,133.83
5g7rJvWYVrloJZwKiShqlS,Dirty Paws,71,278373,0,['Of Monsters and Men'],2012-01-01 00:00:00+00:00,0.359,D#,0.107,0.0124,111.709
2ikkgfIIM9kGKZCXzXnTpj,I Don't Like,67,293840,1,"['Chief Keef', 'Lil Reese']",2012-01-01 00:00:00+00:00,0.742,D,0.000634,0.0,131.986

Resumen numérico:
        popularity   duration_ms     explicit  danceability  acousticness  instrumentalness        tempo
count  9744.000000  9.744000e+03  9744.000000   9744.000000   9744.000000       9744.000000  9744.000000
mean     37.055829  2.370632e+05     0.067939      0.591974      0.278499          0.088549   122.507633
std      18.219441  9.849530e+04     0.251655      0.153033      0.294817          0.243825    28.452681
min       0.000000  1.364000e+04     0.000000      0.000000      0.000000          0.000000     0.000000
25%      29.000000  1.964930e+05     0.000000      0.493000      0.024675          0.000000    99.253500
50%      40.000000  2.274145e+05     0.000000      0.600000      0.159000          0.000002   124.995000
75%      49.000000  2.652500e+05     0.000000      0.703250      0.482250          0.001090   139.801750
max      85.000000  4.397767e+06     1.000000      0.986000      0.995000          0.997000   217.963000
