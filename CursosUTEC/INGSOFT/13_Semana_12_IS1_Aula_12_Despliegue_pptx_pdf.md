---
curso: INGSOFT
titulo: 13 - Semana 12/IS1 - Aula 12 - Despliegue__pptx
slides: 25
fuente: 13 - Semana 12/IS1 - Aula 12 - Despliegue__pptx.pdf
---

Ingeniería de Software

       Profesor Christian Paz
                                               Desarrollo de Software




    Análisis                     Diseño              Implementación            Pruebas                 Despliegue             Mantenimiento


Qué debe    hacer   el   Cómo      se   hará   el   Hacer el Software.   El software hace lo que   Entregar,   poner   en   El software funciona, pero
software?                software?                                       se supone que debe        marcha.                  le falta esto, o está lento,
                                                                         hacer?                                             o necesita mejorar esto.
1.
 Despliegue de
 Software
                  Despliegue de Software (Deployment)

•   El despliegue de software consiste en la transición de todas las estructuras de código fuente (código, scripts) hacia
    software en ejecución.
•   Esta actividad inicia desde la etapa de Diseño especialmente referido a la arquitectura.
•   Puede realizarse de forma manual hasta totalmente automatizada.
•   Las actividades de despliegue usualmente son efectuadas por alguien con perfil de “DevOps”.
 Diseño

                              Diagramas de Arquitectura



Desarrollo   Código, Scripts de BD, Configuración

                                                          Despliegue




 Pruebas       Casos de Prueba automatizados y
               manuales
Despliegue de Software




                   Con base en el modelo de arquitectura:
                   •   Definir la infraestructura que
                       soportará la arquitectura.
                   •   Considerar ambientes de desarrollo,
                       pruebas y producción.
                   •   Necesidades de red (permisos,
                       firewall).
                   •   Creación de scripts de despliegue.
Despliegue de Software




                   Con base en el modelo de arquitectura:
                   •   Inicialización de datos.
                   •   Scripts de inicialización de datos.
                   •   Configuración inicial del sistema.
                   •   Cuál es el procedimiento de
                       despliegue cada nueva versión.
                   •   Validación del despliegue.
Despliegue de Software




                   Con base en el modelo de arquitectura:
                   •   Cómo monitorear el funcionamiento
                       del software.
                   •   Cómo alertar sobre algún
                       funcionamiento incorrecto del
                       software.
                   •   Cómo proceder a atender una alerta
                       generada.
                                           Preparación
• Definir la Infraestructura que soportará la arquitectura propuesta:
      Hardware o Virtualización (ambientes en nube).
      Sistema Operativo.

•   Ej:
•   Frontend: VM en AWS.
•   Movie Service: Lambda.
•   MySQL: RDBMS gestionado por AWS.
•   Api Gateway en AWS.
                                           Preparación

• Definir la Infraestructura que soportará la arquitectura propuesta:
      Hardware o Virtualización (ambientes en nube).
      Sistema Operativo.

•   Ej:
•   Frontend: Nginx instalado en IP 192.168.0.204.
•   Movie Service: Dockerizado en k8s.
•   MySQL: Servidor en IP 192.168.0.205 Puerto 1593.
•   Api Gateway configurado en el mismo Nginx del frontend.
                                           Preparación

• Ambientes:                                      • Instalación de Software necesario.
     Desarrollo.
     Pruebas.
     Producción

•   Ej:
•   Desarrollo: Servidor con 16G de RAM.
•   Pruebas: 32GB de RAM.
•   Producción: 64GB de RAM.
                                         Preparación

• Conectividad de Red y Seguridad.
Nginx tendrá salida a Internet y requerirá un SSL / HTTPS.
Debido a la conexión al API externa, Movie Service deberá
tener salida a internet.
                        Versionamiento de Software
Proceso de asignar identificadores únicos a diferentes versiones de un programa o aplicación para gestionar
y rastrear sus cambios a lo largo del tiempo.
• Identificar el estado del software: Saber si es una versión inicial, una actualización menor o una
  importante.
• Facilitar la colaboración: Ayuda a los equipos a coordinar el trabajo en diferentes versiones.
• Mantener la trazabilidad: Permite saber qué funcionalidades o cambios están presentes en cada versión.
• Mejorar la compatibilidad: Garantiza que los usuarios o sistemas relacionados puedan adaptarse a
  nuevas versiones.
                       Versionamiento de Software

Herramientas: Git (Github, GitLab, Azure Devops).
                           Integración Continua (CI)

Integrar con frecuencia los cambios de código de todos los desarrolladores en un repositorio central, seguido
de la automatización de pruebas y compilaciones para garantizar que el nuevo código no cause problemas
en el proyecto.


Detectar y solucionar errores rápidamente, mejorar la calidad del software y reducir el tiempo
necesario para lanzar actualizaciones.
                           Integración Continua (CI)
• Detección temprana de errores: Al probar cambios con frecuencia, los problemas se identifican
  rápidamente.
• Colaboración eficiente: Los desarrolladores trabajan en paralelo sin causar conflictos en el código.
• Mayor calidad del software: Se asegura que el código siempre esté en un estado funcional y probado.
• Menor riesgo en despliegues: Las actualizaciones pequeñas y frecuentes son más seguras que grandes
  cambios aplicados de una vez.
                    Integración Continua (CI)

Herramientas
• Jenkins.
• Github actions.
• Ansible.
Integración Continua
                           Despliegue continuo (CD)

Consiste en automatizar todo el proceso de implementación de nuevas versiones del software en un
entorno de producción, asegurando que los cambios que han pasado las pruebas automatizadas se
desplieguen directamente a los usuarios finales.


Garantizar que los cambios en el código, como nuevas funcionalidades, correcciones de errores o
mejoras, lleguen rápidamente a producción de manera confiable y sin intervención manual.
                    Despliegue continuo (CD)

Herramientas
• Jenkins.
• Github actions.
• Ansible.

CD
                                    Implementación

• Configuración del Sistema:
      URLs.
      Cadenas de Conexión a BD.
      Usuarios / Passwords / Certificados de las APIs.
      Inicialización de BD.
                                   Implementación




API Key OMDb: Desarrollo y Producción.
Cadena de Conexión BD.
Ruta de Conexión del frontend al API Gateway.
                                           Validación
• Pruebas Unitarias / Integración ejecutadas antes de despliegue.
• Una vez que se realice el despliegue en cualquier ambiente:
      Validar que la versión desplegada funcione.
GRACIAS
CHRISTIAN PAZ TRILLO

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
