---
curso: BIGDATA
titulo: 15 - Semana 13/A comprehensive guide to Data and AI Governance
slides: 39
fuente: 15 - Semana 13/A comprehensive guide to Data and AI Governance.pdf
---

eBook
 eBook

The  Data Team’s
 A Comprehensive Guide
Guide  to the Databricks
 to Data and AI Governance
Lakehouse Platform
How to build a unified governance strategy
for your data and AI estate
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                                                                         2




Contents

                                                                       Executive Summary............................................................................................................................... 4

                                      CHAPTER 1                        Data Governance.. ...................... ............................................................................................................ 5
                                                                       		
                                                                        Key data governance challenges...................................................................................................... 5
                                                                                Data governance on the lakehouse.................................................................................................. 6
                                                                       			              What is a data lakehouse?..................................................................................................... 6
                                                                                        Data management.. .... ............................................................................................................ 7
                                                                       			                 Data ingestion. . ................................................................................................................... 8
                                                                       			                 Data persistence and organization..................................................................................... 9
                                                                       			                 Data integration.................................................................................................................. 9
                                                                       			                 Data federation. . ..... ........................................................................................................... 10
                                                                       		                  Metadata management.. ..................................................................................................... 11
                                                                       		                  Data discovery and classification...................................................................................... 13
                                                                       			              Data security.. ............ ........................................................................................................... 14
                                                                       			                 Access management ........................................................................................................ 14
                                                                       			                 Auditing entitlements and access..................................................................................... 17
                                                                       			              Data lineage............... ........................................................................................................... 18
                                                                       			              Data quality management and monitoring. . ......................................................................... 20
                                                                                        Data intelligence........ .......................................................................................................... 22
                                                                       			              Data sharing and collaboration............................................................................................ 23
                                                                       			                 Privacy-safe data clean rooms......................................................................................... 24
                                                                       			                 Data marketplaces. . .......................................................................................................... 25
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                                                                            3




                                      CHAPTER 2                        AI Governance...................................................................................................................................... 26
                                                                                AI governance on the lakehouse. . ................................................................................................... 27
                                                                       			               Compliance and ethics........................................................................................................ 27
                                                                       			               Machine learning reproducibility.. ........................................................................................ 28
                                                                       			               Explainability and transparency. . .......................................................................................... 31
                                                                       			               Model monitoring....... .......................................................................................................... 32
                                                                                         Model serving.. ..................................................................................................................... 34
                                                                                         AI security. . ................ .......................................................................................................... 34
                                                                       			               Cataloging and documentation. . .......................................................................................... 35
                                      CHAPTER 3                        Platform Security and Compliance..................................................................................................... 36
                                                                                Platform security.................. .......................................................................................................... 36
                                                                                Data compliance.................. .......................................................................................................... 37


                                                                       About the Authors.. .................... .......................................................................................................... 38
                                                                       About Databricks....................... .......................................................................................................... 39
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                   4




Executive Summary
            The dynamic interplay of data, analytics and artificial                        AI governance is accentuated even further. These advanced technologies
            intelligence (AI) is driving a wave of transformative innovations              empower organizations to create content, simulate scenarios and enhance
                                                                                           decision-making. However, they also amplify concerns regarding data privacy,
            across diverse sectors, reshaping revenue streams and
                                                                                           bias mitigation and ethical considerations. As AI becomes increasingly
            redefining corporate management paradigms. McKinsey
                                                                                           ingrained in core operations, the need for meticulous governance to ensure
            & Company’s projections underline the enormity of this                         fairness, accountability and security becomes paramount. McKinsey’s Global
            potential, estimating that by 2030, analytics and AI could                     Survey on AI emphasizes that organizations achieving the highest AI returns
            introduce more than $15 trillion in fresh business value.                      have comprehensive AI governance frameworks that cover every stage of the
            Furthermore, McKinsey’s recent State of AI report reveals that,                model development process. This sentiment is echoed by Forrester in their
                                                                                           2023 AI Predictions, stating that one in four tech executives will be reporting
            due to advancements in generative AI, 40% of organizations
                                                                                           to their board on AI governance. AI has now become an essential aspect of
            are planning to increase their overall investment in AI. This
                                                                                           enterprises and consequently, AI governance is joining cybersecurity and
            trend is driving a global upsurge in organizational investments                compliance as a topic of discussion at the board level.
            aimed at cultivating data-driven cultures and establishing
                                                                                           Data and AI governance serve as the intricate yet pivotal foundations of digital
            competitive advantages.
                                                                                           transformation endeavors. Data teams grapple with an array of challenges,
            Despite these investments, the challenge of deriving significant value from    including managing diverse data sources, dismantling silos, upholding data
            data and AI initiatives persists. Often, the heart of this challenge lies in   and ML model quality, facilitating trusted data discovery, ensuring secure data
            the absence of a comprehensive and actionable data and AI governance           access and navigating regulatory landscapes.
            strategy that encompasses the entire range of data applications, spanning      A forward-looking data governance strategy emerges as the guiding compass,
            from business intelligence to machine learning (ML). Gartner’s insights        addressing these complexities and empowering organizations to fully unlock
            provide additional depth, predicting that until 2025, a staggering 80%         the potential of their data investments.
            of organizations striving for digital business expansion will encounter
                                                                                           This eBook explores the methodologies that drive successful data and AI
            obstacles due to outdated approaches to data and analytics governance.
                                                                                           governance strategies. Additionally, it uncovers the role of the Databricks Data
            In today’s landscape, characterized by a renaissance in generative AI          Intelligence Platform as a catalyst for streamlining these transformative efforts.
            and large language models (LLMs), the importance of robust data and            As organizations navigate an era characterized by AI-centric data strategies,
                                                                                           the convergence of innovation and governance becomes the foundation for
                                                                                           sustainable growth and responsible technological advancement.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                         5




Chapter 1
Data Governance
Data is one of the most valuable assets for many organizations, but data           amounts of unstructured data in cloud storage platforms like AWS S3, Azure
governance is the key to unlocking that value.                                     ADLS and Google Cloud Storage (GCS). In fact, IDC predicts that by 2025,
                                                                                   approximately 80% of data in any organization will be unstructured. A subset
Data governance is a framework of principles, practices and tooling that helps     of this unstructured data is transformed into structured tables within data
manage the complete lifecycle of your data and aligns data-related requirements    warehouses for business intelligence purposes. Unfortunately, this data movement
to the business strategy. A pragmatic data governance strategy gives data teams    creates silos, with data scattered between two systems. Additionally, modern
superior data management, visibility and auditing of data access patterns across   data assets like dashboards, machine learning models and notebooks contribute
their organization. Implementing an effective data governance solution helps       to this fragmentation. The absence of a unified view hampers data and AI asset
companies protect their data from unauthorized access and ensures that rules       discovery, access and effective analysis. This leads to delays in decision-making
are in place to comply with regulatory requirements. Many organizations have       and inhibits innovation. Managing these silos requires extra resources and
leveraged their strong stance on data governance as a competitive differentiator   investments in data integration technologies, data engineering and governance
to earn and maintain customer trust, ensure sound data and privacy practices       processes, resulting in higher operational costs.
and protect their data assets.
                                                                                   Complex access management: Enterprises utilize various tools to secure access
Key data governance challenges                                                     to diverse data and AI assets, leading to complex, inconsistent and error-prone
                                                                                   access management. Different permission structures are applied to data lakes
Crafting an effective data governance strategy has become a complex
                                                                                   and data warehouses, resulting in inconsistent controls. Furthermore, the tools
undertaking due to how organizations collect and analyze data. Many
                                                                                   supporting these platforms have fundamentally different structures, hindering
organizations grapple with the following issues:
                                                                                   collaboration between the teams responsible for them. This inconsistency affects
                                                                                   permissions management, audits, data discovery and sharing. Handling modern
Fragmented data landscape: The presence of data silos across various sources,
                                                                                   data assets like dashboards, machine learning models and notebooks, each with
such as data lakes, warehouses and databases, poses significant challenges
                                                                                   their own permission models, further complicates the issue. When these assets
for governance teams. These silos hinder the creation of a cohesive view of
                                                                                   exist across multiple clouds, the complexity grows due to varying cloud-specific
