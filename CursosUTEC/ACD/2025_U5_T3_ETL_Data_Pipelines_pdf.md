---
curso: ACD
titulo: [2025] U5_T3 ETL Data Pipelines
slides: 25
fuente: [2025] U5_T3 ETL Data Pipelines.pdf
---

## Slide 1

Portada decorativa: título "ETL Data Pipelines", curso "DS3021 Análisis Computacional de Datos", autor "Mg. José Espinoza Melgarejo". Fondo con imagen decorativa (túnel digital con silueta de persona). Logos UTEC/TransformaTec decorativos.

## Slide 2

"Objetivo de sesión": Al finalizar esta sesión el estudiante implementará un proceso ETL a partir de diferentes fuentes de datos. Imagen decorativa lateral (dos personas trabajando en oficina, en tono azul).

## Slide 3

Slide título de unidad: "U5_L1: ETL Data Pipelines". Imagen decorativa de fondo (dos personas con bata de laboratorio observando equipo electrónico).

## Slide 4

Slide separador: "Parte I: Configuración y creación del proyecto". Imagen decorativa (mano robótica tocando un holograma del planeta).

## Slide 5

**Paso 0: Crear las tablas**

Texto: Primero abriremos SQL Server y crearemos una base de datos llamada 'STG_NW'. Luego, crearemos las estructuras de las tablas 'Empleados', 'Categorias', 'Proveedores' y 'Productos' a partir del archivo 'SQL_Landing_Estructuras_Tablas'.

Captura de pantalla: dos pestañas de script SQL abiertas en SSMS ('SQL_Landing_Estruc...', 'script_Ventas_Dato...'). Código SQL visible:

```sql
--Creando BD Landing o Stagging
create database STG_NW
go

use STG_NW
go

--Estructura tabla Empleados
CREATE TABLE [empleados] (
    [EmployeeID] varchar(50),
    [LastName] varchar(50),
    [FirstName] varchar(50),
    ...
```

## Slide 6

**Paso 1: Verificar extensiones**

Texto: Abrimos Visual Studio y buscamos el botón para crear un proyecto. Buscamos la opción 'Integration Services Project' y en caso no figure, le damos al botón 'Atrás' y elegimos la opción 'Continuar sin código'.

Dos capturas de pantalla lado a lado:
- Izquierda: ventana "Visual Studio 2019" con panel "Abrir recientes" y "Tareas iniciales" (Clonar un repositorio, Abrir un proyecto o una solución, Abrir una carpeta local, Crear un proyecto). Botón "Continuar sin código" resaltado con recuadro rojo en la parte inferior.
- Derecha: ventana "Crear un proyecto" con buscador de plantillas, filtros por lenguaje/plataforma/tipo, y lista de plantillas recientes (Aplicación web ASP.NET, Servicio en la nube de Azure, Solución en blanco, Aplicación de consola .NET Framework, etc.).

## Slide 7

**Paso 2: Instalar extensiones**

Texto: En la pestaña 'Extensiones' elegimos 'Administrar extensiones' y descargamos e instalamos 'SQL Server Integration Services Projects', 'Microsoft Reporting Services Projects' y 'Microsoft Analysis Services Projects'.

Captura de pantalla: ventana "Administrar extensiones" con árbol lateral (Instalado, En línea > Visual Studio Marketplace, Actualizaciones, Roaming Extension Manager). Lista de extensiones disponibles: GitHub Extension for Visual Studio, Microsoft Visual Studio Installer Projects, ReSharper, CodeMaid, y resaltada con recuadro rojo y flecha azul: "SQL Server Integration Services Projects" (Microsoft) - descripción "This project may be used for building high performance data integration and workflow solutions, including extraction, transforma...". Panel derecho muestra detalles: Creado por GitHub, Versión 2.11.106.19330, Installs 2643054, Categoría de precios Gratis, Clasificación (104 votos).

## Slide 8

**Paso 3: Crear proyecto**

Texto: Creamos el proyecto con la opción 'Integration Services Project' y le damos un nombre.

