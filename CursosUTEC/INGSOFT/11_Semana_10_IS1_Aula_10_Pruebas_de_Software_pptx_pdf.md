---
curso: INGSOFT
titulo: 11 - Semana 10/IS1 - Aula 10 - Pruebas de Software__pptx
slides: 28
fuente: 11 - Semana 10/IS1 - Aula 10 - Pruebas de Software__pptx.pdf
---

## Slide 1

Portada (decorativa: fondo azul con silueta de persona junto a robot humanoide en un túnel tecnológico, logo UTEC, "Reinventa el mundo", logo TransformaTec).

**Ingeniería de Software**
Profesor Christian Paz

## Slide 2

Título: **Desarrollo de Software**

Diagrama horizontal tipo timeline: seis círculos azules con íconos conectados por una línea con puntos amarillos, y debajo de cada uno una tarjeta con nombre y descripción. La etapa **Pruebas** está resaltada en amarillo (destacada respecto a las demás grises).

| Etapa (ícono) | Descripción |
|---|---|
| Análisis (diana/objetivo) | ¿Qué debe hacer el software? |
| Diseño (lupa) | ¿Cómo se hará el software? |
| Implementación (cohete) | Hacer el Software. |
| **Pruebas (calendario/checklist)** — resaltada | ¿El software hace lo que se supone que debe hacer? |
| Despliegue (cohete despegando) | Entregar, poner en marcha. |
| Mantenimiento (eslabón/cadena) | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

## Slide 3

Portada de sección (decorativa: mano robótica tocando un globo terráqueo digital al lado derecho).

**1.**
**Pruebas de Software** (con ícono de clipboard/checklist)

## Slide 4

Título: **Pruebas de Software**

- Verificar que cada parte de un software haga lo que se espera que haga.
- Descubrir defectos antes de que el usuario final lo haga.

Cita (recuadro): "Las pruebas pueden mostrar la presencia de errores mas no su ausencia" — Dijkstra, 1992.

## Slide 5

Título: **Inspecciones de Software**

Diagrama de árbol/jerarquía. Nodo raíz "Inspecciones" (redondeado, arriba al centro) del que bajan flechas hacia cinco cajas rectangulares:
- Especificación de requerimientos
- Arquitectura de software
- Modelos de diseño UML
- Esquemas de base de datos
- Programa

Además:
- De "Especificación de requerimientos" baja una flecha a **"Prototipo de sistema"**.
- Un nodo redondeado **"Pruebas"** (abajo a la derecha) tiene una flecha que sube hacia "Programa" y otra flecha que va horizontalmente a la izquierda hacia "Prototipo de sistema".

Texto lateral (arriba derecha):
- En paralelo con el desarrollo.
- No son tan costosas.
- Pueden detectar errores en cada componente sin afectar los otros.
- Verificación estática.

## Slide 6

Título: **Caso de Prueba – Test Case**

- Un caso de prueba es un conjunto de condiciones, variables y secuencia de pasos bajo las cuales un evaluador determinará si un sistema, software o una de sus características funciona correctamente.

## Slide 7

Título: **Proceso de Pruebas de Software**

Diagrama de flujo horizontal (proceso de pruebas). Fila inferior de cajas redondeadas conectadas por flechas de izquierda a derecha:

`Diseñar casos de prueba` → `Preparar datos de prueba` → `Correr el programa con datos de prueba` → `Comparar resultados de casos de prueba`

Encima de cada transición hay una caja de "artefacto" (rectangular) que alimenta el flujo:
- Sobre "Diseñar/Preparar": **Casos de prueba**
- Sobre "Preparar/Correr": **Datos de prueba**
- Sobre "Correr/Comparar": **Resultados de prueba**
- A la derecha del todo: **Reportes de prueba**

Una línea superior conecta "Casos de prueba" con "Comparar resultados", cerrando el ciclo del proceso.

## Slide 8

Portada de sección (decorativa: mano robótica y globo digital, ícono clipboard).

**2.**
**Pruebas durante el Ciclo de Vida**

Referencia bibliográfica (abajo izquierda):
https://learning.oreilly.com/library/view/clean-code-a/9780136083238/
**Clean Code: A Handbook of Agile Software Craftsmanship** — By Robert C. Martin

## Slide 9

Título: **Pruebas durante el ciclo de vida**

- Pruebas de Desarrollo (Desarrolladores y Diseñadores).
- Pruebas de Versión (Equipo de Prueba).
- Pruebas de Usuario (Usuario real o potencial).

## Slide 10

Título: **Pruebas de Desarrollo** (marcador lateral: *Pruebas de desarrollo* resaltado en naranja, luego Pruebas de versión / Pruebas de usuario)

- Pruebas de Unidad:
  - Probar componentes: clases, métodos.
  - Llamar las rutinas con diferentes parámetros.
  - Partes:
    - Inicialización
    - Llamada con valores de entrada (Ejecución)
    - Comparación de valores esperados con valores de salida. (Assert)

