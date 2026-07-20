---
curso: BIGDATA
titulo: 15 - Semana 13/Actividad_13_Datasets__Empleados
slides: 0
fuente: 15 - Semana 13/Actividad_13_Datasets__Empleados.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 15 - Semana 13/Actividad_13_Datasets__Empleados.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Actividad_13_Datasets__Empleados.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Empleados
Filas: 9 · Columnas: 17
Columnas y tipos: IdEmpleado (int64), Apellidos (object), Nombre (object), Cargo (object), Tratamiento (object), FechaNacimiento (datetime64[ns]), FechaContratación (datetime64[ns]), Dirección (object), Ciudad (object), Región (object), CódPostal (object), País (object), TelDomicilio (object), Extensión (int64), Foto (object), Notas (object), Jefe (float64)

Muestra (primeras 9 de 9 filas, formato CSV):
IdEmpleado,Apellidos,Nombre,Cargo,Tratamiento,FechaNacimiento,FechaContratación,Dirección,Ciudad,Región,CódPostal,País,TelDomicilio,Extensión,Foto,Notas,Jefe
1,Davolio,Nancy,Representante de ventas,Srta.,1968-12-08,1992-05-01,"507 - 20th Ave. E._x000d_
Apt. 2A",Seattle,WA,98122,EE.UU.,(206) 555-9857,5467,EMPID1.BMP,"Su formación incluye una licenciatura en Psicología por la Universidad del Estado de Colorado. También escribió ""El arte de la llamada en frío"". Nancy es miembro de Toastmasters International.",2.0
2,Fuller,Andrew,Vicepresidente comercial,Dr.,1952-02-19,1992-08-14,908 W. Capital Way,Tacoma,WA,98401,EE.UU.,(206) 555-9482,3457,EMPID2.BMP,"Andrew completó su licenciatura en Comercio y un doctorado en Marketing Internacional de la Universidad de Dallas. Habla con fluidez en francés e italiano y lee el alemán. Ingresó en la empresa como representante de ventas, fue ascendido a gerente de cuentas y después fue nombrado vicepresidente comercial._x000d_
Andrew es miembro de la Mesa redonda de administración de Ventas, la Cámara de comercio de Seattle y de la Asociación de importadores de la Cuenca del Pacífico.",
3,Leverling,Janet,Representante de ventas,Srta.,1963-08-30,1992-04-01,722 Moss Bay Blvd.,Kirkland,WA,98033,EE.UU.,(206) 555-3412,3355,EMPID3.BMP,Janet es licenciada en Química por la Universidad de Boston. También ha completado un programa de formación en Gestión de minoristas de alimentación. Janet fue contratada como vendedora asociada y fue ascendida a representante de ventas.,2.0
4,Peacock,Margaret,Representante de ventas,Sra.,1958-09-19,1993-05-03,4110 Old Redmond Rd.,Redmond,WA,98052,EE.UU.,(206) 555-8122,5176,EMPID4.BMP,"Margaret es licenciada en Literatura inglesa por el Colegio Universitario Concordia, y tiene un máster del Instituto Americano de Artes Culinarias. Estuvo asignada temporalmente a la oficina de Londres antes de regresar a su puesto permanente en Seattle.",2.0
5,Buchanan,Steven,Gerente de ventas,Sr.,1955-03-04,1993-10-17,14 Garrett Hill,Londres,,SW1 8JR,Reino Unido,(71) 555-4848,3453,EMPID5.BMP,"Steven Buchanan se graduó en la Universidad de St. Andrews, Escocia. Tras su ingreso en la empresa dedicó 6 meses a un programa de orientación en la oficina de Seattle y luego volvió a su puesto permanente en Londres, donde fue ascendido a gerente de ventas. Completó con éxito los cursos de Telemarketing y Gestión de ventas internacional. Habla francés.",2.0
6,Suyama,Michael,Representante de ventas,Sr.,1963-07-02,1993-10-17,"Coventry House_x000d_
Miner Rd.",Londres,,EC2 7JR,Reino Unido,(71) 555-7773,428,EMPID6.BMP,"Michael se graduó en la Universidad de Sussex (MA, economía) y la Universidad de California en Los Angeles (MBA, marketing). También ha asistido a cursos de Ventas multiculturales y Administración del tiempo para profesionales de ventas. Habla_x000d_
japonés y lee y escribe en francés, portugués y español.",5.0
7,King,Robert,Representante de ventas,Sr.,1960-05-29,1994-01-02,"Edgeham Hollow_x000d_
Winchester Way",Londres,,RG1 9SP,Reino Unido,(71) 555-5598,465,EMPID7.BMP,"Robert King colaboró en la organización Peace Corps y viajó extensamente antes de completar su licenciatura en inglés en la Universidad de Michigan, el año en que ingresó en la empresa. Después de completar un curso denominado ""Ventas en Europa"", fue_x000d_
transferido a la oficina de Londres.",5.0
8,Callahan,Laura,Coordinador ventas interno,Srta.,1958-01-09,1994-03-05,4726 - 11th Ave. N.E.,Seattle,WA,98105,EE.UU.,(206) 555-1189,2344,EMPID8.BMP,Laura se graduó en Psicología por la Universidad de Washington. También completó un curso de francés de negocios. Lee y escribe en francés.,2.0
9,Dodsworth,Anne,Representante de ventas,Srta.,1969-07-02,1994-11-15,7 Houndstooth Rd.,Londres,,WG2 7LT,Reino Unido,(71) 555-4444,452,EMPID9.BMP,Anne tiene una licenciatura en inglés por el  St. Lawrence College.  Habla con fluidez el francés y el alemán.,5.0

Resumen numérico:
       IdEmpleado    Extensión      Jefe
count    9.000000     9.000000  8.000000
mean     5.000000  2733.000000  3.125000
std      2.738613  1958.430366  1.552648
min      1.000000   428.000000  2.000000
25%      3.000000   465.000000  2.000000
50%      5.000000  3355.000000  2.000000
75%      7.000000  3457.000000  5.000000
max      9.000000  5467.000000  5.000000
