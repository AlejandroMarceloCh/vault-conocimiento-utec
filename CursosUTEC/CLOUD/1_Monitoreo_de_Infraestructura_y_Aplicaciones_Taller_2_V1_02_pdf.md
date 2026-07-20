---
curso: CLOUD
titulo: 1. Monitoreo de Infraestructura y Aplicaciones - Taller 2 - V1.02
slides: 20
fuente: 1. Monitoreo de Infraestructura y Aplicaciones - Taller 2 - V1.02.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Monitoreo de Infraestructura y Aplicaciones
Semana 12 - Taller 2: CloudWatch

                      ELABORADO POR: GERALDO COLCHADO
             1. Objetivo del taller 2
             2. Ejercicio 1: Logs Insights - Básico (Log no
                estructurado)
             3. Ejercicio 2: Logs Insights - Campos adicionales
Contenido       (Log no estructurado)
CloudWatch
             4. Ejercicio 3: Logs Insights - Avanzado (Log no
                estructurado)
             5. Ejercicio 4: Ejercicio propuesto (Log
                estructurado json)
             6. Cierre
CloudWatch
Objetivo del Taller 2
• Aprender a explorar y analizar los logs de ejecución de lambdas
• Aprende la funcionalidad de Logs Insights
             1. Objetivo del taller 2
             2. Ejercicio 1: Logs Insights - Básico (Log no
                estructurado)
             3. Ejercicio 2: Logs Insights - Campos adicionales
Contenido       (Log no estructurado)
CloudWatch
             4. Ejercicio 3: Logs Insights - Avanzado (Log no
                estructurado)
             5. Ejercicio 4: Ejercicio propuesto (Log
                estructurado json)
             6. Cierre
      CloudWatch
      Ejercicio 1: Logs Insights - Básico
Paso 1: Ingresar a la   Paso 2: Colocar el período de tiempo que indique el docente
opción:


                        Paso 3: Seleccione el grupo de
                        registro que indique el
                        docente y ejecute la consulta
      CloudWatch
      Ejercicio 1: Logs Insights - Básico
Paso 4: Analice los
resultados
             1. Objetivo del taller 2
             2. Ejercicio 1: Logs Insights - Básico (Log no
                estructurado)
             3. Ejercicio 2: Logs Insights - Campos adicionales
Contenido       (Log no estructurado)
CloudWatch
             4. Ejercicio 3: Logs Insights - Avanzado (Log no
                estructurado)
             5. Ejercicio 4: Ejercicio propuesto (Log
                estructurado json)
             6. Cierre
      CloudWatch
      Ejercicio 2: Logs Insights - Campos adicionales
Paso 1: Adicione campos de la ejecución del lambda


fields @timestamp, @message, @requestId, @type,
@duration, @billedDuration, @memorySize, @maxMem
oryUsed
| sort @timestamp asc
| limit 100
      CloudWatch
      Ejercicio 2: Logs Insights - Campos adicionales
Paso 2: Analice los
resultados
             1. Objetivo del taller 2
             2. Ejercicio 1: Logs Insights - Básico (Log no
                estructurado)
             3. Ejercicio 2: Logs Insights - Campos adicionales
Contenido       (Log no estructurado)
CloudWatch
             4. Ejercicio 3: Logs Insights - Avanzado (Log no
                estructurado)
             5. Ejercicio 4: Ejercicio propuesto (Log
                estructurado json)
             6. Cierre
      CloudWatch
      Ejercicio 3: Logs Insights - Avanzado
Paso 1: Agregue filtros, ordene
diferente y analice resultados

fields @timestamp, @message,
@requestId, @type, @duration,
 @billedDuration, @memorySize
, @maxMemoryUsed
| sort @duration desc
| filter @type = 'REPORT'
| limit 100
      CloudWatch
      Ejercicio 3: Logs Insights - Avanzado
Paso 2: Modifique filtros, ordene
diferente y analice resultados

fields @timestamp, @message
| sort @timestamp asc
| filter @message like /(OK|Forbidden|Err)/
| limit 100
             1. Objetivo del taller 2
             2. Ejercicio 1: Logs Insights - Básico (Log no
                estructurado)
             3. Ejercicio 2: Logs Insights - Campos adicionales
Contenido       (Log no estructurado)
CloudWatch
             4. Ejercicio 3: Logs Insights - Avanzado (Log no
                estructurado)
             5. Ejercicio 4: Ejercicio propuesto (Log
                estructurado json)
             6. Cierre
        CloudWatch
        Ejercicio 4: Ejercicio propuesto (Guiado)
•   Verifique el lambda “GenerarEventoSensorIoT” que pinte en log la lectura del sensor.
•   Habilite la regla “SimuladorSensorIoT” en EventBridge por unos 7 minutos
•   Deshabilite la regla “SimuladorSensorIoT” en EventBridge
•   Ejecuta las consultas indicadas y suba sus capturas de pantalla al padlet

    fields @timestamp, @message                          4




    | sort @timestamp desc
    | filter @message like /(FAB1)/
    | limit 100
  CloudWatch
  Ejercicio 4: Ejercicio propuesto (Guiado)
fields @timestamp, tenant_id, lectura_id, lectura_datos.medicion, lectura_datos.unidad_medida
| sort lectura_datos.medicion desc
| filter @message like /(FAB1)/



                                           4
      CloudWatch
      Ejercicio 4: Ejercicio propuesto (Guiado)
fields @timestamp, tenant_id, lectura_id, lectura_datos.medicion, lectura_datos.unidad_medida
| sort lectura_datos.medicion desc
| filter @message like /(FAB1)/ and lectura_datos.medicion > 600
| limit 100


                                               4
        CloudWatch
        Ejercicio 4: Ejercicio propuesto (Guiado)
filter @message like /(FAB1)/
| stats count(*) as numeroMediciones,
  max(lectura_datos.medicion) as mayorMedicion,
  min(lectura_datos.medicion) as menorMedicion,
  avg(lectura_datos.medicion) as promedioMedicion
                                                    4
             1. Objetivo del taller 2
             2. Ejercicio 1: Logs Insights - Básico (Log no
                estructurado)
             3. Ejercicio 2: Logs Insights - Campos adicionales
Contenido       (Log no estructurado)
CloudWatch
             4. Ejercicio 3: Logs Insights - Avanzado (Log no
                estructurado)
             5. Ejercicio 4: Ejercicio propuesto (Log
                estructurado json)
             6. Cierre
Cierre:
CloudWatch - Qué aprendimos?
• Explorar y analizar los logs de ejecución de lambdas
• Funcionalidad de Logs Insights
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
