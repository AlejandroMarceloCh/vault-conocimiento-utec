---
curso: ML
titulo: tSNE_UMAP_CS3061_UTEC_ML
slides: 41
fuente: tSNE_UMAP_CS3061_UTEC_ML.pdf
---

## Slide 1

# t-SNE & UMAP
# Reducción No Lineal
# de Dimensionalidad

*Exploración Geométrica en Espacios de Alta Dimensión*

## Slide 2

# Agenda

*Contenido de la sesión*

1. Motivación y Límites de PCA
2. t-SNE: Intuición y Fundamentos
3. t-SNE: Matemática y Algoritmo
4. UMAP: Intuición y Variedades
5. UMAP: Matemática y Algoritmo
6. Comparación PCA vs t-SNE vs UMAP
7. Implementación en Python

## Slide 3

01

**Motivación:**
**¿Por qué PCA no es suficiente?**

## Slide 4

# The Curse of Dimensionality

*La maldición de la dimensionalidad*

**Espacio de Alta Dimensión**
Los vectores de datos de alta dimensión X ∈ ℝⁿ no pueden visualizarse directamente. Necesitamos proyectarlos en 2D o 3D.

**Problema de distancias**
En alta dimensión, todos los pares de puntos tienden a ser equidistantes. Las métricas de distancia pierden significado.

**PCA: limitación clave**
PCA solo captura relaciones LINEALES. Si los clusters tienen geometría curva o no lineal, PCA los aplasta y mezcla.

**¿Qué necesitamos?**
Métodos que preserven la ESTRUCTURA LOCAL: si dos muestras eran vecinas en el espacio original, deben serlo en 2D. Aquí entran t-SNE y UMAP.

💡 **Reflexión:** ¿Por qué visualizar datos en 2D/3D es útil antes de entrenar un clasificador?

## Slide 5

# When PCA Fails

*Cuándo PCA no es suficiente*

**PCA en datos con curva tipo Swiss Roll**

Datos originales:
Puntos en espiral 3D bien separados

Después de PCA 2D:
Todo colapsado y mezclado
❌ Grupos inseparables

**Figura:** Dos gráficos lado a lado. A la izquierda, "Swiss Roll": nube de puntos en 3D (ejes de 0 a 10 y de -10 a 10 aproximadamente) formando una espiral enrollada, con puntos coloreados en azul y rojo entremezclados siguiendo la curva. A la derecha, "PCA": proyección 2D resultante (eje PC2 de -10 a 20, eje horizontal de -10 a 10) donde los puntos azules y rojos quedan mezclados formando un anillo/óvalo, sin separación clara entre clases.

*Principio clave: PCA preserva varianza global · t-SNE/UMAP preservan vecindad local*

## Slide 6

# When PCA Fails

*Cuándo PCA no es suficiente*

**PCA en datos con curva tipo Swiss Roll**
Datos originales: Puntos en espiral 3D bien separados
Después de PCA 2D: Todo colapsado y mezclado
❌ Grupos inseparables

**t-SNE / UMAP en los mismos datos**
Datos originales: Los mismos puntos en espiral 3D
Después de t-SNE/UMAP 2D: Estructura preservada
✅ Grupos claramente separados

*Principio clave: PCA preserva varianza global · t-SNE/UMAP preservan vecindad local*

## Slide 7

# When PCA Fails

*Cuándo PCA no es suficiente*

**t-SNE / UMAP en los mismos datos**
Datos originales: Los mismos puntos en espiral 3D
Después de t-SNE/UMAP 2D: Estructura preservada
✅ Grupos claramente separados

**Figura:** Dos gráficos apilados. Arriba, nube de puntos 3D (n_samples=1500) formando una espiral tipo Swiss Roll, coloreada con gradiente continuo (escala de color viridis, de morado/azul a verde/amarillo) que indica la posición a lo largo de la variedad. Abajo, "t-SNE Embedding of Swiss Roll": proyección 2D (ejes aproximadamente -30 a 40 en ambos) donde la espiral aparece "desenrollada" en una franja continua, conservando el mismo gradiente de color de un extremo a otro, mostrando que la estructura de vecindad local se preservó.

*Principio clave: PCA preserva varianza global · t-SNE/UMAP preservan vecindad local*

## Slide 8

02

**t-SNE**
**t-distributed Stochastic Neighbor**
**Embedding**

## Slide 9

# t-SNE: Core Intuition

*Intuición fundamental*

**La idea central:**
"Si dos puntos son vecinos en alta dimensión, deben seguir siendo vecinos en 2D"

