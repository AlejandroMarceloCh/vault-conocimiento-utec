---
curso: BIGDATA
titulo: 14 - Semana 12/Hands on guide to apps on databricks
slides: 65
fuente: 14 - Semana 12/Hands on guide to apps on databricks.pdf
---

A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                     2




Contents
                                                                     Conclusion                                                  22

Introduction to Building Apps
on Databricks                                                   4    Get started                                                 22




The application deployment challenge                             6
                                                                     The Transactional Foundation
                                                                     for Intelligent Applications                               23
Databricks Apps and Lakebase: A unified application platform     7

What this guide covers                                           8
                                                                     Introduction		                                              24

                                                                     Why Lakebase and Databricks Apps		                          24



                                                                9
                                                                     Getting started: Build a transactional app with Lakebase    25
From Notebooks to Production
                                                                     Extending the lakehouse with Lakebase                       31
Applications
                                                                     Summary                                                     32




The challenge of production data applications                   10

Architecture and how it works                                   10

Anatomy of the app                                              13

Defining Databricks Asset Bundles resources                     17

Considerations and best practices                               20
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                 3




                                                                33
                                                                             Lessons learned                                 49
Turning Analytics Into                                                       Try it yourself                                 49
Applications



Introduction: Analytics and operations are converging                   34
                                                                             How to Build AI Agents With
                                                                             Conversational Memory Using Lakebase           50
What is reverse ETL?                                                    34

Challenges of reverse ETL                                               35

Lakebase: Integrated by default for easy reverse ETL                    35   Why conversational memory matters               51

Sample use case: Building an intelligent support portal with Lakebase   36   Using Lakebase as the state layer for agents    51

Conclusion                                                              39   Memory patterns for AI agents                   52

                                                                             Architecture overview                           53




                                                                40
                                                                             Implementation guide                            54
Delivering Secure, Real-Time                                                 Conclusion                                      64
Applications on Databricks                                                   Resources                                       64




Introduction                                                            41

Key technologies                                                        42

Solution overview                                                       42

Step-by-step guide                                                      43

Highlights on Postgres connection with OAuth                            48
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S




01                                                              Introduction to Building
                                                                Apps on Databricks
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                         5




                                                                                     The problem isn’t a lack of data or AI capability. It’s the difficulty of
Introduction to Building Apps                                                        delivering those capabilities as trusted, production-grade applications
on Databricks                                                                        that others can use.


As AI and analytics capabilities mature across organizations, a new challenge        This guide is designed to help close that gap. Through practical walkthroughs,
has emerged: delivering insights in a form people can actually use.                  working code examples and real-world patterns, you’ll learn how Databricks
                                                                                     Apps and Lakebase work together to take an application from a working
Data teams today have powerful tools for exploration and analysis. Notebooks         prototype to a production application without leaving the platform.
support rapid iteration, dashboards enable broad visibility and models drive
prediction and automation. But when business requirements shift to an
interactive application that combines live data with user input — such as an
AI assistant embedded in a workflow or a custom tool tailored to a specific
operational process — teams often hit a wall.


Historically, building production applications meant stepping outside the
data platform entirely. Moving from analysis to application meant provisioning
infrastructure, configuring databases, implementing authentication, setting up
deployment pipelines and navigating security reviews. Each step added cost, risk
and time — without directly contributing to the business value of the application.
For many organizations, this last mile challenge delayed applications for months
or stopped them from ever shipping.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                             6




                                                                                       ■   Deployment automation and environment management: Moving code
T H E A P P LI CAT I O N D E P LOY M E N T C H A LLE N G E
                                                                                           from development to staging to production requires continuous integration
                                                                                           and continuous delivery (CI/CD) pipelines, environment configuration and
For teams building data and AI applications today, the path from working                   careful coordination
prototype to production deployment is filled with undifferentiated heavy lifting.      ■   Governance and compliance: Enterprise applications must respect data
Whether you’re a Python-fluent data engineer extending an analysis                         access policies, maintain audit trails and enforce fine-grained permissions.
or a JavaScript developer building on lakehouse data, you encounter the                    Implementing governance controls in application code — separate from the
same obstacles:                                                                            governance already established in the data platform — duplicates work and
■   Infrastructure provisioning and management: Every application needs                    creates opportunities for policy drift.
    somewhere to run. Traditionally, this means provisioning VMs or containers,
    configuring load balancers, setting up SSL certificates and managing               These challenges create real costs. Deployment complexity kills momentum:
    scaling policies.                                                                  When you can’t ship changes quickly and confidently, you slow iteration and
■   Authentication and security complexity: Production applications require            waste time coordinating between teams. The result is that valuable capabilities

    secure authentication flows, credential management and access controls.            remain locked inside the data platform, accessible only to some technical users

    Implementing open authorization (OAuth) correctly, rotating secrets and            rather than the broader organization.

    ensuring compliance with security policies demands specialized knowledge.
    Getting it wrong creates vulnerabilities, and getting it right takes significant
    engineering effort.
■   Data synchronization and latency: Interactive applications need fast
    access to data, but analytical data stores aren’t optimized for the low-
    latency, high-concurrency access patterns that user-facing applications
    need. Building pipelines to move data from analytical systems to operational
    databases and keeping that data fresh adds another layer of complexity and
    potential failure points.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                        7




DATA B R I C KS A P P S A N D L A K E BAS E :                                     Databricks Apps provides a serverless application hosting platform for running
                                                                                  web applications built with open source frameworks like Streamlit, Dash,
A U N I F I E D A P P LI CAT I O N P L AT FO R M
                                                                                  Flask, FastAPI and React. Applications inherit the platform’s built-in security,

Databricks addresses these challenges by bringing application hosting and         compliance and resource management features. There’s no infrastructure to

operational databases directly into the Data Intelligence Platform. Rather than   provision, no containers to manage and no scaling policies to configure. Apps

requiring separate infrastructure for applications, Databricks provides an        automatically integrate with Unity Catalog for governance and support both

integrated solution where apps run alongside the data and AI capabilities they    service principal authentication for app-level access and on-behalf-of-user

depend on.                                                                        authorization for user-level permissions.

                                                                                  Lakebase is a fully managed PostgreSQL database deeply integrated with the
                                                                                  lakehouse. It provides the transactional, low-latency data access that interactive
                                                                                  applications require while automatically synchronizing data from Unity Catalog
                                                                                  tables. With Lakebase, you can:
                                                                                  ■   Serve analytical insights to applications in real time
                                                                                  ■   Store application state and user inputs
                                                                                  ■   Maintain full atomicity, consistency, isolation and durability (ACID)
                                                                                      transaction support
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                           8




All of this is possible without building custom extract, transform, load (ETL)       Historically, bridging OLTP and OLAP systems involved complex data engineering
pipelines or managing database infrastructure.                                       and bespoke integration layers. Deploying applications required separate
                                                                                     DevOps teams, disparate CI/CD pipelines and manual security configurations.
Together, these capabilities transform what’s possible:                              With Lakebase and Databricks Apps together, these complexities are significantly
                                                                                     reduced. Developers can access real-time analytical data directly from the
                                                                                     transactional layer and deploy interactive applications in minutes rather
  TRADITIONAL APPROACH                            MODERN DATABRICKS APPS
                                                                                     than months.
                                                  AND LAKEBASE APPROACH

  Separate hosting infrastructure                 Serverless compute and zero        W H AT T H I S G U I D E C OV E R S
                                                  infrastructure management
                                                                                     This guide provides hands-on instruction for building production-ready data
  Custom authentication systems                   Built-in OAuth and Unity Catalog   and AI applications on Databricks. Rather than focusing on isolated features, each
                                                  integration                        chapter walks through a complete application pattern using working code you
                                                                                     can adapt to your own use cases.
  Manual data synchronization                     Automated synced tables from
  pipelines                                       Unity Catalog                      You’ll see how to:
                                                                                     ■   Move from notebooks and prototypes to real applications
  Fragmented governance across                    Unified governance through Unity
                                                                                     ■   Serve analytical data and application state through a transactional layer
  systems                                         Catalog
                                                                                     ■   Build secure, governed applications without custom infrastructure
  Complex, multi-tool deployment                  Single-command deployment with     ■   Deploy and operate applications using repeatable, production-ready patterns
                                                  Databricks Asset Bundles (DABs)
                                                                                     By the end of this guide, you should clearly understand how to build, deploy and
                                                                                     manage intelligent applications on the Databricks Platform with confidence.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S




02                                                              From Notebooks to
                                                                Production Applications
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                         10




                                                                                   A R C H I T ECT U R E A N D H OW I T WO R KS
From Notebooks to
Production Applications                                                            We’ll walk through a taxi trip application that demonstrates the entire pattern:
                                                                                   a React and FastAPI application that reads from Lakebase synced tables,
by Pascal Vogel, Evan Pandya and Christopher Pries                                 with automatic data updates from Unity Catalog Delta tables happening
                                                                                   within seconds.
T H E C H A LLE N G E O F P R O D U CT I O N DATA A P P LI CAT I O N S
                                                                                   The following diagram provides a simplified view of the solution architecture.
Building production-ready data applications is complex. You often need separate
tools to host the app, manage the database and move data between systems.
Each layer adds setup, maintenance and deployment overhead.


