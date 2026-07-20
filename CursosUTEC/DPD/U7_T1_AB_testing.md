---
curso: DPD
titulo: U7_T1_AB_testing.pptx
slides: 65
fuente: U7_T1_AB_testing.pptx.pdf
---

# U7_T1_AB_testing.pptx

## Índice

1. [Objetivos de la Sesión](#objetivos-de-la-sesión)
2. [Contexto: Ciclo de Vida y Sistemas de Recomendación](#contexto-ciclo-de-vida-y-sistemas-de-recomendación)
3. [A/B Testing — Definiciones](#ab-testing--definiciones)
4. [Fundamentos de Experimentación en Negocios](#fundamentos-de-experimentación-en-negocios)
5. [Proceso de A/B Testing](#proceso-de-ab-testing)
6. [Significancia Estadística](#significancia-estadística)
7. [Diseño de AB Testing](#diseño-de-ab-testing)
8. [AB Testing en DS](#ab-testing-en-ds)
9. [Conclusiones](#conclusiones)
10. [Glosario](#glosario)

## Objetivos de la Sesión

Comprender la naturaleza y utilidad de A/B testing, identificar los problemas empresariales que pueden ser abordados con esta herramienta y mostrar la experiencia práctica de utilizar A/B testing en la toma de decisiones.

Además comprender el uso de A/B testing en ciencia de datos.

**Figura:** Título «Objetivos de la Sesión» en tipografía sans-serif grande, negrita y negra, dividido en dos líneas («Objetivos de la» / «Sesión»). A la derecha del primer párrafo, un ícono de línea azul que representa la cabeza y hombros de una persona junto a un documento con varias líneas de texto. El primer párrafo de objetivos aparece en texto negro, con la frase final «mostrar la experiencia práctica de utilizar A/B testing en la toma de decisiones.» resaltada en color azul claro/cian. El segundo párrafo en texto negro. una de las secciones fotográficas tiene una superposición de color azul brillante.

(slides 3)

## Contexto: Ciclo de Vida y Sistemas de Recomendación

### Ciclo de Vida

**Figura:** Diagrama titulado «CICLO DE VIDA» que representa el ciclo de vida de un producto de datos, compuesto por tres bucles circulares interconectados que representan tres etapas principales: **Prototype**, **Industrialize** y **Operate**.

**1. Prototype (bucle superior izquierdo):** Etapa de desarrollo y validación inicial.
- **Capture (Data = Data Products):** sub-puntos «From Eco-system», «To systems», «From Catalogue», «External». Íconos: globo, base de datos y cuadrícula.
- **Understand:** sub-puntos «Join», «Annotate / Collaborate», «proc(semantic)», «EDA / Feat Eng». Íconos: lupa sobre monedas y grupo de personas.
- **Model (Data Product Prototype):** sub-puntos «Experiments», «Use-case specific», «Schema / Structures», «Algorithms / models», «Business flows». Íconos: matraz de Erlenmeyer y diagrama de flujo.
- **Visualize:** «Data Stories / Journeys». Ícono: distintos tipos de gráficos de datos.
- **Present:** «Business / Stakeholders», «Fast feedback».

**2. Industrialize (bucle central):** Transición de prototipo a producto listo para producción.
- **Engineer:** «Hardening (pipelines)», «Packaging», «Automation», «CI/CD». Íconos: engranajes y caja.
- **Test:** «A/B», «Train with Production data», «Regression». Íconos: red neuronal y lista de verificación «TEST».
- **Control:** «Policies», «DQ rules», «Map to taxonomy / Data Dictionary». Íconos: carpeta con candado y etiqueta «AD».
- **Publish:** «Data Products published to eco-system».

**3. Operate (bucle inferior derecho):** Mantenimiento y monitoreo en producción.
- **Execute / Adapt:** «Runtime operations», «Continuous Training», «Parameter adjustment», «Bug Fixing». Ícono: engranajes con flechas circulares.
- **Monitor:** «Observability», «Skew / Drift», «DQ / Policy breaches», «System errors», «Usage», «ESG». Íconos: lupa sobre diversos medidores.
- **Retire:** «Switch off if not used / too expensive». Ícono: mano presionando un botón de encendido.

**Flujo e interconexiones:** Flechas grandes de color azul claro indican el flujo hacia adelante de **Prototype** a **Industrialize**, y de **Industrialize** a **Operate**. Bucles de retroalimentación con flechas que regresan de **Industrialize** a **Prototype** y de **Operate** a **Industrialize**, indicando un proceso iterativo.

(slides 4)

### Sistemas de Recomendación

Descomposición de la matriz de calificaciones $R$ en el producto de $P$ y $Q$.

Cada usuario y cada ítem se describen con $F$ características latentes.

- $P$: factores de usuario
- $Q$: factores de ítem

¿Cómo sabemos que tan bueno es una recomendación?

Predicción del usuario $u$ acerca del item $i$:

$$p_{u,i} = q_i^T p_u = \sum_{f=1}^{F} q_{i,f} \cdot p_{u,f}$$

**Figura:** Título «Sistemas de Recomendación» en tipografía sans-serif grande, negrita y gris. En el centro de la slide, texto en rojo semitransparente de gran tamaño con la pregunta «¿Cómo sabemos que tan bueno es una recomendación?». Diagrama de factorización de matrices en tres partes:

- **Matriz de calificaciones (izquierda):** Cuadrícula dispersa etiquetada «Ratings matrix». Las filas corresponden a avatares de usuarios y las columnas a pósters de películas. La mayoría de las celdas están vacías; algunas contienen calificaciones numéricas (por ejemplo, 1, 2, 4, 5).
- **Descomposición (centro):** La matriz dispersa es aproximadamente igual ($\approx$) al producto de dos matrices: **Matriz $P$ (factores de usuario)**, un rectángulo alto y estrecho de color gris cuyas filas corresponden a avatares de usuarios; y **Matriz $Q$ (factores de ítem)**, un rectángulo ancho y delgado de color gris cuyas columnas corresponden a pósters de películas. La intersección representa la dimensión $F$ (número de factores/características latentes), etiquetada «F factors».
- **Matriz predicha (derecha):** Cuadrícula densa con borde azul que contiene valores numéricos predichos para cada celda (por ejemplo, 2, 3, 1, 4, 5, 1 en la primera fila), representando la matriz completada tras las predicciones del sistema de recomendación.

En la parte inferior, la fórmula de predicción mostrada arriba.

(slides 5)

## A/B Testing — Definiciones

### Historia y adopción

En el año 2000, los ingenieros de Google querían determinar el número óptimo de resultados que debían mostrar en los resultados del motor de búsqueda. Para recopilar evidencia que les ayudara a tomar esta decisión, realizaron algo llamado A/B Testing.

**Figura:** En la parte superior, el párrafo transcrito arriba; las palabras «2000» y «el número óptimo de resultados que debían mostrar en los resultados del motor de búsqueda» aparecen resaltadas en negrita. Debajo, un infográfico de estilo dibujado a mano que ilustra el proceso de A/B testing:

1. **Visitors (Visitantes):** En el extremo izquierdo, una columna vertical de cinco íconos de personas estilizadas (alternando azul y rojo) etiquetada «Visitors».
2. **A/B Test:** Flechas conducen a los visitantes hacia un círculo rojo etiquetado «A/B Test».
3. **La división:** Desde este círculo, los visitantes se dividen en dos grupos:
   - **Option A:** Dos visitantes son dirigidos hacia un mockup de página web etiquetado «Option A», con una barra de encabezado roja. Una flecha conduce desde este mockup hacia un resultado; sobre la flecha, un círculo azul contiene el valor «17%».
   - **Option B:** Dos visitantes son dirigidos hacia un mockup etiquetado «Option B», con un círculo rojo grande en el centro. Una flecha conduce hacia un resultado final; sobre la flecha, un círculo rojo contiene el valor «25%».
4. **Resultados:** Ambos caminos conducen hacia un mockup final de interfaz de usuario a la derecha, indicando que «Option B» tuvo mejor desempeño (25% vs 17%).

Esta fue la primera prueba A/B realizada por Google, y se dice que son los pioneros de las pruebas A/B en la era digital.

muchas empresas más pequeñas también utilizan este enfoque para tomar decisiones basadas en datos (marketing, mejorar su contenido y experiencia del cliente).

**Figura:** En la parte superior, el texto transcrito arriba sobre el papel pionero de Google en A/B testing. En la parte inferior, el texto sobre empresas más pequeñas; la frase «más pequeñas» está resaltada en color azul claro/cian.

Plataformas de A/B testing:

- Optimizely
- Google Firebase
- Oracle CX Marketing
- VWO
- Adobe Target
- …

muchas empresas más pequeñas también utilizan este enfoque para tomar decisiones basadas en datos (marketing, mejorar su contenido y experiencia del cliente).

**Figura:** En la parte superior, el mismo encabezado sobre Google como pionero de A/B testing. En el centro, una lista con viñetas de plataformas de A/B testing (enumeradas arriba). En la parte inferior, el texto sobre empresas más pequeñas; las palabras «más pequeñas» resaltadas en color azul claro/cian brillante.

(slides 7–9)

### Definiciones

Las pruebas A/B o pruebas divididas, originadas en los ensayos controlados aleatorios estadísticos, son una de las formas más populares para que las empresas prueben:

- nuevas características de UX
- nuevas versiones de un producto
- nuevas versiones de un algoritmo

**Figura:** Encabezado «DEFINICIONES:» en tipografía sans-serif negrita de color gris oscuro en la parte superior izquierda. Subtítulo «A/B Testing» en color azul claro/cian debajo. Párrafo de definición en el cuerpo de la slide; las frases «pruebas A/B» y «pruebas divididas» en negrita. Lista de tres viñetas debajo del párrafo.

La práctica de usar experimentos aleatorizados para tomar decisiones empresariales.

**Figura:** Encabezado «DEFINICIONES:» en gris oscuro y subtítulo «A/B Testing» en cian en la parte superior izquierda. Texto centrado con la definición transcrita arriba. Debajo del texto, dos capturas de pantalla lado a lado que representan un escenario de A/B test en una página de producto de Nike:

- **Versión A:** Etiquetada con una «A» grande en un recuadro blanco sobre la captura. Muestra una página de producto para un zapato de baloncesto azul Nike «NIKE REACT HYPERDUNK FLYKNIT», precio $160. El botón «ADD TO CART» en la parte inferior de la página es de color **naranja**.
- **Versión B:** Etiquetada con una «B» grande en un recuadro blanco sobre la captura. Muestra la misma página de producto, pero el botón «ADD TO CART» es de color **verde**.

La práctica de usar experimentos aleatorizados para tomar decisiones empresariales.

Las pruebas A/B NO son:

probar múltiples estrategias de manera improvisada y comparar resultados.

**Figura:** Encabezado «DEFINICIONES:» en gris oscuro y subtítulo «A/B Testing» en cian en la parte superior izquierda. Bloque de texto con la definición positiva transcrita arriba. En el centro, las mismas dos capturas de pantalla lado a lado del zapato Nike (versión A con botón naranja, versión B con botón verde), cada una etiquetada con «A» y «B» respectivamente en recuadros blancos.

(slides 10–12)

### ¿Cuándo usar apropiadamente?

Los experimentos aleatorizados son el "gold standard" para medir causa y efecto.

○ Las pruebas A/B pueden ayudarte a predecir el futuro

Pueden ayudarte a comprender realmente qué componentes de tus productos/servicios generan valor.

Pueden facilitar una cultura de medición empírica y aprendizaje organizacional.

**Figura:** Título «AB TESTING» en negrita negra en la parte superior izquierda. Subtítulo «¿Cuándo usar apropiadamente?» en color cian debajo. Tres bloques de texto con los puntos transcritos arriba; el primer bloque incluye un sub-punto con círculo vacío (○).

"LA EXPERIMENTACIÓN ES EL MÉTODO MENOS ARROGANTE DE ADQUIRIR CONOCIMIENTO"

Isaac Asimov
Padre de las tres leyes de la robótica

**Figura:** Slide con fondo gris oscuro dividida en dos secciones. **Lado izquierdo:** Fotografía en blanco y negro de **Isaac Asimov**, mostrado de pecho hacia arriba, con traje oscuro, camisa con cuello, gafas de montura gruesa y patillas blancas prominentes; su mano derecha descansa contra su barbilla en una pose reflexiva. **Lado derecho:** Cita grande en español, en tipografía sans-serif mayúsculas: «LA EXPERIMENTACIÓN ES EL MÉTODO MENOS ARROGANTE DE ADQUIRIR CONOCIMIENTO»; la mayor parte del texto es blanco, pero las palabras «EXPERIMENTACIÓN» y «CONOCIMIENTO» están resaltadas en color cian/azul claro brillante. Debajo de la cita, atribución alineada a la derecha: «Isaac Asimov» en blanco, y debajo, subrayado, «Padre de las tres leyes de la robótica». Número de página «14» en la esquina inferior derecha en tipografía gris claro pequeña.

Las empresas tecnológicas (Microsoft, Google, Amazon, Facebook) son conocidas por tener organizaciones intensamente experimentales.

Las nuevas empresas de software han permitido una experimentación rigurosa incluso para empresas muy pequeñas (o equipos pequeños y no técnicos en grandes empresas).

Casi todas las plataformas de análisis web pueden ser utilizadas para experimentación.

**Figura:** Título «AB TESTING» en negrita negra en la parte superior izquierda. Subtítulo «¿Cuándo usar apropiadamente?» en color cian debajo. Tres párrafos con los puntos transcritos arriba; en cada párrafo, frases clave resaltadas en color cian: «tener organizaciones intensamente experimentales.», «experimentación rigurosa incluso para empresas muy pequeñas», y «de análisis web».

(slides 13–15)

## Fundamentos de Experimentación en Negocios

### ¿Por qué se ejecutan experimentos?

La experimentación aleatoria es una técnica de recolección de datos que está específicamente diseñada como un medio para la "inferencia causal".

Inferencia causal:

El proceso de entender y medir la Causa & Efecto.

**Figura:** Título «¿Por qué se ejecutan experimentos?» en negrita gris oscuro/negro. Párrafo sobre experimentación aleatoria; la frase «inferencia causal» resaltada en color cian/azul claro brillante. Subtítulo en negrita «Inferencia causal:» seguido de la definición transcrita arriba.

(slides 18)

### Correlación no implica Causalidad

Diferencia entre correlación y causalidad:

- La semana pasada, rediseñamos nuestra página de inicio y las conversiones de clientes aumentaron.

- Las conversiones de clientes aumentaron la semana pasada debido a nuestro nuevo diseño de la página de inicio.

**Figura:** Título «Correlación no implica Causalidad» en negrita gris oscuro en la parte superior. Subtítulo en cursiva «Diferencia entre correlación y causalidad:». Dos viñetas en texto cursiva con las afirmaciones transcritas arriba: la primera es una observación de correlación; la segunda es una afirmación de causalidad.

(slides 19)

### ¿Por qué este problema es difícil?

Es difícil separar tus acciones de otros factores que podrían afectar el comportamiento del cliente:

**Figura:** Título «¿Por qué este problema es difícil?» en negrita. Subtítulo con el texto transcrito arriba. Diagrama central que ilustra cómo múltiples variables influyen en un único resultado:

1. **Variable independiente (la acción, izquierda):** Ícono de una ventana de navegador que contiene dos rectángulos etiquetados «A» y «B». Debajo, el texto «Diseño de página». Una flecha de color verde azulado apunta desde este ícono hacia una laptop central.
2. **Variable dependiente (el resultado, centro inferior):** Ícono de una laptop etiquetada «Comportamiento del cliente». Es el objetivo al que apuntan todas las flechas.
3. **Factores de confusión (el «ruido», derecha):** Cuatro flechas de color verde azulado apuntan hacia la laptop central desde el lado derecho, cada una representando un factor externo:
   - **Día de la semana:** Acompañado de un ícono de un billete de dólar.
   - **Clima:** Acompañado de un ícono de un sol detrás de una nube de lluvia.
   - **Campañas de marketing - Competidores:** Acompañado de un ícono de una silueta de cabeza azul gritando.
   - **Estrategias - Competidores:** Acompañado de un ícono de emoji de diablo morado.

(slides 20)

### ¿Cómo ayuda la randomización?

La aleatorización de qué página de inicio ven los clientes te permite aislar el efecto de esa variable; con suficientes datos, otros factores que afectan el comportamiento deberían equilibrarse.

**Figura:** Diagrama central con un ícono de laptop etiquetado «Comportamiento del cliente» en el centro. Hacia ese nodo convergen cinco flechas desde factores externos:

- **Izquierda (variable principal):** Ícono de ventana de navegador con dos recuadros internos etiquetados «A» y «B», con la etiqueta «Diseño de página» debajo. Una flecha azul grande apunta desde este ícono hacia el laptop central.
- **Arriba-derecha:** Ícono de signo de dólar verde con la etiqueta «Día de la semana».
- **Centro-derecha (arriba):** Ícono de sol y nube de lluvia con la etiqueta «Clima».
- **Centro-derecha (medio):** Ícono de silueta de cabeza hablando en color azul con la etiqueta «Campañas de marketing - Competidores».
- **Abajo-derecha:** Ícono de emoji de diablito morado con la etiqueta «Estrategias - Competidores».

Todas las flechas apuntan hacia el laptop central «Comportamiento del cliente».

(slides 21)

### Cuándo son valiosas las pruebas A/B

son valiosas en situaciones cuando

1. [Estás dispuesto a admitir que] No sabes cuál es la mejor.

1. Puedes implementar cada estrategia utilizando la aleatorización.

1. Puedes medir los resultados de cada estrategia en las dimensiones que te importan

**Figura:** Título «AB TESTING» en tipografía sans-serif grande, negrita y gris oscuro en la parte superior izquierda. Subtítulo «son valiosas en situaciones cuando» en color cian. Lista de tres puntos en cursiva, cada uno precedido por «1.».

(slides 22)

### ¿Qué deberíamos medir?

- Esto depende críticamente de tu industria/contexto

- Existen muchos recursos en línea y guías de experiencia del usuario

- Ojo: Lo que funciona para una empresa puede no funcionar para la tuya
  - Si desarrollas una cultura de experimentación sistemática, aprenderás qué componentes de tu sitio servicio son los más importantes.

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «¿Qué deberíamos medir?» en color cian. Tres viñetas principales en texto negro; la frase «componentes de tu sitio servicio son los más importantes.» del sub-bullet aparece resaltada en color cian.

(slides 23)

### Etapas

1. Desarrolla un conjunto de "hipótesis" para probar: por ejemplo, "variaciones", "tratamientos", "estrategias" etc.

2. Define tus criterios de evaluación clave

3. Define tu tamaño de muestra previsto y los criterios de parada

4. Ejecuta tu experimento: Asigna aleatoriamente a los clientes a los brazos de tratamiento

5. Evalúa tus resultados: Implementa el brazo "ganador"

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Etapas» en color cian. Cinco pasos numerados en tipografía cursiva negra.

(slides 24)

## Proceso de A/B Testing

### Visión general del proceso

**Figura:** Título «AB TESTING» en negrita negra y subtítulo «Proceso» en color cian en la parte superior izquierda. Diagrama circular central que representa el proceso de A/B testing, compuesto por un anillo circular de color verde azulado claro con cinco círculos numerados de color verde azulado oscuro distribuidos a lo largo del camino, en secuencia horaria:

1. **Paso 1 (aproximadamente a las 9 en punto):** «Hipótesis de la prueba A/B».
2. **Paso 2 (aproximadamente a las 7 en punto):** «Diseño de la prueba A/B».
3. **Paso 3 (aproximadamente a las 4 en punto):** «Ejecutar la prueba A/B».
4. **Paso 4 (aproximadamente a las 2 en punto):** «Análisis de resultados | Significancia estadística».
5. **Paso 5 (a las 12 en punto):** «Análisis de resultados | Significancia práctica».

Ícono de tres flechas apuntando a la derecha dentro de una forma hexagonal en la esquina inferior derecha.

(slides 16)

### Ejemplo práctico: Nike

**Figura:** Slide con el encabezado «Ejemplo:» en texto azul en la esquina superior izquierda. En el centro, captura de pantalla de una ventana de navegador mostrando una página de producto de Nike vista a través de una herramienta de edición o A/B testing:

- **Producto:** «NIKE REACT HYPERDUNK 2017 FLYKNIT», categoría «BASKETBALL SHOE», precio «$160».
- **Calificación:** 4 estrellas con «(3)» reseñas.
- **Imagen principal:** Zapatilla de baloncesto azul de caña alta, con borde de selección azul y etiqueta «Image <img>».
- **Miniaturas:** Cuatro imágenes en miniatura debajo de la imagen principal.
- **Opciones de color:** Cuatro muestras de color debajo del precio.
- **Selector de talla:** Cuadro desplegable gris con tooltip negro que dice «Select a Size».
- **Botón CTA:** Botón naranja brillante «ADD TO CART» en la parte inferior de la sección de detalles del producto.

**Panel de edición (lado derecho):** Barra superior azul con íconos de deshacer, rehacer y cerrar (X). Panel vertical con propiedades de estilo CSS: opciones de texto (color, subrayado, alineación), sección «BACKGROUND» con valor `rgba(0, 0, 0, 0)` (transparente), campos para imágenes de fondo y configuración de repetición.

(slides 25)

#### Hipótesis

**Figura:** Slide con el encabezado «Hipótesis:» en azul claro en la esquina superior izquierda. Dos mockups lado a lado de una página de producto Nike, etiquetados «A» y «B»:

**Detalles del producto (idénticos en ambas versiones):**
- Nombre: «NIKE REACT HYPERDUNK 2017 FLYKNIT»
- Tipo: «BASKETBALL SHOE»
- Imagen: Zapatilla de baloncesto azul marino de caña alta con upper Flyknit texturizado y suela azul claro.
- Reseñas: 4 estrellas con «(28)» reseñas.
- Selector de talla con tooltip «Select a Size».

**Diferencias entre variantes (variables del experimento):**

| Elemento | Variante A | Variante B |
| :--- | :--- | :--- |
| Precio | $190 | $160 |
| Botón «ADD TO CART» | Naranja brillante | Verde lima |

**Figura:** Slide con el encabezado «Hipótesis:» en azul claro. Dos capturas de pantalla lado a lado de la página de producto Nike «NIKE REACT HYPERDUNK 2017 FLYKNIT» con precio «$160»:

- **Variante A (izquierda):** Botón «ADD TO CART» de color **naranja**.
- **Variante B (derecha):** Botón «ADD TO CART» de color **verde**.

Todos los demás elementos de la página (menú de navegación, imagen del zapato, precio, calificación con estrellas, variantes de color y selector de talla) son idénticos entre las dos versiones.

**Preguntas en la parte inferior izquierda (texto azul claro):**
- ¿Criterio de evaluación?
- ¿Cuánto tiempo se ejecutará?

**Figura:** Slide con el encabezado «Hipótesis:» en azul. Dos capturas de pantalla lado a lado de la página de producto Nike «NIKE REACT HYPERDUNK 2017 FLYKNIT» con precio «$160»:

- **Variante A:** Botón «ADD TO CART» **naranja**.
- **Variante B:** Botón «ADD TO CART» **verde**.

Calificación visible: 4 estrellas con 19 reseñas. Incluye muestras de color y desplegable de selección de talla.

¿Criterio de evaluación?: Ratio de conversión

¿Cuánto tiempo se ejecutará? 2 Semanas

(slides 26–28)

#### Ejecución y resultados

**Figura:** Diagrama de flujo circular que ilustra el proceso de A/B testing:

1. **Usuario (arriba-izquierda):** Ícono de persona «Usuario» junto a un laptop. Flecha hacia un cilindro etiquetado «Servidor». Texto: «El usuario hace un requerimiento al servidor».

2. **Asignación aleatoria:** Desde el servidor, flecha hacia la derecha con la etiqueta «Testing randomizado». El proceso se divide en dos caminos asignando al usuario a Variante A o Variante B.

3. **Tratamiento mostrado:**
   - **Variante A:** Página web de zapato Nike azul con botón CTA **naranja**.
   - **Variante B:** Misma página con botón CTA **verde**.
   - Flecha de retorno al laptop con texto: «El usuario ve el tratamiento asignado».

4. **Registro de acciones:** Flecha hacia abajo desde el laptop con texto: «El software de pruebas registra las acciones del usuario (por ejemplo, compra/no compra)».

5. **Reporte de resultados:** Flecha hacia una tabla etiquetada «Reporte de resultados».

**Tabla de resultados:**

| Variant | Sessions | Conversion | Conversion Rate | Lift over baseline | p-value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| A (Orange) | 4812 | 127 | 2.59% | -- | -- |
| B (Green) | 4858 | 78 | 1.60% | -0.99 | 0.02* |

**Figura:** En la parte superior, dos botones visuales de las variantes:

- **Variante A:** Botón rectangular naranja con texto blanco «ADD TO CART».
- **Variante B:** Botón rectangular verde lima con texto blanco «ADD TO CART».

**Tabla de resultados:**

| Variante | Sesiones | Conversión | Conversión (%) | P-value |
| :--- | :--- | :--- | :--- | :--- |
| A | 4912 | 127 | 2.59% | |
| B | 4866 | 78 | 1.60% | |

La columna «P-value» está vacía para ambas variantes. Contornos hexagonales grises tenues en el fondo.

(slides 29–30)

### Proceso — Hipótesis

**Figura:** Diagrama circular con un anillo de color verde azulado claro y cinco círculos numerados distribuidos alrededor, representando un flujo secuencial en sentido horario:

| Paso | Etiqueta | Posición | Estilo |
| :--- | :--- | :--- | :--- |
| 1 | Hipótesis de la prueba A/B | ~9 en punto (izquierda) | Círculo verde azulado oscuro (resaltado, paso activo); texto en color teal/azul |
| 2 | Diseño de la prueba A/B | ~7 en punto | Círculo gris; texto gris claro |
| 3 | Ejecutar la prueba A/B | ~5 en punto | Círculo gris; texto gris claro |
| 4 | Análisis de resultados \| Significancia estadística | ~3 en punto | Círculo gris; texto gris claro |
| 5 | Análisis de resultados \| Significancia práctica | 12 en punto (arriba) | Círculo gris; texto gris claro |

Título «Proceso» en tipografía sans-serif azul claro grande en la parte superior izquierda. Ícono de tres flechas apuntando a la derecha en cian y azul en la esquina inferior derecha.

La hipótesis de negocio describe qué dos productos se están comparando y cuál es el impacto o la diferencia deseada para el negocio:

- cómo 'arreglar' un problema potencial en el producto

- la solución influirá en los Indicadores Clave de Desempeño (KPIs)

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Proceso - Hipótesis» en color cian. Las palabras «dos productos» y «comparando» en el párrafo principal aparecen resaltadas en cian. La palabra «arreglar» en la primera viñeta aparece resaltada en cian.

Métrica Primaria. es una forma de medir el rendimiento del producto que se está probando en A/B testing, tanto para los grupos experimentales como para los de control.

Se utilizará para identificar si hay una diferencia estadísticamente significativa entre estos dos grupos.

- única métrica primaria

- ¿mayores ingresos?
- ¿mayor compromiso?
- ¿más visualizaciones?

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Proceso - Hipótesis» en color cian. Las frases «producto que se está probando» y «estadísticamente significativa» aparecen resaltadas en cian. Viñeta «única métrica primaria» en la parte inferior izquierda. Tres preguntas de ejemplo de métricas en la parte inferior derecha.

(slides 31–33)

### Proceso — Hipótesis — Métrica

Ganancia:

$$\text{Ratio de Conversión} = \frac{\text{Número de Conversión}}{\text{Número de Visitantes}} \times 100\%$$

$$= \frac{50}{1000} \times 100\% = 5\%$$

**Figura:** Título «AB TESTING» en letras mayúsculas gris oscuro. Subtítulo «Proceso – Hipótesis - Métrica» en azul claro. Encabezado «Ganancia:» en color cian. Fórmula del Ratio de Conversión con ejemplo numérico.

Engagement:

$$\text{Click To Rate (CTR)} = \frac{\text{Número de Clicks}}{\text{Número de apariciones}} \times 100\%$$

$$= \frac{25}{1000} \times 100\% = 2.55\%$$

- Tiempo en el Sitio Web,
- Páginas Vistas por Sesión,
- Interacciones en Redes Sociales,
- Clics en Enlaces,
- Comentarios y Reseñas,
- Tasa de Apertura y Click en Correos Electrónicos,
- Descargas

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Proceso – Hipótesis - Métrica» en cian. Encabezado «Engagement:» en cian. Fórmula de Click To Rate (CTR) con ejemplo numérico que muestra 2.55%. Lista de siete métricas de engagement en viñetas en la parte inferior izquierda.

(slides 34–35)

### Prueba de hipótesis estadística

La prueba de hipótesis o hipótesis estadística es un procedimiento estadístico que se utiliza para determinar si existe una diferencia significativa entre los datos observados y los datos esperados.

- para probar los resultados de un experimento
- establecer la significancia estadística

**Figura:** Título «AB TESTING» en gris oscuro. Subtítulo «Proceso – Hipótesis» en azul claro. Los términos «prueba de hipótesis» e «hipótesis estadística» en el párrafo principal aparecen resaltados en azul claro. Dos viñetas con los propósitos del procedimiento.

(slides 36)

## Significancia Estadística

### ¿Qué es un test de hipótesis?

Es una herramienta estadística que nos sirve para aceptar o rechazar con confianza estadística una hipótesis que hemos obtenido en una muestra.

¿Qué deberíamos medir?

1. Necesitamos plantear una hipótesis sobre el objetivo de negocio que queremos testar.

1. Necesitamos una muestra de datos que sea representativa de la población a estudiar y suficientemente grande

1. Procedimiento estadístico.

**Figura:** Título «¿Qué es un test de hipótesis?» en gris oscuro. Definición en texto cursiva. Subtítulo «¿Qué deberíamos medir?» en azul claro. Tres puntos numerados, cada uno precedido por «1.».

(slides 38)

### Pasos del test de hipótesis

pasos:

1. Plantear la hipótesis h0 y h1.
2. Elegir el nivel de confianza y por tanto el Alpha
3. Elegir el estadístico de contraste adecuado a la prueba y calcular el p-valor

Necesitamos una muestra de datos que sea representativa de la población a estudiar y suficientemente grande

**Figura:** Título «Test de hipótesis:» en negrita gris oscuro. Subtítulo «pasos:» en cursiva. Tres pasos numerados en cursiva. Frase final en cursiva en la parte inferior de la slide.

(slides 39)

### Ejemplo: contraste de proporciones (Nike)

Ejemplo de una prueba de hasta 1000 visitas por versión (de forma aleatoria para los usuarios), medimos cuantas ventas genera cada una de las versions.

**Figura:** Dos capturas de pantalla lado a lado de la página de producto Nike «NIKE REACT HYPERDUNK 2017 FLYKNIT» con precio «$160», etiquetadas «A» y «B» en la esquina superior derecha de cada captura:

- **Versión A (izquierda):** Botón «ADD TO CART» de color **naranja**. Resultado debajo: **38 ventas**.
- **Versión B (derecha):** Botón «ADD TO CART» de color **verde**. Resultado debajo: **60 ventas**.

Ambas capturas muestran la zapatilla, detalles del producto y opciones de selección de forma casi idéntica.

(slides 40)

#### Paso 1: Hipótesis

**Hipótesis Nula:** Las ventas en ambas páginas son estadísticamente iguales

Tasa de conversión página A = Tasa de conversión página B

**Hipótesis Alternativa:** Las ventas en ambas páginas son significativamente diferentes

Tasa de conversión página A $\neq$ Tasa de conversión página B

**Figura:** Título «Paso 1: Hipótesis» en tipografía sans-serif azul claro en la parte superior izquierda. Dos cajas horizontales apiladas, cada una con borde punteado azul:

- **Caja superior (Hipótesis Nula):** A la izquierda, botón rectangular redondeado azul con texto blanco «Hipótesis Nula». A la derecha, texto «Las ventas en ambas páginas son estadísticamente iguales» y debajo, en cursiva más pequeña, «Tasa de conversión página A = Tasa de conversión página B».

- **Caja inferior (Hipótesis Alternativa):** A la izquierda, botón rectangular redondeado azul con texto blanco «Hipótesis Alternativa». A la derecha, texto «Las ventas en ambas páginas son significativamente diferentes» y debajo, en cursiva más pequeña, «Tasa de conversión página A != Tasa de conversión página B».

(slides 41)

#### Paso 2: Nivel de confianza y alpha

¿La conclusión es 100% segura?

- No. El test de hipótesis es una herramienta probabilística, que se basa en la probabilidad normal.

- Eso significa que siempre hay una probabilidad de que nos equivoquemos en la conclusión final.

- Por ello es necesario controlar ese riesgo, y se hace mediante el nivel de confianza.

- Podríamos definirlo como: de cada 100 veces que repitiéramos este experimento, ¿en cuantas de ellas la conclusión no sería la misma que estamos aceptando?

- Con ese dato, que fijamos nosotros obtenemos un parámetro que necesitaremos, y que se llama Alpha y es 1-NC.

¿Cómo de seguro quiero estar?

Creo que al 95% está bien

**Figura:** Título «Paso 2: Elegir un nivel de confianza y por tanto alpha» en azul claro en la parte superior izquierda. Cinco viñetas en texto negro en el cuerpo principal. En el lado derecho, ilustración de una persona con un signo de interrogación en un globo de pensamiento, acompañada del texto lateral «¿Cómo de seguro quiero estar?» y «Creo que al 95% está bien».

(slides 42)

#### Pasos 3 y 4: Estadístico de contraste y p-valor

- En este caso particular es un contraste de proporciones

- Podemos utilizar el z-test

- Aplicando esa prueba el software nos devolverá un dato que se llama pValor

- Si pValor es menor que Alpha entonces podemos rechazar H0

- Si el pValor es mayor o igual que Alpha entonces NO podemos rechazar H0

**Figura:** Título «Paso 3 y 4: Elegir el estadístico de contraste adecuado a la prueba, calcular el pValor y controlarlo con el alpha» en azul claro en la parte superior izquierda. Cinco viñetas en texto negro; los términos «pValor» y «z-test» aparecen resaltados en azul claro, y «H0» aparece resaltado en rojo.

(slides 43)

### Recursos

https://colab.research.google.com/drive/1Om4IH-FOa6vCCWfOh8LKB2UPM51zGnDr?usp=sharing

https://neilpatel.com/ab-testing-calculator/

https://abtestguide.com/calc/

**Figura:** Tres URLs listadas verticalmente en el lado izquierdo de la slide.

(slides 44)

## Diseño de AB Testing

### Unidades de Randomización

"Unidad de randomización" (randomization unit) se refiere al nivel o entidad a la que se aplica la aleatorización en un experimento.

- También conocidas como unidades de diversificación

- Quién o qué asignamos aleatoriamente a cada variante de una prueba A/B

- Impacta la experiencia del usuario y las métricas utilizadas

Puede que consideremos Unidad de randomización son solo los usuarios, sin embargo NO siempre es así

**Figura:** Título «AB TESTING» en negrita gris oscuro en la parte superior izquierda. Subtítulo «1. Unidades de Randomización» en color cian. Párrafo de definición en texto negro. Tres viñetas; las palabras «diversificación», «Quién» y «qué» aparecen resaltadas (en negrita o color verde). En la parte inferior central, frase en color rojo/rosa claro: «Puede que consideremos Unidad de randomización son solo los usuarios, sin embargo NO siempre es así».

(slides 46)

| Unidad de randomización | Pros | Contras |
| :--- | :--- | :--- |
| ID de Usuario o login que los usuarios usan en plataformas y dispositivos | Estable a lo largo del tiempo y plataformas | Identificable |
| Cookie , un ID de usuario seudónimo, específico para un navegador y un dispositivo | Anónimo | Los usuarios pueden borrar cookies, no es persistente a través de plataformas |
| Evento , por ejemplo, una vista de página o sesión | Un nivel más fino de granularidad crea más unidades | Solo apropiado cuando los cambios no son visibles para el usuario |
| ID de Dispositivo | ID inmutable asociado con un dispositivo específico | Identificable, solo disponible para dispositivos móviles |

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Unidades de Randomización» en color cian. Tabla de tres columnas con encabezados en color verde azulado oscuro; las filas alternan fondo gris claro y azul claro. Los nombres de unidad («ID de Usuario», «Cookie», «Evento», «ID de Dispositivo») aparecen en negrita.

(slides 47)

#### ID Usuario

1. Situaciones:
   1. Plataformas de Suscripción: Servicios como Netflix o Spotify que necesitan rastrear el comportamiento del usuario a lo largo del tiempo para personalizar recomendaciones.
   2. E-commerce: Seguimiento de usuarios registrados para personalizar ofertas, carritos de compra y experiencias de usuario.
   3. Aplicaciones de Redes Sociales: Seguimiento de interacciones de los usuarios para ajustar el contenido mostrado en los feeds.

2. Ventajas:
   1. Permite un seguimiento consistente y coherente de los usuarios.
   2. Ideal para análisis longitudinales y personalización.

4. Desventajas:
   1. Puede plantear problemas de privacidad y cumplimiento de normativas.

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Unidades de Randomización – ID Usuario» en color cian y verde oscuro. Lista numerada con tres secciones (1. Situaciones, 2. Ventajas, 4. Desventajas — la numeración salta del 2 al 4). En la sección Situaciones, frases clave resaltadas en color cian: «necesitan rastrear el comportamiento del usuario a lo largo», «personalizar ofertas, carritos de compra y experiencias de usuario», «para ajustar el contenido mostrado en los feeds».

(slides 48)

#### Cookie

Situaciones:
1. Análisis Web Básico: rastrear visitas, conversiones y comportamiento general.
2. Publicidad en Línea: Personalización de anuncios y seguimiento de efectividad de campañas publicitarias.
3. Pruebas A/B en Sitios Web: Para determinar qué versiones de páginas web funcionan mejor en términos de conversión sin necesidad de registro del usuario.

Ventajas:
4. Permite rastrear a los usuarios de manera anónima.
5. Fácil de implementar y utilizar en análisis web.

Desventajas:
6. Los usuarios pueden borrar las cookies, interrumpiendo el seguimiento.
7. No permite rastrear usuarios a través de diferentes dispositivos o navegadores.

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Unidades de Randomización – Cookie» en color cian. Tres secciones (Situaciones, Ventajas, Desventajas) con listas numeradas; la numeración continúa secuencialmente del 1 al 7 a través de las tres secciones. En la situación 3, la frase «sin necesidad de registro del usuario» aparece resaltada en color cian.

(slides 49)

#### Evento

- Situaciones:
  - Análisis de Comportamiento en Tiempo Real: Seguimiento de vistas de página, clics en botones o interacciones en tiempo real.
  - Optimización de Contenido: Determinar qué partes de una página o aplicación son más atractivas para los usuarios.
  - Experimentos de Funcionalidad: Pruebas de nuevas funcionalidades donde los cambios no son visibles para el usuario.

- Ventajas:
  - Detalle más granular.
  - Más puntos de datos para análisis preciso

- Desventajas:
  - Adecuado solo cuando los cambios no son visibles.
  - Puede generar gran cantidad de datos.

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Unidades de Randomización – Evento» en color cian. Tres secciones con viñetas (Situaciones, Ventajas, Desventajas).

(slides 50)

#### Dispositivo

Situaciones:
- Aplicaciones Móviles
- Análisis de Comportamiento de Dispositivos
- Publicidad Móvil

Ventajas:
- Seguimiento persistente y consistente
- Ideal para análisis específicos de dispositivos

Desventajas:
- Solo aplicable a dispositivos móviles
- Problemas de privacidad y cumplimiento

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Unidades de Randomización – Dispositivo» en color cian. Tres secciones (Situaciones, Ventajas, Desventajas) con viñetas.

(slides 51)

#### Resumen de unidades de randomización

ID de Usuario:
- Servicios que requieren seguimiento continuo y personalización

Cookie:
- Análisis web y publicidad en línea

Evento:
- Análisis de comportamiento en tiempo real

ID de Dispositivo:
- Aplicaciones y publicidad móvil

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «Unidades de Randomización» en color cian. Cuatro unidades de randomización listadas con sus nombres en color rojizo/naranja claro y descripciones en negro debajo de cada una.

(slides 52)

### Métrica

- Tiempo en el Sitio Web,

- Páginas Vistas por Sesión,

- Interacciones en Redes Sociales,

- Clicks en Enlaces,

- Comentarios y Reseñas,

- Tasa de Apertura y Click en Correos Electrónicos,

- Descargas

- Establecer el Nivel de Significancia ($\alpha$) => Generalmente 0.05

**Figura:** Título «AB TESTING» en negrita gris oscuro. Subtítulo «2. Métrica» en color cian. Siete viñetas en color cian con métricas de engagement en el lado izquierdo. En la parte inferior, viñeta separada en negro: «Establecer el Nivel de Significancia (α) => Generalmente 0.05».

(slides 53)

## AB Testing en DS

### Idea Base

Antes de implementar este modelo para todos los usuarios, ejecutar este nuevo modelo o modelo "retador" lado a lado con un modelo existente "campeón" en una prueba A/B para encontrar evidencia empírica del impacto que este nuevo modelo tiene en las métricas de negocio, tales como la tasa de clics, la tasa de conversión o los ingresos.

**Figura:** Título «Idea Base:» en color cian en la parte superior izquierda. Diagrama de flujo lineal de tres etapas en el centro:

1. **Offline Evaluation (caja gris, izquierda):** Encima, flecha circular etiquetada «Days» indicando iteración en días. ejes «False positive rate» y «True sensitive rate».

2. **Flecha amarilla «Success»** hacia la etapa central.

3. **A/B Testing (cajas amarillas apiladas, centro):** Encima, flecha circular etiquetada «Weeks» indicando iteración en semanas. Debajo, gráfico de líneas titulado «Real-time Feedback» con dos series (Variant 1 en azul, Variant 2 en naranja) sobre eje «timestamp». Flecha punteada gris etiquetada «Adjust» retrocede desde A/B Testing hacia Offline Evaluation.

4. **Flecha amarilla «Success»** hacia la etapa final.

5. **Deploy model to all users (caja azul, derecha):** Etapa final de despliegue.

Párrafo explicativo en español en la parte inferior de la slide.

(slides 55)

### ¿Cuándo usar?

| Conjunto de Datos Diferente | Modelo Diferente |
| :--- | :--- |
| El conjunto de datos ha sido actualizado para incluir los datos más recientes. | Estás probando una arquitectura de algoritmo diferente. |
| El conjunto de datos ha sido limpiado, normalizado o escalado de forma diferente. | Estás experimentando con diferentes hiperparámetros. |
| El conjunto de datos ha sido remuestreado para eliminar sesgos o ajustar por desequilibrio en clases minoritarias. | Estás utilizando aprendizaje por transferencia para afinar un modelo preentrenado. |

**Figura:** Título «¿Cuándo usar?» en color azul en la parte superior izquierda. Tabla de dos columnas centrada horizontalmente con encabezados «Conjunto de Datos Diferente» y «Modelo Diferente»; bordes y texto en color cian/azul claro. Tres filas de contenido en cada columna.

(slides 56)

### Ejemplo: clasificación de reseñas (Amazon Echo Show 5)

Amazon Echo Show 5, el cual tiene 937 reseñas con una calificación promedio de 4.5 estrellas de 5. La página también muestra una reseña positiva destacada y una crítica destacada.

Entrenar un modelo de clasificación de ML que luego puede identificar las reseñas más útiles basándose únicamente en el texto libre.

**Figura:** Texto descriptivo en la parte superior. Captura de pantalla central de una página de reseñas de Amazon para «Echo Show 5 – Compact smart display with Alexa – Charcoal Fabric»:

- **Calificación global:** «4.5 out of 5 stars», «937 global ratings».
- **Histograma de calificaciones:**
  - 5 star: 72%
  - 4 star: 15%
  - 3 star: 6%
  - 2 star: 3%
  - 1 star: 4%

- **Reseña positiva destacada (columna izquierda):**
  - Reseñador: Jeff R (#1 REVIEWER)
  - Calificación: 5 estrellas
  - Título: «Best Echo Device so Far»
  - Fecha: July 5, 2019
  - Contenido: el reseñador elogia el diseño del dispositivo, lo usa como reloj de cabecera y lo describe como «the sleekest and most attractive unit to date».
  - Métrica de utilidad (caja verde): «85 people found this helpful».

- **Reseña crítica destacada (columna derecha):**
  - Reseñador: Earl E Adopter (TOP 1000 REVIEWER)
  - Calificación: 1 estrella
  - Título: «More of a nuisance than an assistant.»
  - Fecha: August 9, 2019
  - Contenido: el reseñador se queja de ser «bombarded with unwanted news, info and other unwanted distractions»; argumenta que un asistente inteligente debería ser solo un reloj hasta que se le pida información.
  - Métrica de utilidad (caja roja): «32 people found this helpful».

Texto en la parte inferior: «Entrenar un modelo de clasificación de ML que luego puede identificar las reseñas más útiles basándose únicamente en el texto libre.»

(slides 57)

### Sistemas de recomendación

**Figura:** Título «Sistemas de recomendación:» en color azul claro en la parte superior izquierda. Diagrama de flujo de izquierda a derecha que ilustra un A/B test en un motor de recomendaciones:

1. **Entrada (extremo izquierdo):** Cuatro íconos de usuario representando visitantes. Flechas apuntan hacia un ícono de navegador web.

2. **División experimental:** Desde el navegador, flecha hacia una banda vertical gris etiquetada «A/B Test». Los usuarios se dividen en dos grupos (dos íconos de usuario cada uno, dentro de cajas punteadas).

3. **«Inspire Recommendations Engine» (caja punteada grande, derecha):**
   - **Camino superior (grupo control):** Flecha hacia un círculo cian etiquetado «Control Version». Junto a él, fila de seis zapatillas (estilo Vans en colores blanco, rojo y verde).
   - **Camino inferior (grupo alternativo):** Flecha hacia un círculo naranja etiquetado «Alternative Version». Junto a él, fila de seis zapatillas diferentes (incluyendo estilos atléticos/running en marrón, rojo y granate).

(slides 58)

### Experimenting at Scale

Opción 1: Las pruebas A/B pueden evaluar el redactado o el color del botón de llamada a la acción (CTA), y posiblemente dos variaciones del diseño de la página.

Opción 2: Experimentos de optimización impulsados por IA con 15 elementos diferentes y 34 variaciones de esos elementos, resultando en 10,800 combinaciones posibles.

**Figura:** Título «Experimenting at Scale» en color azul en la parte superior izquierda. Dos secciones lado a lado:

- **Sección izquierda (Opción 1):** Texto descriptivo arriba. Debajo, dos wireframes simplificados de página web etiquetados «A» y «B»; son idénticos excepto por un botón rectangular central: en el mockup A el botón es **rojo**, en el mockup B el botón es **negro**. Otros elementos de página (encabezado, imágenes, bloques de texto) representados con placeholders azules y grises.

- **Sección derecha (Opción 2):** Texto descriptivo arriba. Las etiquetas contienen letras (A, B, C, D, E) dentro de cajas de colores; algunas cajas son **rojas** (variación específica) y otras **grises**. Ejemplos de etiquetas visibles: «A B», «A B C», «A B C D», «A B C D E».

(slides 59)

## Conclusiones

### Cierre de la sesión

En esta sesión vimos:

- Conceptos Fundamentales de A/B testing.
- Pasos del proceso de A/B Testing
- Como configurar A/B Testing
- Prueba estadística
- Aplicación práctica

**Figura:** En la parte superior izquierda, el encabezado «Cierre:» en tipografía sans-serif de color azul claro/cian, de gran tamaño. Debajo, el texto en negrita «En esta sesión vimos:» en color negro. A continuación, una lista de cinco viñetas con los temas enumerados arriba, en texto negro. En el borde izquierdo, un pequeño triángulo decorativo de color azul claro apuntando hacia el interior de la slide.

(slides 61)

### Conclusiones

- La prueba AB es un método de comparación estadística que se utiliza para comparar diferentes variantes de una versión básica de un producto.
- A/B testing es uno de los conceptos más importantes en la ciencia de datos y en el mundo tecnológico en general, porque es uno de los métodos más efectivos para sacar conclusiones sobre cualquier hipótesis que uno pueda tener.

**Figura:** En la parte superior izquierda, el título «Conclusiones» en tipografía sans-serif de color azul claro/cian. Debajo, dos viñetas en texto negro; las frases «comparación estadística» y «métodos más efectivos para sacar conclusiones sobre cualquier hipótesis que uno pueda tener.» aparecen resaltadas en el mismo color azul claro/cian que el título. En el borde izquierdo, un triángulo decorativo cian apuntando hacia el interior.

(slides 62)

### Referencias bibliográficas

**Figura:** En el centro de la slide se muestran dos portadas de libros, una al lado de la otra:

Título principal en letras blancas mayúsculas y negritas: «TRUSTWORTHY ONLINE CONTROLLED EXPERIMENTS». Subtítulo en texto blanco más pequeño: «A PRACTICAL GUIDE TO A/B TESTING». Autores en la parte inferior: Ron Kohavi, Diane Tang y Ya Xu. Elemento visual: una figurita de plástico azul de un hipopótamo (referencia a «HiPPO» — Highest Paid Person's Opinion).

- **Portada derecha:** Fondo claro. Título principal en tipografía serif negra delgada y mayúsculas: «EXPERIMENTATION WORKS». Subtítulo centrado debajo: «THE SURPRISING POWER OF BUSINESS EXPERIMENTS». Autor en la parte inferior: Stefan H. Thomke. Elemento visual: ilustración de un matraz de laboratorio de fondo redondo con líquido rosa, con un cursor de ratón de computadora apuntando sobre él, simbolizando la intersección entre experimentación científica y negocios digitales.

En el borde izquierdo, un triángulo decorativo cian.

(slides 63)

### Actividad: DPD-ABtesting (Blooket)

**Figura:** Captura de pantalla de una tarjeta de interfaz de usuario de la plataforma educativa Blooket, estructurada en tres secciones verticales:

1. **Encabezado (fondo turquesa):** La palabra «Blooket» centrada en la parte superior, en tipografía blanca redondeada y lúdica. A la derecha, una etiqueta en forma de píldora de color verde azulado oscuro que dice «12 Questions».

2. Debajo, el texto «5 Plays» indicando el número de veces que se ha jugado el set. Debajo de eso, «Edited 5 months ago» en tipografía más pequeña y gris claro.

3. **Botones de acción (sección inferior):** Fila de tres botones cuadrados con íconos oscuros: lápiz (Editar), bote de basura (Eliminar) y engranaje (Configuración). Debajo, dos botones más grandes: botón «Assign» con ícono de documento, y botón «Host» en color turquesa brillante con un ícono blanco de triángulo de reproducción para iniciar una sesión en vivo.

(slides 64)

## Glosario

**A/B Testing (pruebas A/B / pruebas divididas):** Las pruebas A/B o pruebas divididas, originadas en los ensayos controlados aleatorios estadísticos, son una de las formas más populares para que las empresas prueben nuevas características de UX, nuevas versiones de un producto o nuevas versiones de un algoritmo. La práctica de usar experimentos aleatorizados para tomar decisiones empresariales.

**Inferencia causal:** El proceso de entender y medir la Causa & Efecto. La experimentación aleatoria es una técnica de recolección de datos específicamente diseñada como un medio para la inferencia causal.

**Métrica Primaria:** Forma de medir el rendimiento del producto que se está probando en A/B testing, tanto para los grupos experimentales como para los de control. Se utiliza para identificar si hay una diferencia estadísticamente significativa entre estos dos grupos.

**Prueba de hipótesis / hipótesis estadística:** Procedimiento estadístico que se utiliza para determinar si existe una diferencia significativa entre los datos observados y los datos esperados. Herramienta estadística que sirve para aceptar o rechazar con confianza estadística una hipótesis obtenida en una muestra.

**Hipótesis Nula (H0):** Las ventas en ambas páginas son estadísticamente iguales (Tasa de conversión página A = Tasa de conversión página B).

**Hipótesis Alternativa (H1):** Las ventas en ambas páginas son significativamente diferentes (Tasa de conversión página A $\neq$ Tasa de conversión página B).

**Alpha:** Parámetro obtenido a partir del nivel de confianza (NC); Alpha = 1 - NC. Se utiliza para controlar el riesgo de error en la conclusión del test de hipótesis.

**p-valor (pValor):** Dato devuelto por el software al aplicar el estadístico de contraste. Si pValor es menor que Alpha entonces se puede rechazar H0; si el pValor es mayor o igual que Alpha entonces NO se puede rechazar H0.

**Unidad de randomización (randomization unit):** Nivel o entidad a la que se aplica la aleatorización en un experimento. También conocidas como unidades de diversificación. Define quién o qué se asigna aleatoriamente a cada variante de una prueba A/B.

**Ratio de Conversión:** $\text{Ratio de Conversión} = \frac{\text{Número de Conversión}}{\text{Número de Visitantes}} \times 100\%$

**Click To Rate (CTR):** $\text{Click To Rate (CTR)} = \frac{\text{Número de Clicks}}{\text{Número de apariciones}} \times 100\%$