data, resulting in inefficient data discovery. Most organizations store massive
                                                                                   access management frameworks.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                                        6




                            The challenges of data governance                                                      Data governance on the lakehouse
         Business
       intelligence
                             SQL
                           analytics
                                                    Incomplete
                                                    support for
                                                     use cases
                                                                                Data science
                                                                                  and ML
                                                                                                          Data
                                                                                                       streaming
                                                                                                                   What is a data lakehouse?
                                                                                                                   In a 2020 whitepaper, Lakehouse: A New Generation of Open Platforms that Unify
          Governance and security                  Incompatible
                                                                                  Governance and security
                                                                                                                   Data Warehousing and Advanced Analytics, Databricks founders set the vision
                                                    security and
                Table ACLs                      governance models                     Files and blobs              for a data lakehouse architecture that combines the capabilities of both data
                                                                                                                   warehouses and data lakes to achieve the performance of a data warehouse with
                                            Copy subsets of data
                                                                                                                   the economies and scale of a data lake. This unified approach simplifies your
                                                 Disjointed                                                        modern data stack by eliminating the data silos that traditionally separate and
          Data warehouse                       and duplicative                         Data lake                   complicate data engineering, analytics, BI, data science and machine learning.
           Structured tables                     data silos                         Unstructured files:
                                                                                 logs, text, images, video




 Inadequate monitoring and visibility: The lack of comprehensive monitoring
 and visibility into the lifecycle of data and AI assets between systems
 hampers effective audits, impact analyses and error diagnosis within data                                                    All ML, SQL, BI
                                                                                                                         and streaming use cases
 and AI pipelines. This inability to track the origin, evolution, transformations,
 movements and usage of assets undermines data quality assurance.

 Limited cross-platform sharing and collaboration: The absence of a
 standardized sharing solution inhibits secure cross-cloud and cross-platform
 sharing and collaboration of data and AI assets, including machine learning
 models, notebooks and dashboards. This situation forces enterprises to
 replicate data across multiple platforms, clouds and regions to facilitate
 collaboration, resulting in redundancy.

 Organizations need a unified approach to simplify data, analytics and                                             The Databricks Data Intelligence Platform unifies your data warehousing and AI
 AI governance. Gartner predicts that by 2026, 20% of large enterprises                                            use cases on a single platform. It combines the capabilities of data lakes
 will adopt a single data and analytics governance platform to streamline                                          and data warehouses to deliver reliability and performance without sacrificing
 and automate governance efforts. Let’s explore how the Databricks Data                                            open standards and support for both structured and unstructured data. And to
 Intelligence Platform addresses these challenges.                                                                 simplify data governance, the Databricks Data Intelligence Platform offers
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                         7




Unity Catalog, an open and unified governance solution for data, analytics and   Data management
AI on your lakehouse. By minimizing the copies of your data and moving to a
single data processing layer where all your data governance controls can run     Data management lays the foundation for how you execute your data governance
together, you improve your chances of staying in compliance and detecting a      strategy. The practice of data management involves the collection, integration,
data breach.                                                                     organization and persistence of trusted datasets to help organizations maximize
                                                                                 value. More than ever, an organization’s value is based on how well it can derive
In this chapter, we’ll discuss how you can leverage the Databricks Data          value from the data under its management. Data management also involves
Intelligence Platform to manage and govern the end-to-end data lifecycle.        helping organizations understand their data usage frequency and provides tools
                                                                                 for data lifecycle management.

                                                                                 Data management can be performed on any system that persists data. In the
                                                                                 analytics realm, this has historically been done on a data warehouse. Data
                                                                                 warehouses consist of tabular data and therefore have managed datasets via
                                                                                 constructs such as tables and views, which consist of rows and columns. Data
                                                                                 lakes are capable of persisting any type of structured or unstructured data for
                                                                                 data science or machine learning use cases. Data lakes are capable of storing file
                                                                                 formats like Apache Parquet, images or video, or raw text files for unstructured
                                                                                 data. The variety of such datasets requires that all data be managed at the file
                                                                                 level.

                                                                                 With a data lakehouse, organizations can persist their data once and use it for
                                                                                 all analytics use cases. This concept alone helps reduce data duplication and
                                                                                 minimize the scope of all data that an organization needs to manage.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                  8




Data ingestion
Before data can be persisted for future use, it must first be collected. Data can be      Another common data source, especially for data streaming, is a distributed
collected from anywhere, but is primarily collected from the following sources:           message queue such as Apache Kafka. This connection allows for low-latency
                                                                                          processing of messages in sequential order. In addition to open source queues,
   • Cloud storage                                                                        each of the major cloud providers has its own native message queue service.
   • Message queues                                                                       All of these can be leveraged in Databricks as just another Apache Spark™
                                                                                          Structured Streaming data source.
   • Relational databases
                                                                                          One of the most popular data sources to collect data from is a relational database
   • SaaS APIs
                                                                                          management system (RDBMS). Even though an RDBMS can perform its own data
Increasingly, data is collected from files written to object storage services that are    management, data is typically exported from these databases so that analytics
native to public cloud providers. This data could include anything from a handful         can be performed without impacting the online uses of the databases. This data
to millions of files written per day. The data can include any type of file, including:   can be collected either through static reads via the Apache Spark JDBC data
                                                                                          source or by applying a listener to the transaction log of the RDBMS. Databricks
   • Unstructured (PDF, text, audio, video)                                               partners with a number of vendors within Partner Connect to integrate directly
   • Semi-structured (JSON)
                                                                                          with the transaction log of these RDBMS systems so that every change to the
                                                                                          data can be captured.
   • Structured (Parquet, Avro)
                                                                                          The rise of software as a service (SaaS) means that more and more data is being
Databricks provides Auto Loader functionality to automatically detect new                 created and mastered within cloud-based services rather than on-premises
files on cloud storage, merge any schema changes and validate data against the            databases. These disparate services need to have their data exported and
expected schema. Auto Loader provides this functionality across all of the major          combined to produce value. Typically, this is done by making a series of API calls
public cloud providers.                                                                   to the SaaS provider endpoints. There are a number of vendors who have created
                                                                                          hundreds of connectors to easily collect such data using managed services
                                                                                          created specifically for the task. They can also be found in Partner Connect.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                9




Data persistence and organization                                                     Data integration

After data has been collected, it needs to be persisted somewhere so that it          Data typically needs to be integrated from disparate sources in order to maximize
can be managed and governed. With the rise of the public cloud, that place is         value. This can be done either in batch or streaming mode to make insights
increasingly cloud storage services such as AWS S3, Azure ADLS and GCP GCS.           available as quickly as possible. Integrating data typically requires some kind
Each of these services has its unique characteristics which may or may not            of orchestration so that an end-to-end process can be architected to collect,
provide atomicity and consistency at the file level. Because of this variance,        ingest, combine, transform and deliver the product of all these steps. This is why
data processing against these storage layers has historically been fraught with       Databricks provides Workflows as a fully managed solution to orchestrate all of
data quality issues. To overcome this challenge, Delta Lake was developed as          the tasks necessary to integrate data.
an open format storage layer to deliver reliability, security and performance
on a data lake for both streaming and batch operations.                               An orchestration engine generally understands the dependency graph of
                                                                                      operations and whether these tasks successfully complete or not. However,
Delta Lake provides ACID transactions for structured tables, allowing distributed     a general-purpose orchestration engine doesn’t have knowledge of the data
write operations while maintaining a consistent view of the data for reads. This is   being processed and can’t make adjustments accordingly. Delta Live Tables is
the foundation for what makes a data lakehouse. Delta Lake is primitive for data      the first extract, transform and load (ETL) framework that uses a simple declarative
integrity, but also serves as an enabler for performance gains when querying the      approach to building reliable data pipelines and automatically managing your
data. The statistics of the underlying files are centralized so that they may be      infrastructure at scale. Because Delta Live Tables is aware of the amount of data
skipped from reads when performing queries. Every transaction against Delta           it’s about to process, it can automatically trigger infrastructure to scale up or
Lake is persisted alongside the data so that a change data feed can be queried        down so that service level objectives are met for data pipelines, regardless of
for easy change data capture against the tables themselves. Finally, because the      whether it’s done in batch or streaming mode.
transactions are retained, the table can be queried because it was represented
at a point in the past using time travel.                                             One type of data integration that can uniquely be performed in a data lakehouse
                                                                                      is entity resolution (ER). ER is all about understanding how data represents
                                                                                      real-world “things” — or “entities.” Common examples are a person, a product,
                                                                                      a household, a vendor or a location. ER is typically used in the practice of master
                                                                                      data management (MDM) when conforming dimensions in a data mart. A simple
                                                                                      example is recognizing that a record pertaining to “Bill Wallace” is in fact the same
                                                                                      person being referenced as “William Wallace” from a different system. Linking
                                                                                      these records requires applying sophisticated algorithms at scale against a graph
                                                                                      of data.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                               10




