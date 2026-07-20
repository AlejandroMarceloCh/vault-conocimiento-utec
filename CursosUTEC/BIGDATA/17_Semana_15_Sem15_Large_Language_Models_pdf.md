---
curso: BIGDATA
titulo: 17 - Semana 15/Sem15_Large Language Models
slides: 44
fuente: 17 - Semana 15/Sem15_Large Language Models.pdf
---

LLM y Optimización
Mg. Aldo Lezama Benavides


Semana 15
       Objetivo de la sesión

1. Comprender los fundamentos de los Large Language Models (LLM), su
   arquitectura Transformer y las características que les permiten procesar
   y generar lenguaje natural.
2. Analizar las principales técnicas de optimización de LLM, incluyendo
   Knowledge Distillation, Quantization y Pruning, identificando su
   funcionamiento y objetivos.
3. Evaluar el impacto de las técnicas de compresión de modelos en la
   reducción del consumo de memoria, el costo computacional y la latencia
   de inferencia, manteniendo un rendimiento competitivo.
                 Contenido de la sesión

    01.              02.            03.          04.

Large Language
                   Distillation   Quantization   Pruning
    Models
01.   Large Language Models
                                Large Language Models
Un Large Language Model (LLM) es un modelo de inteligencia
artificial entrenado sobre enormes volúmenes de texto con el
objetivo de comprender y generar lenguaje natural.


Los LLMs están basados en arquitecturas Transformer y utilizan
miles de millones de parámetros para aprender patrones
lingüísticos, relaciones semánticas y conocimiento general
contenido en grandes colecciones de documentos.


A diferencia de los modelos tradicionales de Machine Learning,
los LLMs no siguen reglas predefinidas. En su lugar, aprenden
representaciones estadísticas del lenguaje a partir de grandes
cantidades de datos.
                                Large Language Models


Características principales
• Aprenden a partir de grandes corpus de texto.
• Comprenden el contexto de una conversación.
• Generan texto coherente y fluido.
• Pueden resolver múltiples tareas sin necesidad de entrenar
  un modelo diferente para cada una.
                             Arquitectura Transformer
La mayoría de los modelos modernos, como GPT, Llama y Mistral, utilizan
la arquitectura Transformer, propuesta en 2017.
Sus componentes principales son:
Embeddings
Transforman las palabras o tokens en vectores numéricos.
Self-Attention
Permite que cada palabra analice la importancia de todas las demás
palabras de la oración.
Feed Forward Network (FFN)
Procesa la información obtenida por la atención mediante una red neuronal
completamente conectada.
Capas Transformer
Estos bloques se repiten decenas o cientos de veces para construir
modelos de gran capacidad.
                           Millones de parámetros

Los parámetros son los pesos que la red neuronal aprende durante el
entrenamiento y representan el conocimiento almacenado por el
                                                                        Modelo       Parámetros
modelo.
A mayor cantidad de parámetros:                                       BERT Base      110 millones
• mayor capacidad de aprendizaje;
                                                                      GPT-2 Large    774 millones
• mejor representación del lenguaje;
• mayor consumo de memoria;                                           Llama 3 8B    8 mil millones
• mayor costo computacional;
• mayor tiempo de inferencia.                                         Llama 3 70B   70 mil millones

No obstante, un mayor número de parámetros no garantiza siempre
mejores resultados. Modelos más pequeños y bien optimizados pueden
ofrecer un rendimiento comparable en tareas específicas.
                          Necesidad de optimización

Los LLMs modernos requieren enormes recursos computacionales. Por ejemplo, un modelo de varios miles de
millones de parámetros puede necesitar decenas o cientos de gigabytes de memoria para ejecutarse en formato
FP32. Esto genera varios desafíos:
• alto consumo de memoria;
• elevada latencia de inferencia;
• mayor consumo energético;
• altos costos de infraestructura;
Para resolver estos problemas se emplean técnicas de compresión de modelos, entre ellas:
• Pruning: elimina conexiones o parámetros poco relevantes.
• Quantization: reduce la precisión numérica de los parámetros.
• Knowledge Distillation: transfiere el conocimiento de un modelo grande a uno más pequeño.
02.   Distillation
                        ¿Qué es Knowledge Distillation?
La Knowledge Distillation (KD) es una técnica de compresión de
modelos en la que un modelo grande y complejo, denominado
Teacher, transfiere su conocimiento a un modelo más pequeño
y eficiente, denominado Student.


El objetivo no es copiar exactamente los parámetros del modelo
grande, sino aprender su comportamiento, permitiendo que el
modelo pequeño alcance un rendimiento similar con muchos
menos recursos computacionales.


