---
curso: ML
titulo: PCA_tSNE_UMAP_Ejercicio
slides: 0
fuente: PCA_tSNE_UMAP_Ejercicio.py
---

# PCA vs t-SNE vs UMAP: reducción de dimensionalidad comparada

Este script es un ejercicio guiado (con bloques `TODO` por completar) que enfrenta las tres técnicas más usadas de reducción de dimensionalidad sobre un mismo conjunto: `toro_10d_200.csv`, 200 puntos descritos por diez features (`x1`…`x10`) y una columna `clase`. El flujo es canónico: carga los datos con pandas, separa la matriz de features `X` de las etiquetas `y`, y estandariza con `StandardScaler`. El comentario lo subraya como paso obligatorio: PCA, t-SNE y UMAP son sensibles a la escala, y sin normalizar, las variables de mayor rango dominarían la geometría resultante.

El corazón conceptual es proyectar un espacio de 10 dimensiones a 2D para poder visualizarlo, y contrastar tres filosofías distintas. PCA es lineal y busca las direcciones de máxima varianza (por eso el ejercicio pide reportar `var_ret`, la varianza retenida). t-SNE y UMAP son no lineales y preservan estructura local de vecindad, controlada por hiperparámetros clave: `perplexity=30` en t-SNE, `n_neighbors=15` y `min_dist=0.1` en UMAP. La visualización final los pone lado a lado, coloreando por clase, para que el alumno vea cómo cada método separa (o no) los grupos del "toro" 10D.

En un proyecto real esto es EDA y diagnóstico: explorar clusters, detectar separabilidad antes de clasificar y comunicar datos de alta dimensión. Conecta con estandarización, clustering y con los modelos supervisados que vendrían después.

```py
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap
import warnings
import time
import matplotlib.pyplot as plt

# ── 1. Cargar datos desde CSV ──────────────────────────────────────
df = pd.read_csv('toro_10d_200.csv')
print(f"Shape: {df.shape}")
print(df.head())

# Separar features y etiquetas
X = df[['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']].values
y = df['clase'].values

# Estandarizar (IMPORTANTE antes de PCA, t-SNE y UMAP)
X_sc = StandardScaler().fit_transform(X)

# ── 2. PCA a 2D ───────────────────────────────────────────────────
# TODO: aplicar PCA con n_components=2
# Z_pca = ...
# var_ret = ...  # varianza retenida en %

# ── 3. t-SNE a 2D ─────────────────────────────────────────────────
# TODO: aplicar t-SNE con perplexity=30, max_iter=1000, init='pca'
# Z_tsne = ...

# ── 4. UMAP a 2D ──────────────────────────────────────────────────
# TODO: aplicar UMAP con n_neighbors=15, min_dist=0.1
# Z_umap = ...

# ── 5. Visualización: 3 métodos lado a lado ───────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 5),
                         num="Toro 10D — PCA vs t-SNE vs UMAP")
for ax, (Z, titulo) in zip(axes, [
    (Z_pca,  f'PCA 2D  (var={var_ret:.0f}%)'),
    (Z_tsne, f't-SNE 2D'),
    (Z_umap, f'UMAP 2D'),
]):
    sc = ax.scatter(Z[:,0], Z[:,1], c=y, cmap='tab10', s=20, alpha=0.85)
    plt.colorbar(sc, ax=ax, label='Clase')
    ax.set_title(titulo, fontsize=14)
    ax.set_xlabel('Dim 1', fontsize=12)
    ax.set_ylabel('Dim 2', fontsize=12)

plt.suptitle('Toro 10D — reducción de dimensionalidad',
             fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()
```
