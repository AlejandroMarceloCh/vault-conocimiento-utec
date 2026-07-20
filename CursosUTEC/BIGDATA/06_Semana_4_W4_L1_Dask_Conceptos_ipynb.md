---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L1 Dask Conceptos
slides: 0
fuente: 06 - Semana 4/W4 L1 Dask Conceptos.ipynb
---

<div id="cc2844ca-0581-4623-966c-6b5ea730a1f0" class="cell markdown">

# Introducción a Dask

- Curso Big Data
- Universidad UTEC
- Docente: Mg. Aldo Lezama Benavides

Dask es una librería de **computación paralela y distribuida** en Python.\
Permite trabajar con volúmenes de datos más grandes que la memoria de un computador y escalar desde un **laptop personal** hasta un **clúster de servidores**.

------------------------------------------------------------------------

## ¿Por qué usar Dask?

- **Limitaciones de NumPy y pandas**: funcionan muy bien, pero sólo si los datos caben en memoria RAM.\
- **Solución de Dask**: divide los datos en **bloques más pequeños (chunks)** y los procesa en paralelo.\
- Esto permite:
  - Procesar datasets más grandes que la RAM.\
  - Usar todos los **núcleos del procesador** disponibles.\
  - Escalar a entornos distribuidos como Hadoop, Spark o Kubernetes.

------------------------------------------------------------------------

## Conceptos clave de Dask

### Lazy Evaluation (Evaluación diferida)

- Dask **no ejecuta** las operaciones inmediatamente.\
- En lugar de eso, construye un **grafo de tareas**.\
- El cálculo ocurre solo cuando usamos `.compute()`.\
- Ventaja: Dask puede optimizar el orden de las operaciones antes de ejecutarlas.

### Chunks (bloques de datos)

- Los datos grandes se dividen en **bloques pequeños**.\
- Cada bloque se procesa de manera independiente.\
- Ejemplo:
  - Dataset de 100 millones de filas.\
  - Dask lo divide en 100 particiones de 1 millón cada una.\
- Estos bloques se procesan en paralelo y luego se combinan.

### Paralelización

- Dask aprovecha múltiples **núcleos de CPU** en tu laptop.\
- También puede trabajar en un **clúster de servidores**, distribuyendo las tareas entre varias máquinas.\
- Usa distintos **schedulers** (motores de ejecución):
  - **Threads** → múltiples hilos (por defecto).\
  - **Processes** → procesos independientes (útil cuando el GIL de Python limita).\
  - **Distributed** → para clusters.

------------------------------------------------------------------------

## Tipos de estructuras en Dask

### Dask Array

- Equivalente a un **NumPy array**, pero dividido en chunks.\
- Ideal para cálculos numéricos grandes: sumas, medias, multiplicaciones de matrices, álgebra lineal.

### Dask DataFrame

- Equivalente a un **pandas DataFrame**, pero dividido en particiones.\
- Ideal para datos tabulares grandes que no caben en memoria.\
- Sintaxis casi igual a pandas: `.head()`, `.groupby()`, `.mean()`.

### Dask Bag

- Equivalente a una **lista de Python**, pero paralelizada.\
- Útil para datos **semi-estructurados** como texto, JSON o logs.\
- Tiene operaciones tipo `map`, `filter`, `reduce`.

------------------------------------------------------------------------

## Grafo de tareas

- Cada operación en Dask se traduce en un **grafo de tareas**.\
- Los nodos son operaciones y las flechas son dependencias.\
- Antes de ejecutar, Dask construye este grafo y lo optimiza para reducir costos.\
- Una vez optimizado, ejecuta todas las operaciones en paralelo.

------------------------------------------------------------------------

## Cuándo conviene usar Dask

- Cuando los datos son **más grandes que la RAM**.\
- Cuando queremos aprovechar **múltiples núcleos** del procesador.\
- Cuando necesitamos escalar a un **clúster distribuido**.\
- Cuando queremos usar **la misma sintaxis de NumPy/pandas**, pero con mayor escalabilidad.

**Importante**:

- Para datasets pequeños, NumPy/pandas suelen ser más rápidos.\
- Dask introduce algo de overhead en la coordinación de tareas.

------------------------------------------------------------------------

## Resumen final

- Dask es una librería que extiende **NumPy, pandas y listas de Python** al mundo del cómputo paralelo y distribuido.\

- Sus principios clave son:

  - **Lazy evaluation** → operaciones diferidas.\
  - **Chunks** → división de datos en bloques pequeños.\
  - **Paralelización** → ejecución en múltiples núcleos o máquinas.\

- Sus estructuras principales son:

  - **Dask Array** (numérico)\
  - **Dask DataFrame** (tabular)\
  - **Dask Bag** (semi-estructurado)\

- **Grafo de tareas**: describe y optimiza los cálculos antes de ejecutarlos.

- Con Dask, podemos trabajar con datos que no caben en memoria y aprovechar mejor el hardware disponible.

</div>

<div id="7602ff0e-3ce4-49c0-939c-f1ed030c1ef2" class="cell code">

``` python
```

</div>
