---
curso: BD1
titulo: Clase 10 Seguridad.pptx
slides: 42
fuente: Clase 10 Seguridad.pptx.pdf
---

## Slide 1

Portada del curso (decorativa: fondo tunel digital azul, logo UTEC, banner "Reinventa el mundo").

Título: "Seguridad en la base de datos y acceso programático"
Subtítulo: "CS2041- Base de Datos I" · "Ciclo 2024-1"
Autores: Teófilo Chambilla - tchambilla@utec.edu.pe · Brenner Ojeda - bojeda@utec.edu.pe

## Slide 2

Título: "Índice"
Lista de contenidos del capítulo:
- Error de Capa 8
- Acceso programático
- SQL Dinámico
- Store procedure
- Caso de uso

Imagen decorativa a la derecha: mano robótica sobre mapa del mundo digital (chrome decorativo).

## Slide 3

Diagrama de la malla curricular del curso CS2041 Bases de Datos I (Ciclo 2023-1), mostrando el mapa de temas del curso como una línea de progreso horizontal:

Fila superior (temas de introducción, sin barra de progreso): "Introducción"

Fila de bloques de progreso (barras azules = completado, celeste claro = pendiente), de izquierda a derecha:
- Modelo Relacional
- Algebra Relacional & Cálculo Relacional
- SQL
- (bloque sin etiqueta visible)
- Planificación y — (bloque azul)
- (bloque celeste claro, pendiente) — corresponde a "Seguridad" / "Transacciones y ACID" (recuadros azul claro apilados arriba a la derecha)
- NO SQL/GRAFO (bloque celeste claro, pendiente)

Debajo de cada bloque, subtemas: Entidad-Relación | Actualización, Restricciones | Dependencias funcionales | Optimización de Consultas

A la derecha, dos recuadros apilados en azul claro indicando módulos próximos: "Seguridad" (el módulo de esta clase) y "Transacciones y ACID".
Iconos decorativos: un mago con varita (mascota) y una bandera a cuadros (meta/fin del curso).

## Slide 4

Título: "RESULTADOS DE APRENDIZAJE"
Lista con checkboxes (☐):
- Podrá explicar la seguridad de la base de datos.
- Utilizar correctamente los script al momento de implementar en la aplicación
- Prevenir manipulación de datos por usuarios terceros

Ícono decorativo a la derecha: tablet con engranajes y check verde (ícono de "verificado/configurado").

## Slide 5

Título: "Las preguntas de hoy"

Contiene 3 tablas de ejemplo (esquema de base de datos astronómica) usadas como caso de estudio para las preguntas de la clase:

**Tabla Planeta** (columnas: nombre, dist, radio, grav, días, años, temp, anillo):
| nombre | dist | radio | grav | días | años | temp | anillo |
|---|---|---|---|---|---|---|---|
| Mercurio | 0,39 | 0,38 | 2,8 | 58,646 | 0,241 | 440 | false |
| Venus | 0,72 | 0,95 | 8,9 | -243,019 | 0,615 | 730 | false |
| Tierra | 1,00 | 1,00 | 9,8 | 0,997 | 1,000 | 288 | false |
| Marte | 1,52 | 0,53 | 3,7 | 1,026 | 1,880 | 186 | false |
| Júpiter | 5,20 | 10,97 | 22,9 | 0,414 | 11,862 | 152 | true |
| Saturno | 9,54 | 9,14 | 9,1 | 0,444 | 29,447 | 134 | true |
| Urano | 19,19 | 3,98 | 7,8 | -0,719 | 84,017 | 76 | true |
| Neptuno | 30,07 | 3,86 | 11,0 | 0,671 | 164,791 | 53 | true |

**Tabla Satélite** (columnas: nombre, planeta, descubridor, año):
| nombre | planeta | descubridor | año |
|---|---|---|---|
| Luna | Tierra | ⊥ | ⊥ |
| Ganímedes | Júpiter | Galileo Galilei | 1610 |
| Calisto | Júpiter | Galileo Galilei | 1610 |
| Europa | Júpiter | Galileo Galilei | 1610 |
| Ío | Júpiter | Galileo Galilei | 1610 |
| Titán | Saturno | Christiaan Huygens | 1655 |
| Tritón | Neptuno | William Lassell | 1846 |

