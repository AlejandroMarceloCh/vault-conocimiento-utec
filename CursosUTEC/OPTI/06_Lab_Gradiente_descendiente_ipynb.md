---
curso: OPTI
titulo: 06_Lab_Gradiente_descendiente
slides: 0
fuente: 06_Lab_Gradiente_descendiente.ipynb
---

<div class="cell markdown" id="Ji3B8vd7aHJb">

**Ejercicio:** Considere la función
``` math
f(x, y)=10x^2+y^2
```

a\) Implemente la función y su gradiente.

b\) Implemente el Método del Gradiende Descendiente. Considere el punto inicial $`x_0=(2, 8)`$ y $`\alpha=0.001`$. Indique cuántas iteraciones fueron necesarias para que el algoritmo converja con una tolerancia de $`10^{-5}`$.

c\) Realice una gráfica del valor de la función con respecto al número de iteraciones.

d\) Fije una cantidad máxima de iteraciones de $`10^5`$ e indique qué sucede con el algoritmo para distintos valores de $`\alpha`$: ¿para qué valores de $`\alpha`$ converge el algoritmo?

</div>

<div class="cell code" id="d-rldta4Z1oB">

``` python
import numpy as np
import matplotlib.pyplot as plt

def f(punto):
  return 10*(punto[0]**2) + (punto[1]**2)

def g(punto):
  fx = 20*punto[0]
  fy = 2*punto[1]
  return np.array([fx,fy])
```

</div>

<div class="cell code" id="Nu4G_YULWM7q">