① Mide cercanía en alta dimensión usando probabilidades Gaussianas centradas en cada punto
② Coloca puntos aleatoriamente en 2D e inicializa posiciones
③ Mide cercanía en 2D usando distribución t-Student (cola pesada)
④ Optimiza iterativamente: mueve puntos en 2D hasta que ambas distribuciones coincidan

💡 **Reflexión:** ¿Por qué t-SNE usa distribución t-Student en 2D y no la misma Gaussiana que en alta dimensión?

## Slide 10

# t-SNE: High-D Similarities

*Similitudes en alta dimensión (Paso 1)*

Para cada par de puntos i, j en ℝⁿ, calculamos la probabilidad condicional:

$p(j|i) = \exp(-\|x_i - x_j\|^2 / 2\sigma_i^2) / \sum_{k \neq i} \exp(-\|x_i - x_k\|^2 / 2\sigma_i^2)$

**σᵢ (Perplexity)**
Ajustado automáticamente según la densidad local alrededor de i. Controla el 'radio de vecindad' efectivo.

**Distribución Gaussiana**
Vecinos cercanos → probabilidad alta. Puntos lejanos → probabilidad ≈ 0. Enfocado localmente.

**Simetrización**
$p_{ij} = (p(j|i) + p(i|j)) / 2N$
Garantiza que $p_{ij} = p_{ji}$.

*Interpretación: $p_{ij}$ es la probabilidad de que el punto i 'elegiría' a j como vecino bajo una Gaussiana centrada en i.*

💡 **Reflexión:** ¿Qué ocurriría si todos los $p_{ij}$ fueran iguales? ¿Qué nos diría eso sobre la estructura de los datos?

## Slide 11

# t-SNE: High-D Similarities

*Similitudes en alta dimensión (Paso 1)*

Para cada par de puntos i, j en ℝⁿ, calculamos la probabilidad condicional:

**Figura:** Diagrama de dos paneles conectado por una flecha. Panel izquierdo "Original Multi-Dimensional Space": puntos dispersos (naranjas, verdes, azules) alrededor de un "point of interest" (rojo, centro), con flechas punteadas indicando "1. Measure distances between point of interest and all other points". Panel derecho "Normal Distribution Used To Calculate Similarity": una curva de campana (distribución normal) sobre la cual se proyectan los mismos puntos según su distancia al punto de interés, con anotaciones "2. Plot the distances on a normal curve" y "3. Calculate similarity scores"; los puntos cercanos al centro (bajo la curva, cerca del pico) obtienen mayor similitud que los alejados en las colas.

## Slide 12

# t-SNE: Low-D Similarities & t-Distribution

*Similitudes en baja dimensión — el truco de la t-Student*

En el espacio 2D usamos distribución t-Student con 1 grado de libertad (Cauchy):

$q_{ij} = (1 + \|y_i - y_j\|^2)^{-1} / \sum_{k \neq l} (1 + \|y_k - y_l\|^2)^{-1}$

**¿Por qué t-Student y no Gaussiana?**
En alta dimensión las distancias se comprimen: todo parece equidistante. La cola pesada de la t-Student permite que puntos moderadamente lejanos en 2D representen puntos muy lejanos en alta dimensión → evita que grupos distintos colisionen en la proyección.

**Gaussiana (cola delgada)**
Cae rápido → puntos lejanos tienen probabilidad casi 0. Aplasta la estructura.

**t-Student (cola pesada)**
Decae más lento → permite 'empujar' grupos separados más lejos en 2D.

💡 **Reflexión:** ¿Por qué importa el número de grados de libertad en la t-Student que usa t-SNE?

## Slide 13

# t-SNE: Low-D Similarities & t-Distribution

*Similitudes en baja dimensión — el truco de la t-Student*

**Gaussiana (cola delgada)**
Cae rápido → puntos lejanos tienen probabilidad casi 0. Aplasta la estructura.

**t-Student (cola pesada)**
Decae más lento → permite 'empujar' grupos separados más lejos en 2D.

**Figura:** Gráfico "Gaussian vs Student-t Distribution", eje x de -4 a 4, eje y "PDF" de 0.00 a 0.40. Curva azul "Gaussian (mean=0, std=1)" con pico ~0.40 en x=0 y caída rápida hacia los extremos. Curva naranja "Student-t (df=1)" con pico más bajo (~0.32) en x=0 pero colas visiblemente más pesadas (más altas que la Gaussiana) en los extremos, ilustrando cómo la t-Student mantiene mayor densidad de probabilidad a distancias grandes.

## Slide 14

# t-SNE: KL Divergence Optimization

*Optimización por Divergencia KL*

t-SNE minimiza la diferencia entre las distribuciones P (alta dimensión) y Q (baja dimensión):

