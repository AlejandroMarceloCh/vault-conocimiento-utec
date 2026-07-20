---
curso: ACD
titulo: SQL_Landing_Estructuras_Tablas
slides: 0
fuente: SQL_Landing_Estructuras_Tablas.sql
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: SQL_Landing_Estructuras_Tablas.sql. -->

<!-- INTERPRETAR: código fuente (SQL_Landing_Estructuras_Tablas.sql). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

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
    [Title] varchar(50),
    [TitleOfCourtesy] varchar(50),
    [BirthDate] varchar(50),
    [HireDate] varchar(50),
    [Address] varchar(50),
    [City] varchar(50),
    [Region] varchar(50),
    [PostalCode] varchar(50),
    [Country] varchar(50),
    [HomePhone] varchar(50),
    [Extension] varchar(50),
    [ReportsTo] varchar(50)
    )
go

--Estructura tabla Categor�as
CREATE TABLE [categorias] (
    [CategoryID] float,
    [CategoryName] nvarchar(max),
    [Description] nvarchar(max)
)
go

--Estructura tabla Proveedores
CREATE TABLE [proveedores] (
    [SupplierID] float,
    [CompanyName] nvarchar(max),
    [ContactName] nvarchar(max),
    [ContactTitle] nvarchar(max),
    [Address] nvarchar(max),
    [City] nvarchar(max),
    [Region] nvarchar(max),
    [PostalCode] nvarchar(max),
    [Country] nvarchar(max),
    [Phone] nvarchar(max),
    [Fax] nvarchar(max),
    [HomePage] nvarchar(max)
)
go

--Estructura tabla Productos
CREATE TABLE [productos] (
    [ProductID] float,
    [ProductName] nvarchar(max),
    [SupplierID] float,
    [CategoryID] float,
    [QuantityPerUnit] nvarchar(max),
    [UnitPrice] money,
    [UnitsInStock] float,
    [UnitsOnOrder] float,
    [ReorderLevel] float,
    [Discontinued] float
)
go
```
