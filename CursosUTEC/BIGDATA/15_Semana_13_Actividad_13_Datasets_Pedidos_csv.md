---
curso: BIGDATA
titulo: 15 - Semana 13/Actividad_13_Datasets__Pedidos
slides: 0
fuente: 15 - Semana 13/Actividad_13_Datasets__Pedidos.csv
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 15 - Semana 13/Actividad_13_Datasets__Pedidos.csv. -->

<!-- INTERPRETAR: datos tabulares de Actividad_13_Datasets__Pedidos.csv. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: csv
Filas: 830 · Columnas: 14
Columnas y tipos: IdPedido (int64), IdCliente (object), IdEmpleado (int64), FechaPedido (object), FechaEntrega (object), FechaEnvío (object), FormaEnvío (int64), Cargo (int64), Destinatario (object), DirecciónDestinatario (object), CiudadDestinatario (object), RegiónDestinatario (object), CódPostalDestinatario (object), PaísDestinatario (object)

Muestra (primeras 40 de 830 filas, formato CSV):
IdPedido,IdCliente,IdEmpleado,FechaPedido,FechaEntrega,FechaEnvío,FormaEnvío,Cargo,Destinatario,DirecciónDestinatario,CiudadDestinatario,RegiónDestinatario,CódPostalDestinatario,PaísDestinatario
10248,WILMK,5,4/7/1996 00:00:00,1/8/1996 00:00:00,16/7/1996 00:00:00,3,32,Wilman Kala,Keskuskatu 45,Helsinki,,21240,Finlandia
10249,TOMSP,6,5/7/1996 00:00:00,16/8/1996 00:00:00,10/7/1996 00:00:00,1,12,Toms Spezialitäten,Luisenstr. 48,Münster,,44087,Alemania
10250,HANAR,4,8/7/1996 00:00:00,5/8/1996 00:00:00,12/7/1996 00:00:00,2,66,Hanari Carnes,"Rua do Paço, 67",Río de Janeiro,RJ,05454-876,Brasil
10251,VICTE,3,8/7/1996 00:00:00,5/8/1996 00:00:00,15/7/1996 00:00:00,1,41,Victuailles en stock,"2, rue du Commerce",Lyon,,69004,Francia
10252,SUPRD,4,9/7/1996 00:00:00,6/8/1996 00:00:00,11/7/1996 00:00:00,2,51,Suprêmes délices,"Boulevard Tirou, 255",Charleroi,,B-6000,Bélgica
10253,HANAR,3,10/7/1996 00:00:00,24/7/1996 00:00:00,16/7/1996 00:00:00,2,58,Hanari Carnes,"Rua do Paço, 67",Río de Janeiro,RJ,05454-876,Brasil
10254,CHOPS,5,11/7/1996 00:00:00,8/8/1996 00:00:00,23/7/1996 00:00:00,2,23,Chop-suey Chinese,Hauptstr. 31,Bern,,3012,Suiza
10255,RICSU,9,12/7/1996 00:00:00,9/8/1996 00:00:00,15/7/1996 00:00:00,3,148,Richter Supermarkt,Starenweg 5,Genève,,1204,Suiza
10256,WELLI,3,15/7/1996 00:00:00,12/8/1996 00:00:00,17/7/1996 00:00:00,2,14,Wellington Importadora,"Rua do Mercado, 12",Resende,SP,08737-363,Brasil
10257,HILAA,4,16/7/1996 00:00:00,13/8/1996 00:00:00,22/7/1996 00:00:00,3,82,HILARIÓN-Abastos,Carrera 22 con Ave. Carlos Soublette #8-35,San Cristóbal,Táchira,5022,Venezuela
10258,ERNSH,1,17/7/1996 00:00:00,14/8/1996 00:00:00,23/7/1996 00:00:00,1,141,Ernst Handel,Kirchgasse 6,Graz,,8010,Austria
10259,CENTC,4,18/7/1996 00:00:00,15/8/1996 00:00:00,25/7/1996 00:00:00,3,3,Centro comercial Moctezuma,Sierras de Granada 9993,México D.F.,,05022,México
10260,OTTIK,4,19/7/1996 00:00:00,16/8/1996 00:00:00,29/7/1996 00:00:00,1,55,Ottilies Käseladen,Mehrheimerstr. 369,Köln,,50739,Alemania
10261,QUEDE,4,19/7/1996 00:00:00,16/8/1996 00:00:00,30/7/1996 00:00:00,2,3,Que Delícia,"Rua da Panificadora, 12",Río de Janeiro,RJ,02389-673,Brasil
10262,RATTC,8,22/7/1996 00:00:00,19/8/1996 00:00:00,25/7/1996 00:00:00,3,48,Rattlesnake Canyon Grocery,2817 Milton Dr.,Albuquerque,NM,87110,Estados Unidos
10263,ERNSH,9,23/7/1996 00:00:00,20/8/1996 00:00:00,31/7/1996 00:00:00,3,146,Ernst Handel,Kirchgasse 6,Graz,,8010,Austria
10264,FOLKO,6,24/7/1996 00:00:00,21/8/1996 00:00:00,23/8/1996 00:00:00,3,4,Folk och fä HB,Åkergatan 24,Bräcke,,S-844 67,Suecia
10265,BLONP,2,25/7/1996 00:00:00,22/8/1996 00:00:00,12/8/1996 00:00:00,1,55,Blondel père et fils,"24, place Kléber",Strasbourg,,67000,Francia
10266,WARTH,3,26/7/1996 00:00:00,6/9/1996 00:00:00,31/7/1996 00:00:00,3,26,Wartian Herkku,Torikatu 38,Oulu,,90110,Finlandia
10267,FRANK,4,29/7/1996 00:00:00,26/8/1996 00:00:00,6/8/1996 00:00:00,1,209,Frankenversand,Berliner Platz 43,München,,80805,Alemania
10268,GROSR,8,30/7/1996 00:00:00,27/8/1996 00:00:00,2/8/1996 00:00:00,3,66,GROSELLA-Restaurante,5ª Ave. Los Palos Grandes,Caracas,DF,1081,Venezuela
10269,WHITC,5,31/7/1996 00:00:00,14/8/1996 00:00:00,9/8/1996 00:00:00,1,5,White Clover Markets,1029 - 12th Ave. S.,Seattle,WA,98124,Estados Unidos
10270,WARTH,1,1/8/1996 00:00:00,29/8/1996 00:00:00,2/8/1996 00:00:00,1,137,Wartian Herkku,Torikatu 38,Oulu,,90110,Finlandia
10271,SPLIR,6,1/8/1996 00:00:00,29/8/1996 00:00:00,30/8/1996 00:00:00,2,5,Split Rail Beer & Ale,P.O. Box 555,Lander,WY,82520,Estados Unidos
10272,RATTC,6,2/8/1996 00:00:00,30/8/1996 00:00:00,6/8/1996 00:00:00,2,98,Rattlesnake Canyon Grocery,2817 Milton Dr.,Albuquerque,NM,87110,Estados Unidos
10273,QUICK,3,5/8/1996 00:00:00,2/9/1996 00:00:00,12/8/1996 00:00:00,3,76,QUICK-Stop,Taucherstraße 10,Cunewalde,,01307,Alemania
10274,VINET,6,6/8/1996 00:00:00,3/9/1996 00:00:00,16/8/1996 00:00:00,1,6,Vins et alcools Chevalier,59 rue de l'Abbaye,Reims,,51100,Francia
10275,MAGAA,1,7/8/1996 00:00:00,4/9/1996 00:00:00,9/8/1996 00:00:00,1,27,Magazzini Alimentari Riuniti,Via Ludovico il Moro 22,Bérgamo,,24100,Italia
10276,TORTU,8,8/8/1996 00:00:00,22/8/1996 00:00:00,14/8/1996 00:00:00,3,14,Tortuga Restaurante,Avda. Azteca 123,México D.F.,,05033,México
10277,MORGK,2,9/8/1996 00:00:00,6/9/1996 00:00:00,13/8/1996 00:00:00,3,126,Morgenstern Gesundkost,Heerstr. 22,Leipzig,,04179,Alemania
10278,BERGS,8,12/8/1996 00:00:00,9/9/1996 00:00:00,16/8/1996 00:00:00,2,93,Berglunds snabbköp,Berguvsvägen  8,Luleå,,S-958 22,Suecia
10279,LEHMS,8,13/8/1996 00:00:00,10/9/1996 00:00:00,16/8/1996 00:00:00,2,26,Lehmanns Marktstand,Magazinweg 7,Frankfurt a.M. ,,60528,Alemania
10280,BERGS,2,14/8/1996 00:00:00,11/9/1996 00:00:00,12/9/1996 00:00:00,1,9,Berglunds snabbköp,Berguvsvägen  8,Luleå,,S-958 22,Suecia
10281,ROMEY,4,14/8/1996 00:00:00,28/8/1996 00:00:00,21/8/1996 00:00:00,1,3,Romero y tomillo,"Gran Vía, 1",Madrid,,28001,España
10282,ROMEY,4,15/8/1996 00:00:00,12/9/1996 00:00:00,21/8/1996 00:00:00,1,13,Romero y tomillo,"Gran Vía, 1",Madrid,,28001,España
10283,LILAS,3,16/8/1996 00:00:00,13/9/1996 00:00:00,23/8/1996 00:00:00,3,85,LILA-Supermercado,Carrera 52 con Ave. Bolívar #65-98 Llano Largo,Barquisimeto,Lara,3508,Venezuela
10284,LEHMS,4,19/8/1996 00:00:00,16/9/1996 00:00:00,27/8/1996 00:00:00,1,77,Lehmanns Marktstand,Magazinweg 7,Frankfurt a.M. ,,60528,Alemania
10285,QUICK,1,20/8/1996 00:00:00,17/9/1996 00:00:00,26/8/1996 00:00:00,2,77,QUICK-Stop,Taucherstraße 10,Cunewalde,,01307,Alemania
10286,QUICK,8,21/8/1996 00:00:00,18/9/1996 00:00:00,30/8/1996 00:00:00,3,229,QUICK-Stop,Taucherstraße 10,Cunewalde,,01307,Alemania
10287,RICAR,8,22/8/1996 00:00:00,19/9/1996 00:00:00,28/8/1996 00:00:00,3,13,Ricardo Adocicados,"Av. Copacabana, 267",Río de Janeiro,RJ,02389-890,Brasil

Resumen numérico:
           IdPedido  IdEmpleado  FormaEnvío        Cargo
count    830.000000  830.000000  830.000000   830.000000
mean   10662.500000    4.403614    2.008434    78.239759
std      239.744656    2.499648    0.778899   116.786007
min    10248.000000    1.000000    1.000000     0.000000
25%    10455.250000    2.000000    1.000000    13.000000
50%    10662.500000    4.000000    2.000000    41.000000
75%    10869.750000    7.000000    3.000000    91.000000
max    11077.000000    9.000000    3.000000  1008.000000