Dos capturas de pantalla:
- Izquierda: ventana "Crear un proyecto" con buscador "inte" y resultado resaltado en recuadro rojo con flecha azul: "Integration Services Project" — descripción "This project may be used for building high performance da[ta] workflow solutions that can be run on SSIS catalog, includi[ng] transformation, and loading (ETL) operations for data war[ehouses]". Debajo, dos opciones más: "Integration Services Project (Azure-Enabled)" e "Integration Services Import Project Wizard".
- Derecha: ventana "Configure su nuevo proyecto" con campos: Nombre del proyecto = "ETL_STG_NW", Ubicación = "C:\Users\jespinozame\source\repos", Nombre de la solución = "ETL_STG_NW", checkbox "Colocar la solución y el proyecto en el mismo directorio" (sin marcar).

## Slide 9

Slide separador: "Parte II: Creación de tareas y flujos de datos". Imagen decorativa (mano robótica tocando holograma del planeta, igual estilo que slide 4).

## Slide 10

**Paso 4: Crear y configurar tareas**

Texto: Una vez abierto el proyecto, arrastramos en el área de trabajo la herramienta 'Tarea Ejecutar SQL'. Hacemos doble clic izquierdo y le podemos asignar un nombre desde el apartado 'General', asimismo, en 'Instrucción SQL' estableceremos una nueva conexión.

Dos capturas de pantalla:
- Superior: panel "Cuadro de herramientas de SSIS" con lista (Favoritos: Tarea Ejecutar SQL resaltada, Tarea Flujo de datos; Comunes: Tarea de expresión, Tarea de generación de..., Tarea de procesamiento...) junto a área de diseño "Package.dtsx [Diseño]" con pestañas (Flujo de control, Flujo de datos, Parámetros, Controladores de event..., Explorador de paque...) mostrando un nodo "Limpiar tablas" con icono de tarea SQL.
- Inferior: panel de propiedades con árbol (General, Asignación de parámetros, Conjunto de resultados, Expresiones) y tabla de propiedades: Conjunto de resultados=Ninguno, Name=Limpiar tablas, Description=Tarea Ejecutar SQL, Instrucción SQL > ConnectionType=OLE DB, Connection=<Nueva conexión..> (resaltado), SQLSourceType, SQLStatement, IsQueryStoredProcedure=False, BypassPrepare=True, Opciones > TimeOut=0, CodePage=1252, TypeConversionMode=Permitido.

## Slide 11

**Paso 5: Buscar base de datos**

Texto: Configuramos el proveedor y colocamos el nombre del servidor que tenemos en SQL Server, y buscar la base de datos 'STG_NW'. Además, limpiamos las tablas con 'delete'.

Dos capturas de pantalla:
- Izquierda: ventana de conexión con Proveedor="OLE DB nativo\Microsoft OLE DB Provider for SQL Server" (resaltado en rojo), Nombre del servidor="LPDOC20219\SQLEXPRESS", Autenticación="Autenticación de Windows", y sección "Establecer conexión con una base de datos" con "Seleccionar o escribir el nombre de la base de datos" = "STG_NW".
- Derecha: panel de propiedades similar al anterior con ventana emergente "Escribir consulta SQL" mostrando el código:
```sql
delete empleados;
delete categorias;
delete proveedores;
delete productos;
```

## Slide 12

Continuación del Paso 5 (sin número de paso nuevo en el título, es la config final).

Texto: La configuración final de la tarea debería quedar como en la imagen mostrada, con la opción 'BypassPrepare' tomando como valor 'False'.

Captura de pantalla: panel de propiedades de la tarea "Tarea Ejecutar SQL" con árbol (General, Asignación de parámetros, Conjunto de resultados, Expresiones) y tabla: Name=Limpiar tablas, Description=Tarea Ejecutar SQL, ConnectionType=OLE DB, Connection=LPDOC20219\SQLEXPRESS.STG_NW, SQLSourceType=Entrada directa, SQLStatement=delete empleados;delete categorias;delete..., IsQueryStoredProcedure=False, BypassPrepare=False (resaltado en azul), Opciones > TimeOut=0, CodePage=1252, TypeConversionMode=Permitido. Descripción de ayuda: "BypassPrepare - Indica si la tarea debe preparar la consulta antes de ejecutarla." Botones Examinar, Generar consulta, Analizar consulta, Aceptar/Cancelar/Ayuda.

## Slide 13

**Paso 6: Crear y configurar tareas de flujo de datos**

Texto: Arrastramos en el área de trabajo la herramienta 'Tarea Flujo de datos' y entramos a esta. Luego, arrastramos la herramienta 'Asistente de orígenes' y cuando ingresamos seleccionamos como tipo de origen 'Excel' y en la parte derecha la opción 'Nueva'.

