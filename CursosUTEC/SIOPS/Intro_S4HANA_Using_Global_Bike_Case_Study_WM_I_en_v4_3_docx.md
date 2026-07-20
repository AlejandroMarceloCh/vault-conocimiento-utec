---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_WM_I_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_WM_I_en_v4.3.docx
---

Warehouse Management (WM) I

> This case study explains an integrated warehouse management process which is triggered by a purchase order for a warehouse-managed storage location.

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
<th><p>MOTIVATION</p>
<p>Warehousing has significant value for logistics.</p>
<p>Current trends such as higher cost pressure, shorter cycles of innovation, higher customer expectations and globalization of markets make great demands on companies, particularly on warehouse logistics. This is especially difficult in industries with high differentiation like the consumer goods industry. Furthermore, customers have increasingly higher demands on reliability, promptness and flexibility of deliveries.</p>
<p>Warehouse management systems support the global flow of goods between the producer and the purchaser and facilitate near fail-proof logistic operations in increasingly complex supply chains.</p></th>
<th></th>
<th><p>PREREQUISITES</p>
<p>Before you use this case study, you should be familiar with navigation in the SAP system.</p>
<p>In order to work successfully through this case study, it is not necessary to finish the WM exercises. Anyway, it is recommended.</p>
<p>NOTES</p>
<p>This case study uses the Global Bike (GB) data set, which has been exclusively created for SAP UA global curricula.</p>
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
<th colspan="2" style="text-align: left;"><p><strong>Learning Objective</strong> Understand and perform a warehousing process for externally procured goods.</p>
<p><strong>Scenario</strong> Due to increasing sales output in your San Diego distribution center, management has decided to install a Warehouse Management System. This implementation has just been completed and the new system needs to be tested. For this purpose, trading goods should be procured by a vendor and put in the stock in San Diego, using the new warehouse management system.</p>
<p><strong>Employees involved</strong> Jennifer Brown (Plant Manager)<br />
Carolin Bruzik (Warehouse Supervisor)<br />
Sunil Gupta (Warehouse Employee)<br />
Yoshi Agawa (Goods Receipt Clerk)</p></th>
<th style="text-align: right;"><strong>Time</strong> 65 min</th>
</tr>
<tr>
<th colspan="3"></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">In order to receive goods from a vendor you need to create a purchase order. Goods will be sent by the vendor to the distribution center and you will create a goods receipt in San Diego. The system will automatically create a transfer order for the received goods to put them into stock. In conclusion, you will check if the goods were stored in the correct storage bins. As this case study focuses on Warehouse Management, detailed instructions of how to receive the invoice and how to pay the vendor are not included. However, you may use respective parts of the Materials Management (MM) case study to finalize the procurement process and see the financial impact.</th>
</tr>
<tr>
<th colspan="3" style="text-align: left;"><img src="media/image2.png" style="width:6.46382in;height:1.63641in" alt="Bild12" /></th>
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
<p><a href="#step-1-create-purchase-order">Step 1: Create Purchase Order <span>4</span></a></p>
<p><a href="#step-2-display-material-inventory">Step 2: Display Material Inventory <span>6</span></a></p>
<p><a href="#step-3-display-material-inventory-value">Step 3: Display Material Inventory Value <span>8</span></a></p>
<p><a href="#step-4-receive-goods">Step 4: Receive Goods <span>9</span></a></p>
<p><a href="#step-5-display-material-inventory">Step 5: Display Material Inventory <span>12</span></a></p>
<p><a href="#step-6-display-material-inventory-value">Step 6: Display Material Inventory Value <span>15</span></a></p>
<p><a href="#step-7-run-bin-status-report">Step 7: Run Bin Status Report <span>16</span></a></p>
<p><a href="#step-8-create-transfer-order">Step 8: Create Transfer Order <span>18</span></a></p>
<p><a href="#step-9-confirm-transfer-order">Step 9: Confirm Transfer Order <span>20</span></a></p>
<p><a href="#step-10-run-bin-status-report">Step 10: Run Bin Status Report <span>22</span></a></p>
<p><a href="#wm-i-challenge">WM I Challenge <span>24</span></a></p></th>
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
<th colspan="2"><h1 id="step-1-create-purchase-order">Step 1: Create Purchase Order</h1></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><p><strong>Task</strong> Create a purchase order.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create an immediate purchase order for materials from a supplier, i.e. to start the procurement process without having created a purchase requisition before.</p>
<p><strong>Name (Position)</strong> Jennifer Brown (Plant Manager)</p></th>
<th style="text-align: right;"><strong>Time</strong> 10 min</th>
</tr>
<tr>
<th colspan="2"></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">To create a purchase order, use the app <em>Manage Purchase Orders</em> in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Plant Manager</em> role.</th>
<th>Start</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image3.png" style="width:1.60236in;height:1.5748in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2">Click on <img src="media/image4.png" style="width:0.45669in;height:0.17717in" />.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Purchase Order</em> screen, enter the <em>type of purchasing Doc</em>. <strong>NB Standard PO</strong> and <strong>103###</strong> (replace ### with your number) as <em>Supplier</em>.</th>
<th><p>NB Standard PO</p>
<p>103###</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Then, fill in <strong>N00</strong> as <em>Purchasing Group</em>.</th>
<th>N00</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image5.png" style="width:5.16597in;height:1.10833in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2">In the <em>Items</em> tab, click on <img src="media/image4.png" style="width:0.45669in;height:0.17717in" /> to create the item. Enter <strong>KPAD1###</strong> as the <em>material</em> (replace ### with your number), <strong>SD00</strong> as the <em>plant</em>, <strong>50</strong> as the <em>order Quantity</em>, <strong>40</strong> USD as the <em>net order price.</em></th>
<th><p>KPAD1###</p>
<p>SD00</p>
<p>50</p>
<p>40</p></th>
</tr>
<tr>
<th colspan="2"><img src="media/image6.png" style="width:5.16597in;height:1.33472in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2">Click on <img src="media/image7.png" style="width:0.12205in;height:0.17717in" /> to go to the <em>Purchase Order Item</em> screen.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Delivery details</em> tab, enter <strong>TG00</strong> as the <em>storage location</em>. In the <em>Schedule lines</em> tab, enter <strong>8 days from today</strong> as the <em>delivery date</em>.</th>
<th><p>TG00</p>
<p>8 days from today</p></th>
</tr>
<tr>
<th colspan="2">Click on <img src="media/image8.png" style="width:0.33858in;height:0.17717in" />.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Items tab</em>, click again on <img src="media/image4.png" style="width:0.45669in;height:0.17717in" />, but select <strong>EPAD1###</strong> as the <em>material</em> and repeat your entries.</th>
<th>Repeat for EPAD1###</th>
</tr>
<tr>
<th colspan="2">Click on <img src="media/image8.png" style="width:0.33858in;height:0.17717in" />. Then click on <img src="media/image9.png" style="width:0.33733in;height:0.17717in" /> to save your order. The system assigns a document number for the standard order.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image10.png" style="width:2.94203in;height:1.81838in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</th>
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

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2" style="text-align: left;"><h1 id="step-2-display-material-inventory">Step 2: Display Material Inventory</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> View the inventory of your material.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to display the inventory of your material.</p>
<p><strong>Name (Position)</strong> Jennifer Brown (Plant Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material stock, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Plant Manager</em> role the app <em>Stock - Single material</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image12.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <strong>KPAD1###</strong> as Material (remember to replace ### with your number). Click on Enter.</td>
<td style="text-align: right;">KPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image13.png" style="width:5.16528in;height:2.04792in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Note that the unrestricted-use stock of goods in San Diego is zero. If you can not see the <em>Stock History</em> you can easily insert it in the <em>Settings</em> <img src="media/image14.png" style="width:0.21805in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image15.png" style="width:5.16528in;height:0.75208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the icon in the row for DC San Diego in the Stock History symbol <img src="media/image16.png" style="width:0.75197in;height:0.19685in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The system will now display the stock history of your material KPAD1### in SD TG00.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image17.png" style="width:5.16528in;height:2.83819in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat this task for the material <strong>EPAD1###</strong>.</td>
<td style="text-align: right;">Repeat for EPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Plant Manager</em> role the app <em>Display Stock Overview</em>. Enter <strong>KPAD1###</strong> as Material</td>
<td style="text-align: right;">KPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:5.16528in;height:1.23611in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">After double clicking on <em>SD00 DC San Diego</em>, you will see a separate <em>Stock Overview</em> for your distribution center and the On-Order Stock balance of 50.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image19.png" style="width:5.07665in;height:1.42018in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-3-display-material-inventory-value">Step 3: Display Material Inventory Value</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> View the value of your material inventory.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to display your material inventory.</p>
<p><strong>Name (Position)</strong> Jennifer Brown (Plant Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory value, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Plant Manager</em> role the app <em>Display Warehouse Stock</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image20.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Warehouse Stocks of Material</em> screen, enter <strong>KPAD1###</strong> as Material. Ensure that all other search criteria fields are blank and click on <img src="media/image21.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;">KPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image22.png" style="width:4.85875in;height:2.54998in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can see that all values listed for this material are currently zero.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat this task for the material <strong>EPAD1###</strong>.</td>
<td style="text-align: right;">Repeat for EPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-4-receive-goods">Step 4: Receive Goods</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Receive goods at receiving plant.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to create a goods receipt which documents the receiving of your materials in San Diego.</p>
<p><strong>Name (Position)</strong> Yoshi Agawa (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a goods receipt, use the app <em>Post Goods Receipt for Purchasing Document</em> in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Goods Receipt Clerk</em> role.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image23.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your <strong>purchasing document number</strong> in the <em>Purchasing document</em> field.</td>
<td style="text-align: right;">Purchasing Document Number</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If you want to search for your <em>purchasing document number</em>, use the F4 help.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your three-digit number *### in the <em>Search</em> field and click on <img src="media/image24.png" style="width:0.24449in;height:0.17717in" />. Your purchasing document is displayed. Double-click on it to accept it.</td>
<td style="text-align: right;">*###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image25.png" style="width:5.16528in;height:1.44583in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image26.png" style="width:5.09126in;height:2.56901in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <strong>Individual slip</strong> for <em>printing</em>.</td>
<td style="text-align: right;">Individual slip</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image27.png" style="width:5.08755in;height:0.7706in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on line <em>Material</em> KPAD1### to see detailed information.</td>
<td style="text-align: right;">KPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Check that the <em>storage location</em> <strong>Trading Goods</strong> and <em>stock type</em> is set to <strong>Unrestricted-Use</strong>. Select the checkbox for <strong>delivery completed.</strong></td>
<td style="text-align: right;"><p>Trading Goods</p>
<p>Unrestricted Use</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image28.png" style="width:4.8024in;height:2.24326in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now click on <img src="media/image29.png" style="width:0.46063in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat this step for <strong>EPAD1###</strong>.</td>
<td style="text-align: right;">EPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now click on <img src="media/image29.png" style="width:0.46063in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Leave both lines selected.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image30.png" style="width:5.09965in;height:1.49602in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image31.png" style="width:0.26772in;height:0.17717in" /> to save your receipt. The system will assign a unique material document number.</td>
<td style="text-align: right;">Material document number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image32.png" style="width:2.90293in;height:1.54869in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-5-display-material-inventory">Step 5: Display Material Inventory</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> View the inventory of your material again.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to display the inventory of your material again.</p>
<p><strong>Name (Position)</strong> Jennifer Brown (Plant Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material stock, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Plant Manager</em> role the app <em>Stock - Single material</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image12.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <strong>KPAD1###</strong> as Material (remember to replace ### with your number). Lick on Enter.</td>
<td style="text-align: right;">KPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image33.png" style="width:5.16528in;height:2.07708in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Note that the unrestricted-use stock of goods in San Diego has changed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image34.png" style="width:5.16528in;height:0.75556in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the icon in the row for SD San Diego in the Stock History symbol <img src="media/image35.png" style="width:0.29389in;height:0.17717in" />. The system will now display the stock history of your material KPAD1### in SD TG00.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image36.png" style="width:5.16528in;height:2.83333in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat this task for the material <strong>EPAD1###</strong>.</td>
<td style="text-align: right;">Repeat for EPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Plant Manager</em> role the app <em>Display Stock Overview</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:4.90303in;height:1.90288in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image38.png" style="width:5.16528in;height:1.89792in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image39.png" style="width:5.0072in;height:2.07364in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-6-display-material-inventory-value">Step 6: Display Material Inventory Value</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> View the value of your material inventory again.</p>
<p><strong>Short Description</strong> In this step, you will use the Fiori Launchpad to display the value of your material inventory again.</p>
<p><strong>Name (Position)</strong> Jennifer Brown (Plant Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory value, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Plant Manager</em> role the app <em>Display Warehouse Stock</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image20.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Warehouse Stocks of Material</em> screen, enter <strong>KPAD1###</strong> as Material (remember to replace ### with your number). Ensure that all other search criteria fields are blank and click on <img src="media/image21.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;">KPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image40.png" style="width:4.68332in;height:2.43383in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see the value for the 50 units of your material has been added to the distribution center in San Diego.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat this task for the material <strong>EPAD1###</strong>.</td>
<td style="text-align: right;">EPAD1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad..</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-7-run-bin-status-report">Step 7: Run Bin Status Report</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Check the status of your bins.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to run a bin status report, which will display a detailed report of each storage bin within the specified warehouse.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To run a bin status report, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Warehouse Supervisor</em> role the app <em>Run Bin Status Report</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:1.53937in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> (for your San Diego Warehouse) as Warehouse Number and <strong>STBN*###</strong> as Storage bin (replace ### with your number).</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image42.png" style="width:4.88219in;height:1.45146in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note:</strong> The warehouse number is the highest level of organizational unit in warehouse management. In practice, the warehouse number usually corresponds to a physical building or distribution center. Each warehouse number has a substructure that maps the spatial relationship in the warehouse complex in detail.</p>
<p><img src="media/image43.png" style="width:3.79711in;height:2.24182in" /></p>
<p>Storage bins are the lowest level of organizational structure. They are assigned to a storage type and a storage section (if one exists). Storage bins represent the physical location where the goods are stored in the warehouse.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image21.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image44.png" style="width:4.2016in;height:2.49318in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Overview</em> screen you should see a list of all your storage bins for the entire warehouse in San Diego. Double click on one of your storage bins to get detailed information. As you can see the ordered materials are not present yet. Currently they are located in temporary bins.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-8-create-transfer-order">Step 8: Create Transfer Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Create a transfer order.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to create a transfer order to place your goods into your storage bin. It is a handoff from inventory management to warehouse management. The system recognizes that there are goods that have been received but need to be put away.</p>
<p><strong>Name (Position)</strong> Sunil Gupta (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a transfer order, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Warehouse Employee</em> role the app <em>Display Transfer Requirement – List for Material</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image45.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Transfer Requirement: List of Material</em> screen, enter <strong>100</strong> (for your San Diego Warehouse) as Warehouse Number, <strong>KPAD1###</strong> as Material (replace ### with your number) and <strong>SD00</strong> as Plant. Then, press Enter.</td>
<td style="text-align: right;"><p>100</p>
<p>KPAD1###</p>
<p>SD00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image46.png" style="width:5.16528in;height:2.475in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Transfer Requirements for Material</em> screen, you should see a line item describing the goods just received for your purchase order. The requirement number should be the same as the purchase order number you received earlier. Make sure that the line item is selected.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image47.png" style="width:4.75503in;height:1.1849in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image48.png" style="width:0.75591in;height:0.17717in" /> button.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create TO for TR 00000000XX 0001: Prepare for Putaway</em> screen, hit Enter to copy your quantity of 50 from the <em>Palletization</em> section to the <em>Items</em> section. Enter <strong>001</strong> as <em>Sec</em>, <strong>STBN-1-###</strong> as <em>Destination Bin</em> (replace ### with your number) and use F4 to select <strong>Shelf Storage</strong> a <em>Type</em>. Confirm your entries by pressing Enter.</td>
<td style="text-align: right;"><p>001</p>
<p>STBN-1-###</p>
<p>001 (Shelf Storage)</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image49.png" style="width:5.16528in;height:3.87847in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image50.png" style="width:0.3622in;height:0.17717in" /> to save your transfer order. If any warnings occur ignore them by pressing Enter. The system will assign a unique transfer order number. Please write down this number.</td>
<td style="text-align: right;">Transfer Order Number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image51.png" style="width:2.51787in;height:0.2666in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat the whole procedure for your material <strong>EPAD1###</strong> to put it in the same storage bin.</td>
<td style="text-align: right;">Transfer Order Number</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-9-confirm-transfer-order">Step 9: Confirm Transfer Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Confirm your transfer order.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to confirm the transfer order you created in the previous step. This is to confirm that the goods are physically in the storage bin indicated in the transfer order.</p>
<p><strong>Name (Position)</strong> Sunil Gupta (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To confirm a transfer order, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Warehouse Employee</em> role the app <em>Confirm Transfer Order</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image52.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Confirm Transfer Order: Initial Screen</em>, enter the <strong>Transfer Order Number</strong> from the previous task and <strong>100</strong> as Warehouse Number. Then press Enter.</td>
<td style="text-align: right;"><p>Transfer Order Number</p>
<p>100</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image53.png" style="width:3.17377in;height:1.2084in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If you have not written down the number, you can search for it using the app <em>Display Transfer Order / Material</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image54.png" style="width:3.90992in;height:0.86115in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Transfer Orders for Materials</em> you have to fill in <strong>100</strong> as <em>Warehouse number</em> and your material <strong>KPAD1### / EPAD1###</strong> to display the regarding transfer order. Then, click on <img src="media/image21.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>100</p>
<p>KPAD1###</p>
<p>EPAD1###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Confirm Transfer Order: Overview of Transfer Order Items</em> screen you should see an overview of your transfer order created in the previous step. Review all of the details to make sure you have the correct quantity and storage bin.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image55.png" style="width:5.16528in;height:1.17431in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image50.png" style="width:0.3622in;height:0.17717in" /> to confirm your transfer order. The system will return a success message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image56.png" style="width:3.31782in;height:0.25868in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat this step for your other transfer order number (second material).</td>
<td style="text-align: right;">Repeat for second Transfer Order</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-10-run-bin-status-report">Step 10: Run Bin Status Report</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Check the status of your bins again.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to run a bin status report, which will display a detailed report of each storage bin within the specified warehouse.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To run a bin status report, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Warehouse Supervisor</em> role the app <em>Run Bin Status Report</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image57.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> (for your San Diego Warehouse) as Warehouse Number and <strong>STBN*###</strong> as Storage bin (replace ### with your number).</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image58.png" style="width:5.16528in;height:1.52917in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image21.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image59.png" style="width:4.1408in;height:2.65916in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Overview</em> screen you should see that the Storage Bin <strong>STBN-1-###</strong> is filled now. Click on this storage bin to display detailed information and check whether 50 of each of your goods are stored in it.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image60.png" style="width:4.3406in;height:0.9595in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can also display the quant assigned to each material. To do this, select a material and press <img src="media/image61.png" style="width:0.87162in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image62.png" style="width:4.89608in;height:2.52096in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image11.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="wm-i-challenge">WM I Challenge</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><strong>Learning Objective</strong> Understand and perform a warehousing process for ext. goods.</td>
<td style="text-align: right;"><strong>Time</strong> 40 min</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p><strong>Motivation</strong> After having finished the <em>Warehouse Management I</em> case study successfully, you should now be able to solve the following challenge.</p>
<p><strong>Scenario</strong> The warehouse management system has been tested without any problems, so the management decided to use the system productively. Now your task is to order two different products (water bottles and road helmets) from the supplier <em>Spy Gear</em>, 50 pieces each. A water bottle will cost 11 USD and a road helmet will cost 27 USD. The trading goods should be delivered in 8 days.</p>
<p>After receipt of the goods in your goods SD00 in San Diego, they are to be stored separately in two different storage bins. The goods are stored in the destination storage bins STBN-2-### for the water bottles and STBN-3-### for the street helmets.</p>
<p><strong>Task Information</strong> You can use the <em>Warehouse Management I</em> case study as a guideline, but it is recommended to complete this challenge without further assistance to prove your WM skills.</p></td>
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