$L = KL(P \| Q) = \sum_i \sum_j p_{ij} \cdot \log(p_{ij} / q_{ij})$

**¿Qué hace el gradiente?**
Mueve cada punto $y_i$ en 2D. Si $p_{ij} > q_{ij}$ (vecinos en alta dimensión pero no en 2D) → los atrae. Si $p_{ij} < q_{ij}$ → los repele.

**Método de optimización**
Descenso por gradiente iterativo, típicamente 1000 iteraciones. Lento para N grande: complejidad $O(N^2)$ en versión original.

⚠ **Propiedad asimétrica de la KL:**
Si $p_{ij}$ es alto (vecinos reales) pero $q_{ij}$ es bajo → penalización muy alta. t-SNE prioriza conservar vecinos reales sobre separar los lejanos.

## Slide 15

# t-SNE: The Perplexity Hyperparameter

*El hiperparámetro más importante: Perplexity*

La perplejidad controla cuántos vecinos efectivos considera cada punto:

$Perplexity = 2^{H(P_i)}$ donde $H(P_i) = -\sum_j p(j|i) \log_2 p(j|i)$

**Perplexity 5–15**
*Pocos vecinos*
Microestructura muy detallada. Grupos pequeños y compactos. Riesgo de fragmentación artificial.

**Perplexity 30–50**
*Vecinos moderados*
Balance entre estructura local y global. Valor recomendado para la mayoría de datasets.

**Perplexity 50+**
*Muchos vecinos*
Captura estructura más global. Grupos más difusos. Puede perder detalles locales.

*Rango típico: 5 a 50 · Default sklearn: 30 · Siempre usar random_state=42 para reproducibilidad*

💡 **Reflexión:** Si tu dataset tiene N=10,000 muestras y Perplexity=5000, ¿qué problema teórico surge?

## Slide 16

# t-SNE: Limitations & Pitfalls

*Limitaciones críticas de t-SNE*

Conocer estas limitaciones es fundamental para el análisis crítico del informe:

❌ **No preserva distancias globales**
La distancia ENTRE clusters en el plot 2D NO tiene significado real. Dos clusters cercanos en la visualización pueden estar muy lejos en el espacio original.

❌ **No determinístico**
Cada ejecución con distinta semilla produce un resultado diferente. Siempre fijar random_state=42.

❌ **No tiene transform()**
No puede proyectar datos nuevos. No hay función transform() — solo fit_transform(). Inutilizable en producción.

❌ **Complejidad O(N²)**
Muy lento con N grande. Para N > 50,000 usar la variante Barnes-Hut (O(N log N)) o considerar UMAP.

💡 **Reflexión:** ¿En qué escenarios de producción sería problemático usar t-SNE? ¿Podría usarse como preprocesamiento para un clasificador?

## Slide 17

03

**UMAP**
**Uniform Manifold Approximation and**
**Projection**

## Slide 18

# UMAP: Core Intuition & Manifolds

*Intuición: Variedades Múltiples (Manifolds)*

"Los datos de alta dimensión no llenan el espacio aleatoriamente — viven sobre una superficie curva de menor dimensión (variedad) incrustada en ℝⁿ."

**Analogía de la hoja de papel:**

**Espacio 3D**
Una hoja de papel enrollada en tubo está en ℝ³. Los puntos viven en la hoja (variedad 2D).

**Distorsión euclidiana**
Puntos cerca en ℝ³ pueden estar lejos sobre la hoja. PCA mide distancias en ℝ³ → error.

**Lo que hace UMAP**
Aprende la geometría de la variedad y la 'desenrolla' en 2D preservando distancias geodésicas.

*Fundamento matemático: topología algebraica y teoría de categorías. Mucho más riguroso que t-SNE.*

💡 **Reflexión:** ¿Qué es una 'variedad' (manifold) en términos intuitivos? Dar un ejemplo de su vida cotidiana.

## Slide 19

# UMAP: Core Intuition & Manifolds

*Intuición: Variedades Múltiples (Manifolds)*

"Los datos de alta dimensión no llenan el espacio aleatoriamente — viven sobre una superficie curva de menor dimensión (variedad) incrustada en ℝⁿ."

**Figura:** Dos gráficos conectados por una flecha. Izquierda "Point cloud in a 3-dimensional space": nube de puntos 3D con 7 clusters de colores distintos (leyenda "Clusters" 1-7: rosado, rojo, morado, verde, gris, naranja, azul) entremezclados en el espacio tridimensional. Derecha "UMAP Dimensionality Reduction": proyección 2D (eje "UMAP Dimension 2", rango aproximado -5 a 15; eje horizontal -4 a 12) donde los mismos 7 clusters aparecen ahora claramente separados en regiones distintas del plano, conservando sus colores/etiquetas originales.