Dos capturas de pantalla:
- Superior: área de diseño "Flujo de control" con dos nodos conectados por flecha verde: "Limpiar tablas" → "Categorias" (icono de base de datos).
- Inferior: ventana "Asistente de orígenes - Agregar nuevo origen" con lista "Seleccionar tipo de origen": SQL Server, Excel (resaltado/seleccionado), Flat File, Oracle; y panel derecho "Seleccionar administradores de conexiones" con "Nueva..." resaltado en azul.

## Slide 14

Continuación del paso 6 (sin título de paso nuevo).

Texto: Buscamos la ubicación de nuestro archivo de Excel, para luego darle al botón 'Aceptar'. Luego, volvemos a entrar a nuestro asistente de orígenes que ahora será de tipo Excel y buscamos la tabla 'categorias'.

Dos capturas de pantalla:
- Superior: ventana "Administrador de conexiones con Excel" con campo "Ruta de acceso del archivo Excel" = "D:\Documentos\Descargas\dataBI\almacen.xls" (resaltado con flecha azul) y "Versión de Excel" = "Microsoft Excel 97-2003", botón "Examinar...".
- Inferior: ventana de asistente de orígenes Excel con árbol (Administrador de co..., Columnas, Salida de error), "Excel connection manager" = "Administrador de conexiones con Excel", "Modo de acceso a datos" = "Tabla o vista", "Name of the Excel sheet" = "Categories" (resaltado con flecha azul).

## Slide 15

**Paso 7: Agregar conversión de datos**

Texto: En la pestaña 'Columnas', nos aseguramos de que se hayan seleccionado todas. Agregamos la herramienta Conversión de datos y lo conectamos con nuestro archivo de orígenes con los ajustes mostrados.

Dos capturas de pantalla:
- Izquierda: pestaña "Columnas" con lista "Columnas externas dis..." (Nombre, CategoryID, CategoryName todas marcadas) y tabla mapeo Columna externa → Columna de salida: CategoryID→CategoryID, CategoryName→CategoryName, Description→Description.
- Derecha: ventana "Data Conversion Transformation Editor" con lista "Columnas de entrada di..." (Nombre, CategoryID, CategoryName, Description) y tabla: Input Column=Description → Output Alias="Copy of Description", Data Type="cadena Unicode [DT_...", Length=100; Input Column=CategoryName → Output Alias="Copy of CategoryNa...", Length=250.

## Slide 16

**Paso 8: Agregar destino de OLE DB**

Texto: Añadimos la herramienta Destino de OLE DB. Entramos en esta y seleccionamos la tabla 'categorias'. En la pestaña 'Asignaciones', indicamos qué campos serán utilizados para la recepción de los datos.

Dos capturas de pantalla:
- Izquierda: ventana con árbol (Administrador de co..., Asignaciones, Salida de error) y config: "Administrador de conexiones OLE DB" = "LPDOC20219\SQLEXPRESS.STG_NW", "Modo de acceso a datos" = "Carga rápida de tabla o vista", "Nombre de la tabla o la vista" = "[dbo].[categorias]", checkboxes Mantener valores de/NULL (sin marcar), Bloqueo de tabla/Comprobar restricciones (marcados), Filas por lote (vacío), Tamaño máximo de confirmación = 2147483647.
- Derecha: pestaña "Asignaciones" mostrando diagrama de líneas conectando "Columnas de entrada disp..." (Nombre, CategoryID, CategoryName, Description, Copy of Description) con "Columnas de desti..." (Nombre, CategoryID, CategoryName, Description). Tabla debajo: Columna de entrada → Columna de destino: CategoryID→CategoryID, Copy of CategoryName→CategoryName, Copy of Description→Description.

## Slide 17

Continuación del Paso 8 (config final tabla categorías + repetir proceso).

Texto: Así, para el caso de la tabla 'categorías', la configuración final quedaría como se observa. Repetimos el mismo proceso para los datos de 'Proveedores' y 'Productos' del archivo de Excel.

Captura de pantalla: área "Flujo de datos" de la "Tarea Flujo de datos: Categorias" mostrando pipeline vertical con 3 nodos conectados: "Origen de Excel" (icono Excel verde) → "Conversión de datos" → "Destino de OLE DB".

## Slide 18

**Paso 9: Crear y configurar tareas de flujo de datos**

