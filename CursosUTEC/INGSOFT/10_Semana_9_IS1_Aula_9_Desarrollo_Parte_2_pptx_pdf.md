---
curso: INGSOFT
titulo: 10 - Semana 9/IS1 - Aula 9 - Desarrollo - Parte 2__pptx
slides: 27
fuente: 10 - Semana 9/IS1 - Aula 9 - Desarrollo - Parte 2__pptx.pdf
---

## Slide 1

Portada. Título grande: **Ingeniería de Software**. Subtítulo: *Profesor Christian Paz*. Fondo decorativo (silueta caminando por un túnel tecnológico azul), logo UTEC y branding TransformaTec / "Reinventa el mundo".

## Slide 2

Portada de sección. Número grande **1.** con ícono de checklist. Título: **Coding Process**.

Referencia bibliográfica:
- URL: https://learning.oreilly.com/library/view/clean-code-a/9780136083238/
- **Clean Code: A Handbook of Agile Software Craftsmanship** — By Robert C. Martin.

Imagen decorativa: mano robótica tocando un globo terráqueo digital.

## Slide 3

Título: **Proceso de Codificación**

- La actividad de desarrollo es inherentemente colaborativa.
- Cada individuo tiene una forma de programar, pero comparten el mismo código fuente.
- Alinear expectativas, mi código es mejor que el tuyo, o la forma en que tu programas no me gusta.

(Banda superior decorativa: foto de equipo de trabajo frente a computadora.)

## Slide 4

Título: **Proceso de Codificación**

- Existen reglas de codificación: formato, indentación, documentación.
- Existen estándares: uso de determinadas bibliotecas en lugar de otras.
- Tamaño de archivos, de funciones, etc.
- Reglas automáticas y revisión manual.

## Slide 5

Título: **Desafíos**

- Entender que no todos programamos igual.
- Entender que la forma en que yo lo haría no necesariamente es la única.
- Balance entre como lo haría yo y respetar la opinión de los otros.
- El código que yo escribo lo verán todos.

## Slide 6

Título: **Code Review**

- El código es revisado por una o más personas antes de ser introducido al repositorio de código, y un grupo de revisores tienen la responsabilidad de aprobar el cambio.
- Cada componente es revisado por los especialistas en el componente.
- Los aprobadores son personas con más experiencia (Senior).

## Slide 7

Título: **Code Review - Beneficios**

- El cambio es documentado con una explicación del conjunto de archivos modificados.
- Mantener una cierta consistencia en el código.
- Detección de posibles errores.

## Slide 8

Título: **Code Review - Beneficios**

- Asegura que el código es comprensible por otros.
- Minimiza riesgo de introducir código malicioso.
- Compartir conocimiento: sugerencias de cómo mejorar el código y los revisores también aprenden de las ideas de los programadores.

## Slide 9

Título: **Ejemplo de Código**

- Repo: https://github.com/cpazutec/proyecto_distancia
- Uso de Interfaz (dos implementaciones)

## Slide 10

Título: **Ejemplo de Código**

- Pull Request (implementación con otra API): https://github.com/cpazutec/proyecto_distancia/pull/1

## Slide 11

Portada de sección. Número grande **2.** con ícono de checklist. Título: **Design Patterns**.

Referencia: https://learning.oreilly.com/library/view/clean-code-a/9780136083238/ — **Clean Code: A Handbook of Agile Software Craftsmanship** — By Robert C. Martin. Imagen decorativa: mano robótica tocando globo digital.

## Slide 12

Título: **Design Patterns**

- Un patrón es una descripción de un problema y la esencia de su solución, de modo que la solución puede reutilizarse en diferentes configuraciones.
- El primer libro en introducir el concepto en Software OO fue el "Gang of Four".
- Son Plantillas que se pueden aplicar a diversos problemas.

URL: https://refactoring.guru/design-patterns/what-is-pattern

**Visual (no en texto plano):** A la derecha, portada del libro *Design Patterns: Elements of Reusable Object-Oriented Software* (Addison-Wesley Professional Computing Series) de Erich Gamma, Richard Helm, Ralph Johnson y John Vlissides, con "Foreword by Grady Booch" — el famoso "Gang of Four".

## Slide 13

Título: **Design Patterns**