Idea clave
Distillation no comprime directamente el modelo; aprende una
versión compacta de la función que el modelo grande ha
aprendido.
                        Arquitectura Teacher–Student
                                y Aprendizaje

En lugar de aprender únicamente la respuesta correcta,
el Student aprende las probabilidades completas que
produce el Teacher.


Estas probabilidades contienen información rica sobre la
relación entre las distintas respuestas posibles. El
Student aprende no solo qué respuesta es correcta, sino
también qué respuestas son similares o plausibles según
el Teacher.
                            Función de pérdida en Distillation

El entrenamiento busca minimizar la diferencia entre las predicciones
del Student y las del Teacher.
1. Cross-Entropy Loss
Compara las predicciones del Student con las etiquetas reales.
Objetivo: aprender la respuesta correcta.
2. KL Divergence
Compara las probabilidades generadas por el Student con las del
Teacher.
Objetivo: que el Student imite el comportamiento del Teacher.
3. Pérdida Combinada (la más utilizada)
Combina Cross-Entropy + KL Divergence
Objetivo: aprender tanto de las etiquetas reales como del
conocimiento del Teacher.
              Ventajas                                       Aplicaciones



Reduce      significativamente   el   número   de   Versiones compactas de modelos GPT.
parámetros.                                         Asistentes virtuales.
Disminuye el consumo de memoria.                    Chatbots empresariales.
Reduce el costo de inferencia.                      Modelos para smartphones.
Mejora la velocidad de respuesta.                   Sistemas de búsqueda y recomendación
Facilita el despliegue en dispositivos Edge y
móviles..
                       Casos de Knowledge Distillation
Modelo Teacher   Modelo Student     Parámetros        Reducción                    Rendimiento aproximado


                                                      40% menos        Conserva aproximadamente 97% del rendimiento de
  BERT Base        DistilBERT      110 M → 66 M
                                                      parámetros          BERT y es ~60% más rápido en inferencia.


                                                     ≈96% menos      Mantiene entre 96% y 97% del rendimiento de BERT en
 BERT Large        TinyBERT        340 M → 14.5 M
                                                      parámetros                     múltiples tareas NLP.


                                                                      Conserva alrededor del 99% del desempeño en tareas
                                                     ≈77% menos
  BERT Base       MobileBERT       110 M → 25 M                        de comprensión del lenguaje y ofrece una inferencia
                                                      parámetros
                                                                           mucho más rápida en dispositivos móviles.

                                                                       Conserva más del 99% del rendimiento en tareas de
                                                     ≈91% menos
RoBERTa Large       MiniLM         355 M → 33 M                      recuperación y comprensión del lenguaje, siendo varias
                                                      parámetros
                                                                                      veces más rápido.

                                                                      Mantienen buena calidad para tareas específicas,
                  Modelos GPT
                                                    Más del 90% de reduciendo significativamente el costo de inferencia. No
    GPT-3           destilados     175 B → 1–13 B
                                                      reducción     existe una versión oficial destilada de GPT-3 publicada
                 (investigación)
                                                                                          por OpenAI.
03.   Quantization
                                          Quantization
Es una técnica de compresión de modelos que consiste en reducir la
precisión numérica utilizada para representar los pesos y las
activaciones de una red neuronal. En lugar de almacenar los
parámetros utilizando números de alta precisión, como 32 bits, se
emplean representaciones de menor precisión, como 16, 8 o incluso
4 bits. La cuantización no elimina parámetros ni modifica la
arquitectura del modelo. Todos los pesos permanecen presentes;
únicamente cambia la forma en que son representados en memoria.
El objetivo principal es disminuir el consumo de memoria, reducir el
costo computacional y acelerar la inferencia, manteniendo una
pérdida mínima de precisión.
Idea clave: La Quantization no reduce el número de parámetros;
reduce el número de bits utilizados para representar cada parámetro.
                        ¿Por qué funciona la Quantization?

Durante el entrenamiento, los pesos de una red neuronal se
almacenan normalmente en formato Float32 (32 bits). Sin embargo,
numerosos estudios han demostrado que no siempre es necesario
utilizar una precisión tan elevada para realizar inferencias.
Al reducir la cantidad de bits por parámetro:
• disminuye el tamaño del modelo;
• se reduce el tráfico de memoria;
• aumentan las operaciones por segundo que puede realizar el
  hardware.
La mayoría de procesadores modernos (CPU, GPU y aceleradores
de IA) incorporan instrucciones optimizadas para operaciones en
INT8, lo que permite ejecutar los modelos significativamente más
rápido.
       Comparación de Métodos de Quantization




