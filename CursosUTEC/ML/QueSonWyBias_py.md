---
curso: ML
titulo: QueSonWyBias
slides: 0
fuente: QueSonWyBias.py
---

# Parte 1 — ¿Qué son w (slope) y b (bias)?

Este código es una animación interactiva de regresión lineal simple construida con `matplotlib` y sliders, pensada para las semanas 2 y 3 del curso. No entrena un modelo automáticamente: entrega el control de los parámetros al estudiante para que entienda, de forma manual, qué significa cada uno. Sobre un conjunto fijo de catorce puntos `(x, y)` casi perfectamente lineales, dibuja la hipótesis `h(x) = x·w + b` y dos deslizadores, uno para `w` y otro para `b`. Al mover `w` cambia la inclinación de la recta; al mover `b` la recta sube o baja completa. Un panel lateral recalcula en vivo la ecuación, describe si la recta sube, baja o queda horizontal, marca el valor de `y` cuando `x=0` y muestra el error cuadrático medio `L(w,b)` a través de la función `mse_loss`.

El concepto que ejercita es el corazón de la regresión lineal: `w` como pendiente (cuánto cambia la salida por cada unidad de entrada) y `b` como sesgo o intercepto (el valor de partida). También deja preparadas las piezas del aprendizaje que vendrá después: `gradiente_w`, `gradiente_b` y `w_optimo`, es decir, el descenso de gradiente y la solución analítica por mínimos cuadrados.

En un proyecto real de datos, esta es la base de cualquier modelo predictivo lineal y del ajuste por MSE. Conecta directamente con las funciones de pérdida, la optimización por gradiente y, más adelante, con la regresión múltiple y regularizada.

