---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_WM_III_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_WM_III_en_v4.3.docx
---

Warehouse Management (WM) III

> This case study explains an integrated warehouse management process, which is triggered released/set off by a sales order for material, to be delivered to the customer from a warehouse-managed storage location.

ss

------------------------------------------------------------------------

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 32%" />
<col style="width: 2%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th><p>Product</p>
<p>S/4HANA 2023</p>
<p>Global Bike</p>
<p>Fiori 3.0</p>
<p>Level</p>
<p>Beginner</p>
<p>Focus</p>
<p>Warehouse Management</p>
<p>Authors</p>
<p>Simha Magal</p>
<p>Stefan Weidner</p>
<p>Chris Bernhardt</p>
<p>Version</p>
<p>4.3</p>
<p>Last Update</p>
<p>July 2025</p></th>
<th style="text-align: left;"><p>MOTIVATION</p>
<p>Warehousing has significant value for logistics.</p>
<p>Current trends such as higher cost pressure, shorter cycles of innovation, higher customer expectations and globalization of markets make great demands on companies, particularly on warehouse logistics. This is especially difficult in industries with high distinction like the consumer goods industry. Furthermore, customers have increasingly higher demands on reliability, promptness and flexibility of deliveries.</p>
<p>Warehouse management systems support the global flow of goods between the producer and the purchaser and facilitate near fail-proof logistic operations in increasingly complex supply chains.</p></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"><p>PREREQUISITES</p>
<p>Before you use this case study, you should be familiar with navigation in the SAP system.</p>
<p>In order to work successfully through this case study, it is not necessary to finish the WM exercises. Anyway, it is recommended.</p>
<p>NOTES</p>
<p>This case study uses the Global Bike (GBI) data set, which has been exclusively created for SAP UA global curricula.</p>
<p><img src="media/image1.png" style="width:1.68893in;height:0.62765in" alt="M:\Curricula\Vorlagen\Logo_Global Bike\Global_Bike_Logo_neu_2018\Logo1.png" /></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="process-overview">Process Overview</h1></th>
</tr>
<tr>
<th colspan="2"><p><strong>Learning Objective</strong> Understand and perform a warehousing sales process cycle.</p>
<p><strong>Scenario</strong> Due to increasing sales output in your San Diego distribution center, the management has decided to install a Warehouse Management System there. After running some tests, you have some material in your warehouse and you can fulfill a new sales order.</p>
<p><strong>Employees involved</strong> Karim Messalem (Sales Person 1 US West)<br />
Carolin Bruzik (Warehouse Supervisor)<br />
Sunil Gupta (Warehouse Employee)<br />
Zarah Morello (Good Issue Clerk)</p></th>
<th style="text-align: right;"><strong>Time</strong> 85 min</th>
</tr>
<tr>
<th colspan="3"></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">First, you have to create a sales order. In order to fulfill this new sales order, you need to create an outbound delivery. You may remember this part from the SD case study. However, this time the process is slightly different, because you deliver from a warehouse-managed storage location. After picking the materials, goods are shipped to the customer. Because this case study focuses on Warehouse Management, detailed instructions of how to create the invoice and how to receive the payment are not included. However, you may use respective parts of the Sales and Distribution (SD) case study to finalize the sales process and see the financial impact.</th>
</tr>
<tr>
<th colspan="3" style="text-align: center;"><img src="media/image2.png" style="width:6.54306in;height:3.59722in" /></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**\**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><h1 id="table-of-contents" class="TOC-Heading">Table of Contents</h1>
<p><a href="#process-overview">Process Overview <span>2</span></a></p>
<p><a href="#step-1-create-sales-order">Step 1: Create Sales Order <span>4</span></a></p>
<p><a href="#step-2-display-material-inventory">Step 2: Display Material Inventory <span>6</span></a></p>
<p><a href="#step-3-create-outbound-delivery">Step 3: Create Outbound Delivery <span>8</span></a></p>
<p><a href="#step-4-change-outbound-delivery">Step 4: Change Outbound Delivery <span>9</span></a></p>
<p><a href="#step-5-display-material-inventory">Step 5: Display Material Inventory <span>11</span></a></p>
<p><a href="#step-6-pick-materials-with-transfer-order">Step 6: Pick Materials with Transfer Order <span>13</span></a></p>
<p><a href="#step-7-run-bin-status-report">Step 7: Run Bin Status Report <span>15</span></a></p>
<p><a href="#step-8-confirm-transfer-order">Step 8: Confirm Transfer Order <span>18</span></a></p>
<p><a href="#step-9-run-bin-status-report">Step 9: Run Bin Status Report <span>20</span></a></p>
<p><a href="#step-10-display-material-inventory-value">Step 10: Display Material Inventory Value <span>22</span></a></p>
<p><a href="#step-11-ship-materials">Step 11: Ship Materials <span>23</span></a></p>
<p><a href="#step-12-display-material-inventory">Step 12: Display Material Inventory <span>25</span></a></p>
<p><a href="#step-13-display-material-inventory-value">Step 13: Display Material Inventory Value <span>26</span></a></p>
<p><a href="#wm-iii-challenge">WM III Challenge <span>27</span></a></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-1-create-sales-order">Step 1: Create Sales Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a sales order.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to create a sales order.</p>
<p><strong>Name (Position)</strong> Karim Messalem (Sales Person 1 US West)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a sales order, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Sales Person</em> role the app <em>Manage Sales Orders-Version 2.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image3.png" style="width:1.58868in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Manage sales orders – Version 2</em> view, first click on the button <img src="media/image4.png" style="width:0.40748in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create</em> enter <strong>OR</strong> (Standard Order) as <em>Sales Order Type</em>, <strong>UW00</strong> as <em>Sales Organization</em>, <strong>WH</strong> (Wholesale) as <em>Distribution Channel</em>, <strong>BI</strong> (Bicycles) as <em>Division</em>. Confirm your entries by clicking <img src="media/image5.png" style="width:0.38337in;height:0.17502in" />.</td>
<td style="text-align: right;"><p>OR</p>
<p>UW00</p>
<p>WH</p>
<p>BI</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image6.png" style="width:2.02466in;height:2.4201in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Sales Order</em> view, enter <strong>133###</strong> (SoCal Bikes Irvine; replace ### with your number) as Sold-To Party and <strong>54321###</strong> as the <em>Customer Reference</em>. Enter <strong>one week from today</strong> as the <em>Requested delivery date</em>.</td>
<td style="text-align: right;"><p>133###</p>
<p>54321###</p>
<p>one week from today</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image7.png" style="width:5.05962in;height:1.57543in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then enter <strong>PRTR2###</strong> as the <em>product</em> and <strong>5</strong> as the <em>Requested quantity</em> in the Items area.</td>
<td style="text-align: right;"><p>PRTR2###</p>
<p>5</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image8.png" style="width:5.16528in;height:0.77292in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then click on <img src="media/image5.png" style="width:0.38337in;height:0.17502in" /> to save your order. The system will now assign an individual order number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image9.png" style="width:2.5698in;height:1.29684in" /></td>
<td style="text-align: right;">Standard Order Number</td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-2-display-material-inventory">Step 2: Display Material Inventory</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the inventory of your material.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to display the inventory of your material.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Stock - Single Material.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image11.png" style="width:1.60331in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Stock - Single Material</em> screen, enter <strong>PRTR2###</strong> as Material (remember to replace ### with your number). Klick Enter.</td>
<td style="text-align: right;">PRTR2###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image12.png" style="width:4.77713in;height:2.25433in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Note that you still have the same amount of unrestricted-use stock in San Diego.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image13.png" style="width:4.71352in;height:3.49933in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-3-create-outbound-delivery">Step 3: Create Outbound Delivery</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create an outbound delivery.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create the outbound delivery note for the sales order.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create an outbound delivery, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Create Outbound Delivery.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image14.png" style="width:1.58177in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will be taken to the <em>Create Outbound Delivery</em> screen. If you cannot see the header area, expand it by clicking on the button <img src="media/image15.png" style="width:0.17222in;height:0.17708in" />. In the header area that now opens, enter <strong>133###</strong> (SOCAL Bikes Irvine; replace ### with your number) as Ship-To Party, <strong>SD00</strong> as <em>Shipping point</em>, and <strong>Due up until next week</strong> as Planned Creation Date using the input help <img src="media/image16.png" style="width:0.18759in;height:0.17717in" />. Start the search by pressing <img src="media/image17.png" style="width:0.24449in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>133###</p>
<p>SD00</p>
<p>Due up until<br />
next week</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create Outbound Deliveries</em> screen, select the Sales Document and click on the button <img src="media/image18.png" style="width:0.99972in;height:0.17717in" />. You will receive a message that one log was created.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image19.png" style="width:5.16528in;height:1.1135in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">A log will then be generated. Click on the button <img src="media/image20.png" style="width:0.66245in;height:0.17717in" /> to display the log. Make a note of the number that uniquely identifies your delivery.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-4-change-outbound-delivery">Step 4: Change Outbound Delivery</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Change the outbound delivery.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to assign the storage location to the outbound delivery note for the sales order.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To change the outbound delivery, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Change Outbound Delivery.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image21.png" style="width:1.58174in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Change Outbound Delivery</em> screen, enter your delivery number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Alternatively, use the F4 help in the field <em>Outbound Delivery</em>. In the tab <em>Outbound Delivery: Not Posted for Goods Issue</em> enter <strong>133###</strong> (SOCAL Bikes Irvine; replace ### with your number) as Ship-To Party and <strong>SD00</strong> as Shipping point to find your Outbound Delivery number. Confirm your entries by pressing <img src="media/image17.png" style="width:0.24449in;height:0.17717in" />. Double-click on your outbound delivery to transfer it to the field Outbound Delivery.</td>
<td style="text-align: right;"><p>133###</p>
<p>SD00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image22.png" style="width:5.16528in;height:1.64236in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Confirm it with <img src="media/image23.png" style="width:0.46671in;height:0.17502in" /> to get to the <em>Outbound Delivery Change Screen</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image24.png" style="width:5.16528in;height:1.74306in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your Storage Location <strong>Finished Goods</strong> and confirm with Enter. By filling the field Storage Location, the SAP System realizes that you selected a WM controlled warehouse. Click on <img src="media/image25.png" style="width:0.30836in;height:0.17502in" /> to save your changes.</td>
<td style="text-align: right;">FG00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image26.png" style="width:2.67628in;height:0.25772in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-5-display-material-inventory">Step 5: Display Material Inventory</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the inventory of your material again.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to display the inventory of your material again.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Stock - Single Material.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image11.png" style="width:1.60331in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Stock - Single Material</em> screen, enter <strong>PRTR2###</strong> as Material (remember to replace ### with your number). Klick Enter.</td>
<td style="text-align: right;">PRTR2###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image27.png" style="width:5.16528in;height:3.22708in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Note that the amount of goods in San Diego has not changed yet.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Note In the App <em>Display Stock Overview</em> enter <strong>PRTR2###</strong> as Material. Select <img src="media/image28.png" style="width:0.41732in;height:0.17717in" /> to go to the stock overview. In the stock overview, you can scroll to the right to see the quantity (5) for the upcoming delivery.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image29.png" style="width:5.16528in;height:1.19306in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="3"><h1 id="step-6-pick-materials-with-transfer-order">Step 6: Pick Materials with Transfer Order</h1></th>
</tr>
<tr>
<th colspan="2"><p><strong>Task</strong> Create a transfer order to pick the materials.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to create a transfer order based on the delivery note created previously.</p>
<p><strong>Name (Position)</strong> Sunil Gupta (Warehouse Employee)</p></th>
<th style="text-align: right;"><strong>Time</strong> 10 min</th>
<th></th>
</tr>
<tr>
<th colspan="2"></th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">To create an outbound delivery, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Employee</em> role the app <em>Outbound Deliveries for Picking.</em></th>
<th>Start</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image30.png" style="width:1.5818in;height:1.5748in" /></th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Outbound Deliveries for Picking</em> screen, enter <strong>SD00</strong> as Shipping Point/Receiving Pt and select <strong>Only WM Picking</strong><em>.</em></th>
<th><p>SD00</p>
<p>Only WM-Picking</p></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image31.png" style="width:5.16528in;height:2.54097in" /></th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2">Then, click on <img src="media/image28.png" style="width:0.41732in;height:0.17717in" /> or press F8 to execute.</th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Day’s Workload for Picking</em> screen, you should see a line item with your <strong>Outbound Delivery Number</strong>. Select it and click on the <img src="media/image32.png" style="width:0.79993in;height:0.17717in" /> button.</th>
<th>Outbound Delivery Number</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image33.png" style="width:5.16528in;height:1.925in" /></th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Create Transfer Order for Delivery Note: Initial Screen</em>, press Enter to create your transfer order to be able to pick your documents. This will produce the following screen.</th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image34.png" style="width:5.16528in;height:1.55694in" /></th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">On the next screen, click on <img src="media/image35.png" style="width:0.36475in;height:0.17717in" /> to save your transfer order. The system will save the transfer order automatically and assign a unique transfer order number. Please note your number: ________________</th>
<th>Transfer Order Number</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image36.png" style="width:2.52432in;height:0.3334in" /></th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</th>
<th></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: right;"></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-7-run-bin-status-report">Step 7: Run Bin Status Report</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Check the status of your bins.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to run a bin status report, which will display a detailed report of each storage bin within the specified warehouse.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To run a bin status report, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Run Bin Status Report.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:1.5958in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> (for your San Diego Warehouse) as Warehouse Number and <strong>STBN*###</strong> as Storage bin (replace ### with your number). Then, click on <img src="media/image28.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image38.png" style="width:5.16528in;height:1.51319in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> The warehouse number is the highest level of organizational unit in warehouse management. In practice, the warehouse number usually corresponds to a physical building or distribution center. Each warehouse number has a substructure that maps the spatial relationship in the warehouse complex in detail.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image39.png" style="width:3.79711in;height:2.24182in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Storage bins are the lowest level of organizational structure. They are assigned to a storage type and a storage section (if one exists). Storage bins represent the physical location, where the goods are stored in the warehouse.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Overview</em> screen you should see that the Storage Bin <strong>STBN-8-###</strong> is filled.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image40.png" style="width:4.59525in;height:2.89505in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on your material to display detailed information of this quant and check whether 10 pieces of your good are stored in it.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> As you can see 15 pieces of your material are marked as available stock and the other 5 as pick quantity.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:4.73324in;height:3.40198in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-8-confirm-transfer-order">Step 8: Confirm Transfer Order</h1></th>
</tr>
<tr>
<th colspan="2"><p><strong>Task</strong> Confirm your transfer order.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to confirm the transfer order, you created in the previous step. This confirms that the goods have been physically picked from the storage bin, indicated in the transfer order.</p>
<p><strong>Name (Position)</strong> Sunil Gupta (Warehouse Employee)</p></th>
<th style="text-align: right;"><strong>Time</strong> 5 min</th>
</tr>
<tr>
<th colspan="2"></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">To confirm a transfer order, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Employee</em> role the app <em>Confirm Transfer Order.</em></th>
<th>Start</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image42.png" style="width:1.56787in;height:1.5748in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Confirm Transfer Order: Initial Screen</em>, enter the <strong>TO Number</strong> from the previous task and <strong>100</strong> as Warehouse Number. Then, press Enter.</th>
<th><p>TO Number</p>
<p>100</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><strong>Note</strong> If you have not written down the number, you can search for it using the app <em>Display Transfer Order</em>.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image43.png" style="width:4.22277in;height:0.93915in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Transfer Orders: List of Resident Documents</em> you have to fill in <strong>100</strong> as <em>Warehouse number</em>. Then, click on <img src="media/image28.png" style="width:0.41732in;height:0.17717in" />.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image44.png" style="width:3.54842in;height:1.39902in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Confirm Transfer Order: Overview of Transfer Order Items</em> screen, you should see an overview of your transfer order created in the previous step. Review all of the details to make sure you have the correct quantity and storage bin.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image45.png" style="width:5.16528in;height:2.29375in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Then, click on <img src="media/image46.png" style="width:0.37648in;height:0.17717in" /> to confirm your transfer order. The system will return a success message.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image47.png" style="width:2.76507in;height:0.25511in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: right;"></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-9-run-bin-status-report">Step 9: Run Bin Status Report</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Check the status of your bins again.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to run a bin status report, which displays a detailed report of each storage bin within the specified warehouse.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To run a bin status report, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Run Bin Status Report.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:1.5958in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> (for your San Diego Warehouse) as Warehouse Number and <strong>STBN*###</strong> as Storage bin (replace ### with your number). Then, click on <img src="media/image28.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image48.png" style="width:5.16528in;height:1.52292in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Overview</em> screen click on your material in Storage Bin <strong>STBN-8-###</strong> to display detailed information and check if there are just 15 pieces of your good left.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image49.png" style="width:5.16528in;height:3.84931in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-10-display-material-inventory-value">Step 10: Display Material Inventory Value</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the value of your material inventory.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to display the value of your material inventory.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory value, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Warehouse Stock.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image50.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Warehouse Stocks of Material</em> screen, enter <strong>PRTR2###</strong> as Material (replace ### with your number) and <strong>SD00</strong> as Plant. Ensure that all other search criteria fields are blank and click on <img src="media/image28.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>PRTR2###</p>
<p>SD00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image51.png" style="width:5.16528in;height:1.74514in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Note the total value associated with the DC in San Diego.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-11-ship-materials">Step 11: Ship Materials</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Ship the materials.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to ship the materials by posting a goods issue. This will reduce unrestricted stock to reflect that the inventory is shipped. It also indicates a change of ownership.</p>
<p><strong>Name (Position)</strong> Zarah Morello (Good Issue Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To ship materials, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Good Issue Clerk</em> role the app <em>Manage Outbound Deliveries.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image52.png" style="width:1.58171in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Manage deliveries</em> view, you will see a list of all deliveries. To narrow down the list, expand the header area by clicking on the button <img src="media/image15.png" style="width:0.17222in;height:0.17708in" />. Enter your customer number <strong>133###</strong> in the <em>Ship-to Party</em> field. After you have initiated the search with <img src="media/image17.png" style="width:0.24449in;height:0.17717in" />, only your delivery will be displayed in the lower area.</td>
<td style="text-align: right;">133###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image53.png" style="width:5.16528in;height:1.31806in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can see that the outbound delivery has been fully picked and confirmed, but the goods issue is still pending.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Outbound delivery</em> view, you will first see the general information. By clicking twice on the delivery document number and displaying the delivery, check the picked quantity 5 in the Items area.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image54.png" style="width:5.16528in;height:1.44722in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">After a successful check, click on <img src="media/image55.png" style="width:0.17708in;height:0.17708in" /> to return to the <em>Manage outbound deliveries</em> view. In the <em>Deliveries</em> area, select your outbound delivery and then click on <img src="media/image56.png" style="width:0.5476in;height:0.17717in" />. In the popup <em>Post Goods Issue</em>, select today's date and click on <img src="media/image57.png" style="width:0.55297in;height:0.17717in" /> to confirm. The system will display a success message. If you want to check the status of the outbound delivery, you must adjust the <em>Overall status</em> field in the header area accordingly.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image58.png" style="width:5.16528in;height:1.35278in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-12-display-material-inventory">Step 12: Display Material Inventory</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the inventory of your material again.</p>
<p><strong>Short Description</strong> Use Fiori Launchpad to display the inventory of your material again.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Stock - Single Material.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image59.png" style="width:1.60609in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Stock - Single Material</em> screen, enter <strong>PRTR2###</strong> as Material (remember to replace ### with your number). Click Enter.</td>
<td style="text-align: right;">PRTR2###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image60.png" style="width:4.9558in;height:2.5965in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Note that the amount of your goods in San Diego has decreased. This represents that 5 pieces of your material actually have been shipped.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-13-display-material-inventory-value">Step 13: Display Material Inventory Value</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the value of your material inventory again.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to display the value of your material inventory again.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory value, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Warehouse Stock.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image50.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Warehouse Stocks of Material</em> screen, enter <strong>PRTR2###</strong> as Material (remember to replace ### with your number) and <strong>SD00</strong> as Plant. Ensure that all other search criteria fields are blank and click on <img src="media/image28.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>PRTR2###</p>
<p>SD00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image61.png" style="width:5.16528in;height:1.75139in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see the values, associated with the material in San Diego, has been decreased. So there is no value associated to the <em>Transit/Transf.</em> for San Diego. This indicates the change of ownership after processing the shipping order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="wm-iii-challenge">WM III Challenge</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><strong>Learning Objective</strong> Understand and perform a warehousing sales process cycle.</td>
<td style="text-align: right;"><strong>Time</strong> 65 min</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p><strong>Motivation</strong> After having finished the <em>Warehouse Management III</em> case study successfully, you should now be able to solve the following challenge.</p>
<p><strong>Scenario</strong> The warehouse management system has been tested without any problems, so the management decided to use the system productively. Due to a higher demand of bikes for the Tour de France, black Professional Touring Bikes are almost out of stock in Europe. They are still available in the Distribution Center in San Diego, so the delivery of the wholesale sales order can be managed by the new warehouse management system.</p>
<p>The customer VeloDOM from Magdeburg (Germany) ordered 20 black Professional Touring Bikes with a delivery time of 10 days.</p>
<p><strong>Task Information</strong> You can use the case study <em>Warehouse Management III</em> as a guideline, but it is recommended to complete this challenge without further assistance to prove your WM skills.</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>
