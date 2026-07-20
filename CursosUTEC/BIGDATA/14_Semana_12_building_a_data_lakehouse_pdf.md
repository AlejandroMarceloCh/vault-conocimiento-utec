---
curso: BIGDATA
titulo: 14 - Semana 12/building-a-data-lakehouse
slides: 19
fuente: 14 - Semana 12/building-a-data-lakehouse.pdf
---

                                                                  White paper
                                                               September 2021




Building a data
lakehouse on
Google Cloud
Platform
Rachel Levy, Steve Thill and Firat Tekiner




BigQuery as a data           Analyzing data in the   Making it seamless
lakehouse                    data lakehouse

Page 6                       Page 13                 Page 16
Executive summary
                                                               Operationalizing
For over a decade, the technology industry has searched
for optimal ways to store and analyze vast amounts of data.    and governing this
These storage solutions need to handle the volume,
latency, resilience, and varying data access requirements      architecture is
demanded by organizations. To tackle these issues,
companies have been making the best out of existing            challenging, costly,
technology stacks. This typically involves trying to either
make a data lake behave like an interactive data warehouse     and reduces agility.
or trying to make a data warehouse act like a data lake,
processing and storing vast amounts of semi-structured
                                                               As organizations
data. Both approaches have resulted in unhappy users,
high costs, and data duplication across the enterprise. The
Google Cloud data lakehouse pattern solves these
                                                               are moving to the
shortcomings.
                                                               cloud, they want to
Historically, organizations have implemented siloed and
separate architectures. Data warehouses store structured,      break these silos.
aggregate data (primarily used for BI and reporting),
whereas data lakes store large volumes of unstructured and
semi-structured data (primarily used for ML workloads).
This approach often results in complex ETL pipelines
because of extensive data movement, processing, and
duplication. Operationalizing and governing this
architecture is challenging, costly, and reduces agility. As
organizations are moving to the cloud, they want to break
these silos.

To address these issues, a new architecture choice has
emerged: the data lakehouse. The data lakehouse
combines the key benefits of data lakes and data
warehouses. This architecture offers a low-cost storage
format that is accessible by various processing engines like
Spark while also providing powerful management and
optimization features.




                                                                                    2
For example, our data center enables a Dataproc environment to
connect to either Google Cloud Storage or the BigQuery storage
subsystem and read/write data at storage speeds, thanks to our
network that achieves petabit bisectional bandwidth. This allows        With trust in the
Spark developers to leverage data inside BigQuery without the
need for data duplication and cumbersome ETL operations. The            data you have, you
speed of the internal Google network enables your organization
to bring the processing to the data and avoid data duplication,         spend more time
reducing data latency, processing time, data discrepancies, and
cost. In addition, Dataplex, our intelligent data fabric, enables you   deriving value out
to manage your distributed data assets while making data
securely accessible to all your analytics tools.
                                                                        of the data and less
Dataplex provides metadata-led data management with built-in
data quality and governance capabilities. With trust in the data,
                                                                        time wrestling with
you have, you spend more time deriving value out of data and
less time wrestling with infrastructure boundaries and
                                                                        infrastructure
inefficiencies.
                                                                        boundaries and
Additionally, with the integrated analytics experience provided by
Dataplex, you are enabled to rapidly create, secure, integrate,         inefficiencies.
and analyze your data at scale. Finally, you can build an analytics
strategy that augments existing architecture and meets your
financial governance goals.

The landscape of data continues to evolve and grow at an
exponential rate. It is important to have flexible patterns and
limitless scale to ensure data is used as an investment, rather
than a sunk cost.




                                                                                             3
