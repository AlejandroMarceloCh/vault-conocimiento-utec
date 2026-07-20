---
curso: BD2
titulo: 02 Organización Física y Almacenamiento
slides: 43
fuente: 02 Organización Física y Almacenamiento.pdf
---

# 02 Organización Física y Almacenamiento

## Índice

- [Organización de Archivos](#organización-de-archivos)
  - [Conceptos fundamentales](#conceptos-fundamentales)
  - [Operaciones básicas en archivos](#operaciones-básicas-en-archivos)
  - [Operaciones básicas en archivos con C++](#operaciones-básicas-en-archivos-con-c)
  - [Operaciones básicas en archivos con Python](#operaciones-básicas-en-archivos-con-python)
- [Modelos de Almacenamiento](#modelos-de-almacenamiento)
  - [Heap Files](#heap-files)
  - [Registros de Longitud Fija](#registros-de-longitud-fija)
  - [Registros de Longitud Variable](#registros-de-longitud-variable)
  - [Comparativa: Longitud Fija vs Variable](#comparativa-longitud-fija-vs-variable)
- [Preguntas](#preguntas)
- [Conclusiones](#conclusiones)
- [Glosario](#glosario)

## Organización de Archivos

File Structures: An object-oriented approach with C++, Michael J. Folk. Addison Wesley, 3rd Edition, 1998.

### Conceptos fundamentales

- ¿Cómo se almacenan realmente los datos en
  una base de datos?
- ¿Por qué algunas consultas son más rápidas
  que otras?
- ¿Cómo impacta la organización de archivos en
  el rendimiento del análisis de datos y machine
  learning?

**Figura:** Slide titulada «Conceptos» en la esquina superior izquierda. En el centro, un recuadro azul redondeado contiene: a la izquierda, un diagrama de flujo con una caja blanca etiquetada «DBMS» y una flecha blanca apuntando a un icono de cilindro (base de datos); a la derecha, las tres preguntas en viñetas con texto blanco. En la parte inferior, imágenes e iconos de medios de almacenamiento: «SSD» (Solid State Drive) con imagen de circuito; «HDD» (Hard Disk Drive) con imagen de disco duro abierto; tarjeta SD, microSD y memoria USB; y tres discos ópticos etiquetados «Blu-ray», «DVD» y «CD».

Tipos de Organización de Archivos

1.   Archivos Secuenciales – Útiles para lecturas masivas (logs, ETL).
2.   Archivos Indexados – Permite búsquedas rápidas.

**Figura:** Slide titulada «Conceptos». Tres diagramas de arquitectura en la parte superior: (1) a la izquierda, «DBMS» con flecha directa hacia un cilindro etiquetado «Hard disk»; (2) en el centro, «DBMS» con flecha hacia «File System», que a su vez apunta a «Hard disk»; (3) a la derecha, una flecha desde «File System» hacia un recuadro verde con el encabezado «10 M table => 20,000 pages» que contiene un diagrama de árbol etiquetado «unix Indexes», con nodos internos rectangulares azules y nodos hoja cuadrados naranjas en la base; flechas señalan los cuadrados naranjas inferiores como «512-byte pages». En la parte inferior, un recuadro enmarcado con el título «Tipos de Organización de Archivos» y la lista numerada de los dos tipos de archivos.

Una base de datos es almacenado
como una colección de archivos.

Cada archivo se organiza en
páginas

Cada página contiene una
secuencia de registros.

Un registro es una secuencia de
campos.

- un archivo ⇔ una tabla
- un registro ⇔ una tupla
- un campo ⇔ una columna

**Figura:** Slide titulada «Conceptos». Columna izquierda con jerarquía descendente en cuatro cajas azul claro redondeadas, cada una con un icono: (1) carpeta — «Una base de datos es almacenado como una colección de archivos.»; (2) documento — «Cada archivo se organiza en páginas»; (3) lista/tabla — «Cada página contiene una secuencia de registros.»; (4) credencial/ID — «Un registro es una secuencia de campos.» Columna derecha con tres viñetas y flechas dobles ($\iff$) que mapean los conceptos físicos a los lógicos.

Key: Es un atributo que identifica de forma única cada registro, como la
clave primaria en una base de datos. Permite acceder rápidamente a la
información y evitar duplicados.

Page: Cuando un archivo es demasiado grande, se divide en páginas
(bloques de igual tamaño) para facilitar su manejo en memoria. Estas
páginas son la unidad de intercambio entre el disco y la memoria
principal, permitiendo operaciones como inserción, modificación,
eliminación y búsqueda.

Index: Es un puntero a un registro en un archivo, que permite acceder a
los datos de forma más rápida y eficiente, evitando búsquedas
secuenciales.

**Figura:** Slide titulada «Conceptos». Tres cajas rectangulares azul claro apiladas verticalmente. (1) Icono de llave azul — definición de «Key» con términos en negrita: «forma única», «acceder rápidamente», «evitar duplicados». (2) Icono de cuadrícula verde 3×3 — definición de «Page» con términos en negrita: «divide en páginas», «de intercambio entre el disco y la memoria». (3) Icono de árbol jerárquico verde — definición de «Index» con término en negrita: «evitando búsquedas secuenciales».

Los archivos pueden ser:

- Archivos de texto
  Guardan datos como caracteres (ej. números
  como "123").
- Archivos binarios
  Almacenan datos en formato binario (ej.
  números en código máquina).

**Figura:** Slide titulada «Conceptos». Encabezado en caja azul: «Los archivos pueden ser:». Debajo, recuadro blanco con borde azul fino que contiene dos viñetas: «Archivos de texto» con su descripción, y «Archivos binarios» con su descripción.

(slides 3–7)

### Operaciones básicas en archivos

Read: Recupera registros de un archivo. Puede ser secuencial
(uno tras otro) o directa (usando un índice o clave). La eficiencia
depende de la estructura del archivo y el uso de buffers.

Write: Agrega registros al archivo. Puede hacerse al final, en una
posición específica, o sobrescribiendo registros existentes. La
reorganización y fragmentación pueden afectar el rendimiento.

Delete: Remueve registros mediante eliminación lógica (marcado
como inactivo) o física (borrado definitivo). Puede requerir
reorganización o reutilización del espacio.

**Figura:** Slide con título grande «Operaciones básicas en archivos» en la parte superior. Tres bloques de texto: «Read» con términos en negrita «secuencial» y «directa»; «Write» con términos en negrita «final», «posición específica» y «sobrescribiendo»; «Delete» resaltado con fondo melocotón claro, con términos en negrita «eliminación lógica» y «física». Acento triangular azul a la izquierda y forma triangular gris a la derecha.

(slide 8)

### Operaciones básicas en archivos con C++

| Class | Contents |
|---|---|
| **filebuf** | Its purpose is to set the file buffers to read and write. Contains **Openprot** constant used in the **open()** of file stream classes. Also contains **close()** and **open()** as members. |
| **fstreambase** | Provides operations common to file streams. Serves as a base for **fstream**, **ifstream** and **ofstream** class. Contains **open()** and **close()** functions. |
| **ifstream** | Provides input operations. Contains **open()** with default input mode. Inherits the functions **get()**, **getline()**, **read()**, **seekg()**, **tellg()** functions from istream. |
| **ofstream** | Provides output operations. Contains **open()** with default output mode. Inherits **put()**, **seekp()**, **tellp()** and **write()** functions from ostream. |
| **fstream** | Provides support for simultaneous input and output operations. Contains open with default input mode. Inherits all the functions from **istream** and **ostream** classes through **iostream**. |

https://www.geeksforgeeks.org/file-handling-c-classes/

**Figura:** Slide titulada «Operaciones básicas en archivos con C++». Tabla de dos columnas («Class» y «Contents») con cinco filas describiendo las clases de manejo de archivos en C++. Enlace en la parte inferior de la tabla. Acento triangular azul decorativo en la esquina superior izquierda.

```cpp
#include <iostream>
#include <fstream>
using namespace std;

struct Datos {
    int numero;
    float decimal;
};

void escribir(const string& archivo, const Datos& datos) {
    ofstream ptrFile(archivo, ios::binary);
    if (ptrFile) {
        ptrFile.write(reinterpret_cast<const char*>(&datos),
                      sizeof(Datos));
        ptrFile.close();
        cout << "Datos guardados en " << archivo;
    } else {
        cerr << "No se pudo abrir el archivo.";
    }
}

int main() {
    Datos datos = {42, 3.14f};
    string archivo = "datos.bin";
    escribir(archivo, datos);
    return 0;
}
```

```cpp
#include <iostream>
#include <fstream>
using namespace std;

struct Datos {
    int numero;
    float decimal;
};

Datos leer(const string& archivo) {
    Datos datos;
    ifstream ptrFile(archivo, ios::binary);
    if (ptrFile) {
        ptrFile.read(reinterpret_cast<char*>(&datos),
                     sizeof(Datos));
        ptrFile.close();
        cout << "Número leído: " << datos.numero;
        cout << "Decimal leído: " << datos.decimal;
    } else {
        cerr << "No se pudo abrir el archivo.";
    }
    return datos;
}

int main() {
    string archivo = "datos.bin";
    leer(archivo);
    return 0;
}
```

**Figura:** Slide titulada «Operaciones básicas en archivos con C++». Dos recuadros azules lado a lado: a la izquierda, código C++ para escribir un struct `Datos` (con campos `int numero` y `float decimal`) a un archivo binario `datos.bin` usando `ofstream`, `reinterpret_cast` y `sizeof(Datos)`; a la derecha, código C++ para leer el struct desde el mismo archivo binario usando `ifstream` y `reinterpret_cast`.

(slides 9–10)

### Operaciones básicas en archivos con Python

```python
import struct
import pickle
import csv
import json
import xml.etree
…
```

File Handling in Python [Complete Series]

**Figura:** Slide titulada «Operaciones básicas en archivos con Python». En el centro, un recuadro redondeado verde azulado oscuro etiquetado «File Operations», del cual irradian diez óvalos naranjas con las operaciones: Create, Open, Read, Write, Delete, Close, Truncate, Flush, Writelines y Change across permission. A la derecha del diagrama, lista de sentencias `import` (struct, pickle, csv, json, xml.etree, …). En la parte inferior izquierda, enlace subrayado «File Handling in Python [Complete Series]». Acento triangular azul en el borde izquierdo.

import
struct

```python
import struct

def escribir(archivo, numero, decimal):
    datos_empaquetados = struct.pack('if', numero, decimal)
    with open(archivo, 'wb') as ptrFile:
        ptrFile.write(datos_empaquetados)
    print(f"Datos guardados en {archivo}")

# Ejemplo de escritura de datos
archivo = 'datos.bin'
escribir(archivo, 42, 3.14)
```

```python
import struct

def leer(archivo):
    with open(archivo, 'rb') as ptrFile:
        contenido = ptrFile.read()
    numero, decimal = struct.unpack('if', contenido)
    print(f"Número leído: {numero}")
    print(f"Decimal leído: {decimal}")
    return numero, decimal

# Ejemplo de lectura de datos
archivo = 'datos.bin'
leer(archivo)
```

https://docs.python.org/3/library/struct.html

**Figura:** Slide titulada «Operaciones básicas en archivos con Python». En la parte superior, diagrama conceptual del módulo `struct`: dos cajas rojas «int» y «float» con flecha hacia un cubo azul etiquetado `pack(...)`, que produce una caja «binary» con filas de 1s y 0s; flecha hacia un icono con cremallera etiquetado `unpack(...)`, que devuelve las cajas «int» y «float». Texto «import struct» prominente a la izquierda del diagrama. En la parte inferior, dos recuadros con código Python: izquierda para empaquetar y escribir datos binarios; derecha para leer y desempaquetar. Enlace a la documentación de Python en la parte inferior izquierda.

import
pickle

```python
import pickle

datos = {
    'nombre': 'Ana',
    'edad': 28,
    'intereses': ['música', 'viajes', 'lectura']
}

with open('datos.pkl', 'wb') as archivo:
    pickle.dump(datos, archivo)

print("Datos guardados exitosamente.")
```

```python
import pickle

# Leer desde archivo binario
with open('datos.pkl', 'rb') as archivo:
    datos_recuperados = pickle.load(archivo)

print("Datos leídos:")
print(datos_recuperados)
```

https://www.geeksforgeeks.org/understanding-python-pickling-example/

**Figura:** Slide titulada «Operaciones básicas en archivos con Python». En la parte superior, diagrama de serialización/deserialización: caja verde «Object» → flecha → caja amarilla «Byte Stream» → flechas hacia tres destinos (icono de archivos «File», cilindro «Database», icono de cabeza con engranaje «Memory»); proceso inverso desde «Database» → «Byte Stream» → «Object». Texto «import pickle» en la parte superior izquierda. En la parte inferior, dos recuadros con código Python: izquierda para serializar un diccionario a `datos.pkl` con `pickle.dump`; derecha para deserializar con `pickle.load`. Enlace a GeeksforGeeks en la parte inferior.

(slides 11–13)

## Modelos de Almacenamiento

1- Registros de Longitud Fija

2- Registros de Longitud Variable

File Structures: An object-oriented approach with C++, Michael J. Folk. Addison Wesley, 3rd Edition, 1998.

### Heap Files

Un heap file es la estructura de almacenamiento más básica: un conjunto de páginas donde los registros se insertan sin orden.

#### Ventajas

- Inserciones rápidas (append al final)
- Estructura simple, sin
  mantenimiento de orden
- Ideal para cargas de trabajo INSERT-
  heavy
- Sin overhead de índice en escritura

#### Desventajas

- Búsqueda secuencial: O(n) páginas
- Sin garantía de orden en recuperación
- Espacio fragmentado con DELETEs
  frecuentes
- Requiere VACUUM para recuperar
  espacio

Ramakrishnan Cap. 8 — Heap File Organization

**Figura:** Slide titulada «Heap Files». Definición en la parte superior. Dos columnas en recuadros: izquierda con borde azul «Ventajas» (cuatro viñetas); derecha con borde naranja «Desventajas» (cuatro viñetas). Referencia «Ramakrishnan Cap. 8 — Heap File Organization» en la parte inferior izquierda. Acento triangular azul en la esquina superior izquierda.

(slide 15)

### Registros de Longitud Fija

#### Definición y tipos PostgreSQL

- Todos los registros en un archivo tienen la misma longitud y cantidad de
  campos

##### Tipo de datos de longitud fija en PostgreSQL

| Tipo de dato | Descripción | Tamaño fijo |
|---|---|---|
| `INTEGER / INT` | Entero de 4 bytes | 4 bytes |
| `SMALLINT` | Entero pequeño | 2 bytes |
| `BIGINT` | Entero grande | 8 bytes |
| `REAL` | Número de punto flotante | 4 bytes |
| `DOUBLE PRECISION` | Número de punto flotante doble | 8 bytes |
| `BOOLEAN` | Verdadero o falso | 1 byte |
| `CHAR(n)` | Cadena de longitud fija | n bytes |
| `DATE` | Fecha (sin hora) | 4 bytes |
| `TIME` | Hora (sin fecha) | 8 bytes |

**Figura:** Slide titulada «Registros de Longitud Fija». Viñeta con la regla principal (términos «la misma longitud y cantidad de campos» en negrita). Tabla de tres columnas con tipos de datos de longitud fija en PostgreSQL y sus tamaños.

(slide 16)

#### Estructura y offset

- Todos los registros en un archivo tienen la misma longitud y cantidad de
  campos.
- Cada campo tiene un tamaño fijo, lo que permite ubicar los valores
  fácilmente, ya que sus posiciones están predeterminadas.

archivo.dat

| Offset | Campo 1 | Campo 2 | Campo 3 | Campo 4 |
|---|---|---|---|---|
| 0 | Howard | Paredes | Zegarra | Computacion |
| 51 | Penny | Vargas | Cordero | Industrial |

Tamaños de campo: 12, 12, 12, 15

$$\text{Offset} = \text{seekg}(\, i \times 51 \,)$$

**Figura:** Slide titulada «Registros de Longitud Fija». Dos viñetas con las reglas de longitud fija. Diagrama de un archivo `archivo.dat` en formato tabla: registro 1 en offset 0 con valores «Howard», «Paredes», «Zegarra», «Computacion» y tamaños de campo 12, 12, 12, 15 bytes respectivamente; registro 2 en offset 51 con valores «Penny», «Vargas», «Cordero», «Industrial» con la misma estructura. Fórmula debajo: `Offset = seekg( i * 51 )`, indicando que cada registro ocupa 51 bytes (12+12+12+15).

(slide 17)

#### Acceso directo

- Como todos los registros tienen el mismo tamaño, es fácil
  calcular su posición exacta y acceder directamente a ellos sin
  necesidad de recorrer todo el archivo.

```cpp
Alumno record;
size = sizeof(record);
offset = i * size;
```

- $i$: posición lógica del
  registro
- $offset$: posición física del
  registro

**Figura:** Slide titulada «Registros de Longitud Fija: Acceso Directo». Texto explicativo con «posición exacta» en negrita. Diagrama de un bloque de memoria continuo dividido en «Record 1» (posiciones 1 a 150) y «Record 2» (posiciones 151 a 300, siguiente sección en 301), cada registro con longitud fija de 150 unidades; leyenda con segmentos «Occupied» (gris oscuro) y «Free» (blanco). Recuadro de código con las variables `Alumno record`, `size = sizeof(record)` y `offset = i * size`. Definiciones: `i` = posición lógica del registro; `size` = tamaño del struct en memoria; `offset` = posición física del registro. Acento triangular azul en el borde izquierdo.

(slide 18)

#### Ejemplo C++ — Archivo de Texto

Record

```cpp
class Alumno
{
public:
    char Nombre [12];
    char Apellidos [12];
    int edad;
};
```

Archivo de Texto

```cpp
void escribirRegistro(const char* filename,
                      const Alumno &record) {
    ofstream file(filename, ios::app);
    file << left << setw(12) << record.Nombre
         << left << setw(12) << record.Apellidos
         << setw(4) << record.edad
         << "\n";
    file.close();
}
```

```cpp
Alumno leerRegistro(const char* filename,
                    int pos) {
    ifstream file(filename);
    Alumno record;
    file.seekg(pos * (12 + 12 + 4 + 1), ios::beg);
    file.read(record.Nombre, 12);
    file.read(record.Apellidos, 12);
    file >> record.edad;
    file.close();
    return record;
}
```

**Figura:** Slide titulada «Registros de Longitud Fija: Ejemplo C++». Columna izquierda con encabezado «Record» y la definición de la clase `Alumno` (campos `char Nombre[12]`, `char Apellidos[12]`, `int edad`). Columna derecha con encabezado «Archivo de Texto»: función `escribirRegistro` que escribe con `setw(12)` para nombre y apellidos, `setw(4)` para edad y salto de línea; función `leerRegistro` que usa `seekg(pos * (12 + 12 + 4 + 1), ios::beg)` para acceder al registro en posición `pos` (tamaño total de registro = 29 bytes).

(slide 19)

#### Ejemplo C++ — Archivo Binario

Record

```cpp
class Alumno
{
public:
    char Nombre [12];
    char Apellidos [12];
    int edad;
};
```

Archivo Binario

```cpp
void escribirRegistro (const char* filename,
                       const Alumno &record)
{
    ofstream file(filename, ios::binary | ios::app);
    file.write((const char*)(&record), sizeof(Alumno));
    file.close();
}
```

```cpp
Alumno leerRegistro (const char* filename,
                     int pos)
{
    ifstream file(filename, ios::binary);
    Alumno record;
    file.seekg(pos * sizeof(Alumno), ios::beg);
    file.read((char*)(&record), sizeof(Alumno));
    file.close();
    return record;
}
```

**Figura:** Slide titulada «Registros de Longitud Fija: Ejemplo C++». Columna izquierda con encabezado «Record» y la misma definición de la clase `Alumno`. Columna derecha con encabezado «Archivo Binario»: función `escribirRegistro` que abre en modo `ios::binary | ios::app` y escribe el bloque de memoria con `file.write((const char*)(&record), sizeof(Alumno))`; función `leerRegistro` que abre en modo binario, posiciona con `seekg(pos * sizeof(Alumno), ios::beg)` y lee con `file.read((char*)(&record), sizeof(Alumno))`.

(slide 20)

#### Ejemplo Python — Archivo de Texto

```python
def escribirRegistro (filename, alumno):
    with open(filename, "a") as file: # Modo append
        # 12+12+3=27 caracteres fijos
        file.write(f"{alumno.nombre:<12}{alumno.apellido:<12}{alumno.edad:03}\n")

def leerRegistro (filename, pos):
    with open(filename, "r") as file:
        file.seek(pos * 27) # Mover el puntero a la posición indicada
        line = file.read(27)
        if line:
            nombre = line[:12].strip()
            apellido = line[12:24].strip()
            edad = int(line[24:27].strip())
            return Alumno(nombre, apellido, edad)
        return None
```

**Figura:** Slide con título «Registros de Longitud Fija: Ejemplo Python» y subtítulo «Archivo de Texto». Muestra dos funciones Python en un bloque de código: `escribirRegistro` abre el archivo en modo append (`"a"`), calcula $12+12+3=27$ caracteres fijos por registro, y escribe nombre (12 chars alineado izquierda), apellido (12 chars) y edad (3 dígitos con cero a la izquierda) seguido de salto de línea; `leerRegistro` abre en modo lectura, hace `seek(pos * 27)` para posicionamiento directo, lee 27 caracteres, extrae los campos por slicing y retorna un objeto `Alumno` o `None`.

(slide 21)

#### Ejemplo Python — Archivo Binario

```python
import struct
FORMAT = '12s12si' # 12 bytes para nombre, 12 para apellido, 4 para edad (int)
RECORD_SIZE = struct.calcsize(FORMAT) # 28 bytes por registro
def escribirRegistro (filename, alumno):
    with open(filename, "ab") as file: # Modo append binary
        record = struct.pack(FORMAT, alumno.nombre.encode(),
                             alumno.apellido.encode(), alumno.edad)
        file.write(record)
def leerRegistro (filename, pos):
    with open(filename, "rb") as file:
        file.seek(pos * RECORD_SIZE) # Posicionamiento directo
        data = file.read(RECORD_SIZE)
        if not data:
            return None
        nombre, apellido, edad = struct.unpack(FORMAT, data)
        return Alumno(nombre.decode().strip(), apellido.decode().strip(), edad)
```

**Figura:** Slide con título «Registros de Longitud Fija: Ejemplo Python» y subtítulo «Archivo Binario». Muestra código Python que usa el módulo `struct`: formato `'12s12si'` (12 bytes string nombre, 12 bytes string apellido, 4 bytes int edad), `RECORD_SIZE = 28 bytes`. `escribirRegistro` abre en modo `"ab"`, empaqueta con `struct.pack` tras `.encode()` de strings. `leerRegistro` abre en `"rb"`, hace `seek(pos * RECORD_SIZE)`, lee `RECORD_SIZE` bytes, desempaqueta con `struct.unpack` y decodifica con `.decode().strip()`.

(slide 22)

#### Problemas

●   Problemas:

    ○ El acceso a los registros es simple pero se corre el riesgo de cruzar bloques.

    ○   La modificación no permite que los registros crucen el límite del bloque.

    ○   ¿Eliminación de registros?

| | Id | Nombre | Ciclo |
|---|---|---|---|
| 1 | P-102 | Andrea | 5 |
| 2 | P-251 | Carlos | 7 |
| 3 | P-412 | Maria | 3 |
| 4 | P-255 | Juan | 7 |
| 5 | P-250 | Javier | 7 |
| 6 | P-312 | Mabel | 3 |
| 7 | P-982 | Saulo | 9 |

**Figura:** Slide con título «Registros de Longitud Fija». A la izquierda, lista de problemas con viñetas (acceso simple pero riesgo de cruzar bloques; modificación no permite cruzar límite del bloque; pregunta en rojo «¿Eliminación de registros?»). A la derecha, tabla de 7 registros con columnas índice (1–7, fondo gris), Id, Nombre y Ciclo; celdas de datos con fondo amarillo claro.

(slide 23)

#### Eliminación — Alternativa 1

●   Alternativa 1:

    ○ Mover los registros $i+1,\ldots,n$ hacia $i,\ldots,n-1$

       ¿En donde mantener el size?

           ¿Complejidad?

| | Id | Nombre | Ciclo |
|---|---|---|---|
| 1 | P-102 | Andrea | 5 |
| 2 | P-251 | Carlos | 7 |
| 3 | P-412 | Maria | 3 |
| 4 | P-255 | Juan | 7 |
| 5 | P-250 | Javier | 7 |
| 6 | P-312 | Mabel | 3 |
| 7 | P-982 | Saulo | 9 |

**Figura:** Slide titulada «Registros de Longitud Fija: Eliminación». Describe Alternativa 1: mover registros $i+1,\ldots,n$ hacia $i,\ldots,n-1$. Preguntas en rojo: «¿En donde mantener el size?» y «¿Complejidad?». Tabla con los 7 registros originales. Entre la columna índice y la columna Id, flechas curvas azules apuntando hacia arriba desde las filas 3→2, 4→3, 5→4, 6→5 y 7→6, indicando desplazamiento al eliminar el registro en posición $i$ (ej. fila 2).

Estado tras la eliminación y desplazamiento:

| | Id | Nombre | Ciclo |
|---|---|---|---|
| 1 | P-102 | Andrea | 5 |
| 2 | P-412 | Maria | 3 |
| 3 | P-255 | Juan | 7 |
| 4 | P-250 | Javier | 7 |
| 5 | P-312 | Mabel | 3 |
| 6 | P-982 | Saulo | 9 |
| 7 | P-982 | Saulo | 9 |

**Figura:** Misma slide de Alternativa 1 pero mostrando el estado tras la eliminación y desplazamiento: el registro P-251 Carlos (fila 2 original) fue eliminado; todos los registros posteriores se desplazaron una posición hacia arriba. La fila 7 conserva P-982 Saulo 9 (duplicado del resultado del desplazamiento). Las preguntas «¿En donde mantener el size?» y «¿Complejidad?» permanecen en rojo.

(slides 24–25)

#### Eliminación — Alternativa 2

●   Alternativa 2:

    ○ Mover el registro $n$ hacia $i$

          ¿Complejidad?

| | Id | Nombre | Ciclo |
|---|---|---|---|
| 1 | P-102 | Andrea | 5 |
| 2 | P-251 | Carlos | 7 |
| 3 | P-412 | Maria | 3 |
| 4 | P-255 | Juan | 7 |
| 5 | P-250 | Javier | 7 |
| 6 | P-312 | Mabel | 3 |
| 7 | P-982 | Saulo | 9 |

**Figura:** Slide de Alternativa 2: «Mover el registro $n$ hacia $i$». Pregunta en rojo «¿Complejidad?». Tabla con 7 registros en estado original. Flecha curva azul desde la fila 7 (Saulo, P-982) apuntando hacia la fila 2 (Carlos, P-251), indicando que el último registro se mueve a la posición del registro eliminado.

Estado resultante:

             Size = 5

| | Id | Nombre | Ciclo |
|---|---|---|---|
| 1 | P-102 | Andrea | 5 |
| 2 | P-982 | Saulo | 9 |
| 3 | P-312 | Mabel | 3 |
| 4 | P-255 | Juan | 7 |
| 5 | P-250 | Javier | 7 |
| 6 | P-312 | Mabel | 3 |
| 7 | P-982 | Saulo | 9 |

**Figura:** Estado resultante de Alternativa 2 tras eliminaciones. Etiqueta roja «Size = 5». Las filas 1–5 (fondo naranja claro) son los registros activos: Andrea, Saulo (movido desde posición 7), Mabel (movida desde posición 6), Juan, Javier. Las filas 6 y 7 están encerradas en un recuadro azul delgado (copias fantasma de Mabel y Saulo); quedan fuera del tamaño lógico (Size = 5).

(slides 26–27)

#### Eliminación — Alternativa 3 (Free List)

●   Alternativa 3:
    ○ No mover registros, pero
      enlazar todos los registros
      liberados en una lista (Free
      List).

Free List: eliminar registros 6, 4 y 1.

**Figura:** Diagrama de una tabla vertical con filas: `header`, `record 0` a `record 8`. Cuatro columnas: las tres primeras contienen datos del registro (Id, nombre/ciudad, valor numérico) y la cuarta columna derecha almacena punteros de la Free List. Registros ocupados: record 0 → A-102 | Perryridge | 400; record 2 → A-215 | Mianus | 700; record 3 → A-101 | Downtown | 500; record 5 → A-201 | Perryridge | 900; record 7 → A-110 | Downtown | 600; record 8 → A-218 | Perryridge | 700. Registros eliminados (record 1, 4, 6) sin datos, fondo gris. Cadena de punteros: header → record 1 → record 4 → record 6 → símbolo de tierra (null).

(slide 28)

#### Free List — Funcionamiento

● Free List:Gestiona espacios de registros eliminados
para su reutilización.
● Cómo funciona:
   1.   El header almacena la dirección del primer registro eliminado.
   2.   Cada registro eliminado guarda la dirección del siguiente.
   3.   Se forma una lista enlazada de espacios reutilizables.
● Optimización: Usar los mismos registros eliminados para almacenar punteros.

Free List: eliminar registros 6, 4 y 1.

**Figura:** Mismo diagrama de Free List que en slide 28: tabla con header y records 0–8, cuatro columnas, punteros encadenados header → record 1 → record 4 → record 6 → null. Registros activos con datos (A-102 Perryridge 400, A-215 Mianus 700, A-101 Downtown 500, A-201 Perryridge 900, A-110 Downtown 600, A-218 Perryridge 700). Records 1, 4 y 6 vacíos y enlazados. Pie: «Free List: eliminar registros 6, 4 y 1.» Texto explicativo a la izquierda con los cuatro bullets sobre funcionamiento y optimización.

(slide 29)

#### Free List — Ejemplo y complejidades

datos.dat

Eliminar 3, 5 y 1

```
-1
```

| | Id | Nombre | Ciclo | NextDel |
|---|---|---|---|---|
| 1 | P-256 | Federico | 1 | 0 |
| 2 | P-251 | Carlos | 7 | 0 |
| 3 | P-412 | Maria | 3 | 0 |
| 4 | P-255 | Juan | 7 | 0 |
| 5 | P-250 | Javier | 7 | 0 |
| 6 | P-312 | Mabel | 3 | 0 |
| 7 | P-982 | Saulo | 9 | 0 |

| | Eliminación | Inserción |
|---|---|---|
| FIFO | $O(\ )$ | $O(\ )$ |
| LIFO | $O(\ )$ | $O(\ )$ |

\* k es total de eliminados

**Figura:** Slide titulada «Free List:». Archivo `datos.dat` con puntero de cabecera `-1` (lista vacía inicialmente). Tabla de 7 registros con columnas Id, Nombre, Ciclo y NextDel (todos NextDel = 0). Instrucción «Eliminar 3, 5 y 1». A la derecha, tabla comparativa de complejidades FIFO y LIFO con casillas vacías para Eliminación e Inserción: $O(\ )$. Nota al pie: «\* k es total de eliminados».

(slide 30)

### Registros de Longitud Variable

#### Definición y tipos PostgreSQL

• Los registros tienen campos cuyo espacio se ajusta al contenido almacenado. Incluyen una cabecera adicional para indicar la longitud.

Tipo de datos de longitud variable en PostgreSQL

| Tipo de dato | Descripción | Tamaño variable |
|---|---|---|
| `VARCHAR(n)` | Cadena de longitud variable | Hasta n bytes + 4 bytes de cabecera |
| `TEXT` | Cadena sin límite de longitud | Según contenido |
| `BYTEA` | Datos binarios | Según contenido |
| `JSON / JSONB` | Datos en formato JSON | Según contenido |
| `ARRAY` | Arreglo de cualquier tipo | Según contenido |
| `NUMERIC / DECIMAL` | Precisión arbitraria | Según precisión |

**Figura:** Slide con título «Registros de Longitud Variable», bullet explicativo sobre campos que se ajustan al contenido con cabecera de longitud. Tabla de seis filas con tipos de datos PostgreSQL de longitud variable (VARCHAR, TEXT, BYTEA, JSON/JSONB, ARRAY, NUMERIC/DECIMAL) con descripción y tamaño variable. Pie: «Tipo de datos de longitud variable en PostgreSQL».

(slide 31)

#### Manejo y métodos de delimitación

El manejo de archivos con registros de longitud variable es una solución en los sistemas de bases de datos para soportar campos de tamaño dinámico, como TEXT, JSON y BYTEA

Ventaja: Permite un uso más eficiente de la memoria, tanto en RAM como en almacenamiento secundario.

Para identificar el inicio y el fin de cada campo o registro, se emplean métodos específicos:

| Delimitadores: Caracteres especiales que separan los campos. | Indicadores de longitud: Valores numéricos que indican el tamaño de cada campo o registro. |
|---|---|

**Figura:** Diagrama de flujo vertical con tres cajas azules conectadas por flechas descendentes. Caja superior: manejo de archivos con registros de longitud variable para campos dinámicos (TEXT, JSON, BYTEA). Caja media: ventaja de uso eficiente de memoria en RAM y almacenamiento secundario. Caja inferior dividida en dos columnas: «Delimitadores» (caracteres especiales que separan campos) e «Indicadores de longitud» (valores numéricos que indican tamaño).

(slide 32)

#### Archivos de Texto

1. Archivos de Texto: Usa caracteres especiales para separar los campos.
 ● Los separadores no deben aparecer dentro de los valores de los campos.
 ● Para ubicar un campo, es necesario recorrer el registro hasta encontrarlo.

```
Howard|Paredes|Zegarra|Computacion|5|1500.50                \n
Penny|Vargas|Cordero|Industrial|2|2850.00                   como separador de registro
```

Problemas:
      ◆ El delimitador es parte del contenido.
      ◆ Acceso directo a un registro.      $O(n)$
      ◆ Eliminar un registro.              $O(n)$

**Figura:** Slide sección «1. Archivos de Texto». Dos registros de ejemplo separados por `|` en un recuadro gris; flecha hacia recuadro punteado indicando `\n` como separador de registro. Recuadro rojo/rosa con borde punteado «Problemas» listando tres inconvenientes con complejidades $O(n)$ para acceso directo y eliminación.

(slide 33)

#### Archivos Binarios

2. Archivos Binarios: Usa indicadores de longitud para definir el tamaño de cada
campo o registro.
  ● El indicador de longitud se coloca al inicio del campo o registro.

  ●   Solo es necesario especificar el tamaño de campos de tipo texto.

```
43:6:Howard7:Paredes7:Zegarra11:Computacion4:58:1500.50
40:5:Penny6:Vargas7:Cordero10:Industrial4:28:2850.00
```

Problemas:
      ◆ El delimitador es parte del contenido
      ◆ Acceso directo a un registro
      ◆ Eliminar un registro

https://www.cs.scranton.edu/~mccloske/courses/cmps340/file_record_storage.html

**Figura:** Slide sección «2. Archivos Binarios». Recuadro gris con dos registros binarios usando indicadores de longitud: registro 1 longitud total 43 con campos 6:Howard, 7:Paredes, 7:Zegarra, 11:Computacion, 4:5, 8:1500.50; registro 2 longitud total 40 con campos 5:Penny, 6:Vargas, 7:Cordero, 10:Industrial, 4:2, 8:2850.00. Recuadro «Problemas» con tres puntos (el primero tachado en la imagen). URL de referencia al pie.

(slide 34)

#### Slotted Page

3. Slotted Page: cabecera que indica el inicio de cada registro

●   Slotted Page contiene:
•    Localización y tamaño de cada registro.
•    El número de registros de entrada.
      ○ El final del espacio libre separado para este encabezado.
●   Para localizar un registro siempre se verifica el encabezado
●   Mantener actualizado el encabezado

http://labe.felk.cvut.cz/~stepan/AE3B33OSD/Lesson10-Data_Access.pdf

**Figura:** Diagrama central de una Slotted Page como rectángulo horizontal dividido en dos zonas. Zona izquierda (contorno azul): cabecera con filas «Size» y «Location», columna «Entries Cnt», varios slots (par Size/Location), área «Free space» y puntero «End of free space pointer» (línea punteada). Zona derecha (contorno naranja): bloques grises de distinto ancho representando registros de longitud variable; flechas desde cada Location en la cabecera apuntan al inicio de cada bloque de datos.

(slide 35)

#### Estructura de una Página — Registros de Longitud Variable

Estructura de una Página - Reg. Long. Variable

Slotted Page
•   Header de página contiene un array de (offset, length)
•   Tuplas se insertan desde el final de la página hacia arriba
•   Permite compactar sin cambiar el RID externo

**Figura:** Diagrama vertical de página dividida en cuatro secciones de arriba a abajo: (1) «Page Header / ItemId Array (Line Pointers)» — amarillo, anotación «Offsets a los tuples»; (2) «Free Space» — gris oscuro, «Espacio disponible»; (3) «Tuple Data (Filas)» — verde, «Datos reales (crece ↑)» con flecha hacia arriba; (4) «Special Space» — azul claro, «B-tree, etc.» A la derecha, tres bullets bajo «Slotted Page» sobre array (offset, length), inserción desde el final hacia arriba, y compactación sin cambiar RID externo.

(slide 36)

#### Demo: Insertar, Leer y Eliminar en SlottedPage

```python
p = SlottedPage()
# Insertar 3 registros (JSON simulado)
s0 = p.insert(b'{id:1,nom:"Ana",dep:"ENG"}')
s1 = p.insert(b'{id:2,nom:"Alejandro García",dep:"MKT"}')
s2 = p.insert(b'{id:3,nom:"Bo",dep:"FIN"}')
print(p._nslots)                      # → 3
print(p.free_space())                 # → 8 003 bytes libres

# Leer por slot_id — O(1) siempre
print(p.read(0)) # b'{id:1,...}'
print(p.read(1))             # b'{id:2,...}'
print(p.read(2))             # b'{id:3,...}'

# Eliminar slot 1 (dead tuple)
p.delete(1)
print(p.read(1))                        # b'' (muerto)

# Slots 0 y 2 siguen válidos e intactos
print(p.read(0))                        # ✓ igual
print(p.read(2))                        # ✓ igual

# Persistir en disco
open('/tmp/pg0.bin','wb').write(p._buf)
```

Estado de la página

| Slot | Estado |
|---|---|
| Slot[0] | (vivo) |
| Slot[1] | (eliminado) |
| Slot[2] | (vivo) |

PAGE HEADER (8B)

FREE SPACE — Aprox. 8003 bytes

| Tuple | Tamaño | Estado |
|---|---|---|
| Tuple 2 | 22B | vivo |
| Tuple 1 * | (eliminado) | * espacio recuperable con compact() |
| Tuple 0 | 31B | vivo |

slot_id es estable incluso tras deletions — compact() reordena físicamente sin cambiar los slot_ids. Los índices no se invalidan.

**Figura:** Slide dividida en dos mitades. Izquierda: bloque de código Python oscuro con operaciones insert/read/delete en `SlottedPage` y persistencia a `/tmp/pg0.bin`. Derecha: diagrama «Estado de la página» con PAGE HEADER (8B) arriba; fila de slots Slot[0] verde (vivo), Slot[1] gris (eliminado), Slot[2] verde (vivo); zona FREE SPACE central (~8003 bytes); abajo tres tuplas creciendo hacia arriba: Tuple 2 (22B, verde), Tuple 1* (gris, eliminado), Tuple 0 (31B, verde). Nota al pie sobre estabilidad de slot_id y compact().

(slide 37)

#### Header independiente

Header independiente

Header.dat

| | Posición | Tamaño |
|---|---|---|
| 1 | 0 | 18 |
| 2 | 18 | 21 |
| 3 | 39 | 20 |
| 4 | 59 | 24 |
| 5 | 83 | 24 |

Datos.txt

| | Codigo\|Nombre\|Apellidos\|Carrera |
|---|---|
| 1 | 001\|Jose\|Lopez\|CS |
| 2 | 002\|Maria\|Vergara\|IN |
| 3 | 003\|Luis\|Vergara\|IN |
| 4 | 004\|Patricia\|Vergara\|IN |
| 5 | 005\|Valentin\|Vergara\|IN |

`seekg(0)` → registro 1

`seekg(18)` → registro 2

`seekg(39)` → registro 3

`seekg(59)` → registro 4

`seekg(83)` → registro 5

Leer el registro i → $T(n) = 1 + 1 = 2$ → $O(1)$

**Figura:** Dos tablas lado a lado. Izquierda `Header.dat` con columnas Posición y Tamaño para 5 registros (offsets 0, 18, 39, 59, 83 y tamaños 18, 21, 20, 24, 24). Derecha `Datos.txt` con registros delimitados por `|` (Codigo|Nombre|Apellidos|Carrera). Flechas azules desde llamadas `seekg(offset)` hacia el inicio de cada registro correspondiente. Fórmula al pie: leer registro $i$ requiere $T(n) = 1 + 1 = 2$ operaciones → $O(1)$.

(slide 38)

#### Slotted Page — Problemas

3. Slotted Page: cabecera que indica el inicio de cada registro

Problemas:
      ◆ El delimitador es un carácter
      ◆ Acceso directo a un registro
      ◆ ¿Eliminar un registro?

**Figura:** Slide con subtítulo «3. Slotted Page: cabecera que indica el inicio de cada registro». Recuadro rosa con borde punteado «Problemas» con tres puntos: los dos primeros tachados («El delimitador es un carácter» y «Acceso directo a un registro»), el tercero en rojo y negrita sin tachar: «¿Eliminar un registro?».

(slide 39)

### Comparativa: Longitud Fija vs Variable

¿Cuándo elegir cada estrategia? Análisis de trade-offs en el diseño de almacenamiento.

| Dimensión | Longitud FIJA | Longitud VARIABLE |
|---|---|---|
| Tamaño en disco | Fijo (padding si campo corto) | Real (sin desperdicio) |
| Acceso a campo i | $O(1)$ — $offset = base + i \times size$ | $O(1)$ — leer offset del header |
| Acceso por slot | $O(1)$ — $slot \times record\_size$ | $O(1)$ — slot descriptor |
| Complejidad implementación | Muy simple (memcpy / struct) | Mayor (header + gestión de gaps) |
| Actualizaciones | Simple si valor mismo tamaño | Puede requerir reubicación |
| Compactación | No necesita | compact() periódico |
| Casos de uso | Números, fechas, enums, tipos fijos | Texto libre, JSON, arrays |
| PostgreSQL usa | int4, float8, date, bool… | VARCHAR, TEXT, JSONB, arrays |

PostgreSQL usa un HÍBRIDO: campos fijos al inicio del tuple (alineados, acceso $O(1)$) y campos variables al final referenciados por tabla de atributos (attbyval/attlen en pg_attribute).

**Figura:** Slide con tabla comparativa de 8 dimensiones entre Longitud FIJA y Longitud VARIABLE, con filas para tamaño en disco, acceso a campo, acceso por slot, complejidad, actualizaciones, compactación, casos de uso y tipos PostgreSQL. Nota al pie sobre enfoque híbrido de PostgreSQL con campos fijos alineados al inicio del tuple y campos variables al final referenciados por `attbyval`/`attlen` en `pg_attribute`.

(slide 40)

## Preguntas

- ¿Qué es el FillFactor en paginas de disco?
- ¿Cuál es el costo de acceso en cada operación?: Scan Secuencial, Búsqueda, Insertar y Eliminar
- ¿Cómo implementar un Heap File en Python/C++ con paginación?

**Figura:** En la parte superior izquierda, el título «Preguntas» en texto grande y negrita con subrayado. Debajo, tres viñetas con las preguntas listadas. En la esquina superior derecha, líneas decorativas punteadas en azul y amarillo. En la parte inferior, líneas decorativas punteadas en azul y amarillo.

(slide 41)

## Conclusiones

### Registros de Longitud Fija:

- Son fáciles de manejar y permiten un acceso rápido y directo a cualquier registro, ya que todos tienen el mismo tamaño.
- Pueden desperdiciar espacio si los campos no se utilizan completamente o la necesidad de truncar la información si el dato excede el tamaño fijo.

### Registros de Longitud Variable:

- Permiten un uso más eficiente del espacio, ya que solo ocupan el espacio necesario para los datos.
- La gestión de estos registros puede ser más compleja, ya que se necesitan métodos específicos para identificar el inicio y el fin de cada campo o registro.

**Figura:** El título central «Conclusiones» en texto grande y negrita con subrayado. Dos secciones con encabezados «Registros de Longitud Fija:» y «Registros de Longitud Variable:», cada una con dos viñetas marcadas con iconos de flecha azul. Líneas decorativas punteadas en azul y amarillo en el borde derecho e inferior.

(slide 42)

## Glosario

- **Key:** Atributo que identifica de forma única cada registro, como la clave primaria en una base de datos. Permite acceder rápidamente a la información y evitar duplicados.
- **Page:** Cuando un archivo es demasiado grande, se divide en páginas (bloques de igual tamaño) para facilitar su manejo en memoria. Estas páginas son la unidad de intercambio entre el disco y la memoria principal, permitiendo operaciones como inserción, modificación, eliminación y búsqueda.
- **Index:** Puntero a un registro en un archivo, que permite acceder a los datos de forma más rápida y eficiente, evitando búsquedas secuenciales.
- **Read:** Recupera registros de un archivo. Puede ser secuencial (uno tras otro) o directa (usando un índice o clave).
- **Write:** Agrega registros al archivo. Puede hacerse al final, en una posición específica, o sobrescribiendo registros existentes.
- **Delete:** Remueve registros mediante eliminación lógica (marcado como inactivo) o física (borrado definitivo).
- **Archivos de texto:** Guardan datos como caracteres (ej. números como "123").
- **Archivos binarios:** Almacenan datos en formato binario (ej. números en código máquina).
- **Heap file:** Estructura de almacenamiento más básica: un conjunto de páginas donde los registros se insertan sin orden.
- **Free List:** Gestiona espacios de registros eliminados para su reutilización. El header almacena la dirección del primer registro eliminado; cada registro eliminado guarda la dirección del siguiente, formando una lista enlazada de espacios reutilizables.
- **Delimitadores:** Caracteres especiales que separan los campos.
- **Indicadores de longitud:** Valores numéricos que indican el tamaño de cada campo o registro.
- **Slotted Page:** Cabecera que indica el inicio de cada registro. Contiene la localización y tamaño de cada registro, el número de registros de entrada, y el final del espacio libre separado para este encabezado.