Visual (derecha): dos diagramas de piezas de rompecabezas.
- **REAL SYSTEM**: cuadrícula de piezas de puzzle; la mayoría grises, algunas amarillas y una verde en el centro.
  - Green = class in focus
  - Yellow = dependencies
  - Grey = other unrelated classes
- **CLASS IN UNIT TEST**: una pieza verde central rodeada de piezas amarillas (sin las grises).
  - Green = class in focus
  - Yellow = mocks for the unit test

Ilustra que en un test unitario la clase en foco (verde) se aísla y sus dependencias se reemplazan por mocks (amarillo).

## Slide 11

Título: **Pruebas de Desarrollo** (marcador lateral: Pruebas de desarrollo resaltado)

Pruebas de Unidad — ejemplo de código (test unitario, sintaxis Java-like):

```java
TestCuenta {
    void testRetiro100de100() {
        Cuenta c = new Cuenta(mockCliente, 100, Soles);   // <<- Inicializacion
        c.retiro(100, Soles);                             // << - Ejecucion
        AssertEquals(0, c.saldo(), "El saldo no fue actualizado correctamente");  // <- Verificacion o Asercion
    }
}

testRetiro200de500()
```

## Slide 12

Título: **Selección de Datos de Prueba** (marcador lateral: Pruebas de desarrollo resaltado)

Diagrama de particiones de equivalencia (sin texto adicional, solo la figura). Dos óvalos grandes conectados por una caja central "Sistema":

- Óvalo izquierdo = **Entradas posibles**, con varias regiones internas señaladas por flechas desde el rótulo **"Particiones de equivalencia de entrada"**.
- Flecha del óvalo izquierdo → caja **Sistema** → flecha hacia el óvalo derecho.
- Óvalo derecho = **Salidas posibles**, con regiones señaladas por **"Particiones de salida"**; una anotación **"Salidas correctas"** apunta a una región del óvalo derecho.

Idea: elegir datos representativos de cada partición de equivalencia en lugar de probar todas las entradas.

## Slide 13

Título: **Pruebas de Desarrollo** (marcador lateral: Pruebas de desarrollo resaltado)

Pruebas de Componente e Integración:
- Probar diversos puntos de interacción entre clases.
- Validar elementos persistidos.
- Validar formatos de integración entre componentes.

## Slide 14

Título: **Pruebas de Desarrollo** (marcador lateral: Pruebas de desarrollo resaltado)

Columna izquierda — **Beneficios:**
- Cobertura de código.
- Pruebas de regresión.
- Depuración simplificada.

Columna derecha — pseudocódigo del método con líneas resaltadas (para ilustrar cobertura de código; cada línea es una rama a cubrir):

```
Retiro(Cuenta cuenta, Int valor)
    if(valor<=0)
        return valorNoValido        // resaltado verde
    if(cuenta.saldo<valor)
        return saldoInsuficiente    // resaltado cyan
    cuenta.saldo = cuenta.saldo – valor;
    return cuenta.saldo;
```

Cálculo de cobertura (líneas ejecutadas / 6 líneas totales):
- TestRetiro20deCuentaSaldo100  -> 4 / 6 = 66.6%
- TestRetiro0deCuentaSaldo100   -> 2 / 6 = 33.3%
- TestRetiro200deCuentaSaldo100 -> 3 / 6 = 50%

Cobertura Código: 6/6 = 100%

## Slide 15

Título: **Pruebas de Versión** (marcador lateral: *Pruebas de versión* resaltado en naranja)

Texto (derecha):
- Equipo independiente.
- Menos: Descubrir bugs del sistema.
- Más: Comprobar que el sistema cumpla con los requerimientos.

Visual (izquierda): comparación **White Box vs Black Box Testing**.
- Caja blanca rotulada "White Box Testing": Input → (caja) → Output.
- Debajo, en rojo: **Vs**
- Caja negra rotulada "Black Box Testing": Input → (caja) → Output.

Ilustra caja de cristal (se ve el interior/lógica) frente a caja negra (solo entradas y salidas).

## Slide 16

(Marcador lateral: Pruebas de versión resaltado)

- Escenario de Pruebas
- Caso de Pruebas

Tabla ejemplo de casos de prueba (login), cabecera naranja:

| Test Case | Precondition | Test Steps | Test Data | Expected Result |
|---|---|---|---|---|
| Verify login with valid credentials | User should have a network connection | 1. Launch the URL 2. Enter valid username 3. Enter valid password 4. Click on "Login" button | Username: Bill / Password: Truth@14 | User should be able to login successfully |
| Verify login with invalid credentials | User should have network connection | 1. Launch the URL 2. Enter valid username 3. Enter invalid password 4. Click on "Login" button | Username: Jill / Password: adgdgd | User should not be able to login and error message should be shown |