Introduction
In the ever-evolving world of data architectures and                  underlying infrastructure and thus enable teams to
ecosystems, there is a growing suite of tools being                   focus on bringing value to the business. Data
offered to enable data management, governance,                        engineers should be able to focus on making the raw
scalability, and even machine learning. With promises                 data more useful to an organization. Data scientists
of digital transformation and evolution, organizations                should be able to focus on looking at the data, using
often find themselves with sophisticated solutions                    tools to exploit hidden information, and producing
that have a considerable amount of bolt-on features.                  predictive data models.
However, the ultimate goal should be to simplify the



                                                                  Data Catalog
                                                                  & Governance



                                               Data                                          Business
                                            Preparation                                    Intelligence




                       100+ SaaS & Google
                            Sources                                                                       AI Platform &
                                                                                                          Data Science




                                                          Azure      GCS             AWS
                                                                   Data Lake




                                                                  Real-Time
                                                             Streaming & Ingestion




Figure 1: Data ecosystem




                                                                                                                          4
Google Cloud has taken this approach by using our           In reality, these promises were not realized for many
planet-scale analytics platform to bring together two       organizations. This was mainly because they were not
foundational solutions. The core capabilities for           easily operationalized, productionized, or utilized. To
enterprise data operations, data lakes, and data            interact with data in the lake, an end user had to be
warehouses have been unified — simplifying the              fairly proficient in particular coding paradigms, which
management tasks while increasing the value. The            limited the set of people who could use the data. All
centerpiece of this architectural revolution is             of these in return increased the total cost of
BigQuery. As shown in Figure 1, BigQuery is at the          ownership. There were also significant data
center of our customers’ Data Ecosystem because it          governance challenges created by the data lakes .
is both tightly integrated with Google Cloud and open       They did not work well with the existing identity and
to partners’ technologies. BigQuery provides the            access management (IAM) and security models.
lakehouse architecture, which brings the best of the        Furthermore, they ended up creating data silos
lake and the warehouse without the overhead of both.        because data was not easily shared across the
This unlocks the value of data and ensures a unified        Hadoop environment.
governance approach with tools such as Dataplex and
Analytics Hub.                                              During the big data era, these two systems co-existed
                                                            and complemented each other as the two main
Data warehouses are systems that came about when            database management systems of enterprises,
business leaders were looking to gain analytical            residing side by side. Traditionally, structured and
insight from operational data stores. The legacy            processed data was stored in the data warehouse. On
systems that may have worked for the past 40 years          the other hand, data lakes provided the ability to land
have proven to be expensive and cannot often                raw data without having to create a schema. This
address the challenges around data freshness,               model created silos between teams. Essentially, data
scaling, and high costs. Also, data warehouses only fit     warehouse users were closer to the business and had
the needs of tabular data, limiting their usability for a   ideas about how to improve analysis, often without
rapidly growing variety of data types and structures.       the ability to explore the data to drive a deeper
Schema was often applied on-write and was driven by         understanding. Data lake users, conversely, were
a specific analytic use case. This also limited the         closer to the raw data and had the tools and
flexibility of future use of the data for things such as    capabilities to explore the data. However, they spend
machine learning and advanced analytics.                    so much time doing this, they were consequently
                                                            more focused on the data itself than on the business.
To solve some data warehouse limitations, new
technologies (such as Hadoop-powered Data Lakes)            The architecture of a data lakehouse reduces
were developed and ushered in the big data era. For         operational costs, simplifies transformation
example, data lakes were developed as low-cost              processes, and enhances governance. This model is
storage solutions that essentially amounted to              built on convergence of data lakes and warehouses,
distributed storage of files. They looked great on          as well as data teams across organizations. In
paper by promising low cost and the ability to scale.       essence, it implements warehouse-like data
                                                            structures and data management functions on
                                                            low-cost storage that is typical of data lakes.


                                                                                                           5
BigQuery as a
data lakehouse                                                                             Data
                                                                                         pipeline

In many ways, a data lakehouse becomes a way of
centralizing and unifying disparate data sources and
engineering efforts across an organization. This
means, like any type of data infrastructure, a data                                                 Data Scientists
lakehouse must include components to ingest, store,
                                                                 GCS      BigQuery
