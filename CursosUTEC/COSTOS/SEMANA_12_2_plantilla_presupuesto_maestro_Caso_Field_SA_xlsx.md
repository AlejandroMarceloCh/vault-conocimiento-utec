---
curso: COSTOS
titulo: SEMANA_ 12.2 plantilla presupuesto maestro - Caso Field SA
slides: 0
fuente: SEMANA_ 12.2 plantilla presupuesto maestro - Caso Field SA.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: SEMANA_ 12.2 plantilla presupuesto maestro - Caso Field SA.xlsx. -->

<!-- INTERPRETAR: datos tabulares de SEMANA_ 12.2 plantilla presupuesto maestro - Caso Field SA.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Datos
Filas: 61 · Columnas: 7
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object)

Muestra (primeras 40 de 61 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
BALANCE GENERAL,,,,,,
Al 30/09/2010,,,,,,
ACTIVO,,,,PASIVO,,
Caja y Bancos,,12000,,Cuentas por pagar,,90000
Cuentas por cobrar,,136500,,Otras cuentas por pagar,,16500
Productos terminados,,60800,,Pasivo corriente,,106500
Materia Prima,,10000,,Deuda de largo plazo,,230000
Activo corriente,,219300,,Total pasivo,,336500
Activo fijo ,,300000,,PATRIMONIO NETO,,
-Depreciación,,45000,,Capital,,100000
,,,,Resultado acumulado,,37800
Total Activo,,474300,,Total pasivo y pat. Neto,,474300
,,,,,,
,,,,,,
A),,,,,,
,Mes,unidades,,,,
,Octubre,15000,,,,
,Noviembre,21000,,,,
,Diciembre,16000,,,,
,Enero,17000,,,,
,Febrero,18000,,,,
,Marzo,15000,,,,
,,,,,,
C),,,,,,
,Referencia,Inv. Inicial (actual),,Inv. Final (Proyectado),,
,X-10,4000,,30% del volumen de ventas,,
,Mat. A,30000,onzas,,,
,Mat. B,15000,onzas,,,
,,,,,,
D),,,,,,
,Referencia,Cantidad,,Precio,,
,Material A,25,onzas,0.3,onza,
,Material B,15,onzas,0.45,onza,
,Mano de obra,Cada 4 horas se elaboran 20 productos ,,,,
,,Costo por hora S/. 5.50,,,0.2,Hr x prod
,,,,,,
F),Costos,,S/. ,,,
,Sueldos y salarios,,225000,,,
,Depreciación,,15000,,,
,Mantenimiento,,97200,,,

## Hoja: solucion
Filas: 160 · Columnas: 9
Columnas y tipos: 1) (object), Presupuesto de ventas (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (float64)

Muestra (primeras 40 de 160 filas, formato CSV):
1),Presupuesto de ventas,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8
,MES,,,,,,,
,Octubre,,,,,,,
,Noviembre,,,,,,,
,Diciembre,,,,,,,
,Enero,,,,,,,
,Febrero,,,,,,,
,Marzo,,,,,,,
,,,,,,,,
2),Cronograma de cobranza,,,,,,,
,MES,,,,,,,
,,,,,,,,
,Octubre,,,,,,,
,Noviembre,,,,,,,
,Diciembre,,,,,,,
,Enero,,,,,,,
,Febrero,,,,,,,
,Marzo,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
,,,,,,,,
3),Presupuesto de producción,,,,,,,
,REFERENCIA,,,,,,,
,Pto. Ventas,,,,,,,
,+ Inv. Final (30%),,,,,,,
,Stock total,,,,,,,
,- Inv. Inicial,,,,,,,
,PRODUCCIÓN,,,,,,,
,,,,,,,,
4),Presupuesto de consumo de materiales,,,,,,,
,MATERIAL:,A,,,,,,
,MES,,,,,,,
,,,,,,,,
,Octubre,,,,,,,
,Noviembre,,,,,,,
,Diciembre,,,,,,,
,Enero,,,,,,,
,Febrero,,,,,,,
,Marzo,,,,,,,
,,,,,,,,

Resumen numérico:
       Unnamed: 8
count    5.000000
mean     1.000000
std      2.236068
min      0.000000
25%      0.000000
50%      0.000000
75%      0.000000
max      5.000000

## Hoja: Hoja3
Filas: 19 · Columnas: 2
Columnas y tipos: Encontrar TEM DEUDA A LARGO PLAZO (object), Unnamed: 1 (float64)

Muestra (primeras 19 de 19 filas, formato CSV):
Encontrar TEM DEUDA A LARGO PLAZO,Unnamed: 1
TEA,0.25
Dias que tengo,360.0
dias que quiero,30.0
TEM,0.018769265121506118
,
PAGO CUOTA MENSUAL,
TASA,0.018769265121506118
Nper,12.0
VA,230000.0
VF,0.0
Tipo,0.0
PAGO,21584.65488973193
,
,
Encontrar TEM,
TEA,0.15
Dias que tengo,360.0
dias que quiero,30.0
TEM,0.01171491691985338

Resumen numérico:
          Unnamed: 1
count      14.000000
mean    18026.936010
std     61279.041821
min         0.000000
25%         0.018769
50%         6.125000
75%       277.500000
max    230000.000000
