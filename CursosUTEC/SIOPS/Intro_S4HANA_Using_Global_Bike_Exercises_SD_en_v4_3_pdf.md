---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Exercises_SD_en_v4.3
slides: 17
fuente: Intro_S4HANA_Using_Global_Bike_Exercises_SD_en_v4.3.pdf
---

                                                                                   EXERCISE




             SD 1: Display Customer Master Data


  Exercise Use the SAP Fiori Launchpad to display a customer.                      Time 10 min
  Task Global Bike has several customers in the USA. Display one customer
  from the USA (Beantown Bikes).
  Name (Position) Maria Diaz (Sales Person 1 US East)


  To display a customer, in the Sales and Distribution space and the section                  Start

  Sales Person, locate and open the Manage Business Partner Master Data app.




  In the next screen, the SAP system expects you to enter a business partner
  number that is used to represent customers or suppliers.

  A business partner (BP) is an organization (firm, branch office), person, or a   Business Partner

  group of persons or organizations in which your company has a business
  interest.
  You can create and manage your business partners and their roles centrally in
  a company. For this purpose, you enter the general data of the BP once and
  assign business partner roles (BP roles) to them. For each BP role, specific
  data is stored. This general data is ‘independent’ of the role the partner
  performs in the different business processes in S/4HANA. This prevents data
  from being created and stored redundantly.
  Structure: For each BP, you specify a unique business partner number (BP
  number). You create and manage the following general elements of a BP:
        general data, e.g. name, address, and communication data
        identification data, e.g. industry, identification, and tax numbers
        status data, e.g. status of the business relationship




© SAP UCC Magdeburg                                                                        Page 1
                                                                                     EXERCISE

  During the course of the business relationship, the business partner can assume
  other business partner roles. When a partner appears in a new role, you only
  need to add their master data, as the general data remains unchanged.




  Since you do not know any business partner (and in our case a customer
  number) in the Global Bike company, you need to find one. In order to do so,
  in the Business Partner field click the input help icon    .

  Besides the input help, you can use the SAP ad-hoc help (F1) to have the
  system explain particular fields on the screen. The help differs depending on
  the app type (Fiori or SAP GUI for HTML).
  If you are using a native Fiori app, the Help Topics will open at the right edge      Help Topics
  of the screen and optionally, blue circles are appearing for specific terms.
  Either you can find further information in the help topics or you can click on
  one of the blue circles to open the corresponding help entry directly.




  On the other hand, if you are using an SAP GUI for HTML app, the
  Performance Assistant popup will appear, providing you with information
  about the currently selected field.