Even at medium scale — e.g., 1 million records — care must be taken with               Additionally, enterprises manage various governance tools to oversee and
processing techniques. ER is all about comparing records to each other, and it’s       secure their scattered data across platforms and data sources. This results in
fundamentally an O(n2) problem. For example, 1 million records could require on        governance that is inconsistent and fragmented across their data infrastructure.
the order of 1 trillion comparisons. The Databricks Data Intelligence Platform is an   Such fragmented governance and lax adherence to compliance standards lead to
excellent choice because it inherently uses distributed processing and still allows    duplicated efforts and heighten the risk of being unable to monitor and safeguard
for the use of powerful packaged OSS — like Zingg and Splink. At this medium           against unauthorized access or data leaks.
scale, you also need to look into prefiltering techniques like binning, blocking
and preclustering. At any scale, the Databricks Data Intelligence Platform can         Databricks Data Intelligence Platform offers Lakehouse Federation, empowering
                                                                                       you to build an open, efficient and secure data mesh architecture. With
provide the tools needed to be successful with the integration of ER.
                                                                                       Lakehouse Federation, you can access a uniform data management, discovery
                                                                                       and governance experience for all your data across various platforms, including
Data federation                                                                        MySQL, PostgreSQL, Amazon Redshift, Snowflake, Azure SQL Database,
Data is often spread out and compartmentalized among numerous                          Azure Synapse, Google BigQuery, Oracle and more, all within the Databricks
heterogeneous data stores. To fully harness the potential of their data,               environment without the need for traditional ETL. This enables you to establish
organizations require a centralized access point to query data from diverse data       a unified data access permission model to set and enforce data access rules,
                                                                                       ensuring the protection of data across all sources. Users can implement rules like
sources. In the conventional approach, data teams typically transfer their data
                                                                                       security at the row and column levels, policies based on tags, centralized auditing
from external sources or systems to a chosen platform (such as a lakehouse),
                                                                                       consistently across platforms, and track data usage and meet compliance
a process involving ETL procedures. As an alternative, they can depend on
                                                                                       requirements with integrated data lineage and auditabilty features.
query federation/data virtualization vendors to create a unified virtual layer of
all their data. Essentially, data virtualization establishes an analytical database
of enterprise data without necessitating ETL procedures. This eliminates the
necessity for engineers to duplicate, move or modify the data, empowering data
scientists to engage with the data at its source. However, this also introduces
additional intricacies and expenses. The integration of data brings about
dependencies on data engineering and creates numerous bottlenecks.




                                                                                                                                         Lakehouse Federation in Unity Catalog
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                         11




Metadata management
You can’t govern data if you don’t know that it exists. Metadata is just
                                                                                                                       Databricks Unity Catalog
data about data. It’s data that describes your data and provides semantic value
to an otherwise unidentifiable sea of information.
                                                                                                                             Access
                                                                                                   Discovery                                         Lineage
                                                                                                                             Controls
An enterprise’s centralized metadata layer is both a representation of
that organization’s information architecture (how the data is organized for
consumption and storage) as well as a semantic layer that describes what                          Data Sharing               Auditing               Monitoring
that data is and what it isn’t.


A good data governance program must be tied with a centralized metadata layer
                                                                                         Tables                              Models                      Dashboards
that provides a macro view across your enterprise of the data assets available
                                                                                                               Files                    Notebooks
and in use. This is usually organized across segregation points such
as data domains, business units, applications or software development
lifecycles (SDLC). This centralized metadata layer also needs visibility to
a common federated view of identity in your organization so you can ensure
                                                                                    A centralized metadata layer ensures that your centralized governance teams
that the right users and the right groups have access to the right data.
                                                                                    have the ability to dictate access controls and retrieve audit information from
                                                                                    a single place, greatly reducing organizational risk due to improperly applied
Databricks Unity Catalog offers a centralized metadata layer, called a metastore,
                                                                                    access controls. Because Unity Catalog metastores are aligned to cloud
that provides the ability to catalog and share data assets across your lakehouse
                                                                                    provider regions, they implicitly enforce data access along regional boundaries
and across your enterprise’s regions and clouds. These data assets could be
                                                                                    and ensure that your users aren’t accessing data from other regions unless you
your files, tables, dashboards, ML models, etc.
                                                                                    explicitly allow it to happen. This ensures and helps you meet your complex data
                                                                                    residency requirements.


                                                                                    Unity Catalog allows you to define metadata across logical hierarchies
                                                                                    called catalogs, which can be thought of as data domains and can be tied to
                                                                                    segregation points in your information architecture. Using access controls on
                                                                                    catalogs and within their hierarchies, you can assign business groups to see
                                                                                    the relevant parts of your information architecture.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                 12




                                                                                                Use across SDLC environment scopes
The advantage of having all of your metadata in a
single place is that searching for data becomes a                                                Dev         Schema/database   Tables/Views

lot simpler. Using the Unity Catalog Search features,
you can search across tables and columns to                                                    Staging       Schema/database   Tables/Views
find the exact data artifacts that you’re looking
for. This helps achieve compliance with “right to                                                Prod        Schema/database   Tables/Views
be forgotten” regulations, which require that you
understand exactly what data lives in what datasets                                             Use across business units
in order to search those datasets so that you can
                                                                                               bu_1_dev      Schema/database   Tables/Views
remove a specific customer’s information.
                                                                                  Unity
                                                                                 Catalog     bu_1_staging    Schema/database   Tables/Views

                                                                                Metastore
                                                                                              bu_1_prod      Schema/database   Tables/Views



                                                                                                Use across team sandbox

                                                                                            team_x_sandbox   Schema/database   Tables/Views



                                                                                            team_y_sandbox   Schema/database   Tables/Views



                                                                                            team_z_sandbox   Schema/database   Tables/Views
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                13




Data discovery and classification
As organizations collect massive amounts of data from various sources and in            This built-in search capability automatically leverages the governance model put
multiple formats, making the data easily discoverable for analytics, AI or ML use       in place by Unity Catalog. Users will only see search results for data such as the
cases becomes critical to accelerate data democratization and unlock the true           files, tables and other assets they can access, which serves as a productivity
value of the data. Per IDC, a typical data team spends around 80% of their time         boost for the user and a critical control for data administrators who want to
on data discovery, preparation and protection, while only 20% of their time is          ensure that sensitive data is protected. This can help prevent duplication of data
spent on actual analytics. Additionally, the influx of data isn’t limited to files or   across an organization. Duplicative datasets are problematic because it costs
tables. There are also modern data assets such as dashboards, machine learning          money to persist them, and because of the potential for them to be governed at
models, queries, libraries and notebooks. Therefore, data discovery becomes             different security levels.
a key pillar of a robust data governance strategy, enabling data teams to easily
find data assets across their organization, collaborate on different projects and
innovate quickly and efficiently.


Whenever a new data project is undertaken, the first instinct is to “see what
data is available.” Metadata must be captured, indexed and made searchable
to accomplish this, and that is exactly what Unity Catalog does. Each asset
cataloged within Unity Catalog undergoes automatic indexing and meticulous
classification through machine learning algorithms, enhancing its discoverability.
Users are further empowered to affix tags to any registered asset, amplifying the
efficiency of their searches across an array of metadata fields, encompassing
table names, column names, comments and distinctive tags. This comprehensive
approach ensures swift and precise retrieval of the requisite data, facilitating
seamless and targeted analysis.


This unified search experience in the Databricks Data Intelligence Platform
enables users to search not just files and tables, but other assets such as
notebooks, libraries, queries, dashboards, etc., resulting in better collaboration
among data teams and faster innovation.
                                                                                                                                                  Built-in search and discovery
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                                 14




Data security                                                                   Access management
                                                                                                                                         When you think about implementing RBAC
A good data security governance program helps                                   A good data security governance program
                                                                                                                                         on a data platform, you’re mixing your operational
organizations:                                                                  provides methods to control access to data.
                                                                                                                                         model with business groups to make sure that
                                                                                Access controls are the mechanisms that
   • Achieve regulatory and/or organizational                                                                                            individuals have the right level of access to data
     compliance over the use of data                                            describe which groups or individuals can access
                                                                                                                                         resources at the right point in your process of
                                                                                what data. These are statements of policy, and
   • Provide methods to control access to data                                                                                           sourcing, building and analyzing those data insights.
                                                                                they can be extremely granular and specific, right
   • Provide facilities to determine who has access                             down to definitions of every record of data or
     to data                                                                                                                             For example, consider the different types of groups
                                                                                file that every individual has access to. Or they
                                                                                                                                         across a typical software development lifecycle.
   • Provide facilities to understand who has                                   can be very expressive and broad, e.g., all finance
     accessed data                                                              users can see all financial data.


                                                                                Any statement of policy on data generally                                RBAC across software
In this section, we’ll cover some of the drivers for                            looks like this: <Principal> can/can’t perform                           development lifecycle
good data security governance, what organizational                              <Action> on <Resource>                                                              Code
models for governance look like, and how you can
align well-defined processes and technology
offerings to create an effective data security                                  Role/resource-based access control                                     Engineers
                                                                                                                                                       Scientists                  Analysts
