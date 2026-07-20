---
curso: ML
titulo: Solucionario_Examen_Parcial
slides: 5
fuente: Solucionario_Examen_Parcial.pdf
---

Universidad de Ingeniería y Tecnología
Examen Parcial - Machine Learning 2026-I
Docente: Manuel Eduardo Loaiza Fernández
Descripción: Solucionario a las preguntas del examen

I. Fundamentos básicos (3 puntos)

1. Un modelo de regresión lineal presenta un error de entrenamiento muy bajo y un error de
prueba extremadamente alto. ¿Qué escenario describe mejor este comportamiento?
a) Underfitting
b) Overfitting
c) Data leakage
d) Feature scaling

Justificación: Un error de entrenamiento muy bajo combinado con un error de prueba
extremadamente alto indica que el modelo memorizó los datos de entrenamiento incluyendo
su ruido, perdiendo la capacidad de generalizar a datos nuevos.

2. En regresión logística binaria, la función sigmoide se utiliza principalmente para:
a) Reducir el número de características (features)
b) Convertir una salida lineal en una probabilidad
c) Eliminar outliers
d) Aplicar regularización automática

Justificación: La función sigmoide transforma la salida lineal ∈ (−∞, +∞) en un valor σ(z)
∈ (0, 1), permitiendo interpretarlo como una probabilidad de pertenencia a la clase positiva.
3. El resultado σ(z) se interpreta directamente como la probabilidad de que la muestra
pertenezca a la clase 1, y la clasificación se decide con un umbral (típicamente 0.5).

3. Un hiperplano posee una normal esta normal se puede usar para:
a) Medir el tamaño del hiperplano dentro del universo de muestra
b) Para medir la distancia entre los support vectors y los otros elementos dentro de la
clase
c) Eliminar outliers que están fuera del hiperplano
d) Aplicar regularización automática a los elementos fuera del hiperplano

Justificación: El vector normal al hiperplano permite calcular la distancia perpendicular de
cualquier punto, en particular de los support vectors , al hiperplano separador, lo que define
el margen que SVM busca maximizar.

II. Regresión Lineal (6 puntos)

En este pregunta, cada alumno tuvo datos para operar que generan diferentes resultados
individualmente, por ese motivo la forma de calificar fue siguiendo lo siguientes criterios:

Criterios:
    1)​ Normalización z-score y construcción de la matriz X. (2 puntos)
           a)​ Completa la siguiente tabla de normalización. La columna x0 = 1 para
               todos los ítems.
               Se validó el nivel de desarrollo de esta pregunta basado en el concepto de
               normalización, completar la tabla y los cálculos que podían colocarse en el
               cálculo de verificación fue llevado en consideración en la puntuación de la
               pregunta.
           b)​ Verificación: para el ítem 1 de tu dataset, muestra el cálculo explícito de
               x1_n:
               Se validó el desarrollo básico de los cálculos en un ítem de la muestra que se
               normalizo.

   2)​ Gradient Descent — 5 iteraciones (2 puntos)
          a)​ Para cada iteración muestra: los valores de y_hat, error y gradiente para
              al menos 2 ítems (el primero y el último). Completa la tabla resumen:
              Se validó el nivel de desarrollo de esta pregunta basado en el concepto de
              seguir el desarrollo del algoritmo de Gradiente Descendiente en base al
              pseudocódigo que se brindó de apoyo en el enunciado del examen.
              Completar la tabla cumpliendo las iteraciones requeridas y realizar el cálculo
              del MSE a cada iteración para validar el comportamiento del modelo de
              regresión lineal. Esto fue evaluado en base a la muestra de ítems que se le
              asignaron a cada alumno.
          b)​ ¿El MSE disminuye de forma consistente en las 5 iteraciones? ¿Qué
              concluyes sobre la elección de lr = 0.05 para este dataset?:
              Se validó la respuesta basado en el comportamiento del MSE calculado en la
              pregunta anterior, considerando que la muestra de ítems que se le asignaron
              a cada alumno tienen comportamientos diferentes en la evolución del MSE.

   3)​ Cálculo de R² con los pesos de la iteración 5. (2 puntos)
          a)​ Calcula y_hat para los 8 ítems con los w de la iteración 5, luego calcula
              SS_res, SS_tot y R². Muestra cada paso:
              Se validó el nivel de desarrollo de esta pregunta basado en el concepto del
              coeficiente de determinación “R²”, en base al cual podemos interpretar el
              grado de interpretación y predicción de nuestro modelo ante el entrenamiento
              que se realizó.
          b)​ Interpretación: observando la evolución del MSE en las 5 iteraciones,
              ¿el modelo está convergiendo? ¿El “R²” obtenido con 5 iteraciones
              refleja la calidad real del modelo? ¿Qué esperas si ejecutas 50
              iteraciones más?:
              Se validó el entendimiento e interpretación del MSE en las diferentes
              iteraciones, en algunos casos se aceptaron hasta 3 iteraciones en donde se
              vea la evolución del MSE a cada iteración. Con pocas iteraciones validar el
              comportamiento del coeficiente “R²” también fue fundamental para responder
              , según sus datos, como sería el comportamiento futuro en 50 iteraciones.

