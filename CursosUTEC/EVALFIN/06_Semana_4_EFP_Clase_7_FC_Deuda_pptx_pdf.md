---
curso: EVALFIN
titulo: 06 - Semana 4/EFP - Clase 7 - FC Deuda__pptx
slides: 24
fuente: 06 - Semana 4/EFP - Clase 7 - FC Deuda__pptx.pdf
---

## Slide 1

Portada. Título: "Flujo de Caja de la Deuda (Flujo de Caja del Financiamiento)". Subtítulo: "Evaluación Financiera de Proyectos - Semana 7". Fondo decorativo: túnel digital azul con silueta de robot caminando, logos UTEC y TransformaTec (decorativo).

## Slide 2

Título lateral: "Objetivo(s) de la sesión". Imagen decorativa: dos personas revisando documentos (foto con overlay azul, decorativa).

Objetivos (bullets):
- Analizar el flujo de caja del financiamiento (deuda).
- Evaluar el impacto de intereses y escudo fiscal en el flujo del accionista.

## Slide 3

Título: "Contenido". Imagen decorativa de fondo: persona con visor VR y globo digital.

Lista numerada:
1. Métodos de amortización de deuda (repaso).
2. Cálculo del escudo fiscal.
3. Flujo de caja de la deuda (financiamiento).
4. Caso de aplicación.

## Slide 4

Slide separador de sección "1." con ícono de portapapeles. Texto: "Métodos de amortización de deuda". Fondo decorativo: mano robótica tocando globo digital.

## Slide 5

Título: "Métodos de amortización de deuda". Dos columnas de texto:

Columna izquierda: Los métodos más usados para el cálculo del pago de la deuda son:
1. Método de cuota fija (Sistema Francés).
2. Método de amortización constante (Sistema Alemán).

Columna derecha: En cualquier método, la cuota a pagar tiene 2 componentes que se muestran en el flujo de caja del financiamiento (deuda):
- Amortización del principal (pago de una parte de la deuda).
- Intereses (pago del costo de la deuda).

Recuadro inferior "Ejemplo": Supongamos un préstamo de $5,000 con una TEM del 1% y un plazo de 6 meses. Calcule los pagos mensuales.

## Slide 6

Título: "Método de cuota fija (Sistema Francés)".

Columna izquierda: Cuota mensual es constante, pero la proporción de interés y amortización cambia con el tiempo (intereses disminuyen y amortización aumenta). La fórmula de la cuota fija es (recuadro con borde celeste):

$$VA = R * \dfrac{1-(1+i)^{-n}}{i}$$

Donde:
- VA = 5,000 (monto del préstamo)
- n = 6 (número de meses)
- r = 1% (tasa de i mensual)
- R = cuota mensual

Columna derecha: "Calculando:" con fórmula despejada y flecha azul hacia el resultado:

$$R = \dfrac{VA}{\dfrac{1-(1+i)^{-n}}{i}} \;\Rightarrow\; R = \dfrac{5,000}{\dfrac{1-(1+1\%)^{-6}}{1\%}} = 862.74$$

Texto: Cada mes se paga $862.74, con una proporción cambiante de interés y amortización.

Alternativa con Excel: función PAGO de Excel:
```
= PAGO ( 0.01 ; 6 ; 5000)
= -$ 862.74
```
Nota: Excel nos da la respuesta con símbolo monetario y signo negativo (-).

## Slide 7

Título: "Método de cuota fija - cuadro de amortización". Tres cajas de fórmula en la parte superior conectadas con flechas a las columnas de la tabla:
- Interés = Saldo inicial x tasa de i mensual
- Amortización = Cuota fija - Interés
- Saldo Final = Saldo inicial - Amortización
- (nota lateral) Saldo inicial = Saldo Final anterior

Tabla de amortización (Sistema Francés, préstamo $5,000, TEM 1%, 6 meses):

