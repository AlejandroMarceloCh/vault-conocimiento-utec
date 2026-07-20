---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Slides_QM_en_v4.3_VF
slides: 29
fuente: Intro_S4HANA_Using_Global_Bike_Slides_QM_en_v4.3_VF.pdf
---

Quality Management (QM)
Curriculum: Introduction to S/4HANA using Global Bike
Teaching material - Information



       i                     Teaching material - Version

                              ▪ 4.3 (June 2025)

                              ▪ Software used
                                  • SAP S/4HANA 2023
                                  • Fiori 3.0
                              ▪ Model
                                  • Global Bike


                              ▪ Prerequisites
                                  •    No Prerequisites needed




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.          2
Module Information



                             Authors

                              ▪ Tim Böttcher
                              ▪ Babett Ruß




                             Target Audience

                              ▪ Beginner




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   3
Module Information



                             Learning Objectives

                              You are able to
                              ▪ name functionalities of the QM module.
                              ▪ define the central organizational structures of the QM module.
                              ▪ summarize the master data which is most important for the QM module.
                              ▪ explain a standard QM process.




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                4
Functionality


▪ Quality Planning                                        ▪ Control in Logistics

▪ Quality Inspection                                      ▪ Archiving

▪ Quality Control                                         ▪ Data Transfer

▪ Quality Certificates

▪ Quality Notifications

▪ Test Equipment Management

▪ Inspection Using Multiple Specifications

▪ Stability Study



© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                            5
Unit Overview


▪ QM Organizational Structure

▪ QM Master Data

▪ QM Processes




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   6
QM Organizational Structure

▪ Client
  • An independent environment in the system

▪ Company Code
  • Smallest org unit for which you can maintain a legal set of books

▪ Plant
  • Operating area or branch within a company
    −   Manufacturing, distribution, purchasing or maintenance facility

▪ Storage Location
  • An organizational unit allowing differentiation between the various stocks of a material in a plant




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                   7
QM Organizational Structure


▪ Purchasing Organization
  • The buying activity for a plant takes place at the purchasing organization
  • Organization unit responsible for procuring services and materials
  • Negotiates conditions of the purchase with the vendors

▪ Purchasing Group
  • Key that represents the buyer or group of buyers who are responsible for certain purchasing activities
  • Channel of communication for vendors




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                      8
Global Bike Structure for Quality Management


                                                                            Global Bike                                               Client




                                                                                                                                    Company
                                         Global Bike Inc.                                 Global Bike Germany GmbH                     Code




                                Dallas                    San Diego         Miami              Heidelberg         Hamburg              Plant


                                   Raw Materials           Trading Goods      Trading Goods     Raw Materials      Trading Goods
                                                                                                                                     Storage
                                   Semi-fin. Goods         Finished Goods     Finished Goods    Semi-fin. Goods    Finished Goods   Location
                                   Finished Goods          Miscellaneous      Miscellaneous     Finished Goods     Miscellaneous

                                   Miscellaneous                                                Miscellaneous




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                        9
Global Bike Enterprise Structure in SAP ERP (Logistics)

                                Shipping Point                   DL00      MI00        SD00          TO00               HD00         HH00               PE00

                                                             RM00        TG00        TG00       TG00                   RM00     TG00               TG00
                                Storage                    SF00         FG00      FG00         FG00                SF00        FG00               FG00
                                Location
                                                          FG00      MI00        MI00          MI00               FG00         MI00               MI00
                                                      MI00                                                      MI00

                                                                  Central Purchasing Organization (global) GL00
                                               Purchasing Org. US00                    CA00                 PO DE00                     AU00

                                            Purchasing Group North America                               PGr Europe                    Asia
                                                        N00                                               E00                         A00




                                  Dallas       Miami       S. Diego        Toronto            Heidelb.   Hamburg              Perth                     Plant
                                 DL00         MI00         SD00           TO00                HD00       HH00                 PE00
                          CC US00                                       CA00                CC DE00                      AU00                 Company Code

                         Client Global Bike

© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                                         10
Agenda


▪ QM Organizational Structure

▪ QM Master Data

▪ QM Processes




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   11
Customer Master Data


▪ Customer Master
  • Contains all of the information necessary for processing
    orders, deliveries, invoices and customer payment
  • Every customer MUST have a master record

▪ Created by Sales Area
  • Sales Organization
  • Distribution Channel
  • Division




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.        12
Customer Master Data


▪ The customer master information is divided into 3 areas:
  • General Data
  • Company Code Data
  • Sales Area Data




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.      13
Material Master Data


