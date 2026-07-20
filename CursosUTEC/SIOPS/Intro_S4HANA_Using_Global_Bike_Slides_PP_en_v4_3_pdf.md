---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Slides_PP_en_v4.3
slides: 59
fuente: Intro_S4HANA_Using_Global_Bike_Slides_PP_en_v4.3.pdf
---

Production Planning and Execution (PP)
Curriculum: Introduction to S/4HANA using Global Bike
Teaching material - Information




       i                     Teaching material - Version

                               4.3 (July 2025)

                               Software used
                                  • S/4HANA 20223
                                  • Fiori 3.0
                               Model
                                  • Global Bike


                               Prerequisites
                                  •    No prerequisites needed




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

                               Understand a manufacturing process cycle
                               Get familiar with the basics of a production plan




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                             4
Functionality


 SAP divides production into multiple processes

  • Production Planning

  • Manufacturing Execution
       Discrete Manufacturing
       Repetitive Manufacturing
       KANBAN

  • Production – Process Industries
       Integrated planning tool for batch-orientated process manufacturing
       Design primarily for chemical, pharmaceutical, food and beverage industries along with batch-oriented electronics




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                     5
Unit Overview


 PP Organizational Structure

 PP Master Data

 PP Processes
  • Material Planning
  • Production Planning
  • Manufacturing Execution Process




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   6
PP Organizational Structure

 Client
  • An independent environment in the system

 Company Code
  • Smallest org unit for which you can maintain a legal set of books

 Plant
  • Operating area or branch within a company
          Manufacturing, distribution, purchasing or maintenance facility

 Storage Location
  • An organizational unit allowing differentiation between the various stocks of a material in a plant

 Work Center Locations (in SAP system  master data)
  •       An organizational unit that defines where and when an operation is performed
  •       Has an available capacity
  •       Activities performed are valuated by charge rates, which are determined by cost centers and activity types.
  •       Can be machines, people, production lines or groups of tradespeople

© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                 7
Global Bike Structure for Production Planning

                                                                     Global Bike                                              Client




                                                                                                                           Company
                                      Global Bike Inc.                         Global Bike Germany GmbH                       Code



                                            Dallas                                    Heidelberg                               Plant


                                                   Raw Materials                            Raw Materials

                                                   Semi-fin. Goods                          Semi-fin. Goods
                                                                                                                            Storage
                                                                                                                           Location
                                                   Finished Goods                           Finished Goods

                                                   Miscellaneous                            Miscellaneous

                                               Assembly                                 Assembly

                                               Packaging                                Packaging             (Work Center Location)

                                               Inspection                               Inspection



© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                8
GBI Enterprise Structure in SAP ERP (Logistics)

                                Shipping Point                   DL00      MI00        SD00          TO00               HD00         HH00               PE00

                                                            RM00         TG00        TG00       TG00                   RM00     TG00               TG00
                                Storage                    SF00         FG00      FG00         FG00                SF00        FG00               FG00
                                Location
                                                          FG00      MI00        MI00          MI00               FG00         MI00               MI00
                                                     MI00                                                       MI00

                                                                  Central Purchasing Organization (global) GL00
                                               Purchasing Org. US00                    CA00                 PO DE00                     AU00

                                            Purchasing Group North America                               PGr Europe                    Asia
                                                        N00                                               E00                         A00




                                  Dallas       Miami       S. Diego        Toronto            Heidelb.   Hamburg              Perth                     Plant
                                 DL00         MI00         SD00           TO00                HD00       HH00                 PE00
                          CC US00                                       CA00                CC DE00                       AU00                Company Code

                         Client GBI

© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                                         9
Unit Overview


 PP Organizational Structure

 PP Master Data

 PP Processes
  • Material Planning
  • Production Planning
  • Manufacturing Execution Process




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   10
PP Master Data


 Material

 Bill of Materials (BOM)

 Routing
  • BOM and routing are like a cooking recipe
  • BOM = ingredients
  • Routing = steps in the recipe

 Work Center

 Product Group




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   11
Material Master Record




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   12
Bill of Materials (BOM)


 List of components that make up a product or assembly

 Wheel Assembly                                             Seat Kit
  •   Tire
                                                             Handle Bar
  •   Tube
  •   Wheel                                                  Pedal Assembly
  •   Hex Nut                                                Chain
  •   Lock Washer                                            Brake Kit
  •   Socket Head Bolt
                                                             Warranty Document
 Frame                                                      Packaging

 Derailleur Gear Assembly




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                           13
Bill of Materials (BOM)


 Single-Level
                                                                                            Single-Level

                                                                         Finished Bike

                                                          Wheel Assembly         Pedal Assembly

                                                              Frame                      Chain
                                                           Derailleur Gear
                                                                                    Brake Kit
                                                             Assembly

                                                              Seat Kit            Warranty Doc.

                                                            Handle Bar              Packaging




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                    14
Bill of Materials (BOM)


 Single-Level vs. Multi-Level                                                                                                          Single-Level

                                                                                           Finished Bike
                                                          Single-Level


                                                          Wheel       Frame Derailleur Seat Handle Bar   Pedal   Chain   Brake   Doc.     Pack.

                                                               Tire

                                                               Tube

                                                              Wheel

                                                             Hex nut

                                                               Lock

                                                               Bolt
                                                                                                                                          Multi-Level



© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                                 15
Bill of Materials (BOM)


 Variant Bill of Materials (BOM)
  • Several products with a large proportion of identical parts.
                                                                              Single-Level

                                                          Deluxe Bike (red)                                      Single-Level

                                                                                         Professional Bike (black)
                                     Aluminum Wheel                  Pedal Assembly
                                                                                 Carbon Wheel           Pedal Assembly
                                           Frame red                     Chain
                                                                                  Frame black                Chain
                                      Derailleur Gear
                                                                        Brake Kit
                                        Assembly                                Derailleur Gear
                                                                                                           Brake Kit
                                                                                   Assembly
                                             Seat Kit                 Warranty Doc.
                                                                                    Seat Kit             Warranty Doc.
                                          Handle Bar                   Packaging
                                                                                  Handle Bar              Packaging


© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                         16
BOM – Item Categories


 An object that defines items in a BOM according to criteria, such as the object type of the component, for
  example, material master record or document info record.

 The item category controls the following:
  •   Screen sequence
  •   Field selection
  •   Default values
  •   Material entry
  •   Inventory management
  •   Subitems

 Item Categories
  •   Stock item
  •   Non-stock item
  •   Variable material – Sheet of steel
  •   Document item
  •   Text item
© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                        17
Routing


 Routings enable the planning of the production of        Example: Routing – Operation 20
  materials (products)                                     • Attach seat to frame
                                                           • Work Center – ASSY1000: Assembly Work Center
 Routings are used as a template for production orders    • Time: 1 minute
  and run schedules

 Routings are also used as a basis for product costing

 Series of sequential steps (operations) that must be
  carried out to produce a given product

 Routings contain:
  • What, Where, When, How




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                     18
Routing


 Routing for Finished Bike

           Operation                                         Plant
                                                                                              Description              Activity Type - unit in a controlling area
                                Work Center                                                                             that classifies the activities performed in a cost
                                                                                                                       center. Examples in production cost centers are
                                                                                                                                machine hours or finished units.




                                                          Control Key - key that specifies
                                                          how an operation or a sub-operation is
                                                          processed in functions such as orders,
                                                                                                            Time and Unit of Measure
                                                              costing or capacity planning.


© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                                                  19
Work Center

 A location within a plant where Value-added work (operations or activities) is performed
  • Work Centers can represent
          People or Groups of people
          Machines or Groups of machines
          Assembly Lines

 Work Center used to define capacities
  •       Labor
  •       Machine
  •       Output
  •       Emissions

 Capacities used in
  • Capacity requirements planning (CRP)
  • Detailed scheduling
  • Costing




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                      20

Work Center

 Work Centers capture and use the following Resource related data

  • Basic Data
       Person Responsible, Location of Work Center

  • Scheduling Information
       Queues and Move Times (interoperation), Formula Keys

  • Costing Data
       Cost Center, Activity Types

  • Personnel Data
       People, Positions, Qualifications

  • Capacity Planning
       Available Capacity, Formulas, Operating Time

  • Default Data
       Control Key, Standard Text Key
© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.              21
Product Group


 Aggregate planning that groups together materials or other product groups (Product Families)

 Multi- or Single-Level Product Groups
  • The lowest level must always consist of materials




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                          22
PP Processes


 Production Planning & Execution
  •   Forecasting
  •   Sales and Operations Planning (SOP)
  •   Demand Management
  •   Master Production Scheduling (MPS)
  •   Material Requirement Planning (MRP)

 Production Order




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   23
Production Planning & Execution

                                                            SIS              Forecasting               CO/PA


                                                                          Sales & Operations
                                                                               Planning
                                                                                                     Strategic Planning

                                                                              Demand
                                                                             Management

                                                                                                      Detailed Planning
                                                                                MPS



                                                                                MRP



                                                          Manufacturing                             Procurement
                                                           Execution                                  Process


                                                             Order
                                                           Settlement
                                                                                               Manufacturing Execution

© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                   24
Production Planning & Execution


 Players in the Game                                            SIS              Forecasting          CO/PA


  • Strategic Planning                                                         Sales & Operations          Strategic
                                                                                    Planning               Planning
       CEO, COO, CIO, CFO, Controller, Marketing Director

  • Detailed Planning                                                             Demand
                                                                                 Management
       Line Managers, Production Scheduler, MRP Controller,
        Capacity Planners
                                                                                                             Detailed
                                                                                     MPS
                                                                                                             Planning
  • Execution
       Line Workers, Shop Floor Supervisors
                                                                                     MRP



                                                               Manufacturing                        Procurement
                                                                Execution                             Process


                                                                  Order                                Manufacturing
                                                                Settlement                                Execution

© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                 25
Forecasting


 Forecasting is the foundation of a reliable SOP

 Accurate forecasts are essential in the manufacturing sector

 Overstocked & understocked warehouses result in the same
  issue: A loss in profits.

 Forecasts are ALWAYS WRONG




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.          26
Forecasting


 Forecasting Models
  •   Trend
  •   Seasonal
  •   Trend and Seasonal
  •   Constant

 Selecting a Model
  • Automatically
  • Manually




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   27
Sales and Operations Planning (SOP)


 Information Origination
  •   Sales
  •   Marketing
  •   Manufacturing
  •   Accounting
  •   Human Resources
  •   Purchasing

 Intra-firm Collaboration
  • Institutional Common Sense




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   28
Sales and Operations Planning (SOP)


 Flexible forecasting and planning tool

 Usually consists of three layers:
  • Sales Plan
  • Production Plan
  • Rough Cut Capacity Plan

 Planned at an aggregate level in time buckets




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   29
Demand Management


 The planning of requirement quantities and requirement dates for finished products and important assemblies

 Definition of the strategy for planning and producing or procuring a finished product

 Link between Strategic Planning (SOP) & Detailed Planning (MPS/MRP)

 Demand management can be done manually or based on previous planning results such as sales planning,
  SOP, and forecast.

 The results of Demand Management is called the Demand Program, it is generated from our independent
  requirements - PIR - Planned Independent Requirements and CIR - Customer Independent Requirements




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                         30
Demand Management



                                        Forecast                                                    Sales

                                                             Planned                    Customer
                                                           Independent                Independent
                                                          Requirements               Requirements



                                                                         Demand
                                                                         Program




                                                                         MPS / MRP




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                     31
Planning Strategies


 Planning strategies represent the business procedures for
  • The planning of production quantities
  • Dates

 Wide range of strategies

 Multiple types of planning strategies based upon environment
  • Make-To-Stock (MTS)
  • Make-To-order (MTO)
       Driven by sales orders
  • Configurable materials
       Mass customization of one
  • Assembly orders




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.          32
Planning Strategies for Make-to-Stock and Make-to-Order


