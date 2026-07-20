---
curso: INGSOFT
titulo: 08 - Semana 6/IS1 - Aula 6 - Algunos elementos de Diseño__pptx
slides: 20
fuente: 08 - Semana 6/IS1 - Aula 6 - Algunos elementos de Diseño__pptx.pdf
---

Ingeniería de Software

       Profesor Christian Paz
         Arquitectura Monolítica

         Arquitectura en Capas (Layers)

         Microservicios

         Arquitectura Orientada a Eventos

         Casos de Estudio




Agenda
         Bibliografía:
         https://learning.oreilly.com/library/view/software-
         architecture-patterns/9781098134280/
1.
 Arquitectura Monolítica
    Arquitectura Monolítica
Un único elemento de distribución contiene toda la
funcionalidad del software.


Ej: Sistema Operativo.
Juego que funciona localmente sin conexión a
internet.
Aplicación que se instala y ejecuta localmente.
Ventajas:


• Eficiencia al usar el hardware.
• Baja necesidad de conectividad.
• Simplicidad de estructura de código


Desventajas
• Sin modularidad en tiempo de ejecución.
• Single Point of Failure.
• Dificultad de despliegue (actualizaciones).
2.
 Arquitectura en Capas
Arquitectura Cliente Servidor
Arquitectura de varias
        capas
Cada capa tiene una responsabilidad específica.
La comunicación se hace a a través de red o no.
Los elementos que transitan entre las capas
deben ser lo más simple posible (POJO: Plain Old
Java Objects).
Ventajas:
• Facilidad de dividir el trabajo por especialidad (front, back, database).
• Manejo de código simple.
• Simplicidad de despiegue.


Desventajas
• Escalabilidad horizontal limitada.
• Funcionalidad está dividida en varias capas (agregar un campo en
  BD requiere campos en todas las capas).
3.
 Microservicios
               Microservicios
Cada servicio se encarga de una funcionalidad
específica y es responsable por el manejo de los
datos asociados.


API Gateway esconde la estructura interna de los
microservicios a los clientes.


Cada servicio puede escalar de forma diferente.


Cada servicio es reutilizable.
                                                                                  Microservicios
https://miservidor.com.pe/account/crearcuenta  http://192.168.1.12/crearcuenta


https://miservidor.com.pe/inventory/registrar  http://192.168.1.13/registrar

https://miservidor.com.pe/shipping/entregar




                                                                                                • Son componentes de software
                                                                                                                  independientes.

                                                                                                       • Despliegue independiente.

                                                                                                • Comunicación estándar HTTP.

                                                                                                        • Independencia de datos.

                                                                                                                   • Escalabilidad.
                                                                                  Common
                                                                                  - Entidades (POJO)
                                                                                  - Helpers


                                                                                  Account Service
                                                                                  - Import Common
Ventajas:
• Independencia de cada funcionalidad.
• Agilidad para los cambios.
• Alta tolerancia a fallas y facilidad de escalamiento horizontal y
  vertical.


Desventajas
• Cuando existen muchas interacciones entre los microservicios
  (orquestación) puede resultar complejo y costoso.
• Cuando los datos están muy interconectados.
• Consideraciones para latencia, seguridad y replicación de datos.
4.
 Arquitectura Orientada
 a Eventos
        Arquitectura Orientada
              a Eventos
En algunas situaciones, los procesos
de software pueden ser considerados
como eventos.


Ej: Creación de Cuenta de Alumno.


- Creación de Cuenta Google.
- Creación de Cuenta Canvas.
- Creación en el Sistema Financiero.


- Notificación Usuario está listo para
  uso.
Ventajas:
• Alta tolerancia a fallas.
• Manejo asíncrono de operaciones pesadas o lentas.


Desventajas
• Si los clientes requieren una respuesta inmediata.
• Complejidad en el manejo de errores.


• peru.gob.pe/miscertificados
• -> insertar en una cola mi dni, correo al cual me reporten.
5.
 Casos de Estudio
                                  Caso de Estudio
• Sistema de venta de entradas masivo (Concierto) [Demanda por compra > Posibilidad de Atención].

• Sistema de control de ingreso de ese evento asumiendo que el local de ingreso es remoto y tiene
  mala conectividad a internet.



• https://excalidraw.com/#json=tLIFaYHjyPSWmPYBJ8Upo,bS6WL-bN37ZGYog_jYr-Jg
                            Caso de Estudio
• Venta de entradas en eventos masivos (Ej: Concierto con alta demanda).
GRACIAS
CHRISTIAN PAZ TRILLO

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