and analyze data. A data lakehouse, however,
compared to either a data lake or data warehouse,
attempts to centralize these components to provide a
more unified dataset for all users, regardless of skill
set. The ethos of the data lakehouse is about
                                                                                                    Data Analysts
believing that all users can and should be data users,
regardless of technical capabilities. By providing an                     BigQuery
underlying and centralized effort to make the data
accessible, different tools can sit on top of the
lakehouse that meets each user’s capabilities.

To make it possible for all users to have access to the                                             General User
same underlying data, the data lakehouse takes                 reports    BigQuery
advantage of BigQuery’s storage and the compute
power to use views rather than materialized tables.
This is important because a data lakehouse has the
same storage subsystem, enabling shared storage
behind the views to minimize unnecessary data                                                       Business Users
replication. This is all done in BigQuery, without the
                                                                  Workday reports,
standard storage premium often associated with                  SAP financial reports,
traditional data warehouses. The permanent location                     JDA

for raw, enriched, and business data then becomes
the lakehouse.




                                                          Figure 2: Accessing data for end users




                                                                                                        6
A modern data warehouse like BigQuery can handle         governed in it). In many organizations adopting data
massive data volumes and has cost parity with other      lakehouses, the centralized analytics or IT team
data storage mechanisms such as Cloud Storage. This      ingests the data from source systems and provides a
reduces operational costs, simplifies transformation     standardized set of views that various teams can then
processes, and enhances governance. Furthermore, a       leverage for their own use cases. An example of these
data warehouse is then used as the data fabric for all   views is in Figure 3.
the datasets (that are kept and




Figure 3: Data architecture




                                                                                                      7
In this example, IT teams can ingest data into the           by providing a nearly limitless and instantaneous
bronze layer and utilize views to cleanse the data           scalability due, in large part, to the separation of
through the staging/silver layer (see Figure 3), while       compute and storage.
the specific use of the data can then be made into
curated views in their own projects. A deep dive into        BigQuery's separation of storage and compute allows
each of the architectural components of a data               for BigQuery compute to be brought to other storage
lakehouse on Google Cloud is found in the next               mechanisms through federated queries and have
sections.                                                    other compute paradigms by using data stored in
                                                             native BigQuery format through the Storage API.
Traditionally, with data warehousing, compute and            BigQuery has a Storage API that allows the storage
storage were scarce resources that teams competed            (which is separated from the compute clusters) to be
for. When those resources were no longer available, it       treated like structured data in a lake. Rather than
often led to fragmentation of resources (data marts).        reading in parquet or Avro files, Dataproc, Google
These arbitrary resource constraints tied the ability to     Cloud’s managed Hadoop, can read the data directly
unlock the data’s value to the capacity of the               from BigQuery storage, run its computations, and
hardware, rather than the capacity of the imagination.       write it back to BigQuery. An example of this is seen in
Data lakehouses, specifically on Google Cloud,               Figure 4.
remove the artificial constraints to unlock data’s value




                       Cloud Dataflow             BigQuery         Cloud Dataproc              Vertex AI




       PROCESSING
       STORAGE




                                  Cloud Storage                             BigQuery Storage
                                      (files)                                   (tables)




Figure 4: Data processing and storage



                                                                                                              8
Separation of compute and storage is key to managing resources
in the cloud. It enables resource sharing across applications with
reduced overhead. Furthermore, it enables setting budgets at
various levels and stages. It is possible to define caps for
different workloads meeting SLAs. For example, flexible slots in
BigQuery simultaneously provide SLA guarantees and elasticity.             IT       Reporting    Analysis      Customer
Resource guarantees can be done at minute intervals, monthly
intervals, or yearly intervals at BigQuery level. On the other hand,
Ephemeral Dataproc clusters let you bring up complex Hadoop
(including Spark) clusters within a matter of seconds, running the
required workload and shutting it down. A combination of these
means you can manage overruns and handle unexpected hikes
without requiring considerable capital investment.

Another important aspect of reducing operational overhead is
using the capabilities of underlying infrastructure. Consider          Figure 5: Data warehouse and
Dataflow and BigQuery; while they have different underlying            data marts
infrastructure, Google manages the uptime and mechanics
behind the scenes of both services. For example, backups,
snapshots, and resiliency are available all out of the box. In turn,
this reduces resource and operational overheads. You can also
experience better observability by exploiting monitoring
dashboards with Cloud Monitoring to lead for operational
excellence.

This is how the lines that have traditionally been drawn between
data lakes and data warehouses can start to blur. External                 IT       Reporting    Analysis      Customer

storage of files in Google Cloud Storage (GCS) can be accessed
through BigQuery federated queries and Bigtable’s data. The
data lakehouse flips the paradigm of infrastructure procurement                 Owner   Editor   Viewer     Viewer

around and makes data access a permissioning problem and
data processing an OpEx/budgeting problem. In traditional IT
organizations, a data warehouse and surrounding data marts
would be additional hardware purchases for different lines of
business or use cases, as depicted in Figure 5.

Instead, creating a single-source-of-truth storage layer
accessible by a highly scalable serverless compute cluster
                                                                       Figure 6: Data access control
enables data access to be controlled by access control listed, as
granular as the organization requires. This is one of the key
principles in making a data lakehouse work for all users in an
enterprise (Figure 6).




                                                                                                                 9
Ingesting data
                                                         transactional systems that stream data in real time.
                                                         For example, when streaming data into a lakehouse
                                                         such as BigQuery, it is best to use an append-only

into the data                                            model. This means that historical data will always be in
                                                         the table, but the query can include a where clause
                                                         that ensures only the latest version of each record is

lakehouse                                                included in each view. Remember, storage is cheap
                                                         and organizations can afford to keep historical data
                                                         that can then be used for additional use cases.

Ingesting data into the lakehouse is the first part of
                                                         There are several managed services on Google Cloud
the data pipeline. There are several ways to ingest
                                                         that help ingest data into the lakehouse. Pub/Sub is a
data into BigQuery, but they generally fall into two
                                                         messaging service that runs on our global network
categories: batch data or streaming data. Depending
                                                         and enables asynchronous communication on the
on the source system and data requirements, data
                                                         order of 100s of milliseconds. The messages are
engineering teams may decide how to get the data
                                                         streamed from Pub/Sub to Dataflow for real-time
into the lakehouse.
                                                         analytics, while Dataproc is used for batched file
                                                         ingestion.
With a traditional data lake and data warehouse
dichotomy, the data files may be dropped into the lake
                                                         Once the data lands in BigQuery, it is queryable.
in a semi-structured state. Then a subset of that data
                                                         Following the layered approach that leverages views
would be transformed and structured to be stored in
                                                         over materialized tables, the most up-to-date data
the warehouse where analysts could use the data.
                                                         end up in every “gold layer” project (see Figure 3)
With the data lakehouse, however, there is no need to
                                                         utilizing the data lakehouse architecture. Instead of
store the data in those separate systems.
                                                         streaming all of this data into a lake and then
                                                         structuring it for the warehouse, you have the best of
Traditionally, applications are loaded in batches,
                                                         both in BigQuery.
whereby data can be batch loaded directly into a data
lake or data warehouse. Batch ingestion is powerful in
                                                         Views can only be used to present the most recent
a system like BigQuery because it uses massive
                                                         record of the data, but there are also performance
compute clusters that parallelize the ingestion.
                                                         benefits to this architecture. It enables the capability
                                                         to restore data from a point in time if there is a
This means that even terabytes of data                   corruption event. In addition, having date-based
can be ingested into BigQuery in less                    partitioning provides a performance enhancement
than a few minutes.                                      and a cost-saving as well. BigQuery charges for the
                                                         on-demand model based on how much data is read,
On the other hand, many newer use cases enabled by       not the time it takes the compute clusters to process
new technologies allow for data to be streamed           data. This means that you can use partitioning to only
directly into the data lakehouse and analyzed in real    query a certain timeframe, minimizing the data
time. Real-time data may originate from IoT devices or   scanned and thus the cost incurred.




                                                                                                       10
Storing data in
                                                           There may be instances where Spark or other ETL
                                                           processes are already codified, so changing them for
                                                           the sake of new technology might not make sense. If,

the data                                                   however, any transformations can be written in SQL,
                                                           BigQuery is likely a great place to send them. Utilizing
                                                           some BigQuery tuning best practices like partitioning

lakehouse                                                  and clustering is one way to keep costs and
                                                           performance optimal. It could also be a good
                                                           opportunity to materialize a table instead of storing
                                                           the logic as a view.
One of the key benefits of the data lakehouse is
minimizing the copies of data made and stored across
                                                           Furthermore, not all data is structured or tabular
an enterprise. Many enterprises suffer from different
                                                           enough to be stored in a database. This is increasingly
personas copying a subset of the data, making
                                                           common when the proliferation of unstructured data
transformations, and then using that data to make
                                                           sources (such as image files or text) is going to be
decisions. Without sharing this data across the
                                                           analyzed by an enterprise. Non-tabular or
enterprise, data will lack consistency and become less
                                                           unstructured data does not reside in BigQuery. To use
trustworthy. Furthermore, it becomes a data
                                                           those types of unstructured data, you might need a
governance nightmare; imagine a “right to be
                                                           machine learning platform. It is important, though, to
forgotten” GDPR request coming in and tracking all
                                                           ensure that this is part of the unified data lakehouse
copies of the data to remove that individual.
                                                           and that it can work with the following architecture.
                                                           This enables the metadata to be stored with the rest
To mitigate this, the data lakehouse stores the data in
                                                           of the metadata so that it can still be searchable as
a single-source-of-truth layer, making minimal copies
                                                           part of the underlying data platform.
of the data. Data is ingested into BigQuery and then
stored in the “raw” layer. Leveraging ELT over ETL,
                                                           This type of architecture is the complete data
BigQuery enables SQL-based transformations to be
                                                           lakehouse with unstructured data. If there is no
stored as logical views. While dumping raw data into
                                                           unstructured data, the top half of Figure 7 still works
data warehouse storage may have been expensive in
                                                           as previously discussed and uses the same principles
traditional data warehouses, there is no premium
                                                           to be an enterprise data lakehouse.
charge on BigQuery storage. Its cost is comparable to
blob storage in Cloud Storage. Without a cost
premium, there is no longer a required cost-based
justification for storage.

When performing ETL, the transformations take place
outside of BigQuery, potentially in a tool that does not
scale as well. It might end up transforming the data
line by line rather than parallelizing the queries.




                                                                                                         11
Figure 7: Data lakehouse design pattern




                                          12
             BigQuery storage                         Hadoop Spark             High-perf dataframes


                                                      Data ow                  Unified batch & stream ETL


                                                      ODBC JDBC                Third party tools


                                                      Custom connectors        Break down the storage wall




Figure 8: BigQuery Storage API




Analyzing data
in the data
lakehouse                                                    There are a few ways to use the data that is stored in
                                                             BigQuery, and the access method should be based on
                                                             an end user’s skill set. Meeting users at their level of
Once the data is ingested and stored in the data             data access including SQL, Python, or more
lakehouse, it must be analyzed and activated to drive        GUI-based methods mean that technological skills do
business value. If the data is not accessible to the         not limit their ability to use data for any job. Data
right resources, it is not even paying for the storage       scientists may be working outside traditional
costs it incurs. To activate the data, an analyst or data    SQL-based or BI types of tools. Because BigQuery
scientist must find insight that drives action.              has the storage API, tools such as Spark running on
Traditional reporting with data in a warehouse is to         Dataproc or AI notebooks can easily be integrated into
look back at historical data over the past week,             the workflow. The paradigm shift here is that the data
month, quarter, etc. While there is value in                 lakehouse architecture supports bringing the
understanding these trends in the business, it is also       compute to the data rather than moving the data
important to use analytics to look forward so that           around. In addition to the BigQuery SQL engine, the
real-time actions can be taken to correct issues             following diagram demonstrates other computation
before or once they arrive.                                  frameworks.




                                                                                                             13
The data lakehouse architecture makes it easy to                                When data is organized and democratized with a
share data with granular access controls across                                 business-driven approach, data can be leveraged as a
enterprises and with other/partner companies. For                               shareable and monetizable asset within an
example, role-based access methods across a suite                               organization or with partner organizations. To
of products make it possible to apply the same rules                            formalize this capability, Google offers a layer on top
to data in its transformation journey, ensuring data                            of BigQuery called Analytics Hub, that can create
governance and reduced operational cost. Therefore,                             private data exchanges. Exchange administrators
Spark code using the BigQuery Storage API as well as                            (a.k.a. data curators) give permission to publish and
users using spreadsheets rather than writing SQL                                subscribe data in the exchange to specific individuals
would still be leveraging the data lakehouse as their                           or groups both internally and externally to business
data source. This would allow increased collaboration                           partners or buyers, as depicted in Figure 9.
across the organization and enable the
democratization of data.




        Analytics Hub
        Private, Public, Commercial
        or Google hosted
        exchanges / listings                                Public       Commercial    Google
                                                Private




         Publisher project                                Subscriber project

                  BigQuery                                           BigQuery




              Source                  Shared                         Linked
              datasets                dataset                        datasets


         VPC-SC Perimeter                                 VPC-SC Perimeter




Figure 9: Analytics Hub




                                                                                                                            14
You can publish, discover and subscribe to shared                          exchange. You can drive innovation with access to
assets that are powered by the scalability of                              unique Google datasets, commercial/industry
BigQuery, including open source formats. Publishers                        datasets, public datasets, or curated data exchanges
can view aggregated usage metrics. Data providers                          from your organization or partner ecosystem. These
can reach enterprise BigQuery customers with data,                         capabilities can be driven when data operations are
insights, ML models, or visualizations, and leverage                       optimized to provide more valuable opportunities to
Cloud marketplace to monetize their apps, insights, or                     the organization, rather than spending time feeding
models. This is similar to how BigQuery public                             and caring for individual, and potentially redundant,
datasets are managed through a Google-managed                              systems.




                                                                    Retailers




                                       Suppliers                                               Logistics




                       Google                                                                               Private & Public




                             Web                                                                           NOAA       Credit
                Patents                                                                                               Bureau
                           Analytics
                                                              BigQuery
                                                                                                           World
                COVID-19    Trends                                                                         Bank       Media




                                               What items produce                 Where are the
                                                 highest repeat                 bottlenecks across
                                               purchase rates and                our supply chain?
                                                    margins?




Figure 10: Analytics Hub for secure & scalable sharing




                                                                                                                               15
Making it
                                                                              systems. And it complements this by automatically
                                                                              registering metadata as tables and filesets as
                                                                              metastores and Data Catalog. Furthermore, with our

seamless                                                                      integrated Cloud Data Loss Prevention API (DLP) and
                                                                              built-in data quality checks, the tagging of sensitive
                                                                              data is tightly integrated.
Dataplex provides a managed lakehouse service that
enables enterprises to rapidly build federated                                Dataplex also enables easier management of the
lakehouses. Curate, catalog, secure, integrate, and                           lakehouse with simpler security controls. Consistent
analyze any type of data at any scale with an                                 security policy and enforcement across Cloud Storage
integrated experience. Dataplex enables quickly built                         and BigQuery is enabled out of the box. Also enabled
lakes without needing to acquire and worry about                              are managed Data Lake Storage with fine-grained
different resources. It expands automatic data                                access control, ACID transactions on files, and a
discovery and schema inference across different                               BigQuery single pane of glass.



                                                                   Integrated workspaces

    Analytics
                 BigQuery                          Spark                   Data ow                 Ai Platform              Data Studio

   Experience
                                           Serverless                                                       BYOI




                                                                      Unified metastore



      Data
                      Data Intelligence
                                                            Fine-grained Security and Governance




   Management
                                          Data Lifecycle Management (Ingest, discover, prep, monitor, serve, archive)


                                                                  Logical data organization




                      Structured                        Semi-structured                   Unstructured                  Streaming Data


   Storage
                                             GCP                          Multi-Cloud                    On-premises




Figure 11: Dataplex


                                                                                                                                         16
With Dataplex, an integrated analytics workspace is                 notebook repository with links to associated data
becoming a reality. There is no infrastructure to                   while being able to save and share notebooks as if
manage and it provides one-click access to insights                 they were sharing another asset within the
for different personas. This means that data                        organization. Data analysts are able to use SQL
administrators are able to set up and manage                        Workspace for ad-hoc analysis without being
workspaces together with appropriate environment                    dependent on any data processing environment.
profiles, including compute parameters, libraries, etc.             Effectively, through a single pane of glass they will be
At the same time, they are able to control user access              able to use Presto, Hive, or BigQuery without needing
and manage costs through one seamless interface.                    to access various environments.
Data scientists have one-click access to notebooks.
Further, they can discover notebooks by using a



                            Data science

                            Analytics


                            Unified Metastore                                      Data Catalog


                                           Apply data validation and quality checks


                                  Automatic metadata extraction, profiling, and classification




                        Structured                     Semi-structured                      Unstructured




Figure 12: Datalake with Dataplex



Last, but not least, data access is made simple and                 serverless Spark for data science. All Cloud Storage
straightforward. An integrated experience across all                data is automatically made queryable through OSS
Google Cloud Data Analytics services provides virtual               tools and BigQuery, while enabling search and
lakehouse experiences. This is complemented with an                 discovery across the board by using Data Catalog.
integrated serverless notebook experience with




                                                                                                                  17
Conclusion
We are in a transformative era for data analytics in the            Google is a data company, with a world-class suite of
Cloud. As data volumes increase and companies                       analytics products. But our secret sauce lies in our
become more data-driven, they need to break down                    planet-scale, intelligent infrastructure upon which our
data silos and make data more accessible by                         products are built. Not only can you develop a
numerous users across the business. We have seen an                 lakehouse that meets your data users’ needs, but we
increase in the number of unified data platform                     have you covered in unique hardware and networking,
architecture options that meet the needs of different               integration that enables streaming at unlimited scale,
organization types. Google Cloud’s suite of data                    a serverless data warehouse with an unmatched
analytics products is well suited for any modern                    99.99% uptime SLA, and flexible and intelligent
analytics data platform pattern, including a data                   compute that takes the guesswork out of provisioning
lakehouse.                                                          servers.




   Compute: No need to plan for VMs
   or machines. Select a budget plan
   and Google does the rest.
                                                      Flexible &
   Infrastructure: Unique hardware and                intelligent
   networking integration enable streaming            compute
   at virtually unlimited scale.

   Storage: Colossus & Spanner for replication.
   No single point of failure. BQ 99.99% SLA is
   10x more reliable than competition.                Integrated
                                                      infrastructure



    BigQuery




                                                      Infinite scalability
                                                      Unmatched reliability

 4.3 minutes   43 minutes   43 minutes   43 minutes




      Figure 13: Our secret sauce


                                                                                                                  18
Building a data
lakehouse on
Google Cloud
Platform
September 2021




   Interested in getting started? Contact us to learn more.




                                                              19
