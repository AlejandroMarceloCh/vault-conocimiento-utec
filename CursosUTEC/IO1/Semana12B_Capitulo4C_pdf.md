---
curso: IO1
titulo: Semana12B-Capitulo4C
slides: 64
fuente: Semana12B-Capitulo4C.pdf
---

## Slide 1
Portada del capítulo: "Teoría de la dualidad". Imagen decorativa de fondo: René Magritte, *La Décalcomanie* (1966) — pintura surrealista con silueta recortada de un hombre de espaldas sobre fondo de cielo/cortina roja, usada solo como ilustración decorativa de portada, sin relación matemática con el contenido. Logo UTEC.

## Slide 2
Slide de transición/título de sección: "Investigación de operaciones 1" — texto simple, sin gráficos relevantes.

## Slide 3
Título de sección: "A la búsqueda de un límite inferior" (solo título, sin contenido adicional visible).

## Slide 4
"A la búsqueda de un límite inferior". Texto: "Cualquier solución factible es un límite inferior del óptimo". Pregunta retórica al pie: "¿Por ejemplo?" — invita a que el estudiante proponga un punto factible.

## Slide 5
"A la búsqueda de un límite superior". Dos ejemplos de evaluación de la función objetivo en puntos factibles: `(1, 0, 0) => 4` y `(0, 0, 3) => 9`. Pregunta: "¿Cuánto cerca estamos del óptimo?" y "Necesitamos un límite superior".

## Slide 6
"A la búsqueda de un límite superior". Pregunta: "¿Cómo encontrar un límite superior?" con respuesta guiada: "Podemos utilizar las restricciones".

## Slide 7
"A la búsqueda de un límite superior". Texto: "Buscamos una combinación lineal de las dos restricciones que sea mayor que la función objetivo".

## Slide 8
"A la búsqueda de un límite superior". Pregunta: "¿Ejemplo?" (transición hacia el ejemplo numérico de las siguientes slides).

## Slide 9
"A la búsqueda de un límite superior". Se muestran las restricciones del ejemplo trabajado, marcadas con las variables x2 y x3 destacadas como "mayor que la función objetivo":
$$11x_1 + 5x_2 + 3x_3 \le 11$$
$$10x_1 + x_2 + 3x_3 \le 10$$

## Slide 10
"A la búsqueda de un límite superior". Mismas restricciones que la slide anterior. Pregunta: "¿Se puede mejorar? ¿Qué significa mejorar el límite superior? Un mejor límite superior debería ser mayor o menor que 11?" (razonamiento guiado sobre cómo combinar las restricciones para bajar la cota).

## Slide 11
"A la búsqueda de un límite superior". Mismas restricciones, ahora resaltando x1 con la pregunta "todavía mayor que la función objetivo" — se explora combinar las restricciones multiplicándolas por coeficientes y1, y2 no negativos.

## Slide 12
"A la búsqueda de un límite superior". Se introduce formalmente la combinación lineal con multiplicadores y1≥0, y2≥0 sobre las restricciones:
$$11x_1+5x_2+3x_3 \le 11,\quad 10x_1+x_2+3x_3\le10$$
$$(y_1+3y_2)x_1+(4y_1{-}y_2)x_2+(y_2)x_3 \le y_1+3y_2$$
Pregunta: "Que tenemos que hacer? Maximizar? Minimizar?"

## Slide 13
"A la búsqueda de un límite superior". Igual que la anterior, con la pregunta "¿Tenemos restricciones?" y la conclusión de que hay que **Minimizar** (el límite superior y1+3y2 sujeto a que los coeficientes dominen a los de la función objetivo original, con y1,y2≥0).

## Slide 14
"A la búsqueda de un límite superior". Se cierra el razonamiento: "Ese problema de minimización es el **dual** del problema de maximización original" — primera aparición explícita del concepto de problema dual, con la combinación lineal de restricciones mostrada como demostración informal.

## Slide 15
"Dual de un problema". Slide de build/animación (primera de una secuencia): aparecen dos columnas encabezadas "Problema primal…" y "…y su dual", inicialmente vacías o con muy poco contenido — se van revelando en las slides 16-18 siguientes.

## Slide 16
"Dual de un problema" (continuación del build). Columnas "Problema primal… / …y su dual" con más elementos revelados progresivamente (probablemente la función objetivo del primal apareciendo del lado izquierdo).

## Slide 17
"Dual de un problema" (continuación del build). Un paso más de la animación mostrando la construcción fila por fila del dual a partir del primal (restricciones → variables duales, coeficientes → función objetivo dual).