## Slide 20

# UMAP: Neighborhood Graph Construction

*Construcción del grafo de vecindad (Paso 1)*

UMAP construye un grafo pesado donde cada punto se conecta con sus k vecinos más cercanos:

$w(x_i, x_j) = \exp(-(d(x_i,x_j) - \rho_i) / \sigma_i)$

**ρᵢ (rho)**
Distancia al vecino más cercano de i. Normaliza localmente → adapta la métrica a la densidad local.

**σᵢ (sigma)**
Escala de normalización ajustada automáticamente. Equivale al parámetro de ancho de la Gaussiana en t-SNE.

**Diferencia con t-SNE**
UMAP normaliza distancias LOCALMENTE. Zonas densas y dispersas se tratan con la misma importancia.

Resultado: Un grafo ponderado donde aristas de alto peso = puntos muy similares. El grafo captura la topología local de la variedad en el espacio original.

💡 **Reflexión:** ¿Por qué la normalización local (ρᵢ) es importante cuando los datos tienen densidades variables?

## Slide 21

# UMAP: Optimization & Loss Function

*Optimización en baja dimensión (Pasos 2 y 3)*

UMAP optimiza la representación 2D minimizando la entropía cruzada entre ambos grafos:

$L = \Sigma_{ij} [ w^H(i,j) \cdot \log(w^L(i,j)) + (1-w^H(i,j)) \cdot \log(1-w^L(i,j)) ]$

*$w^H$ = peso del grafo en alta dimensión · $w^L$ = peso en baja dimensión (2D o 3D)*

**Inicialización inteligente**
UMAP puede inicializar con PCA en lugar de aleatoriamente → convergencia más rápida y resultado más estable (determinístico).

**Muestreo negativo (SGD)**
Optimiza con Stochastic Gradient Descent + muestreo de pares negativos. Complejidad O(N) por iteración → MUCHO más rápido que t-SNE.

**Ventaja clave sobre t-SNE:** UMAP tiene función transform() → puede proyectar datos nuevos sin reentrenar. Esto lo hace viable en producción.

## Slide 22

# UMAP: n_neighbors Hyperparameter

*Hiperparámetro n_neighbors: estructura local vs global*

n_neighbors controla cuántos vecinos considera cada punto al construir el grafo:

**n_neighbors = 2–5** *[Muy local]*
Grupos muy fragmentados. Puede crear clusters artificiales.

**n_neighbors = 15** *[Balance (default)]*
Captura bien estructura local. Recomendado como punto de partida.

**n_neighbors = 50–200** *[Semi-global]*
Grupos más cohesivos. Mejor para ver estructura jerárquica.

*Comparación análoga: n_neighbors en UMAP ≈ Perplexity en t-SNE (ambos controlan el tamaño del vecindario)*

**Reflexión:** Si aumentas n_neighbors, ¿qué le pasa a la frontera entre clusters? ¿Se hace más o menos nítida?

## Slide 23

# UMAP: min_dist Hyperparameter

*Hiperparámetro min_dist: compacidad de los clusters*

min_dist controla qué tan comprimidos quedan los puntos dentro de cada cluster en 2D:

**min_dist = 0.0–0.1 (compacto)**
Los puntos dentro de cada cluster se agrupan muy juntos en 2D.
- Ideal para ver separación entre clusters.
- Recomendado como punto de partida.
- Mejor con Silhouette Score.

**min_dist = 0.5–1.0 (esparcido)**
Los puntos se distribuyen más uniformemente dentro de cada cluster.
- Mejor para ver distribución continua.
- Más fiel a la densidad real.
- Clusters menos visibles.

**Default: min_dist=0.1 · Para el proyecto de clasificación de los datos: empezar con n_neighbors=15, min_dist=0.1**

**Reflexión:** ¿Cambiar min_dist afecta la separación ENTRE clusters o solo la compacidad DENTRO de ellos?

## Slide 24

# UMAP: Advantages Over t-SNE

*Ventajas de UMAP sobre t-SNE*

**Velocidad**
UMAP es significativamente más rápido. O(N) por iteración con SGD vs O(N²) de t-SNE. Para N=50,000: minutos vs horas.

**Función transform()**
UMAP puede proyectar datos nuevos sin reentrenar. t-SNE no tiene esta capacidad. Esto lo hace viable en pipelines de producción.

**Preserva estructura global**
UMAP preserva mejor la distancia relativa ENTRE clusters (no solo vecindad local). t-SNE hace que las distancias inter-cluster sean meaningless.

**Determinístico**
Con random_state fijo y init='spectral', UMAP produce resultados reproducibles. t-SNE es inherentemente estocástico.