- **Los patrones creacionales** proporcionan mecanismos para la creación de objetos que aumentan la flexibilidad y la reutilización del código existente.
- **Los patrones estructurales** explican cómo ensamblar objetos y clases en estructuras más grandes, manteniéndolas flexibles y eficientes.
- **Los patrones de comportamiento** se encargan de la comunicación efectiva y la asignación de responsabilidades entre objetos.

## Slide 14

Título: **Creacional: Singleton**

Se utiliza cuando se desea que exista sólo una instancia de una clase. Ejemplos: Objeto Compartido.

Source: https://integu.net/singleton-pattern/

**Visual (no en texto plano):** Diagrama dibujado a mano con la analogía de una impresora compartida:
- *Izquierda:* cuatro grupos de empleados ("Employees printing their assignments") con flechas apuntando hacia una única impresora central. Leyenda: "One printer shared between all employees in the office".
- *Centro:* recuadro con dos puntos numerados — (1) "Class can be initialized from anywhere." y (2) "Unnecessary arguments distributed around the system".
- *Derecha:* empleados imprimiendo ("Printing assignments") comparten la impresora distribuyendo el objeto ("Sharing printer through distributing the object"); una impresora adicional aparece tachada con una X ("Additional instance").

## Slide 15

Título: **Estructural: Adapter**

Voy a consumir una API (Client) que espera una determinada estructura (Target).

Tengo una clase que posee los datos necesarios pero con otra estructura (Adaptee).

Creo una nueva clase que "adapta" mi clase original a la estructura esperada por la API (Adapter).

**Visual (no en texto plano):** Ilustración con la analogía del enchufe/adaptador. Tres elementos con bocadillos: un enchufe (**Client** — "Original form of request"), un adaptador de corriente (**Adapter** — "Converts requests to be compatible") y un tomacorriente de pared (**Adaptee** — "External Incompatible"). Una flecha curva conecta Client → Adaptee con el texto: "Client needs to get the service from Adaptee, which is incompatible & cannot interact directly". Pie: *Figure 1 - Adapter Pattern Concept*.

## Slide 16

Título: **Estructural: Adapter**

Solo visual (no hay texto plano). **Diagrama dibujado a mano con la analogía de reservar hoteles:**
- *Izquierda (problema):* un **Developer** con flechas hacia dos hoteles distintos (**Hong Kong** — rascacielos, y **Bali** — templo/pagoda), marcado con una X ("No swapping"). Recuadro: (1) "Require individual interaction for each of the hotels within the same context." (2) "No possibility of swapping between the hotels".
- *Derecha (solución):* etiquetas **Target — Adapter — Adaptee**. Un edificio genérico **HOTEL** (Target) recibe de dos adaptadores (cajas con hotel + ícono específico tachados en diagonal) que envuelven a **Hong Kong** y **Bali** (Adaptee). Leyenda "Common hotel functionalities". Recuadro: (1) "The conversion logics are thereby hidden away inside its own class" (2) "The individual hotels can be swapped between each other".

## Slide 17

Título: **Estructural: Adapter**

Solo visual (no hay texto plano). **Diagrama UML del patrón Adapter:**

```
        <<Interface>>
          HotelTarget
    -----------------------
    printAvailableRooms()
    bookByRoomNymber()
              △
              ┊ implements
              ┊
   ┌──────────────────────┐        Has-a     ┌──────────────────────┐
   │   BaliHotelAdapter    │ ───────────────▶ │      BaliHotel        │
   ├──────────────────────┤                  ├──────────────────────┤
   │ printAvailableRooms() │                  │ getAllAvailableRooms()│
   │ bookByRoomNymber()    │                  │ bookRoom()            │
   └──────────────────────┘                  └──────────────────────┘
```

`BaliHotelAdapter` *implementa* la interfaz `HotelTarget` y *tiene-un* (Has-a) `BaliHotel` al que delega. (Textos tal cual en la slide, incluido el typo "RoomNymber".)

## Slide 18

Título: **Comportamental: Observer**

Establece una relación de uno a muchos entre objetos, donde los cambios de estado en un objeto desencadenan actualizaciones en múltiples objetos dependientes.

**Visual (no en texto plano):** Diagrama del patrón Observer (estilo refactoring.guru). Una clase **Publisher** con campo `- subscribers[]` y método `notifySubscribers()` emite flechas hacia varios **Subscriber** apilados, cada uno con método `+ update()`. Bocadillo del Publisher: *"Guys, I just want to let you know that something has just happened to me."*