## Slide 18
"Dual de un problema" (última del build). Las dos columnas "Problema primal" y "su dual" completas, mostrando la correspondencia final entre ambos programas lineales.

## Slide 19
"Dual de un problema". Pregunta guía: "¿Cómo escribir el problema en forma canónica?" — transición hacia el procedimiento general de dualización.

## Slide 20
"Dual de un problema". Explicación: "Minimizar algo es maximizar su negativo y 'negativar' el resultado" — regla mnemotécnica para convertir min↔max al dualizar.

## Slide 21
"Dual de un problema". Aplicación concreta de la regla anterior con un ejemplo numérico:
$$-\max\; y_1+3y_2$$
$$\text{s.t.}\quad y_1+3y_2 \ge 4$$
$$4y_1+y_2 \ge 1$$
$$y_2 \ge 3$$
$$y_1,y_2\ge0$$
Título recordatorio al pie: "Minimizar algo es maximizar su negativo y 'negativar' el resultado".

## Slide 22
"El dual del dual de un problema es su primal". Dos columnas "Primal" y "Dual" (slide introductoria de la propiedad de involución de la dualidad), contenido mínimo visible aparte del título.

## Slide 23
"Teorema de la dualidad débil". Enunciado formal: dado (x1,…,xn) factible del primal y (y1,…,ym) factible del dual:
$$\sum_j c_j x_j \le \sum_i b_i y_i$$
Anotación: "Valor objetivo de cualquier solución del problema de maximización ≤ Valor objetivo de cualquier solución del problema de minimización".

## Slide 24
"Teorema de la dualidad débil". Repite el enunciado anterior, añadiendo la anotación de que la desigualdad da "el mejor límite superior del primal": "Valor óptimo del problema de maximización ≤ Valor óptimo del problema de minimización".

## Slide 25
"Teorema de la dualidad débil". Diagrama de recta numérica con dos corchetes `]` y `[` mostrando dos intervalos disjuntos: a la izquierda "valores posibles del primal" y a la derecha "valores posibles del dual", ilustrando que el conjunto de valores factibles del primal está siempre por debajo del conjunto de valores factibles del dual.

## Slide 26
"Teorema de la dualidad débil". Mismo diagrama de recta numérica, pero ahora marcando los extremos como "valor óptimo del primal" (corchete derecho `]`) y "valor óptimo del dual" (corchete izquierdo `[`), con la pregunta manuscrita en rojo: "¿gap (diferencia) de dualidad?"

## Slide 27
"Teorema de la dualidad débil". Diagrama similar pero con los corchetes `][` juntándose (sin espacio entre "valor óptimo del primal" y "valor óptimo del dual"), y la pregunta: "…o no gap? Si no hay gap, ¿qué significa?"

## Slide 28
"Teorema de la dualidad fuerte". Enunciado formal con superíndices *: si el primal tiene solución óptima (x1*,…,xn*), el dual también tiene solución óptima (y1*,…,ym*) tal que:
$$\sum_j c_j x_j^{*} = \sum_i b_i y_i^{*}$$
Columnas "Primal" y "Dual" con la igualdad "Valor óptimo del problema de maximización = Valor óptimo del problema de minimización".

## Slide 29
"Teorema de la dualidad fuerte". Repite la igualdad de valores óptimos maximización = minimización, con diagrama de recta numérica mostrando los corchetes `][` unidos (sin gap) etiquetados "valor óptimo del primal" / "valor óptimo del dual", y la nota: "No hay gap de optimalidad si existe una solución óptima para el problema primal o dual".

## Slide 30
"Resultados" (corolarios de la dualidad fuerte/débil), lista:
1. Primal óptimo ⟺ dual óptimo
2. Primal no acotado ⟹ dual no factible
3. Dual no acotado ⟹ primal no factible

## Slide 31
"Ejercicio 1". Enunciado:
$$\max\; z = 5x_1+2x_2$$
$$\text{s.t.}\quad x_1+x_2 \le 2$$
$$2x_1+3x_2 \le 5$$
$$x_1,x_2\ge 0$$
Consigna: "Escribir el dual del programa".

## Slide 32
"Ejercicio 2". Enunciado:
$$\min\; z=6x_1+3x_2$$
$$\text{s.t.}\quad 6x_1-3x_2+x_3 \ge 2$$
$$3x_1+4x_2+x_3\ge5$$
$$x_1,x_2,x_3\ge0$$
Consigna: "Escribir el dual del programa".

## Slide 33
"Ejercicio 3". Enunciado (verificado en imagen):
$$\max\; z=x_1+x_2$$
$$\text{s.t.}\quad 2x_1+x_2=5$$
$$3x_1-x_2=6$$
$$x_1,x_2\in\mathbb{R}$$
Consigna: "Escribir el dual del programa". (Nota: variables libres, restricciones de igualdad — caso especial de dualización.)

