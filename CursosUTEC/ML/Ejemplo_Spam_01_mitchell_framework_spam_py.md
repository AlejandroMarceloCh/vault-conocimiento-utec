---
curso: ML
titulo: Ejemplo_Spam_01/mitchell_framework_spam
slides: 0
fuente: Ejemplo_Spam_01/mitchell_framework_spam.py
---

# Detección de spam bajo el framework de Mitchell

Este código implementa un clasificador binario de spam usando **regresión logística** de scikit-learn, y su valor didáctico está en que organiza todo el flujo alrededor de la definición formal de aprendizaje de Tom Mitchell: un programa aprende de la experiencia E, respecto a una tarea T, medida por un rendimiento P. Aquí T es clasificar un email como spam (1) o no-spam (0), E son emails etiquetados y P es el accuracy y el F1-score.

A alto nivel, el script recorre cinco pasos de un pipeline supervisado. Genera datos sintéticos con `make_classification` (1000 emails, 10 features, desbalance 70/30 que imita la realidad). Divide en train/test con `train_test_split` usando `stratify=y` para conservar la proporción de clases, insistiendo en la regla de no dejar que el modelo vea el test. Aplica `StandardScaler` con la disciplina correcta —`fit` solo sobre train, `transform` sobre ambos— para no filtrar información. Entrena la `LogisticRegression`, cuyos coeficientes θ se interpretan como el peso de cada feature en el riesgo de spam. Finalmente evalúa con accuracy, F1 y matriz de confusión, señalando por qué el F1 importa más bajo desbalance de clases.

El concepto central que ejercita es el **aprendizaje supervisado end-to-end** y la higiene metodológica: data leakage, escalado, estratificación y métricas apropiadas. En un proyecto real es la plantilla base de cualquier clasificación, y conecta con evaluación de modelos, preprocesamiento y regresión logística del resto del curso.

