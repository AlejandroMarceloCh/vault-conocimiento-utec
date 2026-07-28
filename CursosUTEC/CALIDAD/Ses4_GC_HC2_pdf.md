---
curso: CALIDAD
titulo: Ses4_GC_HC2
slides: 14
fuente: Ses4_GC_HC2.pdf
---

## Slide 1

Portada: "Las 7 Herramientas de la Calidad". Fondo celeste degradado con foto decorativa del edificio UTEC y logo UTEC + tagline "Reinventa el mundo". Sin contenido temático adicional (decorativa).

## Slide 2

Título "Objetivo". Texto entre corchetes decorativos: "Identificar y medir el proyecto de mejora. Así como el alcance de este. Se utilizará las principales herramientas básicas de la Calidad". Sin elementos visuales adicionales de contenido.

## Slide 3

Título "Contenido de sesión aquí" (placeholder de plantilla, sin editar). Tres bloques numerados con corchetes decorativos:
- 01. Diagrama Pareto.
- 02. Diagrama de dispersión
- 03. Muestreo de estratificación.

## Slide 4

Título "Diagrama de Pareto". Texto resaltado en amarillo: "Un diagrama de Pareto es una gráfica de barras. El largo de las barras representa la frecuencia o el costo, o el tiempo, o el dinero, y son acomodados con barras largas a la izquierda y las barras cortas a la derecha. De esta manera el gráfico representa visualmente qué situaciones son más significativos."

Debajo, captura de un gráfico de Pareto de ejemplo ("Diagrama Pareto nº reclamaciones empresa gráfica"):
- Eje Y izquierdo: "nº reclamaciones" con marcas 87, 187, 287, 387, 487.
- Eje Y derecho: "% acumulado" con marcas 0% a 100%.
- Eje X ("Causas"): Arrugas, entrega, Repintado, Molas, encuadernación, papel, los acabados, tintas, ganancia, Errores de texto, montaje, facturación, Errores de corte, registro, imágenes, color, transporte, Varios — barras azules decrecientes de izquierda a derecha.
- Línea de % acumulado (curva negra con marcadores blancos) que sube y cruza la línea roja horizontal en 80% justo en la intersección con la línea roja vertical trazada aproximadamente en la barra "encuadernación" (valor cercano a 387 reclamaciones), marcando el punto donde se alcanza el 80% acumulado.

## Slide 5

Título "Diagrama de Pareto" (continuación). Lateral derecho: "Como Hacer Diagrama Pareto?" (pregunta guía, sin desarrollo textual adicional en la slide).

Tabla de datos reproducida:

| Tipos de Defecto/Ocurrencia de eventos | Lunes | Martes | Miercoles | Jueves | Viernes | Sabado | Domingo | TOTAL |
|---|---|---|---|---|---|---|---|---|
| Mesas sucias | 1 | 0 | 0 | 3 | 4 | 9 | 9 | 26 |
| Anfitrion no saluda | 3 | 3 | 7 | 8 | 1 | 12 | 13 | 47 |
| Baños sucios | 1 | 1 | 1 | 4 | 9 | 7 | 5 | 28 |
| Demora con la cuenta | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 5 |
| No hay algun producto | 0 | 1 | 3 | 1 | 2 | 1 | 0 | 8 |
| Demora en la preparacion | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 6 |
| Alimentos fuera de temperatura | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Pocos mozos | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| Temperatura del ambiente | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 3 |
| Volumen muy alto | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 4 |
| **TOTAL** | 9 | 9 | 13 | 18 | 20 | 31 | 30 | 130 |

Es la base de datos que alimentaría un diagrama de Pareto (ejemplo restaurante).

## Slide 6

Título "Diagrama de Pareto" (continuación). Lateral derecho: "Como Interepretar Diagrama Pareto?" (pregunta guía).

Gráfico de Pareto construido a partir de la tabla anterior (datos del restaurante), ordenado de mayor a menor:
- Eje Y izquierdo "Counts" (0 a 50). Eje Y derecho % acumulado (0% a 120%).
- Barras (azul/lila) con valores: Anfitrion no saluda=47, Baños sucios=28, Mesas sucias=26, No hay algun producto=8, Demora en la preparacion=6, Demora con la cuenta=5, Volumen muy alto=4, Temperatura del ambiente=3, Pocos mozos=2, Alimentos fuera de temperatura=1.
- Línea naranja de % acumulado con etiquetas: 36%, 58%, 78%, 84%, 88%, 92%, 95%, 98%, 99%, 100%.
- Se observa que las primeras 3 causas (Anfitrion no saluda, Baños sucios, Mesas sucias) ya acumulan 78% de los defectos — ejemplifica el principio 80/20.

## Slide 7

Título "Diagrama de dispersión". Texto resaltado en amarillo: "Los diagramas de dispersión grafican pares de datos numéricos, con una variable en cada eje, para buscar una relación entre ellos. Si se correlacionan las variables, los puntos caerán a lo largo de una línea o curva. Cuanto mejor sea la correlación, los puntos estarán más pegados a la línea de tendencia."

Debajo, gráfico "Diagrama de Dispersión" (captura tipo Excel):
- Eje X: "peso" (50 a 100). Eje Y: "estatura" (1,5 a 2,0).
- Puntos azules (serie "estatura") dispersos con tendencia positiva.
- Línea de tendencia lineal negra ("Lineal (estatura)").
- Ecuación de la recta: y = 0,0055x + 1,3685
- Coeficiente de determinación: R² = 0,5003
- Interpretación implícita: correlación positiva moderada entre peso y estatura.

