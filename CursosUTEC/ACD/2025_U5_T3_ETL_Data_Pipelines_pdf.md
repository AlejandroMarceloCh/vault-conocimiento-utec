---
curso: ACD
titulo: [2025] U5_T3 ETL Data Pipelines
slides: 25
fuente: [2025] U5_T3 ETL Data Pipelines.pdf
---

ETL Data Pipelines

 DS3021 Análisis Computacional de Datos




                                   Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Al finalizar esta sesión el estudiante
                     implementará un proceso ETL a partir de
                     diferentes fuentes de datos.
U5_L1: ETL Data Pipelines
Parte I: Configuración y
creación del proyecto
                  Paso 0: Crear las tablas

Primero abriremos SQL Server y crearemos una base de datos llamada ‘STG_NW’. Luego,
crearemos las estructuras de las tablas ‘Empleados’, ‘Categorias’, ‘Proveedores’ y
‘Productos’ a partir el archivo ‘SQL_Landing_Estructuras_Tablas’.
               Paso 1: Verificar extensiones

Abrimos Visual Studio y buscamos el botón para crear un proyecto. Buscamos la opción
‘Integration Services Project’ y en caso no figure, le damos al botón ‘Atrás’ y elegimos la
opción ‘Continuar sin código’.
                Paso 2: Instalar extensiones

En la pestaña ‘Extensiones’ elegimos ‘Administrar extensiones’ y descargamos e instalamos
‘SQL Server Integration Services Projects’, ‘Microsoft Reporting Services Projects’ y
‘Microsoft Analysis Services Projects’.
                    Paso 3: Crear proyecto

Creamos el proyecto con la opción ‘Integration Services Project’ y le damos un nombre.
Parte II: Creación de
tareas y flujos de datos
            Paso 4: Crear y configurar tareas


Una vez abierto el
proyecto, arrastramos en
el área de trabajo la
herramienta         ‘Tarea
Ejecutar SQL’. Hacemos
doble clic izquierdo y le
podemos      asignar    un
nombre       desde       el
apartado         ‘General’,
asimismo, en ‘Instrucción
SQL’ estableceremos una
nueva conexión.
              Paso 5: Buscar base de datos

Configuramos el proveedor y colocamos el nombre del servidor que tenemos en SQL
Server, y buscar la base de datos ‘STG_NW’. Además, limpiamos las tablas con ‘delete’.
La configuración final de la tarea debería quedar como en la imagen mostrada, con la opción
‘BypassPrepare’ tomando como valor ‘False’.
  Paso 6: Crear y configurar tareas de flujo de datos

Arrastramos en el área de trabajo la herramienta Tarea Flujo de datos y entramos a esta.
Luego, arrastramos la herramienta ‘Asistente de orígenes’ y cuando ingresamos
seleccionamos como tipo de origen ‘Excel’ y en la parte derecha la opción ‘Nueva’
Buscamos la ubicación de
nuestro archivo de Excel,
para luego darle al botón
‘Aceptar’.           Luego,
volvemos a entrar a
nuestro     asistente   de
orígenes que ahora será
de tipo Excel y buscamos
la tabla ‘categorias’.
            Paso 7: Agregar conversión de datos

                                            En la pestaña ‘Columnas’, nos aseguramos
                                            de que se hayan seleccionado todas.




Agregamos la herramienta Conversión de
datos y lo conectamos con nuestro archivo
de orígenes con los ajustes mostrados.
          Paso 8: Agregar destino de OLE DB

Añadimos la herramienta Destino de OLE DB. Entramos en esta y seleccionamos la tabla
‘categorias’. En la pestaña ‘Asignaciones’, indicamos qué campos serán utilizados para la
recepción de los datos.
Así, para el caso de la tabla ‘categorías’, la configuración final quedaría como se observa.
Repetimos el mismo proceso para los datos de ‘Proveedores’ y ‘Productos’ del archivo de
Excel.
  Paso 9: Crear y configurar tareas de flujo de datos

De nuevo, arrastramos en el área de trabajo la herramienta Tarea Flujo de datos y entramos
a esta. Luego, arrastramos la herramienta ‘Asistente de orígenes’ y cuando ingresamos
seleccionamos como tipo de origen ‘Flat File’ y en la parte derecha la opción ‘Nueva’.
            Paso 10: Agregar conversión de datos

                                                Buscamos la ubicación de nuestro archivo de
                                                texto y dejamos la configuración por defecto
                                                en la pestaña ‘General’ y en ‘Columnas’.




Para el archivo ‘personal’, en la herramienta
Conversión de datos, realizamos los ajustes
que se muestran.
         Paso 11: Agregar destino de OLE DB

Añadimos la herramienta Destino de OLE DB. Entramos en esta y seleccionamos la tabla
‘empleados’. En la pestaña ‘Asignaciones’, indicamos qué campos serán utilizados para la
recepción de los datos.

Parte III: Ejecución del
proyecto
                 Paso 12: Ejecutar el flujo de datos

Cuando tengamos nuestro esquema listo, le damos al botón Iniciar que se encuentra en la
parte superior. En caso se nos muestre un error o advertencia, entramos a la tarea de flujo
de datos correspondiente y le damos clic derecho. Aparecerá la opción ‘Mostrar el Editor
avanzado’ y allí buscamos la pestaña ‘Propiedades de entrada y salida’ para corregir ya sea
el tipo de datos o la longitud de las columnas.
Si el proceso se realizó sin errores, se mostrará un símbolo de check en color verde.
    Paso 13: Verificar datos cargados en repositorio



Si vamos a SQL Server,
podemos ver que los
datos provenientes del
archivo de Excel y de
texto fueron cargados y
transformados y llevados
a un único repositorio de
datos.
Desde la opción ‘Database
Diagrams’, vemos que las
tablas      no       están
relacionadas,    así   que
podemos       hacer   esto
manualmente.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
