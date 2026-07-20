---
curso: MKT
titulo: Solucionario
slides: 0
fuente: Solucionario.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Solucionario.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Solucionario.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Bazaar solution
Filas: 33 · Columnas: 18
Columnas y tipos: Table 1: Weekly traffic from Google by origin of click (for branded keywords searches only)  (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (float64), Unnamed: 9 (float64), Unnamed: 10 (float64), Unnamed: 11 (float64), Unnamed: 12 (float64), Unnamed: 13 (float64), Unnamed: 14 (float64), Unnamed: 15 (float64), Cost per click  (object), 0.6 (float64)

Muestra (primeras 33 de 33 filas, formato CSV):
Table 1: Weekly traffic from Google by origin of click (for branded keywords searches only) ,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Cost per click ,0.6
Week,1,2,3,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,,,,Conversion rate after arriving on website ,0.12
Sponsored,32269,31951,32143,31417.0,31194.0,31576.0,30951.0,30611.0,30401.0,0.0,0.0,0.0,,,,Average margin per conversion ,21.0
Organic ,127876,128169,125717,126264.0,123871.0,124053.0,126105.0,123064.0,121637.0,150188.0,148658.0,146584.0,,,,Margin from a customer arrival on the website,2.52
Total,160145,160120,157860,157681.0,155065.0,155629.0,157056.0,153675.0,152038.0,150188.0,148658.0,146584.0,,,,,
,125195.11111111111,,,,,,,,,,,,,,,,
Table 2: Weekly traffic from Bing by origin of click (for branded keywords searches only) ,,,,,,,,,,,,,,,,BOB'S CALCULATION (INCORRECT) ,
Week,1,2,3,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,,,,Weekly average traffic through ads,31390.333333333332
Sponsored,3965,3984,3960,3952.0,3874.0,3932.0,3890.0,3883.0,3843.0,3815.0,3754.0,3754.0,,,,% of traffic through ads,0.2004677602359805
Organic ,15805,15964,15815,15810.0,15633.0,15797.0,15462.0,15309.0,15499.0,15185.0,15159.0,15036.0,,,,,
Total,19770,19948,19775,19762.0,19507.0,19729.0,19352.0,19192.0,19342.0,19000.0,18913.0,18790.0,,,,Spend on an ad,0.6
,,,,,,,,,,,,,,,,"""Revenue"" from an ad ",2.52
Table 3: Average weekly total traffic from Google,,,,,,,,,,,,,,,,ROI of ad spend ,3.2
Weeks 1-9,Weeks 10-12,,,,,,,,,,,,,,,,
156585.44444444444,148476.66666666666,-0.05178500343085673,8108.777777777781,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,DIFF CALCULATION (INCORRECT) ,
Table 4: Average weekly total traffic from Bing,,,,,,,,,,,,,,,,% of traffic attributed to ads,0.05178500343085673
Weeks 1-9,Weeks 10-12,,,,,,,,,,,,,,,Weekly average traffic attributable to ads,8108.777777777781
19597.444444444445,18901,-0.03553751339460364,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,Spend on ads ,18834.199999999997
,,,,,,,,,,,,,,,,"""Revenue"" from additional traffic due to ads ",20434.12000000001
Table 5: Actual and Projected Weekly Average Total Traffic in Weeks 1-9 and 10-12,,,,,,,,,,,,,,,,ROI of ad spend ,0.08494759533189693
,Weeks 1-9,Weeks 10-12,Reduction in traffic (Diff 1),,,,,,,,,,,,,,
Google,156585.44444444444,148476.66666666666,-0.05178500343085673,,,,,,,,,,,,,,
Bing,19597.444444444445,18901,-0.03553751339460364,,,,,,,,,,,,,DIFF-IN-DIFF CALCULATION ,
,,Normalized reduction in traffic (Diff 2),-0.016247490036253087,,,,,,,,,,,,,% of traffic attributable to ads,0.016247490036253087
,,,,,,,,,,,,,,,,Weekly average traffic attributable to ads,2544.1204484333725
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,Effective number that switched from sponsored to organic,28846.21288489996
,,,,,,,,,,,,,,,,% that switched from sponsored to organic,0.9189521047318164
,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,Spend on ads ,18834.199999999997
,,,,,,,,,,,,,,,,"""Revenue"" from additional traffic due to ads ",6411.183530052099
,,,,,,,,,,,,,,,,ROI of ad spend ,-0.6595988398736289

Resumen numérico:
          Unnamed: 4     Unnamed: 5   Unnamed: 6     Unnamed: 7     Unnamed: 8     Unnamed: 9    Unnamed: 10    Unnamed: 11    Unnamed: 12  Unnamed: 13  Unnamed: 14  Unnamed: 15           0.6
count       8.000000       8.000000       8.0000       8.000000       8.000000       8.000000       8.000000       8.000000       8.000000          0.0          0.0          0.0     20.000000
mean    44361.750000   43644.250000   43841.0000   44103.750000   43218.750000   42847.250000   42299.500000   41895.500000   41346.500000          NaN          NaN          NaN   6771.686039
std     61766.051149   60667.244282   60809.4792   61637.884913   60205.220931   59494.705802   66980.837063   66287.391792   65346.015087          NaN          NaN          NaN  10614.484626
min         4.000000       5.000000       6.0000       7.000000       8.000000       9.000000       0.000000       0.000000       0.000000          NaN          NaN          NaN     -0.659599
25%      2965.000000    2906.750000    2950.5000    2919.250000    2914.250000    2884.500000      10.000000      11.000000      12.000000          NaN          NaN          NaN      0.180351
50%     17786.000000   17570.000000   17763.0000   17407.000000   17250.500000   17420.500000    9500.000000    9456.500000    9395.000000          NaN          NaN          NaN      2.860000
75%     55128.750000   54363.250000   54695.2500   54739.500000   53724.250000   53210.000000   51797.000000   51349.250000   50738.500000          NaN          NaN          NaN  10790.133333
max    157681.000000  155065.000000  155629.0000  157056.000000  153675.000000  152038.000000  150188.000000  148658.000000  146584.000000          NaN          NaN          NaN  31390.333333
