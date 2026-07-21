---
curso: INGSOFT
titulo: 12 - Semana 11/IS1 - Aula 11 - Pruebas de Software - Parte 2__pptx
slides: 31
fuente: 12 - Semana 11/IS1 - Aula 11 - Pruebas de Software - Parte 2__pptx.pdf
---

## Slide 1

Portada (decorativa: fondo azul con silueta humano-robot en túnel tecnológico).

# Ingeniería de Software
Profesor Christian Paz

## Slide 2

Título: **Desarrollo de Software**

Diagrama de línea de tiempo horizontal (pipeline) con 6 etapas conectadas por una línea con nodos circulares (cada uno con un ícono blanco). La etapa "Pruebas" está resaltada en amarillo/lima; las demás en azul. De izquierda a derecha:

| Etapa | Ícono | Descripción |
|-------|-------|-------------|
| **Análisis** | diana/target | ¿Qué debe hacer el software? |
| **Diseño** | lupa | ¿Cómo se hará el software? |
| **Implementación** | cohete despegando | Hacer el Software. |
| **Pruebas** (resaltada) | calendario con checks | El software hace lo que se supone que debe hacer? |
| **Despliegue** | cohete | Entregar, poner en marcha. |
| **Mantenimiento** | eslabón de cadena | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

## Slide 3

Slide de sección (decorativa: mano robótica tocando un globo terráqueo digital).

# 1. Detección y Corrección de errores

## Slide 4

Título: **Detección y corrección de errores**

- La etapa de pruebas tiene como objetivo encontrar los posibles errores en el software antes de que los encuentre el usuario.
- El reporte de pruebas resulta en una lista de todos los casos de prueba que hayan fallado.
- Existen otros errores que se pueden encontrar de forma manual y también deben ser reportados (usualmente se adicionan a la lista de casos de prueba).

## Slide 5

Título: **Detección del Error**

- Test Case: Creación de Usuario con un email ya registrado.
- Status: Fail.
- Expected Result: Se emite un mensaje de error.
- Actual Result: Se pudo crear el usuario con un email ya registrado.

## Slide 6

Título: **Detección del error**

Contiene un meme (Fry de Futurama entrecerrando los ojos, esquina superior derecha) con el texto: "ESTO ES MUY RARO... EN MI MAQUINA FUNCIONA".

Si el error no está asociado a un Test Case.

- Reproducción del error.
- Tener un conjunto de pasos (mínimos si fuera posible) para repetir el error.
- Construir un nuevo test case.
- Identificar el conjunto de inputs y el estado que producen el error.

## Slide 7

Título: **Errores de lógica**

El software entrega valores equivocados o realiza acciones no esperadas.

Ejemplos:
- El sistema no redujo el stock después de la compra finalizada.
- El usuario hizo logout pero si ingresa al sistema su sesión aún continúa activa.

## Slide 8

Título: **Errores en tiempo de ejecución**

El software no está preparado para una condición y arroja un error inesperado.

Ejemplos:
- División entre cero.
- Excepción de tamaño de array.
- Excepción de variable nula.

## Slide 9

Título: **Errores de integración**

Cuando algún componente externo al software no responde o cambia su interfaz y resulta en un error en el software.

Ejemplo:
- El software requiere enviar un correo de confirmación, pero el servidor de correos falla.
- La conexión a la BD se pierde.

## Slide 10

Título: **Errores de rendimiento**

Incluyen tiempos de respuesta lentos o falta de recursos después de un tiempo de uso.

Ejemplos:
- El sistema demora 5s en responder a un botón y sale un mensaje de error por ese motivo.
- El servidor se reinicia o apaga sin aparentemente razón.

## Slide 11

Título: **Corrección del error - Debugging**

Captura de pantalla de VS Code depurando una app Flask en Python (`app.py`), con anotaciones en verde (flechas señalando cada panel).

Panel izquierdo (RUN AND DEBUG, config "Python: Flask"):
- **VARIABLES → Locals**: `name: 'Sebastian'`, `today: datetime.date(2020, 3, 9)` (expandido: `day: 9`, `max: datetime.date(9999, 12, 31)`, `min: datetime.date(1, 1, 1)`, `month: 3`, `resolution: datetime.timedelta(days=1)`, `year: 2020`). Anotación: *"List of all available variables in the current scope"*.
- **WATCH**: `name: 'Sebastian'`. Anotación: *"You can define some variables that you want to watch all the time"*.
- **CALL STACK**: MainThread PAUSED, Thread-6 PAUSED ON BREAKPOINT, `home  app.py 9:1`.
- **BREAKPOINTS**: Raised Exceptions (off), Uncaught Exceptions (on), `app.py` línea 9 (breakpoint rojo activo).

