---
curso: FUNDOPS
titulo: solucion textil amazonas
slides: 13
fuente: solucion textil amazonas.pdf
---

## Slide 1

Tabla de datos base del caso "Tamaño de Planta" con 3 columnas de escenario (Pequeña, Mediana, Grande):

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Tasa de Producción en horario normal (kg/hora) | 60 | 80 | 90 |
| Tasa de Producción en horas extra (kg/hora) | 50 | 60 | 65 |
| Número de Operarios | 7 | 8 | 8 |
| Consumo de kg material / kg producto | 0.80 | 0.78 | 0.77 |
| Consumo de L agua / kg producto | 7.5 | 5.5 | 4.8 |
| Capacidad de almacenaje | 10,000 | 15,000 | 20,000 |
| Consumo kW | 80 | 110 | 140 |
| Costo fijo ($) | 150,000 | 250,000 | 350,000 |
| Inversión ($) | 800,000 | 1,200,000 | 1,500,000 |

Filas en fondo rosa/salmón claro (formato Excel), encabezado en amarillo claro ("Tamaño de Planta" como título de grupo de columnas).

## Slide 2

Continuación de la tabla de parámetros generales (celdas alternando rosa claro/blanco, tipo hoja de cálculo pegada):

| Parámetro | Valor |
|---|---|
| Costo de M.O. por Hora Normal ($/horaxoperario) | 40 |
| Porcentaje Adicional Horas Extras (%) | 60% |
| Nro. Días x Semana | 5 |
| Nro. Semanas x Año | 52 |
| Nro. de Días x Año (resaltado amarillo) | 260 |
| Costo de Electricidad (US$/kWh) | 0.15 |
| Costo de Agua (US$/l) | 0.03 |
| Costo de Almacenaje (US$/kg) | 3 |
| Costo de Almacenaje Adicional (US$/kg) | 6 |
| Factor de Almacenaje (%) | 15% |
| Costo de Materiales (US$/kg) | 2.93 |
| Precio (US$/kg) (resaltado amarillo) | 14 |
| Demanda Anual (kg/año) | 80,000 |
| Precio de Venta (US$/kg) | 14 |
| Tasa de Descuento Anual (%) | 9% |
| Horizonte de Evaluación Financiera (años) | 5 |
| Tasa de Descuento Mensual (%) (resaltado amarillo) | 0.721% |

## Slide 3

Tabla pequeña con el esquema de horas y costo por hora:

| | Número de Horas por Día (horas/día) | Costo por Hora (US$/hora) |
|---|---|---|
| Horas Mínimas | 5 | 40 |
| Horas Normales | 8 | 40 |
| Horas Extras | 2 | 64 |

## Slide 4

Enunciado punto 1: "Calcule la capacidad mínima, regular (máxima en horas regulares) y máxima (incluyendo horas extras) anuales." Con bullets: Regular = Normal; Máxima = normal + extras.

Fórmula recuadrada en azul:
```
Capacidad de producción (kg/año) = Tasa producción (kg/hr) x Horas trabajadas (hr/día) x (días/semana) x (semanas/año)
```

Tabla de resultados (etiqueta "Máxima" a la izquierda de la última fila):

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Capacidad de Producción Mínima (kg/año) | 78,000 (en rojo) | 104,000 | 117,000 |
| Capacidad de Producción Normal (kg/año) | 124,800 | 166,400 | 187,200 |
| Capacidad de Producción en Horas Extras (kg/año) | 26,000 | 31,200 | 33,800 |
| Capacidad de Producción Horas Normales + Extras (kg/año) | 150,800 | 197,600 | 221,000 |

Debajo, se repiten (miniaturizadas) las dos tablas de datos base de las slides 1 y 3 (tasas de producción y horas/costo por hora) como referencia visual.

## Slide 5

Enunciado punto 2: "Verifique la factibilidad de lograr cubrir la demanda y las horas trabajadas (separadas por horas regulares y horas extra)." Demanda Anual (kg/año) = 80,000.

Repite la tabla de capacidades de la slide 4 (con sombra de recuadro).