governance model for your enterprise’s data.                                    When you apply policy across roles or groups,
                                                                                                                                                 Dev
                                                                                                                                       Data
We’ll specifically examine security within lakehouse                            you’re implementing what is known as role-based                                                     Prod


architectures.                                                                  access control (RBAC). We can also think of this as                                 Staging
                                                                                resource-based access control, as you’re applying
                                                                                                                                                                      Engineers
                                                                                differential access controls based on resources as
                                                                                                                                                                      QA
                                                                                well. The difference is more of an implementation
                                                                                detail, i.e., where the access control record lives,
                                                                                                                                                Source                             Source
                                                                                whether on the resource that you are protecting or
                                                                                on the principal. Functionally, for this discussion,
                                                                                they’re the same.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                    15




In the simplistic case above, you have groups of engineers, scientists and quality           Some data platforms and data lakes offer some form of RBAC across
assurance engineers that need access to enough source data to develop jobs                   coarse-grained objects like tables or files, but not across both. To offer RBAC
or insights, and analysts who need to access production data to be able to                   across file systems, you need the common metadata layer we discussed before.
make business decisions. Assume, for a simple example, that all of your data is
contained within a single catalog across environment scopes. Using groups, you               Remember from earlier that data is more than just registered tables in your
can achieve differential access control ensuring that the right teams have access            catalog. Data lives in files, in directories on your data lake and as objects that you
to the right data at the right time in the process.                                          need to manage in your data platform.

Alternatively, consider RBAC across medallion architecture. This can be a
                                                                                             The following is an example of a cloud storage container layout:
parallel for any multi-hop architecture; for example, whether you’re working with
production data throughout the pipeline like medallion architecture, or with
subsets of anonymized or de-identified data throughout the pipeline in SDLC
multi-hop architecture.                                                                         Bucket root
                                                                                                                                                 user1/


                                                                                                                             users/


                                       RBAC across                                                                                              user2/

                                                                                                           /
                                    medallion architecture                                                                                                          table1/
                                                                                                                                                tables/
                      Service                                                                                                shared/
                                                                                                                                                                    table1/
                      Principals Only                                              Analyst

                                                                                                                                                 tmp/
                 Source/Bronze                                                  Prod/Gold                                                                             ....




                                                      Silver                                 Here you have a mix of objects living in the same cloud storage bucket, user or
                                                                                             team directories, and places where versioned data may live. Providing access
                                                                                             control over this via cloud controls is limited and difficult to manage at scale. To
                                                       Scientists
                                                                                             compound that problem, the interfaces to apply access control lists (ACLs) are
                                                       Engineers
                                                                                             not homogenous as you move across different cloud providers in the pursuit of
                                                                                             multicloud architectures. So you end up creating and managing controls in different
                                                                                             places, which relies on costly resources or automation to keep things in sync.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                             16




And because each system works differently, you have to map the intent of each         straightforward rules and tags, ABAC ensures consistent governance across all
policy you write to every downstream system, which can be an integration              data sources, whether native to Databricks or federated from external sources.
challenge even if working with a data governance toolkit.                             Its flexibility extends to the ease of defining and managing access policies,
                                                                                      providing users with intuitive options such as the policy builder UI, SQL queries
When you factor in the centralized metadata and centralized user management           and APIs. Moreover, Databricks ABAC seamlessly integrates with third-party
components offered by Unity Catalog, a data governance user in your enterprise        governance tools, enhancing its interoperability and allowing organizations to
can run simple ANSI SQL GRANT statements on objects to provide access to a            leverage existing investments in governance infrastructure.
group and manage the membership of that group externally. This lets members
of the group dictate who has access to SELECT or MODIFY data in your catalog          With ABAC, users can establish access controls tailored to specific attributes
and across your data lakes.                                                           of resources like workspaces, data assets such as tables and AI assets. These
                                                                                      attributes encompass a wide range of parameters, including user-defined tags,
Unity Catalog also offers the same capabilities via REST APIs and Terraform           workspace details, location, identity and time. Whether it’s ensuring sensitive
modules to allow integration with existing entitlement request platforms or           data remains restricted to authorized personnel or dynamically adjusting access
policies as code platforms. These objects can also be file storage paths in your      based on changing project requirements, ABAC empowers users to enforce
cloud storage containers.                                                             security measures with granular precision.

In the example above, consider the encircled objects to be external locations
within Unity Catalog. This allows you to provide differential access control on
various parts of your container hierarchy, ensuring that users have access to their
subdirectories and that groups have access to read from the shared locations.


Attribute-based access control
Applying access controls on resources and roles can be exceedingly complex
when you have thousands of resources and thousands of groups. Attribute-
based access controls ABAC, offer a simplified way to dictate access control
based on the semantics of your data. You apply semantic definition by
associating attributes, known as tags, to resources, users and groups.


ABAC offers organizations a high-leverage governance solution that simplifies the
enforcement of governance policies across their entire lakehouse. By employing
                                                                                                                                             Attribute-based access controls
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                        17




Auditing entitlements and access
Earlier, we discussed two tenets of an effective data security governance         Achieving this with existing cloud security controls is a task that requires ETL
program: understanding who has access to what data, and who has recently          from access logs, centralization across thousands of different sources and
accessed what data. This is critical for almost all compliance requirements for   federation across multiple formats. Depending on the capabilities of the source
regulated industries, and it’s a fundamental facet of any security governance     systems, this typically only gets you the first two key pieces of information.
program.
                                                                                  Unity Catalog offers a centralized audit feature that homogenizes access across
Without effective audit mechanisms in place, you don’t understand your risk       your metastore, including access to logical objects as well as access to arbitrary
surface area. That is to say, you don’t know who can potentially misuse data      cloud storage paths in your data lakes. In addition, Unity Catalog helps you to
within your organization. Being able to proactively identify overentitled users   understand the specific operations, i.e., queries that your users are performing.
and groups and change their accesses accordingly in a centralized manner is       Unity Catalog also offers a comprehensive UI, APIs and system tables that allow
a key function of a well-designed audit team within a security or data            you to query the ACLs on resources, so you can effectively audit access by
governance organization.                                                          resources or by users to understand audit implications in real time, without
                                                                                  waiting for systems to be in sync or for audit data to be shipped
An effective audit mechanism functionally provides three key pieces               and consolidated.
of information:
   • For any resource, indicate who had access at any point in time               Combining this information across cloud architectures becomes simpler
   • For any access to a resource, indicate the resource that performed           because you’re operating in a common format, and audit data can be readily
     the operation                                                                combined for aggregate views across multiple metastores in different clouds
                                                                                  and cloud regions.
   • For any access to a resource, indicate the operation performed by
     the resource
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                       18




Data lineage
Today, organizations deal with an influx of data from multiple sources, and       This typically means identifying the tables and datasets used in a report or
building a better understanding of where data is coming from and how it’s         dashboard and tracing the source of these tables and fields, making data
consumed becomes paramount to ensure the quality and trustworthiness of           traceability a key requirement for their data architecture. Data lineage helps
the data. Data lineage is a powerful tool that helps data leaders drive better    organizations be compliant and audit-ready, thereby alleviating the operational
transparency and understanding of data in their organizations. The term data      overhead of manually creating the trails of data flows for audit reporting.
lineage describes the transformations and refinements of data from source
to insight. Lineage includes capturing all the relevant metadata and events       Impact analysis/change management
associated with the data in its lifecycle, including the source of the dataset,   Data goes through multiple updates or revisions over its lifecycle, and
what other datasets were used to create it, who created it and when, what         understanding the potential impact of any data changes on downstream
transformations were performed, what other datasets leverage it, and many         consumers becomes important from a risk management standpoint. With
other events and attributes. With a data lineage solution, data teams get an      data lineage, data teams can see all the downstream consumers — applications,
end-to-end view of how data is transformed and how it flows across their data     dashboards, machine learning models, datasets, etc. — impacted by data
estate.                                                                           changes. They can see the severity of the impact and notify the relevant
                                                                                  stakeholders. Lineage also helps IT teams proactively communicate data
As more and more organizations embrace a data-driven culture and set up           migrations to the appropriate teams, ensuring business continuity.
processes and tools to democratize and scale data and AI, data lineage is
becoming an essential pillar of a pragmatic data governance strategy.             Data quality assurance
                                                                                  Data lineage also empowers data consumers such as data scientists, data
To help you understand the importance of data lineage, we highlight some          engineers and data analysts to be context-aware as they perform analyses,
common use cases:                                                                 resulting in better quality outcomes. Data stewards can see which datasets are
                                                                                  no longer accessed or have become obsolete to retire unnecessary data and