**Más hiperparámetros**
n_neighbors + min_dist ofrecen control más intuitivo que la perplexity de t-SNE.

**Reflexión:** ¿Cuándo usarías t-SNE y cuándo UMAP en un pipeline real? ¿Pueden usarse ambos?

## Slide 25

# UMAP: Limitations & Considerations

*Limitaciones y consideraciones de UMAP*

**Interpretación de distancias**
Las distancias entre clusters son más significativas que en t-SNE pero SIGUEN siendo aproximadas. No son distancias euclidianas reales en el espacio original.

**Sensible a n_neighbors**
Con n_neighbors muy bajo puede crear estructura que no existe en los datos (overfitting topológico). Siempre validar con múltiples valores.

**Librería externa**
UMAP NO está en scikit-learn. Requiere: pip install umap-learn. Importar como: import umap

**Tiempo de instalación**
umap-learn tiene dependencias pesadas (numba, llvmlite). En entornos con GPU puede acelerar significativamente.

**Reflexión:** ¿Cómo verificarías que los clusters encontrados por UMAP son reales y no artefactos del algoritmo?

## Slide 26

**Figura:** Slide separador de sección, fondo azul sólido. Texto: "04" (número grande de sección) y título "Comparación: PCA vs t-SNE vs UMAP".

## Slide 27

# PCA vs t-SNE vs UMAP: Conceptual Comparison

*Comparación conceptual de los tres métodos*

**Figura:** Tabla comparativa de 8 filas × 3 columnas (PCA, t-SNE, UMAP) sobre el aspecto indicado en la primera columna.

| Aspecto | PCA | t-SNE | UMAP |
|---|---|---|---|
| Tipo | Lineal | No lineal | No lineal |
| Preserva | Varianza global | Vecindad local | Vecindad local + global parcial |
| Velocidad | Muy rápido | Lento O(N²) | Moderado O(N) |
| Determinístico | Sí | No | Con random_state |
| transform() | Sí | No | Sí |
| Distancia global | Significativa | Sin significado | Parcial |
| Metrica reportable | % varianza | Tiempo + visual | Tiempo + visual |
| Instalación | sklearn | sklearn | pip umap-learn |

## Slide 28

**Figura:** Slide separador de sección, fondo azul sólido. Texto: "05" (número grande de sección) y título "Implementación en Python: PCA, t-SNE y UMAP".

## Slide 29

# Synthetic Dataset: Why PCA Falls Short

*Dataset sintético para demostrar la necesidad de t-SNE y UMAP*

Usaremos un dataset sintético intencionalmente no lineal para mostrar el límite de PCA:

**Figura:** Bloque de código Python con fondo azul oscuro, texto sintaxis-resaltado.

```
import numpy as np
from sklearn.datasets import make_swiss_roll, make_moons
from sklearn.preprocessing import StandardScaler

# Caso 1: Swiss Roll — variedad 2D enrollada en R^3
# PCA lo aplasta; t-SNE y UMAP lo "desenrollan"
X_roll, y_roll = make_swiss_roll(n_samples=1500, noise=0.1, random_state=42)
# X_roll tiene 3 dimensiones con estructura de espiral no lineal

# Caso 2: Moons en alta dimension — estructura no lineal incrustada en Rd
# Generamos moons en 2D y los proyectamos a 30 dimensiones con ruido
X_2d, y_moons = make_moons(n_samples=1000, noise=0.05, random_state=42)
noise_dims = np.random.RandomState(42).randn(1000, 28) * 0.3
X_moons     = np.hstack([X_2d, noise_dims])   # shape (1000, 30)

# Trabajamos con el Swiss Roll para el ejemplo principal
X, y = X_roll, y_roll.astype(int) % 4   # 4 clases artificiales
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(f"Dataset: {X.shape}  |  Clases: {np.unique(y)}")
```

**Swiss Roll: 3 dimensiones, pero la estructura real es 2D (una hoja enrollada). PCA la aplasta al proyectar.**

## Slide 30

# Python: PCA on Swiss Roll — The Limitation

*PCA aplicado al Swiss Roll — observando su limitación*

PCA proyecta linealmente: aplasta la estructura curva y mezcla clases que deberían separarse.

**Figura:** Bloque de código Python con fondo azul oscuro.