**Tabla Aterrizaje** (columnas: nave, planeta, país, año):
| nave | planeta | país | año |
|---|---|---|---|
| Messenger | Mercurio | EEUU | 2015 |
| Venera 3 | Venus | URRS | 1966 |
| Pioneer | Venus | EEUU | 1978 |
| Mars 2 lander | Marte | URRS | 1971 |
| Viking 1 | Marte | EEUU | 1976 |
| Beagle 2 | Marte | ESA | 2003 |
| Galileo | Júpiter | EEUU | 2003 |

Debajo, dos recuadros con las preguntas centrales de la clase:
- "¿Cómo aseguramos la manipulación segura?"
- "Y ¿cómo evitar cambios no permitidos?"

## Slide 6

Slide divisor de sección (fondo azul con foto decorativa de dos investigadores en laboratorio).
Número grande "1" — Título de sección: "ERROR CAPA 8"
Referencia bibliográfica: "Capítulo 6 | Ramakrishnan / Gehrke"

## Slide 7

Diagrama educativo (imagen tomada de Platzi, marca de agua "Platzi" visible) del modelo OSI de 7 capas, representado como pila de capas apiladas en 3D con colores distintos, de arriba hacia abajo:

1. **7. Aplicación** (lila) — "Procesamiento de red a aplicación" — protocolos: DNS, WWW/HTTP, P2P, EMAIL/POP, SMTP, Telnet, FTP. Iconos: navegador Google, monitor, persona.
2. **6. Presentación** (rosado) — "Representación de datos y encriptación" — "Reconocer los datos: HTML, DOC, JPEG, MP3, AVI, Sockets". Iconos: base de datos, personas, routers.
3. **5. Sesión** (violeta) — "Comunicación entre hosts" — "Session establishment in TCP, SIP, RTP, RPC-Named pipes". Iconos: routers/switches.
4. **4. Transporte** (azul) — "Conexiones punto a punto y confiabilidad" — TCP, UDP, SCTP, SSL, TLS. Iconos: personas y routers.
5. **3. Red** (verde lima) — "Definición de ruta y direccionamiento" — IP, ARP, IPsec, ICMP, IGMP, OSPF. Iconos: routers.
6. **2. Enlace de datos** (naranja) — "Direccionamiento físico" — Ethernet, 802.11, MAC/LLC, VLAN, ATM, HDP, Fibre Channel, Frame Relay, HDLC, PPP, Q.921, Token Ring. Iconos: switch, tarjetas MAC.
7. **1. Física** (rojo/rosado) — "Medios de comunicación, señal y transmisión binaria" — RS-232, RJ45, V.34, 100BASE-TX, SDH, DSL, 802.11. Iconos: cable de red.

Flecha vertical a la izquierda indica dirección ascendente de las capas (de física a aplicación). El nombre de la slide alude al chiste "Error de Capa 8": la capa 8 (no existente en el modelo OSI) representa el error humano/usuario.

## Slide 8

Collage de 4 memes humorísticos sobre el "Error de Capa 8" (error del usuario/humano, no técnico):
1. Meme "EL DE SISTEMAS" con foto de Robert Downey Jr. serio, texto: "CUANDO LO LLAMAN POR UN ERROR DE CAPA 8" (marca "TRUE TALENT").
2. Meme de Los Simpson: un hacker encapuchado frente a una pantalla con código, mientras Homero (con cara de asustado) se señala culpable — texto: "ME HACKEARON POR MI CULPA".
3. Meme de Ralph Wiggum (Simpsons) frente a una computadora vieja con pantalla en negro mostrando error "Se cayó el sistttttttttttteeeeeeee -" mientras aprieta una tecla feliz.
4. Captura de un reportaje de noticias (marca de agua "DragonJAR.org") con dos mujeres en un centro de monitoreo con múltiples pantallas, una entrevistada con micrófono, con anotaciones circuladas en rojo sobre notas en una pizarra al fondo.

## Slide 9

Captura de pantalla de un artículo periodístico de La República (Perú), sección Política:
Titular: "Empresas accedían ilegalmente a información de OSCE para ganar millonarios contratos del Estado"
Bajada: "Consorcios conseguían las ofertas que consignaban otras empresas a proyectos del Estado para ofrecer un mejor precio y así ganar las obras. Servicio les podría llegar a costar hasta 30.000 dólares, pero contratos sobrepasaban los centenares de millones de soles."
Lista de titulares relacionados (en rojo):
- "Benji Espinoza: 'Vamos a pedir la nulidad absoluta de la investigación al presidente Castillo'"
- "María del Carmen Alva habría violado la Constitución cuando dijo 'las FF. AA. están con nosotros'"
- "Operador del 'Club del Tarot' implica a Karelim López con los chinos"
- "Congreso: solo pretenden más poder con la bicameralidad"