## Slide 19

Título: **Comportamental: Observer**

Solo visual (no hay texto plano). **Diagrama UML del ejemplo Observer:**

Interfaz **Publisher** (verde):
```
<<Interface>> Publisher
+ addObserver(Observer): void
+ removeObserver(Observer): void
+ notifyObservers(): void
```
Interfaz **Observer** (verde):
```
<<Interface>> Observer
+ update(int, int): void
```

Clase **LocationTransponder** (implementa Publisher):
```
- xCordinate : int
- yCordinate : int
- observerList: List<Observer>
+ addObserver(Observer): void
+ removeObserver(Observer): void
+ notifyObservers(): void
+ setLocation(int, int): void
```
`LocationTransponder` **uses** la interfaz Observer.

Dos clases implementan **Observer**:
```
LocationTracker              PathDrawer
- currentX : int             - currentX : int
- currentY : int             - currentY : int
+ update(int,int): void      + update(int,int): void
```

Clase cliente **ObserverPatternExample** con `+ main(String []): void`, que **asks** (usa) `LocationTransponder`. (Textos tal cual, incluido typo "xCordinate/yCordinate".)

## Slide 20

Portada de sección. Número grande **3.** con ícono de checklist. Título: **Técnicas de Programación**.

Referencia: https://learning.oreilly.com/library/view/clean-code-a/9780136083238/ — **Clean Code: A Handbook of Agile Software Craftsmanship** — By Robert C. Martin. Imagen decorativa: mano robótica tocando globo digital.

## Slide 21

Título: **Serialización**

Permite convertir un objeto en memoria a una representación que pueda ser transportada o almacenada para uso futuro.

- Guardar estado de un objeto en disco.
- Enviar objetos a través de la red (APIs REST).
- Persistencia de datos en BD no relacionales (MongoDB).
- Comunicación entre sistemas en lenguajes diferentes (Python – C).

## Slide 22

Título: **Serialización - Formatos**

- Json (Java Script Object Notation): Ligero y legible por humanos.
- XML: Estructurado y extensible, pero más pesado.
- Binario (Protobuf, Avro – Apache): No legibles por humano, ligeros.
- CSV: Simple para listas sin jerarquías.

## Slide 23

Título: **Serialización - Ejemplo**

**Visual:** tres recuadros comparando el mismo dato en tres formatos.

JSON:
```json
{
    "nombre": "Lima",
    "pais": "Perú",
    "coordenadas": {
        "latitud": -12.0464,
        "longitud": -77.0428
    }
}
```

XML:
```xml
<ciudad>
    <nombre>Lima</nombre>
    <pais>Perú</pais>
    <coordenadas>
        <latitud>-12.0464</latitud>
        <longitud>-77.0428</longitud>
    </coordenadas>
</ciudad>
```

CSV:
```csv
city,country,lat,lon
Lima,Peru,-12.0464,-77.0428
Cusco,Peru,-13.5319,-71.9675
Arequipa,Peru,-16.409,-71.5375
```

## Slide 24

Título: **Excepciones**

Son condiciones de error o "excepción" en general que deben ser manejadas de forma especial dentro del flujo de código, y normalmente se relacionan con condiciones de excepción detectadas en los casos de uso.

```python
try:
    with open("worldcities.csv") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Proceso de lectura terminado.")
```

## Slide 25

Título: **Excepciones**

Se pueden manejar excepciones propias de la lógica de negocio:

```python
try:
    respuesta = requests.get(url, headers=headers, timeout=5)
    respuesta.raise_for_status()  # Lanza error si status no es 200
    datos = respuesta.json()

    if not datos:
        raise ValueError(f"No se encontraron resultados para {ciudad}, {pais}")
```

## Slide 26

Título: **Excepciones**

O crear excepciones propias:

```python
class CoordenadasInvalidas(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Y usarla así:
if not (-90 <= lat1 <= 90 and -180 <= lon1 <= 180):
    raise CoordenadasInvalidas("Latitud o longitud inválida para ciudad 1")
```

## Slide 27

Cierre. Título grande: **GRACIAS**. Subtítulo: *CHRISTIAN PAZ TRILLO*. Fondo decorativo (foto de laboratorio con dos personas) y branding UTEC / TransformaTec.
