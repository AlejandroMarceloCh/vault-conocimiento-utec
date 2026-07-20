---
curso: ACD
titulo: [2025] U4_T1 Ingeniería de Características
slides: 13
fuente: [2025] U4_T1 Ingeniería de Características.pdf
---

Ingeniería de Características

      DS3021 Análisis Computacional de Datos




                                        Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Comprender e identificar la importancia
                     de la ingeniería de características en
                     Ciencia de Datos.
1.
     Ingeniería de
     Características
               Ingeniería de Características
La ingeniería de características es un proceso esencial en el preprocesamiento de datos para
mejorar la calidad y la relevancia de las características utilizadas en un modelo de machine
learning. Este proceso puede involucrar la extracción de características a partir de datos brutos,
la selección de características relevantes y la eliminación de las no relevantes, y la creación de
nuevas características a partir de características existentes.
  Tipos de Ingeniería de Características



                   1                                          2


 Preprocesamiento de características            Generación de características
       (Feature preprocessing)                     (Feature generation)

Consiste en transformar y actualizar las   Consiste en crear nuevas características
características existentes.                a partir de los datos existentes.
                                            Importancia de la
                                       Ingeniería de Características

                                                        Mejora de desempeño
                                                        Las características bien diseñadas
                                                        pueden elevar la precisión y
                                                        eficiencia del modelo.




Manejo de datos ruidosos                                                      Captura de patrones específicos
Ayuda a identificar y eliminar                                                Facilita la identificación de patrones
información irrelevante o ruido,                                              no evidentes en las características
mejorando la calidad de los datos.                                            originales.




               Adaptación al modelo
                                                                                     Interpretación y comprensión
               Ajusta características para satisfacer
                                                                                     Características bien diseñadas hacen
               requisitos específicos de ciertos
                                                                                     el modelo más interpretable.
               algoritmos.
         Retos que plantea
    la ingeniería de caraterísticas

     La recopilación de datos es el proceso de agrupar todos los datos que se necesitan
1    para el machine learning. Dicho proceso puede resultar tedioso, ya que los datos
     residen en muchos orígenes de datos, incluidos portátiles, almacenamientos de
     datos, la nube, aplicaciones y dispositivos.


     El etiquetado de datos es el proceso para identificar los datos sin procesar

2    (imágenes, archivos de texto, videos, etc.) y agregar una o más etiquetas significativas
     e informativas para proporcionar contexto, de manera que un modelo de machine
     learning pueda aprender de estos.


     Una vez que los datos están limpios y etiquetados, los equipos de machine learning a
     menudo los exploran para asegurarse de que son correctos y están listos para el
3    machine learning. Las visualizaciones como histogramas, gráficos de dispersión,
     gráficos de caja, gráficos de línea y gráficos de barra son herramientas útiles para
     confirmar que los datos son correctos.
2.
 Técnicas de ingeniería
 de características
Técnicas de Ingeniería de Características
                               Es el proceso de convertir un tipo de característica en otra
 Transformación de             forma más legible para un modelo en particular. Esto
   características             consiste en transformar datos continuos en datos
                               categóricos, o viceversa.




        Discretización (binning)                              Codificación one-hot

 Transforma los valores numéricos                   Es lo contrario de la discretización. Crea
 continuos      en       características            características numéricas a partir de
 categóricas. Compara cada valor con                variables     categóricas       asignando
 los valores vecinos que lo rodean y                características       categóricas        a
 luego ordena los puntos de datos en                representaciones binarias en una matriz
 varios segmentos o intervalos (bins).              o espacio vectorial.
Técnicas de Ingeniería de Características
                              Es una técnica de estandarización para cambiar la escala
    Escalado de               de características y limitar el impacto de las escalas
   características            grandes en los modelos.




       Escalado mínimo-máximo                          Escalado de la puntuación Z

 Reescala todos los valores de una
                                                 Reescala las características para que
 característica determinada para que se
                                                 tengan   una     desviación   estándar
 sitúen entre los valores mínimo y
                                                 compartida de 1 con una media de 0.
 máximo especificados, a menudo 0 y 1.
Técnicas de Ingeniería de Características
                                Es una técnica para crear un nuevo espacio dimensional
    Extracción y
                                para un modelo mediante la combinación de variables en
    selección de                nuevas variables sustitutas o para reducir las dimensiones
   características              del espacio de características del modelo.




   Análisis de componentes principales                   Análisis discriminatorio lineal
                  (PCA)                                               (LDA)
 Método común de extracción de                     Método que proyecta los datos del
 características   que      combina      y         modelo en un nuevo espacio de menor
 transforma las características originales         dimensionalidad, produciendo variables
 de un conjunto de datos para producir             de     componentes      principalmente
 nuevas características o variables                destinadas a maximizar la diferencia de
 llamadas componentes principales.                 clase en los datos.
Técnicas de Ingeniería de Características

 Transformación de   Convierte datos entre formatos continuos y categóricos
   características   para mejorar la comprensión del modelo.



   Escalado de       Estandariza las características para reducir el efecto de
  características    escalas desiguales en los modelos.



   Extracción y      Transforma o reduce el espacio de características
   selección de      mediante la combinación de variables para mejorar el
  características    rendimiento del modelo.
U4_L1 Ingeniería de Características

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