URL fuente: https://larepublica.pe/politica/2022/06/05/empresas-accedian-ilegalmente-a-informacion-de-la-osce-para-ganar-millonarios-contratos-del-estado/

Es un caso real ilustrando el "error de Capa 8" (acceso ilegal a datos por explotación de vulnerabilidades/procesos, no técnica).

## Slide 10

Slide divisor de sección (fondo azul con foto decorativa de investigadores en laboratorio).
Número grande "2" — Título: "ACCESO PROGRAMÁTICO (JAVA): JAVA DATABASE CONNECTIVITY (JDBC)"
Referencia: "Capítulo 6 | Ramakrishnan / Gehrke"

## Slide 11

Título: "Java Database Connectivity (JDBC)"

Diagrama de arquitectura JDBC (jerarquía en cascada, de arriba a abajo):
- **JAVA APPLICATION** (caja azul, arriba)
  → **JDBC API** (caja roja)
  → **Driver Manager** (caja morada), que se ramifica en 3:
    - **JDBC DRIVER** (roja) → base de datos **ORACLE**
    - **JDBC DRIVER** (roja) → base de datos **MySQL**
    - **JDBC DRIVER** (roja) → base de datos **SYBASE**

Las tres bases de datos (Oracle, MySQL, Sybase) están agrupadas en un recuadro punteado naranja etiquetado "Externas".

## Slide 12

Título: "Veremos el ejemplo ApellidoApp.java"

Bloque de código Java (fragmento de clase de conexión a BD):
```java
public class ApellidoApp {
    private static final String HOST = "245.25.45.84";
    private static final String PORT = "5440";
    private static final String DATABASE = "cc2701";
    private static final String CONNECTION_URL = "jdbc:postgresql://"+HOST+":"+PORT+"/"+DATABASE;
    private static final String USERNAME = "cc3201";
    private static final String PASSWORD = "!_<3_databases";
    private static final String SSL = "true";

    private static final String KILL = "-k";

    public static void main(String[] args) throws SQLException, IOException{
        String url = CONNECTION_URL;

        Properties props = new Properties();
        props.setProperty("user",USERNAME);
        props.setProperty("password",PASSWORD);
        props.setProperty("ssl",SSL);

        // la siguiente propiedad es para deshabilitar la validación de
        // certificados en SSL (normalmente, no se recomienda, pero en el lab,
        // será complejo instalar un certificado en cada truststore)
        props.setProperty("sslfactory","org.postgresql.ssl.NonValidatingFactory");
        Connection conn = DriverManager.getConnection(url, props);
        Statement st = null;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in, "utf-8"));
```
(Nota: los valores de HOST/PORT/USERNAME/PASSWORD son de ejemplo ilustrativo del lab, no credenciales reales de producción.)

## Slide 13

Título: "Consulta vs. Actualización"

- Para hacer consultas (SELECT):
```java
String consulta = "SELECT ...";
ResultSet rs = statement.executeQuery(consulta);
```

- Para hacer actualizaciones (INSERT; UPDATE, …):
```java
String actualizacion = "UPDATE ...";
int tuplasAfectadas = statement.executeUpdate(actualizacion);
```

## Slide 14

Título: "Un problema …"

Dos bloques de código lado a lado ilustrando el mismo problema en dos lenguajes (Java a la izquierda, Python a la derecha en un recuadro oscuro tipo terminal):

Java:
```java
System.out.println("Ingrese un apellido paterno:");
String input = br.readLine().trim();
if(input.equals(KILL)) break;

// crear un statement en blanco
st = conn.createStatement();

// crear la consulta
String consulta = "SELECT * FROM estudiante "
              + "WHERE apellido='"+ input +"'"
              + "ORDER BY nota DESC LIMIT 100";

// ejecutar una consulta
ResultSet rs = st.executeQuery(consulta);
```

Python:
```python
def get_clients():
    conn = None
    try:
        conn = psycopg2.connect(database='x', user='x', password='x')
        cur = conn.cursor()
        cur.execute('select * from clientes;')
        for row in cur.fetchall():
            print(row[0], row[1], row[2])
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
```

