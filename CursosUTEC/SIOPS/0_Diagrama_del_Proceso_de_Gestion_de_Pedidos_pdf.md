---
curso: SIOPS
titulo: 0. Diagrama del Proceso de Gestión de Pedidos
slides: 1
fuente: 0. Diagrama del Proceso de Gestión de Pedidos.pdf
---

## Slide 1

Diagrama de flujo de proceso de negocio (estilo BPMN simplificado, dos filas de cajas azules conectadas con flechas), sin título de texto adicional en la slide.

**Fila superior** (izquierda a derecha, cajas azul claro):
1. "Recibir Consulta"
2. "Recibir Orden de Compra"
3. (hueco) "Recibir Pago"

**Fila inferior** (izquierda a derecha, cajas azul más oscuro, en secuencia continua):
1. "Crear Oferta"
2. "Crear Pedido de Cliente"
3. "Preparar Envío"
4. "Realizar Envío"
5. "Enviar Factura"
6. "Contabilizar Pago"

**Conexiones (flechas):**
- "Recibir Consulta" → baja hacia "Crear Oferta"
- "Crear Oferta" → sube hacia "Recibir Orden de Compra"
- "Recibir Orden de Compra" → baja hacia "Crear Pedido de Cliente"
- "Crear Pedido de Cliente" → "Preparar Envío" → "Realizar Envío" → "Enviar Factura" (flechas horizontales en línea recta, misma fila)
- "Enviar Factura" → sube hacia "Recibir Pago"
- "Recibir Pago" → baja hacia "Contabilizar Pago"

**Lectura del proceso end-to-end:** Recibir Consulta → Crear Oferta → Recibir Orden de Compra → Crear Pedido de Cliente → Preparar Envío → Realizar Envío → Enviar Factura → Recibir Pago → Contabilizar Pago. El diagrama alterna entre pasos de interacción con el cliente/externos (fila superior: recibir consulta, recibir orden de compra, recibir pago) y pasos de ejecución interna (fila inferior: crear oferta, crear pedido, preparar/realizar envío, enviar factura, contabilizar pago), formando un patrón en zigzag típico de un ciclo order-to-cash.

Todo el contenido de la slide es el diagrama; no hay texto adicional, notas al pie ni chrome decorativo relevante.