## Slide 8

Título "Diagrama de dispersión" (continuación). Lateral derecho: "Como seleccionar el diagrama de dispersión?"

Imagen tipo diagrama/matriz de decisión titulada "TIPOS DE PRUEBAS ESTADISTICAS" (fondo negro), con un eje Y etiquetado "CONTINUA" arriba y "DISCRETA" abajo, y eje X etiquetado "DISCRETA" (izquierda, subdividido en "1" y "2" muestras) y "CONTINUA" (derecha), con línea roja de referencia en el valor 30 (ambos ejes). Cuadrantes:
- Arriba-izquierda (Y continua, X discreta ≤30): ANOVA (3 a +)
- Arriba-derecha (Y continua, X continua): CORRELACIÓN Y REGRESIÓN
- Abajo-izquierda (Y discreta, X discreta): CHI CUADRADO
- Abajo-derecha (Y discreta, X continua): REGRESIÓN LOGÍSTICA

Este diagrama ubica el diagrama de dispersión/correlación-regresión como la prueba adecuada cuando ambas variables (X e Y) son continuas.

## Slide 9

Título "Diagrama de dispersión" (continuación). Lateral derecho: "Como Hacer Diagrama de dispersión?"

Tabla de datos de ejemplo (50 personas) con columnas "N° Persona | Altura (m) | Peso (Kg.)" repetida en dos bloques (personas 001-025 y 026-050). Valores de altura entre 1.51 y 2.00 m, peso entre 58.0 y 97.6 kg. Es la base de datos cruda para construir un diagrama de dispersión altura vs. peso (no se reproduce fila por fila por ser tabular extensa de datos crudos, pero se conserva el rango: alturas 1.51–2.00 m, pesos 58.0–97.6 kg, 50 registros).

## Slide 10

Título "Diagrama de dispersión" (continuación). Lateral derecho: "Como Interpretar Diagrama de dispersión?"

Imagen (fondo negro) titulada "CORRELACIÒN": "Es la Fuerza de Asociación entre 2 Variables. Se mide con el Coeficiente de Pearson (r) -1 ≤ r ≤ 1. Cuánto más cercano esté el coeficiente de Correlación de Pearson a −1 o 1; mayor probabilidad de Correlación."

Tres mini-gráficos de dispersión de ejemplo, lado a lado:
- Izquierda: puntos con tendencia descendente clara → "-1 ≤ r < 0 — Correlación Negativa"
- Centro: nube de puntos azules sin patrón → "r = 0 — No hay Correlación"
- Derecha: puntos con tendencia ascendente clara → "0 < r ≤ 1 — Correlación Positiva"

Texto en amarillo/naranja al pie: "Precauciones: Dado que no estamos modificando el proceso (variando x) y midiendo su efecto (en Y): encontrar que "hay correlación" no siempre significa que al variar X, variará Y (Causa – Efecto). Solo debemos usar correlación cuando hay una persuasión razonable que X podría afectar Y."

## Slide 11

Título "Diagrama de Estratificación". Texto resaltado en amarillo: "La estratificación es una técnica utilizada en combinación con otras herramientas de análisis de datos. Cuando los datos de una variedad de fuentes o categorías se han agrupado juntos, el significado de los datos puede ser imposible ver. Esta técnica separa los datos de modo que los patrones se pueden ver."

Debajo, gráfico de dispersión estratificado "Purity vs. Iron":
- Eje X: "Iron (parts per million)" de 0.10 a 0.70.
- Eje Y: "% Purity" de 98.0 a 100.0.
- Tres series marcadas con símbolos distintos y agrupadas en contornos (óvalos) separados: ● Reactor 1, △ Reactor 2, □ Reactor 3.
- Se ven dos bandas/grupos claramente diferenciados: una banda superior (mayor pureza, ~99.0–99.8%) que agrupa mayormente Reactor 1 y Reactor 2, y una banda inferior (~98.2–99.0%) que agrupa mayormente Reactor 3 — ilustra cómo estratificar por reactor revela un patrón que estaba oculto al ver todos los puntos juntos.

## Slide 12

Título "Diagrama de Estratificación" (continuación). Texto: "Los Diagramas de Estratificación se utilizan para determinar si una salida (y) se estratifica de acuerdo con una categoría relacionada a la salida. Si los datos son estratificados, los puntos trazados exhiben patrones únicos asociados a la categoría."

"Estos son ejemplos de diferentes fuentes que podrían requerir que la data sea estratificada:" — lista con viñetas:
- Equipos
- Turnos
- Departamentos
- Materiales
- Proveedores
- Días de la semana
- Tiempo durante el día
- Productos

## Slide 13

Título "Conclusiones". Dos bloques numerados con corchetes decorativos:
- 01. Aprenderás a seleccionar las herramientas de calidad
- 02. Aprenderás a usar las herramientas de calidad

## Slide 14

Slide de cierre: fondo celeste degradado con logo grande de UTEC ("Universidad de Ingeniería y Tecnología") centrado y elementos gráficos decorativos (hexágonos, cruz dorada, círculo). Sin contenido temático (decorativa).