Debajo, pregunta y respuesta resaltadas en recuadros punteados:
"¿Hay algún problema aquí?" → "... no hemos 'verificado' el input."

## Slide 15

Título: "Inyección SQL"
Texto: "Un usuario malintencionado puede ingresar un string de entrada para hacer algo inesperado"

Collage de 4 imágenes/memes sobre hackers/ciberseguridad (decorativas, ilustran el concepto de "hacker" pop-culturalmente):
1. Escena de película con hacker manipulando múltiples monitores en un cuarto oscuro con luces verdes/azules.
2. Meme de "gordo comprando PCs" (imgflip.com) en una tienda de electrónica.
3. Reflejo de código verde en lentes de sol de una persona (estética "hacker Matrix").
4. Escena de oficina/laboratorio con dos personas trabajando en un mostrador con equipos.

(No incluye código de ejemplo aún; el código se desarrolla en el slide siguiente.)

## Slide 16

Título: "Inyección SQL"
Texto: "Un usuario malintencionado puede ingresar un string de entrada para hacer algo inesperado"

Cómic de 4 viñetas (xkcd "Exploits of a Mom" / "Little Bobby Tables"), estilo dibujo a mano:
1. "HI, THIS IS YOUR SON'S SCHOOL. WE'RE HAVING SOME COMPUTER TROUBLE." (una mujer al teléfono, otra sentada con una taza)
2. "OH, DEAR – DID HE BREAK SOMETHING?" — "IN A WAY –"
3. "DID YOU REALLY NAME YOUR SON Robert'); DROP TABLE Students;-- ?" — "OH, YES. LITTLE BOBBY TABLES, WE CALL HIM."
4. "WELL, WE'VE LOST THIS YEAR'S STUDENT RECORDS. I HOPE YOU'RE HAPPY." — "AND I HOPE YOU'VE LEARNED TO SANITIZE YOUR DATABASE INPUTS."

Debajo, código SQL mostrando la construcción de la consulta vulnerable y el resultado de la inyección:
```sql
SELECT nota FROM Students WHERE name=''+input+''
SELECT nota FROM Students WHERE name='Robert'); DROP TABLE Students; --'
```
Nota al pie: `('--' empieza un comentario)`

## Slide 17

Título: "Inyección SQL"

Mismo cómic xkcd de Bobby Tables (idéntico al slide 16).

Debajo, variante del código SQL mostrando otro tipo de inyección (bypass de autenticación con `OR 1=1`):
```sql
SELECT nota FROM Students WHERE name=''+input+''
SELECT nota FROM Students WHERE name='Robert' OR 1=1 --'
```
Pregunta/respuesta: "¿Qué hace el ejemplo?" → "¡Devolverá toda la tabla!"

## Slide 18

Título: "Parece estúpido pero …"

Captura de artículo de noticias (estilo Washington Post, sección "WHITE HOUSE"):
Titular: "Mueller report: Russia hacked state databases and voting machine companies"
Subtítulo: "Russian intelligence officers injected malicious SQL code and then ran commands to extract information"
Cuerpo: "The Russian intelligence officers at GRU exploited known vulnerabilities on websites of state and local election offices by injecting malicious SQL code on such websites that then ran commands on underlying databases to extract information. Using those techniques in June 2016, 'the GRU compromised the computer network of the Illinois State Board of Elections by exploiting a vulnerability in the SBOE's website,' the report said. 'The GRU then gained access to a database containing information on millions of registered Illinois voters, and extracted data related to thousands of U.S. voters before the malicious activity was identified.'"

## Slide 19

Título: "Parece estúpido pero …"

Captura de la definición de OWASP sobre "Injection":
"A code injection happens when an attacker sends invalid data to the web application with the intention to make it do something that the application was not designed/programmed to do. Perhaps the most common example around this security vulnerability is the SQL query consuming untrusted data. You can see one of OWASP's examples below:"

Código de ejemplo (vulnerabilidad OWASP):
```java
String query = "SELECT * FROM accounts WHERE custID = '" + request.getParameter("id") + "'";
```
"This query can be exploited by calling up the web page executing it with the following URL: http://example.com/app/accountView?id=' or '1'='1 causing the return of all the rows stored on the database table."

Fuente: OWASP: Open Web Application Security Project — https://sucuri.net/guides/owasp-top-10-security-vulnerabilities-2020/

