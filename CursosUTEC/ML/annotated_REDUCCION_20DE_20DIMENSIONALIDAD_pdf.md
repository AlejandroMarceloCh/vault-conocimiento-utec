---
curso: ML
titulo: annotated-REDUCCION%20DE%20DIMENSIONALIDAD
slides: 7
fuente: annotated-REDUCCION%20DE%20DIMENSIONALIDAD.pdf
---

         Machine Learning​

ACTIVIDAD SOBRE ALGORITMOS DE REDUCCIÓN DE
             DIMENSIONALIDAD


                    GRUPO


              INTEGRANTES

             Alejandro Marcelo

              José Guerrero

               París Herrera

             Leonardo Montoya
                                            2026
Codigo:
https://colab.research.google.com/drive/1s9QVgAriYp41yzlfcQ1TuQHD-O2NH8Nc?usp=sha
ring



1. Pipeline del código
Se analiza el comportamiento de tres algoritmos de reducción de dimensionalidad — PCA,
t-SNE y UMAP — sobre el dataset toro_10d_200.csv, que contiene 200 muestras descritas
por 10 variables (x1…x10) agrupadas en 4 clases. Los datos representan una estructura
tipo toro embebida en 10 dimensiones, con separación entre clases fuertemente no lineal.

Todas las variables se estandarizan con StandardScaler antes de aplicar cada algoritmo,
paso indispensable porque PCA es sensible a la escala (varianza) y t-SNE/UMAP se basan
en distancias. La reducción se realiza a 2D y a 3D para los tres métodos.

Para t-SNE se varió el hiperparámetro perplexity (5, 10, 20, 30, 50). Para UMAP se varió la
combinación de n_neighbors (5, 10, 15, 30, 50) y min_dist (0.0, 0.1, 0.3, 0.5, 0.99),
incluyendo una serie con n_neighbors fijo en 15 para aislar el efecto de min_dist. En total se
evaluaron 34 configuraciones (2 de PCA + 10 de t-SNE + 22 de UMAP, sumando 2D y 3D).

La separabilidad de las clases en cada embedding se cuantifica con el coeficiente de silueta
(silhouette score), calculado sobre las etiquetas reales de clase. Valores cercanos a 1
indican clases compactas y bien separadas; valores cercanos a 0, solapamiento. Esta
métrica permite comparar configuraciones de forma objetiva además de la inspección visual.

2. Comparación de Resultados:
2.1. Análisis de PCA

Se aplicó PCA con 2 y 3 componentes principales, se obtuvo un único resultado por
dimensionalidad.

2.1.1. PCA 2D

Se obtuvo una varianza retenida de 77.96% y un silhouette score de 0.2600. Esto indica que
con solo 2 componentes principales se captura casi el 78% de la varianza total de las 10
dimensiones originales, lo cual es razonable pero implica una pérdida del 22% de la
información.

En el gráfico se observa que las 4 clases están parcialmente separadas pero con
considerable solapamiento. Se distingue una tendencia donde las clases 0 y 1 (tonos azules
y cyan) se agrupan hacia la parte inferior, mientras que las clases 2 y 3 (tonos rosa y rojo)
tienden hacia la parte superior. Sin embargo, no existen fronteras limpias entre las clases.
Esto se puede explicar porque el toro es una estructura no lineal y PCA, al ser una
proyección lineal, no logra "desenrollar" esa geometría: lo que hace es aplastar la rosquilla,
mezclando clases que en el espacio original estaban en lados opuestos del toro.
2.1.2. PCA 3D

Se obtuvo una varianza retenida de 98.42% y un silhouette score de 0.2442. La varianza
retenida subió significativamente (de 78% a 98%), pero el silhouette bajó (de 0.26 a 0.24).
Esto demuestra que varianza retenida y separación de clases no son equivalentes. La
tercera componente principal captura un 20% adicional de varianza, pero esa varianza
corresponde a direcciones que no necesariamente ayudan a distinguir las clases y puede
agregar una dimensión donde las clases se solapan aún más.

