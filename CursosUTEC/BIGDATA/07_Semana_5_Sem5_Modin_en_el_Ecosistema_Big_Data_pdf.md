---
curso: BIGDATA
titulo: 07 - Semana 5/Sem5_Modin en el Ecosistema Big Data
slides: 22
fuente: 07 - Semana 5/Sem5_Modin en el Ecosistema Big Data.pdf
---

Modin en el
Ecosistema Big Data
Mg. Aldo Lezama Benavides


Semana 5
    Objetivo de la sesión

Comprender qué es Modin y su rol en el ecosistema Big Data
Analizar cómo Modin permite manejar y procesar grandes
volúmenes de datos en Python
Reconocer las funciones de Pandas que Modin paraleliza para
mejorar rendimiento.
Identificar las ventajas de usar Modin sobre Pandas tradicional en
proyectos de Big Data.
               Contenido de la sesión

   01.               02.              03.              04.

Modin en Big       Funciones      Pandas vs Dask
                                                   Modin en GColab
   Data           paralelizadas     vs Modin
01.   Modin en Big Data
                           Modin en el ecosistema Big Data

El análisis de datos en Python a menudo comienza con Pandas, una librería
que ha simplificado enormemente la manipulación de datos tabulares. Su
                                                                                             df.rename
API intuitiva ha hecho de la limpieza, transformación y análisis de datos una
                                                                                                             df.describe
tarea accesible. Sin embargo, Pandas tiene una limitación fundamental: es       df.drop

una librería in-memory y de un solo hilo. Esto significa que solo puede
procesar datos que caben por completo en la memoria RAM de tu máquina,
y solo puede utilizar un único núcleo de tu procesador para realizar sus
                                                                                                         pd.merge
cálculos. Cuando trabajas con un dataset de 10 GB en una máquina con 8          df.groupby
GB de RAM, Pandas simplemente fallará. Y si la operación es muy pesada,                                             df.pivot
                                                                                              pd.join
como un groupby complejo en un dataset de 100 GB, te verás atrapado en
una espera interminable.
                              ¡El Cuello de Botella de Pandas:
                                  Cuando tus Datos Crecen

1. Limitación de Memoria (In-Memory)
Pandas debe cargar todo el conjunto de datos en la memoria RAM de tu
computadora para poder procesarlo. Si tu archivo es más grande que la
memoria disponible, Pandas no puede funcionar y generará un error
(MemoryError).


2. Limitación de Procesamiento (Un Solo Hilo)
Pandas utiliza un solo núcleo de tu CPU para ejecutar las operaciones. Aunque
tu máquina tenga 8, 16 o más núcleos, solo uno se usa para el trabajo de
Pandas. Esto hace que las operaciones complejas y los datasets grandes sean
extremadamente lentos.
                                          Pandas vs Modin




Podemos observar que Pandas Dataframe solo utiliza un núcleo de la CPU, mientras que la función Modin utiliza todos los núcleos.
Modin es una biblioteca de código abierto , por lo que el código fuente y diversas pruebas de rendimiento que demuestran su eficiencia
en comparación con Pandas están disponibles en GitHub . Según el repositorio de Modin en GitHub, Modin cubre el 90,8 % de las
API de Pandas Dataframe y el 88,05 % de las API de Pandas Series. Por lo tanto, podemos ver que la cobertura de API de la función
Modin es bastante alta, lo que la convierte en una herramienta muy fácil y fiable para escalar y paralelizar el flujo de trabajo de Pandas.
Modin en el ecosistema Big Data

               El funcionamiento de Modin es tres capas clave:

               Capa del Usuario (API de Pandas): En la parte superior, los usuarios
               escriben su código de análisis de datos usando la sintaxis de Pandas, la cual
               ya les es familiar. La única diferencia es que importan Modin en lugar de
               Pandas (import modin.pandas as pd)

               Capa de Optimización (Modin Engine): Esta capa intermedia toma los
               comandos del usuario y los divide en tareas más pequeñas y eficientes. Modin
               es el "cerebro" que decide cómo paralelizar las operaciones para que puedan
               ejecutarse en múltiples núcleos

               Capa del Motor (Backend): En la base, el motor de cómputo distribuido (como
               Dask o Ray) ejecuta las tareas en paralelo. Esta capa es la que realmente
               realiza el trabajo pesado, distribuyendo el cómputo para procesar grandes
               volúmenes de datos de manera eficiente
                                                            Backends en Modin
                           Modin puede ejecutar su motor de paralelización sobre diferentes backends1, siendo los más comunes Ray,
                                                Dask y Unidist. Cada uno es un sistema distribuido con filosofías distintas:




            pip install "modin[ray]"                                            pip install "modin[dask]"                        pip install "modin[mpi]"


   Ray es un marco unificado para escalar                                Dask es un framework de computación             Unidist es un marco que tiene como
   aplicaciones de IA y Python. Ray consta                               distribuida en Python. Nació en el              objetivo proporcionar una API unificada
   de un entorno de ejecución distribuido y                              mundo de ciencia de datos para escalar          para la ejecución distribuida al admitir
   un conjunto de bibliotecas de IA para                                 librerías como NumPy, Pandas y Scikit-          varios backends de ejecución de alto
   simplificar        el      procesamiento           de                 learn. Orientado a colecciones (arrays,         rendimiento. No es un motor en sí, sino
   aprendizaje automático:                                               dataframes, bags) con una interfaz muy          una abstracción que permite a Modin (y
                                                                         parecida a pandas/numpy                         otras   librerías)    trabajar   de   manera
                                                                                                                         unificada     sobre      Ray,     Dask     o
                                                                                                                         Multiprocessing.