Databricks simplifies this by consolidating everything on a single platform —
the Databricks Data Intelligence Platform. Databricks Apps runs web applications
on serverless compute. Lakebase provides a managed Postgres database that
syncs with Unity Catalog, giving apps fast access to governed data. And with
Databricks Asset Bundles (DABs), you can package code, infrastructure and data
pipelines together and deploy them with a single command.                          At a high level, Databricks Apps serves as the front end where users explore and
                                                                                   visualize data. Lakebase provides the Postgres database that the app queries,
This chapter shows how these three pieces work together to build and deploy a      keeping it close to live data from Unity Catalog with synced tables. DABs tie
real data application, from syncing Unity Catalog data to Lakebase to running a    everything together by defining and deploying all resources — app, database and
web app on the Databricks Platform and automating deployment with DABs.            data synchronization — as one version-controlled unit.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                      11




Main solution components:
■   Databricks app: Users interact with a web application built using React,
    TypeScript, Vite and FastAPI. The app reads data from a Unity Catalog synced
    table stored in a Lakebase Postgres database.
■   Unity Catalog synced table: A read-only Postgres table that’s automatically
    synced with a Unity Catalog table via a managed synchronization pipeline
    and runs on a Lakebase database instance
■   Lakebase database instance: Manages Lakebase storage and compute and
    provides Postgres endpoints for the Databricks app to connect to
■   Unity Catalog table: A Delta table containing data about taxi rides in New
    York City cloned from the samples.nyctaxi.trips sample table available in
    every database workspace
■   Databricks Asset Bundles (DABs): A bundle in which all key elements of the
    architecture are defined in code


The example app displays recent taxi trips in table and chart format and
automatically polls for new trips. It reads data from a Lakebase synced table,
which mirrors a Delta table in Unity Catalog.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                             12




Because the synced table updates automatically, any change in the Unity        Then trigger a refresh of the synced trips_synced table:
Catalog table appears in the app within seconds — no custom ETL needed.

You can test this by inserting new data into the source Delta table and then
refreshing the synced table:


SQL

  INSERT INTO main.default.trips (id, tpep_pickup_datetime, tpep_
  dropoff_datetime, trip_distance, fare_amount, pickup_zip, dropoff_
  zip)

  VALUES

    (21933, '2025-08-20 10:00:00', '2025-09-20 10:30:00', 5.2, 18.50,
  '10001', '10002'),

    (21934, '2025-08-21 11:00:00', '2025-09-21 11:30:00', 6.1, 20.00,
  '10003', '10004'),

    (21935, '2025-08-22 12:00:00', '2025-09-22 12:30:00', 7.3, 22.75,
  '10005', '10006')

                                                                               The managed pipeline that powers the sync creates a snapshot copy of the
                                                                               source Delta table and writes to the target Postgres table.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                   13




Within a few seconds, the new records appear in the dashboard. The app polls    A N ATO M Y O F T H E A P P
for updates and allows users to refresh on demand, demonstrating how Lakebase
keeps operational data current without requiring additional engineering.        Let’s examine how the various elements of the solution come together in the
                                                                                Databricks app.

                                                                                Authentication and database connection

                                                                                Each Databricks app has a unique service principal identity assigned on creation
                                                                                that it uses to interact with other Databricks resources, including Lakebase.

                                                                                Lakebase supports OAuth machine-to-machine (M2M) authentication. An app
                                                                                can obtain a valid token using the WorkspaceClient in the Databricks SDK for
                                                                                Python along with its service principal credentials. The WorkspaceClient handles
                                                                                refreshing the short-lived OAuth token, which expires in an hour.




This seamless data flow happens because Lakebase synced tables handle all
synchronization automatically.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                     14




The app then uses this token when establishing a connection to Lakebase using   PYTHON
the Psycopg Python Postgres adapter:
                                                                                # app/main.py

                                                                                [...]
