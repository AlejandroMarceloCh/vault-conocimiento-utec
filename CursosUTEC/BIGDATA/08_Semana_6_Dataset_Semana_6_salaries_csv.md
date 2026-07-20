---
curso: BIGDATA
titulo: 08 - Semana 6/Dataset_Semana_6__salaries
slides: 0
fuente: 08 - Semana 6/Dataset_Semana_6__salaries.csv
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 08 - Semana 6/Dataset_Semana_6__salaries.csv. -->

<!-- INTERPRETAR: datos tabulares de Dataset_Semana_6__salaries.csv. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: csv
Filas: 37234 · Columnas: 11
Columnas y tipos: work_year (int64), experience_level (object), employment_type (object), job_title (object), salary (int64), salary_currency (object), salary_in_usd (int64), employee_residence (object), remote_ratio (int64), company_location (object), company_size (object)

Muestra (primeras 40 de 37234 filas, formato CSV):
work_year,experience_level,employment_type,job_title,salary,salary_currency,salary_in_usd,employee_residence,remote_ratio,company_location,company_size
2020,EN,FT,Azure Data Engineer,100000,USD,100000,MU,0,MU,S
2020,EN,CT,Staff Data Analyst,60000,CAD,44753,CA,50,CA,L
2020,SE,FT,Staff Data Scientist,164000,USD,164000,US,50,US,M
2020,EN,FT,Data Analyst,42000,EUR,47899,DE,0,DE,L
2020,EX,FT,Data Scientist,300000,USD,300000,US,100,US,L
2020,MI,CT,Sales Data Analyst,60000,USD,60000,NG,0,NG,M
2020,EX,FT,Staff Data Analyst,15000,USD,15000,NG,0,CA,M
2020,MI,FT,Business Data Analyst,95000,USD,95000,US,0,US,M
2020,EN,FT,Data Analyst,20000,EUR,22809,PT,100,PT,M
2020,EN,FT,Data Scientist,43200,EUR,49268,DE,0,DE,S
2020,SE,FT,Machine Learning Manager,157000,CAD,117104,CA,50,CA,L
2020,EN,FT,Data Engineer,48000,EUR,54742,PK,100,DE,L
2020,MI,FT,Product Data Analyst,20000,USD,20000,HN,0,HN,S
2020,MI,FT,Data Engineer,51999,EUR,59303,DE,100,DE,S
2020,EN,FT,Big Data Engineer,70000,USD,70000,US,100,US,L
2020,SE,FT,Data Scientist,60000,EUR,68428,GR,100,US,L
2020,MI,FT,Research Scientist,450000,USD,450000,US,0,US,M
2020,MI,FT,Data Analyst,41000,EUR,46759,FR,50,FR,L
2020,MI,FT,Data Engineer,65000,EUR,74130,AT,50,AT,L
2020,MI,FT,Data Scientist,103000,USD,103000,US,100,US,L
2020,EN,FT,Machine Learning Engineer,250000,USD,250000,US,50,US,L
2020,EN,FT,Machine Learning Engineer,138000,USD,138000,US,100,US,S
2020,MI,FT,Data Scientist,45760,USD,45760,PH,100,US,S
2020,EX,FT,Data Engineer,70000,EUR,79833,ES,50,ES,L
2020,MI,FT,Machine Learning Infrastructure Engineer,44000,EUR,50180,PT,0,PT,M
2020,MI,FT,Data Engineer,106000,USD,106000,US,100,US,L
2020,MI,FT,Data Engineer,88000,GBP,112872,GB,50,GB,L
2020,EN,PT,Machine Learning Engineer,14000,EUR,15966,DE,100,DE,S
2020,MI,FT,Data Scientist,60000,GBP,76958,GB,100,GB,S
2020,SE,FT,Data Engineer,188000,USD,188000,US,100,US,L
2020,MI,FT,Data Scientist,105000,USD,105000,US,100,US,L
2020,MI,FT,Data Engineer,61500,EUR,70139,FR,50,FR,L
2020,SE,FT,Data Engineer,720000,MXN,33511,MX,0,MX,S
2020,EN,FT,Data Analyst,91000,USD,91000,US,100,US,L
2020,EN,FT,Research Scientist,42000,USD,42000,NL,50,NL,L
2020,MI,FT,Lead Data Scientist,115000,USD,115000,AE,0,AE,L
2020,SE,FT,Machine Learning Scientist,260000,USD,260000,JP,0,JP,S
2020,SE,FT,Big Data Engineer,85000,GBP,109024,GB,50,GB,M
2020,MI,FT,Data Scientist,70000,EUR,79833,DE,0,DE,L
2020,SE,FT,Machine Learning Engineer,150000,USD,150000,US,50,US,L

Resumen numérico:
          work_year        salary  salary_in_usd  remote_ratio
count  37234.000000  3.723400e+04   37234.000000  37234.000000
mean    2023.656443  1.667366e+05  160540.603105     23.197884
std        0.611469  2.338090e+05   72679.876280     42.005217
min     2020.000000  1.400000e+04   15000.000000      0.000000
25%     2023.000000  1.100000e+05  110000.000000      0.000000
50%     2024.000000  1.500000e+05  150000.000000      0.000000
75%     2024.000000  2.000000e+05  200000.000000      0.000000
max     2024.000000  3.040000e+07  800000.000000    100.000000