Compliance and audit readiness                                                    ensure data quality for end business users.
Many compliance regulations, such as the General Data Protection Regulation
(GDPR), the California Consumer Privacy Act (CCPA), the Health Insurance          Debugging and diagnostics
Portability and Accountability Act (HIPPA), the Basel Committee on Banking        You can have all the checks and balances in place, but something will eventually
Supervision (BCBS), and the Sarbanes-Oxley Act (SOX), require organizations       break. Data lineage helps data teams perform a root cause analysis of any errors
to have a clear understanding and visibility of their data flow and prove the     in their data pipelines, applications, dashboards, machine learning models, etc.,
data/reports they are submitting came from a trusted and verified source.         by tracing the error to its source. This significantly reduces the debugging time,
                                                                                  saving days, or, in many cases, months of manual effort.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                              19




Unity Catalog provides automated and real-
time lineage by automatically capturing lineage
generated by operations executed in the Databricks
Platform. Lineage is not limited to just SQL. It works
across all workloads in any language supported
by Databricks — Python, SQL, R and Scala. This
empowers all personas — data analysts, data
scientists and ML experts — to augment their tools
with data intelligence and the context surrounding
the data, resulting in better insights. Unity Catalog
captures data lineage for tables, views, columns
and files. This information is displayed in real time,
providing data teams a granular view of how data
flows both upstream and downstream from a
particular table or column in the Databricks Data
Intelligence Platform with just a few clicks. Unity
Catalog can also capture lineage associated with
non-data entities, such as notebooks, workflows and
dashboards. This helps with end-to-end visibility
into how data is used in your organization.



                                                                                Data lineage in Unity Catalog
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                             20




Data quality management and monitoring
Data needs to be trusted to harness its true value. Bad-quality data leads to     In addition to being able to view the provenance of a dataset, it’s important
inaccurate analytics, poor decision-making and cost overhead. Gartner estimates   to understand if the data within the table has violated any rules provided by
that poor data quality costs organizations an average $12.9 million every year.   domain experts. Delta Live Tables (DLT) performs checks against data during
An effective data governance strategy must include a focus on data quality so     runtime when processing the data. These checks are called expectations and are
that the provenance of data can be known, rules can be enforced on the data       aggregated and viewable for each DLT table. Delta Live Tables helps to ensure
and changes can be tracked.                                                       accurate and useful BI, data science and machine learning with high-quality data
                                                                                  for downstream users. DLT prevents bad data from flowing into tables through
When evaluating a dataset for quality, a few key attributes                       validation and integrity checks, and avoids data quality errors with predefined
should be examined:                                                               error policies (fail, drop, alert or quarantine data). In addition, you can monitor
                                                                                  data quality trends over time to get insight into how your data is evolving and
   • Is the data accurate in every detail? Is it complete?
                                                                                  where changes may be necessary.
   • Where is it coming from?

   • How fresh is the data?

   • Does the dataset violate any data quality rules?


With automated and real-time data lineage, Unity Catalog makes it easy to
quickly understand who owns a dataset and where its data originated. Data
lineage is automatically captured for Unity Catalog datasets. A user can easily
traverse the lineage to see both the upstream data sources that were used to
generate the dataset and the downstream consumers in the form of other tables,
notebooks, dashboards, etc.




                                                                                                                        Automatic data quality testing with Delta Live Tables

A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                    21




In the realm of data and ML quality, despite the implementation of meticulous          To confront these challenges, the Databricks Data Intelligence Platform
checks and balances, the inevitability of occasional disruptions remains.              introduced Lakehouse Monitoring — an integrated solution for overseeing data and
Therefore, data teams must embrace the task of monitoring data quality over            ML model quality. This holistic approach empowers users to configure monitoring
time. Consider a scenario in which a data engineer overlooks utilizing the “update”    parameters for both data and ML models. Proactive alerts are triggered when
command on a table, leading to the accumulation of numerous rows with each             data quality metrics, such as the percentage of null values in a table, fall below
data load. Consequently, end data users encounter obstacles when querying the          predefined thresholds, or when sensitive data is detected in unmasked form, or
data for their specific use cases. This issue often only surfaces when a data user     even in the presence of significant prediction drift in the ML model. The solution
reports it. Similarly, envision a situation where a reference table misses values in   also encompasses autogenerated dashboards. Leveraging the lineage information
a row following an update, causing downstream queries to fail when merging it          within Unity Catalog, data teams can conduct root cause analysis and assess the
with another table. Additionally, contemplate the instance where the performance       impact of quality issues, thereby enhancing their ability to address and mitigate
and accuracy of a trained machine learning model erodes as the production data         disruptions effectively.
distribution diverges from the distribution on which the model was trained. This
situation is compounded when application development teams deactivate these
production models. As a result, data teams grapple with the following challenges:

   • Reactive issue management: Data consumers encounter problems before
     data owners, leading to inefficiencies in resolution

   • Bottlenecked operations: Data consumers are deprived of self-service
     experiences, necessitating their reliance on data engineering teams to rectify
     quality issues

   • Inefficient processes: Debugging quality issues and reverting changes can
                                                                                                                                            Proactive alerts on quality issues
     consume weeks, impacting overall operational efficiency


Existing monitoring solutions often pose hurdles. Setting up monitors, crafting
dashboards and configuring alerts demand substantial time and resources.
Furthermore, data teams employ diverse quality metrics and frameworks, which
deter them from adopting multiple solutions and manually creating isolated
dashboards for custom metrics. The predicament escalates as data teams
                                                                                                                      Root cause analysis and impact assessment with lineage
manage segregated monitoring tools for data scientists and data engineers,
impeding collaboration and debugging efforts.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                           22




Data intelligence
As organizations accumulate vast amounts of data and diverse assets like ML
models, notebooks and dashboards, distilling intelligence from the data landscape
becomes crucial. This opportunity not only enables the democratization of
data and AI for both technical and nontechnical audiences in a scalable manner
but also has the potential to accelerate business efforts and create a distinct
competitive advantage.


LLMs have heralded the promise of instating language interfaces for data, and
the integration of AI assistants by data companies is becoming commonplace.
However, in reality, a significant number of these solutions fall short of their
intended objectives. Each organization possesses unique datasets, industry-
specific jargon and internal knowledge that are essential for addressing their
distinct business inquiries. The mere deployment of an LLM trained on web data
to answer questions unique to the business often yields erroneous outcomes. The
                                                                                                                                                              DatabricksIQ
simplest terms, like “customer” or the fiscal year, can exhibit discrepancies across
different companies.                                                                   DatabricksIQ leverages data, usage patterns and the organizational structure to
                                                                                       grasp the specific terminology and unique data environment of your business.
To address this critical need, Databricks introduced DatabricksIQ, an innovative       This results in markedly improved responses compared to the naive application of
knowledge engine that directly confronts these challenges by autonomously              LLMs. Any user in your organization, whether technical or nontechnical can utilize
assimilating knowledge about business and data concepts within your enterprise.        DatabricksIQ to search, understand and extract insights from the data in natural
DatabricksIQ leverages insights from the complete Databricks Data Intelligence         language. The impact of DatabricksIQ isn’t limited to enhancing queries and
Platform, including Unity Catalog, dashboards, notebooks, data pipelines and           troubleshooting. Its functionalities extend to a diverse range of natural language
documentation. With the aid of this knowledge graph, it discerns the practical         interfaces across the Databricks Platform. Furthermore, DatabricksIQ capabilities
application of data, enabling the construction of highly accurate specialized          are accessible through APIs, granting your customers the power to create their
models tailored to your organization.                                                  own AI applications that harness this autonomously cultivated knowledge.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                               23




Data sharing and collaboration
Today’s economy revolves around data. Data sharing has a key role to play           Delta Sharing also provides a robust list of native connectors such as pandas,
in business processes across the enterprise, from product development               Apache Spark, Java, Power BI, Python, Tableau, R and many more, providing data
and internal operations to customer experience and compliance. More and             consumers the flexibility to query, visualize, transform, ingest or enrich shared
more, organizations must exchange data with their business units, customers,        data with their tools of choice, if they are not on the Databricks Platform.
suppliers and partners. Security is critical. And yet, efficiency and immediate
accessibility are equally important. To be truly data-driven, organizations need    Delta Sharing is natively integrated with Unity Catalog, enabling organizations
a better way to share data. Where data sharing was once considered optional,        to centrally manage and audit shared data across organizations and confidently
it’s now fundamental. More organizations are investing in streamlining internal     share data assets while meeting security and compliance needs.
and external data sharing across the value chain. But they still face major
roadblocks — from human inhibition to legacy solutions to vendor lock-in.