| Mes | Saldo inicial | Interés | Amortización | Cuota | Saldo final |
|---|---|---|---|---|---|
| 1 | 5,000 | 50.00 | 812.74 | 862.74 | 4,187 |
| 2 | 4,187 | 41.87 | 820.87 | 862.74 | 3,366 |
| 3 | 3,366 | 33.66 | 829.08 | 862.74 | 2,537 |
| 4 | 2,537 | 25.37 | 837.37 | 862.74 | 1,700 |
| 5 | 1,700 | 17.00 | 845.74 | 862.74 | 854 |
| 6 | 854 | 8.54 | 854.20 | 862.74 | 0 |
| **Total** | | **176.45** | **5,000.00** | **5,176.45** | |

La celda "4,187" (saldo final mes 1) y "4,187" (saldo inicial mes 2) están resaltadas con recuadro rojo para mostrar el enlace entre filas.

## Slide 8

Título: "Método de amortización constante (Sistema Alemán)".

Columna izquierda: Préstamo se amortiza de manera constante cada período, y el pago total disminuye con el tiempo.

La amortización mensual se calcula como:
$$Amortización = A = \dfrac{P}{n} = \dfrac{5,000}{6} = 833.33$$
A = 833.33

El interés del primer mes es:
$$Interés = B = P * r = 5,000 \times 0.01$$
B = 50.00

Columna derecha: El primer pago total sería:
A + B = 833.33 + 50.00 = 883.3

En los meses siguientes, el interés baja porque el saldo pendiente disminuye, haciendo que la cuota total decrezca progresivamente.

## Slide 9

Título: "Método de amortización constante - cuadro de amortización". Mismas tres cajas de fórmula que slide 7, adaptadas:
- Interés = Saldo inicial x tasa de i mensual
- Cuota total = Amortización + Interés
- Saldo Final = Saldo inicial - Amortización
- (nota lateral) Saldo inicial = Saldo Final anterior

Tabla de amortización (Sistema Alemán, préstamo $5,000, TEM 1%, 6 meses):

| Mes | Saldo inicial | Interés | Amortización | Cuota | Saldo final |
|---|---|---|---|---|---|
| 1 | 5,000 | 50.00 | 833.33 | 883.33 | 4,167 |
| 2 | 4,167 | 41.67 | 833.33 | 875.00 | 3,333 |
| 3 | 3,333 | 33.33 | 833.33 | 866.67 | 2,500 |
| 4 | 2,500 | 25.00 | 833.33 | 858.33 | 1,667 |
| 5 | 1,667 | 16.67 | 833.33 | 850.00 | 833 |
| 6 | 833 | 8.33 | 833.33 | 841.67 | 0 |
| **Total** | | **175.00** | **5,000.00** | **5,175.00** | |

Celdas "4,167" resaltadas con recuadro rojo para enlazar saldo final mes 1 con saldo inicial mes 2.

## Slide 10

Título: "Comparación de métodos de amortización". Tabla comparativa:

| Característica | Sistema Francés | Sistema Alemán |
|---|---|---|
| Cuota | Constante (862.74 mensual). | Decreciente (de 883.33 a 841.67). |
| Amortización | Creciente (de 812.87 a 854.20). | Constante (833.33 mensual). |
| Total pagado (capital + interés) | 5,176.45 | 5,175.00 |
| Ventaja deudor | Cuotas estables. | Ahorro mínimo en intereses. |
| Ventaja acreedor | Mayor rentabilidad (intereses iniciales). | Recupera capital más rápido. |

## Slide 11

Slide de transición con foto de fondo (persona con lupa sobre casa miniatura y monedas, decorativa). Texto superpuesto: "Entre ambos métodos, la diferencia en intereses es mínima en préstamos a plazos cortos, pero se amplía en plazos largos."

## Slide 12

Slide separador de sección "2." con ícono de portapapeles. Texto: "Cálculo del escudo fiscal". Fondo decorativo: mano robótica tocando globo digital (igual que slide 4).

## Slide 13

Título: "Escudo fiscal". Ícono decorativo: escudo verde con monedas doradas.

Texto: Beneficio tributario generado por la deducción de intereses.

