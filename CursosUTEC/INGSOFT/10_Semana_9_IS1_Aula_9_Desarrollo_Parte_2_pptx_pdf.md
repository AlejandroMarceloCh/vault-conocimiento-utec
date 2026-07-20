---
curso: INGSOFT
titulo: 10 - Semana 9/IS1 - Aula 9 - Desarrollo - Parte 2__pptx
slides: 27
fuente: 10 - Semana 9/IS1 - Aula 9 - Desarrollo - Parte 2__pptx.pdf
---

Ingeniería de Software

       Profesor Christian Paz
1.
          Coding Process


https://learning.oreilly.com/library/view/clean-code-a/9780136083238/

Clean Code: A Handbook of Agile Software Craftsmanship
queue
By Robert C. Martin
                 Proceso de Codificación

• La actividad de desarrollo es inherentemente colaborativa.

• Cada individuo tiene una forma de programar, pero comparten el mismo código
  fuente.

• Alinear expectativas, mi código es mejor que el tuyo, o la forma en que tu
  programas no me gusta.
                 Proceso de Codificación

• Existen reglas de codificación: formato, indentación, documentación.

• Existen estándares: uso de determinadas bibliotecas en lugar de otras.

• Tamaño de archivos, de funciones, etc.

• Reglas automáticas y revisión manual.
                                 Desafíos

• Entender que no todos programamos igual.

• Entender que la forma en que yo lo haría no necesariamente es la única.

• Balance entre como lo haría yo y respetar la opinión de los otros.

• El código que yo escribo lo verán todos.
                             Code Review

• El código es revisado por una o más personas antes de ser introducido al
  repositorio de código, y un grupo de revisores tienen la responsabilidad de
  aprobar el cambio.

• Cada componente es revisado por los especialistas en el componente.

• Los aprobadores son personas con más experiencia (Senior).
                 Code Review - Beneficios

• El cambio es documentado con una explicación del conjunto de archivos
  modificados.

• Mantener una cierta consistencia en el código.

• Detección de posibles errores.
                 Code Review - Beneficios

• Asegura que el código es comprensible por otros.

• Minimiza riesgo de introducir código malicioso.

• Compartir conocimiento: sugerencias de cómo mejorar el código y los revisores
  también aprenden de las ideas de los programadores.
                       Ejemplo de Código




• Repo:

https://github.com/cpazutec/proyecto_distancia

Uso de Interfaz (dos implementaciones)
                       Ejemplo de Código




• Pull Request (implementación con otra API):



https://github.com/cpazutec/proyecto_distancia/pull/1
2.
          Design Patterns


https://learning.oreilly.com/library/view/clean-code-a/9780136083238/

Clean Code: A Handbook of Agile Software Craftsmanship
queue
By Robert C. Martin
                                  Design Patterns




• Un patrón es una descripción de un problema y la esencia de su solución, de
  modo que la solución puede reutilizarse en diferentes configuraciones.
• El primer libro en introducir el concepto en Software OO fue el "Gang of Four".
• Son Plantillas que se pueden aplicar a diversos problemas.



https://refactoring.guru/design-patterns/what-is-pattern
                                Design Patterns




• Los patrones creacionales proporcionan mecanismos para la creación de objetos
  que aumentan la flexibilidad y la reutilización del código existente.
• Los patrones estructurales explican cómo ensamblar objetos y clases en
  estructuras más grandes, manteniéndolas flexibles y eficientes.
• Los patrones de comportamiento se encargan de la comunicación efectiva y la
  asignación de responsabilidades entre objetos.
                             Creacional: Singleton



Se utiliza cuando se desea que exista sólo una instancia de una clase.
Ejemplos: Objeto Compartido.




                                                                         Source: https://integu.net/singleton-pattern/
                                    Estructural: Adapter




Voy a consumir una API (Client) que espera una
determinada estructura (Target) .

Tengo una clase que posee los datos necesarios pero
con otra estructura (Adaptee).

Creo una nueva clase que “adapta” mi clase original a
la estructura esperada por la API (Adapter).
Estructural: Adapter




                Source: https://integu.net/adapter-pattern/
Estructural: Adapter
                          Comportamental: Observer




Establece una relación de uno a muchos entre objetos,
donde los cambios de estado en un objeto
desencadenan actualizaciones en múltiples objetos
dependientes.
Comportamental: Observer
3.
          Técnicas de
          Programación


https://learning.oreilly.com/library/view/clean-code-a/9780136083238/

Clean Code: A Handbook of Agile Software Craftsmanship
queue
By Robert C. Martin

                                          Serialización




Permite convertir un objeto en memoria a una representación que pueda ser transportada o almacenada para
uso futuro.

- Guardar estado de un objeto en disco.

- Enviar objetos a través de la red (APIs REST).

- Persistencia de datos en BD no relacionales (MongoDB).

- Comunicación entre sistemas en lenguajes diferentes (Python – C).
                              Serialización - Formatos




- Json (Java Script Object Notation): Ligero y legible por humanos.

- XML: Estructurado y extensible, pero más pesado.

- Binario (Protobuf, Avro – Apache): No legibles por humano, ligeros.

- CSV: Simple para listas sin jerarquías.
                                   Serialización - Ejemplo



         {
             "nombre": "Lima",           <ciudad>
             "pais": "Perú",
                                                 <nombre>Lima</nombre>
             "coordenadas": {
                 "latitud": -12.0464,            <pais>Perú</pais>
                 "longitud": -77.0428
                                                 <coordenadas>
             }
                                                     <latitud>-12.0464</latitud>
         }
                                                     <longitud>-77.0428</longitud>
city,country,lat,lon
Lima,Peru,-12.0464,-77.0428                      </coordenadas>
Cusco,Peru,-13.5319,-71.9675
                                            </ciudad>
Arequipa,Peru,-16.409,-71.5375
                                          Excepciones




Son condiciones de error o “excepción” en general que deben ser manejadas de forma especial dentro del flujo
de código, y normalmente se relacionan con condiciones de excepción detectadas en los casos de uso.



          try:
              with open(”worldcities.csv") as archivo:
                   contenido = archivo.read()
          except FileNotFoundError:
              print("El archivo no existe.")
          finally:
              print("Proceso de lectura terminado.")
                                         Excepciones




Se pueden manejar excepciones propias de la lógica de negocio:


     try:
                 respuesta = requests.get(url, headers=headers, timeout=5)
                 respuesta.raise_for_status() # Lanza error si status no es 200
                 datos = respuesta.json()

                 if not datos:
                     raise ValueError(f"No se encontraron resultados para {ciudad}, {pais}")
                                       Excepciones




O crear excepciones propias:


    class CoordenadasInvalidas(Exception):
        def __init__(self, mensaje):
            super().__init__(mensaje)

    # Y usarla así:
    if not (-90 <= lat1 <= 90 and -180 <= lon1 <= 180):
        raise CoordenadasInvalidas("Latitud o longitud inválida para ciudad 1")
GRACIAS
CHRISTIAN PAZ TRILLO

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
