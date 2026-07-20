---
curso: SIOPS
titulo: 1. Teoría Semana 3 -Financial Accounting II
slides: 14
fuente: 1. Teoría Semana 3 -Financial Accounting II.pdf
---

Financial
Accounting II
         Profesor: Carlos Villanueva Qwistgaard



                    IN3010 - Sistemas de Información para Operaciones
AGENDA
 01   INTEGRATION BETWEEN FI AND CO




 02   SAP S/4HANA FINANCE - SIMPLIFIED DATA
      MODEL




 03
      WORKING WITH BUSINESS PARTNERS
      AND INVOICES




                                              IN3010 - Sistemas de Información para Operaciones
Introduction

There is an integration between FI and CO




                                            IN3010 - Sistemas de Información para Operaciones
01
     FI and CO Integration
     Profitability or profit center accounting let us determine the profit/loss by
     profit center. You design the profit center and assign it to the respective
     objects that you want to capture.


     Cost Objects are: cost centers, internal orders, production orders, WBS
     elements, maintenance orders, activities.


     There are objects considered real objects: cost centers , profitability
     segments




01               IN3010 - Sistemas de Información para Operaciones
01
     FI and CO
     Integration
     The main task of FI is basically to post FI transactions,
     revenue and expenditures, legal reporting requirements.
     On the CO side, the main purpose is to capture costs,
     collect revenues or expenditures by areas of responsibility.
     We have objects created in FI (mainly G/L accounts),
     others created in CO (cost centers, internal orders,
     production orders, maintenance orders).




02                                                                  IN3010 - Sistemas de Información para Operaciones
01
     FI and CO
     Integration
     When we incur some kind of cost, it is captured by
     Cost Accounting




03                                                        IN3010 - Sistemas de Información para Operaciones
01
     FI and CO
     Integration
     On the FI side, we create expenditures,
     referred as costs. On the CO side, this costs
     are captured by a Cost Element.




04                                                   IN3010 - Sistemas de Información para Operaciones
01
     FI and CO
     Integration
     When we create a G/L account, we link it
     automatically to the primary cost element.
     Primary and secondary costs elements are
     created in FI but they live in CO.




05                                                IN3010 - Sistemas de Información para Operaciones
01
     FI and CO
     Integration
     Primary cost elements are stored in
     Management Accounting Master Data and then
     we have Financial accounting master data, in
     the form of G/L accounts




                                                    General Ledger (G/L) Accounts and Cost Elements




06                                                                     IN3010 - Sistemas de Información para Operaciones
Review


     when we are capturing our expenditures on the
     FI side, those same expenditures and
     revenues can be recorded on the CO side by
     way of my primary cost elements.




                      IN3010 - Sistemas de Información para Operaciones
02
     SAP S/4HANA Finance - Simplified Data Model

                                 • Universal journal is the basis of
                                   SAP’s integrated accounting system.


                                 • FI and CO are using one table.


                                 • Documents posted to the universal
                                   journal or general ledger documents,
                                   CO documents, asset documents,
                                   material management documents
                                   and profitability analysis

01                                   IN3010 - Sistemas de Información para Operaciones
02      SAP S/4HANA Finance - Simplified Data Model
     • FI – Finance Accounting
        • FI is intended for legal reporting. It can be used to draw up a balance sheet and
          an income statement at the level of accounting entities.
        • The level at which FI is needed is determined by law. Legal reporting is different
          for each country.
     • CO – Management Accounting
        • The purpose of Management Accounting is to collect revenue and expenses by
          areas of responsibility to be used for internal management reporting purposes.
        • Management Accounting analyzes costs and revenues at high levels across
          country boundaries. For example, it can analyze costs for all production
          departments worldwide.
        • Costs and revenues from FI are used in Management Accounting.
        • Management Accounting provides Controlling (CO) objects, which can represent
          areas of responsibilities that incur costs, revenues, or both, which allow an
          organization to track both costs and revenues internally.​


02                                                                IN3010 - Sistemas de Información para Operaciones
03
        Working with Business
        Partners and Invoices
     Any company that wishes to do business
     with a specific vendor has to create a
     company code segment. The company
     code data contains information such as the
     reconciliation account, terms of payment,
     payment methods, dunning data, or
     correspondence settings.




01
03
     Vendor Master Record — Business Partner
                          In SAP S/4HANA, Business Partner is the term
                          used to classify a natural person, group
                          (married couple, executive board) or
                          organization (legal person, parts of a legal
                          entity, maps any kind of situation in the day to
                          day business).


                          There is one point of entry to manage business
                          partners, customers and vendors.


                          In class, FI Vendor will be used for account

02
                          payables.
                                      IN3010 - Sistemas de Información para Operaciones

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