## Slide 20

Título: "Más ejemplos …"
Enlace: https://en.wikipedia.org/wiki/SQL_injection

Captura de la sección "Examples" de la página de Wikipedia sobre SQL injection (lista larga de incidentes reales de inyección SQL, texto pequeño y denso, con casos como Guess.com 2002, Taiwan security magazine 2005, Rhode Island government 2006, Indian tourism site 2006, Microsoft UK 2007, Kaspersky Malaysia 2008, Maldivian hackers 2013, HBGary 2011, etc.). Imagen decorativa superpuesta: hombre con cara en las manos (facepalm), estilo dibujo lineal.

## Slide 21

Título: "Más ejemplos …"
Enlace: https://en.wikipedia.org/wiki/SQL_injection

Continuación visual del slide anterior: sobre el fondo de la misma lista de Wikipedia (texto denso, parcialmente tapado), se superponen logos de empresas/organizaciones afectadas por inyecciones SQL según los ejemplos de la página:
SONY, YAHOO!, The Pirate Bay, Microsoft, MySQL, 7-Eleven, Royal Navy, HBGary.

## Slide 22

Título: "La historia de HBGary y Anonymous"

Lista cronológica de eventos:
- 2010/12/08: Anonymous empiezan un "DDoS" (denegación de servicio distribuido) contra MasterCard, Visa, etc., por no aceptar donaciones a Wikileaks
- 2011/02/05: Aaron Barr (CEO de HBGary Federal, una empresa de ciberseguridad) dice al Financial Times que ha logrado obtener información sobre las identidades de miembros de Anonymous
- 2011/02/05-06: Anonymous usa inyecciones SQL para obtener todos los datos de usuarios de HBGary, incluyendo hashes de contraseñas, con los cuales (y una tabla arcoíris) pueden hackear las cuentas sociales de Aaron Barr …

A la derecha: logo de HBGary ("Detecting Tomorrow's Threats Today", parte de ManTech International Corporation) y foto de Aaron Barr (hombre de traje).

## Slide 23

Título: "La historia de HBGary y Anonymous"

Captura de pantalla de una cuenta de Twitter comprometida (@aaronbarr), mostrando tweets publicados por los atacantes tras hackear la cuenta, con datos personales expuestos (dirección y número de seguro social, pixelados/ocultados en la captura):
- "Today we taught everyone a lesson. When we actually decide to bite back against those who try to bring us down, we bite back hard. #gameover" (23 minutes ago via web)
- Enlace a vocaroo con texto "Aaron's new resumé amirite #hurrhurr"
- "Spot the edit: [enlace LinkedIn] you Ted Vera, you're not getting away either! Nom nom nom, who's next? Penny? #hbgary"
- "Here's my address: [dato pixelado]"
- "Here's my social security number: [dato pixelado]"

A la derecha, mismo logo de HBGary y foto de Aaron Barr que en el slide anterior.

## Slide 24

Título: "Inyección SQL"

Repetición del cómic xkcd de Bobby Tables (mismas 4 viñetas de slides anteriores).

Código:
```java
String consulta = "SELECT nota FROM Students WHERE name='"+input+"'";
ResultSet rs = statement.executeQuery(consulta);
```
Recuadro: "¿Cómo podemos resolver el problema?"

## Slide 25

Título: "Inyección SQL: ¿escapar los strings?"

Repetición del cómic xkcd de Bobby Tables.

Código mostrando el problema y una posible solución (función "escapar"):
```java
String consulta = "SELECT nota FROM Students WHERE name='"+input+"'";
ResultSet rs = statement.executeQuery(consulta);
```
"¿Cómo podemos resolver el problema?"
```java
String consulta = "SELECT nota FROM Students WHERE name='"+escapar(input)+"'";
ResultSet rs = statement.executeQuery(consulta);
```

Recuadro conclusión (amarillo, con borde punteado naranja): "Mejor, pero sería complicado implementar la función escapar en un lenguaje de programación general y garantizar que prevenga cada tipo de inyección en cada versión (futura) de cada sistema de BdD dado cualquier tipo de consulta y entrada!"

## Slide 26

Slide divisor de sección (fondo azul, foto decorativa de investigadores en laboratorio).
Número grande "3" — Título: "SQL DINÁMICO"
Referencia: "Capítulo 6 | Ramakrishnan / Gehrke"

## Slide 27