"Fórmula:" representada con 3 círculos conectados conceptualmente (diagrama de flujo horizontal, sin flechas explícitas, solo yuxtapuestos):
- Círculo gris: "Escudo Fiscal"
- Círculo celeste: "Intereses Pagados"
- Círculo celeste: "Tasa Impositiva"

Fórmula implícita: Escudo Fiscal = Intereses Pagados × Tasa Impositiva.

## Slide 14

Slide separador de sección "3." con ícono de portapapeles. Texto: "Flujo de caja de la deuda (financiamiento)". Fondo decorativo: mano robótica tocando globo digital (igual que slides 4 y 12).

## Slide 15

Título: "Línea de tiempo en los proyectos". Diagrama de 3 flechas/chevrons horizontales consecutivas (tipo proceso secuencial):

1. Flecha gris clara: "Flujo de caja económico" — Evalúa la rentabilidad del proyecto.
2. Flecha celeste (resaltada, al centro): "Flujo de caja de la deuda" — Incorpora el financiamiento.
3. Flecha gris oscura: "Flujo de caja financiero" — Mide el retorno al accionista.

Debajo de cada flecha hay una barra de color a juego con un ícono ilustrativo circular: barra gris con ícono de "cash flow" (dinero/gráficos), barra celeste con ícono de calendario y bolsas de dinero, barra gris con ícono de personas e intercambio de monedas (decorativos, refuerzan cada etapa).

## Slide 16

Título: "Flujo de caja de la deuda (financiamiento)". Ilustración decorativa a la derecha: círculo de íconos financieros (alcancía, chequera, tarjeta, billete, caja fuerte, foco, calculadora, maletín, flecha de crecimiento) rodeando un ícono central de moneda con flechas circulares (representa "ciclo de caja").

Bullets:
- Registra ingresos y pagos por financiamiento, como obtener y pagar préstamos o emitir acciones.
- Se analiza separado del flujo económico.

## Slide 17

Título: "Flujo de caja de la deuda (financiamiento)". Diagrama de 4 cuadrantes de color (rectángulo dividido en 4 secciones con esquinas redondeadas) con etiqueta central superpuesta "Componentes":

- Cuadrante superior izquierdo (gris claro): "Préstamos y financiamiento externo": Ingresos provenientes de créditos y otros financiamientos.
- Cuadrante superior derecho (celeste): "Pago de financiamiento": Amortización de capital y pago de intereses.
- Cuadrante inferior izquierdo (gris oscuro): "Emisión o recompra de acciones": Entradas de capital o pagos por la recompra de acciones propias.
- Cuadrante inferior derecho (celeste claro): "Dividendos": Pagos a los accionistas por las utilidades obtenidas.

## Slide 18

Título: "Flujo de caja de la deuda (financiamiento)". Tabla financiera (ejemplo numérico, préstamo de 500,000 a 3 años):

| | 0 | 2022 | 2023 | 2024 |
|---|---|---|---|---|
| Préstamo | 500,000 | | | |
| Amortización | | -163,377.34 | -166,644.88 | -169,977.78 |
| Interés | | -10,000.00 | -6,732.45 | -3,399.56 |
| Escudo fiscal | | 2,950.00 | 1,986.07 | 1,002.87 |
| **Flujo de caja de la deuda (financiamiento)** | **500,000** | **-170,427.34** | **-171,391.26** | **-172,374.47** |

## Slide 19

Slide separador de sección "4." con ícono de portapapeles. Texto: "Casos de aplicación". Fondo decorativo: mano robótica tocando globo digital (igual que slides 4, 12, 14).

## Slide 20

Título: "Caso EVALFIN – Parte 2". Ilustración decorativa a la derecha: personas con signo de interrogación y lupa sobre checklist (representa "análisis/preguntas").

Columna izquierda: El proyecto se financiará con un préstamo equivalente al 80% de la inversión en activos fijos y 70% del capital de trabajo inicial. El préstamo será en moneda extranjera (US$), con las siguientes condiciones:
- Plazo: 3 años, incluye 1 año de gracia.
- Amortización: cuotas anuales vencidas y fijas.
- Tasa de interés: TEA 10%.