III. Regresión No Lineal (6 puntos)

En este pregunta, cada alumno tuvo datos para operar que generan diferentes resultados
individualmente, por ese motivo la forma de calificar fue siguiendo lo siguientes criterios:
   1)​ Feature engineering — calcular y normalizar área². (2 puntos)
          a)​ Completa la columna x4_n en la siguiente tabla:
              Se validó el nivel de desarrollo de esta pregunta basado en el concepto de
              ver como variaba el comportamiento de la variable asignada al parámetro de
              área, que era una de las características nuevas a ser consideradas en el
              modelo. Tanto su adaptación no lineal y su normalización nos dan indicios de
              cómo puede contribuir este nuevo parámetro en el entrenamiento de nuestro
              modelo.
   2)​ Gradient Descent — 5 iteraciones con X extendida. (2 puntos)
          a)​ Muestra el desarrollo completo de la iteración 1. Para las iteraciones 2 a
              5 muestra únicamente el gradiente y la actualización de w. Completa la
              tabla resumen:
              Se validó el nivel de desarrollo de esta pregunta basado en el concepto de
              seguir el desarrollo del algoritmo de Gradiente Descendiente pero ahora para
              el modelo incluyendo la variable no lineal como el área. Se brindó el
              pseudocódigo de apoyo en el enunciado del examen para aplicar el algoritmo
              en el modelo considerando la nueva variable x4 y su peso w4
              correspondiente. Completar la tabla cumpliendo las iteraciones requeridas y
              realizar el cálculo del MSE a cada iteración para validar el comportamiento
              del modelo de regresión no lineal. Esto fue evaluado en base a la muestra de
              ítems que se le asignaron a cada alumno.
          b)​ Analiza el peso w4 obtenido en la iteración 5. ¿Es positivo o negativo?
              ¿Qué significa económicamente ese signo en el contexto del precio de
              una vivienda? :
              Se validó el nivel de desarrollo de esta pregunta basado en el signo que el
              peso w4 y su interpretación sobre el problema analizado que es el precio de
              una vivienda. Positivo contribuye y negativo no contribuye con la predicción
              del precio final del inmueble

   3)​ Cálculo de “R²” y comparación con el modelo lineal. (2 puntos)
          a)​ Con los pesos de la iteración 5 del modelo no lineal, calcula “R²”.
              Completa la tabla comparativa:
              Se validó el nivel de desarrollo de esta pregunta basado en el desarrollo y
              cálculo del coeficiente “R²” tanto para el modelo lineal y no lineal. Se
              consideró en la calificación la interpretación entre ambos casos, si no se
              pudo culminar el cálculo de alguno de los modelos esta pregunta no podría
              ser completada de forma adecuada.
          b)​ ¿Por qué el MSE del modelo no lineal baja más rápido que el del modelo
              lineal en las primeras iteraciones? Explica en términos del gradiente y
              de la varianza adicional que captura la feature x4:
              Se validó el nivel de desarrollo de esta pregunta basado en el
              comportamiento de la variable x4 y su interpretación del comportamiento del
              MSE, en donde esta variable nueva en el modelo no lineal afectaba la
              convergencia del modelo no lineal comparado al modelo lineal.


IV. Preguntas Teóricas (5 puntos)
Responde de manera breve y precisa. Justifica con conceptos del curso.

