---
curso: BIGDATA
titulo: 14 - Semana 12/Hands on guide to apps on databricks
slides: 65
fuente: 14 - Semana 12/Hands on guide to apps on databricks.pdf
---

## Slide 1
Portada. Fondo azul oscuro con formas geométricas rojas tipo `</>` (símbolo de código). Logo Databricks. Título: "A Hands-On Guide to Apps on Databricks". Decorativa.

## Slide 2
Índice de contenidos (parte 1 de 2), dos columnas. Columna izquierda: "Introduction to Building Apps on Databricks" (pág. 4) con subsecciones (The application deployment challenge - 6, Databricks Apps and Lakebase: A unified application platform - 7, What this guide covers - 8); "From Notebooks to Production Applications" (pág. 9) con subsecciones (The challenge of production data applications - 10, Architecture and how it works - 10, Anatomy of the app - 13, Defining Databricks Asset Bundles resources - 17, Considerations and best practices - 20). Columna derecha: Conclusion - 22, Get started - 22; "The Transactional Foundation for Intelligent Applications" (pág. 23) con subsecciones (Introduction - 24, Why Lakebase and Databricks Apps - 24, Getting started: Build a transactional app with Lakebase - 25, Extending the lakehouse with Lakebase - 31, Summary - 32).

## Slide 3
Índice de contenidos (parte 2 de 2). Columna izquierda: "Turning Analytics Into Applications" (pág. 33) con subsecciones (Introduction: Analytics and operations are converging - 34, What is reverse ETL? - 34, Challenges of reverse ETL - 35, Lakebase: Integrated by default for easy reverse ETL - 35, Sample use case: Building an intelligent support portal with Lakebase - 36, Conclusion - 39); "Delivering Secure, Real-Time Applications on Databricks" (pág. 40) con subsecciones (Introduction - 41, Key technologies - 42, Solution overview - 42, Step-by-step guide - 43, Highlights on Postgres connection with OAuth - 48). Columna derecha: Lessons learned - 49, Try it yourself - 49; "How to Build AI Agents With Conversational Memory Using Lakebase" (pág. 50) con subsecciones (Why conversational memory matters - 51, Using Lakebase as the state layer for agents - 51, Memory patterns for AI agents - 52, Architecture overview - 53, Implementation guide - 54, Conclusion - 64, Resources - 64).

## Slide 4
Portada de capítulo "01 - Introduction to Building Apps on Databricks". Fondo oscuro con número "01" en rojo grande. Decorativa.

## Slide 5
Texto introductorio. Título "Introduction to Building Apps on Databricks". Explica que el reto no es la falta de datos/IA sino entregar esas capacidades como aplicaciones production-grade confiables. Menciona que la guía usa walkthroughs prácticos con código funcional. A la derecha, elemento gráfico decorativo (formas rojas tipo `</>`).

## Slide 6
"THE APPLICATION DEPLOYMENT CHALLENGE". Lista de obstáculos comunes al construir apps de datos/IA: Infrastructure provisioning and management, Authentication and security complexity, Data synchronization and latency (columna izq); Deployment automation and environment management, Governance and compliance (columna der). Cierra con nota sobre costos de la complejidad de deployment.

## Slide 7
"DATABRICKS APPS AND LAKEBASE: A UNIFIED APPLICATION PLATFORM". Diagrama de arquitectura de la plataforma Databricks (recuadro con capas apiladas):
- Capa superior: "Custom apps" (Secure data and AI apps), "AI/BI" (Agentic business intelligence), "And more…"
- Capa media: "Lakeflow" (Ingest, ETL, streaming), "DBSQL" (Data warehousing), "Lakebase" (Serverless Postgres)
- Capa recuadrada en rojo: "Agent Bricks" (Agentic AI & machine learning), "Unity Catalog"
- Capa base: "Delta Lake", "Iceberg", "Postgres"
Texto a la derecha describe Databricks Apps (hosting serverless para Streamlit, Dash, Flask, FastAPI, React) y Lakebase (Postgres gestionado, sincronizado con Unity Catalog) con lista de capacidades (servir insights en tiempo real, guardar estado de app, ACID).

## Slide 8
Tabla comparativa "TRADITIONAL APPROACH" vs "MODERN DATABRICKS APPS AND LAKEBASE APPROACH":