Tabla de factibilidad (encabezados resaltados en amarillo):

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Capacidad de Producción Mínima (kg/año) | Infactible (rojo) | Factible | Factible |
| Capacidad de Producción Normal (kg/año) | Factible | ---- | ---- |
| Capacidad de Producción Horas Normales + Extras (kg/año) | ---- | ---- | ---- |

Recuadro azul con nota: "Si la capacidad satisface la demanda anual, ya no es necesario indicar la factibilidad con mayor capacidad."

## Slide 6

Enunciado punto 3: "Calcule la cantidad de horas regulares y de horas extras necesarias según la demanda."

Fórmula resaltada en amarillo:
$$\text{Cantidad de horas (hr/día)} = \frac{\text{demanda anual}\ (\text{kg/año})}{\text{tasa de producción}\ (\text{kg/hr})}$$
Anotación: "Convertirlo a hr/día".

Tabla:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Cantidad de Horas Necesarias a Capacidad Mínima (horas/día) | no factible (rojo) | 3.85 | 3.42 |
| Cantidad de Horas Regulares a Capacidad Normal (horas/día) | 5.13 | - | - |
| Cantidad de Horas extras (horas/día) | - | - | - |
| Cantidad de Horas Normales + Extras Necesarias (horas/día) | 5.13 | - | - |

Recuadro azul: "La cantidad de horas regulares 5.13, cumple o está dentro de las 8 horas, ya no es necesario calcular cantidad de horas extras".

Debajo, tabla en miniatura repite tasas de producción normal/extra (referencia).

## Slide 7

Repite exactamente el contenido de la Slide 6 (mismo enunciado punto 3, misma fórmula, misma tabla y misma nota azul), y añade además una segunda fórmula y tabla anuales:

Fórmula:
$$\text{Cantidad de horas (hr/año)} = \frac{\text{demanda anual}\ (\text{kg/año})}{\text{tasa de producción}\ (\text{kg/hr})}$$

Tabla adicional:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Cantidad de Horas Regulares a Capacidad Mínima (horas/año) | - | 1,000.00 | 888.89 |
| Cantidad de Horas Regulares a Capacidad Normal (horas/año) | 1,333.33 | - | - |
| Cantidad de Horas extras (horas/año) | - | - | - |
| Cantidad de Horas Normales + Extras Necesarias (horas/año) | 1,333.33 | 1,000.00 | 888.89 |

## Slide 8

Enunciado punto 4: "Calcule los costos totales de mano de obra." Arriba a la derecha se repite (miniatura) la tabla de horas anuales de la slide 7, con las columnas Mediana y Grande resaltadas con recuadro rojo.

Recuadro azul: "Cantidad de horas/día a pagar, para las horas mínimas según dato se paga como mínimo 5 horas trabajadas".

Tabla:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Cantidad de Horas Regulares a Capacidad Mínima (horas/día) | - | 5 | 5 |
| Cantidad de Horas Regulares a Capacidad Normal (horas/día) | 5.13 | - | - |
| Cantidad de Horas extras (horas/día) | - | - | - |
| Cantidad de Horas Normales + Extras Necesarias (horas/día) | 5.13 | - | - |

Recuadro azul con fórmula: "Costo total de mano de obra ($/año) = cant horas pagar(hr/día) x (días/año) x costos por hora ($/hr) x # operarios".

Tabla de resultados:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Costo Total de M.O. en Horario Mínimo (US$/año) | - | 416,000.00 | 416,000.00 |
| Costo Total de M.O. en Horario Regular (US$/año) | 373,333.33 | - | - |
| Costo Total de M.O. en Horas Extras (US$/año) | - | - | - |
| Costo Total de Mano de Obra (US$/año) | 373,333.33 | 416,000.00 | 416,000.00 |

Debajo, tablas miniatura de referencia: horas/costo por hora, y número de operarios (7, 8, 8).

## Slide 9

Enunciado punto 5: "Calcule los costos totales de materiales, agua, energía y almacenamiento."

Repite tabla de parámetros de consumo (material, agua, almacenaje, kW) y tabla de capacidad máxima (150,800 / 197,600 / 221,000).

Recuadro azul: "requerimiento anual de insumos".

Tabla de cálculos intermedios (fórmulas incluidas como texto en la celda):

