---
curso: INGSOFT
titulo: 11 - Semana 10/IS1 - Aula 10 - Pruebas de Software__pptx
slides: 28
fuente: 11 - Semana 10/IS1 - Aula 10 - Pruebas de Software__pptx.pdf
---

Ingeniería de Software

       Profesor Christian Paz
                                               Desarrollo de Software




    Análisis                     Diseño              Implementación            Pruebas                 Despliegue             Mantenimiento


Qué debe    hacer   el   Cómo      se   hará   el   Hacer el Software.   El software hace lo que   Entregar,   poner   en   El software funciona, pero
software?                software?                                       se supone que debe        marcha.                  le falta esto, o está lento,
                                                                         hacer?                                             o necesita mejorar esto.
1.
 Pruebas de Software
                                            Pruebas de Software

•   Verificar que cada parte de un software haga lo que se espera que haga.
•   Descubrir defectos antes de que el usuario final lo haga.



           "Las pruebas pueden mostrar la presencia de errores mas no su ausencia"
           Dijkstra, 1992.
Inspecciones de Software




                                            En paralelo con el desarrollo.
                                                    No son tan costosas.
              Pueden detectar errores en cada componente sin afectar los
                                                                    otros.
                                                    Verificación estática.
                             Caso de Prueba – Test Case

•   Un caso de prueba es un conjunto de condiciones, variables y secuencia de pasos bajo las cuales un evaluador
    determinará si un sistema, software o una de sus características funciona correctamente.
Proceso de Pruebas de Software
2.
          Pruebas durante el
          Ciclo de Vida


https://learning.oreilly.com/library/view/clean-code-a/9780136083238/

Clean Code: A Handbook of Agile Software Craftsmanship
queue
By Robert C. Martin
         Pruebas durante el ciclo de vida

• Pruebas de Desarrollo (Desarrolladores y Diseñadores). >

• Pruebas de Versión (Equipo de Prueba).

• Pruebas de Usuario (Usuario real o potencial).
                                                  Pruebas de desarrollo.
                                                  Pruebas de versión.
                                                  Pruebas de usuario.

Pruebas de Desarrollo



• Pruebas de Unidad:

  Probar componentes: clases, métodos.
  Llamar las rutinas con diferentes parámetros.


  Partes
  - Inicialización
  - Llamada con valores de entrada (Ejecución)
  - Comparación de valores esperados con
  valores de salida. (Assert)
                                Pruebas de Desarrollo
Pruebas de Unidad:

  TestCuenta {
  void testRetiro100de100() {
      Cuenta c = new Cuenta(mockCliente, 100, Soles); <<- Inicializacion
      c.retiro(100, Soles); << - Ejecucion
      AssertEquals(0, c.saldo(), "El saldo no fue actualizado correctamente"); <- Verificacion o Asercion
  }

  }

  testRetiro200de500()
                                                                                            Pruebas de desarrollo.
                                                                                            Pruebas de versión.
                                                                                            Pruebas de usuario.
Selección de Datos de Prueba




                               Pruebas de desarrollo.
                               Pruebas de versión.
                               Pruebas de usuario.
                                 Pruebas de Desarrollo

Pruebas de Componente e Integración:

Probar diversos puntos de interacción entre clases.

Validar elementos persistidos.

Validar formatos de integración entre componentes.


                                                         Pruebas de desarrollo.
                                                         Pruebas de versión.
                                                         Pruebas de usuario.
                           Pruebas de Desarrollo
                               Retiro(Cuenta cuenta, Int valor)
                                 if(valor<=0)
Beneficios:                         return valorNoValido
                                 if(cuenta.saldo<valor)
Cobertura de código.                return saldoInsuficiente
                                 cuenta.saldo = cuenta.saldo – valor;
                                 return cuenta.saldo;
Pruebas de regresión.

Depuración simplificada.       TestRetiro20deCuentaSaldo100 -> 4 / 6 = 66.6%
                               TestRetiro0deCuentaSaldo100 -> 2 / 6 = 33.3%
                               TestRetiro200deCuentaSaldo100 -> 3/6 = 50%
                                                                               Pruebas de desarrollo.
                               Cobertura Codigo: 6/6 = 100%                    Pruebas de versión.
                                                                               Pruebas de usuario.
Pruebas de Versión




        Equipo independiente.

        Menos: Descubrir bugs del sistema.

        Más: Comprobar que el sistema cumpla con los requerimientos.




                                             Pruebas de desarrollo.
                                             Pruebas de versión.
                                             Pruebas de usuario.
                         Pruebas de desarrollo.
• Escenario de Pruebas   Pruebas de versión.
                         Pruebas de usuario.
• Caso de Pruebas
                                  Pruebas de versión

Pruebas de rendimiento

