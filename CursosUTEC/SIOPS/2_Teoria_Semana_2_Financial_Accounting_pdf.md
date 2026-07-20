---
curso: SIOPS
titulo: 2. Teoría Semana 2 -Financial Accounting
slides: 14
fuente: 2. Teoría Semana 2 -Financial Accounting.pdf
---

Financial
Accounting
         Profesor: Carlos Villanueva Qwistgaard.




                 IN3010 - Sistemas de Información para Operaciones
AGENDA
  01   INTRODUCTION




  02   FINANCIALACCOUNTING
       OVERVIEW




  03   MANAGEMENTACCOUNTING
       OVERVIEW
Introduction
The role of accounting processes is to record the
financial consequences of the various process
steps. In turn, the organization uses this financial
information to plan and manage these processes.
Financial Accounting
Overview
 Financials can be subdivided in two major parts:
 Financial Accounting (FI) and Management Accounting (CO).


 Financial Accounting has the task to meet legal requirements.


 The main tasks are as follows:
    Post all financial transactions, revenues, and expenses. Keep
    them unchanged in the system for reporting purposes.
    Allow the setting up of a profit and loss statement and a
    balance sheet to fulfill the legal requirements of a country or of a
    financial reporting standard.
Financial
Accounting
Financial Accounting is subject to legal requirements
of a country, and, in addition, to requirements of
certain financial reporting standards, such as US
Generally Accepted Accounting Principles (GAAP),
International Financial Reporting Standards (IFRS),
and Handelsgesetzbuch (HGB). The stakeholders of
such financial reportings are outside the
companies, for example, suppliers, banks, tax
government, and so on.
Financial
Accounting
The central task of General Ledger Accounting is to
provide a comprehensive picture of external
accounting and financial records.
The General Ledger (G/L) serves as a complete
record of all business transactions. The G/L is
managed at the company code level. All accounting-
relevant transactions made in other components, e.g.
Logistics (LO) or Human Resources (HR), are posted
in real time to FI by means of automatic account
determination. The aim of recording business
transactions is to create a balance sheet and
profit and loss (P&L) statement.
 Financial
 Accounting
The General Ledger (G/L) is the core of
Financial Accounting (FI).
The FI application component fulfills all the
international requirements that must be met
by the FI department of an organization.
FI focuses on General Ledger Accounting
and the processing of receivables (FI-AR),
payables (FI-AP), and Asset Accounting
(FI-AA).
Management
Accounting
Components
  CO contains all of the functions necessary for controlling cost and revenue
  effectively. It covers all aspects of management controlling and includes many tools for
  compiling information for company management.
Management Accounting
Management Accounting
Data that the system creates in other SAP S/4HANA applications can have a direct influence
on CO. For example, if you purchase a non-stock item, the system posts an expense to the
general ledger (G/L). The system also posts this expense as costs to the cost center for
which the item was purchased. This cost center can then pass these costs as overhead to a
production cost center.


FI, in the SAP S/4HANA application, is a primary source of data for CO. In fact,
most expense postings in the G/L result in a cost posting in CO. These expense postings
to the G/L can be journal postings, vendor invoices, or depreciation postings from Asset
Management.


Management Accounting provides information that management can use to make
decisions. It facilitates the coordination, supervision and optimization of all processes within
a company. This involves recording both the consumption of production factors and the
services provided by an organization.
Management Accounting

     Profitability Analysis analyzes the profit or loss of an organization
     according to individual market segments. In Profitability Analysis,
     costs are assigned to the revenues of each market segment. This
     gives you a basis for calculating prices, targeting customers,
     determining conditions, and choosing sales channels, for example.
     Sales order management is a primary source for revenue
     postings from billing documents to revenue postings in CO-PA
     and PCA. In addition to direct postings from FI, Profitability
     Analysis (CO-PA) can receive cost assessments from cost centers
     and ABC processes, settlements of costs from internal orders,
     and settlements of production variances from cost objects.
Management Accounting


     Within the Overhead Cost Controlling (CO-OM) area, you can
     post costs to cost centers, internal orders, and processes from
     other SAP S/4HANA applications (external costs). Cost centers
     can then allocate these costs to other cost centers, internal orders,
     and processes in Activity-Based Costing (ABC). ABC, in turn, can
     pass costs to cost centers and internal orders. Internal orders can
     settle costs to cost centers, processes in ABC, and other internal
     orders.
Management Accounting

     You use Cost Center Accounting for controlling purposes in your
     organization. Cost center accounting takes the costs incurred in a
     company and allocates them to the actual subareas that caused
     them.
     Cost centers are separate areas within a controlling area at which
     costs are incurred. You can create cost centers according to
     various criteria including functional considerations, allocation
     criteria, activities provided, or according to their physical location
     and/or management area.
Management Accounting

     An activity type defines the type of activity that can be provided
     by a cost center. Activity outputs supplied by one cost center (the
     sending cost center) to other cost centers, orders, or processes,
     represent the utilization of resources for this sending cost center.
     You valuate activities using a price calculated on the basis of
     certain business or management information.
     Internal orders are used to plan, collect, and analyze the
     costs arising from internal activities.
     SAP Human Capital Management (HCM) can generate cost
     postings in CO. SAP HCM allows you to allocate labor costs to
     various controlling objects. In addition, you can transfer and use
     planned personnel costs for planning in CO.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
