---
curso: INGSOFT
titulo: 12 - Semana 11/IS1 - Aula 11 - Pruebas de Software - Parte 2__pptx
slides: 31
fuente: 12 - Semana 11/IS1 - Aula 11 - Pruebas de Software - Parte 2__pptx.pdf
---

Ingeniería de Software

       Profesor Christian Paz
                                               Desarrollo de Software




    Análisis                     Diseño              Implementación            Pruebas                 Despliegue             Mantenimiento


Qué debe    hacer   el   Cómo      se   hará   el   Hacer el Software.   El software hace lo que   Entregar,   poner   en   El software funciona, pero
software?                software?                                       se supone que debe        marcha.                  le falta esto, o está lento,
                                                                         hacer?                                             o necesita mejorar esto.
1.
 Detección y Corrección
 de errores
              Detección y corrección de errores
•   La etapa de pruebas tiene como objetivo encontrar los posibles errores en el software antes de que
    los encuentre el usuario.


•   El reporte de pruebas resulta en una lista de todos los casos de prueba que hayan fallado.


•   Existen otros errores que se pueden encontrar de forma manual y también deben ser reportados
    (usualmente se adicionan a la lista de casos de prueba).
                            Detección del Error
•   Test Case: Creación de Usuario con un email ya registrado.

•   Status: Fail.

•   Expected Result: Se emite un mensaje de error.

•   Actual Result: Se pudo crear el usuario con un email ya registrado.
                       Detección del error
Si el error no está asociado a un Test Case.

• Reproducción del error.

• Tener un conjunto de pasos (mínimos si fuera posible) para repetir el error.

• Construir un nuevo test case.

• Identificar el conjunto de inputs y el estado que producen el error.
                           Errores de lógica
El software entrega valores equivocados o realiza acciones no esperadas.

Ejemplos:

• El sistema no redujo el stock después de la compra finalizada.

• El usuario hizo logout pero si ingresa al sistema su sesión aún continúa activa.
            Errores en tiempo de ejecución
El software no está preparado para una condición y arroja un error inesperado.

Ejemplos:

• División entre cero.

• Excepción de tamaño de array.

• Excepción de variable nula.
                   Errores de integración
Cuando algún componente externo al software no responde o cambia su interfaz y resulta en un error
en el software.

Ejemplo:

• El software requiere enviar un correo de confirmación, pero el servidor de correos falla.

• La conexión a la BD se pierde.
                  Errores de rendimiento

Incluyen tiempos de respuesta lentos o falta de recursos después de un tiempo de uso.
Ejemplos:


• El sistema demora 5s en responder a un botón y sale un mensaje de error por ese motivo.
• El servidor se reinicia o apaga sin aparentemente razón.
Corrección del error - Debugging
Corrección del
error - Logging
Corrección del error - Pruebas unitarias

Las pruebas unitarias ayudan a aislar errores y evitar que vuelvan a suceder.


Crear una prueba unitaria que falle para el caso de prueba reportado pero considerando el mínimo
conjunto de pasos que ocasiona el error.
                      Corrección del error

• Cambiar el código de forma que se corrija el error.

• Realizar pruebas para confirmar que el error ya no ocurra.

• Realizar pruebas para que la corrección realizada no introduzca nuevos errores.

• Realizar la corrección de forma coherente con la estructura general del sistema.
2.
 TDD: Test Driven
 Development
                  Test Driven Development




• TDD es una técnica en la cual las pruebas son escritas antes del código
  propiamente dicho.

• Red: Escribir un test que falla.

• Green: Escribir el código mínimo que pase el test.

• Refactor: Mejorar el código conservando el test en estado pass.

• Objetivo: Asegurar que el código funcione sea mantenible y posibilidad de mejora
  continua.
                              Test Driven Development




             • Ejemplo: https://github.com/cpazutec/tdd (Main Branch)
        def quicksort(arr):
                return arr
        def test_unsorted_array(self):
                self.assertEqual(quicksort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
                                 AssertionError: Lists differ: [3, 6, 8, 10, 1, 2, 1] != [1, 1, 2, 3, 6, 8, 10]
Paso 1:
Basic Test                       First differing element 0:
+                                3
No-Op Code                       1

                                 - [3, 6, 8, 10, 1, 2, 1]
    Test Fail                    + [1, 1, 2, 3, 6, 8, 10]

                                 ----------------------------------------------------------------------
                                 Ran 1 test in 0.000s

                                 FAILED (failures=1)
                                     Test Driven Development




                • Ejemplo: https://github.com/cpazutec/tdd (secondversion Branch)
                    def quicksort(arr, low=0, high=None):
                        if high is None:
                            high = len(arr) - 1

                        if low < high:
                            # Partition the array and get the pivot index
Paso 3:                     pivot_index = partition(arr, low, high)
Improved code
                            # Recursively sort elements before and after the partition
                            quicksort(arr, low, pivot_index - 1)
                            quicksort(arr, pivot_index + 1, high)

                        return arr   # This allows us to return the sorted array for convenience
                    …
                                     ----------------------------------------------------------------------
        Test Pass                    Ran 1 test in 0.000s

                                     OK
                  Test Driven Development




• Calidad de Código.

• Mejor diseño.

• Facilidad para refactorizar.

• Documentación mejorada por las pruebas.

• Consumo de tiempo para iniciar la implementación.
                 Test Driven Development




• Escribir tests pequeños.

• Las pruebas deben ser independientes.

• Dar nombres apropiados a los tests.

• Automatizar la ejecución de tests en el pipeline de despliegue.

3.
 Refactorización
                            Refactorización
• Refactorización es el proceso de reorganizar o modificar el código fuente de un programa sin
  cambiar su comportamiento externo.
• El objetivo principal es mejorar la estructura interna del código, haciéndolo más legible, mantenible
  y escalable.
Refactorización – Extracción de Métodos
     Refactorización – Renombrar




def calcular_area(l, w):   def calcular_area(longitud, ancho):
  resultado = l * w          area = longitud * ancho
  return resultado           return area
         Refactorización – Reutilizar




boolean retiro(valor)                 boolean retiro(valor)
  if(valor>saldo)                       if(tieneSaldoSuficiente(valor) == false)
     return false                          return false
  saldo = saldo - valor                 saldo = saldo - valor
  return true                           return true

boolean tieneSaldoSuficiente(valor)   boolean tieneSaldoSuficiente(valor)
  if(valor>saldo)                       if(valor>saldo)
     return false                          return false
  return true                           return true
Refactorización – Extracción de Clases
Refactorización – Simplificar
       condicionales
   División de métodos o archivos grandes




• Tiene muchas responsabilidades.

• Dificulta la comprensión.

• Reutilizar código.

• Facilidad para crear un test automático.
GRACIAS
CHRISTIAN PAZ TRILLO
                                  Práctica




https://github.com/cpazutec/refactoringvotes

Refactorizar este código y describir las técnicas aplicadas en los comentarios.

Cada técnica diferente les da tres puntos.
                          Práctica de Pruebas Unitarias

Sobre la implementación del API de Cambio de Monedas:


Elaborar e implementar pruebas unitarias.
Elaborar casos de prueba manual con el formato Precondition, Test Steps, Test Data, Expected Result.


Mostrar que se puedan ejecutar en su aplicación.


Considerar:
Caso de éxito.
Casos de falla: transferencia sin saldo, transferencia a usuario que no exista.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