``` python
def gradiente_descendiente(f, gradiente, alpha, x0, epsilon, max_iteraciones):
  iteraciones = 0

  tol=epsilon+1

  valores = [] # Lista para almacenar los valores de f

  while tol > epsilon:

    if iteraciones == max_iteraciones:
      print("El algoritmo no convergió en ", max_iteraciones, " iteraciones")
      break

    valores.append(f(x0))

    x1 = x0-alpha*gradiente(x0)

    tol = np.linalg.norm(x1-x0)

    x0=x1

    iteraciones += 1
  return x0, valores, iteraciones
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="-YJAcWUUWV-I" outputId="c056c277-be7d-4586-fa71-e9f499b8f646">

``` python
# Solucion b)
x0 = np.array([2, 8])
alpha =  0.001
epsilon = 10**-5
iter_max = 10**4
x_min, valores, iteraciones = gradiente_descendiente(f, g, alpha, x0, epsilon, iter_max)
print(x_min, iteraciones)
```

<div class="output stream stdout">

    [8.94480905e-33 4.98190812e-03] 3687

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:447}" id="fiyrt8j4WmN3" outputId="09db0250-f302-423a-ed71-53eb2b8fbfc0">

``` python
# Solucion c)
print(valores[-1])
plt.plot(valores, color='red')
plt.show()
```

<div class="output stream stdout">

    2.491898476001402e-05

</div>

<div class="output display_data">

![](2848a3c9c8b5e10c280a310fb94bf0afe681135b.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="T12JgAoJtZOr" outputId="ff02c331-0ecf-48e7-e22a-a253e8763c47">

``` python
x0 = np.array([2, 8])
alpha =  0.11
epsilon = 10**-5
iter_max = 10**5
x_min, valores, iteraciones = gradiente_descendiente(f, g, alpha, x0, epsilon, iter_max)
print(x_min, iteraciones)
```

<div class="output stream stdout">

    [    nan 1.e-323] 3875

</div>

<div class="output stream stderr">

    /tmp/ipython-input-2604268519.py:5: RuntimeWarning: overflow encountered in scalar multiply
      return 10*(punto[0]**2) + (punto[1]**2)
    /tmp/ipython-input-2604268519.py:5: RuntimeWarning: overflow encountered in scalar power
      return 10*(punto[0]**2) + (punto[1]**2)
    /tmp/ipython-input-2604268519.py:8: RuntimeWarning: overflow encountered in scalar multiply
      fx = 20*punto[0]
    /tmp/ipython-input-1626038771.py:16: RuntimeWarning: invalid value encountered in subtract
      x1 = x0-alpha*gradiente(x0)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:477}" id="Rzz2m316tm8I" outputId="33f52c89-6bfa-458b-fe6f-cbeaeac09225">

``` python
plt.plot(valores[10**1:], color='red')
plt.show()
```

<div class="output stream stderr">

    /usr/local/lib/python3.12/dist-packages/matplotlib/ticker.py:2176: RuntimeWarning: overflow encountered in multiply
      steps = self._extended_steps * scale
    /usr/local/lib/python3.12/dist-packages/matplotlib/ticker.py:2218: RuntimeWarning: overflow encountered in scalar subtract
      high = edge.ge(_vmax - best_vmin)
    /usr/local/lib/python3.12/dist-packages/matplotlib/ticker.py:2034: RuntimeWarning: invalid value encountered in scalar divmod
      d, m = divmod(x, self.step)

</div>

<div class="output error" ename="ValueError" evalue="arange: cannot compute length">

    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    /usr/local/lib/python3.12/dist-packages/IPython/core/formatters.py in __call__(self, obj)
        339                 pass
        340             else:
    --> 341                 return printer(obj)
        342             # Finally look for special method names
        343             method = get_real_method(obj, self.print_method)

    /usr/local/lib/python3.12/dist-packages/IPython/core/pylabtools.py in print_figure(fig, fmt, bbox_inches, base64, **kwargs)
        149         FigureCanvasBase(fig)
        150 
    --> 151     fig.canvas.print_figure(bytes_io, **kw)
        152     data = bytes_io.getvalue()
        153     if fmt == 'svg':

    /usr/local/lib/python3.12/dist-packages/matplotlib/backend_bases.py in print_figure(self, filename, dpi, facecolor, edgecolor, orientation, format, bbox_inches, pad_inches, bbox_extra_artists, backend, **kwargs)
       2153                 # so that we can inject the orientation
       2154                 with getattr(renderer, "_draw_disabled", nullcontext)():
    -> 2155                     self.figure.draw(renderer)
       2156             if bbox_inches:
       2157                 if bbox_inches == "tight":

    /usr/local/lib/python3.12/dist-packages/matplotlib/artist.py in draw_wrapper(artist, renderer, *args, **kwargs)
         92     @wraps(draw)
         93     def draw_wrapper(artist, renderer, *args, **kwargs):
    ---> 94         result = draw(artist, renderer, *args, **kwargs)
         95         if renderer._rasterizing:
         96             renderer.stop_rasterizing()

    /usr/local/lib/python3.12/dist-packages/matplotlib/artist.py in draw_wrapper(artist, renderer)
         69                 renderer.start_filter()
         70 
    ---> 71             return draw(artist, renderer)
         72         finally:
         73             if artist.get_agg_filter() is not None:

    /usr/local/lib/python3.12/dist-packages/matplotlib/figure.py in draw(self, renderer)
       3255 
       3256                 self.patch.draw(renderer)
    -> 3257                 mimage._draw_list_compositing_images(
       3258                     renderer, self, artists, self.suppressComposite)
       3259 

    /usr/local/lib/python3.12/dist-packages/matplotlib/image.py in _draw_list_compositing_images(renderer, parent, artists, suppress_composite)
        132     if not_composite or not has_images:
        133         for a in artists:
    --> 134             a.draw(renderer)
        135     else:
        136         # Composite any adjacent images together

    /usr/local/lib/python3.12/dist-packages/matplotlib/artist.py in draw_wrapper(artist, renderer)
         69                 renderer.start_filter()
         70 
    ---> 71             return draw(artist, renderer)
         72         finally:
         73             if artist.get_agg_filter() is not None:

    /usr/local/lib/python3.12/dist-packages/matplotlib/axes/_base.py in draw(self, renderer)
       3179             _draw_rasterized(self.get_figure(root=True), artists_rasterized, renderer)
       3180 
    -> 3181         mimage._draw_list_compositing_images(
       3182             renderer, self, artists, self.get_figure(root=True).suppressComposite)
       3183 

    /usr/local/lib/python3.12/dist-packages/matplotlib/image.py in _draw_list_compositing_images(renderer, parent, artists, suppress_composite)
        132     if not_composite or not has_images:
        133         for a in artists:
    --> 134             a.draw(renderer)
        135     else:
        136         # Composite any adjacent images together

    /usr/local/lib/python3.12/dist-packages/matplotlib/artist.py in draw_wrapper(artist, renderer)
         69                 renderer.start_filter()
         70 
    ---> 71             return draw(artist, renderer)
         72         finally:
         73             if artist.get_agg_filter() is not None:

    /usr/local/lib/python3.12/dist-packages/matplotlib/axis.py in draw(self, renderer)
       1413         renderer.open_group(__name__, gid=self.get_gid())
       1414 
    -> 1415         ticks_to_draw = self._update_ticks()
       1416         tlb1, tlb2 = self._get_ticklabel_bboxes(ticks_to_draw, renderer)
       1417 

    /usr/local/lib/python3.12/dist-packages/matplotlib/axis.py in _update_ticks(self)
       1290         the axes.  Return the list of ticks that will be drawn.
       1291         """
    -> 1292         major_locs = self.get_majorticklocs()
       1293         major_labels = self.major.formatter.format_ticks(major_locs)
       1294         major_ticks = self.get_major_ticks(len(major_locs))

    /usr/local/lib/python3.12/dist-packages/matplotlib/axis.py in get_majorticklocs(self)
       1534     def get_majorticklocs(self):
       1535         """Return this Axis' major tick locations in data coordinates."""
    -> 1536         return self.major.locator()
       1537 
       1538     def get_minorticklocs(self):

    /usr/local/lib/python3.12/dist-packages/matplotlib/ticker.py in __call__(self)
       2226     def __call__(self):
       2227         vmin, vmax = self.axis.get_view_interval()
    -> 2228         return self.tick_values(vmin, vmax)
       2229 
       2230     def tick_values(self, vmin, vmax):

    /usr/local/lib/python3.12/dist-packages/matplotlib/ticker.py in tick_values(self, vmin, vmax)
       2234         vmin, vmax = mtransforms.nonsingular(
       2235             vmin, vmax, expander=1e-13, tiny=1e-14)
    -> 2236         locs = self._raw_ticks(vmin, vmax)
       2237 
       2238         prune = self._prune

    /usr/local/lib/python3.12/dist-packages/matplotlib/ticker.py in _raw_ticks(self, vmin, vmax)
       2217             low = edge.le(_vmin - best_vmin)
       2218             high = edge.ge(_vmax - best_vmin)
    -> 2219             ticks = np.arange(low, high + 1) * step + best_vmin
       2220             # Count only the ticks that will be displayed.
       2221             nticks = ((ticks <= _vmax) & (ticks >= _vmin)).sum()

    ValueError: arange: cannot compute length

</div>

<div class="output display_data">

    <Figure size 640x480 with 1 Axes>

</div>

</div>
