---
curso: INGSOFT
titulo: 10 - Semana 9/EC3 Implementacion API Monedas
slides: 0
fuente: 10 - Semana 9/EC3 Implementacion API Monedas.docx
---

# Implementación de API de Monedas

## Grupo e Integrantes:

## Requisitos Funcionales

## 

Implementar una aplicación para intercambio de monedas que tiene como requisitos:

- Soportar múltiples usuarios con sus cuentas en al menos dos monedas (Soles y Dólares).

- Creación de cuenta de un usuario.

- Ofrecer un modo para visualizar el estado de cuenta de un usuario.

- Consultar tasa de cambio de una moneda a otra de alguna API de internet.

- Permitir la transferencia de valores de una moneda a otra y de un usuario a otro entre la misma moneda o diferentes monedas.

  - La tasa de cambio debe ser obtenida online en el momento.

- Permitir ver el historial de operaciones de un usuario.

## Requisitos No Funcionales (Todos son criterios de evaluación)

- Inicializar la aplicación con al menos dos usuarios con saldo en ambas monedas, exactamente estos dos:

  - X (S./ 100, USD 200).

  - Y (S/. 50, USD 100).

- El acceso a las operaciones debe ser por endpoints.

- Lenguaje a elección de los alumnos.

- Implementar acceso a dos APIs diferentes de conversión de monedas.

- Formato soportado: json.

- Usar interfaces (para el API de cambio de monedas, y dar posibilidad de switch entre dos APIS).

- Usar al menos dos patrones de diseño (Ej: Singleton para el acceso al cambio de monedas, Adapter para intercambiar los resultados de ambas APIs, Observer: Actualizar el historial de transacciones).

## Opcional

- Soporte de más monedas.

- Soporte de Usuario / Contraseña.

- Interfaz de usuario: Consola o Web.

- Formatos de exportación: csv, xml.

- Serializar el estado de la aplicación para que al reiniciarla se mantengan los datos después de las operaciones.