▪ Material Master

  • Contains all the information a company needs to manage about a material

  • It is used by most components within the SAP system
    −   Sales and Distribution
    −   Materials Management
    −   Production
    −   Plant Maintenance
    −   Accounting/Controlling
    −   Quality Management

  • Material master data is stored in functional segments called Views




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                       14
Material Master Views



                                                                  Sales Data

                                                Basic Data                        Purchasing Data

                                                                                        Mat. Plan. Data

                                                                Material Master             Forecasting Data

                                                                                          Storage Data

                                             Controlling Data                       Quality Data

                                                                Accounting Data




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                        15
Material Master

                                                          General Information relevant for the entire organization:

                                                                                                           Name
                                                                                                           Weight
                                                                                Client XXX                 Unit of Measure




                       Sales specific information:                                         Storage Location specific information:

                                                                              Delivering Plant                                      Stock Qty
                                                                              Loading Grp
                                           Sales Org. UW00                                           Storage Loc. FG00


                                                      Sales Org. UE00                                       Storage Loc. TG00




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                         16
Vendor Master Data


▪ Vendor Master
  • Contains all the necessary information needed to business with an
    external supplier
  • Used and maintained primarily by the Purchasing and Accounting
    Departments
  • Every vendor MUST have a master record




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                 17
Vendor Master Views


▪ Client Level
  • Address
  • Vendor Number
  • Preferred Communication
                                                               General Data

▪ Company Code Data
  • Reconciliation Account
  • Terms of Payment                                        Company Code Data
  • Bank Account                                          Financial Accounting (FI)
▪ Purchase Org Data
  • Purchasing Currency
  • Salesman’s Name                                         Purchasing Data
  • Vendor Partners                                        Materials Mgmt (MM)


© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                               18
Vendor Master

                                                          General Information relevant for the entire organization:


                                                                                                    Name
                                                                                                    Address
                                                                          Client XXX                Communication




                      Company Code specific information:                              Purch. Organization specific information:

                                                                          Acc. Mgmt                                        Incoterms
                                                                          Payment                                          Currency
                                    Company Code US00                     Bank
                                                                                                Purch. Org. US00


                                              Company Code DE00                                        Purch. Org. DE00



© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                19
Agenda


▪ QM Organizational Structure

▪ QM Master Data

▪ QM Processes
  • Quality Management
  • Quality Management in Procurement
  • Quality Management in SD




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   20

QM Process




       Quality
                                            Inspection    Inspection    Perform      Usage
        Info.
                                               Plan          Lot       Inspection   Decision
       Record




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                        21
Quality Information Record


▪ If a quality assurance agreement or vendor release is required for a material, a Quality Info. Record must be
  created

▪ Determines how a material can be processed further

▪ when a quotation or purchase order is created, the system checks whether a quality info record is required and
  available for the combination of material and vendor

▪ System also checks, whether the vendor and material-vendor combination is blocked or released for quotations,
  purchase orders and/or goods receipt




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                           22
Inspection Plan


▪ Can be created for different uses as model inspection, carrying out an audit, preliminary series inspection,
  goods receipt inspection, goods issue inspection, inspection of stock transfers, inspections in repetitive
  manufacturing

▪ Defines which characteristics are to be inspected in each inspection operation and which test equipment is to be
  used in the inspection

▪ Several materials can be assigned to an inspection plan

▪ Several inspection plans with different inspection operations or inspection characteristics can be created for a
  material or combination of material, vendor and manufacturer, or material and customer




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                              23
Inspection Lot


▪ Request to a plant to inspect a specific quantity of material or one or more pieces of equipment or functional
  locations

▪ Documented by an inspection lot record

▪ Used to record, process and manage information for a quality inspection

▪ Whenever materials are moved from on place to another under certain conditions, the QM component can
  automatically create inspection lots

▪ The system can also create an inspection lot automatically if a delivery is created in the SD component for a
  inspection-relevant material

▪ Can be created automatically or manually




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                            24
Perform Inspection


▪ Inspection of sample units of the inspection lot

▪ Number of non-conforming sample units entered in the SAP System




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.             25
Usage Decision


▪ Confirms that all physical samples have been valuated and the inspection has been completed

▪ Specifies whether the goods in the inspection lot have been accepted or rejected for use

▪ Inspection lot stock can be posted to different stocks
  •   Unrestricted use
  •   Scrap
  •   Sample usage
  •   Blocked stock




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                         26
QM Process in Procurement




    Quality
                               Inspection                 Purchase   Receiving   Inspection    Perform      Usage
     Info.
                                  Plan                     Order      Material      Lot       Inspection   Decision
    Record




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                               27
Quality Management in SD




   Quality                                                              Perform
                      Inspection             Goods        Inspection                 Usage     Goods     Sales   Outbound
    Info                                                                                                                     Invoice
                         Plan                Issue           Lot       Inspection   Decision   Receipt   Order    Delivery
   Record




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.                                                                                28
SAP QM Module Integration


▪ High integration in other SAP modules including:

  • SAP MM
    −   e.g. maintain quality agreements

  • SAP SD
    −   e.g. quality information related to customers

  • SAP PP
    −   e.g. perform inspection planning

  • SAP CO
    −   e.g. integrate SAP QM with controlling process




© 2025 SAP SE / SAP UCC Magdeburg. All rights reserved.   29

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