We believe the future of data sharing should be characterized by open                                                                         DATA CONSUMER ON DATABRICKS


technology. Data sharing shouldn’t be tied to a proprietary technology that                 DATA PROVIDER ON DATABRICKS
                                                                                                                                                    Data consumer #1
introduces unnecessary limitations and financial burdens to the process.
                                                                                                                                         UNITY
                                                                                                                                        CATALOG
                                                                                                Data provider
This philosophy inspired us to develop and release a new protocol for sharing
data: Delta Sharing.                                                                                                UNITY
                                                                                                                   CATALOG
                                                                                                                                        DATA CONSUMER (NOT ON DATABRICKS)

Delta Sharing provides an open solution to securely share live data from your
lakehouse to any computing platform. Recipients don’t have to be on the                                                                           Data consumer #2
Databricks Platform or on the same cloud or a cloud at all. Data providers can
share live data from where it lives in their cloud storage without replicating it
or moving it to another system. This approach reduces the operational cost
of data sharing, as data providers don’t have to replicate the data multiple
times across clouds, regions or data platforms to reach their data consumers.
With Delta Sharing, organizations can easily share existing large-scale
datasets based on the open source formats Apache Parquet and Delta Lake.                                                                           Data sharing with Databricks
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                             24




Privacy-safe data clean rooms
With the demand for external data greater than ever, organizations are looking
for ways to securely exchange their data and consume external data to foster
                                                                                                                       Data Clean Room
data-driven innovations. Historically, organizations have leveraged data-
sharing solutions to share data with their partners and relied on mutual trust
to preserve data privacy. But organizations relinquish control over the data
once it’s shared and have little to no visibility into how data is consumed
by their partners across various platforms. This exposes potential data
misuse and data privacy breaches. With stringent data privacy regulations,
it’s imperative for organizations to have control and visibility into how
their sensitive data is consumed. As a result, organizations need a secure,
controlled and private way to collaborate on data, and this is where data clean
                                                                                                                                                           Data Clean Room
rooms come into the picture.
                                                                                  Powered by open source Delta Sharing, the Databricks Data Intelligence Platform
A data clean room provides a secure, governed and privacy-safe environment        provides a flexible data clean room solution, allowing businesses to easily
in which multiple participants can join their first-party data and perform        collaborate with their customers and partners on any cloud in a privacy-safe way.
analysis on the data without the risk of exposing their data to other             Participants in the data clean rooms can share and join their existing data and
participants. Participants have full control of their data and can decide which   run complex workloads in any language — Python, R, SQL, Java and Scala — on the
participants can perform what analysis on their data without exposing any         data while maintaining data privacy. Additionally, data clean room participants
sensitive data such as personally identifiable information (PII).                 don’t have to do cost-intensive data replication across clouds or regions with
                                                                                  other participants, which simplifies data operations and reduces cost.




                                                                                                               Data clean room with the Databricks Data Intelligence Platform
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                           25




Data marketplaces
The demand for third-party data as a catalyst for data-driven innovations
has reached unprecedented levels. In this landscape, data marketplaces
have emerged as pivotal connectors between data providers and consumers,
facilitating the seamless exploration and dissemination of diverse datasets.

In parallel, the surge in generative AI’s prominence has triggered substantial
industry disruption. Organizations are now under heightened pressure to swiftly
engineer their generative AI models and LLM frameworks, leveraging proprietary
data reserves to gain a competitive edge and carve a distinctive niche for their
offerings.


At the epicenter of this transformative paradigm, Databricks Marketplace
shines as an exemplar. It transcends conventional data exchange platforms
by encompassing a broader gamut, encompassing not only data but also
notebooks, dashboards and machine learning models. This orchestration
                                                                                                                                    Databricks Marketplace
empowers data consumers with expedited insights, granting them access to,
evaluation of, and engagement with an expansive repertoire of data products
originating from a diverse array of third-party vendors.


The ingenuity of this platform extends further, empowering data providers
to infuse novel value into their offerings, thereby shortening sales cycles and
introducing novel value-added services anchored in their data products. At
the core of this marketplace’s potency lies its infrastructure backbone: Delta
Sharing. This architectural innovation seamlessly facilitates data product
access for consumers, alleviating the necessity of platform lock-in. This
open framework fosters an expanded ecosystem, enabling data providers to
                                                                                   Learn more
broaden their market horizon while liberating consumers from vendor-specific
constraints.
                                                                                   To learn more about data sharing on Databricks, please read
                                                                                   this free eBook on data sharing.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                          26




Chapter 2
AI Governance
The principles of governance — accountability, standardization,                 Unlocking consistent value from ML investments requires
compliance, quality and transparency — apply at least as much to                that models are:
AI as to data. AI governance sets out the policies and procedures                • Compliant with necessary regulatory and ethical standards
for the development and application of models in an organization.
                                                                                 • Reproducible in terms of performance and results
With proper governance, ML can bring improved value to business
processes, efficiency in automating or augmenting decision-making                • Explainable and transparent in their development and impact

and decreased regulatory, legal and reputation risks.                            • Routinely monitored and updated to maintain quality

                                                                                 • Properly cataloged and documented following standardized policies
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                  27




AI governance on the lakehouse
Compliance and ethics
The minimum bar that ML governance must set is that any models used need to        Many of these regulations focus on what types of data inputs
conform to regulations pertinent to the industry or application that they serve.   (independent variables) may be used when training models. Using Unity Catalog
For example, in the United States, the financial services and education sectors    for fine-grained control of data is a secure way to programmatically restrict
are subject to legislation dictating what types of inputs may be included in       what can be used as inputs by which teams to ensure compliance.
the development and training of models. These standards are meant to ensure
that protected classes of the population receive equitable access to lending,      However, compliance only covers what must be done. Beyond the legal
housing, education and other crucial services.                                     requirements are a host of potential ethical considerations that constitute
                                                                                   what should be done. It’s in this area where many examples of well-intentioned
When establishing your ML governance program and policies, consult with legal      but poorly governed models have caused reputational headaches for companies
counsel to ensure that you have a thorough understanding of the regulations        of all sizes. A process should be defined as part of your governance program
you must operate under in your jurisdictions. They may vary based on the           to assess model impacts and identify potential misuses before moving
application. For instance, a retailer operating a private label credit card is     to production.
subject to the Equal Credit Opportunity Act just as a financial services company
would be, despite mostly being in a different industry.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                    28




                         Machine learning reproducibility
                         Being able to reproduce the results of machine learning allows for   standards. Due to the multifaceted nature of model development,
                         auditing and peer review of the data and methodology used for        there are multiple stages of the process that must be tracked in
                         creating the final model. This improves trust in the performance     order for the entire study to be reproduced.
                         it will have in production and the ability to meet compliance
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                                      29




1. Feature engineering — The variables, labels                                      of the model in a batch mode and the serving of             train it is often lost, causing problems in trying
and encodings used as inputs to the model should                                    an inference pipeline in a streaming mode without           to recreate how the parameters of the model
be stored in an accessible, reusable manner.                                        having to create and maintain a separate workflow,          were determined. When using Managed MLflow
Databricks includes a Feature Store for this purpose                                which could otherwise introduce discrepancies.              on the Databricks Platform, datasets are logged
that can be referenced in model development.                                                                                                    alongside experiments so that the end-to-end
Databricks Feature Store provides lineage tracing                                   2. Data access, prep and wrangling —                        development cycle of machine learning models can
tied to your broader data governance so that                                        Sampling and splitting data during model                    be reproduced easily.
upstream or downstream impacts from any changes                                     development is a common way to create and then
are visible. It also ensures reproducibility of the logic                           test models for extensibility. Once a model has
used for feature calculation between the training                                   been selected, the data that was used to initially




                                                                          (2) The same features are made                (3) Deployed model automatically
                                                                           available online for low-latency             looks up correct features from the
                                                                                       serving                                    feature store




                                                                                                                                                                             Feature engineering
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                            30




                                                                                                                                                              Model training



                3. Model training — Most machine learning models selected for          optimization of model evaluation metrics. MLflow captures all of these
                production are not the first iteration that the engineers developed.   iterations along with the pertinent metrics so that the entire process of
                Instead, extensive testing and evaluation has gone on to select        training and selecting a model can be reproduced if needed. And with
                appropriate methodologies and frameworks, tune parameters and          Unity Catalog, ML engineering teams can drive better collaboration as
                hyperparameters, and then balance speed of execution with              data can be securely accessed across workspaces for model training.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                           31