En el gráfico 3D se observa que los puntos forman una nube más extendida gracias a la
tercera dimensión, pero las clases siguen mezcladas de manera similar al caso 2D. Se
intuye ligeramente la forma toroidal, pero la separación entre colores no mejora.
3. Comparación a 2D

PCA es prácticamente instantáneo (0.003 s) y retiene 77.96% de varianza en 2
componentes, pero al ser lineal mezcla parcialmente las clases (silhouette 0.260): las clases
rojo y rosa quedan con un borde difuso entre sí. t-SNE, con su mejor perplexity (50),
alcanzó el silhouette más alto de los tres en 2D (0.337) y dibuja las clases como arcos
diferenciados. UMAP, con su mejor combinación (n_neighbors=30, min_dist=0.3), obtuvo un
resultado intermedio (0.316), también con las cuatro clases visualmente distinguibles
aunque con más mezcla entre rosa y celeste.




4. Comparación a 3D

En 3D, como se mencionó anteriormente, PCA mejora notablemente: retiene 98.42% de la
varianza, ya que el toro vive esencialmente en muy pocas direcciones de máxima varianza
del espacio de 10D. Sin embargo, su silhouette en 3D (0.244) es menor al de PCA 2D
(0.260), la dimensión extra agrega información geométrica pero no necesariamente separa
mejor las clases bajo esta métrica, porque la tercera dimensión no es la que más diferencia
a las clases entre sí. t-SNE 3D con perplexity=50 mejora respecto a su versión 2D (0.270 vs
0.337, (estos valores intentamos no tratarlos como comparables entre sí por estar en
espacios de distinta dimensión). UMAP 3D con su mejor combinación (n_neighbors=50,
min_dist=0.1) alcanza 0.285, el más alto de los tres en 3D.




5. Variación de hiperparámetros: t-SNE
La perplexity controla el tamaño del vecindario efectivo que t-SNE intenta preservar. Con
perplexity=5 el algoritmo atiende solo a vecinos muy próximos y fragmenta cada clase en
pequeños grupos dispersos (silhouette 0.115). Los valores intermedios (10 y 20) producen
resultados similares entre sí (0.221 y 0.210), con clases parcialmente agrupadas pero aún
con bordes confusos. El resultado sorprendente es perplexity=30, que da el peor resultado
intermedio (0.140), esto podría evidenciar de que la relación entre perplexity y separabilidad
de clases no es continua en este dataset y conviene siempre verificar empíricamente, no
asumir que un valor intermedio es automáticamente mejor. El mejor resultado, por margen
claro, es perplexity=50 (silhouette 0.337): un vecindario amplio permite capturar la forma
global de cada clase en la superficie del toro.
Resultados — t-SNE 2D (silhouette por perplexity):
 perp=5             perp=10             perp=20            perp=30             perp=50 (mejor)
 0.115              0.221               0.210              0.140               0.337




6. Variación de hiperparámetros: UMAP
Con n_neighbors bajo (5) UMAP fragmenta las clases en cúmulos pequeños y aislados
(silhouette 0.115), similar al efecto visto en t-SNE con perplexity baja: hay muy poca
información de vecindario para reconstruir la forma global de cada clase. A medida que
n_neighbors crece (10, 15, 30, 50) la separabilidad mejora de forma consistente. La mejor
combinación encontrada es n_neighbors=30 con min_dist=0.3 (silhouette 0.316),
donde las cuatro clases quedan dispuestas en bandas claramente diferenciadas alrededor
del toro proyectado. Con n_neighbors=50 los resultados son buenos pero ligeramente
inferiores (0.237 a 0.284 según min_dist), suponiendo que un vecindario demasiado amplio
empieza a mezclar información de clases vecinas.
Fijando n_neighbors=15 y variando solo min_dist se aísla su efecto: valores bajos (0.0 y 0.1)
producen prácticamente el mismo resultado (silhouette 0.208 y 0.207), con grupos
compactos pero algo fragmentados internamente. Subir a min_dist=0.5 aporta una mejora
marginal (0.218). El salto más claro ocurre en min_dist=0.99 (0.270): al expandir los puntos
dentro de cada grupo se reduce la superposición visual entre clases vecinas. Esto confirma
que min_dist por sí solo tiene un efecto más modesto que n_neighbors, pero ayuda
especialmente en sus valores extremos.




Mejor configuración UMAP por dimensión:
 Dimensión                       Mejor combinación               Silhouette
 2D                              n_neighbors=30, min_dist=0.3    0.316
 3D                              n_neighbors=50, min_dist=0.1    0.285


7. t-SNE vs UMAP con la mejor configuración
Comparando ambos métodos en su mejor configuración 2D, t-SNE obtiene un silhouette
ligeramente superior (0.337 frente a 0.316 de UMAP), y visualmente dispone las clases
como arcos largos y continuos sobre el plano. UMAP, aunque levemente por debajo en la
métrica, produce una separación igualmente clara y con una geometría más compacta. La
diferencia entre ambos (0.021) es pequeña frente a la dispersión observada al variar los
propios hiperparámetros de cada método (hasta 0.22 puntos de silhouette entre la peor y la
mejor configuración), lo cual indica que la elección correcta del hiperparámetro pesa más
que la elección del algoritmo en sí.
La diferencia práctica relevante está en la capacidad de generalización: t-SNE no tiene un
método transform() y debe re-ejecutarse por completo si se agregan datos nuevos, mientras
que UMAP sí permite proyectar puntos nuevos sobre el embedding ya aprendido sin
reentrenar desde cero. Para un caso de uso exploratorio puntual, t-SNE es preferible por su
ligera ventaja en separabilidad; para un flujo de trabajo donde lleguen datos nuevos de
forma recurrente, UMAP es la opción más práctica.
8. Tabla resumen comparativa
Método             Tipo              Estructura       Varianza explicada      transform()
PCA                Lineal            Global           Sí                      Sí
t-SNE              No lineal         Local            No                      No
UMAP               No lineal         Local + global   No                      Sí
                                     parcial


Método (2D)          Mejor config.       Silhouette         Tiempo (s)         Var. retenida
PCA                  —                   0.260              0.003              77.96%
t-SNE                perplexity=50       0.337              0.598              N/A
UMAP                 nn=30, md=0.3       0.316              0.314              N/A


9. Conclusiones
  •​    PCA es el método más rápido (milisegundos) y el único interpretable en términos de
        varianza explicada, pero al ser lineal no logra la mejor separabilidad de clases en 2D
        (silhouette 0.260), reflejando que la estructura del toro es no lineal.
  •​    t-SNE alcanzó la mayor separabilidad medida en 2D (silhouette 0.337) con
        perplexity=50. Su comportamiento frente a la perplexity no fue continuo: el valor
        intermedio (30) dio resultados peores que valores cercanos (20 y 50), lo que
        confirma la necesidad de barrer varios valores en vez de asumir uno por defecto.
  •​    UMAP fue competitivo (silhouette 0.316 en 2D con n_neighbors=30, min_dist=0.3) y,
        a diferencia de t-SNE, permite proyectar datos nuevos sin reentrenar, lo que lo hace
        más adecuado para escenarios donde el dataset puede crecer.
  •​    El hiperparámetro con mayor impacto en ambos métodos no lineales fue el que
        controla el tamaño del vecindario (perplexity en t-SNE, n_neighbors en UMAP):
        valores muy bajos fragmentan las clases en ambos casos. min_dist, en cambio, tuvo
        un efecto más acotado, notorio principalmente en sus valores extremos.
  •​    Se podría recomendar que para una exploración visual puntual de este dataset,
        t-SNE con perplexity=50 da el resultado más nítido; para un pipeline que deba
        incorporar datos nuevos de forma recurrente, UMAP con n_neighbors=30 y
        min_dist=0.3 es la opción más adecuada.
