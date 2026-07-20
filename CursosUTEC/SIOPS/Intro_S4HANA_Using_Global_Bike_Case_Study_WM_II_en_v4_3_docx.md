---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_WM_II_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_WM_II_en_v4.3.docx
---

Warehouse Management (WM) II

> This case study explains an integrated warehouse management process, which is triggered by a stock transport order from a manufacturing facility to a warehouse-managed storage location.

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
<p>Current trends such as higher cost pressure, shorter cycles of innovation, higher customer expectations and globalization of markets make great demands on companies, particularly on warehouse logistics. This is especially difficult in industries with high differentiation like the consumer goods industry. Furthermore, customers have increasingly higher demands on reliability, promptness and flexibility of deliveries.</p>
<p>Warehouse management systems support the global flow of goods between the producer and the purchaser and facilitate near fail-proof logistic operations in increasingly complex supply chains.</p></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"><p>PREREQUISITES</p>
<p>Before you use this case study, you should be familiar with navigation in the SAP system.</p>
<p>In order to work successfully through this case study, it is not necessary to finish the WM exercises. However, it is recommended.</p>
<p>NOTES</p>
<p>This case study uses the Global Bike (GBI) data set, which has exclusively been created for SAP UA global curricula.</p>
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
<th colspan="2" style="text-align: left;"><p><strong>Learning Objective</strong> Understand and perform a warehousing process for int. goods</p>
<p><strong>Scenario</strong> Due to increasing sales output in your San Diego distribution center, management has decided to install a Warehouse Management System there. The implementation is completed and now the new system needs to be tested. For this purpose, finished goods should be requested from your manufacturing facility in Dallas and put in stock in San Diego using the new warehouse management system.</p>
<p><strong>Employees involved</strong> Carolin Bruzik (Warehouse Supervisor)<br />
Jennifer Brown (Plant Manager)<br />
Sanjay Datar (Warehouse Employee)<br />
Yoshi Agawa (Goods Receipt Clerk)</p></th>
<th style="text-align: right;"><strong>Time</strong> 90 min</th>
</tr>
<tr>
<th colspan="3"></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">In order to receive goods from the plant in Dallas you need to create a stock transport order. Dallas will send the goods to the San Diego distribution center. As soon as you perform the goods receipt in San Diego, the system will create a transfer order for the received goods. Due to this order, the Warehouse Management will put the goods into stock. In the end, you can check if the goods have been sorted into the correct storage bins.</th>
</tr>
<tr>
<th colspan="3" style="text-align: center;"><img src="media/image2.png" style="width:6.54306in;height:4.28472in" /></th>
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
<p><a href="#step-1-display-material-inventory">Step 1: Display Material Inventory <span>4</span></a></p>
<p><a href="#step-2-create-stock-transport-order">Step 2: Create Stock Transport Order <span>6</span></a></p>
<p><a href="#step-3-display-material-inventory">Step 3: Display Material Inventory <span>8</span></a></p>
<p><a href="#step-4-display-material-inventory-value">Step 4: Display Material Inventory Value <span>10</span></a></p>
<p><a href="#step-5-create-goods-issue">Step 5: Create Goods Issue <span>11</span></a></p>
<p><a href="#step-6-display-material-inventory">Step 6: Display Material Inventory <span>13</span></a></p>
<p><a href="#step-7-display-material-inventory-value">Step 7: Display Material Inventory Value <span>15</span></a></p>
<p><a href="#step-8-create-goods-receipt">Step 8: Create Goods Receipt <span>17</span></a></p>
<p><a href="#step-9-display-material-inventory">Step 9: Display Material Inventory <span>18</span></a></p>
<p><a href="#step-10-display-material-inventory-value">Step 10: Display Material Inventory Value <span>20</span></a></p>
<p><a href="#step-11-run-bin-status-report">Step 11: Run Bin Status Report <span>21</span></a></p>
<p><a href="#step-12-create-transfer-order">Step 12: Create Transfer Order <span>23</span></a></p>
<p><a href="#step-13-confirm-transfer-order">Step 13: Confirm Transfer Order <span>25</span></a></p>
<p><a href="#step-14-run-bin-status-report">Step 14: Run Bin Status Report <span>27</span></a></p>
<p><a href="#wm-ii-challenge">WM II Challenge <span>29</span></a></p></th>
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
<th colspan="2"><h1 id="step-1-display-material-inventory">Step 1: Display Material Inventory</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the inventory of your material.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to display the inventory of your material.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material stock, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Stock - Single material</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image3.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Stock - single material</em> view, enter <strong>DXTR1###</strong> (replace ### with your number) in the Material field.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the following screen you can see the total stock of your material in the warehouse as well as the current stock quantity in the Dallas plant from which you are ordering your material.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image4.png" style="width:5.16528in;height:2.61806in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Write down the stock overview to each plant. Note that your numbers may vary, because of the case studies you performed before.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p>Plant Dallas</p>
<p>_____________</p>
<p>Plant Heidelberg</p>
<p>_____________</p>
<p>Plant Hamburg</p>
<p>_____________</p>
<p>Plant Miami</p>
<p>_____________</p>
<p>Plant San Diego</p>
<p>_____________</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Storage Purchasing</em> page in the <em>Plant Manager</em> role the app <em>Display Stock Overview</em>. Enter <strong>DXTR1###</strong> as Material.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image6.png" style="width:5.16528in;height:1.70278in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image7.png" style="width:5.16528in;height:2.00208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: center;"></td>
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
<th colspan="2"><h1 id="step-2-create-stock-transport-order">Step 2: Create Stock Transport Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a stock transport order.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to create a stock transport order. This means that you request material from another GBI plant instead of procuring it from a vendor.</p>
<p><strong>Name (Position)</strong> Jennifer Brown (Plant Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Plant Manager</em> role the app <em>Create Purchase Order.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image8.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create Purchase Order</em> screen, change the type of purchase order to <strong>Stock Transp. Order</strong> and accept any warning messages with Enter. Fill in <strong>US00</strong> as <em>Purch.Org.</em>, <strong>N00</strong> as <em>Purch. Group</em>, <strong>US00</strong> as <em>Company Code</em> and <strong>DL00</strong> as <em>Supplying Plant</em>. Press <em>Enter</em>.</td>
<td style="text-align: right;"><p>Stock Transp. Order</p>
<p>US00</p>
<p>N00</p>
<p>US00</p>
<p>DL00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image9.png" style="width:5.16528in;height:0.90208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Transfer postings should not involve a physical goods movement; however, in stock transfers, there is always a physical movement of goods. In a plant-to-plant stock transfer, the plants, between which the material is transferred, can belong to the same company code or different company codes. The cross-plant stock transfers can only be booked out of the unrestricted-use stock.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <img src="media/image10.png" style="width:0.17717in;height:0.17717in" /> to expand the Item Overview. Enter <strong>DXTR1###</strong> as <em>Material</em> (replace ### with your number), <strong>10</strong> as <em>PO Quantity</em>, <strong>SD00</strong> as <em>Plant</em>, <strong>FG00</strong> as <em>Storage Location</em> and <strong>8 days from today</strong> as <em>Delivery Date</em>. Confirm your entries by pressing <em>Enter</em>.</td>
<td style="text-align: right;"><p>DXTR1###</p>
<p>10</p>
<p>SD00</p>
<p>FG00</p>
<p>8 days from today</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image11.png" style="width:5.16528in;height:1.79514in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Compare your entries with the screenshot above.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image12.png" style="width:0.29921in;height:0.17717in" /> to save your order. You may receive a warning message which you can ignore by clicking on <img src="media/image13.png" style="width:1.32646in;height:0.19445in" />.</td>
<td style="text-align: right;">Save</td>
</tr>
<tr>
<td colspan="2">The system will assign a unique <em>stock transport order document number</em>.</td>
<td style="text-align: right;">transport order document number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image14.png" style="width:3.64299in;height:0.21075in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Note the stock transport order document number:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-3-display-material-inventory">Step 3: Display Material Inventory</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the inventory of your material again.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to display the inventory of your material again.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Stock Overview.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image15.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <strong>DXTR1###</strong> as Material (replace ### with your number). Make sure that all other search criteria fields are blank and click on <img src="media/image16.png" style="width:0.41732in;height:0.17717in" />. Your numbers may vary.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the following screen, you see the global amount of your material on stock as well as the current amount in your Dallas plant, which you will order the material from.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image17.png" style="width:5.16528in;height:1.19097in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click at <img src="media/image18.png" style="width:0.82677in;height:0.17717in" /> to get more information.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><p><img src="media/image19.png" style="width:4.69469in;height:2.0765in" /></p>
<p>…</p>
<p><img src="media/image20.png" style="width:4.66691in;height:1.13895in" /></p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Close the pop up.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Note that you still have the same amount of goods in Dallas. However, after double clicking on <em>SD00 DC San Diego</em> you can see that you have an On-Order Stock balance of 10 for your distribution center in San Diego.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image21.png" style="width:4.66691in;height:1.89716in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-4-display-material-inventory-value">Step 4: Display Material Inventory Value</h1></th>
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
<td colspan="2" style="text-align: left;">To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Warehouse Stock.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image22.png" style="width:1.55906in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Warehouse Stocks of Material</em> screen, enter <strong>DXTR1###</strong> as Material (replace ### with your number). Click on <img src="media/image16.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image23.png" style="width:4.71832in;height:3.00253in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see, there is no total value associated with the DC in San Diego. Please be aware that your numbers may vary.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-5-create-goods-issue">Step 5: Create Goods Issue</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a goods issue from the issuing plant.</p>
<p><strong>Short Description</strong> In this step, you will use the SAP Fiori Launchpad to issue the goods, requested from your plant in Dallas to your distribution center in San Diego.</p>
<p><strong>Name (Position)</strong> Sanjay Datar (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a goods issue, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Employee</em> role the app <em>Post Goods Movement.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image24.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen, change the Material Document drop down to <strong>Goods Issue</strong> and adjust the type of Goods Issue to a <strong>Purchase Order</strong>.</td>
<td style="text-align: right;"><p>Goods Issue</p>
<p>Purchase Order</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image25.png" style="width:3.39275in;height:0.31742in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> A purchase order is the same as a stock transport order, you technically purchase the goods from the other plant, but it is a transport, because the plants are under the same company code.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Input your <strong>Stock Transport Order Number</strong> in the blank space next to it and 351 as movement type.</td>
<td style="text-align: right;">Stock Transp. Order Nr.</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If you have not written down the TO number you created in the second task, you may use the F4 help in the TO number field (first blank field next to the second drop-down field).</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the following screen choose the <em>Purchasing Documents for Material</em> tab by using <img src="media/image26.png" style="width:0.1389in;height:0.1389in" /> . Then, enter <strong>DXTR1###</strong> as Material and click on <img src="media/image27.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image28.png" style="width:5.16528in;height:1.11597in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Double click on your entry. Your order number will automatically filled in.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image29.png" style="width:5.3016in;height:0.28431in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Press Enter.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">When your order comes up select <strong>OK</strong> and enter <strong>Finished Goods</strong> as Storage Location. Confirm your entries by pressing Enter. If the field is shown greyed minimize Item Overview by choosing <img src="media/image30.png" style="width:0.19549in;height:0.17717in" /></td>
<td style="text-align: right;"><p>OK</p>
<p>Finished Goods</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image31.png" style="width:5.16528in;height:1.54236in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image32.png" style="width:0.26772in;height:0.17717in" /> to save your issue. The system will assign a unique material document number.</td>
<td style="text-align: right;">Material Document Number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image33.png" style="width:3.01824in;height:0.29079in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-6-display-material-inventory">Step 6: Display Material Inventory</h1></th>
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
<td colspan="2" style="text-align: left;">To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Stock Overview.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image15.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Stock Overview</em> screen, enter <strong>DXTR1###</strong> as Material (remember to replace ### with your number). Choose <img src="media/image16.png" style="width:0.41732in;height:0.17717in" />. Please be aware that your numbers may vary.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image34.png" style="width:5.16528in;height:1.18264in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Note that your amount of goods in Dallas has changed now.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">By double clicking on <em>SD00 DC San Diego</em> you can also see, that you still have an On-Order Stock balance of 10 for your distribution center in San Diego. This means that the goods have not arrived in San Diego yet.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">You can also have a look at another overview. To do so, use the app <em>Stock – Single Material</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image35.png" style="width:1.54331in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image36.png" style="width:5.16528in;height:0.90625in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image37.png" style="width:5.16528in;height:3.36736in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"></td>
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
<th colspan="2"><h1 id="step-7-display-material-inventory-value">Step 7: Display Material Inventory Value</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the value of your material inventory again.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to display the value of your material inventory again.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory value, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Warehouse Stock.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image22.png" style="width:1.55906in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Warehouse Stocks of Material</em> screen, enter <strong>DXTR1###</strong> as Material (remember to replace ### with your number). Ensure that all other search criteria fields are blank and click on <img src="media/image16.png" style="width:0.41732in;height:0.17717in" />. Please be aware that your numbers may vary.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image38.png" style="width:5.16528in;height:4.13125in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see the values associated with the material in Dallas has decreased. In addition, the value of <em>Transit/Transf.</em> for San Diego has now increased to the value of the goods on order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-8-create-goods-receipt">Step 8: Create Goods Receipt</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Receive goods at receiving plant.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to confirm the receipt of goods from Dallas by creating a goods receipt.</p>
<p><strong>Name (Position)</strong> Yoshi Agawa (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a goods receipt, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Goods Receipt Clerk</em> role the app <em>Post Goods Movement.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image24.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Goods Movement</em> screen, change the Material Document drop down to <strong>Goods Receipt</strong>, adjust the type of Goods Receipt to a <strong>Purchase Order</strong>, and input your <strong>Stock Transport Order Number</strong> in the blank space next to it. You may use the F4 help like explained in the goods issue task. Then, press Enter.</td>
<td style="text-align: right;"><p>Goods Receipt</p>
<p>Purchase Order</p>
<p>Stock Transport</p>
<p>Order Number</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">After your stock transport order comes up select <strong>OK.</strong> Make sure that <strong>SD00</strong> is chosen as Plant, <strong>101</strong> as Movement Type and <strong>FG00</strong> as Storage Location (for some of this information you may need to scroll over to the right to find it).</td>
<td style="text-align: right;"><p>OK</p>
<p>SD00</p>
<p>101</p>
<p>FG00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image39.png" style="width:4.9442in;height:1.5734in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image32.png" style="width:0.26772in;height:0.17717in" /> to save your receipt. The system will assign a unique material document number.</td>
<td style="text-align: right;">Material Document Number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image40.png" style="width:2.87057in;height:0.27294in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-9-display-material-inventory">Step 9: Display Material Inventory</h1></th>
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
<td colspan="2" style="text-align: left;">To display the material stock, use in the <em>Warehouse Management</em> area on the <em>Issue from Storage</em> page in the <em>Warehouse Supervisor</em> role the app <em>Stock - Single material</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image3.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Stock - single material</em> view, enter <strong>DXTR1###</strong> (replace ### with your number) in the Material field.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image41.png" style="width:5.16528in;height:2.57917in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Note that your amount of goods in San Diego has changed now.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image42.png" style="width:5.16528in;height:3.44583in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> To display the material inventory, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Stock Overview.</em></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image43.png" style="width:5.16528in;height:2.00486in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">By double clicking on <em>SD00 DC San Diego</em> you can see that the On-Order Stock balance is now zero for San Diego and its Unrestricted Use has been updated.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.46489in;height:0.20662in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"></td>
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
<td colspan="2"><p><strong>Task</strong> View the value of your material inventory again.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to display the value of your material inventory again.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the material inventory value, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Warehouse Stock.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image22.png" style="width:1.55906in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Warehouse Stocks of Material</em> screen, enter <strong>DXTR1###</strong> as Material (remember to replace ### with your number). Click on <img src="media/image16.png" style="width:0.41732in;height:0.17717in" />. Please be aware that your numbers may vary.</td>
<td style="text-align: right;">DXTR1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image44.png" style="width:4.71747in;height:3.01788in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see the value of <em>Transit/Transf.</em> for San Diego is now zero and its <em>Unrestricted Amount and Total Value is</em> increased.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-11-run-bin-status-report">Step 11: Run Bin Status Report</h1></th>
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
<td colspan="2" style="text-align: left;">To run a bin status report, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Supervisor</em> role the app <em>Run Bin Status Report.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image45.png" style="width:1.59543in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> (for your San Diego Warehouse) as Warehouse Number and <strong>STBN*###</strong> as Storage bin (replace ### with your number). Then, click on <img src="media/image16.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note</strong> The warehouse number is the highest level of organizational unit in warehouse management. In practice, the warehouse number usually corresponds to a physical building or distribution center. Each warehouse number has a substructure that maps the spatial relationship in the warehouse complex in details.</p>
<p><img src="media/image46.png" style="width:3.79711in;height:2.24182in" /></p>
<p>Storage bins are the lowest level of organizational structure. They are assigned to a storage type and a storage section (if one exists). Storage bins represent the physical location where the goods are stored in the warehouse.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Overview</em> screen you should see a list of all of your storage bins for the entire warehouse in San Diego. Double click on one of your storage bins to get detailed information.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image47.png" style="width:4.713in;height:2.5941in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Your bin report might look different, depending on whether you have already processed a Warehouse Management case study or not.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-12-create-transfer-order">Step 12: Create Transfer Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a transfer order.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to create a transfer order to place your goods into your storage bin. It is a handoff from inventory management to warehouse management. The system recognizes that there are goods that have been received but need to be put away.</p>
<p><strong>Name (Position)</strong> Yoshi Agawa (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a transfer order, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Goods Receipt Clerk</em> role the app <em>Display Transfer Requirement – List of Material.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> If the app is not displayed, search for it using the search bar <img src="media/image48.png" style="width:0.15973in;height:0.14584in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image49.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Transfer Requirement: List of Material</em> screen, enter <strong>100</strong> (for your San Diego Warehouse) as Warehouse Number, <strong>DXTR1###</strong> as Material (replace ### with your number) and <strong>SD00</strong> as Plant. Compare your entries with the screenshot below and then click Enter.</td>
<td style="text-align: right;"><p>100</p>
<p>DXTR1###</p>
<p>SD00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image50.png" style="width:5.16528in;height:2.33043in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Transfer Requirements for Material</em> screen, you should see a line item describing the goods, just received for your stock transport order. The requirement number should be the same as the stock transport order number, you received earlier. Make sure that the line item is selected and click on the <img src="media/image51.png" style="width:0.68898in;height:0.17717in" /> button.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image52.png" style="width:5.16528in;height:1.74097in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create TO for TR 000000XXXX 0001: Prepare for Putaway</em> screen press Enter to copy your quantity of 10 from the <em>Palletization</em> section to the <em>Items</em> section. Enter <strong>001</strong> as Sec, <strong>STBN-7-###</strong> as Destination Bin (replace ### with your number) and use F4 to select <strong>Pallet Storage</strong> as Type. Confirm your entries by pressing Enter.</td>
<td style="text-align: right;"><p>001</p>
<p>STBN-7-###</p>
<p>002 (Pallet Storage)</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image53.png" style="width:5.16528in;height:3.84514in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image54.png" style="width:0.37008in;height:0.17717in" /> to save your transfer order. The system will assign a unique transfer order number. Please write down this number.</td>
<td style="text-align: right;"><p>Transfer Order Number:</p>
<p>________________</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image55.png" style="width:2.64573in;height:0.21497in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.46489in;height:0.20662in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-13-confirm-transfer-order">Step 13: Confirm Transfer Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Confirm your transfer order.</p>
<p><strong>Short Description</strong> Use the Fiori Launchpad to confirm the transfer order you created in the previous step. This is confirming that the goods are physically in the storage bin indicated in the transfer order.</p>
<p><strong>Name (Position)</strong> Yoshi Agawa (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To confirm a transfer order, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Goods Receipt Clerk</em> role the app <em>Confirm Transfer Order.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image56.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Confirm Transfer Order: Initial Screen</em>, enter your <strong>TO Number</strong> from the previous task and <strong>100</strong> as <em>Warehouse Number</em>. Then, press Enter.</td>
<td style="text-align: right;"><p>TO Number</p>
<p>100</p></td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> If you have not written down the number you can search for it using the app <em>Display Transfer Order</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the <em>Transfer Orders: List of Resident Documents</em> you have to fill in <strong>100</strong> as Warehouse number. Then, click on <img src="media/image16.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Confirm Transfer Order: Overview of Transfer Order Items</em> screen, you should see an overview of your transfer order created in the previous step. Review all of the details to make sure you have the correct quantity and storage bin.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image57.png" style="width:5.09343in;height:1.60739in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, click on <img src="media/image54.png" style="width:0.37008in;height:0.17717in" /> to confirm your transfer order. The system will return a success message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image58.png" style="width:2.60368in;height:0.2287in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-14-run-bin-status-report">Step 14: Run Bin Status Report</h1></th>
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
<td colspan="2" style="text-align: left;">To run a bin status report, use in the <em>Warehouse Management</em> area on the <em>Stock Transport Order</em> page in the <em>Warehouse Supervisor</em> role the app <em>Run Bin Status Report.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image59.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> (for your San Diego Warehouse) as Warehouse Number and <strong>STBN*###</strong> as Storage bin (replace ### with your number). Then, click on <img src="media/image16.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image60.png" style="width:4.25473in;height:2.44945in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bin Status Report: Overview</em> screen you should see that the Storage Bin <strong>STBN-7-###</strong> is filled now. Click on your material to display detailed information of this quant and check whether 10 pieces of your goods are stored in your storage bin.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image61.png" style="width:5.16528in;height:3.84167in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image5.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="wm-ii-challenge">WM II Challenge</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><strong>Learning Objective</strong> Understand and perform a warehousing process for int. goods</td>
<td style="text-align: right;"><strong>Time</strong> 75 min</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p><strong>Motivation</strong> After having finished the <em>Warehouse Management II</em> case study successfully, you should now be able to solve the following challenge.</p>
<p><strong>Scenario</strong> The warehouse management system has been tested without any problems, so the management decided to use the system productively. The distribution center in San Diego will soon start delivering customers. In order to do so, you need to ensure that there are enough silver Deluxe Touring Bikes available on stock. Unfortunately, you cannot order any from your plants in Dallas, as there are no free resources available, because of problems with one of the assembly lines. In order to have on time 50 silver Deluxe Touring Bikes (estimation by the management) in San Diego you need to order them from your plant in Heidelberg (Germany). The delivery time is 10 days maximum.</p>
<p>As soon as the goods arrive in your DC in San Diego they need to be stored in the same bin, where the black Touring Bikes from this case study already are.</p>
<p><strong>Task Information</strong> You can use the <em>Warehouse Management II</em> case study as a guideline, but it is recommended to complete this challenge without further assistance to prove your WM skills.</p></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</tbody>
</table>