Explainability and transparency
Data governance is involved in explaining and providing transparency into        As part of MLflow, Databricks integrates bias detection and explainability using
what data is used where and to what end. Similarly, a part of ML governance is   SHapley Additive exPlanations (SHAP). SHAP provides views of which features
concerned with giving insight into how models come up with the conclusions       played the largest roles and which directions led to the outputs scored. SHAP
that they do.                                                                    is a broadly applicable tool for this purpose and can be used on many different
                                                                                 types of algorithms. It may be applied either globally (e.g., it looks at the entire
However, interpreting machine learning models can be challenging, especially     population of scores and evaluates for biases and feature impact) or locally
when more advanced types of algorithms are used in their development.            (e.g., evaluating the score of one record and determining which features played
Some of the most commonly used frameworks, such as XGBoost or neural             significant roles in that one outcome).
networks, are considered too complex for humans to conceptualize. In order
to shine a light into the “black box,” you need tools for evaluating what has    Many additional frameworks are available for assessing bias and providing
happened inside the box.                                                         transparency into the inner workings of models. These may be added to clusters
                                                                                 operating on a Databricks Runtime ML as needed to enhance the explainability
                                                                                 of models developed.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                                32




Model monitoring
Governance does not end once machine learning                                   the possible outcomes were “approve” or “decline,”       The result would be a sudden loss of meaningful
models get to production. If anything, increased                                then the model would only ever classify into these       information and a massive shift in income levels
scrutiny should be placed on models as they’re                                  two categories. If subsequently, the business            showing as “Other.” No actual break in the pipeline
used in “real world” scenarios and are exposed                                  decides to create a team that will manually review       would’ve happened, but the upstream process
to new situations. Traditionally, models that were                              loans that don’t quite meet the approval threshold       change could cause the model to behave erratically
developed using data science and machine                                        but aren’t terribly far off, the model could be          if income was a significant feature.
learning techniques were expected to degrade                                    trained for a third option to classify some range of
in performance and applicability over time. Even                                loans into this group.                                   Data drift — Data changes over time, even without
with online learning capabilities, models sometimes                                                                                      intentional changes made in upstream processes.
span shifts in the market or business practices                                 Upstream data changes — This is broadly thought          Economic conditions, market trends, seasonality,
that necessitate revisiting their training or use.                              of as breaks in the data pipelines that generate the     cultural shifts — anything that changes behavior
It requires continual monitoring to be able to trust                            features that are used in the model. Using proper        will alter the data collected on that behavior. This
and get long-term value from models being used                                  lineage tracking with Unity Catalog and Feature          is probably the most common cause of model
in production.                                                                  Store on Databricks should prevent most outages          degradation in production and the area given most
                                                                                or breaking impacts. However, it’s still possible that   scrutiny. Data drift can cause a slow and gradual
Some of the concerns addressed around                                           a business process change could cause significant        decline or very sudden shocks.
monitoring models include:                                                      problems in a model.
                                                                                                                                         As an example, take a manufacturer that has
Concept drift — This represents a change in                                     An example of this might be seen in how income is        developed a demand forecasting model that can
the possible results that the model could generate.                             bucketed and encoded as variables. Let’s assume          help ensure that materials are in factories at the
Concept drift can come from changes in the                                      that, at the time of model development, there            right time to make goods and get them to shelves.
market, technology, business processes or                                       were increments of $25,000 up to $150,000 and            Then their largest competitor declares bankruptcy
other external factors.                                                         an “Other” bucket, which could be selected from          and there is a sudden surge in demand. No data on
                                                                                a drop-down menu in a customer service screen.           this type of rare event was included in the model,
An example of this could be a sudden allowal                                    Then a change was made to use increments of              so the performance of the forecast is horribly off.
of manual review for certain groups of loan                                     $30,000 up to $150,000 and keep the Other                An alert should be put in place for large swings like
applications. If, when the model was developed,                                 bucket. Because the old values have disappeared,         this so that a new model can be developed taking
                                                                                the new values may not be properly encoded.              into consideration the new competitive landscape.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                             33




Bias — In the context of machine learning, bias is                              With Databricks Lakehouse Monitoring, you
typically seen in the statistical sense, meaning that                           can continuously assess the performance of
there is a mathematically demonstrable imbalance in                             your models, scanning application outputs to
the data seen versus some ground truth. This could                              detect any problematic content. This includes
be seen as an imbalance of input to the model (e.g.,                            monitoring for fairness and bias in sensitive
you know that 50% of your customers are located                                 AI applications like classification models. The
in Europe, but only 15% of the data coming into the                             platform quickly identifies issues such as
model are from European customers) or outputs (e.g.,                            model drift due to outdated data pipelines or
you expect that 2% of your customers will purchase                              unexpected model behavior. Key features include
socks on a given visit, but the recommendation                                  customizable dashboards, real-time alerts,
engine you built shows socks to 80% of customers as                             flexible observation time frames, audit logs and
a top selection for them).                                                      the option to define custom metrics. Additionally,
                                                                                it offers PII detection for enhanced data security.
In common parlance, bias is often seen as the                                   Lakehouse Monitoring, in conjunction with lineage
inequitable treatment of one group of people versus                             tracking from Unity Catalog, accelerates threat                                          Lakehouse Monitoring
another. This is one of the most essential forms of                             response, facilitates faster issue resolution and
bias to monitor for in model performance, as it could                           enables thorough root cause analysis. Databricks
                                                                                                                                       Additionally, the Mosaic training platform, including
cause substantial damages to customer experience                                Inference Tables automatically capture and log
                                                                                                                                       the Mosaic LLM Foundry suite of training tools, and
and reputation and even have legal ramifications. If                            incoming requests and model responses as Delta
                                                                                                                                       the Databricks RAG studio tools, can be used to
you have demographic data available, it’s advisable                             tables in Unity Catalog. This data is invaluable for
                                                                                                                                       assess and tune models post-launch to mitigate
to create a governance policy around checking for                               monitoring, debugging and optimizing ML models
                                                                                                                                       identified issues. The Patronus AI EnterprisePII
disparate impacts across various cross-sections                                 post-deployment.
                                                                                                                                       automated AI evaluation tool included in the LLM
of demographics even if you are not operating in a
                                                                                                                                       Foundry can be useful to detect the presence of a
highly regulated industry where this is required.
                                                                                                                                       customer’s business-sensitive information as part
                                                                                                                                       of model security post-release. Toxicity screening
As part of your ML governance program, establish
                                                                                                                                       and scoring are also incorporated within RAG Studio.
guidelines for what thresholds are acceptable for
                                                                                                                                       The Mosaic Evaluation Gauntlet benchmarking tool
model performance, a cadence for model monitoring
                                                                                                                                       can be used to assess model performance on an
and procedures for alerting when upstream
                                                                                                                                       ongoing basis.
processes are changed or problems are found.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                              34




Model serving
Databricks Model Serving, a serverless solution, provides a unified interface for    the Databricks Data Intelligence Platform. By leveraging these robust security
deploying, governing and querying AI models with secure-by-default REST API          measures and risk mitigation strategies, you can confidently build, deploy and
endpoints. The Model Serving UI enables centralized management of all model          manage your AI systems while maintaining the highest levels of security.
endpoints, including those hosted externally. This platform supports live A/B
testing, allowing you to compare model performance and seamlessly switch to          While many of the risks associated with AI may seem unrelated to
more effective models. Automatic version tracking ensures that your endpoints        cybersecurity (e.g., fairness, transparency, reliability, etc.), canonical controls
remain stable while iterating on your models behind the scenes. Additionally,        that have been managed by cybersecurity teams (e.g., authentication, access
Databricks MLflow AI Gateway centralizes governance, credential management           control, logging, monitoring, etc.) for decades can be deployed to mitigate many
and rate limits for model APIs, including SaaS LLMs, through Gateway Routes (with    non-cybersecurity risks of AI. Therefore, cybersecurity teams are uniquely
each route representing a model from a specific vendor). MLflow AI Gateway offers    positioned to play an outsized role in ensuring the safe and responsible use of
a stable endpoint interface, enabling smooth model updates and testing without       AI across organizations.
disrupting business operations.


AI security
With the rise of AI, concerns about security are also increasing. In fact, 80% of
data experts believe AI increases data security challenges. Recognizing this,
security has become a foundational element of the Databricks Data Intelligence
Platform. We offer robust security controls to safeguard your data and AI
operations, including encryption, network controls, data governance and auditing.
These protections extend throughout the entire AI lifecycle — from data and
model operations to model serving.


To help our customers navigate the ever-evolving landscape of AI security threats,
Databricks has developed a comprehensive list of 55 potential risks associated
with each of the twelve components of an end-to-end AI system. In response
to these identified risks, we provide detailed and actionable recommendations
as part of the Databricks AI Security Framework (DASF) to mitigate them using

                                                                                                                                             Databricks AI Security Framework
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                         35