```
import time
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# PCA completo — scree plot
pca_full = PCA().fit(X_scaled)
varianza_acumulada = pca_full.explained_variance_ratio_.cumsum()
k_95 = np.argmax(varianza_acumulada >= 0.95) + 1

# PCA a 2D — medimos tiempo
t0 = time.time()
pca_2d = PCA(n_components=2)
Z_pca  = pca_2d.fit_transform(X_scaled)
t_pca  = time.time() - t0
var_ret = pca_2d.explained_variance_ratio_.sum() * 100
print(f"Tiempo PCA: {t_pca:.4f}s | Varianza 2D: {var_ret:.1f}%")

# Visualización lado a lado: 3D original vs PCA 2D
fig = plt.figure(figsize=(14, 5))
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(X[:,0], X[:,1], X[:,2], c=y, cmap='tab10', s=8)
ax1.set_title('Swiss Roll original (3D)', fontsize=16)

ax2 = fig.add_subplot(122)
sc = ax2.scatter(Z_pca[:,0], Z_pca[:,1], c=y, cmap='tab10', s=8)
plt.colorbar(sc, ax=ax2, label='Clase')
ax2.set_title(f'PCA 2D — Varianza: {var_ret:.1f}%', fontsize=16)
ax2.set_xlabel('PC1', fontsize=14); ax2.set_ylabel('PC2', fontsize=14)
plt.tight_layout()
plt.show()   # Observar: las clases se MEZCLAN en la proyeccion PCA
```

**Resultado esperado: PCA mezcla los extremos del rollo. Las clases NO se separan → PCA falla aquí.**

## Slide 31

# Python: t-SNE on Swiss Roll — Unrolling the Structure

*t-SNE aplicado al Swiss Roll — desenrollando la variedad*

t-SNE preserva vecindad local y revela la estructura real que PCA ocultaba:

**Figura:** Bloque de código Python con fondo azul oscuro.

```
from sklearn.manifold import TSNE

# t-SNE sobre los datos estandarizados
t0 = time.time()
tsne = TSNE(
    n_components=2,
    perplexity=30,    # vecindario efectivo ~30 puntos
    n_iter=1000,
    random_state=42,
    init='pca'        # inicializacion con PCA = mas estable y rapido
)
Z_tsne  = tsne.fit_transform(X_scaled)
t_tsne  = time.time() - t0
print(f"Tiempo t-SNE: {t_tsne:.2f} s")
# IMPORTANTE: t-SNE NO tiene explained_variance_ratio_

# Comparacion visual PCA vs t-SNE
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
for ax, Z, title, c_label in [
    (axes[0], Z_pca,  f'PCA 2D (varianza={var_ret:.0f}%)', 'PC'),
    (axes[1], Z_tsne, f't-SNE 2D (t={t_tsne:.1f}s)', 't-SNE'),
]:
    sc = ax.scatter(Z[:,0], Z[:,1], c=y, cmap='tab10', s=10, alpha=0.8)
    plt.colorbar(sc, ax=ax, label='Clase')
    ax.set_title(title, fontsize=16)
    ax.set_xlabel(f'{c_label} 1', fontsize=14)
    ax.set_ylabel(f'{c_label} 2', fontsize=14)
plt.tight_layout()
plt.show()   # t-SNE separa las clases; PCA las mezcla
```

**Resultado: t-SNE revela la estructura de espiral. Las clases aparecen claramente separadas.**

## Slide 32

# Python: UMAP on Swiss Roll — Faster & Richer

*UMAP aplicado al Swiss Roll — más rápido y con transform()*

UMAP logra resultados similares a t-SNE pero más rápido y con soporte para nuevos datos:

**Figura:** Bloque de código Python con fondo azul oscuro.

```
# pip install umap-learn
import umap

t0 = time.time()
reducer = umap.UMAP(
    n_components=2,
    n_neighbors=15,   # cuantos vecinos considera cada punto
    min_dist=0.1,     # compacidad de los clusters en 2D
    random_state=42
)
Z_umap = reducer.fit_transform(X_scaled)
t_umap = time.time() - t0
print(f"Tiempo UMAP: {t_umap:.2f} s  (comparar con t-SNE: {t_tsne:.2f} s)")

# UMAP puede proyectar datos NUEVOS (t-SNE no puede)
X_nuevo = scaler.transform(np.array([[0.5, 0.3, -0.2]]))
Z_nuevo = reducer.transform(X_nuevo)   # <- esto t-SNE no tiene
print(f"Punto nuevo proyectado: {Z_nuevo}")

# Comparacion final: 3 metodos
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
for ax, Z, title in [
    (axes[0], Z_pca,  f'PCA (var={var_ret:.0f}%, t={t_pca:.3f}s)'),
    (axes[1], Z_tsne, f't-SNE (t={t_tsne:.1f}s)'),
    (axes[2], Z_umap, f'UMAP (t={t_umap:.1f}s)'),
]:
    sc = ax.scatter(Z[:,0], Z[:,1], c=y, cmap='tab10', s=10, alpha=0.8)
    plt.colorbar(sc, ax=ax, label='Clase')
    ax.set_title(title, fontsize=15)
    ax.set_xlabel('Dim 1', fontsize=14); ax.set_ylabel('Dim 2', fontsize=14)
plt.suptitle('Swiss Roll — PCA vs t-SNE vs UMAP', fontsize=17, fontweight='bold')
plt.tight_layout(); plt.show()
```