```py
"""
=============================================================
CS3061 Machine Learning — UTEC
Animaciones interactivas de Regresión Lineal en Python
=============================================================
Autor:  Prof. D.Sc. Manuel Eduardo Loaiza Fernández
Curso:  Machine Learning — Semanas 2 y 3

Contenido:
  PARTE 1 — ¿Qué son w (slope) y b (bias)?

Requisitos:
  pip install numpy matplotlib ipywidgets

Para ejecutar en Jupyter:
  %matplotlib widget        # o %matplotlib inline (sin interactividad)
  Luego ejecutar cada celda correspondiente.

Para ejecutar en script .py normal:
  python animaciones_regresion.py
  (se abrirán ventanas secuencialmente — cerrar cada una para ver la siguiente)
=============================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.lines import Line2D
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────────────────────
# DATOS COMPARTIDOS
# ─────────────────────────────────────────────────────────────
np.random.seed(42)
X_DATA = np.array([0.5,1.2,2.1,2.8,3.5,4.2,5.0,5.7,6.3,7.1,7.8,8.5,9.0,9.6])
Y_DATA = np.array([2.1,3.8,4.5,6.2,7.1,9.0,10.2,11.8,13.1,14.9,16.0,18.2,19.5,20.8])
N = len(X_DATA)

STYLE = {
    'data_color':    '#2563eb',
    'line_color':    '#e05000',
    'opt_color':     '#1a7a1a',
    'grad_color':    '#9900cc',
    'bg':            '#fafafa',
    'title_size':    13,
    'label_size':    11,
    'formula_size':  11,
}

# ─────────────────────────────────────────────────────────────
# UTILIDADES
# ─────────────────────────────────────────────────────────────
def hipotesis(x, w, b):
    return x * w + b

def mse_loss(x, y, w, b):
    return np.mean((y - hipotesis(x, w, b))**2) / 2

def gradiente_w(x, y, w, b):
    return np.mean((hipotesis(x, w, b) - y) * x)

def gradiente_b(x, y, w, b):
    return np.mean(hipotesis(x, w, b) - y)

def w_optimo():
    """Solución analítica mínimos cuadrados (b fijo en 0.5)."""
    b = 0.5
    return np.sum(X_DATA * (Y_DATA - b)) / np.sum(X_DATA**2)


# =============================================================
# PARTE 1 — ¿QUÉ SON w (slope) y b (bias)?
# =============================================================
def parte1_slope_bias():
    """
    Gráfico interactivo con sliders para w y b.
    Muestra cómo la recta h(x) = xw + b cambia al mover los parámetros.
    """
    fig, axes = plt.subplots(1, 2, figsize=(13, 6))
    fig.patch.set_facecolor(STYLE['bg'])
    fig.suptitle('Parte 1 — ¿Qué son w (slope) y b (bias)?',
                 fontsize=STYLE['title_size'], fontweight='bold', y=0.98)

    ax_main = axes[0]
    ax_info  = axes[1]

    # --- Panel izquierdo: la recta ---
    ax_main.set_facecolor('white')
    ax_main.set_xlim(0, 10)
    ax_main.set_ylim(-5, 25)
    ax_main.set_xlabel('x  (variable de entrada)', fontsize=STYLE['label_size'])
    ax_main.set_ylabel('y  (variable de salida)',  fontsize=STYLE['label_size'])
    ax_main.set_title('h(x) = x·w + b', fontsize=12)
    ax_main.grid(True, alpha=0.25)

    # Puntos de datos
    ax_main.scatter(X_DATA, Y_DATA, color=STYLE['data_color'],
                    s=60, zorder=5, label='Datos reales', alpha=0.8)

    x_line = np.linspace(0, 10, 300)
    w0, b0 = 1.5, 1.0
    line_h,  = ax_main.plot(x_line, hipotesis(x_line, w0, b0),
                             color=STYLE['line_color'], lw=2.5,
                             label=f'h(x) = {w0}·x + {b0}')

    # Línea de referencia en y-axis para b
    vline_b = ax_main.axhline(b0, color='#888', lw=1, linestyle='--', alpha=0.5)
    dot_b,   = ax_main.plot([0], [b0], 'o', color='#c05000', ms=9, zorder=6)

    # Anotación del intercepto
    ann_b = ax_main.annotate(
        f'b = {b0:.1f}\n(intercepto)', xy=(0, b0),
        xytext=(1.2, b0 + 3),
        fontsize=9, color='#c05000',
        arrowprops=dict(arrowstyle='->', color='#c05000', lw=1.2))

    ax_main.legend(loc='upper left', fontsize=9)

    # --- Panel derecho: información textual ---
    ax_info.set_facecolor('white')
    ax_info.axis('off')

    def make_info_text(w, b):
        lines = [
            ('Modelo actual:', '#333333', 13, True),
            (f'   h(x) = x · {w:.2f} + {b:.2f}', '#1863d6', 14, True),
            ('', '', 10, False),
            ('w = slope (pendiente)', '#333333', 11, True),
            (f'   Valor actual: w = {w:.2f}', STYLE['line_color'], 12, True),
            ('', '', 8, False),
        ]
        if w > 0.1:
            lines.append((f'   ↗  La recta SUBE {w:.2f} unidades', '#1a7a1a', 10, False))
            lines.append(('   por cada 1 unidad de x', '#1a7a1a', 10, False))
        elif w < -0.1:
            lines.append((f'   ↘  La recta BAJA {abs(w):.2f} unidades', '#cc0000', 10, False))
            lines.append(('   por cada 1 unidad de x', '#cc0000', 10, False))
        else:
            lines.append(('   → La recta es HORIZONTAL', '#888', 10, False))

        lines += [
            ('', '', 10, False),
            ('b = bias (intercepto)', '#333333', 11, True),
            (f'   Valor actual: b = {b:.2f}', '#c05000', 12, True),
            ('', '', 8, False),
            (f'   Cuando x=0 → y = {b:.2f}', '#c05000', 10, False),
            ('   (donde la recta cruza el eje y)', '#888', 10, False),
            ('', '', 10, False),
            ('MSE actual:', '#333333', 11, True),
            (f'   L(w,b) = {mse_loss(X_DATA,Y_DATA,w,b):.3f}', '#9900cc', 12, True),
        ]
        return lines

    text_objects = []

    def render_info(w, b):
        for t in text_objects:
            t.remove()
        text_objects.clear()
        info = make_info_text(w, b)
        y_pos = 0.95
        for text, color, size, bold in info:
            if text == '':
                y_pos -= 0.025
                continue
            weight = 'bold' if bold else 'normal'
            t = ax_info.text(0.05, y_pos, text, transform=ax_info.transAxes,
                             fontsize=size, color=color, fontweight=weight,
                             verticalalignment='top')
            text_objects.append(t)
            y_pos -= 0.06

    render_info(w0, b0)

    # --- Sliders ---
    plt.subplots_adjust(bottom=0.22, left=0.08, right=0.97, top=0.92, wspace=0.3)

    ax_sw = plt.axes([0.08, 0.12, 0.38, 0.03], facecolor='#f0f0f0')
    ax_sb = plt.axes([0.08, 0.06, 0.38, 0.03], facecolor='#f0f0f0')

    slider_w = Slider(ax_sw, 'w (slope)', -3.0, 5.0, valinit=w0,
                      color='#2563eb', valstep=0.05)
    slider_b = Slider(ax_sb, 'b (bias)',  -5.0, 8.0, valinit=b0,
                      color='#c05000', valstep=0.1)

    def update(val):
        w = slider_w.val
        b = slider_b.val
        # Actualizar recta
        line_h.set_ydata(hipotesis(x_line, w, b))
        line_h.set_label(f'h(x) = {w:.2f}·x + {b:.2f}')
        # Actualizar punto y línea del intercepto
        vline_b.set_ydata([b, b])
        dot_b.set_ydata([b])
        ann_b.set_text(f'b = {b:.1f}\n(intercepto)')
        ann_b.xy = (0, b)
        ann_b.xyann = (1.2, b + 3)
        ax_main.legend(loc='upper left', fontsize=9)
        render_info(w, b)
        fig.canvas.draw_idle()

    slider_w.on_changed(update)
    slider_b.on_changed(update)

    # Anotaciones pedagógicas
    fig.text(0.08, 0.01,
             '→ Mueve w para ver cómo cambia la inclinación    '
             '→ Mueve b para subir/bajar toda la recta',
             fontsize=9, color='#555')

    plt.show()

# =============================================================
# MENÚ PRINCIPAL
# =============================================================
def menu():
    """Muestra un menú para seleccionar la animación a ejecutar."""
    print('\nParte 1 — w (slope) y b (bias)\n')
    parte1_slope_bias()

if __name__ == '__main__':
    menu()
```