Son un conjunto de pruebas enfocadas en el rendimiento de la aplicación en condiciones cercanas (o que
  exceden) las condiciones a las que la aplicación estará sometida durante su vida útil, principalmente en
  condiciones de alto uso. Ejemplos:
- X / TikTok durante un evento (elección del Papa).
- Teleticket al abrir las entradas de un evento.

Herramientas: Jmeter, Locust.                                                            Pruebas de desarrollo.
                                                                                         Pruebas de versión.
                                                                                         Pruebas de usuario.
                                 Pruebas de versión

Pruebas de rendimiento - Load Testing

Ver cómo se comporta el sistema bajo una carga específica de usuarios concurrentes o transacciones.

Ejemplo:

Simular 1000 usuarios accediendo simultáneamente a una aplicación web para ver si el tiempo de respuesta se
mantiene por debajo de 2 segundos.
                                                                                      Pruebas de desarrollo.
                                                                                      Pruebas de versión.
                                                                                      Pruebas de usuario.
                                 Pruebas de versión

Pruebas de rendimiento - Stress Testing

Determinar el punto de ruptura del sistema llevándolo más allá de su capacidad máxima esperada.

Ejemplo:

Aumentar gradualmente los usuarios concurrentes hasta que el sistema se ralentiza o se bloquea, para
identificar el máximo que puede manejar.
                                                                                      Pruebas de desarrollo.
                                                                                      Pruebas de versión.
                                                                                      Pruebas de usuario.
                                 Pruebas de versión

Pruebas de rendimiento - Scalability Testing

Evaluar la capacidad del sistema de escalar horizontal o verticalmente (más usuarios, más datos, más nodos).

Ejemplo:

Ver si agregar más instancias de servidor reduce el tiempo de respuesta al aumentar los usuarios de 100 a
10000.
                                                                                        Pruebas de desarrollo.
                                                                                        Pruebas de versión.
                                                                                        Pruebas de usuario.

                                  Pruebas de versión

Pruebas de rendimiento - Soak Testing (Duración)

Probar la estabilidad del sistema bajo carga sostenida durante un periodo prolongado.

Ejemplo:

Ejecutar la aplicación con 500 usuarios durante 48 horas continuas para ver si hay fugas de memoria, errores, o
degradación.
                                                                                        Pruebas de desarrollo.
                                                                                        Pruebas de versión.
                                                                                        Pruebas de usuario.
                                 Pruebas de versión

Pruebas de rendimiento - Volume Testing

Evaluar el rendimiento del sistema con grandes volúmenes de datos.

Ejemplo:

Cargar 10 millones de registros en una base de datos y luego ejecutar búsquedas para medir el rendimiento de
las consultas.
                                                                                       Pruebas de desarrollo.
                                                                                       Pruebas de versión.
                                                                                       Pruebas de usuario.
                                 Pruebas de versión

Pruebas de rendimiento - Concurrency Testing

Analizar cómo se comporta el sistema cuando múltiples usuarios acceden y modifican los mismos recursos al
mismo tiempo.

Ejemplo:

100 usuarios actualizan el mismo perfil de usuario simultáneamente para verificar problemas de bloqueo o
pérdida de datos.                                                                        Pruebas de desarrollo.
                                                                                      Pruebas de versión.
                                                                                      Pruebas de usuario.
                                 Pruebas de versión

Pruebas de seguridad

Validar que un sistema no sea vulnerable.

Detectar que los puntos del sistema que son accesibles sin autorización sean solo los esperados.

Detectar como reaccionan los puntos del sistema a ataques (datos falsos, inyecciones SQL).

                                                                                        Pruebas de desarrollo.
                                                                                        Pruebas de versión.
                                                                                        Pruebas de usuario.
                               Pruebas de usuario

Pruebas Alfa: Con asistencia del equipo de desarrollo.

Pruebas Beta: Libre acceso a los usuarios.

Pruebas de Aceptación: Pruebas que permitirán decidir si la versión está aceptable para ser desplegada
  en el entorno del cliente.


                                                                                Pruebas de desarrollo.
                                                                                Pruebas de versión.
                                                                                Pruebas de usuario.
                                 Pruebas de usuario

Criterios de aceptación.

Plan de pruebas de aceptación.

Ejecutar pruebas de aceptación

Negociar los resultados de las pruebas.

Rechazo / Aceptación de la versión.                   Pruebas de desarrollo.
                                                      Pruebas de versión.
                                                      Pruebas de usuario.
                         Práctica de Pruebas Unitarias

Sobre el programa de la semana pasada (distancia entre ciudades):


Elaborar e implementar pruebas unitarias.
Elaborar casos de prueba manual con el formato Precondition, Test Steps, Test Data, Expected Result.


Mostrar que se puedan ejecutar en su aplicación.


Considerar:
Caso de éxito.
2 Casos extremos: una de las ciudades no exista y entregar la misma ciudad dos veces.
GRACIAS
CHRISTIAN PAZ TRILLO

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