Título: "Inyección SQL: ¡sentencias pre-compiladas!"

Repetición del cómic xkcd de Bobby Tables.

Código de solución con PreparedStatement (parámetros posicionales):
```java
String consulta = "SELECT nota FROM Students WHERE name='?'";
// donde ? es un parámetro que reemplazaremos con la entrada del usuario
PreparedStatement ps = conn.prepareStatement(consulta);
ps.setString(1, input);
ResultSet rs = ps.executeQuery();
```
Recuadro conclusión: "Mandamos la consulta al sistema de bases de datos y después se reemplazarán los parámetros con la entrada del usuario"

## Slide 28

Título: "Inyección SQL: ¡sentencias pre-compiladas!"

Código con numeración de pasos (comentarios `// 1`, `// 2`, `// 3`):
```java
String consulta = "SELECT nota FROM Students WHERE name=?";

PreparedStatement ps = conn.prepareStatement(consulta);  // 1
ps.setString(1, input);                                   // 2
ResultSet rs = ps.executeQuery();                          // 3
```

Recuadro naranja "El sistema de base de datos" mostrando el paso 1 (compilación de la sentencia sin la entrada):
```
// 1 :  El sistema de bases de datos compila la sentencia
SELECT nota FROM Students WHERE name=?
                QUERY PLAN
--------------------------------------------------------------
 Seq Scan on Students  (cost=0.00..9654.67 rows=57 width=132)
   Filter: ((name)::text = ?::text)
```
Conclusión: "La consulta es compilada por el sistema sin la entrada"

## Slide 29

Mismo código que el slide 29. Recuadro naranja ahora muestra el paso 2 (reemplazo del parámetro en el plan ya compilado):
```
// 2 :  El sistema de bases de datos reempleza el parametro en el plan
SELECT nota FROM Students WHERE name=?
                QUERY PLAN
--------------------------------------------------------------
 Seq Scan on Students  (cost=0.00..9654.67 rows=57 width=132)
   Filter: ((name)::text = 'Robert'::text)
```
Conclusión: "Se reemplaza el parámetro en la sentencia pre-compilada (que es un plan en memoria, no un string)" — el énfasis está en que el input del usuario nunca se concatena como texto SQL, sino que se inserta como valor de dato en un plan ya compilado, evitando la inyección.

## Slide 30

Mismo código. Recuadro naranja ahora muestra el paso 3 (ejecución del plan) y el resultado de la consulta:
```
// 3 :  El sistema de bases de datos ejecuta el plan
SELECT nota FROM Students WHERE name=?
                QUERY PLAN
--------------------------------------------------------------
 Seq Scan on Students  (cost=0.00..9654.67 rows=57 width=132)
   Filter: ((name)::text = 'Robert'::text)
```
Resultado de la consulta (tabla pequeña):
| nota |
|---|
| 3,7 |

## Slide 31

Título: "Sentencias pre-compiladas"

Código con dos parámetros de distinto tipo y reutilización del PreparedStatement en un bucle:
```java
String consulta = "SELECT nota FROM Students WHERE name=? AND year=?";

PreparedStatement ps = conn.prepareStatement(consulta);
for(String[] input:inputs){
   ps.setString(1, input[1]);
   ps.setInt(2, Integer.parseInt(input[2]));
   ResultSet rs = ps.executeQuery();
   ...
}
```
Dos recuadros amarillos de conclusión:
- "Se puede reutilizar el PreparedStatement varias veces (es más eficiente también: se compila la sentencia sólo una vez)"
- "Se puede tener varios parámetros con varios tipos"

## Slide 32

Slide divisor de sección (fondo azul, foto decorativa de investigadores en laboratorio).
Número grande "4" — Título: "PROCEDIMIENTO ALMACENADO"
Referencia: "Capítulo 6 | Ramakrishnan / Gehrke"

## Slide 33

Diagrama (imagen externa, estilo infografía) titulado "Stored Procedures":
Flujo circular entre tres nodos:
- **App** (icono de monitor) ←→ **SQL Statements** (recuadro central azul con lista de tipos de sentencias: ícono de mano/SELECT, ícono de descarga/INSERT, ícono de flecha circular/UPDATE, ícono de basurero/DELETE) ←→ **RDBMS Database** (icono de servidor de base de datos)