Post-Training Quantization (PTQ)                                        Quantization-Aware Training (QAT)
La cuantización se aplica después de que el modelo ha sido entrenado.   Durante el entrenamiento se simula el efecto de la cuantización.
No requiere volver a entrenar la red.                                   El modelo aprende desde el inicio a trabajar con baja precisión.
Es rápida y sencilla de implementar.                                    Ventaja
Ventaja                                                                 Generalmente consigue mayor precisión que PTQ.
Ideal cuando ya se dispone de un modelo entrenado.                      Desventaja
                                                                        Requiere volver a entrenar el modelo.
                                Proceso de Quantization

Etapa 1: Modelo entrenado (FP32)
El proceso de cuantización parte de un modelo previamente entrenado, cuyos pesos y activaciones se encuentran
representados normalmente en formato Float32 (FP32). Esta representación utiliza 32 bits por cada parámetro,
proporcionando una alta precisión numérica durante el entrenamiento.
Aunque FP32 ofrece excelentes resultados, también implica un elevado consumo de memoria y una mayor cantidad de
operaciones aritméticas durante la inferencia. Por esta razón, el modelo constituye el punto de partida para aplicar
técnicas de cuantización que reduzcan estos requerimientos sin modificar la arquitectura de la red neuronal.

                                Proceso de Quantization

Etapa 2: Análisis del rango de valores
En esta etapa se analiza la distribución de los pesos y activaciones del modelo para determinar los valores mínimo y
máximo que deberán representarse con menor precisión.Este análisis permite conocer el rango real de los datos y definir
cómo serán transformados al nuevo formato numérico. En algunos métodos también se emplean percentiles para evitar
que valores atípicos (outliers) afecten la calidad de la cuantización. El objetivo es conservar la mayor cantidad posible de
información utilizando un rango de representación mucho más reducido.
                                Proceso de Quantization

Etapa 3: Cálculo del factor de escala (Scale) y punto cero (Zero Point)
Una vez conocido el rango de valores, se calculan dos parámetros fundamentales:
• Scale (factor de escala): determina la relación entre los valores reales y los valores enteros que representarán esos
  datos.
• Zero Point (punto cero): establece qué valor entero representa el cero en la nueva escala numérica.
Estos parámetros permiten transformar los números de punto flotante (FP32) en valores enteros (INT8, INT4, etc.)
preservando, en la medida de lo posible, la información contenida en los pesos originales.
                               Proceso de Quantization

Etapa 4: Cuantización (Conversión)
En esta etapa se realiza la conversión propiamente dicha. Cada peso y activación del modelo se transforma desde su
representación en punto flotante (FP32) hacia una representación de menor precisión, como INT8 o INT4. Durante este
proceso, los valores son escalados y redondeados al entero más cercano dentro del rango permitido. Como
consecuencia, el modelo ocupa considerablemente menos memoria y puede ejecutarse utilizando operaciones enteras,
que son mucho más eficientes en la mayoría del hardware moderno. Aunque esta conversión introduce una pequeña
pérdida de precisión numérica, generalmente el impacto sobre el rendimiento del modelo es reducido.
                                Proceso de Quantization

Etapa 5: Ejecución en baja precisión
Una vez cuantizado, el modelo realiza la inferencia utilizando operaciones de baja precisión, como INT8 o INT4, en lugar
de operaciones de punto flotante. Esto permite disminuir significativamente el tiempo de ejecución, el consumo energético
y el uso de memoria. Además, muchos procesadores modernos incorporan aceleradores especializados para
operaciones enteras, lo que incrementa aún más la velocidad de inferencia. Esta etapa es especialmente importante en
aplicaciones donde se requiere responder en tiempo real o ejecutar modelos en dispositivos con recursos limitados
                              Proceso de Quantization

Etapa 6: Validación
Después de la cuantización, es necesario evaluar el comportamiento del modelo para verificar que la reducción de
precisión no haya afectado significativamente su desempeño. Para ello, se comparan métricas como la precisión
(Accuracy), la pérdida (Loss), la latencia y el consumo de memoria respecto al modelo original. Si la pérdida de
rendimiento se encuentra dentro de un margen aceptable, el modelo cuantizado puede utilizarse en producción. En caso
contrario, será necesario ajustar el proceso de cuantización o emplear técnicas más avanzadas, como Quantization-
Aware Training (QAT).
                                Proceso de Quantization