PYTHON
                                                                                def get_taxi_trips_data() -> List[TaxiTrip]:
  # app/database.py                                                                 query = f"""
                                                                                        SELECT id, tpep_pickup_datetime, tpep_dropoff_datetime,
  [...]                                                                         trip_distance,
                                                                                                fare_amount, pickup_zip, dropoff_zip
  def get_connection(self):                                                             FROM {db_connection.postgres_schema}.{db_connection.
          token = self.workspace_client.config.oauth_token().access_            postgres_table}
  token                                                                                 ORDER BY tpep_pickup_datetime DESC
                                                                                        LIMIT 100
             return psycopg.connect(                                                """
                 host=self.postgres_host,
                 port=5432,                                                         with db_connection.get_connection() as conn:
                 dbname=self.postgres_database,                                         with conn.cursor() as cur:
                 user=self.postgres_username,                                               cur.execute(query)
                 password=token,                                                            rows = cur.fetchall()
                 sslmode="require",
             )                                                                      return [
                                                                                        TaxiTrip(
  [...]                                                                                      id=row[0],
                                                                                             tpep_pickup_datetime=row[1].isoformat(),
                                                                                             tpep_dropoff_datetime=row[2].isoformat(),
                                                                                             trip_distance=row[3],
The Postgres host and database name are automatically set as environment                     fare_amount=row[4],
variables for the Databricks app when using the Lakebase resource for apps.                  pickup_zip=row[5],
                                                                                             dropoff_zip=row[6],
                                                                                        )
The Postgres user is either the app service principal — when deployed to                for row in rows
                                                                                    ]
Databricks Apps — or the Databricks username of the user running the
app locally.                                                                    [...]

                                                                                @app_api.get("/taxi-trips", response_model=List[TaxiTrip])
RESTful FastAPI back end                                                        def get_taxi_trips():
                                                                                    return get_taxi_trips_data()
The app’s FastAPI back end uses this connection to query Lakebase and fetch
                                                                                [...]
the latest trips data from the synced table:
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                               15




In addition to serving API endpoints, FastAPI can also serve static files using the   React front end
StaticFiles class. By bundling our React front end using Vite’s build process, we
can generate a set of static files that we can serve using FastAPI.                   The React front end calls the FastAPI endpoint to display the data:


                                                                                      JAVASCRIPT
PYTHON
                                                                                       /** app/frontend/src/taxiApi.ts */
  # app/main.py
                                                                                       import axios from "axios";
  from fastapi import FastAPI
                                                                                       import type { TaxiTrip } from "./App";
  from fastapi.staticfiles import StaticFiles
                                                                                       const apiClient = axios.create({ baseURL: "/api" });
  [...]
                                                                                       export const getTaxiTrips = async (): Promise<TaxiTrip[]> => {
  app = FastAPI()
                                                                                          const response = await
                                                                                       apiClient.get<TaxiTrip[]>("/taxi-trips");
  app_frontend = StaticFiles(directory="frontend/dist", html=True)
                                                                                          return response.data;
  app_api = FastAPI()
                                                                                       };
  app.mount("/api", app_api) # Mount more specific route first,
  catchall route second

  app.mount("/", app_frontend)

  [...]
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S              16




The example application uses ag-grid and ag-charts for visualization and
automatically checks for new data every few seconds:



JAVASCRIPT

  /** app/frontend/src/App.tsx */

  const fetchData = async () => {
      try {
        setError(null);
        const data = await getTaxiTrips();
        setTaxiData(data);
        setLastRefresh(new Date());
      } catch (err) {
        setError("Failed to fetch taxi data");
        console.error("Error fetching taxi data:", err);
      }

  useEffect(() => {
    fetchData();

     const interval = setInterval(fetchData, 3000);

    return () => clearInterval(interval);
  }, []);

  [...]
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                    17




D E F I N I N G DATA B R I C KS AS S E T B U N D LES R ES O U R C ES               PYTHON

                                                                                    # databricks.yml
All the Databricks resources and application code shown above can be
maintained as a DAB in a single source code repository. This also means that all    bundle:
                                                                                      name: apps-lakebase-dabs
resources can be deployed to a Databricks workspace with a single command.
See the GitHub repository for detailed deployment instructions.                     # Uploads the app/frontend/dist folder when deploying the bundle
                                                                                    sync:
                                                                                      include:
This simplifies the software development lifecycle and enables deployments via          - app/frontend/dist
CI/CD best practices across development, staging and production environments.
                                                                                    # Include app, database instance and synced table
                                                                                    include:
The following sections explain the bundle files in more detail.                       - resources/*.yml

                                                                                    # Optionally override the catalog and schema for the synced table
Bundle configuration                                                                variables:
                                                                                      catalog:
                                                                                        default: main
The databricks.yml contains the DABs bundle configuration in the form of bundle       schema:
settings and included resources:                                                        default: default

                                                                                    # Add more environments as needed
                                                                                    targets:
                                                                                      dev:
                                                                                        default: true
                                                                                        mode: development
                                                                                        workspace:
                                                                                           host: https://company-dev.cloud.databricks.com/

                                                                                      staging:
                                                                                        mode: production
                                                                                        workspace:
                                                                                          host: https://company-stg.cloud.databricks.com/
                                                                                          root_path: /Users/${workspace.current_user.userName}/.
                                                                                    bundle/${bundle.name}/${bundle.target}




                                                                                   In our example, we only define a development and a staging environment.
                                                                                   For a production use case, consider adding additional environments. See the
                                                                                   Databricks DAB examples repository and the DABs documentation for more
                                                                                   advanced configuration examples.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                         18




Lakebase setup and sync with Unity Catalog                                          PYTHON

                                                                                     # resources/database.yml
To define a Lakebase instance in DABs, use the database_instance resource.
At a minimum, we need to define the capacity field of the instance.                  resources:
                                                                                       database_instances:
                                                                                         trips-app-instance:
Additionally, we define a synced_database_table resource, which sets up                    name: trips-app-instance
a managed synchronization pipeline between a Unity Catalog table and a                     capacity: CU_1
                                                                                       synced_database_tables:
Postgres table.                                                                          trips-app-synced-table:
                                                                                           # Synced table Unity Catalog object name:
                                                                                           name: ${var.catalog}.${var.schema}.trips_synced
For this, define a source table via source_table_full_name. The source table in
                                                                                           database_instance_name: ${resources.database_instances.trips-
Unity Catalog requires a unique (composite) primary key to process updates           app-instance.name}
                                                                                           # Postgres database where synced table is located:
defined in the primary_key_columns field.                                                  logical_database_name: trips-app-database
                                                                                           spec:
The location of the target table in Lakebase is determined by the target database            source_table_full_name: ${var.catalog}.${var.schema}.trips
                                                                                             scheduling_policy: SNAPSHOT
object (logical_database_name) and the table name (name).                                    primary_key_columns:
                                                                                                - id




                                                                                    A synced table is also a Unity Catalog object. In this resource definition, we place
                                                                                    the synced table in the same catalog and schema as the source table using DABs
                                                                                    variables defined in databricks.yml. You can override these defaults by setting
                                                                                    different variable values.

                                                                                    For our use case, we use the SNAPSHOT sync mode. Refer to the
                                                                                    “Considerations and best practices” section of this chapter for a discussion
                                                                                    of the available options.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                         19




Databricks Apps resource                                                             PYTHON

                                                                                      # resources/app.yml
DABs allow us to define both the Databricks Apps compute resource as an
app resource and the application source code in one bundle. This allows us to         resources:

keep both the Databricks resource definition and the source code in a single             apps:
repository. In our case, the app source code, based on FastAPI and Vite, is stored
                                                                                           trips-app:
in the top-level app directory of the project.
                                                                                             name: trips-app
The configuration dynamically references the database_name and
                                                                                             source_code_path: ../app # App source code location
instance_name defined in the database.yml resource definition.
                                                                                             resources: # Resources that the app service principal can
                                                                                      access

                                                                                                 - name: lakebase

                                                                                                   database:

                                                                                                  database_name: ${resources.synced_database_tables.trips-
                                                                                      app-synced-table.logical_database_name}

                                                                                                  instance_name: ${resources.database_instances.trips-app-
                                                                                      instance.name}

                                                                                                     permission: CAN_CONNECT_AND_CREATE




                                                                                     Database is a supported app resource that can be defined in DABs. By defining
                                                                                     the database as an app resource, we automatically create a Postgres role to be
                                                                                     used by the app service principal when interacting with the Lakebase instance.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                 20




C O N S I D E R AT I O N S A N D B ES T P R ACT I C ES
                                                                                                  SNAPSHOT           TRIGGERED           CONTINUOUS

Create modular and reusable bundles                                                 Update        Full table         Initial full copy   Initial load
                                                                                    method        replacement on     and incremental     and real-time
While this example deploys to development and staging environments, DABs                          each run           changes             streaming updates
make it easy to define multiple environments to fit your development lifecycle.
Automate deployment across these environments by setting up CI/CD pipelines
with Azure DevOps, GitHub Actions or other DevOps platforms.                        Performance   10x more           Balanced cost       Higher cost —
                                                                                                  efficient than     and performance     continuously
                                                                                                  other modes                            running
Use DABs substitutions and variables to define environment-specific
configurations. For instance, you can define different Lakebase instance capacity   Latency       High latency —     Medium latency      Lowest latency —
configurations for development and production to reduce costs. Similarly, you                     scheduled or       — on demand         real time, ~15 sec
                                                                                                  manual
can define different Lakebase sync modes for your synced tables to meet
environment-specific data latency requirements.
                                                                                    Best for      ■   Infrequent     ■   Compromise      ■   Mission-critical
                                                                                                      changes            between cost        systems
Choose Lakebase sync modes and optimize performance                                               ■   Modifying          and latency     ■   Real-time data
                                                                                                      >10% of the    ■   Reasonably          requirements
Choosing the right Lakebase sync mode is key to balancing cost and                                    source table       current data    ■   No manual
                                                                                                  ■   Low-           ■   Controlled          refresh
data freshness.
                                                                                                      urgency,           refresh             tolerance
                                                                                                      high-volume        timing
                                                                                                      updates


                                                                                    Limitations   ■   Higher         ■   Avoid running   ■   Highest cost
                                                                                                      latency            >every five     ■   Requires a
                                                                                                  ■   Full table         minutes             change data
                                                                                                      re-creation    ■   Requires a          feed
                                                                                                      each time          change data     ■   Continuous
                                                                                                                         feed                resource
                                                                                                                     ■   More                consumption
                                                                                                                         expensive
                                                                                                                         if run too
                                                                                                                         frequently

A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                    21




Set up notifications for your managed sync pipeline to be alerted in case       Authentication and authorization
of failures.
                                                                                Use OAuth 2.0 for authorization and authentication — don’t rely on legacy
To improve query performance, right-size your Lakebase database instance        personal access tokens (PATs). During development on your local machine, use
by choosing an appropriate instance capacity. Consider creating indexes on      the Databricks command-line interface (CLI) to set up OAuth U2M authentication
the synced table in Postgres that match your query patterns and use the pre-    to seamlessly interact with live Databricks resources such as Lakebase.
installed pg_stat_statements extension to investigate query performance.
                                                                                Similarly, your deployed app uses its associated service principal for OAuth M2M
Prepare your app for production                                                 authentication and authorization with other Databricks services. Alternatively, set
                                                                                up user authorization for your app to perform actions on Databricks resources on
The example application implements a polling-based approach to get the latest   behalf of your app users.
data from Lakebase. Depending on your requirements, you can also implement
a push-based approach using WebSockets or server-sent events to use server      See also Best Practices for Databricks Apps in the Databricks Apps
resources more efficiently and increase the timeliness of data updates.         documentation for additional general and security best practices.

To scale to a larger number of app users by reducing the need for the FastAPI
back end to trigger database operations, consider implementing caching, such
as fastapi-cache, for in-memory caching of query results.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                      22




C O N C LU S I O N                                                                    G E T S TA R T E D

Building production data applications shouldn’t mean juggling separate tools for      Learn more about Lakebase, Databricks Apps and DABs by viewing the
deployment, data synchronization and infrastructure management. Databricks            Databricks documentation. For more developer resources on Databricks Apps,
Apps gives you serverless compute to run your Python and Node.js applications         take a look at the Databricks Apps Cookbook and Cookbook resource collection.
without managing infrastructure. Lakebase synced tables automatically deliver
low-latency data from Unity Catalog Delta tables to Postgres, eliminating custom
ETL pipelines. DABs tie it all together by allowing you to package your application
code, infrastructure definitions and data sync configurations into a single,
version-controlled bundle that deploys consistently across environments.

Deployment complexity kills momentum. When you can’t ship changes quickly
and confidently, you slow down iteration, introduce environment drift and waste
time coordinating between teams. By treating your entire application stack as
code with DABs, you:
■   Enable CI/CD automation
■   Ensure consistent deployments across dev, staging and production
■   Allow your team to focus on building features instead of fighting
    deployment pipelines


This is how you move from prototype to production without the usual
deployment headaches.

The complete example is available in the GitHub repository with step-by-step
deployment instructions.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S




03                                                              The Transactional Foundation
                                                                for Intelligent Applications
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                            24




                                                                                     Databricks Apps supplies a serverless runtime for the UI, along with built-in
The Transactional Foundation                                                         authentication, fine-grained permissions and governance controls that are
for Intelligent Applications                                                         automatically applied to the same data that Lakebase serves. This makes it
                                                                                     easy to build and deploy apps that combine transactional state, analytics
By Jasper Puts and Antonio Javier Samaniego Jurado
                                                                                     and AI without stitching together multiple platforms, synchronizing databases,
                                                                                     replicating pipelines or reconciling security policies across systems.
I N T R O D U CT I O N

                                                                                     W H Y L A K E BAS E A N D DATA B R I C KS A P P S
Building internal tools or AI‑powered applications the traditional way throws
developers into a maze of repetitive, error‑prone tasks. First, they must spin up
                                                                                     Lakebase and Databricks Apps work together to simplify full-stack development
a dedicated Postgres instance, configure networking, backups and monitoring,
                                                                                     on the Databricks Platform:
and then spend hours — or days — plumbing that database into the front-end
framework they’re using. Additionally, they must write custom authentication
                                                                                     ■   Lakebase provides a fully managed Postgres database with fast reads,

flows, map granular permissions and keep those security controls in sync across          writes and updates, plus modern features such as branching and point-in-

the UI, API layer and database. Each application component lives in a different          time recovery

environment, from a managed cloud service to a self‑hosted VM. This forces           ■   Databricks Apps provides the serverless runtime for your application front
developers to juggle disparate deployment pipelines, environment variables and           end, with built-in identity access control and integration with Unity Catalog
credential stores. The result is a fragmented stack where a single change, such as       and other lakehouse components
a schema migration or a new role, ripples through multiple systems, demanding
manual updates, extensive testing and constant coordination. All of this overhead
                                                                                     By combining the two, you can build interactive tools that store and update
distracts developers from the real value add — building the product’s core
                                                                                     state in Lakebase, access governed data in the lakehouse and serve everything
features and intelligence.
                                                                                     through a secure, serverless UI — all without managing separate infrastructure. In
                                                                                     the next example, we’ll show how to build a simple holiday request approval app
With Databricks Lakebase and Databricks Apps, the entire application stack
                                                                                     using this setup.
sits together, alongside the lakehouse. Lakebase is a fully managed Postgres
database that offers low-latency reads and writes, integrated with the same
underlying lakehouse tables that power your analytics and AI workloads.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                    25




G E T T I N G S TA R T E D : B U I LD A T R A N SACT I O N A L A P P             Here’s what the solution covers:

W I T H L A K E BAS E                                                            1.   Provision a Lakebase database
                                                                                      Set up a serverless, Postgres OLTP database with a few clicks.
This walkthrough demonstrates how to create a simple Databricks app that helps
                                                                                 2. Create a Databricks app
managers review and approve holiday requests from their team. The app is built
                                                                                      Build an interactive app using a Python framework — such as Streamlit or
using Databricks Apps and uses Lakebase as the back-end database to store
                                                                                      Dash — that reads from and writes to Lakebase.
and update the requests.
                                                                                 3. Configure schema, tables and access controls
                                                                                      Create the necessary tables and assign fine-grained permissions to the app
                                                                                      using the app’s client ID.

                                                                                 4. Securely connect and interact with Lakebase
                                                                                      Use the Databricks SDK and SQLAlchemy to securely read from and write to
                                                                                      Lakebase from your app code.


                                                                                 The walkthrough is designed to get you started quickly with a minimal working
                                                                                 example. Later, you can extend it with a more advanced configuration.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                       26




Step 1: Provision Lakebase                                                        Step 2: Create a Databricks app and add
                                                                                  database access
Before building the app, you’ll need to create a Lakebase database. To do this,
go to the Compute tab, select OLTP Database and provide a name and size.          Now that we have a database, let’s create the Databricks app that will connect
This provisions a serverless Lakebase instance. In this example, our database     to it. You can start from a blank app or choose a template — e.g., Streamlit or
instance is called lakebase-demo-instance.                                        Flask. After naming your app, add the database as a resource. In this example,
                                                                                  the pre-created databricks_postgres database is selected.




                                                                                  Adding the database resource automatically:
                                                                                  ■   Grants the app CONNECT and CREATE privileges
                                                                                  ■   Creates a Postgres role tied to the app’s client ID


                                                                                  This role will later be used to grant table-level access.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                         27




Step 3: Create a schema, define a table                                   1.   Retrieve the app’s client ID
and set permissions                                                            From the app’s Environment tab, copy the value of the DATABRICKS_
                                                                               CLIENT_ID variable. You’ll need this for the GRANT statements.
With the database provisioned and the app connected, you can create the
                                                                          2. Open the Lakebase SQL editor
schema and define the table the app will use.
                                                                               Go to your Lakebase instance and click New Query. This opens the SQL
                                                                               editor with the database endpoint already selected.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                            28




3. Run the following SQL:                                               Although using the SQL editor is a quick and effective way to perform this
                                                                        process, managing database schemas at scale is best handled by dedicated
SQL                                                                     tools that support versioning, collaboration and automation. Tools like Flyway and

  -- 1. Create schema                                                   Liquibase allow you to track schema changes, integrate with CI/CD pipelines and
                                                                        ensure your database structure evolves safely alongside your application code.
  CREATE SCHEMA IF NOT EXISTS holidays;

  -- 2. Create the table within the schema

  CREATE TABLE IF NOT EXISTS holidays.holiday_requests (

     request_id SERIAL PRIMARY KEY,
     employee_name VARCHAR(255) NOT NULL,
     start_date DATE NOT NULL,
     end_date DATE NOT NULL,
     status VARCHAR(50) NOT NULL,
     manager_note TEXT

  );

  -- 3. Insert some values

  INSERT INTO holidays.holiday_requests (employee_name, start_date,
  end_date, status, manager_note)

     VALUES
       ('Joe', '2025-08-01', '2025-08-20', 'Pending', ''),
       ('Suzy', '2025-07-22', '2025-07-25', 'Pending', ''),
       ('Charlie', '2025-08-01', '2025-08-05', 'Pending', '');

  -- 4. The Lakebase resource in the App already allows connecting to
  Lakebase database instance and the database.

  --      Grant permissions on the required schema and table.
  --      Replace the <CLIENT_ID> with the value from your App

  GRANT USAGE ON SCHEMA holidays TO "<CLIENT_ID>";

  GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE
  holidays.holiday_requests TO "<CLIENT_ID>";
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                               29




Step 4: Build the app                                                             Step 5: Connect securely to Lakebase
With permissions in place, you can now build your app. In this example, the app   Use SQLAlchemy and the Databricks SDK to connect your app to Lakebase with
fetches holiday requests from Lakebase and allows a manager to approve or         secure, token-based authentication. When you add the Lakebase resource,
reject them. Updates are written back to the same table.                          PGHOST and PGUSER are exposed automatically. The SDK handles token caching.


                                                                                  PYTHON

                                                                                   import os
                                                                                   import time

                                                                                   import pandas as pd
                                                                                   from databricks.sdk import WorkspaceClient
                                                                                   from databricks.sdk.core import Config
                                                                                   from sqlalchemy import create_engine, event, text

                                                                                   app_config = Config()
                                                                                   workspace_client = WorkspaceClient()

                                                                                   postgres_username = app_config.client_id
                                                                                   postgres_host = os.getenv("PGHOST")
                                                                                   postgres_port = 5432
                                                                                   postgres_database = "lakebase_demo"

                                                                                   postgres_pool = create_engine(f"postgresql+psycopg://{postgres_
                                                                                   username}:@{postgres_host}:{postgres_port}/{postgres_database}")

                                                                                   @event.listens_for(postgres_pool, "do_connect")
                                                                                   def provide_token(dialect, conn_rec, cargs, cparams):
                                                                                       """Provide the App's OAuth token. Caching is managed by
                                                                                   WorkspaceClient"""
                                                                                       cparams["password"] =
                                                                                   workspace_client.config.oauth_token().access_token
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                 30




Step 6: Read and update data                                              These code snippets can be used in combination with frameworks such as
                                                                          Streamlit, Dash and Flask to pull the data from Lakebase and visualize it in your
The following functions read from and update the holiday request table:
                                                                          app. To ensure all necessary dependencies are installed, add the required
                                                                          packages to your app’s requirements.txt file. The following packages are used in
PYTHON                                                                    the code snippets:

  def get_holiday_requests():
      """Fetch all holiday requests from the database."""                 PLAINTEXT
      engine = get_engine()
      df = pd.read_sql_query("SELECT * FROM holidays.holiday_              pandas==2.3.1
  requests;", engine)                                                      databricks-sdk==0.57.0
      return df                                                            psycopg[binary]==3.2.9
                                                                           sqlalchemy==2.0.41

  def update_request_status(request_id, status, comment):
      """Update the status and manager note for a specific holiday
  request."""
      engine = get_engine()
      with engine.begin() as conn:
          conn.execute(
              text("""
                   UPDATE holidays.holiday_requests
                   SET status = :status, manager_note = :comment
                   WHERE request_id = :request_id
                   """
              ),
              {"status": status, "comment": comment or "", "request_
  id": request_id}
          )
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                           31




E X T E N D I N G T H E L A K E H O U S E W I T H L A K E BAS E                    Lakebase is natively integrated with Databricks, including data synchronization,
                                                                                   identity authentication and network security — just like other data assets in the
Lakebase adds transactional capabilities to the lakehouse by integrating a fully   lakehouse. As a result, you don’t need custom ETL or reverse ETL to move data
managed OLTP database directly into the platform. This reduces the need for        between systems. For example:
external databases or complex pipelines when building applications that require
                                                                                   ■   You can serve analytical features back to applications in real time using the
reads and writes.
                                                                                       Online Feature Store and synced tables
                                                                                   ■   You can synchronize operational data with a Delta table — e.g., for historical
                                                                                       data analysis


                                                                                   These capabilities make it easier to support production-grade use cases like:

                                                                                   ■   Updating state in AI agents
                                                                                   ■   Managing real-time workflows — e.g., approvals, task routing
                                                                                   ■   Feeding live data into recommendation systems or pricing engines

                                                                                   Lakebase is already being used across industries for applications such as
                                                                                   personalized recommendations, chatbot applications and workflow
                                                                                   management tools.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                         32




S U M M A RY

Lakebase provides a transactional Postgres database that works seamlessly with
Databricks Apps and provides easy integration with Lakehouse data. It simplifies
the development of full-stack data and AI applications by eliminating the need
for external OLTP systems or manual integration steps.

If you’re already using Databricks for analytics and AI, Lakebase makes it easier
to add real-time interactivity to your applications. With support for low-latency
transactions, built-in security and tight integration with Databricks Apps, you can
go from prototype to production without leaving the platform.

In this example, we showed you how to:
■   Set up a Lakebase instance and configure access
■   Create a Databricks app that reads and writes to Lakebase
■   Use secure, token-based authentication with minimal setup
■   Build a basic app for managing holiday requests using Python and SQL


For details on usage and pricing, see the Lakebase and Databricks Apps
documentation.
A H A N D S - O N G U I D E TO A P P S O N D ATA B R I C K S




04                                                             Turning Analytics
                                                               Into Applications
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                        34




                                                                                 Without reverse ETL, insights remain in the lakehouse and don’t reach the
Turning Analytics Into Applications                                              applications that need them. The lakehouse is where data gets cleaned, enriched
                                                                                 and turned into analytics, but it isn’t built for low-latency app interactions or
By Firas Farah and Yatish Anand
                                                                                 transactional workloads. That’s where Lakebase comes in. It delivers trusted
                                                                                 lakehouse data directly into the tools where it drives action.
I N T R O D U CT I O N : A N A LY T I C S A N D O P E R AT I O N S
ARE CONVERGING                                                                   In practice, reverse ETL typically involves four key components, all integrated
                                                                                 into Lakebase:
Today’s applications can’t rely solely on raw events. They need curated,         ■   Lakehouse: Stores curated, high-quality data used to drive decisions, such
contextual and actionable data from the lakehouse to power personalization,
                                                                                     as business-level aggregate tables (also known as Gold tables), engineered
automation and intelligent user experiences.
                                                                                     features and ML inference outputs
                                                                                 ■   Syncing pipelines: Move relevant data into operational stores with
Delivering that data reliably with low latency has been a challenge, often
                                                                                     scheduling, freshness guarantees and monitoring
requiring complex pipelines and custom infrastructure.
                                                                                 ■   Operational database: Is optimized for high concurrency, low latency and

W H AT I S R E V E R S E E T L?                                                      ACID transactions
                                                                                 ■   Applications: Serve as the final destination where insights become action,
Reverse ETL syncs high-quality data from a lakehouse into the operational            whether in customer-facing applications, internal tools, APIs or dashboards
systems that power applications. This ensures that trusted datasets and
AI-driven insights flow directly into applications that power personalization,
recommendations, fraud detection and real-time decisioning.                               Lakehouse
                                                                                                               Sync pipelines   Operational       Application
                                                                                                                                 database           layer
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                           35




C H A LLE N G ES O F R E V E R S E E T L                                             L A K E BAS E : I N T EG R AT E D BY D E FAU LT FO R E ASY
                                                                                     REVERSE ETL
Reverse ETL looks simple, but in practice, most teams run into the
these challenges:                                                                    Lakebase removes these barriers and transforms reverse ETL into a fully
■   Brittle, custom-built ETL pipelines: Often require streaming infrastructure,     managed, integrated workflow. It combines a high-performance Postgres engine,
    schema management, error handling and orchestration. They’re brittle and         deep lakehouse integration and built-in data synchronization, allowing fresh
    resource intensive to maintain.                                                  insights to flow into applications without additional infrastructure.
■   Multiple, disconnected systems: Separate stacks for analytics and
    operations result in more infrastructure to manage, additional authentication    These capabilities of Lakebase are especially valuable for reverse ETL:
    layers and a higher risk of format mismatches                                    ■   Deep lakehouse integration: Syncs data from lakehouse tables to Lakebase
■   Inconsistent governance models: Analytical and operational systems often             on a snapshot, scheduled or continuous basis, without building or managing

    reside in different policy domains, making it challenging to apply consistent        external ETL jobs. This replaces the complexity of custom pipelines, retries

    quality controls and audit policies                                                  and monitoring with a native, managed experience.
                                                                                     ■   Fully managed Postgres: Built on open source Postgres, Lakebase supports

These challenges create friction for both developers and the business, slowing           ACID transactions, indexes, joins and extensions such as PostGIS and

efforts to reliably activate data and deliver intelligent, real-time applications.       pgvector. You can connect with existing drivers and tools, such as pgAdmin
                                                                                         or JDBC, thereby avoiding the need to learn new database technologies or
                                                                                         maintain separate OLTP infrastructure.
                                                                                     ■   Scalable, resilient architecture: Lakebase separates compute and storage
                                                                                         for independent scaling, delivering sub-10 ms query latency and thousands
                                                                                         of QPS. Enterprise-grade features include multi-AZ high availability, point-
                                                                                         in-time recovery and encrypted storage, which remove the scaling and
                                                                                         resiliency challenges associated with self-managed databases.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                           36




■   Integrated security and governance: Register Lakebase with Unity Catalog           SA M P LE U S E CAS E : B U I LD I N G A N I N T E LLI G E N T S U P P O R T
    to bring operational data into your centralized governance framework,
                                                                                       P O R TA L W I T H L A K E BAS E
    covering audit trails and permissions at the catalog level. Access via the
    Postgres protocol still utilizes native Postgres roles and permissions, ensuring
                                                                                       As a practical example, let’s walk through how to build an intelligent support
    authentic transactional security while aligning with your broader Databricks
                                                                                       portal powered by Lakebase. This interactive portal helps support teams
    governance model.
                                                                                       triage incoming incidents using ML-driven insights from the lakehouse, such as
■   Cloud-agnostic architecture: Deploy Lakebase alongside your lakehouse in           predicted escalation risk and recommended actions. It does this while allowing
    your preferred cloud environment without rearchitecting your workflows             users to assign ownership, track status and leave comments on each ticket.

With these capabilities in the Databricks Data Intelligence Platform, Lakebase         Lakebase makes this possible by syncing predictions into Postgres while also
replaces the fragmented reverse ETL setup that relies on custom pipelines,             storing updates from the app. This creates a support portal that combines
standalone OLTP systems and separate governance. It delivers an integrated,            analytics with live operations. The same approach applies to many other use
high-performance and secure service, ensuring that analytical insights flow into       cases, including personalization engines and ML-driven dashboards.
applications faster, with less operational effort and with governance preserved.

                                                                                       Watch the app walkthrough.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                    37




Step 1: Sync predictions from the lakehouse to Lakebase

The incident data, enriched with ML predictions, lives in a Delta table and is
updated in near real time via a streaming pipeline. To power the support app,
we use Lakebase reverse ETL to continuously sync this Delta table to a
Postgres table.


In the UI, we select:
■   Sync mode: Continuous for low-latency updates
■   Primary key: incident_id


This ensures the app reflects the latest data with minimal delay.


Note: You can also create the sync pipeline programmatically using the
Databricks SDK.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                     38




Step 2: Create a state table for user inputs

The support app also requires a table to store user-entered data, such as
ownership, status and comments. Since this data is written from the app, it
should be stored in a separate table in Lakebase — rather than the synced table.


Here's the schema:


SQL

  CREATE TABLE support.user_updates (
    incident_id TEXT PRIMARY KEY, owner TEXT, comment TEXT, status
  TEXT
  )




Step 3: Configure Lakebase access in Databricks Apps                               Step 4: Deploy your app code

Databricks Apps supports first-class integration with Lakebase. When creating      With your data synced and permissions in place, you can now deploy the Flask
your app, simply add Lakebase as an app resource and select the Lakebase           app that powers the support portal. The app connects to Lakebase via Postgres
instance and database. Databricks automatically provisions a corresponding         and serves a rich dashboard with charts, filters and interactivity.
Postgres role for the app’s service principal, streamlining app-to-database
connectivity. You can then grant this role the required database, schema and
table permissions.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                       39




C O N C LU S I O N

Bringing analytical insights into operational applications no longer requires a
complex, brittle process. With Lakebase, reverse ETL becomes a fully managed
and integrated capability. It combines the performance of a Postgres engine,
the reliability of a scalable architecture and the governance of the Databricks
Platform. Whether you’re powering an intelligent support portal or building other
real-time, data-driven experiences, Lakebase reduces engineering overhead and
speeds up the path from insight to action.


To learn more about how to create synced tables in Lakebase, check out our
documentation and get started today.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S




05                                                              Delivering Secure, Real-Time
                                                                Applications on Databricks

A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                          41




                                                                                     In the GenAI context, this combination is particularly powerful. Databricks
Delivering Secure, Real-Time                                                         Apps uniquely combines lakehouse data with interactive AI interfaces, such
Applications on Databricks                                                           as Streamlit or Gradio, running directly on the Databricks Data Intelligence
                                                                                     Platform — where your data and models already live. Transactional data from
By Sylvia Christin Schumacher                                                        Lakebase becomes a key enabler powering real-time, context-aware applications
                                                                                     that bring GenAI into production faster with built-in enterprise security and

I N T R O D U CT I O N                                                               governance.


Databricks Lakebase significantly enhances the ability to streamline operational     By surfacing this data directly in app interfaces, enterprises unlock new

databases for building intelligent applications. Databricks Apps enables the quick   capabilities:

deployment of these data and AI apps into production, with out-of-the-box
governance and auth.
                                                                                     ■   AI assistants reference live business data while obeying easily configured
                                                                                         access controls

As a fully managed Postgres service that integrates seamlessly with the              ■   Users make data-driven decisions with up-to-date AI-driven guidance
Databricks Platform, Lakebase allows developers to work with transactional           ■   Retrieval augmented generation (RAG) models ground outputs in
data natively — no custom ETL pipelines, connectors or middleware required.              current facts
Databricks Apps takes this further by eliminating infrastructure management
                                                                                     ■   Workflows stay aligned with evolving transactions through always-available,
entirely, providing managed, serverless compute that automatically inherits your
                                                                                         managed applications
workspace’s security policies and Unity Catalog permissions.

                                                                                     This integration ensures GenAI operates with full enterprise context — exactly
Historically, bridging OLTP and OLAP systems involved complex data engineering
                                                                                     when and where it’s needed, with the production reliability and simplified
and bespoke integration layers, while deploying applications required separate
                                                                                     deployment that modern teams require.
devops and infrastructure teams, disparate CI/CD pipelines and manual security
configurations. With Lakebase and Databricks Apps together, these complexities       In this chapter, we’ll walk through how to build a secure, CI/CD-enabled
are significantly reduced. Developers can now access real-time analytical data       Streamlit app and deploy it as a Databricks app that connects to Lakebase.
directly from the transactional layer and deploy interactive applications in         The app enables users to explore synchronized campaign metrics from Unity
minutes rather than months, making it dramatically easier to incorporate live        Catalog in a read-only interface. This can power use cases such as business
data into production-ready applications.                                             dashboards, campaign monitoring or ad hoc exploration.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                 42




K E Y T EC H N O LO G I ES                                      S O LU T I O N OV E RV I E W

■   Streamlit: Interactive UI framework for Python              The process consists of two major steps:
■   SQLAlchemy: SQL toolkit and ORM for database access         1. Set up Lakebase
                                                                    ■   Create a Lakebase instance (Databricks-managed Postgres)
■   Databricks SDK: Secure OAuth token management
                                                                    ■   Sync a Unity Catalog table into the Postgres instance via Snapshot mode
■   Postgres (Lakebase): Managed OLTP back end
                                                                2. Build a Databricks app
■   DABs: Declarative app deployment and CI/CD integration          ■   Use Streamlit for the UI
■   GitHub: Source control and pipeline automation                  ■   Securely connect to Lakebase using SQLAlchemy and Databricks OAuth
                                                                    ■   Add interactive filters and views on the relational table
                                                                    ■   Use Databricks Asset Bundles (DABs) and GitHub for version control,
                                                                        deployment and automation


                                                                Check out the GitHub repository for full source code and deployment
                                                                instructions.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                           43




S T E P- BY-S T E P G U I D E                                               The repository contains the following files for app deployment:
                                                                            ■   app.py — The main Streamlit application
To streamline development, we recommend setting up Cursor with Databricks   ■   config.yaml — Centralized configuration for database and table parameters
Connect for local testing and iterations.                                   ■   generate_campaign_data.ipynb — Notebook to generate campaign
                                                                                performance data
1. Set up Lakebase                                                          ■   requirements.txt — All Python dependencies, including Streamlit,
                                                                                SQLAlchemy and the Databricks SDK
If you don’t already have a Lakebase instance with synced tables, follow    ■   databricks.yml — Declarative deployment configuration for DABs
these steps:                                                                ■   README.md — Clear documentation for setup and usage
1. Create a Lakebase instance                                               ■   gitignore — Local and environment-specific file exclusion to keep the
    Follow steps 1–7 in the Lakebase documentation to create a Lakebase         repository clean
    instance named postgres-campaigns.
2. Clone the GitHub repository



SHELL

  git clone https://github.com/databricks-solutions/databricks-
  blogposts.git cd

  databricks-blogposts/2025-12-surfacing-lakebase-tables-in-
  databricks-apps
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                     44




3. Create a Unity Catalog table
                                                                                   2. Deploy app
    Open the generate_campaign_data.ipynb script from the cloned
    GitHub repository. Within the notebook widgets, provide the catalog,
                                                                                   We’ll now create a Streamlit app that connects to your Lakebase instance and
    schema and table name, and run the script to generate synthetic campaign
                                                                                   surfaces the data interactively.
    performance data.

4. Sync the Unity Catalog table                                                    1. Update configuration
    Use the Synced Tables feature to create a read-only table in Postgres that        In your cloned GitHub repository, edit config.yaml with your database
    automatically synchronizes data from a Unity Catalog table. Follow the steps      details. You can find the required information under the Connection details
    here to create a synced table. Sync the table to your Lakebase instance           tab of your database.
    from step 1.

    ■   Postgres database: campaign_db
                                                                                   NONE
    ■   Table name: campaign_metrics_synced
                                                                                    postgres:
    ■   Mode: Snapshot
                                                                                      host: "<your-managed-postgres-host>"
                                                                                      port: 5432
You should now have:
                                                                                      database: "<your-postgres-database>" # e.g."postgres-campaigns"
■   A Lakebase instance: postgres-campaigns                                           username_env: "DATABRICKS_CLIENT_ID"
■   A synced relational table: campaign_metrics_synced                                password_env: "DATABRICKS_OAUTH_TOKEN"


                                                                                    synced_table:
                                                                                      schema: "<your-schema>"
                                                                                      name: "<your-synced_table>" # e.g. "campaign_metrics_synced"
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                 45




2. Install dependencies                                                         4. Configure Postgres database
                                                                                     To connect to your own Postgres database, update the DB_CONFIG section
SHELL
                                                                                     in app.py:
  pip install -r requirements.txt
                                                                                NONE

                                                                                 # Database Configuration
3. Set Databricks environment variables
                                                                                 DB_CONFIG = {
    Go to Settings > Developer > Access tokens > Manage > Generate new
                                                                                     "host": "instance-<your-lakebase-id>.database.cloud.databricks.com", #
    token to get a new personal access token (PAT). Set environment variables
                                                                                 Your Postgres host
    as follows:
                                                                                     "port": 5432,
                                                                                     "database": "your_database_name",    # Database name from step 1.2
NONE                                                                                 "schema": "your_schema",        # UC Schema name
  export DATABRICKS_TOKEN=<YOUR_DATABRICKS_PAT>                                      "table": "your_table_name"      # Table name from step 1.2
                                                                                 }
  # General
  export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
  export DATABRICKS_TOKEN="your_personal_access_token"
  export DB_USER="<your.username@your-company.com>"
  export DB_PASSWORD="your_jwt_token_here"
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                            46




5. Update app name                                                       6. Deploy using DABs
    The databricks.yml file defines your app as a deployable resource.
    Populate your app name:                                              NONE

                                                                          databricks bundle init # Initialize DAB in your local directory
NONE
                                                                          databricks bundle validate # Validate bundle config
  resources:                                                              databricks bundle deploy
   apps:                                                                  apps start <your-app-name> # Start app compute
     <your_app_name>:                                                     databricks apps deploy <your-app-name> --source-code-path /
      name: <your_app_name>                                               Workspace/Users/<your-user>/.bundle/<your-app-name>/development/files
      source_code_path: .
                                                                          # For future changes only run
                                                                          databricks bundle deploy



                                                                         Your bundle source code will now be available in the Databricks workspace under
                                                                         the following:


                                                                         NONE

                                                                          /Workspace/Users/<your-username>/.bundle/lakebase-in-dbx-apps/
                                                                          development



                                                                         You can navigate to your app through Compute > Apps > <your-app> and
                                                                         open the provided link. Since your app doesn’t have privileges to access your
                                                                         database yet, you won’t be able to see your data at this point.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                 47




3. Configure app privileges for the database                                      SQL

                                                                                   CREATE EXTENSION IF NOT EXISTS databricks_auth;
1. Extract CLIENT_ID from the app
    ■   Navigate to Compute > Apps > <your-app>
                                                                                   SELECT
    ■   In your app, open the Environment tab and copy your DATABRICKS_
                                                                                   pg_databricks_create_role('<DATABRICKS_CLIENT_ID>','SERVICE_PRINCIPAL');
        CLIENT_ID value
2. Grant privileges to the app
                                                                                   GRANT ALL PRIVILEGES ON DATABASE "<your-postgres-database>" TO
    ■   Back in your Postgres instance (Compute > OLTP Database > >your-
                                                                                   "<DATABRICKS_CLIENT_ID>";
        instance>), click New Query
    ■   Validate that the selected compute in the editor shows Postgres compute
                                                                                   GRANT ALL PRIVILEGES ON SCHEMA <your-schema> TO "<DATABRICKS_
    ■   Switch the database from “postgres” to your Postgres database — e.g.,
                                                                                   CLIENT_ID>";
        postgres-campaigns
    ■   Execute the following code:
                                                                                   GRANT ALL PRIVILEGES ON TABLE <your-schema>.<your-table> TO
                                                                                   "<DATABRICKS_CLIENT_ID>";



                                                                                  You can navigate back to your app through Compute > Apps > <your-app>.
                                                                                  Open the provided link and you’ll see your relational table.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                              48




H I G H LI G H T S O N P O S TG R ES C O N N ECT I O N W I T H OAU T H         PYTHON

                                                                               from databricks import sdk
Using the Databricks SDK, the app uses OAuth tokens to securely authenticate
                                                                               from databricks.sdk.core import Config
against the managed Postgres instance.
                                                                               from sqlalchemy import create_engine, event
■   Requires no manual token management                                        import time
■   Refreshes tokens automatically every 15 minutes
■   Uses your Databricks workspace credentials                                 config = Config()
                                                                               workspace_client = sdk.WorkspaceClient()


                                                                               postgres_pool = create_engine(
                                                                                   f"postgresql+psycopg://{config.client_id}:@<your-db-host>:5432/<your-
                                                                               db-name>"
                                                                               )


                                                                               postgres_password = None
                                                                               last_refresh = time.time()


                                                                               @event.listens_for(postgres_pool, "do_connect")
                                                                               def provide_token(dialect, conn_rec, cargs, cparams):
                                                                                   global postgres_password, last_refresh
                                                                                   if postgres_password is None or time.time() - last_refresh > 900:
                                                                                     postgres_password = workspace_client.config.oauth_token().access_
                                                                               token
                                                                                     last_refresh = time.time()
                                                                                   cparams["password"] = postgres_password
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                        49




LES S O N S LE A R N E D

■   Databricks OAuth — Is seamless and production-ready for app
    authentication
■   Streamlit — Offers rapid prototyping for business-facing tools
■   Databricks Asset Bundles (DABs) — Simplify deployment and rollback —
    essential for CI/CD pipelines
■   Synced tables — Make transactional data immediately accessible in
    Databricks Apps



T RY I T YO U R S E LF

Would you like to try it on your own data?
■   Clone the GitHub repository
■   Customize DB_CONFIG in app.py
■   Customize your-app-name in databricks.yml
■   Deploy using databricks bundle deploy


Bring operational data to life in Databricks Apps with just a few lines of code —
and give your teams the insights they need, where they need them.


Create an intelligent application today. Sync your lakehouse data into Lakebase in
minutes, without building a pipeline or maintaining a server.
A H A N D S - O N G U I D E TO A P P S O N D ATA B R I C K S




06
                                                               How to Build AI Agents
                                                               With Conversational Memory
                                                               Using Lakebase
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                        51




How to Build AI Agents With                                                        U S I N G L A K E BAS E AS T H E S TAT E L AY E R FO R AG E N T S
Conversational Memory Using Lakebase
                                                                                   Stateful agents need a transactional database that can read and write
                                                                                   application state with minimal latency. Lakebase provides this foundation as
By Yatish Anand, Bo Cheng, Cathy Zdravevski, Evan Pandya and Susan Pierce
                                                                                   a fully managed, Postgres-compatible OLTP service integrated fully within the
                                                                                   Databricks Platform. Because it’s Postgres-compatible, you get the reliability
W H Y C O N V E R SAT I O N A L M E M O RY M AT T E R S
                                                                                   and ecosystem of a proven transactional database without standing up
                                                                                   separate infrastructure.
Many AI agents work well in single-turn interactions but struggle when applied
to real operational workflows. In cybersecurity, investigations rarely conclude
                                                                                   In this solution, Lakebase serves as LangGraph’s checkpoint store. Each step of
in a single step — analysts pivot from threat type to source IP, from IP to user
                                                                                   the agent’s execution is persisted under a thread identifier, and when that thread
and from user to device. These investigations often span multiple sessions and
                                                                                   is referenced again, the agent resumes with its full context — prior messages,
require continuity.
                                                                                   tool calls and intermediate state — intact. Low-latency reads mean the agent can
                                                                                   retrieve this context quickly, keeping conversations responsive.
To be effective in production, agents need state. They must remember what has
already happened and resume work with full context intact.
                                                                                   This approach enables real conversational memory without introducing a
                                                                                   separate database or managing additional operational complexity. Agent logic,
In this chapter, you’ll build a cybersecurity AI agent on the Databricks
                                                                                   tools, memory and deployment all live on the same platform where your data
Platform that persists conversational memory across interactions. The agent
                                                                                   and AI workloads already run.
stores execution state in Lakebase using LangGraph checkpointing, allowing
investigations to pause and resume seamlessly. You’ll deploy the agent using the
Databricks AI Agent Framework and expose it to end users as a Databricks app
built using Streamlit.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                     52




M E M O RY PAT T E R N S FO R A I AG E N T S

This chapter focuses on short-term memory implemented through thread-level
checkpointing. Each conversation is associated with a unique thread identifier,
and the agent’s state is saved incrementally as the workflow progresses.
This allows investigations to be resumed at any point without losing context.


Lakebase also supports longer-lived memory patterns that persist information
across threads and users. These patterns enable agents to accumulate
knowledge over time but introduce additional design considerations around
scope, retention and governance. For long-term memory that persists user
preferences or accumulated findings across sessions, see the long-term memory
section in the Databricks documentation.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                   53




A R C H I T ECT U R E OV E RV I E W

The solution consists of the following components:
■   A chat model served on Databricks that performs reasoning
■   Unity Catalog functions that expose governed security data as tools
■   LangGraph orchestration to manage control flow and tool invocation
■   Lakebase Provisioned as a transactional checkpointer for agent state
■   Databricks AI Agent Framework for packaging and deployment
■   A Streamlit-based Databricks app for end user interaction




                                                                           Together, these components form a production-ready, stateful agent
                                                                           architecture that runs entirely on the Databricks Platform.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                            54




I M P LE M E N TAT I O N G U I D E                                               PYTHON

                                                                                 databricks-connect
Prerequisites
                                                                                 databricks-agents
                                                                                 databricks-langchain
This guide assumes familiarity with building AI applications on the Databricks
                                                                                 unitycatalog-langchain[databricks]
Platform and focuses on agent architecture rather than environment
                                                                                 psycopg[binary,pool]
bootstrapping.
                                                                                 langgraph-checkpoint-postgres==2.0.21
                                                                                 langgraph==0.3.4
Before you begin, ensure you have:
                                                                                 langchain
■   A Databricks workspace with access to serverless compute                     mlflow
■   Permissions to create Unity Catalog functions                                uv
■   Permissions to create a Lakebase-provisioned instance
■   Access to Databricks Model Serving and Databricks Apps



You’ll use the following libraries in this demo. Run the setup on Databricks
serverless compute in a notebook, then follow along step by step. The GitHub
repository with the full working solution can be found here.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                              55




Step 1: Add governed security context                                            RETURN
with Unity Catalog functions                                                      SELECT
                                                                                   CONCAT(
Agents depend on trusted context to make decisions. In cybersecurity
                                                                                       'Threat ID: ',
workflows, this context often resides in structured event and identity tables.
                                                                                       threat_id,
Unity Catalog functions provide a secure mechanism to expose this data to
                                                                                       ', ',
agents as callable tools.
                                                                                       'Timestamp: ',
                                                                                       event_timestamp,
In this example, you create two SQL functions:
                                                                                       ', ',
■    get_cyber_threat_info retrieves the most recent threat event for a given          'Source IP: ',
     threat type                                                                       source_ip,
■    get_user_info retrieves user details associated with a source IP address          ', ',
                                                                                       'Protocol: ',
These functions are authored in Databricks SQL (DBSQL) and governed by Unity           protocol,
Catalog, ensuring consistent access control, auditing and lineage.                     ', ',
                                                                                       'Detection Tool: ',
                                                                                       detection_tool
SQL                                                                                )

    -- Create a SQL function that returns the cyber threat info given a threat   FROM

    type                                                                           catalog.schema.cyber_threat_detection

    CREATE OR REPLACE FUNCTION catalog.schema.get_cyber_threat_info(              WHERE

         threat_type STRING COMMENT 'input cyber threat type'                      threat_type = threat_type

     )                                                                            ORDER BY

     RETURNS STRING                                                                event_timestamp DESC

     COMMENT 'Returns latest threat_id, event_timestamp, source_ip, protocol,     LIMIT 1;

    detection_tool given a threat_type'
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                 56




  -- Create a SQL function that returns the user info given a source ip address     FROM
  CREATE OR REPLACE FUNCTION catalog.schema.get_user_info(                             catalog.schema.user_info
       source_ip STRING COMMENT 'input ip address'                                   WHERE
   )                                                                                   ip_address = source_ip
   RETURNS STRING                                                                    LIMIT 1;
   COMMENT 'Returns latest user_name, department, email, ip_address,
  location given a source_ip address'
   RETURN                                                                         Once you create the functions, you should see them in your designated catalog

       SELECT                                                                     and schema, under the Functions tab.

        CONCAT(
            'Username: ',
            user_name,
            ', ',
            'Department: ',
            department,
            ', ',
            'Email: ',
            email,
            ', ',
            'IP Address: ',
            ip_address,
            ', ',
            'Location: ',
            location
        )
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                       57




Step 2: Create a Lakebase instance for checkpointings

To persist agent state, create a Lakebase instance that serves as a LangGraph
checkpointer. Rather than managing an external Postgres database, Lakebase
provides a managed transactional service that integrates directly with Databricks
security and identity.


Each execution step of the agent is written to Lakebase. Because Lakebase is
optimized for low-latency transactional workloads, these writes add minimal
overhead to the agent’s response time. By associating checkpoints with a thread
identifier, the agent can reliably resume conversations across sessions without
sacrificing the responsiveness users expect.


This implementation uses the langgraph-checkpoint-postgres integration
so LangGraph can persist agent state directly into Lakebase using standard
Postgres semantics.


You can create the Lakebase instance using the Databricks SDK for Python or
manage it declaratively with Databricks Asset Bundles (DABs), depending on how
you standardize infrastructure.


In addition, by creating the database catalog, you can now query your
checkpoint history using DBSQL.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                            58




Step 3: Orchestrate with LangGraph and trace                                          Step 4: Deploy the agent with the Databricks AI Agent
with MLflow                                                                           Framework

                                                                                      Once validated, the agent is packaged and deployed using the Databricks AI
                                                                                      Agent Framework. This simplifies registration, versioning and serving while
                                                                                      preserving authentication passthrough to governed resources.


                                                                                      When logging the agent with MLflow, explicitly declare dependent resources,
                                                                                      including model serving endpoints, Unity Catalog functions and the Lakebase
                                                                                      instance. This ensures the deployment has clear visibility into the assets it relies
                                                                                      on. The following code shows only the relevant parts of the predict and predict_
                                                                                      stream functions, which demonstrate the databricks_langchain short-term
                                                                                      memory CheckpointSaver, which integrates with Lakebase. Feel free to check our
                                                                                      GitHub repository for the full model code.




Databricks integrates directly with the LangGraph orchestration framework.
If you’re following along, select the LangGraph option. LangGraph provides the
control plane for agent behavior — when to call the model, when to call tools
and how to persist state between turns. In this implementation, you bind Unity
Catalog tools to the chat model and use a Lakebase-backed checkpointer to
save and restore thread-level state.


Before deployment, validate behavior with MLflow Tracing. Tracing makes it easier
to audit inputs, outputs, tool calls and intermediate steps, which is essential for
debugging and for understanding agent behavior in production.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                            59




PYTHON
                                                                               with
  def predict(self, request: ResponsesAgentRequest) ->                         CheckpointSaver(instance_name=LAKEBASE_INSTANCE_NAME) as
  ResponsesAgentResponse:                                                      checkpointer:
       outputs = [                                                                    graph = self._create_graph(checkpointer)
            event.item
            for event in self.predict_stream(request)                                 for event in graph.stream(
            if event.type == "response.output_item.done"                                   {"messages": langchain_msgs},
       ]                                                                                   checkpoint_config,
       return ResponsesAgentResponse(                                                      stream_mode=["updates", "messages"],
            output=outputs, custom_outputs=request.custom_inputs                      ):
       )                                                                                   if event[0] == "updates":
                                                                                             for node_data in event[1].values():
     def predict_stream(                                                                       if len(node_data.get("messages", [])) > 0:
       self, request: ResponsesAgentRequest                                                         yield from output_to_responses_items_stream(
     ) -> Generator[ResponsesAgentStreamEvent, None, None]:                                             node_data["messages"]
       thread_id = self._get_or_create_thread_id(request)                                           )
       ci = dict(request.custom_inputs or {})                                              elif event[0] == "messages":
       ci["thread_id"] = thread_id                                                           try:
       request.custom_inputs = ci                                                              chunk = event[1][0]
                                                                                               if isinstance(chunk, AIMessageChunk) and chunk.content:
  # Convert incoming Responses messages to ChatCompletions format                                   yield ResponsesAgentStreamEvent(
       # LangChain will automatically convert from ChatCompletions to                                   **self.create_text_delta(
  LangChain format                                                                                           delta=chunk.content, item_id=chunk.id
       cc_msgs = self.prep_msgs_for_cc_llm([i.model_dump() for i in request.                            ),
  input])                                                                                           )
       langchain_msgs = cc_msgs                                                              except Exception as exc:
       checkpoint_config = {"configurable": {"thread_id": thread_id}}                          logger.error("Error streaming chunk: %s", exc)
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                         60




Subsequently, you must log and register your agent using the models from code
                                                                                for tool in tools:
approach in MLflow.
                                                                                    if isinstance(tool, VectorSearchRetrieverTool):
                                                                                      resources.extend(tool.resources)
PYTHON                                                                              elif isinstance(tool, UnityCatalogTool)
  # Determine Databricks resources to specify for automatic auth
  passthrough at deployment time                                                resources.append(DatabricksFunction(function_name=tool.uc_function_
  import mlflow                                                                 name))
  from databricks_langchain import VectorSearchRetrieverTool
  from mlflow.models.resources import (                                         # System policy: resources accessed with system credentials
      DatabricksFunction,                                                       system_policy = SystemAuthPolicy(resources=resources)
      DatabricksServingEndpoint,
      DatabricksLakebase,                                                       # User policy: API scopes for OBO access
      DatabricksVectorSearchIndex,                                              api_scopes = [
  ) # we are adding DatabricksLakebase resource type                                "sql.statement-execution",
  from mlflow.models.auth_policy import AuthPolicy, SystemAuthPolicy,               "mcp.genie",
  UserAuthPolicy                                                                    "mcp.external",
  from unitycatalog.ai.langchain.toolkit import UnityCatalogTool                    "catalog.connections",
  from agent import LLM_ENDPOINT_NAME, LAKEBASE_INSTANCE_NAME,                      "mcp.vectorsearch",
  tools                                                                             "vectorsearch.vector-search-indexes",
  from pkg_resources import get_distribution                                        "iam.current-user:read",
                                                                                    "sql.warehouses",
  # TODO: Manually include additional underlying resources if needed and            "dashboards.genie",
  update values for endpoint/lakebase                                               "serving.serving-endpoints",
  resources = [                                                                     "iam.access-control:read",
      DatabricksServingEndpoint(endpoint_name=LLM_ENDPOINT_NAME),                   "apps.apps",
      DatabricksLakebase(database_instance_name=LAKEBASE_INSTANCE_                  "mcp.functions",
  NAME),                                                                            "vectorsearch.vector-search-endpoints",
  ]                                                                             ]

A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                    61




                                                                                After the model is logged, you can use the catalog to view versions, artifacts and
  user_policy = UserAuthPolicy(api_scopes=api_scopes)
                                                                                even get an overview of lineage showing relevant Unity Catalog objects.

  input_example = {
      "input": [{"role": "user", "content": "What is an LLM agent?"}],
      "custom_inputs": {"thread_id": "example-thread-123"},
  }


  with mlflow.start_run():
      logged_agent_info = mlflow.pyfunc.log_model(
          name="agent",
          python_model="agent.py",
          input_example=input_example,
          pip_requirements=[
               f"databricks-langchain[memory]=={get_distribution('databricks-
  langchain[memory]').version}",
          ],
          resources=resources,
      )
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                                                                                         62




Finally, you can use a simple agents.deploy() function call to create the            After deployment, the agent can be tested using the AI Playground or Review
model serving endpoint and instantiate the Review App for SME evaluation.            App before being exposed to end users. The Review App is a built-in chat UI to
Here, you log any necessary environment variables that your agent needs for          vibe-check your AI app before integrating with your front-end Databricks app.
authentication, such as a service principal client id and client secret designated
for authentication to the Lakebase-provisioned instance.



PYTHON

  from databricks import agents


  agents.deploy(
      UC_MODEL_NAME,
      uc_registered_model_info.version,
      environment_vars={
           "DATABRICKS_HOST": "{{secrets/dbdemos/DATABRICKS_HOST}}",
           "DATABRICKS_CLIENT_ID": "{{secrets/dbdemos/DATABRICKS_CLIENT_
  ID}}",
           "DATABRICKS_CLIENT_SECRET": "{{secrets/dbdemos/DATABRICKS_
  CLIENT_SECRET}}",
      },
      tags={"endpointSource": "playground"},
  )
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                         63




Now you can integrate the model serving endpoint with a Databricks app — the
most secure way to build AI apps on the Databricks Platform — with out-of-the-
box support for Python frameworks like Streamlit, Gradio, Plotly Dash, Shiny and
Flask. For this cybersecurity analyst agent, we’re using Streamlit.


Databricks Apps offers two authentication modes: app authorization (using a
provided service principal) or user authorization (on-behalf-of-user, where the
app acts with the identity of the logged-in user). Either way, you use the MLflow
deployments client to interact with your agent’s model serving endpoint.


The key to conversational memory is the thread_id — a unique identifier that ties
a conversation’s checkpoints together in Lakebase. In your Streamlit app, users
can enter an existing thread_id in the sidebar to resume a previous conversation
exactly where they left off. In the next figure, the thread_id is 4, so if the user
closes the app and later returns with that same identifier, the agent picks up with
full context of the prior conversation.


If no thread_id is provided, the app generates a new one for the session, starting
a fresh conversation. This is a simple implementation to demonstrate how short-
term memory works. In production, your app would typically handle thread_id
persistence automatically, associating each user with their conversation threads
so they don’t have to track identifiers manually.
A H A N D S - O N G U I D E T O A P P S O N D ATA B R I C K S                                            64




C O N C LU S I O N                                                               R ES O U R C ES

Stateful memory is essential for production AI agents. In domains like           ■   Documentation
cybersecurity, investigations span multiple turns and sessions and agents must   ■   Example notebooks
retain context to be effective.
                                                                                 ■   GitHub repository

In this guide, you built a stateful cybersecurity agent on Databricks using
Lakebase as a transactional memory layer for LangGraph checkpointing.
Unity Catalog functions provide governed access to data, MLflow enables
tracing and lifecycle management and the Databricks AI Agent Framework
simplifies deployment. Together, these components deliver an end-to-end agent
architecture that runs entirely on the Databricks Platform.


This pattern applies broadly to any multistep workflow that requires
continuity. With Lakebase, you can add conversational memory to agents
without external databases, keeping state, governance and deployment unified
in a single platform.
Build Intelligent Apps
on the Databricks Platform
With Databricks Apps and Lakebase, the entire application
stack sits together, alongside the lakehouse. By combining the
two, you can build interactive tools that store and update state
in Lakebase, access governed data in the lakehouse and serve
everything through a secure, serverless UI — all without managing
separate infrastructure. This makes it easier to build and deploy
apps that combine transactional state, analytics and AI.


    Try Databricks free                     Watch a demo



Documentation

    Read Databricks Apps documentation                                   Read Lakebase documentation




About Databricks
Databricks is the data and AI company. More than 20,000 organizations worldwide —
including adidas, AT&T, Bayer, Block, Mastercard, Rivian, Unilever and over 60% of the
Fortune 500 — rely on Databricks to build and scale data and AI apps, analytics and agents.
Headquartered in San Francisco with 30+ offices around the globe, Databricks offers a unified
Data Intelligence Platform that includes Agent Bricks, Lakeflow, Lakehouse, Lakebase and Unity
Catalog. To learn more, follow Databricks on LinkedIn, X, YouTube and Instagram.




© Databricks 2026. All rights reserved. Apache, Apache Spark, Spark and the Spark logo are trademarks of the Apache Software Foundation. Privacy Policy | Terms of Use

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
