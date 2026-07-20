---
curso: CONTAGER
titulo: Plantilla flujo de caja UTEC 05 junio 2023
slides: 0
fuente: Plantilla flujo de caja UTEC 05 junio 2023.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Plantilla flujo de caja UTEC 05 junio 2023.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Plantilla flujo de caja UTEC 05 junio 2023.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: IGV
Filas: 42 · Columnas: 10
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (datetime64[ns]), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object)

Muestra (primeras 40 de 42 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9
,,2023-01-01,REGISTRO DE COMPRAS,,0.18,PRECIO,,2023-01-01 00:00:00,
,,,,VALOR DE VENTA,IGV,IMPORTE TOTAL,,40.TRIBUTOS POR PAGAR,
,,2023-01-06,Fact.E-001-7622 ,1500,270,1770,,DEBE,HABER
,,2023-01-25,Fact E/E001-7376,4000,720,4720,,1200.6,27000
,(Estimado),2023-01-28,SERV.AGUA+LUZ+TELEFONIA,1170,210.6,1380.6,,,25799.4
,,,,,1200.6,,,,Tributo por pagar a Sunat
,,,,,,,,,al mes siguiente
,,2023-01-01,REGISTRO DE VENTAS,,,,,,
,,,,VALOR DE VENTA,IGV,IMPORTE TOTAL,,,
,,,Todo el mes,150000,27000,177000,,,
,,,,,27000,,,,
,,,,,,,,,
,,2023-02-01,REGISTRO DE COMPRAS,,,,,2023-02-01 00:00:00,
,,,,VALOR DE VENTA,IGV,IMPORTE TOTAL,,40.TRIBUTOS POR PAGAR,
,(Estimado),2023-02-28,SERV.AGUA+LUZ+TELEFONIA,1170,210.6,1380.6,,DEBE,HABER
,,2023-02-16,E-001-7627 ,2000,360,2360,,570.6,32535
,,,,,570.6,,,,31964.4
,,,,,,,,,Igv por pagar
,,2023-02-01,REGISTRO DE VENTAS,,,,,,
,,,,VALOR DE VENTA,IGV,IMPORTE TOTAL,,,
,,2023-02-05,Nota de debito F/ ND 001-9876 ,750,135,885,,,
,,,Venta según F/,180000,32400,212400,,,
,,,,,32535,,,,
,,,,,,,,,
,,2023-03-01,REGISTRO DE COMPRAS,,,,,2023-03-01 00:00:00,
,,,,VALOR DE VENTA,IGV,IMPORTE TOTAL,,40.TRIBUTOS POR PAGAR,
,(Estimado),2023-02-28,SERV.AGUA+LUZ+TELEFONIA,1170,210.6,1380.6,,DEBE,HABER
,,,Compra de serv.publicitarios,10000,1800,11800,,2010.6,34200
,,,,,2010.6,,,,32189.4
,,,,,,,,,
,,2023-03-01,REGISTRO DE VENTAS,,,,,,
,,,,VALOR DE VENTA,IGV,IMPORTE TOTAL,,,
,,,Ventas según Factura,190000,34200,224200,,,
,,,,,34200,,,,
,,,,,,,,,
,,2023-04-01,REGISTRO DE COMPRAS,,,,,2023-04-01 00:00:00,
,,,,VALOR DE VENTA,IGV,IMPORTE TOTAL,,40.TRIBUTOS POR PAGAR,
,(Estimado),2023-02-28,SERV.AGUA+LUZ+TELEFONIA,1170,210.6,1380.6,,DEBE,HABER
,,,,,,,,,
,,,,,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 7
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: FLUJO DE CAJA
Filas: 26 · Columnas: 7
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object)

Muestra (primeras 26 de 26 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
,,,2023-01-01 00:00:00,2023-02-01 00:00:00,2023-03-01 00:00:00,2023-04-01 00:00:00
,,SALDO INICIAL,5500,74543,211176,317189
,,INGRESOS S/.,,,,
,,COBRANZA F/E001-9811,25000,,,
,,POR COBRANZA ANTIGUA ,,17700,,
,,POR COBRANZA DE INTERES X MORA,,,885,
,,COBRANZA POR VENTAS (ENERO),53100,79650,44250,
,,COBRANZA POR VENTAS(FEB),,74340,95580,42480
,,COBRANZAS POR VENTAS(mar),,,22420,89680
,,TOTAL INGRESOS S/,78100,171690,163135,132160
,,EGRESOS:,,,,
,,ALQUILER MENSUAL,1950,1950,1950,1950
,,PLANILLA,5000,5000,9250,13500
,,PAGO DE RECIBOS,1062,1062,1062,1367.6000000000001
,,PAGO DE IMP . A LA RENTA(de dic 2022),1000,1200,1050,1100
,,PAGO A PROVEEDORES,,,4720,
,,PAGO E-001-7627 ,,,2360,
,,PAGO POR MARKETING ,,,4720,
,,PAGO POR COMISIONES AL BCP,45,45,45,45
,,pago de igv (enero),,25800,31965,32190
,,TOTAL EGRESOS S/,9057,35057,57122,50152.6
,,FLUJO DEL MES S/,69043,136633,106013,82007.4
,,SALDO FINAL S/,74543,211176,317189,399196.4
,,,,,,
,,Borrador:,,,,
,,PAGO DE SERVICIOS,1367.6000000000001,1367.6000000000001,1367.6000000000001,1367.6000000000001

Resumen numérico:
       Unnamed: 0  Unnamed: 1
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN
