---
curso: IO1
titulo: Semana02-Capitulo1
slides: 59
fuente: Semana02-Capitulo1.pdf
---

## Slide 1
Portada. Título "Investigación de operaciones I" / "Capítulo 1: Introducción". Solo logo UTEC (decorativo) y texto de portada, sin contenido adicional.

## Slide 2
**Investigación de operaciones**
- En inglés: **Operations** Research (US) u **Operational** Research (UK)
- Se dice también "Management Science" o "Decision Science"
- Es un pilar de la **Ingeniería Industrial**

## Slide 3
**Propósito**
En investigación de operaciones, mejoramos algo! La definición de INFORMS: **The Science of Better**

## Slide 4
**Temas que tienen mucho que ver con la investigación de operaciones** (lista 1/2):
- Ingeniería industrial
- Data mining / Data science / Big data
- Análisis de decisión
- Business analytics
- Teoría de grafos
- Programación matemática
- Teoría de juegos
- Simulación

## Slide 5
**Temas que tienen mucho que ver con la investigación de operaciones** (lista 2/2):
- Procesos estocásticos
- Supply chain management
- Logística
- Gestión de proyectos
- Computer Science
- Pronósticos

## Slide 6
**¿Qué significa "optimizar"?**
Optimizar es encontrar una solución que no podría ser mejor: una solución **óptima**.

## Slide 7
Slide de transición (solo título grande): "A ver... ¿qué podemos optimizar?"

## Slide 8
Slide de transición (solo título grande): "Problemas 'fáciles' de optimización"

## Slide 9
**Encontrar el camino más corto para ir de la casa a la UTEC**
Diagrama: grafo no dirigido con ~25 nodos (círculos azules) conectados por aristas etiquetadas con pesos numéricos (1 a 7, valores de distancia/costo). Nodo de origen resaltado en **verde** (arriba a la izquierda, "la casa") y nodo destino resaltado en **rojo** (abajo a la derecha, "la UTEC"). El grafo representa una red de calles/caminos; el objetivo es hallar la ruta de menor costo acumulado entre el nodo verde y el nodo rojo (problema de camino más corto / shortest path).

## Slide 10
**Problema de emparejamiento máximo en un grafo bipartito**
Imagen: fotografía en blanco y negro de dos piezas de rompecabezas encajadas, con las palabras "ME" y "YOU" escritas a mano, simbolizando el emparejamiento (matching) entre dos partes.

## Slide 11
Diagrama de grafo bipartito: lado izquierdo (celeste) con nodos **Jeff, Vaughn, Troy, Pierce, Abed**; lado derecho (rosado) con nodos **Britta, Annie, Lunch Lady, Shirley, Super Model**. Múltiples aristas finas cruzadas conectan cada nodo izquierdo con varios nodos derechos (relaciones de preferencia/posible emparejamiento), sin resaltar ninguna combinación particular todavía.

## Slide 12
Mismo grafo bipartito que la slide 11 (Jeff/Vaughn/Troy/Pierce/Abed ↔ Britta/Annie/Lunch Lady/Shirley/Super Model), pero ahora con un subconjunto de aristas resaltadas en **verde/teal grueso**: Jeff–Lunch Lady, Vaughn–Britta, Troy–Annie, Pierce–Super Model, Abed–Shirley (aprox., representando un emparejamiento máximo/una solución seleccionada), mientras el resto de aristas quedan finas en gris.

## Slide 13
**Problema de los matrimonios estables**
Misma imagen que la slide 10: piezas de rompecabezas "ME" / "YOU" en blanco y negro (decorativa/temática, reutilizada).

## Slide 14
Diagrama de grafo bipartito reducido a 3+3: lado izquierdo **Jeff, Abed, Troy**; lado derecho **Britta, Annie, Shirley**. Cada nodo izquierdo tiene una lista de preferencias numeradas (1,2,3 en azul, orden de preferencia hacia el lado derecho) y cada nodo derecho tiene su propia lista de preferencias numeradas (1,2,3 en magenta) hacia el lado izquierdo. Un subconjunto de aristas está resaltado en **verde oliva** representando un emparejamiento propuesto (Jeff–Britta, Abed–Annie, Troy–Shirley aprox.). Debajo, texto manuscrito en rojo: "¿estables?" — pregunta si ese emparejamiento es estable dado el ranking de preferencias.

## Slide 15
Igual que la slide 14 (mismo grafo, mismas preferencias numeradas y aristas verdes resaltadas), agregando la línea de texto: "Observan las preferencias de Jeff y Britta!" — pide al alumno fijarse específicamente en ese par para detectar una posible inestabilidad (ambos podrían preferirse mutuamente más que a sus parejas actuales).

## Slide 16
Igual que la slide 14/15 (mismo diagrama), con la pregunta añadida: "¿Una idea para obtener matrimonios estables?" — invita a proponer un algoritmo (alusión al algoritmo de Gale-Shapley, aunque no se nombra explícitamente).

## Slide 17
Arriba: versión miniatura del mismo diagrama de matrimonios estables (Jeff/Abed/Troy ↔ Britta/Annie/Shirley con preferencias numeradas y "¿estables?"). Abajo, sección **Aplicaciones**:
- Vendedores / compradores: problema de eficiencia del mercado
- Buscador de trabajo / Oferta de puesto
- Donación de riñones
- etc.

## Slide 18
Slide de transición (solo título grande): "Problemas 'difíciles' de optimización"

## Slide 19
**Problema de viajante de comercio**
Conocido en inglés como *Traveling Salesman Problem* (TSP)

## Slide 20
Mapa de Estados Unidos (color arena) con ~25 puntos azules distribuidos por distintos estados (representando ciudades a visitar). Una flecha roja curva señala una región central (zona de Illinois/Chicago), ilustrando visualmente el reto de encontrar la ruta óptima que conecte todos los puntos (instancia visual del TSP).

## Slide 21
Dos fotografías en escala de grises lado a lado: a la izquierda un **circuito integrado (IC)** — chip de silicio con patrón denso de líneas de conexión; a la derecha una **placa de circuito impreso (PCB)** — tablero verde/negro con múltiples pistas de cobre y componentes soldados. Etiquetas debajo de cada imagen: "Integrated Circuit (IC)" y "Printed Circuit Board (PCB)". Ilustra un caso real de TSP: el orden de perforación/conexión de miles de puntos en la fabricación de circuitos.

## Slide 22
Texto manuscrito en rojo "442 hoyos" junto a fotografía de una placa de circuito verde inclinada en perspectiva, mostrando cientos de orificios metalizados (hoyos) y pistas de cobre — ejemplo concreto de instancia TSP con 442 puntos a conectar en el orden más corto posible.

## Slide 23
Texto manuscrito en rojo "2103 hoyos". A la derecha, una cuadrícula de 4×4 paneles con patrones de puntos negros dispersos (representando la disposición física real de 2103 orificios/pines en una placa), cada panel mostrando un patrón similar repetido — instancia aún mayor de TSP.

## Slide 24
Texto manuscrito en rojo "Solución utilizada en producción". Diagrama: malla de nodos negros conectados por una ruta magenta/rosada que zigzaguea recorriendo todos los puntos en un patrón de filas, con algunas diagonales largas cruzando el gráfico — visualiza la ruta (no óptima) efectivamente usada en la línea de producción real para conectar los 2103 hoyos.

## Slide 25
Texto manuscrito en rojo "Solución óptima". Diagrama similar al de la slide 24 (misma malla de nodos), pero con la ruta magenta más compacta y ordenada, sin las diagonales largas cruzando todo el tablero — muestra la ruta óptima calculada para el mismo problema de 2103 puntos, notablemente más corta/eficiente que la solución de producción.

## Slide 26
**DNA sequencing** (título manuscrito en rojo). Imagen: diagrama técnico ilustrado (estilo libro de texto) del proceso de secuenciación de ADN: una hebra de ADN ("Strand to be sequenced") con un primer, mezclas de reacción con cuatro nucleótidos diferentes (colores: A, C, G, T en frascos), fragmentos "primed DNA", productos de replicación separados por electroforesis en gel, y lectura de la secuencia como complemento de las bandas ("Read sequence as complement of bands containing labeled strands"), con la secuencia de ejemplo "ATTCAGCAGGACTA" al pie. A la derecha, dos pasos numerados:
1. Cortar el ADN en millones de pequeños fragmentos de nucleótidos
2. Leer entre 500 y 700 nucleótidos a la vez a partir de los fragmentos

## Slide 27
**DNA Sequencing** — Un reto computacional:
- Ensamblar los fragmentos en una única cadena de nucleótidos (superstring) tal que su tamaño sea lo más pequeño posible.
- Antes de los años 1990 este problema fue considerado como imposible de resolver.

## Slide 28
**DNA Sequencing** — Ejemplo con cadenas de bits:
- Conjunto de fragmentos: {000, 001, 010, 011, 100, 101, 110, 111}
- Fragmentos concatenados (superstring): 000001010011100101110111
- Shortest superstring: se muestra el proceso de superposición (overlap) de fragmentos con líneas verdes conectando extremos coincidentes, reduciendo la cadena original hasta la forma más corta:
```
0001110100
000    010
 001    100
  011101
    110
    111
```
(cada línea muestra cómo los fragmentos de 3 bits se superponen entre sí para formar la superstring más corta de 10 caracteres)

## Slide 29
**DNA Sequencing** — Ejemplo con nucleótidos:
- Conjunto de fragmentos: {ATC, CCA, CAG, TCC, AGT}
- Fragmentos concatenados (superstring): ATCCCACAGTCCAGT
- Shortest superstring?

Diagrama etiquetado **TSP**: grafo dirigido completo de 5 nodos (ATC, CCA, TCC, CAG, AGT) dispuestos en pentágono, con aristas dirigidas etiquetadas con pesos (0,1,2) representando el costo de solapamiento entre fragmentos. Un subconjunto de aristas está resaltado en **magenta/rosa fuerte** con flechas (ATC→CCA→TCC→CAG→AGT aprox.), formando un ciclo/ruta que representa la solución de menor costo total — modela el problema de shortest superstring como un TSP sobre el grafo de solapamientos.

## Slide 30
**Partitioning problem**
Tenemos un conjunto de 10 pelotas, cada con un peso — diagrama de 10 círculos rojos dispuestos en pirámide (4-3-2-1) con los valores: fila superior 12; siguiente 9, 22; siguiente 7, 20, 13; fila inferior 11, 10, 8, 17.
**Objetivo:** Compartir (particionar) las 10 pelotas en 2 grupos (particiones) tal que la diferencia de las sumas en cada grupo sea la menor posible.

## Slide 31
**Knapsack problem (problema de la mochila)**
Imagen: mochila de tela marrón con etiqueta "max: 30kg" señalada por una flecha roja manuscrita. A la izquierda, 7 objetos numerados (círculos azules) con su valor y peso escritos a mano:
1. $10 millones, 11kg
2. $2 millones, 3kg
3. $7 millones, 5kg
4. $11 millones, 15kg
5. $3 millones, 4kg
6. $9 millones, 6kg
7. $1 millón, 2kg
Objetivo implícito: elegir el subconjunto de objetos que maximice el valor sin exceder 30kg.

## Slide 32
Idéntica a la slide 31 (mismos 7 objetos, mismos valores/pesos, mochila "max: 30kg"), pero los círculos numerados 1, 2, 5, 6 cambian de azul a **verde** — posiblemente resaltando una solución propuesta o un subconjunto seleccionado de objetos para la mochila.

## Slide 33
Slide de transición (solo título grande): "¿Donde optimizar?"

