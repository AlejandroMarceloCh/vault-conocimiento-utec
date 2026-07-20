---
curso: BIGDATA
titulo: 03 - Semana 1/Semana 1 Laboratorio Caso Uber
slides: 5
fuente: 03 - Semana 1/Semana 1 Laboratorio Caso Uber.pdf
---

CASO: UBER
ARQUITECTURA
Mg. Aldo Lezama Benavides

Semana 1
                           Caso: “Pricing dinámico en Uber”

Uber nace como una solución para conectar pasajeros con
conductores de forma eficiente. Con el crecimiento de la
demanda, la empresa enfrentó un problema clave:
En horas pico (lluvia, conciertos, tráfico), la demanda
superaba ampliamente la oferta de conductores. Esto
generaba:
• Tiempos de espera largos
• Cancelaciones
• Mala experiencia de usuario
Para resolverlo, Uber implementa pricing dinámico (surge
pricing), que ajusta precios en tiempo real para:
• Incentivar más conductores
• Regular la demanda
• Maximizar eficiencia del sistema
                              Caso: “Pricing dinámico en Uber”




• Buscan maximizar ingresos         • Buscan rapidez y precio razonable   • Balancea oferta y demanda
• Deciden cuándo conectarse         • Sensibles a precios altos           • Optimiza experiencia + revenue
                                                    Actividad
                                   Traducir un problema de negocio en arquitectura Big Data.




1. Entendimiento del negocio                  2. Identificación de datos                       3. Tipos de datos

• ¿Cuál es el principal problema              • ¿Qué datos genera un viaje?                    • Streaming

  en horas pico?                              • ¿Datos        para         entender            • Estructurados

• ¿Por qué no basta con más                      demanda?                                      • No Estructurados

  conductores?                                • ¿Datos de oferta?

• ¿Qué pasa si no hay pricing                 • ¿Variables externas?

  dinámico?                                   • ¿Otros datos?

• ¿Quiénes se ven afectados?
   Caso: “Pricing dinámico en Uber”


4. Identificación de las Vs de Big   5. Arquitectura Big Data

Data                                 • Fuentes

• Volumen                            • Ingestión

• Velocidad                          • Almacenamiento

• Variedad                           • Procesamiento

• Veracidad                          • Consulta

• Valor                              • Visualización

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