Editor central (`app.py`):
```python
from flask import Flask
from datetime import date
app = Flask(__name__)

@app.route("/")
def home():                        # Breakpoint (anotación)
    name = "Sebastian"
    today = date.today()
    formatted_today = today.strftime("%d/%m/%Y")   # línea 9, breakpoint amarillo/resaltada

    return f"Hello, {name}! Today is: {formatted_today}"
```
Tooltip flotante sobre la variable `today` mostrando su valor: `datetime.date(2020, 3, 9)` con day/max/min/month/resolution/year. Anotación: *"If you hover your mouse over a variable, you will see its current value"*.

Panel inferior (TERMINAL / DEBUG CONSOLE): salida de arranque de Flask (`* Serving Flask app "app.py"`, `* Environment: development`, `* Debug mode: off`, `* Running on http://127.0.0.1:5000/`). Anotación: *"You can execute any Python code in the DEBUG CONSOLE tab"*.

## Slide 12

Título: **Corrección del error - Logging**

Captura de código Python (fondo oscuro) mostrando uso del módulo `logging`:
```python
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w', ...)


def funcion_problematica():
    # Código de la función problemática
    logging.debug('Iniciando ejecución de la función problemática')

    try:
        # Código problemático que puede lanzar una excepción
        resultado = 10 / 0
    except Exception as e:
        # Registro de la excepción
        logging.error(f'Ocurrió un error: {str(e)}')

    logging.debug('Finalizando ejecución de la función problemática')

# Ejemplo de uso
logging.info('Iniciando programa')
funcion_problematica()
logging.info('Finalizando programa')
```

## Slide 13

Título: **Corrección del error - Pruebas unitarias**

- Las pruebas unitarias ayudan a aislar errores y evitar que vuelvan a suceder.
- Crear una prueba unitaria que falle para el caso de prueba reportado pero considerando el mínimo conjunto de pasos que ocasiona el error.

## Slide 14

Título: **Corrección del error**

- Cambiar el código de forma que se corrija el error.
- Realizar pruebas para confirmar que el error ya no ocurra.
- Realizar pruebas para que la corrección realizada no introduzca nuevos errores.
- Realizar la corrección de forma coherente con la estructura general del sistema.

## Slide 15

Slide de sección (decorativa: mano robótica y globo digital).

# 2. TDD: Test Driven Development

## Slide 16

Título: **Test Driven Development**

- TDD es una técnica en la cual las pruebas son escritas antes del código propiamente dicho.
- Red: Escribir un test que falla.
- Green: Escribir el código mínimo que pase el test.
- Refactor: Mejorar el código conservando el test en estado pass.
- Objetivo: Asegurar que el código funcione sea mantenible y posibilidad de mejora continua.

## Slide 17

Título: **Test Driven Development**

Ejemplo: https://github.com/cpazutec/tdd (Main Branch)

**Paso 1: Basic Test + No-Op Code** (anotación roja con flecha al código):
```python
def quicksort(arr):
    return arr
def test_unsorted_array(self):
    self.assertEqual(quicksort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
```

**Test Fail** (anotación roja con flecha a la salida):
```
AssertionError: Lists differ: [3, 6, 8, 10, 1, 2, 1] != [1, 1, 2, 3, 6, 8, 10]

First differing element 0:
3
1

- [3, 6, 8, 10, 1, 2, 1]
+ [1, 1, 2, 3, 6, 8, 10]

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

## Slide 18

Título: **Test Driven Development**

Ejemplo: https://github.com/cpazutec/tdd (secondversion Branch)

**Paso 3: Improved code** (anotación roja con flecha al código):
```python
def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after the partition
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

    return arr   # This allows us to return the sorted array for convenience
…
```

**Test Pass** (anotación roja con flecha a la salida):
```
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Slide 19

Título: **Test Driven Development** (ventajas/consideraciones)

- Calidad de Código.
- Mejor diseño.
- Facilidad para refactorizar.
- Documentación mejorada por las pruebas.
- Consumo de tiempo para iniciar la implementación.

## Slide 20

Título: **Test Driven Development** (buenas prácticas)

- Escribir tests pequeños.
- Las pruebas deben ser independientes.
- Dar nombres apropiados a los tests.
- Automatizar la ejecución de tests en el pipeline de despliegue.

## Slide 21

Slide de sección (decorativa: mano robótica y globo digital).

# 3. Refactorización

## Slide 22

Título: **Refactorización**

- Refactorización es el proceso de reorganizar o modificar el código fuente de un programa sin cambiar su comportamiento externo.
- El objetivo principal es mejorar la estructura interna del código, haciéndolo más legible, mantenible y escalable.

## Slide 23

Título: **Refactorización – Extracción de Métodos**

Comparación lado a lado (Java) de dos versiones. Una flecha punteada va desde el bloque resaltado (rosado) en version 1 hacia el nuevo método `copyFile` en version 2 (indicando la extracción).

**version 1** (código anidado, bloque `else` resaltado en rosa):
```java
public void copy(File sourceFolder, File destFolder){
    for (File file : sourceFolder.listFiles()) {
        if (file.isDirectory()) {
            //omitted code
        }
        else {
            FileInputStream fis = null;
            FileOutputStream fos = null;
            //omitted code
        }
    }
}
```