| Insumo | Fórmula | Pequeña | Mediana | Grande |
|---|---|---|---|---|
| Cantidad de Material (kg/año) | Demanda anual x factor de consumo de materiales | 64,000.00 | 62,400.00 | 61,600.00 |
| Cantidad de Agua (l/año) | Demanda anual x (L agua/kg producto) | 600,000.00 | 440,000.00 | 384,000.00 |
| Cantidad de Energía (kWh/año) | (total hr/año) x (consumo kw) | 106,666.67 | 110,000.00 | 124,444.44 |
| Cantidad Requerida de Almacenamiento (kg/año) (texto en naranja) | Demanda anual x factor de almacenaje | 10,000.00 | 12,000.00 | 12,000.00 |
| Cantidad Requerida de Almacenamiento Adicional (kg/año) (texto en naranja) | — | 2,000.00 | - | - |

## Slide 10

Repite la tabla de costos unitarios (electricidad, agua, almacenaje, almacenaje adicional, factor de almacenaje, costo de materiales) y la tabla de requerimiento anual de insumos de la slide 9 (en miniatura, arriba).

Tabla de costos totales resultantes:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Costo Total de Materiales (US$/año) | 187,520.00 | 182,832.00 | 180,488.00 |
| Costo Total de Agua (US$/año) | 18,000.00 | 13,200.00 | 11,520.00 |
| Costo Total de Energía (US$/año) | 16,000.00 | 16,500.00 | 18,666.67 |
| Costo de Almacenamiento (US$/año) | 30,000.00 | 36,000.00 | 36,000.00 |
| Costo Almacenamiento Adicional (US$/año) | 12,000.00 | - | - |
| Costo Total de Almacenamiento (US$/año) | 42,000.00 | 36,000.00 | 36,000.00 |

Las 3 últimas filas tienen fondo gris (subtotales).

## Slide 11

Enunciado punto 6: "Halle el costo total." Repite en miniatura (arriba izq.) la tabla de costo de mano de obra (slide 8) y (arriba der.) la tabla de costo de materiales/agua/energía/almacenamiento (slide 10), más la fila "Costo fijo ($)": 150,000 / 250,000 / 350,000.

Tabla de resultado del costo total anual:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Costo Total Anual (US$/año) | 786,853.33 | 914,532.00 | 1,012,674.67 |

Enunciado punto 7: "Calcule el costo unitario." Recuadro azul: "Costos unitarios = costo total / demanda anual".

Tabla resultado:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Costo Unitario (US$/Kg) | 9.84 | 11.43 | 12.66 |

(Nota: el enunciado salta del punto 7 al punto 9 — no hay punto 8 visible en el material.)

## Slide 12

Enunciado punto 9: "Halle el balance mensual. Balance mensual (utilidad mensual) = (Ingresos-Costos)/12". Nota en negrita: "Ingreso = demanda x precio = 80,000 * 14 = 1.120,000".

Repite tabla de Costo Total Anual (slide 11).

Tabla de resultado:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Balance Mensual (US$/mes) | 27,762.22 | 17,122.33 | 8,943.78 |

Recuadro azul con nota de transición: "Supuestamente la que da mayor utilidad mensual debería ser la mejor alternativa, pero falta hallar VPN,".

## Slide 13

Enunciado punto 10: "Halle el Valor Presente NETO."

Recuadro azul con definición de variables: "Hallamos el valor presente (VP): R = balance o utilidad mensual; i = tasa de descuento mensual; n = horizonte de evaluación meses".

Fórmula del Valor Presente de una anualidad:
$$VP = R\,\frac{1-(1+i)^{-n}}{i}$$

Fórmula de la tasa de descuento mensual (recuadro azul):
$$i = (1+\text{tasa descuento anual})^{1/12} - 1$$

Tabla:

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Valor Presente (US$) | 1,348,445.49 | 831,652.92 | 434,410.36 |

Recuadro: "VPN = VP - INVERSION".

Tabla final (columna Pequeña resaltada en amarillo como respuesta destacada):

| Parámetros | Pequeña | Mediana | Grande |
|---|---|---|---|
| Valor Presente Neto (US$) | 548,445.49 | -368,347.08 | -1,065,589.64 |
