---
curso: ML
titulo: Grupos_ML_2026_I_Final
slides: 0
fuente: Grupos_ML_2026_I_Final.xlsx
---

## Grupos y evaluaciones — Machine Learning 2026-I

Este archivo no es un dataset de entrenamiento sino la hoja administrativa del curso, con dos pestañas. La primera, "Grupos ML 2026-I", tiene 70 filas y 4 columnas y lista la conformación de equipos: el criterio declarado es "12 grupos de 4 integrantes (3 amarillo + 1 naranja) y 2 grupos de 3 integrantes (solo amarillo)". Cada bloque de grupo trae Grupo, N°, Nombre del Estudiante y Carrera, con estudiantes de Ciencia de la Computación, Ciencia de Datos, Bioingeniería, Mecatrónica, Mecánica, Electrónica, Energía, Sistemas de Información y Civil. La segunda pestaña, "Fechas exámenes", fija los pesos y fechas: Examen parcial (EP) 10% en semana 8 (13 mayo), Proyecto 1 (P1) 10% en semana 7 (6 mayo) y Evaluación Continua 1 (EC1) 10% (11 mayo).

Desde ML, el valor pedagógico no está en el contenido sino en la estructura: es un caso real de tabla "sucia" con encabezados de título, celdas fusionadas, columnas Unnamed y filas vacías separadoras. Enseña justamente el trabajo previo a cualquier modelo — parsing de multi-índices, forward-fill del identificador de grupo, drop de filas nulas y reconstrucción del esquema tabular limpio con pandas. Conecta con la fase de preparación de datos que antecede a EDA, feature engineering y evaluación (los mismos pesos y cortes de EP/P1/EC1 que ordenan el curso).

```
Grupos de Trabajo — Machine Learning 2026-I,Unnamed: 1,Unnamed: 2,Unnamed: 3
12 grupos de 4 integrantes (3 amarillo + 1 naranja)  |  2 grupos de 3 integrantes (solo amarillo),,,
,,,
Grupo,N°,Nombre del Estudiante,Carrera
Grupo 1,1,"Perez Villanueva,Jossue Everardo",Bioingeniería
,2,"Rivadeneira Fernandez,Luis Fabiano Ivor",Ciencia de la Computación
...

Fechas Exámenes — Machine Learning 2026-I,Unnamed: 1,Unnamed: 2,Unnamed: 3
Teoría,%,Semana 8,Fecha
Examen parcial (EP),10,11 mayo - 15 mayo,2026-05-13 00:00:00
Práctica y Laboratorio,%,Semana 7,Fecha
Proyecto 1 (P1),10,4 mayo - 8 mayo,2026-05-06 00:00:00
Evaluación Continua 1 (EC1),10,11 mayo - 15 mayo,2026-05-11 00:00:00
```