```py
"""
=========================================================================
  FRAMEWORK DE MITCHELL — EJEMPLOS COMPLETO DETECCION DE SPAM EN PYTHON
  Curso: Machine Learning — UCSP
  Prof. D.Sc. Manuel Eduardo Loaiza Fernández
=========================================================================

RECORDATORIO: El Framework de Mitchell define "aprender" como:

  "Un programa aprende de la EXPERIENCIA E
   con respecto a una clase de TAREAS T
   y medida de RENDIMIENTO P,
   si su rendimiento en T, medido por P,
   mejora con la experiencia E."

Cada ejemplo en este archivo sigue la misma estructura:
  1. Explicación de T, E y P para ese problema
  2. Código Python comentado paso a paso
  3. Evaluación del rendimiento P
  4. Interpretación del resultado

PREREQUISITOS:
  pip install scikit-learn numpy matplotlib pandas
"""

# ── Imports globales ──────────────────────────────────────────────
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# ── Separador visual ──────────────────────────────────────────────
def separador(titulo):
    ancho = 60
    print("\n" + "=" * ancho)
    print(f"  {titulo}")
    print("=" * ancho)

def subseccion(texto):
    print(f"\n  {'─' * 50}")
    print(f"  {texto}")
    print(f"  {'─' * 50}")


# ╔══════════════════════════════════════════════════════════════╗
# ║  EJEMPLO 1 — DETECCIÓN DE SPAM (Clasificación)               ║
# ╚══════════════════════════════════════════════════════════════╝

def ejemplo_1_spam():
    separador("EJEMPLO 1 — Detección de Spam")

    print("""
  FRAMEWORK DE MITCHELL:
  ┌─────────────────────────────────────────────────────┐
  │  T (Tarea):       Clasificar un email como          │
  │                   spam (1) o no-spam (0)            │
  │                                                     │
  │  E (Experiencia): Emails previamente etiquetados    │
  │                   por humanos como spam/no-spam     │
  │                                                     │
  │  P (Rendimiento): Porcentaje de emails clasificados │
  │                   correctamente (Accuracy y F1)     │
  └─────────────────────────────────────────────────────┘
  Paradigma: SUPERVISADO — cada email tiene etiqueta y.
    """)

    # ── Paso 1: Generar datos sintéticos de emails ────────────────
    subseccion("Paso 1: Crear el dataset de entrenamiento (Experiencia E)")

    # En un proyecto real cargaríamos emails reales.
    # Aquí simulamos características numéricas de emails:
    # - frecuencia de palabras clave ("oferta", "gratis", "urgente")
    # - número de signos de exclamación
    # - proporción de mayúsculas
    # - longitud del asunto

    np.random.seed(42)

    # make_classification crea un dataset de clasificación binaria
    # n_samples     = cuántos emails simulamos
    # n_features    = cuántas características por email
    # n_informative = cuántas características realmente distinguen spam
    # weights       = proporción de clases [no-spam, spam] — desbalanceado!

    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        weights=[0.7, 0.3],   # 70% no-spam, 30% spam — como en realidad
        random_state=42
    )

    # Nombres de las características (features)
    nombres_features = [
        "frec_oferta", "frec_gratis", "frec_urgente",
        "num_exclamaciones", "prop_mayusculas",
        "longitud_asunto", "num_links", "frec_dinero",
        "frec_click", "hora_envio"
    ]

    print(f"  Dataset creado:")
    print(f"    Total emails:  {X.shape[0]}")
    print(f"    Features:      {X.shape[1]}")
    print(f"    No-spam (0):   {(y==0).sum()} ({(y==0).mean()*100:.0f}%)")
    print(f"    Spam    (1):   {(y==1).sum()} ({(y==1).mean()*100:.0f}%)")

    # ── Paso 2: Dividir en entrenamiento y prueba ─────────────────
    subseccion("Paso 2: Dividir datos — train/test split")

    # train_test_split divide el dataset en dos partes:
    #   - X_train, y_train: datos que el modelo VE para aprender (E)
    #   - X_test,  y_test:  datos NUEVOS para evaluar rendimiento (P)
    #
    # REGLA DE ORO: el modelo NUNCA debe ver los datos de test durante
    # el entrenamiento. Si los viera, la evaluación sería tramposa.

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.25,       # 25% para evaluar
        random_state=42,
        stratify=y            # mantiene la proporción spam/no-spam
    )

    print(f"  Entrenamiento (E): {X_train.shape[0]} emails")
    print(f"  Prueba (P):        {X_test.shape[0]} emails")

    # ── Paso 3: Escalar los datos ─────────────────────────────────
    subseccion("Paso 3: Preprocesamiento — Feature Scaling")

    # Los algoritmos basados en distancias o gradientes son sensibles
    # a la escala de las features. StandardScaler ajusta cada feature
    # para tener media=0 y desviación estándar=1.
    #
    # IMPORTANTE: fit() solo sobre train, transform() sobre ambos.
    # Si hacemos fit() sobre test, estamos "filtrando" información.

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)  # aprende escala del train
    X_test_scaled  = scaler.transform(X_test)        # aplica esa misma escala

    # ── Paso 4: Entrenar el modelo ────────────────────────────────
    subseccion("Paso 4: Entrenamiento — El programa aprende de E")

    # LogisticRegression es un clasificador lineal.
    # A pesar del nombre, es un clasificador, no un regresor.
    # Aprende los pesos θ que mejor separan spam de no-spam.

    modelo = LogisticRegression(
        C=1.0,             # inverso de regularización (C grande = menos regularización)
        max_iter=1000,     # máximo de iteraciones del optimizador
        random_state=42
    )

    # fit() es donde ocurre el aprendizaje: el modelo ajusta sus parámetros
    # internos usando los emails etiquetados (la Experiencia E)
    modelo.fit(X_train_scaled, y_train)

    print("  Modelo entrenado correctamente.")
    print(f"  Parámetros internos aprendidos (θ):")
    for i, (nombre, coef) in enumerate(zip(nombres_features, modelo.coef_[0])):
        barra = "█" * int(abs(coef) * 5)
        signo = "+" if coef > 0 else "-"
        print(f"    {nombre:20s}: {signo}{abs(coef):.3f}  {barra}")

    # ── Paso 5: Evaluar el rendimiento P ─────────────────────────
    subseccion("Paso 5: Evaluación del Rendimiento P")

    # predict() aplica el modelo aprendido a datos NUEVOS (test)
    y_pred = modelo.predict(X_test_scaled)

    # Accuracy: fracción de emails clasificados correctamente
    acc = accuracy_score(y_test, y_pred)

    # F1-Score: equilibrio entre precision y recall
    # Más útil que accuracy cuando hay desbalance de clases
    f1 = f1_score(y_test, y_pred)

    print(f"\n  RENDIMIENTO P en datos nuevos (test):")
    print(f"    Accuracy:  {acc:.3f}  ({acc*100:.1f}% de emails correctos)")
    print(f"    F1-Score:  {f1:.3f}  (equilibrio precision/recall)")

    # Matriz de confusión: muestra los tipos de errores
    cm = confusion_matrix(y_test, y_pred)
    print(f"\n  Matriz de Confusión:")
    print(f"                  Predicho")
    print(f"                No-spam  Spam")
    print(f"  Real No-spam:  {cm[0,0]:4d}    {cm[0,1]:4d}   ← falsos positivos")
    print(f"  Real Spam:     {cm[1,0]:4d}    {cm[1,1]:4d}   ← falsos negativos")

    # ── Visualización ─────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    fig.suptitle("Ejemplo 1 — Detección de Spam\nFramework de Mitchell: T=Clasificar email | E=Emails etiquetados | P=Accuracy/F1",
                 fontsize=11, fontweight='bold')

    # Panel izquierdo: importancia de features
    ax = axes[0]
    coefs = modelo.coef_[0]
    colores = ['#D85A30' if c > 0 else '#378ADD' for c in coefs]
    bars = ax.barh(nombres_features, np.abs(coefs), color=colores, alpha=0.8)
    ax.set_xlabel('Peso absoluto |θ|')
    ax.set_title('Pesos aprendidos por el modelo\n(rojo=aumenta riesgo spam, azul=reduce riesgo)')
    ax.axvline(0, color='black', linewidth=0.5)

    # Panel derecho: matriz de confusión
    ax = axes[1]
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No-spam', 'Spam'])
    disp.plot(ax=ax, colorbar=False, cmap='Blues')
    ax.set_title(f'Matriz de Confusión\nAccuracy={acc:.2f} | F1={f1:.2f}')

    plt.tight_layout()
    plt.savefig('data/ejemplo1_spam_final.png', dpi=130, bbox_inches='tight')
    plt.close()
    print("\n  Gráfico guardado: ejemplo1_spam.png")

    print(f"""
  CONCLUSIÓN MITCHELL:
    El programa (LogisticRegression) aprendió de la EXPERIENCIA E
    ({X_train.shape[0]} emails etiquetados) para ejecutar la TAREA T
    (clasificar emails nuevos) con RENDIMIENTO P de {acc*100:.1f}% accuracy.
    """)


# ╔══════════════════════════════════════════════════════════════╗
# ║  PROGRAMA PRINCIPAL                                          ║
# ╚══════════════════════════════════════════════════════════════╝

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════╗
║    FRAMEWORK DE MITCHELL — EJEMPLOS EN PYTHON                ║
║    Machine Learning — UCSP 2026                              ║
╚══════════════════════════════════════════════════════════════╝

  Ejecutando todos los ejemplos. Cada uno genera un gráfico
  en la carpeta de salida. Tiempo estimado: 1-2 minutos.
    """)

    ejemplo_1_spam()
   
    print("""
╔══════════════════════════════════════════════════════════════╗
║  COMPLETADO — Gráficos generados:                            ║
║    ejemplo1_spam.png                                         ║
╚══════════════════════════════════════════════════════════════╝
    """)
```
