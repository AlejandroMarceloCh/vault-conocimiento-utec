---
curso: BIGDATA
titulo: 06 - Semana 4/spotify_parquet_1__part.15
slides: 0
fuente: 06 - Semana 4/spotify_parquet_1__part.15.parquet
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 06 - Semana 4/spotify_parquet_1__part.15.parquet. -->

<!-- INTERPRETAR: datos tabulares de spotify_parquet_1__part.15.parquet. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: parquet
Filas: 13937 · Columnas: 12
Columnas y tipos: id (object), name (object), popularity (int64), duration_ms (int64), explicit (int64), artists (object), release_date (datetime64[us, UTC]), danceability (float64), key (object), acousticness (float64), instrumentalness (float64), tempo (float64)

Muestra (primeras 40 de 13937 filas, formato CSV):
id,name,popularity,duration_ms,explicit,artists,release_date,danceability,key,acousticness,instrumentalness,tempo
0VoyCzfd4M5p23pu5HL1Vy,Can't Stop This Feeling (Deep House Dance Party Remix),25,185803,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.637,G#,0.00839,0.0777,123.912
2m50HsnzEczYBaYrcf7duI,מים שקופים,48,180880,0,['Omer Adam'],2020-01-01 00:00:00+00:00,0.625,B,0.47,0.0,91.60600000000001
1HibPS9XZcq91JkEFVNdHx,המלכה של השכונה,41,155427,0,['Omer Adam'],2020-01-01 00:00:00+00:00,0.7859999999999999,F#,0.24100000000000002,0.0,111.992
1QD7KtRE3D1IUHhPsSRpz5,I Have a Dream (Deep House Dance Party Remix),25,141640,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.809,G,0.0119,0.8370000000000001,122.01
5pFAe3583L3RgD4UBczqrC,Searching,0,254280,0,['The Silent Deeds'],2020-01-01 00:00:00+00:00,0.42100000000000004,E,0.0008550000000000001,0.000213,125.00399999999999
3ySvEhEJcZWX6enZTpkzXW,Sweet September,0,215571,0,['The Silent Deeds'],2020-01-01 00:00:00+00:00,0.408,B,0.000951,0.0648,170.005
18Ni5EvqrJesPqVv6HwZg3,"Home - 132 Bpm, 32 Count Pro Edition",16,192772,0,['Gym Workout DJ Team'],2020-01-01 00:00:00+00:00,0.5870000000000001,B,0.0018899999999999998,0.0514,131.983
7oIkxPZosfmpJM86sfytEC,Pergi Hilang Dan Lupakan,51,287974,0,['Vita Alvia'],2020-01-01 00:00:00+00:00,0.759,C,0.00506,1.77e-05,110.001
1FARiXM2DUyVE7vCa4BXjZ,אין סופים טובים,40,209014,0,['Omer Adam'],2020-01-01 00:00:00+00:00,0.679,A,0.23399999999999999,0.0,109.07799999999999
5saAn4DemGjEgtGFHJX7U6,Отиваш си,32,244288,0,"['Emilia', 'Toni Storaro']",2020-01-01 00:00:00+00:00,0.703,D,0.177,3.3600000000000004e-05,141.91
1wDsCKx6DbevWBaHnHnw6U,Happy New Years (Let's Fall in Love Again) 2019,0,230885,0,['Jeff Kiefer'],2020-01-01 00:00:00+00:00,0.41200000000000003,A,0.16899999999999998,1.25e-05,130.06799999999998
0dikInIdkIx7DWsweSJpzQ,רסיסים - אקוסטי,41,189128,0,"['Keren Peles', 'Raviv Kaner']",2020-01-01 00:00:00+00:00,0.42100000000000004,A,0.9420000000000001,1.55e-06,76.342
5P0M3cOeFfsozvQZdPKvlA,"Check the Beat - 132 Bpm, 32 Count Pro Edition",15,206497,0,['Gym Workout DJ Team'],2020-01-01 00:00:00+00:00,0.601,F#,4.28e-06,0.815,132.029
1ShWT8ysXUqZVvCenbPUrJ,Darkness of the Night,0,199219,0,['The Silent Deeds'],2020-01-01 00:00:00+00:00,0.5429999999999999,G,0.0129,0.018000000000000002,128.00799999999998
0GmaOpCPWv7uDuTub2SNLU,יעשו לנו כבוד,42,200973,0,['Omer Adam'],2020-01-01 00:00:00+00:00,0.752,B,0.524,0.0,130.105
23OpaiKRC2kJxilO3Vykco,"The Box - 132 Bpm, 32 Count Pro Edition",17,178208,0,['Gym Workout DJ Team'],2020-01-01 00:00:00+00:00,0.568,C#,0.162,0.000225,131.97799999999998
0YBE89ytDgcVWtzknmokDB,רציתי שזה יכאיב,38,175000,0,['Roni Dalumi'],2020-01-01 00:00:00+00:00,0.645,D,0.109,0.0,192.055
7puPB5ixFOkP7nYysVqCU1,Oh Baby Baby (Electronic Dance Party Remix),25,219257,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.802,C#,0.00042699999999999997,0.182,116.007
73IHbP7MBz8BXsl3fXLKrZ,"Drop It - 132 Bpm, 32 Count Pro Edition",16,197744,0,['Gym Workout DJ Team'],2020-01-01 00:00:00+00:00,0.494,D,0.007659999999999999,0.862,132.143
09MtNaY1DcRqBumCkIRVND,שני משוגעים,50,170773,0,['Omer Adam'],2020-01-01 00:00:00+00:00,0.695,B,0.434,0.0,116.77600000000001
0U9axeaPpEKDK6IYeoakZ3,"Apollo - 132 Bpm, 32 Count Pro Edition",19,196904,0,['Gym Workout DJ Team'],2020-01-01 00:00:00+00:00,0.529,F#,0.0054,0.7490000000000001,131.906
4y3SXCuVXO8fj0BTSUzvy6,Let's Play (Deep House Dance Party Remix),24,185799,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.748,A#,0.125,0.882,124.005
6LlzRIPofOK1QDVQOomrpo,Follow Me (Chill Electronic Music Remix),24,216774,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.7390000000000001,G,0.0349,0.852,124.03299999999999
24BvlSG2Y36Heg1dwLwHtu,Uslanmıyor Bu,63,193083,0,['Zeynep Bastık'],2020-01-01 00:00:00+00:00,0.6970000000000001,G,0.503,0.0,86.0
20vk0FBPnnUXC4wjfMF9Zd,Thinking About You (Chill Deep House Remix),24,205724,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.644,F#,0.0573,0.9129999999999999,124.999
3HFBPDn9PDxqjqLzaolPrw,All My Life (Chill Electronic Music Remix),24,240004,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.648,G,0.0868,0.41,127.977
1JjUJUycDSFvZK0iWGWFW9,Baby You're One of a Kind (Chill Electronic Music Remix),25,230221,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.728,G,4.71e-05,0.56,125.023
56tHWxun34uJ4atMqfjUek,Paradise Like Islands in the Sky (Deep House Dance Party Remix),25,185806,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.8320000000000001,A,0.00639,0.25,124.01899999999999
6wccYNxf7oQlLj3hhBbIno,My Body Is so into You (Deep House Dance Party Remix),25,216774,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.615,A#,0.000225,0.823,124.009
2csxnlEoZThTmNF3Fa6wCd,Apakah Itu Cinta,54,311098,0,['Happy Asmara'],2020-01-01 00:00:00+00:00,0.7120000000000001,A#,0.0010199999999999999,0.1,114.993
01JYQhAS2nLXSdwVlB3nM7,The DJ Played My Favorite Song (Deep House Dance Party Remix),24,232257,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.802,D,0.19399999999999998,0.898,123.995
44pKbfoyixQSaiiJde9i1F,BEG,45,175924,0,"['Omer Adam', 'Netta']",2020-01-01 00:00:00+00:00,0.9159999999999999,C,0.0176,1.06e-05,100.005
5by3TCFHK3YRQzxpR9PcZ0,Caribe,59,140786,1,"['VillaBanks', 'Linch', 'Brando Luis']",2020-01-01 00:00:00+00:00,0.932,C,0.222,0.0,139.96200000000002
4r2M86IJ1stGAI55PRRib0,Balou,45,129061,0,['Benny Jamz'],2020-01-01 00:00:00+00:00,0.904,A#,0.13,0.00279,104.98200000000001
3Y3fjY7sfmHzNOyyTdECAr,"Here We Go! - 132 Bpm, 32 Count Pro Edition",11,194873,0,['Gym Workout DJ Team'],2020-01-01 00:00:00+00:00,0.529,B,4.6e-05,0.5479999999999999,131.977
1BuhfH6uUFbkUhfrMal38H,לשון הרע לא מדבר אליי,40,214760,0,['Omer Adam'],2020-01-01 00:00:00+00:00,0.584,C,0.5760000000000001,0.0,75.018
6O8AI2tOKLKQ6C3Emm2KAL,New Years 2020,12,187800,1,['meija'],2020-01-01 00:00:00+00:00,0.591,C,0.268,0.0,75.0
7CRAq7uALKmK3CDSMzpP39,I Just Want You Baby (Chill Electronic Music Remix),24,201295,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.738,A#,0.40299999999999997,0.9259999999999999,124.05799999999999
5LJ3F6BPFfwpjbzYQN2cIx,One More Time Hands up Hollywood (Electronic Dance Party Remix),25,254977,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.69,E,0.000332,0.0889,128.002
2Gl0xdYcjTkMnqEm687VZB,Lose My Defenses (Yoga & Pilates Chill Electronic Music Remix),25,185807,0,['Greg Sletteland'],2020-01-01 00:00:00+00:00,0.7070000000000001,D#,0.0875,0.935,124.01799999999999

Resumen numérico:
         popularity   duration_ms      explicit  danceability  acousticness  instrumentalness         tempo
count  13937.000000  1.393700e+04  13937.000000  13937.000000  13937.000000      13937.000000  13937.000000
mean      44.686948  2.039203e+05      0.217981      0.657129      0.271750          0.113089    122.364673
std       23.406207  8.716877e+04      0.412889      0.156209      0.275047          0.276204     28.267045
min        0.000000  2.268800e+04      0.000000      0.000000      0.000000          0.000000      0.000000
25%       35.000000  1.659200e+05      0.000000      0.557000      0.038400          0.000000     99.982000
50%       51.000000  1.966140e+05      0.000000      0.676000      0.175000          0.000002    123.003000
75%       61.000000  2.315930e+05      0.000000      0.772000      0.441000          0.001840    139.990000
max       97.000000  4.635478e+06      1.000000      0.986000      0.996000          1.000000    220.470000