**No confundir paquetes: pip install umap-learn · import umap (no 'pip install umap')**

## Slide 33

# Python: High-D Moons — Scaling to More Dimensions

*Ejemplo con datos de mayor dimensión — Moons en $R^{30}$*

El mismo patrón aplica cuando los datos viven en decenas o cientos de dimensiones:

**Figura:** Bloque de código Python con fondo azul oscuro.

```
# Moons en R^30: estructura 2D no lineal + 28 dims de ruido
from sklearn.datasets import make_moons

X_2d, y_m = make_moons(n_samples=1200, noise=0.05, random_state=42)
ruido      = np.random.RandomState(42).randn(1200, 28) * 0.3
X_hd       = np.hstack([X_2d, ruido])          # (1200, 30)
X_hd_sc    = StandardScaler().fit_transform(X_hd)

# PCA a 2D: las 28 dims de ruido diluyen la estructura real
t0 = time.time()
Z_pca_m = PCA(n_components=2).fit_transform(X_hd_sc); t_p = time.time()-t0
var_m    = PCA(n_components=2).fit(X_hd_sc).explained_variance_ratio_.sum()*100

# t-SNE: recupera la estructura de medialuna
t0 = time.time()
Z_tsne_m = TSNE(n_components=2, perplexity=30,
                random_state=42, init='pca').fit_transform(X_hd_sc)
t_t = time.time()-t0

# UMAP: tambien recupera + permite transform()
t0 = time.time()
rdcr     = umap.UMAP(n_neighbors=15, min_dist=0.1, random_state=42)
Z_umap_m = rdcr.fit_transform(X_hd_sc); t_u = time.time()-t0

fig, axes = plt.subplots(1, 3, figsize=(17, 5))
for ax,(Z,ti) in zip(axes, [(Z_pca_m,f'PCA (var={var_m:.0f}%)'),
                               (Z_tsne_m,f't-SNE ({t_t:.1f}s)'),
                               (Z_umap_m,f'UMAP ({t_u:.1f}s)')]):
    sc=ax.scatter(Z[:,0],Z[:,1],c=y_m,cmap='bwr',s=10,alpha=0.8)
    plt.colorbar(sc,ax=ax); ax.set_title(ti,fontsize=15)
    ax.set_xlabel('Dim 1',fontsize=14); ax.set_ylabel('Dim 2',fontsize=14)
plt.tight_layout(); plt.show()
```

**PCA mezcla las medias lunas. t-SNE y UMAP las separan perfectamente a pesar del ruido en 28 dims.**

## Slide 34

# Python: Timing Table & Scree Plot

*Tabla comparativa de tiempos y Scree Plot de PCA*

**Figura:** Bloque de código Python con fondo azul oscuro.

```
import pandas as pd

# ── Tabla comparativa de los tres metodos ──────────────────────
resultados = {
    'Metodo':      ['PCA 2D',  't-SNE 2D', 'UMAP 2D'],
    'Tiempo (s)': [round(t_pca,4), round(t_tsne,2), round(t_umap,2)],
    'Var. ret.':   [f'{var_ret:.1f}%', 'N/A', 'N/A'],
    'Estructura': ['Lineal global', 'Local no lineal', 'Local + global parcial'],
    'transform()': ['Si', 'No', 'Si'],
}
df = pd.DataFrame(resultados)
print(df.to_string(index=False))

# ── Scree plot — cuantos componentes necesita PCA ──────────────
pca_all = PCA().fit(X_scaled)
var_cum = pca_all.explained_variance_ratio_.cumsum()
k95     = np.argmax(var_cum >= 0.95) + 1

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].plot(range(1, len(var_cum)+1), var_cum, 'o-',
             color='#003087', markersize=5, linewidth=2)
axes[0].axhline(0.95, color='red', linestyle='--', label='95%')
axes[0].axvline(k95, color='orange', linestyle='--', label=f'k={k95}')
axes[0].set_xlabel('Numero de componentes', fontsize=14)
axes[0].set_ylabel('Varianza acumulada', fontsize=14)
axes[0].set_title('Scree Plot', fontsize=16); axes[0].legend(fontsize=13)

axes[1].bar(['PCA', 't-SNE', 'UMAP'],
            [t_pca, t_tsne, t_umap],
            color=['#003087','#0055B3','#00A3E0'])
axes[1].set_ylabel('Tiempo (s)', fontsize=14)
axes[1].set_title('Comparacion de Tiempos', fontsize=16)
axes[1].tick_params(labelsize=13)
plt.tight_layout(); plt.show()
```