Flechas etiquetadas:
- App → SQL Statements: "Reuse a Stored Procedure"
- SQL Statements → RDBMS Database: "Stored in"
- RDBMS Database → SQL Statements: "SQL Query"
- SQL Statements/RDBMS → App: "Perform a Task"

Ilustra el ciclo de vida de un procedimiento almacenado: la app reutiliza el stored procedure, que está guardado en la base de datos, la base de datos ejecuta el query, y devuelve el resultado (realiza la tarea) a la app.

## Slide 34

Slide divisor de sección (fondo azul, foto decorativa de investigadores en laboratorio).
Número grande "5" — Título: "RESPALDOS"
(sin referencia bibliográfica visible en esta slide, a diferencia de las anteriores)

## Slide 35

Título: "Tipos de respaldo"

Tres iconos en línea, cada uno con su etiqueta debajo, representando los 3 niveles de respaldo:
1. Ícono de base de datos (cilindro apilado) — "Nivel del sistema de base de datos"
2. Ícono de carpeta abierta — "Nivel del sistema de archivos"
3. Ícono de disco duro — "Nivel del hardware"

## Slide 36

Título: "Respaldos EXTERNOS"
Muestra únicamente 2 de los 3 iconos del slide anterior (sistema de archivos y hardware), indicando que los respaldos externos aplican a esos dos niveles: "Nivel del sistema de archivos" y "Nivel del hardware" (sin contenido de texto adicional aún; es introducción del subtema, desarrollado en los slides 37-38).

## Slide 37

Título: "Respaldos EXTERNOS"
Ícono de carpeta (nivel del sistema de archivos) a la izquierda.

Lista con viñetas sobre el método de "usar métodos estándares de respaldar archivos":
- **Usar métodos estándares de respaldar archivos**
  - ✓ Algo simple
  - Solo hay protección ante errores de hardware si se usa otro disco para respaldar la información
  - ✗ En sí, **no provee protección** ante errores humanos o de software (solo respaldará el estado actual)
  - ✗ En general, **habría que detener el sistema de base de datos** para hacer un respaldo "coherente"
  - ✗ **No podemos consultar los respaldos**

(los ítems marcados con ✗ están en rojo, los con ✓ en negro/verde)

## Slide 38

Título: "Respaldos EXTERNOS"
Ícono de disco duro (nivel del hardware) a la izquierda.

Lista con viñetas sobre "Replicar el disco (p.ej., RAID-1) o la máquina":
- **Replicar el disco (p.ej., RAID-1) o la máquina**
  - ✓ Protección ante errores de hardware
  - ✓ Podemos consultar el respaldo (más lecturas)
  - ✓ No es necesario desactivar el sistema de base de datos
  - ✗ Mantener la réplica actualizada **puede tener un costo** (en particular en el caso de usar otra máquina)
  - ✗ En sí, **no provee protección ante errores humanos o de software** (solo respaldará el estado actual)
  - ✗ Existe **el costo de comprar** y mantener el hardware adicional

## Slide 39

Título: "Respaldos Internos - Completos"
Ícono de base de datos (nivel del sistema de base de datos) a la izquierda.

Lista con viñetas:
- **Respaldar todos los datos dentro del sistema de base de datos cada vez (por ejemplo, cada noche)**
  - ✓ No hay que parar el sistema de base de datos
  - ✓ Más fácil de cargar de nuevo
  - ✗ Mantener una historia de copias completas puede ocupar mucho espacio
  - ✗ No podemos consultar los respaldos

## Slide 40

Slide sobre fondo negro con imagen decorativa: escena pixelada del videojuego "Zero Wing" (meme "All your base are belong to us"), personaje con ojo cibernético y capa morada, texto en pantalla: "CATS: ALL YOUR BASE ARE BELONG TO US."
Título: "Preguntas?" (slide humorística de cierre de sección/cuestionario, sin contenido técnico adicional).

## Slide 41

Título: "Resumen"
Lista final con flechas (➔):
- Es importante el uso correctos de los scripts SQL
- El uso de buenas prácticas es fundamental al momento de implementar las aplicaciones
- Velar la integridad de datos es crucial y es responsabilidad del DBA y el Oficial de Seguridad.
- Siempre usar store procedure o consultas precompiladas

## Slide 42

Slide de cierre (decorativa): fondo azul oscuro con globo terráqueo digital y foto de una persona usando lentes de realidad virtual, banner "Reinventa el mundo", logo UTEC.
Texto: "Gracias"