El saldo de la inversión será financiado con aportes de capital de los accionistas. La tasa de impuesto a las utilidades es 30%. Para el financiamiento con capital propio se considera:

Columna derecha:
- Rendimiento libre de riesgo: 6%.
- Prima de riesgo de mercado: 15%.
- Riesgo país (Perú): 2.10%.

Se pide elaborar el Flujo de caja de la deuda (financiamiento).

## Slide 21

Título: "Caso Delta" (1/3). Caso de aplicación nuevo, no relacionado directamente con EVALFIN — enunciado de un proyecto (Delta Agroindustrial).

Columna izquierda: La empresa Delta Agroindustrial planea lanzar una nueva línea de conservas orgánicas para exportación. Según el estudio técnico, el proyecto requiere las siguientes inversiones iniciales:
- Terreno: US$ 50,000. No se deprecia y se proyecta una revalorización del 20% al año 5.
- Planta de procesamiento (obra civil): US$ 200,000, vida útil 20 años y valor residual del 60% al año 5.
- Maquinaria envasadora: US$ 80,000, vida útil 10 años y valor residual del 30% al final del proyecto.

Columna derecha:
- Equipos de control de calidad: US$ 15,000, vida útil 5 años y valor residual del 10%.
- Gastos preoperativos: US$ 25,000, amortizables linealmente en 5 años.

No se consideran inversiones adicionales durante la vida del proyecto.
- El proceso inicia con el pedido del cliente. Al día siguiente se emite la orden de compra de insumos. Los proveedores entregan en 7 días. Con insumos recibidos, la producción toma 15 días y el transporte al cliente 5 días.

## Slide 22

Título: "Caso Delta" (2/3). Continuación del enunciado.

Columna izquierda:
- Los clientes pagan 30 días después de recibir la mercancía. Los proveedores se pagan 25 días después de recibir los insumos. Se proyecta recuperar 80% del capital de trabajo al final del año 5.
- La empresa proyecta ingresos: Año 1: 50,000 unidades a US$ 5.20 por unidad. Años 2–5: crecimiento anual de 8% en unidades y 3% en precio.
- Egresos variables por unidad: Materia prima: US$ 2.10 (incluye 25% de merma).

Columna derecha:
Mano de obra directa: US$ 0.80. Envases y empaques: US$ 0.60.
- Costos fijos anuales: Sueldos administrativos: US$ 60,000 (crecen 5% anual). Publicidad: US$ 15,000 el primer año, con incremento anual de US$ 2,000. Mantenimiento: US$ 12,000. Servicios (luz, agua, gas): US$ 8,000. Seguros: US$ 5,000.
- La tasa del impuesto a la renta es 29.5%.

## Slide 23

Título: "Caso Delta" (3/3). Cierre del enunciado. Ilustración decorativa igual a slide 20 (personas con lupa y checklist).

Columna izquierda: Estructura de financiamiento del proyecto:
Préstamo BFR: US$ 100,000, plazo 5 años, tasa 8% anual, sistema de amortización francés.
Préstamo BSE: US$ 50,000, plazo 3 años, tasa 6% anual, sistema de amortización alemán.
Aportes de socios: US$ 80,000 (sin intereses ni amortización).
- Costos asociados al financiamiento (Año 0): Comisión por desembolso: 1% del monto total de los préstamos. Gastos notariales: US$ 1,000.

Columna derecha: Se pide elaborar los siguientes flujos de caja del proyecto a 5 años:
1. Flujo de caja de la inversión.
2. Flujo de caja operativo.
3. Flujo de caja económico.
4. Flujo de caja de la deuda (financiamiento).

## Slide 24

Slide de cierre, idéntica a la portada (slide 1). Título: "Flujo de Caja de la Deuda (Flujo de Caja del Financiamiento)". Subtítulo: "Evaluación Financiera de Proyectos - Semana 7". Fondo decorativo: túnel digital azul con silueta de robot, logos UTEC y TransformaTec (decorativa).