Etapa 7: Modelo cuantizado listo para despliegue
La etapa final consiste en obtener un modelo optimizado para su utilización en entornos de producción. El modelo
mantiene la misma arquitectura y realiza exactamente la misma tarea que el modelo original, pero requiere menos
memoria, consume menos energía y ejecuta la inferencia con mayor rapidez. Gracias a estas características, la
cuantización se ha convertido en una técnica fundamental para desplegar Large Language Models (LLMs) en servidores,
computadoras personales, dispositivos móviles y sistemas embebidos, permitiendo reducir los costos de infraestructura
sin comprometer significativamente la calidad de las predicciones.
Flujo de Proceso de Quantization
                                    Ventajas y limitaciones


VENTAJAS                                                   LIMITACIONES


• Reduce considerablemente el tamaño del modelo.           • Puede disminuir ligeramente la precisión.

• Disminuye el consumo de memoria.                         • Algunos modelos son más sensibles que otros a la

• Acelera la inferencia.                                     reducción de precisión.

• Reduce el consumo energético.                            • La mejora en velocidad depende del hardware

• Facilita el despliegue en dispositivos móviles y Edge.     disponible.

• No modifica la arquitectura de la red neuronal           • Cuantizaciones muy agresivas (INT4 o INT2) pueden
                                                             degradar significativamente el rendimiento.
04.   Pruning
                          Pruning en Modelos de Lenguaje
Los modelos de lenguaje actuales contienen miles de millones de
parámetros. Aunque esta enorme cantidad de parámetros les
permite aprender relaciones muy complejas, también provoca que:
• ocupen mucha memoria;
• requieran gran capacidad de procesamiento;
• consuman más energía;
• tengan mayor costo de inferencia
Sin embargo, numerosos estudios han demostrado que no todos
los parámetros son igualmente importantes. Muchos contribuyen
muy poco a la predicción final.
Idea clave:
Si eliminamos los parámetros poco importantes, el modelo puede
seguir   funcionando    casi      igual,   pero   con   menor   costo
computacional.
                                     ¿Qué es el Pruning?

Pruning (poda) consiste en eliminar conexiones, pesos o
incluso neuronas que aportan muy poca información al
modelo.
La idea proviene de la jardinería.
Así como se poda un árbol para eliminar ramas
innecesarias y permitir que crezca de manera más
eficiente, en una red neuronal se eliminan conexiones
redundantes
No se agregan parámetros nuevos.
Simplemente se eliminan los menos útiles.
                 ¿Cómo decide el algoritmo qué eliminar?
Una de las preguntas más importantes en el proceso de Pruning es determinar qué parámetros pueden eliminarse sin
afectar significativamente el rendimiento del modelo. Aunque una red neuronal puede contener millones o incluso miles
de millones de pesos, no todos contribuyen de igual manera a la generación de las predicciones. Algunos parámetros
capturan patrones fundamentales de los datos, mientras que otros tienen una influencia muy reducida y resultan
prácticamente redundantes.


El objetivo del algoritmo de Pruning es asignar un nivel de importancia a cada peso o conjunto de pesos. Aquellos
considerados poco relevantes serán candidatos para su eliminación. Existen diversos métodos para medir esta
importancia, entre los cuales destacan los siguientes:


a) Magnitud del peso (Weight Magnitude)
b) Sensibilidad del modelo
c) Gradientes
d) Métodos basados en importancia estructural
Pruning - Magnitud del peso
                  Pruning – Sensibilidad del modelo

En este enfoque, la importancia de un peso se mide evaluando cuánto cambia el rendimiento del modelo cuando
dicho parámetro es eliminado.


Si al eliminar un peso la función de pérdida (Loss Function) apenas aumenta, significa que ese parámetro tiene poca
relevancia para la tarea y puede eliminarse con un impacto mínimo. En cambio, si su eliminación provoca un
incremento considerable del error, el peso debe conservarse.


Aunque este método suele producir mejores resultados que el criterio basado únicamente en la magnitud, requiere
realizar un mayor número de evaluaciones, incrementando el costo computacional.
                              Pruning – Gradientes

Otra estrategia consiste en analizar el gradiente
asociado a cada peso durante el entrenamiento.
El gradiente indica cuánto contribuye un parámetro a
la reducción del error del modelo. Cuando un peso
presenta gradientes muy pequeños durante varias
iteraciones, significa que modificar dicho parámetro
apenas mejora el aprendizaje, por lo que puede
considerarse un candidato para el Pruning.
Este enfoque incorpora información sobre el proceso
de entrenamiento y permite identificar parámetros
que, aunque no sean pequeños en magnitud, tienen
poca influencia en la optimización del modelo.
                        Pruning – Métodos basados
                        en importancia estructural
En los modelos Transformer utilizados por los LLMs, el análisis no siempre se realiza sobre pesos individuales. En
muchos casos se calcula la importancia de componentes completos, tales como:


• Cabezas de atención (Attention Heads).
• Neuronas de la red Feed Forward (FFN).
• Capas Transformer.
• Bloques completos del modelo.


Si un componente aporta poca información durante la inferencia, puede eliminarse por completo. Este tipo de
evaluación es especialmente útil cuando el objetivo es acelerar la ejecución del modelo en hardware especializado.
                                    Tipos de Pruning


Existen   diversas   formas    de   realizar   el   Pruning,
dependiendo del nivel de la red neuronal sobre el que se
aplique la eliminación de parámetros.
En términos generales, las técnicas de poda se clasifican
en:


❑ Pruning no estructurado (Unstructured Pruning) y
❑ Pruning estructurado (Structured Pruning).


La principal diferencia entre ambas radica en si se eliminan
pesos individuales o estructuras completas de la red.
                                Unstructured Pruning


El   Unstructured   Pruning   elimina   pesos     individuales
considerados      poco   importantes,   sin     modificar   la
arquitectura general del modelo. Es decir, las neuronas y
capas permanecen intactas, pero algunas conexiones
entre ellas desaparecen.


Como resultado, la matriz de pesos se vuelve dispersa
(Sparse Matrix), ya que contiene numerosos valores
iguales a cero.
                                      Structured Pruning

El Structured Pruning elimina estructuras completas de la
red neuronal, en lugar de pesos individuales. Dependiendo
del modelo, estas estructuras pueden ser:
• Neuronas completas.
• Canales (Channels).
• Filtros en redes convolucionales.
• Cabezas de atención (Attention Heads).
• Capas Transformer.
• Bloques completos del modelo.
Al eliminar componentes enteros, la arquitectura del
modelo se simplifica de manera explícita, reduciendo tanto
el número de parámetros como la cantidad de operaciones
necesarias durante la inferencia.
                                  Flujo del Proceso de Pruning




Es la red neuronal completa,         El modelo aprende a partir de        Se evalúa la importancia de cada      Después del pruning, el modelo
con todos sus parámetros y           los datos ajustando sus pesos        peso mediante criterios como su       suele perder algo de precisión
conexiones. Ofrece el máximo         para minimizar el error y realizar   magnitud, gradiente o sensibilidad,   porque    se   han    eliminado
rendimiento,   pero     también      correctamente la tarea para la       identificando aquellos que aportan    conexiones que, aunque    poco
requiere   mayor   memoria    y      que fue diseñado.                    muy poco al resultado.                importantes, aún contribuían al
capacidad de cómputo.                                                                                           rendimiento.

                                  Flujo del Proceso de Pruning




Después del pruning, el modelo           Se reentrena el modelo podado utilizando los datos   Se   obtiene   un   modelo    más
suele perder algo de precisión           originales para recuperar la mayor parte de la       pequeño, con menos parámetros,
porque   se    han   eliminado           precisión perdida sin volver a aumentar su tamaño.   menor consumo de memoria y
conexiones que, aunque poco                                                                   menor     costo     computacional,
importantes, aún contribuían al                                                               manteniendo un rendimiento muy
rendimiento.                                                                                  cercano al modelo original.
             Ventajas                                        Desventajas
Menor tamaño del modelo                              Puede perder precisión
Hay menos parámetros que almacenar.                  Si se elimina demasiada información.


Menor cantidad de operaciones                        Requiere Fine-Tuning
Se realizan menos multiplicaciones.                  Normalmente no basta con eliminar parámetros.
Disminuyen los FLOPs.                                Debe reentrenarse.


Menor latencia                                       No siempre acelera la inferencia
La inferencia puede ejecutarse más rápidamente.      En hardware convencional, los pesos eliminados
Especialmente    con    lotes    pequeños   (batch   pueden seguir ocupando espacio lógico.
pequeño).                                            Por ello el hardware especializado aprovecha
                                                     mucho mejor el pruning estructurado.
Menor consumo energético
Al realizar menos operaciones, disminuye el
consumo eléctrico.
Muy útil en dispositivos Edge.
                      Conclusiones

01.
      Los LLMs ofrecen una gran capacidad para comprender y generar lenguaje natural,
      pero su elevado número de parámetros implica altos requerimientos de memoria,
      procesamiento y energía.




02.
      Knowledge Distillation, Quantization y Pruning son técnicas complementarias de
      optimización que permiten reducir el tamaño y el costo de los modelos sin afectar
      significativamente su desempeño.


      La optimización de LLMs es fundamental para su despliegue en entornos reales, ya
03.   que facilita la ejecución eficiente en servidores, dispositivos móviles y sistemas
      con recursos limitados.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