## Slide 34
**Optimización de smart grids**
Cuatro fotografías: (arriba izq.) parque eólico con turbinas blancas en campo; (abajo izq.) represa hidroeléctrica con embalse y liberación de agua; (derecha, grande) planta de paneles solares fotovoltaicos sobre césped verde bajo cielo azul.

## Slide 35
**Optimización de evacuación de emergencia en producción petrolera offshore**
Izquierda: fotografía de plataforma petrolera offshore al atardecer. Derecha: captura de pantalla de radar satelital meteorológico ("ENHANCED SATELLITE") mostrando el Huracán Irma y tormentas tropicales Katia y Jose en el Caribe/Golfo de México, con datos de ubicación, viento (185 MPH) y presión. Texto: "200 plataformas / 30.000 trabajadores". Logo de **PEMEX** abajo a la derecha.

## Slide 36
**Optimización en radioterapia e imaginería médica**
Izquierda: fotografía de un paciente acostado en una máquina de radioterapia (acelerador lineal marca ELEKTA) con personal médico presente. Derecha/abajo: tres imágenes de tomografía (cortes axiales de cabeza/cuello) con superposición de contornos de colores (mapas de dosis de radiación) etiquetadas "Orig.plan", "1st replan", "2nd replan" — muestran la evolución/optimización del plan de tratamiento de radiación.

## Slide 37
**Optimización para operaciones portuarias**
Tres fotografías de puertos de contenedores: grúas cargando/descargando contenedores de colores desde un buque portacontenedores, vista aérea de grúas pórtico (STS cranes) sobre un patio de contenedores, y otra vista de grúas azules operando junto a un barco rojo.

## Slide 38
**Optimización en minería**
Fotografía de una mina a tajo abierto (open-pit) de gran escala, con terrazas escalonadas talladas en la montaña y montañas nevadas al fondo.

## Slide 39
**Optimización en el sector Oil & Gas**
Tres fotografías: planta industrial petroquímica con tuberías azules; helicóptero amarillo de la compañía "PHI" sobrevolando una plataforma petrolera offshore; camión cisterna de combustible de la marca REPSOL.

## Slide 40
**Optimización en finanzas**
Dos fotografías: fachada de edificio con letrero "BANK" en vidrio reflectante; local comercial con letrero "BCP" (Banco de Crédito del Perú).

## Slide 41
**Optimización en transporte**
Tres imágenes: mapa esquemático de líneas de metro/subte (estilo plano de París, con múltiples líneas de colores y estaciones); camión de reparto FedEx Express en autopista; fila de aviones comerciales alineados en pista de aeropuerto esperando despegue.

## Slide 42
**Optimización en Data Science**
Gráfico de dispersión 2D: puntos rojos (círculos huecos) agrupados en la esquina superior izquierda y puntos azules (círculos rellenos) agrupados en la esquina inferior derecha, separados por una línea recta diagonal negra. Texto manuscrito rojo: "Support Vector Machine" — ilustra el concepto de encontrar el hiperplano separador óptimo entre dos clases.

## Slide 43
**Optimización en Data Science** (continuación)
Mismo gráfico de dispersión (puntos rojos vs azules) que la slide 42, ahora mostrando dos líneas: una fina diagonal (separador subóptimo) y una gruesa con un **margen amarillo sombreado** entre dos líneas discontinuas paralelas — ilustra el concepto de maximizar el margen entre clases en SVM (la línea gruesa con máximo margen es la solución óptima).

## Slide 44
Slide de transición (solo título grande): "Lo que se necesita saber antes de empezar el curso"

## Slide 45
**Expresiones lineales y desigualdades**
- Ejemplo 1: $x + y \le 9$
- Ejemplo 2: $x_1 + 2x_2 - 4x_3 \le 6$
- Los conocimientos básicos de matemáticas o de álgebra lineal son útiles per no indispensables.

## Slide 46
**Sumatorias**
Si $x_i$ representa la cantidad de botellas de soda producidas por la línea de producción $i$, la producción total de botellas por todas las $N$ líneas de producción se puede escribir como:
$$\sum_{i=1}^{N} x_i = x_1 + x_2 + \cdots + x_N$$