## Slide 34
"Ejercicio 4". Enunciado (verificado en imagen):
$$\min\; -2x_1-3x_2-2x_3-3x_4$$
$$\text{s.t.}\quad -2x_1-x_2-3x_3-2x_4 \ge -8$$
$$3x_1+2x_2+2x_3+x_4 \le 7$$
$$x_1,x_2,x_3,x_4\ge0$$
Lista de 5 consignas a la derecha:
1. Escribir el programa en forma estándar
2. Escribir el dual del programa
3. Encontrar una solución óptima del dual con el método gráfico
4. Hacer la primera iteración del simplex con el programa original (primal). Después de 3 iteraciones obtenemos que la solución óptima es (0, 2, 0, 3)
5. Averiguar que la solución encontrada en la pregunta 3 es óptima

## Slide 35
Slide de título de sección: "Método simplex **dual**" (texto centrado, "dual" en negrita).

## Slide 36
Slide inicial del ejemplo guía del método simplex dual (verificado en imagen). Programa primal (P) marcado en rojo:
$$\text{maximize}\; -x_1-x_2$$
$$\text{subject to}\; -2x_1-x_2\le4$$
$$-2x_1+4x_2\le-8$$
$$-x_1+3x_2\le-7$$
$$x_1,x_2\ge0$$
Se indica con flecha roja "Dual (D) —>" el espacio donde se escribirá el dual, y la consigna "Escribir el problema dual" (aún sin resolver en esta slide).

## Slide 37
Continuación (verificado en imagen). Mismo primal (P) a la izquierda; a la derecha se muestra ya resuelto el dual (D):
$$\text{minimize}\;4y_1-8y_2-7y_3$$
$$\text{subject to}\; -2y_1-2y_2-y_3\ge-1$$
$$-y_1+4y_2+3y_3\ge-1$$
$$y_1,y_2,y_3\ge0$$

## Slide 38
Continuación (verificado en imagen). Se piden los "diccionarios iniciales" de (P) y (D), con la nota roja recordatoria "minimizar algo es maximizar su negativo y 'negativar' el resultado" (preparación antes de escribirlos).

## Slide 39
Continuación (verificado en imagen). Diccionarios iniciales ya escritos:
(P): $\zeta=-x_1-x_2$; $w_1=4+2x_1+x_2$; $w_2=-8+2x_1-4x_2$; $w_3=-7+x_1-3x_2$.
(D): $-\xi=-4y_1+8y_2+7y_3$; $z_1=1-2y_1-2y_2-y_3$; $z_2=1-y_1+4y_2+3y_3$.

## Slide 40
Continuación (verificado en imagen). Mismos diccionarios (P) y (D); a la derecha la pregunta "<- diccionario factible?" junto a ambos, planteando si son factibles en el origen.

## Slide 41
Continuación (verificado en imagen). Respuesta: para (P) se anota "<- el diccionario primal **no es** factible" (w2=-8 y w3=-7 son negativos en el origen); para (D) queda pendiente la pregunta "<- diccionario factible?".

## Slide 42
Continuación (verificado en imagen). Se confirma: "<- el diccionario dual **es** factible" (todos los términos independientes de z1, z2 son ≥0), con la conclusión "Idea: más simple aplicar el simplex al dual".

## Slide 43
Continuación — Paso 1 del simplex dual (verificado en imagen). Se identifican la variable de salida (w2, la más negativa en el diccionario primal) y la variable de entrada correspondiente, señaladas con círculos rojo/azul. Nota: "y2 en (D) corresponde a w2 en (P)"; "z1 en (D) corresponde a x1 en (P)" — se explica la correspondencia biunívoca entre variables primal/dual.

## Slide 44
Continuación — Paso 1 (verificado en imagen). Igual señalización de variable de salida (w2 ↔ z1) y variable de entrada (x1 ↔ 8y2), con la instrucción "Escribir el diccionario después del paso 1" (aún sin resolver el pivoteo).

## Slide 45
Continuación — resultado del Paso 1 (verificado en imagen). Diccionarios actualizados tras el pivoteo:
(P): $\zeta=-4-0.5w_2-3x_2$; $w_1=12+w_2+5x_2$; $x_1=4+0.5w_2+2x_2$; $w_3=-3+0.5w_2-x_2$.
(D): $-\xi=4-12y_1-4z_1+3y_3$; $y_2=0.5-y_1-0.5z_1-0.5y_3$; $z_2=3-5y_1-2z_1+y_3$.

