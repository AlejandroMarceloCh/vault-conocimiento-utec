---
curso: INGSOFT
titulo: 15 - Semana 14/Examen final - IS 1
slides: 0
fuente: 15 - Semana 14/Examen final - IS 1.docx
---

Nombre del docente: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Alumno:

Apellidos: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Nombres: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Sección: \_\_\_\_\_\_ Fecha: \_\_\_\_\_\_\_\_\_\_\_\_\_ Nota:

<u>Indicaciones:</u>

La Duración es de 110 minutos.

La evaluación consta de 3 preguntas.

Se permite el uso de calculadora científica y tablas, copias, apuntes, libros y toda información necesaria.

### Caso de Estudio

Desarrollar un software que implemente un sistema de mensajería basado en el siguiente diseño.

<img src="media/image1.png" style="width:5.90625in;height:4.21181in" />

Se debe soportar las operaciones:

- Contactos: Lista los contactos de un alias con su nombre.

- Contactos: Adicionar un contacto a un usuario (si el usuario no existe, lo adiciona a la “BD”).

- Enviar Mensaje: Envía un mensaje de texto a un contacto (validar que esté en la lista de contactos)..

- Mensajes Recibidos: Muestra la lista de mensajes recibidos por el usuario.

## Pregunta 1 (12 puntos)

En un repositorio Github, desarrollar el código fuente (se recomienda usar Python, pero no es obligatorio) que implemente los endpoints:

/mensajeria/contactos?mialias=XXXX GET

/mensajeria/contactos/{alias} POST

{

“contacto”: “{alias del contacto}”,

“nombre”: “nombre del usuario” //solo relevante si el usuario es nuevo

}

/mensajeria/enviar POST

{

“usuario”: “alias del que envia”,

“contacto”: “alias del destinatario”,

“mensaje”: “texto del mensaje”

}

/mensajeria/recibidos?mialias=XXXX GET

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><p>Guardar la información en memoria, inicializar la aplicación con un conjunto de cuentas y contactos, sin operaciones. Ejemplo:</p>
<p>List&lt;Usuario&gt; BD = new List&lt;Usuario&gt;();</p>
<p>BD.add( new Usuario(“cpaz”, “Christian”, [“lmunoz”, “mgrau”]));</p>
<p>BD.add( new Usuario(“lmunoz”, “Luisa”, [“mgrau”]));</p>
<p>BD.add( new Usuario(“mgrau”, “iguel”, [“cpaz”]));</p></td>
</tr>
<tr>
<td style="text-align: left;">Ejemplo de resultados a los endpoint:</td>
</tr>
<tr>
<td style="text-align: left;"><p>/mensajeria/contactos?mialias=cpaz</p>
<p>lmunoz: Luisa</p>
<p>mgrau: Miguel</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>/mensajeria/enviar</p>
<p>“usuario”: “cpaz”,</p>
<p>“contacto”: “almuno”,</p>
<p>“mensaje”: “texto del mensaje”</p>
<p>}</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>/mensajeria/recibidos?mialias=lmunoz</p>
<p>Christian te escribio “hola” el 11/07/23.</p></td>
</tr>
</tbody>
</table>

### Pregunta 2 (8 puntos)

Realizar 4 pruebas unitarias para un caso de éxito y tres de error. Incluir las pruebas unitarias en el mismo repositorio Github.

Adicionar comentarios en cada prueba indicando el caso de prueba.

Ejecutar el Code Coverage y colocar el reporte indicando la cobertura (100% en la clase Usuario, Contacto y Mensaje)

Usar:

python3 -m coverage <u>run</u>

python3 -m <u>covera</u>ge report