## Slide 47
**Sumatorias** (continuación)
Si tenemos que producir al menos 10000 botellas utilizando todas las líneas de producción, podemos escribir:
$$\sum_{i=1}^{N} x_i \ge 10000.$$
Se utiliza frecuentemente notación de conjuntos para escribir una sumatoria. Si $L$ es el conjunto de líneas de producción $\{1,\dots,N\}$, podemos escribir:
$$\sum_{i \in L} x_i \ge 10000.$$

## Slide 48
**Sumatorias** (doble sumatoria)
Si $L$ representa el conjunto de líneas de producción $\{1,\dots,N\}$, y $S$ representa el conjunto de tipos de soda $\{1,\dots,M\}$, y si $x_{ij}$ representa el número de botellas del soda $j \in S$ producidas por la línea de producción $i \in L$, la expresión:
$$\sum_{i \in L} \sum_{j \in S} x_{ij}$$
representa la cantidad de botellas de todo tipo de soda producida por todas las líneas de producción.

## Slide 49
**Sumatorias** (equivalencias)
La expresión
$$\sum_{i \in L} \sum_{j \in S} x_{ij}$$
es equivalente a la expresión
$$\sum_{j \in S} \sum_{i \in L} x_{ij}.$$
Se puede también escribir de forma sintética:
$$\sum_{i \in L,\, j \in S} x_{ij}.$$

## Slide 50
**Sumatorias** (notación de cardinal)
Frecuentemente, al lugar de definir el conjunto de líneas por $L = \{1,\dots,N\}$, con $N$ representando el número de líneas, escribiremos $\{1,\dots,|L|\}$ donde $|L|$ es el número de elementos en el conjunto $L$. Se dice que $|L|$ es el cardinal del conjunto $L$.

## Slide 51
**Conjunto de enteros no negativos**
Es el conjunto de números enteros desde 0 hasta $+\infty$. Se escribe:
$$\mathbb{N} = \{0, 1, 2, \dots\}$$

## Slide 52
**Conjunto de enteros relativos**
Es el conjunto de números enteros desde $-\infty$ hasta $+\infty$. Se escribe:
$$\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$$

## Slide 53
**Conjunto de enteros positivos**
$$\mathbb{N}^* = \{1, 2, \dots\}$$

## Slide 54
Slide de transición (solo título grande): "Operaciones sobre conjuntos"

## Slide 55
**Intersección** de conjuntos:
$$\{1,2,3\} \cap \{3,4,5\} = \{3\}$$
**Unión** de conjuntos:
$$\{1,2,3\} \cup \{3,4,5\} = \{1,2,3,4,5\}$$
**Diferencia** de conjuntos:
$$\{1,2,3,4,5\} \setminus \{3,4\} = \{1,2,5\}$$
$$\mathbb{N}^* = \mathbb{N} \setminus \{0\}$$

## Slide 56
Slide de transición (solo título grande): "Cuantificadores"

## Slide 57
**Cuantificador "para todo"**
Cada línea de producción (del conjunto $L$) produce al menos 1000 botellas:
$$x_i \ge 1000, \quad \forall i \in L.$$
Se lee: "la producción de la línea $i$ es mayor que 1000 botellas, para todas las líneas de $L$" o: "Para cualquiera línea de producción $i$ de $L$, su producción es mayor que 1000 botellas" o: "Para cada línea de producción $i$ de $L$, ...".

## Slide 58
**Cuantificador "existe"**
Existe al menos una línea de producción de $L$ que produce 1000 botellas:
$$\exists i \in L : x_i \ge 1000.$$
**Cuantificador "existe uno y sólo uno"**
Existe una y sola una línea de producción de $L$ que no produce botellas:
$$\exists! i \in L : x_i = 0.$$

## Slide 59
Slide final (solo título grande): "Fin del capítulo 1"