**Este bloque de código genera la tabla + gráficas que sustentan el análisis comparativo formal de cualquier reporte.**

## Slide 35

**Figura:** Slide separador de sección, fondo azul sólido. Texto: "06" (número grande de sección) y título "Resumen".

## Slide 36

# PCA: Key Takeaways

*PCA — Puntos clave a recordar*

**Checklist PCA — Aspectos clave:**

- **Estandarizar** — StandardScaler antes de PCA. Sin esto el modelo es incorrecto.
- **Scree plot** — Graficar varianza acumulada. Marcar el umbral del 95%. Reportar k_95.
- **Scatter 2D** — Plot con colores por clase. Fontsize ≥ 14 en todos los ejes.
- **Reportar métricas** — % varianza con 2 componentes + tiempo de ejecución medido.
- **Analizar resultado** — ¿Se separan bien las clases? Justificar si no → limitación lineal de PCA.

## Slide 37

# t-SNE: Key Takeaways

*t-SNE — Puntos clave a recordar*

**Checklist t-SNE — Aspectos clave:**

- **Usar X_scaled** — Siempre aplicar sobre datos estandarizados. Puede usarse sobre PCA-50 para acelerar.
- **Fijar random_state** — random_state=42 para reproducibilidad. Sin esto cada run da resultado diferente.
- **Probar perplexity** — Ejecutar con perplexity=10, 30, 50. Reportar el que mejor separación visual da.
- **Medir tiempo** — time.time() antes y después de fit_transform(). Comparar con PCA y UMAP.
- **NO reportar varianza** — t-SNE no tiene explained_variance_ratio_. No es una métrica aplicable.

## Slide 38

# UMAP: Key Takeaways

*UMAP — Puntos clave a recordar*

**Checklist UMAP — Aspectos clave:**

- **Instalar correctamente** — pip install umap-learn (NO es sklearn). Verificar: import umap
- **Experimentar hiperparámetros** — n_neighbors: {5, 15, 50} + min_dist: {0.0, 0.1, 0.5}. Reportar el mejor.
- **Comparar con t-SNE** — ¿Qué método separa mejor las clases visualmente? ¿Cuál es más rápido?
- **Demostrar transform()** — Mostrar que reducer.transform(X_new) funciona (diferencia clave con t-SNE).
- **Justificar elección** — Para clustering (Sección 3.2): ¿usarás PCA, t-SNE o UMAP como reducción previa?

## Slide 39

# Recommended Workflow Pipeline

*Flujo de trabajo recomendado*

**Figura:** Diagrama de flujo de 8 pasos numerados en dos filas de 4 tarjetas conectadas.

1. Cargar datos — $X \in \mathbb{R}^{(N \times d)}, y \in \{clases\}$
2. StandardScaler — fit_transform(X)
3. PCA completo — Scree plot + k_95
4. PCA 2D — Scatter + tiempo
5. t-SNE 2D — Perplexity={10,30,50}
6. UMAP 2D — n_neighbors={5,15,50}
7. Tabla comparativa — tiempos + métricas
8. Análisis crítico — ¿Cuál método es mejor?

## Slide 40

# Further Reading & Resources

*Recursos y referencias*

**Artículo original t-SNE**
van der Maaten & Hinton (2008). 'Visualizing Data using t-SNE'. JMLR. — https://jmlr.org/papers/v9/vandermaaten08a.html

**Artículo original UMAP**
McInnes et al. (2018). 'UMAP: Uniform Manifold Approximation and Projection'. arXiv:1802.03426. — https://arxiv.org/abs/1802.03426

**Documentación sklearn PCA**
sklearn.decomposition.PCA — scikit-learn — https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

**Documentación umap-learn**
UMAP documentation — McInnes et al. — https://umap-learn.readthedocs.io

**Tutorial interactivo t-SNE**
How to Use t-SNE Effectively — Wattenberg et al. (Distill.pub) — https://distill.pub/2016/misread-tsne/

## Slide 41

**Resumen Final**

- PCA → rápido, lineal, reporta varianza. Bueno como baseline.
- t-SNE → no lineal, lento, mejor visualización. Solo exploración.
- UMAP → no lineal, rápido, tiene transform(). Mejor para pipelines.
- Los tres métodos son complementarios: comparar tiempos + análisis crítico visual.
- Fontsize ≥ 14 en TODAS las figuras (penalización -3 pts).
