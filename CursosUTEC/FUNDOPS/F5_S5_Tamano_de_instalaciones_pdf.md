---
curso: FUNDOPS
titulo: F5-S5 Tamaño de instalaciones
slides: 7
fuente: F5-S5 Tamaño de instalaciones.pdf
---

## Slide 1

**Título: Tamaño de Instalaciones**

Es la capacidad instalada de producción expresada en unidades de producción por unidades de tiempo. Las decisiones de capacidad involucran las siguientes actividades:

1. Estimar la capacidad de las instalaciones actuales.
2. Pronosticar las necesidades de capacidad futura a largo plazo para todos los productos y servicios.
3. Identificar y analizar fuentes de capacidad para poder cumplir con futuras necesidades de capacidad.
4. Seleccionar de entre fuentes alternativas de capacidad.

Visual: fondo degradado verde azulado (teal) oscuro con una franja/rectángulo rojo decorativo en la esquina superior derecha (chrome decorativo de plantilla). Título en tipografía bold clara. Sin diagramas ni tablas adicionales.

## Slide 2

**Título: Tamaño de Instalaciones**

Variables para medir el tamaño (subtítulo subrayado):
- a) De Flujo: se refiere a la cantidad que se puede producir.
- b) De existencias: son los recursos disponibles para llegar a un determinado nivel de capacidad.

Condicionantes del tamaño (subtítulo subrayado), presentados en dos columnas:

| Columna izquierda | Columna derecha |
|---|---|
| Mercado | Localización |
| Tecnología | Financiación |

Visual: mismo fondo teal con franja roja decorativa. Sin diagramas.

## Slide 3

**Título: Variables a Tomar en cuenta**

1. Localización: Insumos (mano de obra, materiales, capital). Proceso y tecnología. Productos, Medio (nacional, regional, comunidad).
2. Capacidad: Capacidad de Diseño, Capacidad del sistema, Estrategia de Operación.
3. Distribución de la Instalación: Tipo de producto, tipo de proceso, Volumen de producción.

Visual: mismo fondo teal con franja roja decorativa. Lista numerada, sin diagramas ni tablas.

## Slide 4

**Título: Relación entre Capacidad y Producción**

- Capacidad de Diseño: es la Capacidad Teórica de un equipo, lo que debería producirse en condiciones ideales de fabricación.
- Eficiencia: Es el porcentaje de la capacidad de diseño logrado debido al desgaste natural del equipo, al paso del tiempo, a la falta de mantenimiento, etc.
- Capacidad Efectiva: Es la Capacidad de Diseño afectada por el porcentaje de eficiencia.
- Defectuosos y Merma: la producción defectuosa se debe a mal manejo del equipo, material inadecuado, mala calibración del equipo. Si es debido a la naturaleza del proceso se le conoce como MERMA.

Visual: mismo fondo teal con franja roja decorativa. Texto puro, sin diagrama en esta slide (el diagrama aparece en la siguiente).

## Slide 5

**Título: Relación entre Capacidad y Producción**

Visual — diagrama de flujo vertical con 3 cajas rectangulares (bordes blancos, fondo transparente) conectadas por flechas verticales descendentes:

```
┌─────────────────────┐
│ CAPACIDAD DE DISEÑO  │
└──────────┬───────────┘
           │
           ▼
┌─────────────────────┐
│  CAPACIDAD EFECTIVA  │
└──────────┬───────────┘
           │
           ▼
┌─────────────────────┐
│    CAPACIDAD REAL    │
└─────────────────────┘
```

Muestra la cascada jerárquica: la Capacidad de Diseño se reduce a Capacidad Efectiva, que a su vez se reduce a Capacidad Real. Slide sin texto adicional aparte del diagrama y el título.

## Slide 6

**Título: Relación entre Capacidad y Producción**

- Capacidad Real: es lo que la empresa verdaderamente puede producir luego de analizar todos los factores que pueden afectar a su capacidad instalada.

Fórmula (reproducida en LaTeX):

$$\text{Capacidad Real} = \text{C. Diseño} \times \%\text{Efic.} \times (1 - \%\text{def})$$

Visual — diagrama de proceso con entrada/salida: una caja central rotulada "Proceso" con:
- Flecha de entrada desde la izquierda, etiquetada "C. Efectiva"
- Flecha de salida hacia la derecha, etiquetada "C. Real"
- Flecha de salida hacia abajo desde la caja "Proceso", etiquetada "Defectuosos y Merma" (representa la pérdida durante el proceso)

```
C. Efectiva ──▶ [ Proceso ] ──▶ C. Real
                    │
                    ▼
           Defectuosos y Merma
```

## Slide 7

**Título: Pronóstico de la capacidad**

El pronóstico de la capacidad generalmente implica cuatro pasos:
- Calcular la demanda total del producto o servicio.
- Estimar el porcentaje de participación de la empresa en particular.
- Calcular en unidades de capacidad la participación de mercado.
- Convertir las unidades de capacidad en necesidades de capacidad (equipo, materiales, etc).

Visual: mismo fondo teal con franja roja decorativa. Lista con viñetas, sin diagramas ni tablas.