Texto: De nuevo, arrastramos en el área de trabajo la herramienta Tarea Flujo de datos y entramos a esta. Luego, arrastramos la herramienta 'Asistente de orígenes' y cuando ingresamos seleccionamos como tipo de origen 'Flat File' y en la parte derecha la opción 'Nueva'.

Dos capturas de pantalla:
- Superior: área "Flujo de control" con nodos "Limpiar tablas" → "Categorias" conectados por flecha verde.
- Inferior: ventana "Asistente de orígenes" con lista "Seleccionar tipo de origen": SQL Server, Excel, Flat File (resaltado/seleccionado), Oracle; panel derecho "Seleccionar administradores de conexiones" con "Nueva..." resaltado en azul.

## Slide 19

**Paso 10: Agregar conversión de datos**

Texto: Buscamos la ubicación de nuestro archivo de texto y dejamos la configuración por defecto en la pestaña 'General' y en 'Columnas'. Para el archivo 'personal', en la herramienta Conversión de datos, realizamos los ajustes que se muestran.

Dos capturas de pantalla:
- Izquierda: ventana "Administrador de conexiones de archivos planos" con campos: Nombre del administrador de conexiones, Descripción, árbol (General, Columnas, Opciones a..., Vista previ...), Nombre de archivo="D:\Documentos\Desca...", Configuración regional="Español (Perú)", Página de códigos="1252 (ANSI - Latín I)", Formato="Delimitado", Calificador de texto="<ninguno>", Delimitador de filas de encabezados="{CR}{LF}", Filas de encabezados que se omitirán="0", checkbox "Nombres de columna de la primera fila de datos" marcado.
- Derecha: lista "Columnas de entrada di..." (Nombre, EmployeeID resaltado, LastName, FirstName, Title, TitleOfCourtesy, BirthDate) y tabla Input Column → Output Alias → Data Type → Length: Title→Copy of Title→cadena[DT_STR]→30, Address→Copy of Address→...→50, City→Copy of City→...→15, Region→Copy of Region→...→15, PostalCode→Copy of PostalCode→...→10, Country→Copy of Country→...→15, HomePhone→Copy of HomePhone→...→24, Extension→Copy of Extension→...→5, TitleOfCourtesy→Copy of TitleOfCour...→...→5.

## Slide 20

**Paso 11: Agregar destino de OLE DB**

Texto: Añadimos la herramienta Destino de OLE DB. Entramos en esta y seleccionamos la tabla 'empleados'. En la pestaña 'Asignaciones', indicamos qué campos serán utilizados para la recepción de los datos.

Dos capturas de pantalla:
- Izquierda: config OLE DB destino: "Administrador de conexiones OLE DB" = "LPDOC20219\SQLEXPRESS.STG_NW", "Modo de acceso a datos" = "Carga rápida de tabla o vista", "Nombre de la tabla o la vista" = "[dbo].[empleados]".
- Derecha: pestaña "Asignaciones" con diagrama de líneas cruzadas conectando "Columnas de entra..." (Nombre, Copy of Addr..., Copy of City, Copy of Region, Copy of Post..., Copy of Coun..., Copy of Hom..., Copy of Exten... resaltado, Copy of Title...) con "Columnas de desti..." (Nombre, Address, City, Region, PostalCode, Country, HomePhone, Extension, ReportsTo). Tabla: Columna de entrada → Columna de destino: Copy of EmployeeID→EmployeeID, Copy of LastName→LastName, Copy of FirstName→FirstName, Copy of Title→Title, Copy of TitleOfCourtesy→TitleOfCourtesy, BirthDate→BirthDate, HireDate→HireDate, Copy of Address→Address.

## Slide 21

Slide separador: "Parte III: Ejecución del proyecto". Imagen decorativa (persona con bata de laboratorio y tubos de ensayo, tono azul).

## Slide 22

**Paso 12: Ejecutar el flujo de datos**

Texto: Cuando tengamos nuestro esquema listo, le damos al botón Iniciar que se encuentra en la parte superior. En caso se nos muestre un error o advertencia, entramos a la tarea de flujo de datos correspondiente y le damos clic derecho. Aparecerá la opción 'Mostrar el Editor avanzado' y allí buscamos la pestaña 'Propiedades de entrada y salida' para corregir ya sea el tipo de datos o la longitud de las columnas.

Diagrama esquemático (iconos simples en negro, no captura de pantalla): icono de código `</>` conectado por línea horizontal a icono de "play" (▶); debajo del icono de código, línea vertical a un icono de engranaje (⚙); debajo del icono de play, línea vertical a un icono de gráfico de barras ascendente. Representa el flujo código → ejecución → configuración/resultado.