| TRADITIONAL APPROACH | MODERN DATABRICKS APPS AND LAKEBASE APPROACH |
|---|---|
| Separate hosting infrastructure | Serverless compute and zero infrastructure management |
| Custom authentication systems | Built-in OAuth and Unity Catalog integration |
| Manual data synchronization pipelines | Automated synced tables from Unity Catalog |
| Fragmented governance across systems | Unified governance through Unity Catalog |
| Complex, multi-tool deployment | Single-command deployment with Databricks Asset Bundles (DABs) |

A la derecha: sección "WHAT THIS GUIDE COVERS" con lista de qué se aprenderá (mover de notebooks a apps reales, servir datos analíticos y estado vía capa transaccional, construir apps seguras sin infra custom, deploy con patrones repetibles).

## Slide 9
Portada de capítulo "02 - From Notebooks to Production Applications". Fondo oscuro, número "02" en rojo. Decorativa.

## Slide 10
Autoría: "by Pascal Vogel, Evan Pandya and Christopher Pries". "THE CHALLENGE OF PRODUCTION DATA APPLICATIONS" describe la complejidad de apps de datos production-ready. "ARCHITECTURE AND HOW IT WORKS": introduce app de ejemplo de viajes en taxi (React + FastAPI leyendo de tablas sincronizadas de Lakebase).

Diagrama de arquitectura (recuadro punteado rojo "Databricks Asset Bundles (DABs)" que envuelve todo):
- Caja "Databricks Apps": Front end (React) → Back end (FastAPI)
- Flecha hacia caja "Lakebase": Synced table (PostgreSQL table)
- Flecha bidireccional con caja roja "Managed pipeline" hacia caja "Unity Catalog": Managed table (Delta table)

## Slide 11
"Main solution components" (lista): Databricks app (React/TypeScript/Vite/FastAPI), Unity Catalog synced table, Lakebase database instance, Unity Catalog table (clonada de samples.nyctaxi.trips), Databricks Asset Bundles (DABs).

Captura de pantalla de la app "NYC Taxi Dashboard" (navegador macOS, URL trips-app-3488470091230896.aws.databricksapps.com): header con botón rojo "Refresh data" y "Last refresh: 2:13:15 PM". Gráfico de dispersión "Daily fare trends - Distance vs Fare Amount" (eje X Distance en millas 0-15+, eje Y Fare $0-$100, puntos rojos con tendencia creciente). Debajo, tabla con columnas ID, Pickup Time, Dropoff Time, Distance (miles), Fare ($), Pickup ZIP, Dropoff ZIP — filas de ejemplo con IDs 21924-21932, paginación "1 to 20 of 100, Page 1 of 5".

## Slide 12
Bloque de código SQL para insertar nuevos registros de prueba en `main.default.trips` (3 filas con id 21933-21935, fechas 2025-08-20 a 22, trip_distance, fare_amount, pickup/dropoff zip).

Captura de pantalla del Catalog Explorer de Databricks mostrando la tabla `trips_synced` bajo `users > pascal_vogel`, con panel derecho "Overview": Description "Database table synced from another UC table", Synced table status "Online", Source table `users.pascal_vogel.trips`, Primary key(s) "id", Sync schedule "Snapshot", Instance Name "trips-app-instance". Sección "Data Ingest": Pipeline id, Update status "Completed", Last processed commit "17", Last processed timestamp, botón rojo "Sync now" resaltado con marcador numerado (1, 2, 3 indicando pasos de la UI).

## Slide 13
Texto explica que tras el refresh los nuevos registros aparecen en el dashboard en segundos. "ANATOMY OF THE APP" — Authentication and database connection: cada app tiene un service principal; Lakebase soporta OAuth M2M vía WorkspaceClient del SDK de Databricks Python.

Repite la captura del dashboard "NYC Taxi Dashboard" (misma que slide 11, con el gráfico de dispersión y la tabla de viajes).

## Slide 14
Dos bloques de código Python lado a lado:
- Izquierda (`app/database.py`): función `get_connection(self)` que obtiene token OAuth vía `self.workspace_client.config.oauth_token().access_token` y hace `psycopg.connect(host=..., port=5432, dbname=..., user=..., password=token, sslmode="require")`.
- Derecha (`app/main.py`): función `get_taxi_trips_data() -> List[TaxiTrip]` que ejecuta un SELECT sobre la tabla sincronizada (columnas id, tpep_pickup_datetime, tpep_dropoff_datetime, trip_distance, fare_amount, pickup_zip, dropoff_zip) ORDER BY tpep_pickup_datetime DESC LIMIT 100, construye lista de objetos `TaxiTrip`, y expone endpoint FastAPI `@app_api.get("/taxi-trips", ...)`.

