---
curso: COSTOS
titulo: SEMANA_12.3_presupuesto maestro - Caso Field SA
slides: 0
fuente: SEMANA_12.3_presupuesto maestro - Caso Field SA.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: SEMANA_12.3_presupuesto maestro - Caso Field SA.xlsx. -->

<!-- INTERPRETAR: datos tabulares de SEMANA_12.3_presupuesto maestro - Caso Field SA.xlsx. El capítulo debe ser una
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

## Hoja: Hoja2
Filas: 160 · Columnas: 11
Columnas y tipos: 1) (object), Presupuesto de ventas (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object)

Muestra (primeras 40 de 160 filas, formato CSV):
1),Presupuesto de ventas,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,MES,CANTIDAD,"VALOR
S/.",IMPORTE,,,,,,
,Octubre,15000,25,375000,,,,,,
,Noviembre,21000,25,525000,,,,,,
,Diciembre,16000,25,400000,,,,,,
,Enero,17000,25.5,433500,,,,,,
,Febrero,18000,25.5,459000,,,,,,
,Marzo,15000,25.5,382500,,,,,,
,,,,,,,,,,
2),Cronograma de cobranza,,,,,,,,,
,MES,PTO. VENTAS,CONTADO,"LETRA 
30 DIAS","LETRA 
60 DIAS",TOTAL,,,,
,,,0.4,0.5,0.1,,,,,
,Octubre,375000,150000,75000,46500,271500,,,,
,Noviembre,525000,210000,187500,15000,412500,,,,
,Diciembre,400000,160000,262500,37500,460000,,,,
,Enero,433500,173400,200000,52500,425900,,,,
,Febrero,459000,183600,216750,40000,440350,,,,
,Marzo,382500,153000,229500,43350,425850,,,,
,,,,191250,45900,237150,,,,
,,,,,38250,38250,,,,
,,,1030000,1362500,319000,,,,,
,,,,,,,,,,
3),Presupuesto de producción,,,,,,,,,
,REFERENCIA,OCTUBRE,NOVIEMBRE,DICIEMBRE,ENERO,FEBRERO,MARZO,,,
,Pto. Ventas,15000,21000,16000,17000,18000,15000,,,
,+ Inv. Final (30%),4500,6300,4800,5100,5400,4500,,,
,Stock total,19500,27300,20800,22100,23400,19500,,,
,- Inv. Inicial,-4000,-4500,-6300,-4800,-5100,-5400,,,
,PRODUCCIÓN,15500,22800,14500,17300,18300,14100,,,
,,,,,,,,,,
4),Presupuesto de consumo de materiales,,,,,,,,,
,MATERIAL:,A,,,,,,,,
,MES,PTO. PRODUCCIÓN,"CANT.
ONZAS",TOTAL ONZAS,VALORIZACIÓN,,,,,
,,,,,0.3,,,,,
,Octubre,15500,25,387500,116250,,,,,
,Noviembre,22800,25,570000,171000,,,,,
,Diciembre,14500,25,362500,108750,,,,,
,Enero,17300,25,432500,129750,,,,,
,Febrero,18300,25,457500,137250,,,,,
,Marzo,14100,25,352500,105750,,,,,
,,,,,,,,,,

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
PAGO,21584.654889731944
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