## Slide 23

Continuación del Paso 12 (resultado de ejecución).

Texto: Si el proceso se realizó sin errores, se mostrará un símbolo de check en color verde.

Captura de pantalla: interfaz de Visual Studio/SSIS con barra superior (Develop, Default, botón "Iniciar" resaltado con recuadro rojo), pestaña "Package.dtsx [Diseño]*", sub-pestañas (Flujo de control, Flujo de datos, Parámetros, Controladores de event..., Explorador de paque..., Resultados de la ejecución). Área de diseño "Flujo de control" muestra 5 nodos con check verde (ejecución exitosa) conectados: "Limpiar tablas" → "Categorias" → "Proveedor"; "Proveedor" → (flecha hacia abajo) → "Producto" → "Empleado" (flecha izquierda). Todos muestran icono de check verde en la esquina, indicando ejecución sin errores.

## Slide 24

**Paso 13: Verificar datos cargados en repositorio**

Texto: Si vamos a SQL Server, podemos ver que los datos provenientes del archivo de Excel y de texto fueron cargados y transformados y llevados a un único repositorio de datos.

Captura de pantalla: SSMS con panel "Object Explorer" mostrando árbol expandido: servidor LPDOC20219\SQLEXPRESS (SQL Server 1...) > Databases > STG_NW > Tables (System Tables, FileTables, External Tables, Graph Tables, y resaltadas en recuadro rojo: dbo.categorias, dbo.empleados, dbo.productos, dbo.proveedores) > Views, External Resources, Synonyms, Programmability, Query Store, Service Broker, Storage, Security, etc.

Panel derecho: pestañas de queries SQL abiertas (SQLQuery2.sql, SQLQuery3.sql, SQLQuery4.sql). Código visible:
```sql
SELECT TOP (1000) [EmployeeID]
    ,[LastName]
    ,[FirstName]
    ,[Title]
    ,[TitleOfCourtesy]
    ,[BirthDate]
    ,[HireDate]
    ,[Address]
    ,[City]
    ,[Region]
    ,[PostalCode]
    ,[Country]
    ,[HomePhone]
    ,[Extension]
    ,[ReportsTo]
FROM [STG_NW].[dbo].[empleados]
```

Resultados de la consulta en tabla: columnas EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate. Filas de ejemplo: 1-Davolio-Nancy-Sales Representative-Ms.-1948-12-08-1992-05-01; 2-Fuller-Andrew-Vice President, Sales-Dr.-1952-02-19-1992-08-14; 3-Leverling-Janet-Sales Representative-Ms.-1963-08-30-1992-04-01; 4-Peacock-Margaret-Sales Representative-Mrs.-1937-09-19-1993-05-03; 5-Buchanan-Steven-Sales Manager-Mr.-1955-03-04-1993-10-17; 6-Suyama-Michael-Sales Representative-Mr.-1963-07-02-1993-10-17; 7-King-Robert-Sales Representative-Mr.-1960-05-29-1994-01-02; 8-Callahan-Laura-Inside Sales Coordinator-Ms.-1958-01-09-1994-03-05; 9-Dodsworth-Anne-Sales Representative-Ms.-1966-01-27-1994-11-15.

## Slide 25

Continuación del Paso 13 (diagrama de relaciones).

Texto: Desde la opción 'Database Diagrams', vemos que las tablas no están relacionadas, así que podemos hacer esto manualmente.

Captura de pantalla: SSMS con "Object Explorer" (árbol con servidor LAPTOP-R9OQT46M\SQLEXPRESS, Databases > BD_HELADERIA, Housing, organization, pubs, STG_NW > Database Diagrams, Tables (dbo.categorias, dbo.empleados, dbo.productos, dbo.proveedores), Views, etc.) y panel principal "Diagram_1*" mostrando 4 tablas sin líneas de relación entre ellas:
- **empleados**: EmployeeID, LastName, FirstName, Title, BirthDate, HireDate, Address, Region, PostalCode, Country, HomePhone, Extension, ReportsTo
- **categorias**: CategoryID, CategoryName, Description
- **productos**: ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued
- **proveedores**: SupplierID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, HomePhone

Ninguna tabla tiene líneas de conexión entre sí (sin relaciones FK definidas en el diagrama).
