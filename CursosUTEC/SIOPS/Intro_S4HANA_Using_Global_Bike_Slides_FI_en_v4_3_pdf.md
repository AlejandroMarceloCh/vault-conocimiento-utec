---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Slides_FI_en_v4.3
slides: 29
fuente: Intro_S4HANA_Using_Global_Bike_Slides_FI_en_v4.3.pdf
---

Financial Accounting (FI)
Curriculum: Introduction to S/4HANA using Global Bike
Teaching material - Information




       i                     Teaching material - Version

                               4.3 (July 2025)

                               Software used
                                  • S/4HANA 2023
                                  • Fiori 3.0
                               Model
                                  • Global Bike


                               Prerequisites
                                  •    No Prerequisites needed




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.          2
Module Information



                             Authors

                               Bret Wagner
                               Stefan Weidner
                               Babett Ruß



                             Target Audience

                               Beginner




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   3
Module Information



                             Learning Objectives

                              You are able to
                               define the central organizational structures of the FI module.
                               summarize the master data which is most important for the FI module.
                               explain a standard financial accounting process.
                               outline the basic functionalities of FI reporting.
                               recognize some of integration points to other SAP modules.




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                4
Agenda


 FI Organizational Structure

 FI Master Data

 FI Processes

 FI Reporting




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   5
Goal of Financial Accounting (FI)


 Financial Accounting is designed to collect the transactional data that provides a foundation for preparing the
  standard portfolio of reports.

 In general, these reports are primarily, but not exclusively, directed at external parties.

 Standard reports include:
  • Balance Sheet
  • Income Statement
  • Statement of Cash Flows




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                             6
Target Groups


 Internal                                                 External
  • Executives                                             • Legal Authorities
  • Senior Management                                      • Banks
  • Administrative Staff                                   • Auditors
  • Employees                                              • Shareholders
                                                           • Insurance
                                                           • Taxing Authorities
                                                           • Media
                                                           • Financial Analysts




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                           7
FI Organizational Structure


 Represents the legal and/or organizational view of a company

 Forms a framework that supports a company's financial decisions using the methods desired by management

 Allows the accurate and organized collection of business information

 Supports the development and presentation of relevant information to enable and support business decisions




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                        8
FI Organizational Structure


 Client
  • An independent environment in the system

 Company Code
  • Represents an independent legal accounting unit
  • Balanced set of books, as required by law, are prepared at this level.
  • A client may have more than one company code
       United States
       Germany
       United Kingdom
       Australia
       …                                                                              Liabilities &
                                                                             Assets
                                                                                      Owners Equity




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                9
FI Organizational Structure


 Chart of Accounts
  • A classification scheme consisting of a group of general ledger (G/L) accounts
  • Provides a framework for the recording of values to ensure an orderly rendering of accounting data
  • The G/L accounts it contains are used by one or more company codes.

 Credit Control Area
  • An organizational entity which grants and monitors a credit limit for customers.
  • It can include one or more company codes

 Business Area
  • An organizational unit that represents a separate area of operations or responsibilities within an organization and to which
    value changes recorded in Financial Accounting can be allocated
  • Financial statements can be created for business areas, and these statements can be used for various internal reporting
    purposes.




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                            10
Global Bike Structure for Financial Accounting


                                                             Global Bike                                  Client




                                                                                                      Company
                                     Global Bike Inc.                  Global Bike Germany GmbH          Code



                                                            Global Bike                                Chart of
                                                          Chart of Accounts                           Accounts



                                                                  Bikes                           Business Area




                                                           Global Credit Control                  Credit Control
                                                                                                           Area




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                            11
Global Bike Enterprise Structure in SAP ERP (Accounting)



                                                          Business Area – Bikes BI00




                                                                                                                 Company
                                              CC US00                 CC DE00                                       Code

                                         Chart of Accounts (global) GL00
                                     Credit Control Area (global) GL00
                                                                                                         Controlling Area
                                CA North Am. NA00                CA Europe EU00        CA Asia AS00        (see Controlling unit)

                                                                                                      Operating Concern
                          Operating Concern (global) GL00                                                 (see Controlling unit)

                         Client Global Bike

© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                             12
Agenda


 FI Organizational Structure

 FI Master Data

 FI Processes

 FI Reporting




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   13
FI Master Data


 General Ledger (G/L) Accounts
  • The unique combination of Company Code and Chart of Account creates a data storage area called a General Ledger.
  • The General Ledger contains a listing of the transactions effecting each account in the Chart of Accounts and the respective
    account balance.
  • It is utilized in the preparation of financial accounting statements.



 Customer and Vendor Master Data
  • Customer and vendor account balances are maintained in FI through fully integrated accounts receivable and accounts
    payable sub-ledgers.
  • Financial postings for customers and vendors are made directly to their respective individual accounts and accompanied by
    a concurrent automatic posting to the General Ledger.




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                      14
Customer Accounts


 Accounts Receivable Sub-Ledger (FI-AR)
  • Information with respect to customers who purchase the enterprise’s goods and services such as sales and payments
    made
  • Substantive and important integration between Sales and Distribution (SD) and Financial Accounting (FI)
  • Billings in SD generate FI journal entries for sales activity

                                       Customer 189       Customer 142
                                                                          Accounts Receivable
                                           100             300             (General Ledger)

                                                                              950
                                       Customer 135       Customer 123
                                           400             150



© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                 15
Vendor Accounts


 Accounts Payable Subledger (FI-AP)
  • Information with respect to Vendors from whom the enterprise purchases goods and services such as purchases and
    payments made
  • Substantive and important integration between Materials Management (MM) and Financial Accounting (FI)
  • Purchase and goods receipt activities in MM generate FI journal entries

                                     Vendor 100234              Vendor 100435   Accounts Payable
                                                          200           250     (General Ledger)

                                                                                          850
                                     Vendor 100621              Vendor 100846
                                                          100           300




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                               16
Agenda


 FI Organizational Structure

 FI Master Data

 FI Processes

 FI Reporting




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   17
FI Processes


 Posting a G/L Entry




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   18
Agenda


 FI Organizational Structure

 FI Master Data

 FI Processes

 FI Reporting




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   19
FI Reporting

   • G/L Account Summary




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   20

FI Reporting


 Balance Sheet
  •   Presentation of an organization’s Assets, Liabilities, and Equity at a point in time
  •   Assets: What the company owns
  •   Liabilities: What the company owes
  •   Equity: The difference between Assets and Liabilities
  •   Assets = Liabilities + Equity




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                      21
FI Reporting


 Balance Sheet Example




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   22
FI Reporting


 Income Statement
  •   Presentation of an organization’s revenues and expenses for a given period of time (e.g. monthly, quarterly, or yearly)
  •   Revenues, in a simple sense, are inflows of cash as a result of selling activities or the disposal of company assets.
  •   Expenses, in a simple sense, are outflows of cash or the creation of liabilities to support company operations.
  •   Revenues - Expenses = Net Income




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                         23
FI Reporting


 Income Statement Example




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   24
FI Reporting


 Statement of Cash Flows
  • Considers the associated changes, both inflows and outflows, that have occurred in cash – arguably the most important of
    all assets – over a given period of time (e.g. monthly, quarterly, or annually)




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                    25
Accountants and Audit Trails


 Audit trails allow an auditor to begin with an account balance on a financial statement and trace through the
  accounting records to the transactions that support the account balance.

 Audit trails enable an auditor to trace individual transactions to the effected account balance(s) on a financial
  statement.




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                               26
SAP Document Principle


 Each business transaction impacting FI writes data to the SAP database creating a uniquely numbered
  electronic document.

 The document number can be used to recall the transaction at a later date.

 It contains, for example, such critical and necessary information as:
  • Responsible person
  • Date and time of the transaction
  • Commercial content

 Once written to the SAP database, a financial document (one impacting the financial position of the company)
  can not be deleted from the database.

 It can be changed to some degree.

 The SAP document principle provides a solid and important framework for a strong internal control system – a
  requirement of law for companies that operate in most countries in the world.
© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                          27
SAP Document Principle




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   28
SAP FI Module


 Fully integrated with other SAP modules including, but not limited to:
  •   Sales and Distribution (SD)
  •   Materials Management (MM)
  •   Production Planning and Execution (PP)
  •   Managerial Accounting (CO)




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                    29

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