**version 2** (la lógica del `else` se extrae a un método `copyFile`; la llamada resaltada en azul, el método nuevo resaltado en rosa):
```java
public void copy(File sourceFolder, File destFolder){
    for (File file : sourceFolder.listFiles()) {
        if (file.isDirectory()) {
            //omitted code
        }
        else {
            copyFile(file, destFile);
        }
    }
}

public void copyFile(File source, File dest) {
    FileInputStream fis = null;
    FileOutputStream fos = null;
    //omitted code
}
```

## Slide 24

Título: **Refactorización – Renombrar**

Tabla de dos columnas comparando antes/después (Python): se renombran variables poco descriptivas por nombres claros.

| Antes | Después |
|-------|---------|
| `def calcular_area(l, w):`<br>`    resultado = l * w`<br>`    return resultado` | `def calcular_area(longitud, ancho):`<br>`    area = longitud * ancho`<br>`    return area` |

## Slide 25

Título: **Refactorización – Reutilizar**

Tabla de dos columnas (pseudocódigo). A la izquierda la condición `if(valor>saldo)` aparece duplicada (resaltada en rojo en ambos métodos); a la derecha `retiro` reutiliza el método `tieneSaldoSuficiente` (línea resaltada en verde).

**Antes (izquierda):**
```
boolean retiro(valor)
  if(valor>saldo)          // rojo (duplicado)
     return false
  saldo = saldo - valor
  return true

boolean tieneSaldoSuficiente(valor)
  if(valor>saldo)          // rojo (duplicado)
     return false
  return true
```

**Después (derecha):**
```
boolean retiro(valor)
  if(tieneSaldoSuficiente(valor) == false)   // verde (reutiliza método)
     return false
  saldo = saldo - valor
  return true

boolean tieneSaldoSuficiente(valor)
  if(valor>saldo)
     return false
  return true
```

## Slide 26

Título: **Refactorización – Extracción de Clases**

Dos diagramas de clase UML lado a lado.

**Antes** — una sola clase con todo mezclado:
```
+-------------------------+
|         Person          |
+-------------------------+
| name                    |
| officeAreaCode          |
| officeNumber            |
+-------------------------+
| getTelephoneNumber()    |
+-------------------------+
```

**Después** — se extrae `TelephoneNumber`; `Person` se asocia a ella (multiplicidad 1, flecha de asociación):
```
+----------------------+          1   +----------------------+
|       Person         |------------->|   TelephoneNumber    |
+----------------------+              +----------------------+
| name                 |              | officeAreaCode       |
+----------------------+              | officeNumber         |
| getTelephoneNumber() |              +----------------------+
+----------------------+              | getTelephoneNumber() |
                                      +----------------------+
```

## Slide 27

Título: **Refactorización – Simplificar condicionales**

Comparación de dos capturas de código (C#, fondo oscuro). Texto rojo superior: *"Invert the conditions and exit early"*. Flecha roja del bloque anidado (izquierda, recuadrado en rojo) hacia la guard clause (derecha, recuadrada en rojo).

**Antes (condicionales anidados):**
```csharp
var miles = 0.0;

if (car.HasFuel)
{
    if (car.EngineWorks)
    {
        var startingMiles = car.Miles;
        car.Drive();
        var endingMiles = car.Miles;
        miles = endingMiles - startingMiles;
    }
}

return miles;
```

**Después (guard clause):**
```csharp
if (!car.HasFuel || !car.EngineWorks)
    return 0.0;

var startingMiles = car.Miles;
car.Drive();
var endingMiles = car.Miles;
return endingMiles - startingMiles;
```

Anotaciones rojas:
- Code smell: Nested conditionals
- Solution: Guard clause refactoring

## Slide 28

Título: **División de métodos o archivos grandes**

(Razones / señales para dividir un método o archivo grande)

- Tiene muchas responsabilidades.
- Dificulta la comprensión.
- Reutilizar código.
- Facilidad para crear un test automático.

## Slide 29

Slide de cierre (decorativa: dos personas con lentes de seguridad trabajando en un laboratorio, fondo azul).

# GRACIAS
CHRISTIAN PAZ TRILLO

## Slide 30

Título: **Práctica**

https://github.com/cpazutec/refactoringvotes

Refactorizar este código y describir las técnicas aplicadas en los comentarios.

Cada técnica diferente les da tres puntos.

## Slide 31

Título: **Práctica de Pruebas Unitarias**

Sobre la implementación del API de Cambio de Monedas:

- Elaborar e implementar pruebas unitarias.
- Elaborar casos de prueba manual con el formato Precondition, Test Steps, Test Data, Expected Result.
- Mostrar que se puedan ejecutar en su aplicación.

Considerar:
- Caso de éxito.
- Casos de falla: transferencia sin saldo, transferencia a usuario que no exista.