Make-to-Stock                                             Make-to-Order

 Planning takes place using Independent                   Planning takes place using Customer Orders
  Requirements
                                                           Sales are covered by make-to-order production
 Sales are covered by make-to-stock inventory

 Strategies                                               Strategies
  •   10 – Net Requirements Planning                       • 20 – Make to Order Production
  •   11 – Gross Requirements Planning                     • 50 – Planning without Final Assembly
  •   30 – Production by Lot Size                          • 60 – Planning with Planning Material
  •   40 – Planning with Final Assembly




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                     33
Master Production Scheduling (MPS)


 MPS allows a company to distinguish planning methods between materials that have a strong influence on profit
  or use critical resources and those that do not




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                      34
Material Requirement Planning (MRP)


 In MRP, the system calculates the net requirements while considering available warehouse stock and scheduled
  receipts from purchasing and production

 During MRP, all levels of the bill of material are planned

 The output of MRP is a detailed production and/or purchasing plan

 Detailed planning level
  • Execute primary functions
  • Monitor inventory stocks
  • Determine material needs
       Quantity
       Timing
  • Generate purchase or production orders




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                     35
Demand-Independent vs. Dependent


 Independent Demand – Original source of the demand.
  • Independent demand is demand for a finished product, such as a computer, bicycle, or pizza.

 Dependent Demand – Source of demand resides at another level.
  • Dependent demand, on the other hand, is demand for component parts or subassemblies. For example, this would be the
    microchips in the computer, wheels on the bicycle, or cheese on the pizza




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                              36
Material Requirement Planning (MRP)


 MRP is used to ensure the availability of materials based on the need generated by MPS or the Demand
  Program

  • 5 Logical Steps
       Net Requirements Calculation
       Lot Size Calculation
       Procurement Type
       Scheduling
       BOM Explosion




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                  37
Net Requirements



                                                    Procurement
                                                                   Shortage
                                                      Proposal

                                                 Firmed Receipts               Requirements –
                                                                              Planned Ind. Req.,
                                                                                 Reservations
                                                  Firmed Orders
                                                                                Sales Orders,
                                                   or Purchase
                                                                                     Etc.
                                                   Requisitions


                                                          Stock
                                                                                Safety Stock



© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                            38
Lot sizing


 Static
  • Based on fixed values in the Material Master

 Periodic
  • Groups net requirements together from multiple periods

 Optimized
  • Calculates the optimum lot size for a several periods of net requirements




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                         39
Procurement Type


 External Procurement
  • Purchase Requisition
  • Purchase Order
  • Schedule Line

 Internal Procurement
  • Planned Order
  • Production Order
  • Process Order




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   40

Multi-Level Scheduling

                                                                                                       Required
                                                          Planned Order                                  Date

                                                          Purchase Requisition

                                                                                         Finished Product


                                                                          Assembly 1
                                                                    Semi-Finished Good


                                             Raw Material

                                              Component




                                                                                                                  Time
© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                  41
MRP vs. Consumption-Based


 Whether or not a material is planned using MRP or Consumption Based is determined by the MRP Type on the
  MRP1 screen of the Material Master




                                                            MRP      Consumption Based

                                                          PD – MRP   VB – Reorder-Point
                                        VSD – Seasonal MRP           VV – Forecast Based
                                                                     RP – Replenishment



© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                  42
Consumption-Based




                                                                               Lot
                                                                               Size
                                        Reorder
                                         Point




                                                          Safety Stock

                                                                         Replenishment
                                                                           Lead Time


© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                  43
Output of MRP


                                                             MRP
                                            In-House                             External
                                                          Planned Order
                                           Production                          Procurement


                                                           Convert to

                                            Production                     Purchase
                                              Orders                      Requisitions

                                              Process                      Purchase      Schedule
                                              Orders                        Orders        Lines




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                             44
Orders, orders, orders


 Planned Order (planning)
  • A request created in the planning run for a material in the future (converts to either a production or purchase order)

 Production Order (execution)
  • A request or instruction internally to produce a specific product at a specific time

 Purchase Order (execution)
  • A request or instruction to a vendor for a material or service at a specific time




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                      45
Manufacturing Execution Process

                                                            Capacity
                                          Production        Planning    Schedule
                                           Proposal                    and Release
                                       (Planning/Other)

                                                                                  Shop Floor
                                                                                  Documents

                                                Order
                                              Settlement
                                                                                      Goods
                                                                                      Issue
                                                           Goods
                                                           Receipt     Completion
                                                                       Confirmation

© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                        46
Production Order


 Production orders are used to control production operations and associated costs
  • Production orders define the following
       Material produced
       Quantity
       Location
       Timeline
       Work involved
       Resources used
       Cost settlement




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                              47
Production Order

                                                          Components

                               How



                              What


                       How many




                                                                       Timeline




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                           48
Schedule


 Calculates the production dates and capacity requirements for all operations within an order

  • Determines a Routing
       Operation specific timelines
       Material Consumption Points

  • Material Master
       Scheduling Margin Key (Floats)

  • Work Center
       Formulas
       Standard Inter-operation Times




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                          49
Release


 Two release processes
  • Header Level
       Entire order and all operations are released for processing, order is given a REL status
  • Operation Level
       Individual operations within an order are released
       Order is given a PREL status
       Not until the last operation is released does the order obtains a REL status

 Automatic vs. manual




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                            50
Availability Check


 Automatic check to determine whether the component, production resource tools, or capacities in an order are
  available
  • Can be automatic or manually executed
  • Determines availability on the required date

 Generates an availability log
  • Displays results of the check
  • Missing parts list
  • Reservations that could not be verified




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                          51
Schedule & Release


 The time between scheduling and releasing an order is used for company checks and any preparation needed
  for the processing of the order

 Once an order has been released it is ready for execution, we can at this time
  • Print shop floor documents
  • Execute goods movements
  • Accept confirmations against the order




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                      52
Shop Floor Documents


 Shop Floor Documents are printed upon release of the Production Order, examples would be:

  • Operation-based Lists
       Time Tickets, Confirmation Slips

  • Component-based Lists
       Material Withdrawal Slips, Pull List (consumption list)

  • PRT Lists
       Overview of PRT's used with their respective operations

  • Multi-Purpose Lists
       Operation Control Ticket, Object Overview




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                       53
Material Withdrawal


 When a production order is created it references a BOM to determine the necessary components to produce the
  material

 It then places a reservation on each of the components

 Upon release of the order (or operation) you can withdraw the reserved materials from inventory
  • Reservation is updated
  • Inventory is updated
  • Costs are assigned to the order as actual costs




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                    54
Confirmations

 Confirmations are used to monitor and track the progression of an order through its production cycle
  • Confirmation can be done at the operation or order level

 Exact confirmation shortly after completion of an operation is essential for realistic production planning and
  control

 Data that needs confirmation include
  •   Quantities – yield, scrap, rework
  •   Activity data – setup time, machine time
  •   Dates – setup, processing, teardown started or finished
  •   Personnel data – employee who carried out the operation, number of employees involved in the operation
  •   Work center
  •   Goods movements – planned and unplanned
  •   Variance reasons
  •   PRT usage




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                            55
Goods Receipt


 Acceptance of the confirmed quantity of output from the production order into stock

  • Effects of the Goods Receipt
       Updates stock quantity
       Updates stock value
       Changes price stored for future valuation
       Updates production order

  • Three documents are created
       Material document
       Accounting document
       Controlling document




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                 56
Order Settlement

 Consists of settling the actual costs incurred in the order to one or more receiver cost objects
  • Receivers could include: a material, a cost center, an internal order, a sales order, a project, a network, a fixed asset

 Parameters for Order Settlement
  • Settlement Profile
       Specifies the receivers, distributions rules and method
  • Settlement Structure
       Determines how the debit cost elements are assigned to the settlement cost elements

 Settlement Rule
  • Automatically assigned on creation of order, the parameters are used to define this rule
       Has one or more distribution rule assigned to it
       Distribution rules define: cost receiver, settlement share, settlement type




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                         57
Order Settlement


 Settling a Production Order to Stock
  • Debit posting is made to the Production Order with the value of the material *
  • Difference between the debt posting and credit posting is posted to a price difference account




                                           Material       Prod. Order                    Price Diff.

                                          80                     100                     20




                                                           * Material Price is determined by the quantity produced
                                                           times the Standard Price in the Material Master.



© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                              58
Order Settlement


 Costs analyzed
  • Primary
       Materials
       External Processing
  • Secondary
       Production, Material, and Administrative Overhead
       Labor

 Cost Analysis Reporting
  • Calculate and analyze planned costs, target costs, and actual costs of the production order.
  • Calculate and analyze variances




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                            59

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