1 un backend es el motor de ejecución que hace el “trabajo pesado” detrás de una librería o aplicación.




 https://www.youtube.com/watch?v=rXy2uSD2c-w
                                               Código de ejemplo


Primero, con Pandas                                                     Ahora con Modin



Python                                                                  Python



import pandas as pd                                                     import modin.pandas as pd
import time                                                             import time
t_inicio = time.time()                                                  t_inicio = time.time()
df_pandas = pd.read_csv("big_data.csv")                                 df_modin = pd.read_csv("big_data.csv")
t_fin = time.time()                                                     t_fin = time.time()
print(f"Tiempo de carga con Pandas: {t_fin - t_inicio:.2f} segundos")   print(f"Tiempo de carga con Modin: {t_fin - t_inicio:.2f} segundos")




 En un dataset grande (por ejemplo, de 10 GB), el tiempo de carga con Pandas podría ser de 150 segundos, mientras que con Modin
 podría reducirse a 30 segundos o menos.
02.   Funciones paralelizadas
                                        Cargar datos: read_csv


         Pandas                                         Modin



Python                                                   Python




import pandas as pd                                      import modin.pandas as pd

df = pd.read_csv("ventas.csv")                           df = pd.read_csv("ventas.csv")

ventas_cols = df.filter(like="ventas", axis=1)           ventas_cols = df.filter(like="ventas", axis=1)

print(ventas_cols.head())                                print(ventas_cols.head())
                                            Fusionar: merge


         Pandas                                         Modin



Python                                                   Python




import pandas as pd                                      import modin.pandas as pd

client = pd.read_csv("clientes.csv")                     client = pd.read_csv("clientes.csv")

orden = pd.read_csv("ordenes.csv")                       orden = pd.read_csv("ordenes.csv")

merged = pd.merge(client, orden, on="cliente_id",        merged = pd.merge(client, orden, on="cliente_id",

how="inner")                                             how="inner")
                                                 Filtrar: filter


         Pandas                                                Modin



Python                                                             Python




import pandas as pd                                                import modin.pandas as pd

df = pd.read_csv("ventas.csv")                                     df = pd.read_csv("ventas.csv")

ventas_cols = df.filter(like="ventas", axis=1)                     ventas_cols = df.filter(like="ventas", axis=1)

print(ventas_cols.head())                                          print(ventas_cols.head())
                                         Aplicar función: apply


         Pandas                                                Modin



Python                                                         Python




import pandas as pd                                            import modin.pandas as pd

df = pd.read_csv("ventas.csv")                                 df = pd.read_csv("ventas.csv")

df["con_igv"] = df["monto"].apply(lambda x: round(x * 2, 2))   df["con_igv"] = df["monto"].apply(lambda x: round(x * 2, 2))

print(df[["monto", "con_igv"]].head())                         print(df[["monto", "con_igv"]].head())
                                                                         Compatibilidad

              Altamente compatibles                                               Parcialmente compatibles                No compatibles
         (soporte completo o casi completo)                                    (soporte completo o casi completo)


       read_csv()                    filter()                                            datetime                   Funciones muy específicas del API
       read_excel()                  loc[]                                               rolling()
                                                                                                                    de    Pandas   que   tienen   poca
       read_parquet()                iloc[]                                              resample()
                                                                                                                    demanda o que son difíciles de
       groupby()                     describe()                                          pivot_table()
                                                                                                                    paralelizar.
       merge()                       value_counts()
                                                                                                                    Algunas integraciones con librerías
       join()                         dropna()
                                                                                                                    externas (como plotting directo con
       concat()                       fillna()
                                                                                                                    df.plot())
       apply()                       to_csv()
       map()                          to_parquet()

Estas operaciones están paralelizadas por defecto y tienen mejoras de rendimiento
significativas.
03.   Pandas vs Dask vs Modin
                      Comparativa de Librerías para
                     Manipulación de Datos en Python

    Característica                    Pandas                   Dask                         Modin

                                                 Escala a múltiples núcleos y   Escala automáticamente en
Escalabilidad              Memoria local (RAM)
                                                 clústeres                      múltiples núcleos

                                                 Subconjunto compatible con     Compatible con pandas (sin
Interfaz API               pandas
                                                 pandas                         cambiar código)

Tamaño de          datos
                           Memoria limitada      Datos que exceden la RAM       Datos más grandes que RAM
soportado

                                                                                Sí (automático con Ray o
Paralelismo                No                    Sí (por bloques)
                                                                                Dask)

Facilidad de uso           Muy alta              Media                          Muy alta (usa código pandas)

                                                 Integración             con
Ecosistema                 Muy maduro                                           En crecimiento
                                                 herramientas Big Data
04.   Laboratorio
        Modin en GColab




¡¡¡¡¡¡¡¡ Ejecutemos nuestro script !!!!!!!!

                      Conclusiones

01.   Modin facilita la paralelización automática de muchas operaciones de Pandas,
      permitiendo trabajar con grandes volúmenes de datos sin cambiar el código.


      No todas las funciones de Pandas están completamente soportadas o paralelizadas
02.   en Modin, pero cubre la mayoría de las operaciones comunes usadas en análisis de
      datos.




03.   Elegir entre Pandas, Modin y Dask depende del tamaño del dataset, recursos
      computacionales disponibles y la complejidad de las operaciones a realizar.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
