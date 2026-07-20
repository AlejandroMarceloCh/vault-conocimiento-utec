---
curso: CLOUD
titulo: 1. Otros tópicos - Taller 3 - V1.00
slides: 16
fuente: 1. Otros tópicos - Taller 3 - V1.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Otros tópicos
Semana 14 - Taller 3: Optimización de Lambdas

                      ELABORADO POR: GERALDO COLCHADO
                          1. Objetivo del taller 3
                          2. Ejercicio 1: Tiempos de ejecución de Lambdas
                          3. Ejercicio 2: Memoria RAM de Lambdas
Contenido                 4. Ejercicio 3: Última fecha de ejecución de Lambdas
Optimización de Lambdas   5. Ejercicio 4: Aumente la memoria RAM
                          6. Ejercicio 5: Ejercicio propuesto
                          7. Cierre
Optimización de Lambdas
Objetivo del Taller 3
• Aprender a optimizar tiempos de ejecución de Lambdas
                          1. Objetivo del taller 3
                          2. Ejercicio 1: Tiempos de ejecución de Lambdas
                          3. Ejercicio 2: Memoria RAM de Lambdas
Contenido                 4. Ejercicio 3: Última fecha de ejecución de Lambdas
Optimización de Lambdas   5. Ejercicio 4: Aumente la memoria RAM
                          6. Ejercicio 5: Ejercicio propuesto
                          7. Cierre
Optimización de Lambdas
Tiempos de ejecución de Lambdas
•   Paso 1: Identifique el tiempo de ejecución máximo de los siguientes lambdas
    (Utilice AWS Cloud Watch Log Insights): ListarPendientes, ListarAlumnos,
    GenerarEventoSensorIoT, InsertarEventoSensorIoT

    fields @timestamp, @message, @requestId, @type, @duration, @billedDuration,
     @memorySize, @maxMemoryUsed
    | sort @duration desc
    | filter @type = 'REPORT'
    | limit 1000
                          1. Objetivo del taller 3
                          2. Ejercicio 1: Tiempos de ejecución de Lambdas
                          3. Ejercicio 2: Memoria RAM de Lambdas
Contenido                 4. Ejercicio 3: Última fecha de ejecución de Lambdas
Optimización de Lambdas   5. Ejercicio 4: Aumente la memoria RAM
                          6. Ejercicio 5: Ejercicio propuesto
                          7. Cierre
Optimización de Lambdas
Memoria RAM de Lambdas
•   Paso 1: Identifique la Memoria RAM usada por estos Lambdas:
    ListarPendientes, ListarAlumnos, GenerarEventoSensorIoT,
    InsertarEventoSensorIoT
                          1. Objetivo del taller 3
                          2. Ejercicio 1: Tiempos de ejecución de Lambdas
                          3. Ejercicio 2: Memoria RAM de Lambdas
Contenido                 4. Ejercicio 3: Última fecha de ejecución de Lambdas
Optimización de Lambdas   5. Ejercicio 4: Aumente la memoria RAM
                          6. Ejercicio 5: Ejercicio propuesto
                          7. Cierre
Optimización de Lambdas
Ejercicio 3: Última fecha de ejecución de Lambdas
•   Paso 1: Identifique la última fecha de ejecución de lambdas (Utilice AWS
    Cloud Watch Log Insights): ListarPendientes, ListarAlumnos,
    GenerarEventoSensorIoT, InsertarEventoSensorIoT

    fields @timestamp, @message, @requestId, @type, @duration, @billedDuration,
     @memorySize, @maxMemoryUsed
    | sort @timestamp desc
    | filter @type = 'REPORT'
    | limit 1000
                          1. Objetivo del taller 3
                          2. Ejercicio 1: Tiempos de ejecución de Lambdas
                          3. Ejercicio 2: Memoria RAM de Lambdas
Contenido                 4. Ejercicio 3: Última fecha de ejecución de Lambdas
Optimización de Lambdas   5. Ejercicio 4: Aumente la memoria RAM
                          6. Ejercicio 5: Ejercicio propuesto
                          7. Cierre
     Optimización de Lambdas
     Ejercicio 4: Aumente la memoria RAM
•   Paso 1: Aumente la memoria RAM a 512 MB en
    primero y tercero y a 1024 MB en el segundo y
    cuarto lambdas: ListarPendientes, ListarAlumnos,
    GenerarEventoSensorIoT,
    InsertarEventoSensorIoT

•   Paso 2: Ejecute los lambdas y verifique con Logs
    Insights los tiempos de ejecución y compare si
    mejoró tiempo de ejecución en Cold Start.
                          1. Objetivo del taller 3
                          2. Ejercicio 1: Tiempos de ejecución de Lambdas
                          3. Ejercicio 2: Memoria RAM de Lambdas
Contenido                 4. Ejercicio 3: Última fecha de ejecución de Lambdas
Optimización de Lambdas   5. Ejercicio 4: Aumente la memoria RAM
                          6. Ejercicio 5: Ejercicio propuesto
                          7. Cierre
     Optimización de Lambdas
     Ejercicio 5: Ejercicio propuesto
•   Suba al padlet indicado por el docente toda la evidencia del Ejercicio 1 al Ejercicio 4 en un
    documento word, excel o power point donde se muestre la mejora en el tiempo de ejecución del
    Cold Start de los lambdas.
                          1. Objetivo del taller 3
                          2. Ejercicio 1: Tiempos de ejecución de Lambdas
                          3. Ejercicio 2: Memoria RAM de Lambdas
Contenido                 4. Ejercicio 3: Última fecha de ejecución de Lambdas
Optimización de Lambdas   5. Ejercicio 4: Aumente la memoria RAM
                          6. Ejercicio 5: Ejercicio propuesto
                          7. Cierre
Cierre:
Optimización de Lambdas - Qué aprendimos?
• Optimizar tiempos de ejecución de Lambdas
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
