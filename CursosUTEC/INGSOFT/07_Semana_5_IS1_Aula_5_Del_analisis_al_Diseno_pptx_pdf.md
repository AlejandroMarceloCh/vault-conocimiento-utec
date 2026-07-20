---
curso: INGSOFT
titulo: 07 - Semana 5/IS1 - Aula 5 - Del analisis al Diseño__pptx
slides: 20
fuente: 07 - Semana 5/IS1 - Aula 5 - Del analisis al Diseño__pptx.pdf
---

Ingeniería de Software

       Profesor Christian Paz
         Diseño de Software

         Diseño de Arquitectura




Agenda
         Diseño Detallado

         Caso de Estudio
                                               Desarrollo de Software




    Análisis                     Diseño              Implementación            Pruebas                 Despliegue             Mantenimiento


Qué debe    hacer   el   Cómo      se   hará   el   Hacer el Software.   El software hace lo que   Entregar,   poner   en   El software funciona, pero
software?                software?                                       se supone que debe        marcha.                  le falta esto, o está lento,
                                                                         hacer?                                             o necesita mejorar esto.
1.
 Diseño de Software
                                         Diseño
Objetivo:

• Cómo vamos a hacer el software?
• Qué información va a manejar el software y cómo se va a almacenar/transmitir?
• En qué lenguaje? En qué plataformas?
• Cómo va a funcionar el software? Cómo el usuario va a interactuar con él?
• Cómo el equipo se va a organizar para desarrollar el software?
• Cómo el software va a interactuar con otros softwares?
                            Diseño
Partes:

• Diseño de Arquitectura.
• Diseño detallado.
2.
 Diseño de Arquitectura
                      Diseño de Arquitectura
• Representación visual de la estructura y organización de un sistema o aplicación de software.

• Muestra cómo los diferentes componentes de un sistema interactúan entre sí y cómo se
  distribuyen en el entorno de ejecución.

• Facilita la comunicación entre los diferentes participantes del proceso de desarrollo.
                                   Diseño de Arquitectura

Ejemplo:
Arquitectura de Sistema de Ventas de
Entrada de Cine.
Objetivo:
Ver los clientes disponibles.
Que APIs van a ofrecerse.
Mecanismos de almacenamiento:
Cache y RDBMS.
                                     Diseño de Arquitectura

Ejemplo:
Arquitectura de Sistema de Ventas de
Entrada de Cine.
Objetivo:
Ver las plataformas (Nginx, MySQL,
Docker).
Ver los Lenguajes (Vue, NodeJS).
Ver Protocolos (REST, WebSockets).
                                        Diseño de Arquitectura

Ejemplo:
Arquitectura de Sistema de Ventas de
Entrada de Cine.
Objetivo:
Ver los elementos de información y la
interacción entre ellos.
C4

• Modelo de arquitectura en niveles.



• Referencia: https://learning.oreilly.com/library/view/creating-software-with/9798888650219/
  f_0046.xhtml#c4-model.
3.
 Diseño Detallado
                                Diseño Detallado
• Dar mayor detalle a los componentes del Diseño de Arquitectura.

• Conseguir mapear el detalle de los requerimientos a objetos de implementación.

• UX: Interfaz de Usuario (Prototipos en la herramienta final).

• Modelos Estructurales: Datos.

• Modelos de Interacción: Procesos.
                      Modelos Estructurales
• Diagramas de clases, donde inicialmente las clases representan objetos del mundo real.

• Al adicionar más detalles se crean clases para necesidades de implementación.

• Es importante modelar a alto nivel las estructuras de datos de la aplicación para entender como
  se comparten los datos y como serán almacenados.
                                               Modelos
Un Cliente tiene 0 a n cuentas.
Un Cliente usa tarjeta.
Una Cuenta tiene Operaciones.
Una Operación es realizada en un Cajero
Automático.
Un Cajero Automático tiene un Dispensador.

La Tarjeta tiene una operación de validación
de clave.
La Cuenta tiene operación de verificación de
saldo y una de retiro.
                     Modelos de Interacción
• Muestran la interacción entre los actores y los componentes.

• Muestran la interacción entre los objetos del diagrama de clases.

• Muestran el “tiempo de ejecución de una aplicación”.

• Son importantes para entender procesos complejos, que constan de varios pasos.
                                       Modelos
Un Cliente inserta la tarjeta en un
Cajero y se le solicita un PIN.
El Usuario digita el PIN y se valida
si es correcto o no.
El usuario ingresa un monto para
el retiro y se le presenta una lista
de cuentas disponibles.
El usuario selecciona una cuenta y
realiza el retiro.
Se crea la operación y se actualiza
el saldo en la cuenta.
                             Diseño Detallado
• En el Desarrollo Moderno de Software, no resulta necesario hacer un diseño muy detallado
  antes de comenzar a programar.
• Se sugiere tener un modelo estructural muy general que contemple la interacción de las
  entidades más importantes.
• Talvez algunos diagramas de interacción para los flujos más relevantes.
• El resto del diseño detallado se va a modificar tanto durante el desarrollo que es más eficiente
  hacerlo a la par con el desarrollo.
GRACIAS
CHRISTIAN PAZ TRILLO

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