## Slide 17

Título: **Pruebas de versión** (marcador lateral: Pruebas de versión resaltado)

Pruebas de rendimiento:
Son un conjunto de pruebas enfocadas en el rendimiento de la aplicación en condiciones cercanas (o que exceden) las condiciones a las que la aplicación estará sometida durante su vida útil, principalmente en condiciones de alto uso. Ejemplos:
- X / TikTok durante un evento (elección del Papa).
- Teleticket al abrir las entradas de un evento.

Herramientas: Jmeter, Locust.

## Slide 18

Título: **Pruebas de versión** (marcador lateral: Pruebas de versión resaltado)

Pruebas de rendimiento - **Load Testing**
Ver cómo se comporta el sistema bajo una carga específica de usuarios concurrentes o transacciones.

Ejemplo:
Simular 1000 usuarios accediendo simultáneamente a una aplicación web para ver si el tiempo de respuesta se mantiene por debajo de 2 segundos.

## Slide 19

Título: **Pruebas de versión** (marcador lateral: Pruebas de versión resaltado)

Pruebas de rendimiento - **Stress Testing**
Determinar el punto de ruptura del sistema llevándolo más allá de su capacidad máxima esperada.

Ejemplo:
Aumentar gradualmente los usuarios concurrentes hasta que el sistema se ralentiza o se bloquea, para identificar el máximo que puede manejar.

## Slide 20

Título: **Pruebas de versión** (marcador lateral: Pruebas de versión resaltado)

Pruebas de rendimiento - **Scalability Testing**
Evaluar la capacidad del sistema de escalar horizontal o verticalmente (más usuarios, más datos, más nodos).

Ejemplo:
Ver si agregar más instancias de servidor reduce el tiempo de respuesta al aumentar los usuarios de 100 a 10000.

## Slide 21

Título: **Pruebas de versión** (marcador lateral: Pruebas de versión resaltado)

Pruebas de rendimiento - **Soak Testing (Duración)**
Probar la estabilidad del sistema bajo carga sostenida durante un periodo prolongado.

Ejemplo:
Ejecutar la aplicación con 500 usuarios durante 48 horas continuas para ver si hay fugas de memoria, errores, o degradación.

## Slide 22

Título: **Pruebas de versión** (marcador lateral: Pruebas de versión resaltado)

Pruebas de rendimiento - **Volume Testing**
Evaluar el rendimiento del sistema con grandes volúmenes de datos.

Ejemplo:
Cargar 10 millones de registros en una base de datos y luego ejecutar búsquedas para medir el rendimiento de las consultas.

## Slide 23

Título: **Pruebas de versión** (marcador lateral: Pruebas de versión resaltado)

Pruebas de rendimiento - **Concurrency Testing**
Analizar cómo se comporta el sistema cuando múltiples usuarios acceden y modifican los mismos recursos al mismo tiempo.

Ejemplo:
100 usuarios actualizan el mismo perfil de usuario simultáneamente para verificar problemas de bloqueo o pérdida de datos.

## Slide 24

Título: **Pruebas de versión** (marcador lateral: Pruebas de versión resaltado)

Pruebas de seguridad:
- Validar que un sistema no sea vulnerable.
- Detectar que los puntos del sistema que son accesibles sin autorización sean solo los esperados.
- Detectar como reaccionan los puntos del sistema a ataques (datos falsos, inyecciones SQL).

## Slide 25

Título: **Pruebas de usuario** (marcador lateral: *Pruebas de usuario* resaltado en naranja)

- Pruebas Alfa: Con asistencia del equipo de desarrollo.
- Pruebas Beta: Libre acceso a los usuarios.
- Pruebas de Aceptación: Pruebas que permitirán decidir si la versión está aceptable para ser desplegada en el entorno del cliente.

## Slide 26

Título: **Pruebas de usuario** (marcador lateral: Pruebas de usuario resaltado)

- Criterios de aceptación.
- Plan de pruebas de aceptación.
- Ejecutar pruebas de aceptación
- Negociar los resultados de las pruebas.
- Rechazo / Aceptación de la versión.

## Slide 27

Título: **Práctica de Pruebas Unitarias**

Sobre el programa de la semana pasada (distancia entre ciudades):
- Elaborar e implementar pruebas unitarias.
- Elaborar casos de prueba manual con el formato Precondition, Test Steps, Test Data, Expected Result.
- Mostrar que se puedan ejecutar en su aplicación.

Considerar:
- Caso de éxito.
- 2 Casos extremos: una de las ciudades no exista y entregar la misma ciudad dos veces.

## Slide 28

Cierre (decorativa: foto de dos personas en laboratorio con bata blanca y gafas de seguridad, fondo azul).

**GRACIAS**
CHRISTIAN PAZ TRILLO