© SAP UCC Magdeburg                                                                        Page 2
                                                                                        EXERCISE




  Using the input help for business partners, you have the possibility to specify
  different search criteria. Since business partners also include persons, it is also
  possible to filter by first and last name.
  This time, please use the overall Search field. Enter an asterisk (*) followed
                                                                                                  *###
  by your three-digit number (###).




  Note Each time the curriculum material requests you to type in ###, please
  enter the three-digit number you received from your instructor. Since each
  participant receives his or her own master data, the three-digit number serves
  to distinguish between the individual data sets. Please remember that all
  participants work in the same Global Bike company and if you do not select
  any search criteria, you will see all master data (just like in a real company).

  Click      to start searching. A list of all business partners in your data set
  will be displayed. Scroll to the right in the results table to see the business
  partner names.




  Scroll through the list and select the business partner Beantown Bikes. Then,          Beantown Bikes

  click       , so apply the selection.




© SAP UCC Magdeburg                                                                            Page 3
                                                                                    EXERCISE




  The BP number will be displayed in the Business Partner field. Now click
  . The record of the business partner is displayed.




  Note The simplification of data structures is one of the major ideas of SAP
  S/4HANA. For this reason, various transactions, such as the management of
  debtors, creditors or contact persons, have been combined into one transaction
  (Manage Business Partner Master Data).

  Click on the dataset of your business partner. This screen displays the general
  data of your customer Beantown Bike. In the context of the SAP system, this
  data implies all information about the customer that are relevant for the whole
  company such as global names and the address. These can be viewed by
  different departments and do not differ. Click the other tabs in order to see
  further global data about Beantown Bikes.




© SAP UCC Magdeburg                                                                     Page 4
                                                                                        EXERCISE




  Please select the Roles tab. Via auto-scroll, you will be taken to the correct                   Roles

  position. There, you will see that two roles are assigned to the business partner:
  FI Customer and Customer. Within the Customer | (FLCU01) BP Role row,                Customer | FLCU01
  click    .




  Subsequently, click the Sales Areas tab to get information about the sales data            Sales Areas

  from your customer Beantown Bikes. Below the sales areas, you can see the
  company codes. This information could not be found in the general overview,
  because this data is linked to the customer role.




  Click on        to return to the SAP Fiori Launchpad.




© SAP UCC Magdeburg                                                                             Page 5
                                                                                  EXERCISE

             SD 2: Display Customer Order


  Exercise Use the SAP Fiori Launchpad in order to display a customer order.      Time 10 min
  Task Display a customer order for black Deluxe Touring Bikes.
  Name (Position) David Lopez (Sales Representative US East)


  In the Sales and Distribution space, find the section Sales Representative.             Start

  There, use the Manage Sales Orders – Version 2 app to display a sales order.




  In the Sales Order field, enter 1. Click    to search for the document for an              1

  already created sales order. The corresponding order will be displayed.




  The order number is the number that clearly identifies the sales document.
  Generally, there are different types of sales documents in the SAP S/4HANA
  System:
     -   Request
     -   Offer
     -   Order
     -   Master Contract
     -   Complaints




© SAP UCC Magdeburg                                                                    Page 6
                                                                                      EXERCISE




  To get more information click the line of the identified sales order. In the next
  screen, all details of the order placed by the company Beantown Bikes from
  Boston are displayed.

  By means of this sales document, you can observe the typical division of the
  sales documents. They are composed of
     -   Document header
     -   Document items.
  The document header consists of data that is valid for the complete sales
  document, whereas the document items reflect the data of the individual goods
  that are listed in the sales document.

  In the following screen, you can see the document header for the sales
  document with the number 1. As you can see, this sales order is listed under
  the Cust. Reference number Z998 and its net value amounts to $15,000.00.




  Note The purchase order number must not be confused with the number of the
  sales document, which in this case is the document of a standard order.
  Whereas the purchase order number can be assigned freely, the document
  number is generated automatically while compiling the document.




© SAP UCC Magdeburg                                                                       Page 7
                                                                                       EXERCISE


  In the Items overview, you can see that the order only contains the product
  Deluxe Touring Bike (black). Beantown Bike ordered five of these bicycles.




  Now, in the line with the Deluxe Touring Bike (black) click on         to navigate
  to the details page. There, click on the Prices tab to display all the conditions.

  This screen shows that each bicycle costs 3,000.00 USD and that neither
  discounts nor supplements were determined. It furthermore shows that Global
  Bikes makes a profit of 1,600.00 USD per bicycle sold.




  Click on        to return to the SAP Fiori Launchpad.




© SAP UCC Magdeburg                                                                        Page 8
                                                                                         EXERCISE


              SD 3: Display Outbound Delivery Document for Sales Order


  Exercise Use the SAP Fiori Launchpad to display an outbound delivery.                  Time 10 min
  Task In the context of the sales order process, after creating the order, the
  outbound delivery takes place. As a next step, please display the outbound
  delivery document.
  Name (Position) Sergey Petrov (Warehouse Employee)


  In the space Sales and Distribution and the section Warehouse Employee, use                    Start

  the Manage Outbound Deliveries app to display an outbound delivery
  document for a sales order.




  The app might start with a collapsed header area. If so, please expand it by
  clicking on     (Expand Header). Change the Overall Status to All and click                      All
      . You can see different deliveries. Please note, it is possible that your screen
  differs from the following screenshot.




  Click directly on the outbound delivery number 80000000. A context menu                    80000000

  pops up. There, please click on the outbound delivery number 80000000 again
  to view the follow-up document of the sales order introduced in the previous
  step.




© SAP UCC Magdeburg                                                                           Page 9
                                                                                   EXERCISE




  You can see the overall status (“Completed”) and the delivery date. For more
                                                                                  General Information
  information, such as weight and picking status, see the General Information
  tab.




  Scroll to the Process Flow section. There you can see all relevant documents,         Process Flow

  including the sales order of the previous step.




© SAP UCC Magdeburg                                                                        Page 10
                                                                                    EXERCISE


  Afterward, please select the Items tab. Recognize the first line (Item 10) with          Items

  the 5 ordered bicycles.




  Click anywhere on this item line to get a more detailed view.




  Click on       to return to the SAP Fiori Launchpad.




© SAP UCC Magdeburg                                                                     Page 11
                                                                                    EXERCISE


              SD 4: Display Billing Document


  Exercise Use the SAP Fiori Launchpad in order to display billing                   Time 5 min
  documents.
  Task After the delivery of the bicycles to the customer, an invoice was created
  for the customer. Display the billing document in the system.
  Name (Position) Stephanie Bernard (AR Accountant)


  In the space Sales and Distribution and in the section AR Accountant, open the            Start

  Manage Billing Document app to display a billing document.




  In the Billing Document field, enter 90000001 to display the billing document         90000001

  for the corresponding sales order. Select    .




  Note If you see only one column in the display, e.g. Status, please exit the
  app by clicking on        and reopen it or click on    to show more columns
  using the settings.

  Afterward, click on the line with the billing document 90000001 to open the
  details.

  You will be forwarded to your billing document. As you can see, this billing
  document represents a claim for payment of 15,000.00 USD for Beantown
  Bikes.



© SAP UCC Magdeburg                                                                     Page 12
                                                                                     EXERCISE




  Select the Pricing Elements tab. You will see a list of all the items that are     Pricing Elements

  going into the net value, including the internal price of 1,400.00 USD per bike,
  which represents costs for Global Bike. At the top, there is the price of
  3,000.00 USD, which includes the profit share. In addition to the individual
  amounts, all amounts are also calculated on the total quantity of the order.




  Click on       to return to the SAP Fiori Launchpad.




© SAP UCC Magdeburg                                                                        Page 13
                                                                                           EXERCISE


              SD 5: Analyze Document Flow


  Exercise Use the SAP Fiori Launchpad in order to view the Document Flow.                  Time 15 min
  Task There are various possibilities to display the Document Flow. It is
  possible to open it directly from sales order document.
  Name (Position) David Lopez (Sales Representative US East)


  SAP provides a Document Flow tool that tracks the entire sales transaction                  Document Flow

  process from beginning to end. The Document Flow tool is extremely
  powerful because it can be used at any point in the sales order process. It
  provides an audit trail (booking control) for the sales order and all follow-up
  documents chronologically. Furthermore, it is possible to navigate into these
  documents and to display them in detail (drill down).


  In the space Sales and Distribution and in the section Sales Representative,                         Start

  use the Manage Sales Orders – Version 2 app to analyze the Document Flow.




  On the overview screen, in the Sales Order field enter 1 and click        .                             1




  The sales order is displayed in the results list. Among other things, it can be
  seen that the order is already Completed (cf. Overall Status). Please do not
  switch to the detailed view (clicking on the line) but click directly on the order
  number within this line to open the context menu. There, select       . In
  the Define Link List pop-up screen that opens, you can launch the Display
  Document Flow – Sales Order app. The following screenshot shows the                  Display Document Flow
  clicking path.


© SAP UCC Magdeburg                                                                                Page 14
                                                                                   EXERCISE




  The Display Document Flow app opens and the sales document 1 is already
  preselected. Two document flows are displayed: One is the Operational
  Document Flow and the other is the G/L Document Flow.




  With the help of this document chain, complex relationships can be
  recognized. For a better overview, you have the possibility to expand/collapse
  groups, or to Zoom In/Out/Fit the view to the window size in the right screen
  area. By clicking    , you can also fade in a legend.




  When you select a document from the Operational Document Flow, all G/L
  documents associated with it are also highlighted. For example, from the


© SAP UCC Magdeburg                                                                    Page 15
                                                                                      EXERCISE

  Logistics group, please select the Goods Issue Document. The following          Goods Issue Document
  screenshot shows the result.




  The corresponding posting document from the general ledger is outlined in
  blue. Important information about the documents can be taken directly from
  the overview. You can use the settings in the right-hand screen area ( ) to
  show or hide additional information about the general ledger documents.

  In addition, you can display the associated T-Accounts for one or more G/L
  documents. If the G/L documents are correctly marked, you can call up the
  desired view with the help of the                button.




  On the Display Journal Entries –In T-Account View screen, you can now view
  the accounting impact. As you may already know, the focus is on balance sheet
  accounts and profit and loss accounts. The T-Accounts visualize the posting



© SAP UCC Magdeburg                                                                          Page 16
                                                                                   EXERCISE

  principle “debit to credit”. After you had a look at the postings, select   in
  the upper screen area to return to the document flow.

  For more details, you can access any document from the document flow. For
  example, to view the invoice, select it and click the button (Details) that
  appears. The already familiar context menu will open. Select the Manage           Manage Billing
  Billing Documents app.                                                              Documents




  If an error message appears, please ignore it. On the Manage Billing
                                                                                     Process Flow
  Documents screen, you can see all details of the corresponding invoice.
  Finally, choose the Process Flow tab. There you will find an alternative
  document chain.




  Click on       to return to the SAP Fiori Launchpad.




© SAP UCC Magdeburg                                                                     Page 17