## Slide 15
Dos bloques de código:
- Izquierda (Python, `app/main.py`): monta FastAPI con `StaticFiles` para servir el frontend React compilado con Vite (`app.mount("/api", app_api)`, `app.mount("/", app_frontend)`).
- Derecha (JavaScript, `app/frontend/src/taxiApi.ts`): cliente axios (`baseURL: "/api"`) con función `getTaxiTrips` que hace GET a `/taxi-trips`.

## Slide 16
Bloque de código JavaScript (`app/frontend/src/App.tsx`): función `fetchData` que llama `getTaxiTrips()`, maneja errores, y `useEffect` con `setInterval(fetchData, 3000)` para polling cada 3 segundos. A la derecha, elemento gráfico decorativo rojo `</>`.

## Slide 17
"DEFINING DATABRICKS ASSET BUNDLES RESOURCES". Bloque de código YAML (`databricks.yml`) con configuración del bundle: `bundle.name`, `sync.include` (app/frontend/dist), `include` (resources/*.yml), `variables` (catalog default main, schema default default), `targets` (dev con mode development, staging con mode production y root_path parametrizado).

## Slide 18
"Lakebase setup and sync with Unity Catalog". Bloque de código YAML (`resources/database.yml`) definiendo `database_instances.trips-app-instance` (capacity CU_1) y `synced_database_tables.trips-app-synced-table` con `source_table_full_name`, `scheduling_policy: SNAPSHOT`, `primary_key_columns: [id]`.

## Slide 19
"Databricks Apps resource". Bloque de código YAML (`resources/app.yml`) definiendo `resources.apps.trips-app` con `name`, `source_code_path: ../app`, y `resources` (lakebase database con `database_name`, `instance_name`, `permission: CAN_CONNECT_AND_CREATE`).

## Slide 20
"CONSIDERATIONS AND BEST PRACTICES". Tabla comparativa de modos de sincronización de Lakebase (SNAPSHOT / TRIGGERED / CONTINUOUS):

| | SNAPSHOT | TRIGGERED | CONTINUOUS |
|---|---|---|---|
| Update method | Full table replacement on each run | Initial full copy and incremental changes | Initial load and real-time streaming updates |
| Performance | 10x more efficient than other modes | Balanced cost and performance | Higher cost — continuously running |
| Latency | High latency — scheduled or manual | Medium latency — on demand | Lowest latency — real time, ~15 sec |
| Best for | Infrequent changes; Modifying >10% of source table; Low-urgency, high-volume updates | Compromise between cost and latency; Reasonably current data; Controlled refresh timing | Mission-critical systems; Real-time data requirements; No manual refresh tolerance |
| Limitations | Higher latency; Full table re-creation each time | Avoid running >every five minutes; Requires change data feed; More expensive if run too frequently | Highest cost; Requires change data feed; Continuous resource consumption |

## Slide 21
Continúa "Considerations and best practices": notificaciones para el pipeline de sync, right-sizing de instancia, índices, `pg_stat_statements`. "Prepare your app for production": polling vs push (WebSockets/server-sent events), caching con fastapi-cache. Columna derecha "Authentication and authorization": usar OAuth 2.0 (no PATs), CLI para OAuth U2M en local, service principal para OAuth M2M en producción.

## Slide 22
"CONCLUSION" resume beneficios de Databricks Apps + Lakebase + DABs. "GET STARTED" con enlaces a documentación (decorativos, sin URL real visible). Elemento gráfico decorativo rojo.

## Slide 23
Portada de capítulo "03 - The Transactional Foundation for Intelligent Applications". Fondo oscuro, número "03" en rojo. Decorativa.

## Slide 24
Autoría: "By Jasper Puts and Antonio Javier Samaniego Jurado". "INTRODUCTION" describe el dolor de construir herramientas internas/apps IA de forma tradicional (provisionar Postgres, auth custom, etc.). Columna derecha: cómo Databricks Apps + Lakebase resuelven esto. "WHY LAKEBASE AND DATABRICKS APPS" con lista de capacidades de cada uno.

## Slide 25
"GETTING STARTED: BUILD A TRANSACTIONAL APP WITH LAKEBASE". Describe app de ejemplo: gestor de aprobación de vacaciones (holiday request approval).

Diagrama simple: caja "Client" (icono laptop) — flecha punteada — recuadro rojo "Databricks" que contiene "Databricks Apps" (icono) — flecha bidireccional "Reads/Writes" / "Authorized requests via App's service principal (SP)" — "Lakebase" (icono base de datos).

Columna derecha: lista numerada de 4 pasos (Provision a Lakebase database, Create a Databricks app, Configure schema/tables/access controls, Securely connect and interact with Lakebase).

## Slide 26
"Step 1: Provision Lakebase": ir a Compute > OLTP Database, crear instancia (ejemplo `lakebase-demo-instance`). Captura de pantalla de la UI Databricks mostrando pestaña "Compute" con tab "OLTP Database" seleccionada y botón "Create database instance".

"Step 2: Create a Databricks app and add database access": captura de pantalla "Create new app" mostrando opciones (Create a custom app / templates Dash, Flask, Gradio, Shiny, Streamlit, Node.js) y panel derecho "Quickly build secure data applications" con specs de compute (Up to 2 vCPUs, 6 GB memory, 0.5 DBU/hour). Lista: agregar recurso database otorga CONNECT y CREATE, crea rol Postgres ligado al client ID de la app.

## Slide 27
"Step 3: Create a schema, define a table and set permissions". Captura de pantalla de app "holiday-request-manager" en Databricks, tab "Environment" mostrando JSON con variables de entorno (runtime, DATABRICKS_APP_NAME, DATABRICKS_APP_PORT, DATABRICKS_CLIENT_ID resaltado en azul, DATABRICKS_CLIENT_SECRET, DATABRICKS_HOST, etc.).

Columna derecha: pasos "1. Retrieve the app's client ID" y "2. Open the Lakebase SQL editor" con captura de pantalla de la instancia `lakebase-demo-instance` (tabs Configuration, Connection details, Catalogs, Metrics, Permissions) mostrando Instance ID, Status "Available", PostgreSQL version 16, Size.

## Slide 28
"3. Run the following SQL": bloque de código SQL que crea schema `holidays`, tabla `holidays.holiday_requests` (request_id SERIAL PK, employee_name, start_date, end_date, status, manager_note), inserta 3 filas de ejemplo (Joe, Suzy, Charlie), y otorga GRANT USAGE/SELECT/INSERT/UPDATE/DELETE a `<CLIENT_ID>`. Columna derecha: nota sobre herramientas de gestión de schema a escala (Flyway, Liquibase).

## Slide 29
"Step 4: Build the app": captura de pantalla de app "Holiday Request Manager" (tabla con columnas Request ID, Employee, Start Date, End Date, Status, Manager Comment; filas Joe/Charlie/Suzy en estado "Pending"; sección "Action" con radio buttons Approve/Decline, campo de comentario, botón "Submit") junto a un editor SQL de Databricks mostrando `SELECT * FROM holidays.holiday_requests;`.

"Step 5: Connect securely to Lakebase": bloque de código Python usando `WorkspaceClient`, `Config`, SQLAlchemy `create_engine` con f-string de conexión postgresql+psycopg, y evento `do_connect` que inyecta el token OAuth como password.

## Slide 30
"Step 6: Read and update data": bloque de código Python con funciones `get_holiday_requests()` (SELECT vía pandas) y `update_request_status(request_id, status, comment)` (UPDATE vía SQLAlchemy). Columna derecha: lista de paquetes en `requirements.txt` (pandas==2.3.1, databricks-sdk==0.57.0, psycopg[binary]==3.2.9, sqlalchemy==2.0.41).

## Slide 31
"EXTENDING THE LAKEHOUSE WITH LAKEBASE". Diagrama: recuadro rojo "Databricks" con "Unity Catalog" (abajo izq) y elemento "Lakebase" (barra roja central) conectado bidireccionalmente a "Analytical data" (icono lakehouse) vía flechas "ETL" / "Reverse ETL"; y conectado a la derecha con "ML models" (Real-time feature serving), "AI agents" (Agent state), "Databricks Apps" (Transactional data).

Columna derecha: lista de capacidades (Online Feature Store, sync con Delta table) y casos de uso production-grade (actualizar estado de agentes IA, workflows en tiempo real, recomendación/pricing).

## Slide 32
"SUMMARY" del capítulo 3: resume qué se mostró (setup de instancia Lakebase, app que lee/escribe, auth basada en tokens, app de holiday requests). Elemento gráfico decorativo rojo.

## Slide 33
Portada de capítulo "04 - Turning Analytics Into Applications". Fondo oscuro, número "04" en rojo. Decorativa.

## Slide 34
Autoría: "By Firas Farah and Yatish Anand". "INTRODUCTION: ANALYTICS AND OPERATIONS ARE CONVERGING". "WHAT IS REVERSE ETL?" define el concepto. Columna derecha describe los 4 componentes del reverse ETL (Lakehouse, Syncing pipelines, Operational database, Applications).

Diagrama de flujo: caja "Lakehouse" con 4 sub-tablas (Bronze tables, Gold tables, Silver tables, Feature tables) → flecha "Sync pipelines" (icono engranaje) → caja "Operational database" → flecha → caja "Application layer" (iconos formas) rotulada "Internal/Customer-facing apps".

## Slide 35
"CHALLENGES OF REVERSE ETL": lista (Brittle custom-built ETL pipelines, Multiple disconnected systems, Inconsistent governance models). Columna derecha "LAKEBASE: INTEGRATED BY DEFAULT FOR EASY REVERSE ETL": lista de capacidades (Deep lakehouse integration, Fully managed Postgres con ACID/PostGIS/pgvector, Scalable resilient architecture con sub-10ms latency).

## Slide 36
Continúa lista: Integrated security and governance, Cloud-agnostic architecture. Columna derecha "SAMPLE USE CASE: BUILDING AN INTELLIGENT SUPPORT PORTAL WITH LAKEBASE": describe portal de soporte con insights ML (predicted escalation risk). Enlace "Watch the app walkthrough" (decorativo).

## Slide 37
"Step 1: Sync predictions from the lakehouse to Lakebase". Explica sync continuo de Delta table a Postgres con primary key `incident_id`.

Captura de pantalla del modal "Create synced table" de Databricks: campos Destination (Name: incidents_w_preds_st, Database instance: reverse-etl-demo, Postgres database: rev_etl), Synchronization settings (Primary key: incident_id, Sync mode: radio buttons Snapshot/Triggered/Continuous con "Continuous" seleccionado y nota explicativa sobre latencia de segundos y mayor costo, checkbox "Primary key is unique"), Pipeline settings (Create new pipeline, Serverless budget policy: None), botones Cancel/Create.

## Slide 38
"Step 2: Create a state table for user inputs": bloque SQL creando `support.user_updates` (incident_id TEXT PK, owner, comment, status). "Step 3: Configure Lakebase access in Databricks Apps": captura de pantalla "Create new app" wizard paso 2 "Configure (optional)" con sección "App resources", botón "+ Add resource", tabla con columnas Database (reverse-etl-d...), Permission (rev_etl), Resource key (Can conn... / database). "Step 4: Deploy your app code" describe deploy de app Flask.

## Slide 39
"CONCLUSION" del capítulo 4. Enlace "create synced tables" (decorativo). Elemento gráfico decorativo rojo.

## Slide 40
Portada de capítulo "05 - Delivering Secure, Real-Time Applications on Databricks". Fondo oscuro, número "05" en rojo. Decorativa.

## Slide 41
Autoría: "By Sylvia Christin Schumacher". "INTRODUCTION" sobre Lakebase + Databricks Apps para apps inteligentes con gobernanza out-of-the-box. Columna derecha: contexto GenAI — AI assistants, RAG, workflows — y anuncio de que el capítulo construye un app Streamlit CI/CD-enabled conectado a Lakebase, mostrando métricas de campaña sincronizadas de Unity Catalog.

## Slide 42
"KEY TECHNOLOGIES": Streamlit, SQLAlchemy, Databricks SDK, Postgres (Lakebase), DABs, GitHub. Columna derecha "SOLUTION OVERVIEW": 2 pasos (Set up Lakebase — crear instancia y sincronizar tabla UC vía Snapshot mode; Build a Databricks app — Streamlit UI, conexión segura SQLAlchemy+OAuth, filtros interactivos, DABs+GitHub para CI/CD).

## Slide 43
"STEP-BY-STEP GUIDE": recomienda Cursor + Databricks Connect para desarrollo local. "1. Set up Lakebase": crear instancia `postgres-campaigns`, clonar repo GitHub (bloque de código shell con `git clone` del repo `databricks-blogposts`). Columna derecha: lista de archivos del repo (app.py, config.yaml, generate_campaign_data.ipynb, requirements.txt, databricks.yml, README.md, gitignore).

## Slide 44
"3. Create a Unity Catalog table" (notebook `generate_campaign_data.ipynb`). "4. Sync the Unity Catalog table": Postgres database `campaign_db`, Table name `campaign_metrics_synced`, Mode Snapshot. "2. Deploy app" columna derecha: bloque de código config YAML (`config.yaml`) con sección postgres (host, port, database, username_env: DATABRICKS_CLIENT_ID, password_env: DATABRICKS_OAUTH_TOKEN) y synced_table (schema, name).

## Slide 45
"2. Install dependencies" (`pip install -r requirements.txt`). "3. Set Databricks environment variables": bloque de código con `export DATABRICKS_TOKEN`, `DATABRICKS_HOST`, `DB_USER`, `DB_PASSWORD`. Columna derecha "4. Configure Postgres database": bloque de código Python `DB_CONFIG` dict (host, port, database, schema, table).

## Slide 46
"5. Update app name": YAML de `databricks.yml` con `resources.apps.<your_app_name>`. Columna derecha "6. Deploy using DABs": comandos `databricks bundle init/validate/deploy`, `apps start`, `databricks apps deploy --source-code-path ...`. Nota sobre ruta del workspace donde queda el bundle.

## Slide 47
"3. Configure app privileges for the database": pasos 1 (Extract CLIENT_ID) y 2 (Grant privileges). Bloque de código SQL: `CREATE EXTENSION IF NOT EXISTS databricks_auth;`, `SELECT pg_databricks_create_role(...)`, GRANT ALL PRIVILEGES ON DATABASE/SCHEMA/TABLE a `<DATABRICKS_CLIENT_ID>`.

## Slide 48
"HIGHLIGHTS ON POSTGRES CONNECTION WITH OAUTH": lista (no manual token management, refresh cada 15 min, usa credenciales del workspace). Bloque de código Python: `WorkspaceClient`, `Config`, `create_engine`, evento `do_connect` con lógica de cache de token (`if postgres_password is None or time.time() - last_refresh > 900`).

## Slide 49
"LESSONS LEARNED": Databricks OAuth, Streamlit, DABs, Synced tables (cada uno con explicación breve). "TRY IT YOURSELF": pasos para clonar repo, customizar DB_CONFIG y nombre de app, deploy. Elemento gráfico decorativo rojo.

## Slide 50
Portada de capítulo "06 - How to Build AI Agents With Conversational Memory Using Lakebase". Fondo oscuro, número "06" en rojo. Decorativa.

## Slide 51
Autoría: "By Yatish Anand, Bo Cheng, Cathy Zdravevski, Evan Pandya and Susan Pierce". "WHY CONVERSATIONAL MEMORY MATTERS": ejemplo de investigaciones de ciberseguridad multi-turno. Columna derecha "USING LAKEBASE AS THE STATE LAYER FOR AGENTS": Lakebase como checkpoint store de LangGraph, persistencia por thread identifier.

## Slide 52
"MEMORY PATTERNS FOR AI AGENTS": memoria de corto plazo (thread-level checkpointing) vs memoria de largo plazo.

Diagrama "Short-term memory" vs "Long-term memory": izquierda muestra 1 hilo (Thread ID) con secuencia Agent message/User message/Agent message almacenada completa en tabla Lakebase (columnas Thread ID, Conversation) → "Lakebase checkpoint saver" → icono "Agent". Derecha muestra 3 threads distintos cuyo contenido pasa por "Knowledge extraction" → tabla key-value (Key: <Topic>/<Name>, Value: <Memory>/<User Name>) → "Lakebase store". Nota: "Agents can access both short-term and long-term memory" y "* Memory tables could be in the same or different Lakebase instances".

## Slide 53
"ARCHITECTURE OVERVIEW": lista de 6 componentes (chat model, Unity Catalog functions, LangGraph orchestration, Lakebase como checkpointer, Databricks AI Agent Framework, Streamlit app).

Diagrama "AI agent memory architecture": "User" (Chat interface) → "Databricks Apps" (Streamlit UI, Session state) → recuadro "MOSAIC AI AGENT FRAMEWORK" conteniendo "LangGraph Agent" (State graph, Tool orchestration) → "CheckpointSaver" (Checkpointer, Serialization) → "UC functions" (Governed tools, Data access); CheckpointSaver conecta hacia abajo (PERSIST/RETRIEVE) a caja roja "Lakebase" (Conversation checkpoints, Thread state); UC functions conecta a "Delta tables" (Enterprise data, UC governed). Leyenda: rojo = Databricks managed, gris = Agent framework.

## Slide 54
"IMPLEMENTATION GUIDE" / "Prerequisites": lista de requisitos (workspace serverless, permisos UC functions, permisos Lakebase, acceso a Model Serving y Apps). Columna derecha: bloque de código Python listando librerías necesarias (databricks-connect, databricks-agents, databricks-langchain, unitycatalog-langchain[databricks], psycopg[binary,pool], langgraph-checkpoint-postgres==2.0.21, langgraph==0.3.4, langchain, mlflow, uv).

## Slide 55
"Step 1: Add governed security context with Unity Catalog functions": describe 2 funciones SQL (`get_cyber_threat_info`, `get_user_info`). Bloque de código SQL completo de `get_cyber_threat_info(threat_type STRING)` (CREATE OR REPLACE FUNCTION, RETURNS STRING, RETURN SELECT CONCAT(...) FROM catalog.schema.cyber_threat_detection WHERE threat_type = threat_type ORDER BY event_timestamp DESC LIMIT 1).

## Slide 56
Continúa bloque de código SQL: `get_user_info(source_ip STRING)` (RETURN SELECT CONCAT('Username:', user_name, 'Department:', department, 'Email:', email, 'IP Address:', ip_address, 'Location:', location) FROM catalog.schema.user_info WHERE ip_address = source_ip LIMIT 1). Columna derecha: captura de pantalla de Catalog Explorer mostrando función `get_cyber_threat_info` con Description, Definition (código SQL truncado "...8 more lines"), Function metadata (Parameters, Type SCALAR, Return type STRING, Language SQL), panel "About this function" (Owner, Language).

## Slide 57
"Step 2: Create a Lakebase instance for checkpointings": explica uso de `langgraph-checkpoint-postgres`.

Captura de pantalla: instancia Lakebase `bo-test-lakebase-3` (tabs Configuration/Connection details/Catalogs/Metrics/Permissions) mostrando Name, Instance ID, Status "Available", PostgreSQL version 16, Serverless usage policy "None", Size (Capacity Units) "1".

Debajo, captura de un editor SQL ejecutando `SELECT thread_id, metadata, checkpoint, checkpoint_id, parent_checkpoint_id, checkpoint_ns, type FROM 'bo-test-lakebase-catalog'.public.checkpoints;` con tabla de resultados (columnas thread_id, metadata, checkpoint) mostrando filas JSON de ejemplo con steps -1 a 3.

## Slide 58
"Step 3: Orchestrate with LangGraph and trace with MLflow": captura de pantalla "MLflow Trace UI" mostrando un trace (ID, Latency 8.42s) con árbol de spans (predict > predict_stream > LangGraph > agent > call_model > RunnableSequence > RunnableLambda > ChatDatabricks > should_continue > tools > bo_cheng_dnb_de...) y panel "Inputs / Outputs" con JSON de respuesta (ejemplo: información de usuario George Miller). Columna derecha "Step 4: Deploy the agent with the Databricks AI Agent Framework": menciona declarar recursos dependientes (model serving endpoints, UC functions, Lakebase instance) al loguear con MLflow.

## Slide 59
Dos bloques de código Python (continuación de `agent.py`):
- Izquierda: métodos `predict()` y `predict_stream()` de la clase del agente, generando `checkpoint_config = {"configurable": {"thread_id": thread_id}}`.
- Derecha: bloque `with CheckpointSaver(instance_name=LAKEBASE_INSTANCE_NAME) as checkpointer:` iterando `graph.stream(...)` con stream_mode `["updates", "messages"]`, manejando eventos "updates" y "messages", yield de `ResponsesAgentStreamEvent`.

## Slide 60
Bloque de código Python (izquierda): imports de `mlflow`, `DatabricksFunction`, `DatabricksServingEndpoint`, `DatabricksLakebase`, `DatabricksVectorSearchIndex`, `AuthPolicy`, `SystemAuthPolicy`, `UserAuthPolicy`; construcción de lista `resources` incluyendo `DatabricksServingEndpoint` y `DatabricksLakebase(database_instance_name=...)`. Bloque de código Python (derecha): loop agregando recursos de tools (VectorSearchRetrieverTool, UnityCatalogTool), `system_policy = SystemAuthPolicy(resources=resources)`, lista extensa de `api_scopes` (sql.statement-execution, mcp.genie, mcp.external, catalog.connections, mcp.vectorsearch, vectorsearch.vector-search-indexes, iam.current-user:read, sql.warehouses, dashboards.genie, serving.serving-endpoints, iam.access-control:read, apps.apps, mcp.functions, vectorsearch.vector-search-endpoints).

## Slide 61
Bloque de código Python: `user_policy = UserAuthPolicy(...)`, `input_example` de ejemplo (pregunta "What is an LLM agent?" con custom_inputs thread_id), `with mlflow.start_run(): logged_agent_info = mlflow.pyfunc.log_model(name="agent", python_model="agent.py", input_example=..., pip_requirements=[...], resources=resources)`.

Columna derecha: captura de pantalla del Catalog Explorer mostrando "memory_agent version 37" con tab "Lineage" seleccionado, tabla de linaje (agents_bo_cheng_dnb_demos-agents-memory_agent — Downstream Serving endpoint; memory_agent_0_payload y memory_agent_8_payload — Downstream Table; get_cyber_threat_info y get_user_info — Upstream Function; 02-lakebase-langgraph-checkpointer-agent — Upstream Notebook).

## Slide 62
Bloque de código Python: `from databricks import agents; agents.deploy(UC_MODEL_NAME, uc_registered_model_info.version, environment_vars={DATABRICKS_HOST, DATABRICKS_CLIENT_ID, DATABRICKS_CLIENT_SECRET vía secrets}, tags={"endpointSource": "playground"})`.

Columna derecha: captura de pantalla del "Playground" de Databricks mostrando panel izquierdo con JSON de `custom_inputs` (toggle "On", ejemplo `{"thread_id": "4"}`), toggle "AI judge", y panel de chat derecho con selección de endpoint `agents_bo_cheng_dnb_demos-agents-memory_agent`, pregunta de usuario "Who was just mentioned in the previous context?" y respuesta del agente mencionando a George Miller, Finance, malware threat, IP 192.168.1.21, con "Suggested questions" y link "View Trace".

## Slide 63
Texto sobre integración con Databricks app (Streamlit elegido para este agente), dos modos de auth (app authorization / user authorization on-behalf-of-user), y el rol clave de `thread_id` para retomar conversaciones.

Captura de pantalla de un mockup de app "Databricks Cybersecurity Agent" (fondo crema, icono de escudo): subtítulo "This AI assistant is powered by Databricks Foundation Models and features" con bullet "Conversation memory with Lakebase"; hilo de chat con burbujas: usuario pregunta "Who did I just mention?", respuesta "You just mentioned George Miller."; usuario pregunta "What was I concerned about with George?", respuesta detallando amenaza de ciberseguridad detectada por IDS, IP 192.168.1.21, Threat ID 8, TCP, timestamp 2025-09-08 02:35:06.534731; campo de input inferior "What cybersecurity event are you concerned about?".

## Slide 64
"CONCLUSION" del capítulo 6: resume la arquitectura de agente stateful con Lakebase, UC functions, MLflow, y Databricks AI Agent Framework. Columna derecha "RESOURCES": enlaces (Documentation, Example notebooks, GitHub repository — decorativos). Elemento gráfico decorativo rojo.

## Slide 65
Página final de cierre (fondo oscuro). "Build Intelligent Apps on the Databricks Platform" con texto resumen y botones "Try Databricks free" / "Watch a demo". Sección "Documentation" con botones "Read Databricks Apps documentation" / "Read Lakebase documentation". Sección "About Databricks" con boilerplate corporativo (20,000+ organizaciones, clientes ejemplo adidas/AT&T/Bayer/Block/Mastercard/Rivian/Unilever, Fortune 500, sede San Francisco, 30+ oficinas, enlaces a redes sociales). Logo Databricks. Copyright "© Databricks 2026. All rights reserved." con menciones legales de Apache/Spark. Decorativa/boilerplate — sin contenido técnico nuevo.