## Slide 46
Continuación — Paso 2 (verificado en imagen). Se identifica nueva variable de salida (w3 ↔ y2) y variable de entrada (w2 ↔ 3y3), señaladas con círculos. Resultado del pivoteo mostrado a la derecha:
(P): $\zeta=-7-w_3-4x_2$; $w_1=18+2w_3+7x_2$; $x_1=7+w_3+3x_2$; $w_2=6+2w_3+2x_2$.
(D): $-\xi=7-18y_1-7z_1-6y_2$; $y_3=1-2y_1-z_1-2y_2$; $z_2=4-7y_1-3z_1-2y_2$.

## Slide 47
Continuación — conclusión del ejemplo (verificado en imagen). Diccionarios finales de (P) y (D) mostrados (idénticos a los del final de la slide anterior), con la nota "los dos diccionarios son óptimos" (todos los coeficientes del renglón objetivo son del signo correcto). Conclusión en rojo: "**No se necesita** escribir el diccionario dual para aplicar el simplex dual, se puede aplicar directamente al diccionario primal. ¿Cómo no?"

## Slide 48
"¿Cómo no?" — Ilustración del algoritmo aplicado directamente sobre el diccionario primal (verificado en imagen), retomando el diccionario inicial de (P) y (D) con las variables de entrada/salida marcadas. A la derecha, procedimiento en 2 pasos:
1) Seleccionar la variable de salida (entre las variables básicas) que tiene el término constante más negativo.
2) Seleccionar la variable de entrada calculando el ratio del coeficiente de la línea de la variable de salida y del coeficiente del objetivo, eligiendo el pivote que corresponde al ratio más negativo.

## Slide 49
Pregunta de transición (verificado en imagen), texto centrado en rojo: "¿Qué pasa cuando los diccionarios primal y dual, ambos, son no factibles?"

## Slide 50
"¿Se acuerdan del método del problema auxiliar?" (verificado en imagen). Se recuerda el programa original:
$$\max\;\sum_{j=1}^n c_jx_j \quad \text{s.t.}\quad \sum_{j=1}^n a_{ij}x_j\le b_i\ (i=1,\dots,m),\quad x_j\ge0$$
y el problema auxiliar clásico (método de la Fase I):
$$\max\;-x_0\quad\text{s.t.}\quad\Big(\sum_{j=1}^n a_{ij}x_j\Big)-x_0\le b_i,\quad x_j\ge0\ (j=0,\dots,n)$
Nota roja: "Existe un método más elegante con el dual!"

## Slide 51
Nuevo ejemplo con ambos diccionarios no factibles (verificado en imagen). Primal (P):
$$\max\; -x_1+4x_2$$
$$\text{s.t.}\; -2x_1-x_2\le4,\; -2x_1+4x_2\le-8,\; -x_1+3x_2\le-7,\; x_1,x_2\ge0$$
Diccionario primal: $\zeta=-x_1+4x_2$; $w_1=4+2x_1+x_2$; $w_2=-8+2x_1-4x_2$; $w_3=-7+x_1-3x_2$. Dual (D): $-\xi=-4y_1+8y_2+7y_3$; $z_1=1-2y_1-2y_2-y_3$; $z_2=-4-y_1+4y_2+3y_3$. Conclusión: "**Problema**: ningún diccionario es factible".

## Slide 52
Continuación (verificado en imagen). Se presenta la "Idea": modificar el objetivo del primal para que el diccionario inicial del dual sea factible; la solución óptima del problema modificado no será óptima para el original, pero será factible. Se muestra la modificación concreta: $\zeta=-x_1+4x_2 \;\to\; \eta=-x_1-x_2$.

## Slide 53
Continuación (verificado en imagen). Diccionario óptimo del primal modificado (η) obtenido tras el pivoteo:
$\eta=-7-w_3-4x_2$; $w_1=18+2w_3+7x_2$; $x_1=7+w_3+3x_2$; $w_2=6+2w_3+2x_2$.
Se muestra el paso de "substitución" de x1 de vuelta en la función objetivo original ζ = −x1+4x2, obteniendo el nuevo renglón objetivo $\zeta=-7-w_3+x_2$ con variable de entrada x2, lo que conduce a un **problema no acotado** en esa dirección (anotado en rojo).

## Slide 54
"Síntesis" del método (verificado en imagen), lista numerada:
1) Hacemos que el primer diccionario del dual sea factible modificando la función objetivo del primal.
2) Utilizamos el simplex dual sobre el primal.
3) Obtenemos un punto extremo (factible) del primal.
4) Utilizamos el punto extremo encontrado como punto inicial del simplex sobre el problema original.