1. ¿Por qué es imprescindible normalizar los datos antes de aplicar Gradient
Descent? Explica qué ocurriría con los gradientes y la convergencia si las variables
tuvieran escalas muy distintas (por ejemplo, área en m² vs. antigüedad en años).

Sin normalización, las variables de mayor escala dominan el gradiente, obligando a usar un
learning rate (lr) muy pequeño que hace lenta la convergencia de las variables de menor
escala. Con z-score todas las características (features) contribuyen proporcionalmente al
gradiente y el algoritmo de Gradiente Descendiente (GD) converge de forma eficiente.

2. Observa la evolución del MSE en las Partes I y II de tu examen. ¿En cuál de los dos
modelos baja más rápido el MSE en las primeras iteraciones? ¿A qué lo atribuyes?
Relaciona tu respuesta con el concepto de varianza explicada por cada feature.

Esta respuesta depende de los resultados obtenidos en cada uno de los casos individuales
asignados al estudiante en la parte I y II del examen. En la mayoría de los casos el MSE del
modelo de regresión no lineal converge mucho más rápido que el modelo lineal. El
parámetro que mejor contribuye a este cambio es el área del terreno que al tener mejor
definido su comportamiento no lineal sustenta a través de su varianza una caída mas rapida
del MSE.

3. El modelo de regresión logística produce como salida un valor y ∈ [0, 1]. ¿Por qué
este rango lo hace adecuado para modelar probabilidades de clase? ¿Qué ocurriría si
en cambio usáramos una regresión lineal (sin sigmoide) para predecir directamente 0
o 1?

La sigmoide garantiza σ(z) ∈ (0,1) cumpliendo los axiomas de probabilidad que son: nunca
puede ser negativa y nunca puede superar 1. Esto permite interpretar la salida como
P(y=1|x), osea la probabilidad de que ese ítem pertenezca a la clase positiva. La regresión
lineal no tiene esta restricción y produce valores fuera de rango sin interpretación
probabilística válida, además de hacer inadecuada la función de costo MSE para variables
binarias.

4. En el ejemplo de clasificación de insectos, con antena = 3 la probabilidad de ser
Grasshopper es 0.833 y con antena = 5 ambas clases tienen probabilidad 0.500. ¿Qué
representa matemáticamente el punto donde ambas probabilidades son iguales?
¿Qué relación tiene con la frontera de decisión del modelo?

El punto donde ambas probabilidades son 0.5 corresponde matemáticamente a z = 0, es
decir w·x + b = 0, que define la frontera de decisión del modelo. A un lado σ(z) > 0.5 y el
modelo predice clase 1; al otro σ(z) < 0.5 y predice clase 0. Es el límite geométrico que
separa ambas regiones de clasificación. Cuando σ(z) = 0.5 el modelo no tiene evidencia
suficiente para inclinarse hacia ninguna clase y la probabilidad de ser cualquiera de las dos
es idéntica. Esto ocurre únicamente cuando z = 0 debido a que:
σ(0) = 1 / (1 + e^0) = 1 / 2 = 0.5.
5. Un sistema de detección de fraude bancario produce la siguiente matriz de
confusión: TP=10, TN=980, FP=5, FN=5. Calcula accuracy, precision, recall y F1-score.
A pesar de tener un accuracy muy alto, ¿por qué este modelo podría considerarse
deficiente para este problema? ¿Qué métrica priorizarías y por qué?

Total = TP + TN + FP + FN = 10 + 980 + 5 + 5 = 1000

Accuracy = (TP + TN) / Total = (10 + 980) / 1000 = 990/1000 = 0.990 (99.0%)
Precision = TP / (TP + FP)   = 10 / (10 + 5)   = 10/15 = 0.667 (66.7%)
Recall = TP / (TP + FN)     = 10 / (10 + 5)   = 10/15 = 0.667 (66.7%)
F1 Score = 2·P·R / (P + R)   = 2·0.667·0.667 / (0.667+0.667) = 0.667 (66.7%)

El accuracy alto es engañoso porque el dataset está desbalanceado y la mayoría son
transacciones legítimas, por lo que predecir siempre “no fraude” ya da 99% de accuracy. La
métrica relevante es Recall, porque en detección de fraude el costo de un FN (fraude no
detectado) supera ampliamente el de un FP (alarma falsa). Con Recall = 0.667 el modelo
falla en detectar la mitad de los fraudes reales, lo que lo hace deficiente para este problema.