Cataloging and documentation
Gathering and making available metadata around data and ML is core to                 automatically during the model training process provides context for those
governance. Catalogs for ML, in particular, provide insight and guidance on           searching through what has already been developed to use and expand upon.
what is available and how it may be reasonably used. This helps data scientists       With the support for cataloging and managing access to ML feature tables and
build upon one another’s work — taking techniques and expanding upon them             ML models in Unity Catalog, governance policy can then be enforced to ensure
as best practices. Reuse in this way — sometimes a form of transfer learning —        that the security of sensitive data is maintained and the use is appropriate.
accelerates the time to production and value for the company.
                                                                                      With feature engineering supported in Unity Catalog, you no longer need to
Leveraging tools like Databricks Feature Store, MLflow and Unity Catalog is a great   manage separate data catalogs for AI/ML and data. You can have a single, unified
start to identifying existing ML assets within the organization. Metadata captured    catalog for all data and AI.




                         Datasets + feature
                              tables




                                                                                                                                  ML models, feature tables
                                                                                                                                  in Unity Catalog
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                                                36




Chapter 3
Platform Security and Compliance
We learned how data governance ensures the security, quality, integrity, lineage and availability of data across                                          Platform security
an organization. However, to meet stringent regulatory and compliance requirements and alleviate the risk
                                                                                                                                                          Today, more and more organizations recognize the
of any data breaches, the security of the data platform also becomes a key consideration for data and AI
                                                                                                                                                          importance of making high-quality data readily
initiatives. In this chapter, we’ll explore how the Databricks Data Intelligence Platform provides end-to-end
                                                                                                                                                          available for data teams to drive actionable insights
security and helps you meet compliance requirements.
                                                                                                                                                          and business value. At the same time, organizations
                                                                                                                                                          also understand the risks of data breaches, which
                                                                                                                                                          negatively impact brand value and inevitably lead
            Network security                                                                                               User administration
        Deploy to your VPC/VNet                                                                                            Single sign-on                 to the erosion of customer trust. Organizations that
                       Private link                                                                                        SCIM provisioning              operate in multicloud environments need a unified,
                IP access control                                                                                          Service principles
   Autimatic host-based firewalls                                                                                          Lock user accounts w/ SCIM     reliable and consistent approach to secure data.
                                                                                                                           Disable local passwords
                                                                                                                                                          We’ve learned from our customers that a simple and
                                                                                                                           Access management              unified approach to data security for the lakehouse
             Server security                                                                                               Fine-grained access
                                                                                                                           control to workspaces, jobs,
                                                                                                                                                          is one of the most critical requirements for modern
          Manage code versions                                                                                             notebooks, SQL, etc.
                      securely
                                                                                                                           Python and SQL table
                                                                                                                                                          data solutions. With significant investment into
     Built-in secret management                                                                                            access control
       CIS-hardened VM images
                                                                                                                                                          building a highly secure and scalable platform,
                                                                                                                           Job isolation
              updated biweekly
                                                                                                                           Secure API access with         Databricks delivers end-to-end platform security
             Enhanced security                                                                                             personal access tokens
                   monitoring
                                                                                                                           Data psedonymization           for data and users.
                 Cluster policies
          Immutable short-lived
                 infrastructure                               Date security
                                                              Encryption in transit and at rest    Compliance and monitoring
                                                                                                                                                          The Databricks Data Intelligence Platform is
                                                              Column and row-level dynamic views   User activity logging                                  split into two planes — control plane and data
                                                              Data governance with Unity Catalog
                                                                                                   Notebook + SQL history logging
                                                              Data exfiltration controls
                                                                                                   HIPAA, PCI, FedRAMP
                                                                                                                                                          plane — to simplify your permissions, avoid data
        ©2024 Databricks Inc. - All rights reserved           Customer-managed keys
                                                                                                                                                          duplication and reduce risk. The control plane is
                                                                                                       The Databricks Data Intelligence Platform          the management plane where Databricks runs the
                                                                                                                                                          workspace application and manages notebooks,
                                                                                                                                                          configuration and clusters. Unless you choose to
                                                                                                                                                          use serverless compute, the data plane runs inside
                                                                                                                                                          your cloud service provider account, processing
                                                                                                                                                          your data without taking it out of your account.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                37




You can embed Databricks in your data exfiltration protection architecture using          Data compliance
features like customer-managed VPCs/VNets and admin console options that
                                                                                          Meeting the regulatory compliance requirements is perhaps one of the key
disable export. While certain data, such as your notebooks, configurations, logs
                                                                                          drivers for data governance initiatives. Databricks is trusted by the world’s largest
and user information, is present within the control plane, that information is
                                                                                          organizations to provide a powerful lakehouse platform with high security and
encrypted at rest, and communication to and from the control plane is encrypted
                                                                                          scalability. Databricks has put in place controls to meet the unique needs of highly
in transit.
                                                                                          regulated industries, including compliance certifications such as ISO 27001 and
Regardless of where you choose to host the data plane, Databricks networking              SOC2. But Databricks also has industry-specific compliances such as HIPAA for
is straightforward. If you host it yourself, Databricks by default will still configure   healthcare, PCI for financial industries, FedRAMP for federal agencies and so on.
networking for you, but you can also control data plane networking with your own          This is a growing list — as we see more use cases and customers needing more
managed VPC or VNet.                                                                      validations, we’re always willing to jump in and work alongside you to help with
                                                                                          your compliance needs.
The serverless data plane network infrastructure is managed by Databricks in
a Databricks cloud service provider account and shared among customers, with
additional network boundaries between workspaces and between clusters.

Databricks does not rewrite or change your data structure in your storage, nor
does it change or modify any of your security and governance policies. Local
firewalls complement security groups and subnet firewall policies to block
unexpected inbound connections.

From a data perspective, all data is stored in the customer’s cloud object
storage, and Databricks offers end-to-end encryption for both data at rest
and data in motion.

This is the Databricks Platform and its security approach at a high level. For more
details, visit the Databricks Security and Trust Center.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                                                                                                                 38




About the Authors
Amr Ali is a Senior Solutions Architect at Databricks                           Lexy Kassan is a Senior Data and AI Strategist            Mayur Palta is a Senior Specialist Solution Architect
and has over 18 years of experience in building                                 at Databricks, overseeing and guiding customer            at Databricks and leads a competitive intelligence
IT solutions. Amr has helped many organizations                                 organizations through holistic digital transformation     focus for data management and a win-loss
build their data and AI platform around lakehouse                               programs. She is also the founder and host of a data      program at Databricks. Mayur’s career spans
technology to achieve their business goals, with a                              science ethics podcast in which she delves into the       building technology startups, helping Fortune 500
strong emphasis on data architecture governance                                 responsibilities and societal ramifications of applying   enterprises get more value from their data and
and security.                                                                   advanced analytics across both private and public         building data architectures that scale.
                                                                                sectors.
Bernhard Walter is a Lead Product Specialist for
architecture at Databricks and has about 30 years                               Sachin Thakur is a Principal Product Marketing
of experience in different roles in the IT industry. His                        Manager at Databricks. He leads the go-to-market
primary focus at Databricks is to help customers                                strategy for Delta Sharing and Unity Catalog,
to create efficient and future-proof lakehouse                                  and he is passionate about helping organizations
architectures that optimally support their business.                            democratize data and AI with the Databricks Data
                                                                                Intelligence Platform.
Jason Pohl is the Director of Data Management
at Databricks. He helps shepherd new products                                   Zeashan Pappa is a Staff Product Manager for Unity
to market in the fields of data warehousing, data                               Catalog at Databricks and works across product,
engineering and data governance. Jason’s career                                 engineering and field teams on go-to-market
spans architecting legacy data warehouse solutions                              strategy, adoption and thought leadership. He has
to modern data lakehouses in the cloud.                                         20 years of experience in engineering, architecture
                                                                                and tech leadership at a variety of firms.
A C O M P R E H E N S I V E G U I D E T O D ATA A N D A I G O V E R N A N C E                    39




About Databricks
Databricks is the data and AI company. More than 10,000
organizations worldwide — including Block, Comcast, Condé Nast,
Rivian, Shell and over 60% of the Fortune 500 — rely on the Databricks
Data Intelligence Platform to take control of their data and put it
to work with AI. Databricks is headquartered in San Francisco, with
offices around the globe, and was founded by the original creators of
Lakehouse, Apache Spark™, Delta Lake and MLflow.
To learn more, follow Databricks on LinkedIn, X and Facebook.




    Start your free trial


Contact us for a personalized demo at databricks.com/contact

To learn more about migration, visit databricks.com/migration




© Databricks 2024. All rights reserved. Apache, Apache Spark, Spark and
the Spark logo are trademarks of the Apache Software Foundation. Privacy Notice | Terms of Use