## Slide 55
Slide de título de sección: "Interpretación económica de la dualidad" (texto centrado, sin gráficos).

## Slide 56
"Producción de cerveza" (verificado en imagen). Se presenta el modelo base con anotaciones de qué representa cada variable:
$$\max\;6x_1+2x_2$$
$$\text{s.t.}\;6x_1+4x_2\le24\;\text{(Recursos malta Munich, M1)}$$
$$x_1+2x_2\le6\;\text{(Recursos malta Chocolate, M2)}$$
Anotaciones: x1 = # batch Triple (C1), x2 = # batch Oscura (C2).

## Slide 57
"Producción de cerveza" (verificado en imagen). Mismo modelo; se plantea el razonamiento económico: "Vender las 6 unidades de Munich (M1) a y1 dólares/unidad y la unidad de Chocolate (M2) a y2 dólares/unidad genera una utilidad de $6y_1+y_2$ dólares" y la pregunta "¿Me interesa producir un batch menos de Tripel (C1) para vender la malta no utilizada? → depende de los precios y1 e y2".

## Slide 58
"Interpretación económica de las variables duales" (verificado en imagen). Mismo modelo primal; se plantea "¿A qué precio mínimo vender la malta 1?" derivando la restricción dual: $6y_1+y_2\ge6$.

## Slide 59
"Interpretación económica de las variables duales" (verificado en imagen). Análogo para la malta 2: "¿A qué precio mínimo vender la malta 2?" derivando $4y_1+2y_2\ge2$.

## Slide 60
"Interpretación económica de las variables duales" (verificado en imagen). Se plantea el problema dual completo a partir de las dos restricciones anteriores: si un comprador quiere comprar todo el stock de malta al costo mínimo, debe resolver
$$\min\;24y_1+6y_2\quad\text{s.t.}\;6y_1+y_2\ge6,\;4y_1+2y_2\ge2$$
Pregunta paralela: "¿A qué precio mínimo de la malta es interesante no producir cerveza para vender todo el stock de malta?"

## Slide 61
"Interpretación económica de las variables duales" (verificado en imagen). Se muestran las soluciones óptimas de ambos problemas lado a lado: primal $(x_1^*,x_2^*)=(4,0)$, dual $(y_1^*,y_2^*)=(1,0)$. Nota explicativa: "Al óptimo, los valores y1* y y2* representan el valor de la malta. En P.L. se llama 'precios duales' o 'precios sombra' (en inglés: dual prices o shadow prices)".

## Slide 62
"Interpretación económica de las restricciones duales" (verificado en imagen). Se construye el "costo reducido" de la Tripel (C1): $\left(6y_1^*+y_2^*\right)-6$ sobre $4y_1^*+2y_2^*-2$ (expresión con costo de recursos menos utilidad del batch), con la explicación: "Si no se produce Tripel en el plan de producción actual, el incremento en la producción de Tripel mejorará el ingreso sólo si el costo reducido de la Tripel es negativo."

## Slide 63
"Interpretación económica de las restricciones duales" (verificado en imagen). Análogo para la Oscura (C2): costo reducido $\dfrac{6y_1^*+y_2^*-6}{4y_1^*+2y_2^*-2}$ (aquí el "−2" corresponde al coeficiente de C2 en la función objetivo), con la misma explicación aplicada a Oscura. Además se muestran los "últimos diccionarios" del primal y del dual con los coeficientes finales (ζ, x1, w2 por un lado; η, y1, s2 por otro, en notación con variables de holgura s1) y la pregunta: "¿De cuánto debería subir la utilidad de la cerveza C2 para que sea rentable producirla?"

## Slide 64
"Ejercicio 6" (verificado en imagen). Enunciado de aplicación práctica: un vendedor de teléfonos móviles con stock de 8 móviles, 4 kits mano libre y 19 tarjetas prepagables quiere liquidar su stock antes de ser reabastecido. Puede vender paquetes de (1 móvil + 2 tarjetas) con utilidad neta 70 soles, o paquetes de (1 móvil + 1 kit mano libre + 3 tarjetas) con utilidad neta 90 soles, en la cantidad que desee dentro del límite de stock. Preguntas:
1. ¿Cuál cantidad de cada oferta debería proponer para maximizar su utilidad neta?
2. Una tienda propone comprar su stock por mayor. ¿Cuáles son los precios razonables que el vendedor tendría que negociar para cada producto (móvil, kit mano libre, tarjeta)? — (pregunta que exige interpretar económicamente las variables del problema dual, cerrando el capítulo).
