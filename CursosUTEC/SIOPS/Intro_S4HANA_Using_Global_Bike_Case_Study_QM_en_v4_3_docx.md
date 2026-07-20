---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_QM_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_QM_en_v4.3.docx
---

Quality Management (QM)

This case study explains how quality management can be integrated in a sales and distribution process during procurement and thus fosters a thorough understanding of each process step and underlying SAP functionality.

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
<p>Quality Management</p>
<p>Authors</p>
<p>Ray Boykin</p>
<p>Tom Wilder</p>
<p>Parth Dubey</p>
<p>Tim Böttcher</p>
<p>Version</p>
<p>4.3</p>
<p>Last Update</p>
<p>Juli 2025</p></th>
<th><p>MOTIVATION</p>
<p>The purpose of this assignment is that you become familiar with the quality management in sales and Distribution</p></th>
<th></th>
<th><p>PREREQUISITES</p>
<p>Before you use this case study, you should be familiar with navigation in the SAP system.</p>
<p>You should have completed the Navigation exercise and have read the GB Story prior to starting this assignment.</p>
<p>NOTES</p>
<p>This case study uses the Global Bike data set, which has exclusively been created for SAP UA global curricula.</p>
<p>This material was prepared with the assistance of the BSIS 420/620 students at CSU Chico.</p>
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
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Learning Objective</strong> Understand and perform a Quality Management Process integrated in an Order-To-Cash Process.</p>
<p><strong>Scenario</strong> While receiving Material, you need to check the quality in order to sell high value goods. You will take on different roles within the Global Bike Inc. to perform a quality inspection on newly arrived goods and complete a Sales and Distribution process with them. You work for example as a warehouse worker, accounting clerk and sales agent. You will get insight in the Sales and Distribution (SD), the Materials Management (MM), the Financial Accounting FI and CO) and the Warehouse Management (WM) departments.</p>
<p><strong>Employees involved</strong> Catherine Dubios (Sales Representative US West)</p>
<p>Ricardo Robles (Warehouse Supervisor)</p>
<p>Sanjay Datar (Warehous Employee)</p>
<p>Juriko Hamada (Good Issue Clerk)</p>
<p>Yoshi Agawa (Goods Receipt Clerk)</p>
<p>Sunil Gupta (Warehouse Employee)</p>
<p>Karl Gruber (Sales Person 2 US West)</p>
<p>Zarah Morello (Good Issue Clerk)</p>
<p>Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 160 min</td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">You start the process by creating a new customer (Quality Bikes). They will order Bikes from Global Bike. Beforehand some goods are transferred from Dallas to San Diego. Before leaving the warehouse in Dallas, a quality inspection is performed. Afterwards they are moved to San Diego from where they are sold and sent to your customer.</td>
</tr>
</tbody>
</table>

|       The graphic below displays the complete process (22 tasks).       |
|:-----------------------------------------------------------------------:|
| <img src="media/image2.png" style="width:6.54306in;height:4.41736in" /> |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><h1 id="table-of-contents" class="TOC-Heading">Table of Contents</h1>
<p><a href="#process-overview">Process Overview <span>2</span></a></p>
<p><a href="#step-1-create-new-customer">Step 1: Create New Customer <span>5</span></a></p>
<p><a href="#step-2-extend-material-master-with-qm-view">Step 2: Extend Material Master with QM View <span>13</span></a></p>
<p><a href="#step-3-create-quality-info-record-with-customers">Step 3: Create Quality Info Record with Customers <span>16</span></a></p>
<p><a href="#step-4-create-inspection-plan">Step 4: Create Inspection Plan <span>18</span></a></p>
<p><a href="#step-5-create-stock-transport-order">Step 5: Create Stock Transport Order <span>22</span></a></p>
<p><a href="#step-6-post-goods-issue">Step 6: Post Goods Issue <span>24</span></a></p>
<p><a href="#step-7-display-inspection-lot">Step 7: Display Inspection Lot <span>26</span></a></p>
<p><a href="#step-8-perform-inspection-and-record-results">Step 8: Perform Inspection and Record Results <span>28</span></a></p>
<p><a href="#step-9-make-usage-decisions-of-inspection-lots">Step 9: Make Usage Decisions of Inspection Lots <span>30</span></a></p>
<p><a href="#step-10-create-goods-receipt">Step 10: Create Goods Receipt <span>32</span></a></p>
<p><a href="#step-11-create-transfer-order">Step 11: Create Transfer Order <span>34</span></a></p>
<p><a href="#step-12-confirm-transfer-order-i">Step 12: Confirm Transfer Order I <span>36</span></a></p>
<p><a href="#step-13-create-sales-order">Step 13: Create Sales Order <span>37</span></a></p>
<p><a href="#step-14-create-outbound-delivery">Step 14: Create Outbound Delivery <span>39</span></a></p>
<p><a href="#step-15-change-outbound-delivery">Step 15: Change Outbound Delivery <span>41</span></a></p>
<p><a href="#step-16-transfer-stock-from-warehouse-management">Step 16: Transfer Stock from Warehouse Management <span>42</span></a></p>
<p><a href="#step-17-confirm-transfer-order-ii">Step 17: Confirm Transfer Order II <span>44</span></a></p>
<p><a href="#step-18-ship-materials">Step 18: Ship Materials <span>46</span></a></p>
<p><a href="#step-19-create-invoice">Step 19: Create Invoice <span>47</span></a></p>
<p><a href="#step-20-post-invoice">Step 20: Post Invoice <span>48</span></a></p>
<p><a href="#step-21-receive-payment-from-customer">Step 21: Receive Payment from Customer <span>49</span></a></p>
<p><a href="#step-22-review-document-flow">Step 22: Review Document Flow <span>51</span></a></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 0%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="3"><h1 id="step-1-create-new-customer">Step 1: Create New Customer</h1></th>
</tr>
<tr>
<th colspan="2"><p><strong>Task</strong> Create a new customer.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create a new customer.</p>
<p><strong>Name (Position)</strong> Catherine Dubios (Sales Representative US West)</p></th>
<th colspan="2" style="text-align: right;"><strong>Time</strong> 20 min</th>
</tr>
<tr>
<th colspan="2"></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In this case study, we will create the master data for a new customer. Two types of customer data are stored about a customer – sales data and accounting data. The customer master data is created in three groups, or views – general, accounting, and sales. Customers can be created centrally, meaning that all views are generated concurrently, or responsibility can be distributed so that different personnel in the accounting and sales areas are responsible for creating and maintaining the data in their respective views. For this exercise, central creation will be used to enter all of the needed data to define a new customer.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2"></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">To create a new customer, click in the <em>Quality Management</em> area in the role <em>Sales Representative US West</em> on the app <em>Manage Business Partner Master Data</em>.</th>
<th colspan="2">Start</th>
</tr>
<tr>
<th colspan="2"><img src="media/image3.png" style="width:1.59055in;height:1.5748in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">On the <em>Manage Business Partner</em> screen, select the button <img src="media/image4.png" style="width:0.33858in;height:0.17717in" />. A submenu will open. Click <strong>Organization</strong> here.</th>
<th colspan="2">Organization</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><img src="media/image5.png" style="width:5.16528in;height:1.6in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><p><strong>Note</strong> Business Partners are created at a higher level, i.e., across departments. They can be categorized as either a person or an organization.</p>
<p><strong>Person</strong><br />
A person represents an individual natural person involved in business activities.</p>
<p><strong>Organization</strong><br />
An organization can represent various units:</p>
<ul>
<li><p>Company (e.g., a legal entity)</p></li>
<li><p>Departments, etc. (parts of a legal entity)</p></li>
<li><p>Association.</p></li>
</ul>
<p>The term "organization" is used as an umbrella term to cover all situations that can arise in daily business activities.</p>
<p><strong>Roles of Business Partners</strong></p>
<p>Specific roles are assigned to business partners, such as "Customer" or "Supplier." These roles are defined for specific organizational levels (e.g., company code, sales area).<br />
Below, you will get to know and apply the two SAP standard roles for customers:</p>
<ul>
<li><p><strong>FLCU00 | Debtor:</strong> This role stores the data for financial accounting.</p></li>
<li><p><strong>FLCU01 | Customer:</strong> This role stores the sales data.</p></li>
</ul></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">On the <em>Create Organization</em> screen, in the field <em>BP Role</em> click the help icon <img src="media/image6.png" style="width:0.19291in;height:0.17717in" />. In the pop-up that opens, search for <strong>Customer</strong> and then select the entry <strong>FLCU00 | FI Customer</strong>.</th>
<th colspan="2"><p>Customer</p>
<p>FLCU00 | FI Customer</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><img src="media/image7.png" style="width:5.16528in;height:1.65903in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Back on the <em>Create Organization</em> screen, please add the following information. As <em>Organization Title</em> choose <strong>Company (0003)</strong>, and as <em>Name 1</em> enter <strong>Quality Bikes ###</strong>. Remember to replace your three-digit number for ###, e.g. if your number is 114, please enter 114. Further, as <em>Street</em> enter <strong>Lusk Blvd</strong>. and as <em>City</em> enter <strong>San Diego</strong> (with the <em>Postal Code</em> <strong>92121</strong>). In the field <em>Country</em>, please enter <strong>US</strong>, and choose <strong>CA</strong> as <em>Region</em>. Finally, for <em>Language</em> select <strong>EN</strong>.</th>
<th colspan="2"><p>Company (0003)</p>
<p>Quality Bikes ###</p>
<p>Lusk Blvd.</p>
<p>San Diego</p>
<p>92121</p>
<p>US</p>
<p>CA</p>
<p>EN</p></th>
</tr>
<tr>
<th colspan="2"><img src="media/image8.png" style="width:5.16528in;height:2.57083in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Confirm your entries with <img src="media/image9.png" style="width:0.24803in;height:0.17717in" />.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">A new overview is generated. Make sure that you have selected the <em>Basic Data</em> tab. In the <em>General Information</em> area, in the field Search Term 1 add your three-digit number <strong>###</strong>.</th>
<th colspan="2"><p>Basic Data</p>
<p>###</p></th>
</tr>
<tr>
<th colspan="2"><img src="media/image10.png" style="width:3.50138in;height:1.54827in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Then, select the <em>Roles</em> tab. Auto-scroll will take you to the correct position. You will see a line with the details of the business partner role as well as the validity dates.</th>
<th colspan="2">Roles</th>
</tr>
<tr>
<th colspan="2"><img src="media/image11.png" style="width:5.16528in;height:0.64931in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">At the end of the line, click <img src="media/image12.png" style="width:0.19291in;height:0.17717in" /> to maintain further details.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">A new screen is loading. Select the <em>Company Codes</em> tab. Currently, there is no record maintained for the company codes, so please select <img src="media/image4.png" style="width:0.33858in;height:0.17717in" />.</th>
<th colspan="2">Company Codes</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Company Code</em> field, click the input help icon<img src="media/image13.png" style="width:0.2126in;height:0.17717in" />. The following pop-up window opens.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><img src="media/image14.png" style="width:5.16528in;height:1.15833in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Click on <strong>US00</strong> (<em>Global Bike Inc.</em>).</th>
<th colspan="2">US00</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Finance</em> area, as the <em>Reconciliation Account</em> enter <strong>1200000</strong> (<em>Trade Receivables</em>) and as the <em>Sort Key</em> choose <strong>002</strong> (<em>Doc.no., fiscal year</em>). Enter <strong>E3</strong> (Foreign) as <em>Planning Group</em>. In the field <em>Payment Terms</em>, please add <strong>0001</strong> (<em>Payable immediately Due net</em>). Make sure that the <strong>Payment History Record</strong> checkbox is choosen.</th>
<th colspan="2"><p>1200000</p>
<p>002</p>
<p>E3</p>
<p>0001</p>
<p>Payment History Record</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><img src="media/image15.png" style="width:5.16528in;height:1.67986in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Select <img src="media/image16.png" style="width:0.33858in;height:0.17717in" /> to save the draft.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Navigate to the <em>Unloading Points</em> tab. Currently no data record is maintained for the unloading point, select the button <img src="media/image4.png" style="width:0.33858in;height:0.17717in" />.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Enter <strong>Dock 1</strong> as <em>Unloading Point</em> and <strong>US</strong> as <em>Customer Calender</em>.</th>
<th colspan="2"><p>Dock1</p>
<p>US</p></th>
</tr>
<tr>
<th colspan="2"><img src="media/image17.png" style="width:5.16528in;height:0.62917in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Select <img src="media/image16.png" style="width:0.33858in;height:0.17717in" /> to save the draft. You can save the customer role by clicking<img src="media/image18.png" style="width:0.32283in;height:0.17717in" /> once again afterwards.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Select the <em>Address 🡪 Address Details</em> tab. You will see one line with the country details as well as the validity dates. Click <img src="media/image12.png" style="width:0.19291in;height:0.17717in" /> to maintain more details.</th>
<th colspan="2"><p>Address</p>
<p>Address Details</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image19.png" style="width:5.16528in;height:0.60278in" /></th>
<th colspan="2" style="text-align: left;"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Address</em> area, you can use the button <img src="media/image20.png" style="width:0.52362in;height:0.17717in" /> to display all the fields. Please find the <em>Transportation Zone</em> field and click the input help icon <img src="media/image21.png" style="width:0.17717in;height:0.17717in" />. The following pop-up window will open.</th>
<th colspan="2">Transportation Zone</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image22.png" style="width:5.16528in;height:1.17222in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Click on <strong>Region West</strong> to select it. Enter <strong>PST</strong> in the field <em>Time Zone</em> and as <em>Tax Jurisdiction</em> enter <strong>CA0000000.</strong></th>
<th colspan="2"><p>Region West</p>
<p>PST</p>
<p>CA0000000</p></th>
</tr>
<tr>
<th colspan="2"><img src="media/image23.png" style="width:5.16528in;height:3.20972in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2">Finally, use the button <img src="media/image16.png" style="width:0.33858in;height:0.17717in" /> again to save your draft.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><strong>Note</strong> In the general role of the business partner (BP), the business partner name and address is entered. The general role data is relevant for sales and distribution and for accounting. To avoid data redundancy, it is stored centrally (client-specific). It is valid for all organizational units within a client.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">To be able to add sales area data for the customer you have just created, you have to assign a new business partner role. For this purpose, select the <em>Roles</em> tab. There, choose <img src="media/image4.png" style="width:0.33858in;height:0.17717in" /> again to create a new row for another Business Partner Role.</th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the empty <em>Business Partner Role</em> field, click the input help icon <img src="media/image21.png" style="width:0.17717in;height:0.17717in" />. In the pop-up that opens, search for <strong>Customer</strong> and then select the <strong>FLCU01 | Customer</strong> entry.</th>
<th colspan="2"><p>Customer</p>
<p>FLCU01 | Customer</p></th>
</tr>
<tr>
<th colspan="2"><img src="media/image24.png" style="width:5.16528in;height:0.78472in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">At the end of the new row, you can click <img src="media/image12.png" style="width:0.19291in;height:0.17717in" /> to add more details. Select <em>Sales Areas</em> tab to maintain the sales area data of your customer. Since no record currently exists, select the button <img src="media/image4.png" style="width:0.33858in;height:0.17717in" />.</th>
<th colspan="2">Sales Areas</th>
</tr>
<tr>
<th colspan="2"><img src="media/image25.png" style="width:5.16528in;height:0.70208in" /></th>
<th colspan="2"></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Sales Organization</em> field enter <strong>UW00</strong>, as the <em>Distribution Channel</em> enter <strong>WH</strong> (<em>Wholesale</em>), and as the <em>Division</em> choose <strong>BI</strong> (<em>Bicycles</em>). Press enter.</th>
<th colspan="2"><p>UW00</p>
<p>WH</p>
<p>BI</p></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">Next, please select the <em>Sales Area Details</em> tab. In the <em>Sales Orders</em> area, as <em>Sales District</em> enter <strong>US0002</strong> (<em>Southwest USA</em>) and make sure that as the <em>Currency</em> <strong>USD</strong> is specified.</th>
<th><p>Sales Area Details</p>
<p>US0002</p>
<p>USD</p></th>
</tr>
<tr>
<th colspan="3" style="text-align: center;"><p><img src="media/image26.png" style="width:2.28926in;height:0.75708in" /></p>
<p>…</p>
<p><img src="media/image27.png" style="width:2.22689in;height:0.3546in" /></p></th>
<th></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">In the <em>Billing</em> area, as the <em>Incoterms</em> type in <strong>FOB</strong> (<em>Free on Board</em>) and as the <em>Incoterms Location 1</em> <strong>San Diego</strong>. In the <em>Payment Terms</em> field, please add <strong>0001</strong> (<em>payable immediately due net</em>).</th>
<th><p>FOB</p>
<p>San Diego</p>
<p>0001</p></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;"><strong>Note</strong> Incoterms (abbreviation for <strong>In</strong>ternational <strong>Co</strong>mmercial <strong>Terms</strong>) are internationally accepted terms of delivery published by the International Chamber of Commerce (ICC) for international commercial law.</th>
<th>Incoterms</th>
</tr>
<tr>
<th colspan="3"><p><img src="media/image28.png" style="width:2.7603in;height:2.8649in" /></p>
<p>…</p>
<p><img src="media/image29.png" style="width:2.69688in;height:0.44567in" /></p></th>
<th></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">Subsequently, fill in data for the <em>Shipping</em> area. In the fields <em>Delivery Priority</em> and <em>Shipping Conditions</em>, use the drop-down lists to select <strong>Normal item</strong> and <strong>Standard</strong> in chronological order. As the <em>Delivery Plant</em> enter <strong>SD00</strong> (<em>San Diego</em>).</th>
<th><p>Normal item</p>
<p>Standard</p>
<p>SD00</p></th>
</tr>
<tr>
<th colspan="3" style="text-align: center;"><img src="media/image30.png" style="width:2.94939in;height:1.70299in" /></th>
<th></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">In the <em>Accounting</em> area, as the <em>Account assignment group</em> select <strong>Domestic Revenue</strong>. In the following <em>Partial Deliveries</em> area, in the field <em>Partial Delivery Per Item</em>, please use the drop-down list and select <strong>Partial delivery allowed</strong>. Last but not least, enter data for the final area of this tab, <em>Pricing and Statistics</em>. In the <em>Price Group</em> field, use the drop-down list to select <strong>Bulk buyer</strong> and as the <em>Customer Pricing Procedure</em> enter <strong>1</strong> (<em>Standard</em>). Compare your entries with the following screenshots and confirm your entries with enter.</th>
<th><p>Domestic Revenue</p>
<p>Partial delivery allowed</p>
<p>Bulk Buyer</p>
<p>1</p></th>
</tr>
<tr>
<th colspan="3"><img src="media/image31.png" style="width:5.22917in;height:1.03542in" /></th>
<th></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">Then, please select the <em>Taxes</em> tab. For all three tax categories choose the <em>Tax Classification</em> <strong>0</strong> (<em>Exempt</em>).</th>
<th><p>Taxes</p>
<p>0</p></th>
</tr>
<tr>
<th colspan="3" style="text-align: center;"><img src="media/image32.png" style="width:3.91751in;height:1.33601in" /></th>
<th></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">Select <img src="media/image16.png" style="width:0.33858in;height:0.17717in" /> to save your adjustments as a draft. Then press <img src="media/image33.png" style="width:0.29921in;height:0.17717in" /> again to finish editing the customer role. To finally save the business partner, use the <img src="media/image34.png" style="width:0.35827in;height:0.17717in" /> button in the lower screen area.</th>
<th></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">The SAP system will create the master data record for the new BP and assign a unique business partner number. Write down the BP number, which you can find in the header area.</th>
<th></th>
</tr>
<tr>
<th colspan="3" style="text-align: center;"><img src="media/image35.png" style="width:3.05713in;height:1.28521in" /></th>
<th></th>
</tr>
<tr>
<th colspan="3">Click on the home icon <img src="media/image36.png" style="width:0.35433in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</th>
<th></th>
</tr>
<tr>
<th colspan="3" style="text-align: right;"></th>
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
<th colspan="2"><h1 id="step-2-extend-material-master-with-qm-view">Step 2: Extend Material Master with QM View</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Extend material master with QM view.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to extend a material master record for a Bike to add data for the quality management view.</p>
<p><strong>Name (Position)</strong> Ricardo Robles (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a finished good material master record, click in the <em>Quality Management</em> area in the role <em>Warehouse Supervisor</em> on the app <em>Create Material</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:1.6513in;height:0.50653in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">This will produce the following screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image38.png" style="width:3.40088in;height:2.39223in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Material field</em>, type in <strong>ORWN1###</strong> (replace ### with your number) and select <strong>Mechanical Engineering</strong> as an Industry sector.</td>
<td style="text-align: right;"><p>ORWN1###</p>
<p>Mechanical Engineering</p></td>
</tr>
<tr>
<td colspan="2">Then, click on <img src="media/image39.png" style="width:0.48819in;height:0.17717in" /> to proceed. Confirm any warning message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the following popup, select the view <strong>Quality Management</strong> by clicking on the square in front of the row.</td>
<td style="text-align: right;">Quality Management</td>
</tr>
<tr>
<td colspan="2">Also, select <strong>Create views selected</strong>. Then, click on <img src="media/image40.png" style="width:0.18898in;height:0.17717in" />.</td>
<td style="text-align: right;">Create views selected</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:2.6154in;height:3.54229in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Organizational Levels</em> screen, enter <em>plant</em> <strong>DL00</strong> (Dallas). Then, click on <img src="media/image40.png" style="width:0.18898in;height:0.17717in" />.</td>
<td style="text-align: right;">DL00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image42.png" style="width:5.16528in;height:1.51806in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">On the <em>Quality Management</em> tab select <img src="media/image43.png" style="width:0.94094in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Plant DL00 Material ORWN1### : Inspection Setup Data</em> screen create a new Inspection Type by clicking on <img src="media/image44.png" style="width:0.84646in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter Type <strong>02</strong> for <em>InspType</em> and mark it as <strong>active</strong>.</td>
<td style="text-align: right;"><p>02</p>
<p>Active</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image45.png" style="width:5.16528in;height:1.24167in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Choose<img src="media/image46.png" style="width:0.17717in;height:0.17717in" /> to check your entries and show detailed information on the inspection type.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the detailed information uncheck <strong>Automatic UD</strong> and compare the screen with the screenshot below.</td>
<td style="text-align: right;">Automatic UD - unchecked</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image47.png" style="width:5.16528in;height:3.83542in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Proceed with <img src="media/image40.png" style="width:0.18898in;height:0.17717in" />. Then, click on <img src="media/image48.png" style="width:0.29134in;height:0.17717in" /> to save your material.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image49.png" style="width:2.17307in;height:0.30456in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image36.png" style="width:0.35433in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-3-create-quality-info-record-with-customers">Step 3: Create Quality Info Record with Customers</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a quality info record with customers.</p>
<p><strong>Short Description</strong> In this task, you create a quality information record with the customer.</p>
<p><strong>Name (Position)</strong> Ricardo Robles (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a quality info record, click in the <em>Quality Management</em> area in the role <em>Warehouse Supervisor</em> on the app <em>Create Quality Info Record – Sales</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image50.png" style="width:1.59449in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If a quality assurance agreement or a vendor release is required for a material, you must create a quality information record (quality info record). The quality info record determines how the material can be processed further.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">This will produce the following screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image51.png" style="width:2.4333in;height:1.50781in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If your customer number is not entered by default, then search for your new customer using the F4 help with search term <strong>###</strong>.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2">Enter <strong>UW00</strong> as <em>Sales Organization</em> and proceed with <em>Enter</em>.</td>
<td style="text-align: right;">UW00</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image52.png" style="width:0.72835in;height:0.17717in" /> button on the application tool bar. This should produce the following screen:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image53.png" style="width:5.16528in;height:2.49167in" /></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your Material <strong>ORWN1###</strong> and make sure that <strong>Before delivery</strong> is selected in the <em>Quality inspection</em> area.</td>
<td style="text-align: right;"><p>ORWN1###</p>
<p>Before delivery</p></td>
</tr>
<tr>
<td colspan="2">Proceed with <img src="media/image54.png" style="width:0.18898in;height:0.17717in" />. Then, click on <img src="media/image55.png" style="width:0.27559in;height:0.17717in" /> to save your Info record.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image36.png" style="width:0.35433in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-4-create-inspection-plan">Step 4: Create Inspection Plan</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create an inspection plan.</p>
<p><strong>Short Description</strong> In this task, you create an inspection plan for the material you created.</p>
<p><strong>Name (Position)</strong> Ricardo Robles (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create an inspection plan, click in the <em>Quality Management</em> area in the role <em>Warehouse Supervisor</em> on the app <em>Manage Inspection Plans</em>.</td>
<td style="text-align: left;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image56.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> With the help of an inspection plan, you describe how a quality inspection of one or more materials should run. In the inspection plan, you specify the order in which certain inspection procedures are carried out and which inspection characteristics are to be checked against which specifications</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image57.png" style="width:0.37008in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Manage Inspection Plans</em> view, under the <em>General</em> tab, enter <strong>DL00</strong> as the <em>Plant</em>, <strong>6</strong> as the <em>usage</em>, and <strong>4</strong> as the <em>overall status</em>. Additionally, enter <strong>EA</strong> as the <em>unit of measure</em>. Compare the entries with the following screen.</td>
<td style="text-align: right;"><p>DL00</p>
<p>6</p>
<p>4</p>
<p>EA</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image58.png" style="width:5.16528in;height:1.38542in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Continue with the <em>Material Assignment</em> tab. Click on <img src="media/image59.png" style="width:0.71654in;height:0.17717in" />. Search in the pop-up for the material <strong>ORWN1###*</strong>.</td>
<td style="text-align: right;">ORWN1###*</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image60.png" style="width:5.16528in;height:1.63472in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then please select the <strong>ORWN1###</strong> entry that is assigned to plant <strong>DL00</strong>.</td>
<td style="text-align: right;"><p>ORWN1###</p>
<p>DL00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image61.png" style="width:5.16528in;height:0.66736in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the <em>Operations</em> tab and click on <img src="media/image57.png" style="width:0.37008in;height:0.17717in" />. Enter the <em>control key</em> <strong>QM01</strong> and the <em>description</em> <strong>Quality Inspection</strong> for operation 0010.</td>
<td style="text-align: right;"><p>QM01</p>
<p>Quality Inspection</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image62.png" style="width:5.16528in;height:0.78542in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the row with <em>operation 0010</em>, then select the <em>Characteristics</em> tab and click on <img src="media/image63.png" style="width:0.25197in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <strong>Pack</strong> as the <em>master inspection characteristic</em> and <strong>Packing OK</strong> as the <em>inspection characteristic description</em>.</td>
<td style="text-align: right;"><p>Pack</p>
<p>Packing OK</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image64.png" style="width:5.16528in;height:0.53611in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the <em>control Indicators</em><img src="media/image65.png" style="width:0.28609in;height:0.2274in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the checkboxes for <em>Characteristic Attribute</em> and <em>Sampling</em> <em>Procedure</em> . Ensure that <em>Summarized Recording</em> and <em>Required Characteristic</em> are selected. Choose <em>Fixed Scope</em> and <em>No Documentation</em>.</td>
<td style="text-align: right;"><p>Charac. Attribute</p>
<p>Sampling proc.</p>
<p>Summ.Recording</p>
<p>Required Charact.</p>
<p>Fixed scope</p>
<p>No documentation</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image66.png" style="width:2.38549in;height:2.90505in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Then confirm your selection with <img src="media/image67.png" style="width:0.23228in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the row <em>Master Inspection Characteristic PACK</em>, go to the <em>Catalog</em> tab, and select the selected Set <strong>PACK</strong> in plant Dallas.</td>
<td style="text-align: right;"><p>PACK</p>
<p>DL00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image68.png" style="width:5.16528in;height:0.93542in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Sample</em> tab, enter <strong>100%-0</strong> as the <em>Sampling Procedure</em>. Additionally, enter <strong>1</strong> as the <em>base sample Quantity</em> and <strong>EA</strong> as the <em>sample unit of measure</em>.</td>
<td style="text-align: left;"><p>100%-0</p>
<p>1</p>
<p>EA</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image69.png" style="width:5.16528in;height:1.21319in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Continue with <img src="media/image70.png" style="width:0.29528in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the <em>Inspection Plan</em> you created.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image71.png" style="width:5.16528in;height:0.86806in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <img src="media/image72.png" style="width:0.29134in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Proceed as with the previous steps for <em>characteristic 0020</em>, using <em>Master Inspection Characteristics</em> <strong>COLOR</strong> and <strong>Color OK</strong> as the <em>description of the inspection characteristic</em>.</td>
<td style="text-align: right;"><p>COLOR</p>
<p>Color OK</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image73.png" style="width:5.16528in;height:1.13542in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Make sure to enter <strong>COLOR</strong> as the <em>selected Set</em> in the <em>Catalog</em> tab. All other data can be used as for characteristic 0010 PACK.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image74.png" style="width:5.16528in;height:1.23958in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image75.png" style="width:0.31102in;height:0.17717in" /> to save.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the <img src="media/image36.png" style="width:0.35433in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</td>
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
<col style="width: 68%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-5-create-stock-transport-order">Step 5: Create Stock Transport Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create Stock Transport Order</p>
<p><strong>Short Description</strong> In this task, you create a Stock Transport Order for 10 Women’s Off Road Bike from Dallas to San Diego</p>
<p><strong>Name (Position)</strong> Sanjay Datar (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a stock transport order, click in the <em>Quality Management</em> area in the role <em>Warehouse Supervisor</em> on the app <em>Create Purchase Order</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image76.png" style="width:1.61024in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create Purchase Order</em> screen, enter <strong>Stock Transp. Order</strong> as Order Type. You will find Order Type next to the shopping cart <img src="media/image77.png" style="width:1.33858in;height:0.17717in" /> icon. As Supplying Plant choose <strong>DL00</strong>. In the Org. Data tab enter <strong>US00</strong> as Purchase Org<em>.</em>, <strong>N00</strong> as Purch. Group and <strong>US00</strong> as Company Code.</td>
<td style="text-align: right;"><p>Stock Transp. Order</p>
<p>DL00</p>
<p>US00</p>
<p>N00</p>
<p>US00</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image78.png" style="width:4.71309in;height:1.3968in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Expand Items by clicking <img src="media/image79.png" style="width:0.70866in;height:0.17717in" />. Enter the <em>Material</em> <strong>ORW1###</strong> with a <em>PO Quantity</em> of <strong>10</strong>. The <em>Delivery Date</em> shall be <strong>one week from today’s date</strong>. As <em>Plant</em> enter <strong>SD00</strong> and choose the <em>Stor. Location</em> <strong>FG00</strong>.</td>
<td style="text-align: right;"><p>ORWN1###</p>
<p>10</p>
<p>One week from today</p>
<p>SD00</p>
<p>FG00</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image80.png" style="width:5.08947in;height:0.44686in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image75.png" style="width:0.31102in;height:0.17717in" /> to save. Confirm the following popup by clicking on <em>Save.</em></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">The system wants to make sure that the delivery date can be met.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will get a message, that your Order is created. Write down the number you will need it in the next step.</td>
<td style="text-align: right;"><p>Stock Transpnr.</p>
<p>………………………….</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image81.png" style="width:3.28356in;height:0.28456in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the <img src="media/image36.png" style="width:0.35433in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-6-post-goods-issue">Step 6: Post Goods Issue</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create goods issue</p>
<p><strong>Short Description</strong> In this task, you ship the materials to San Diego by posting goods issue.</p>
<p><strong>Name (Position)</strong> Juriko Hamada (Good Issue Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Posting goods issue reduces the inventory quantities and value in Dallas.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post a goods issue, click in the <em>Quality Management</em> area in the role <em>Good Issue Clerk</em> on the app <em>Post Goods Movement</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image82.png" style="width:1.54724in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the following Screen choose <strong>Goods Issue</strong> and <strong>Purchase Order</strong>. Enter in Purchasing Document Number <strong>your</strong> <strong>Stock Transport Order Number</strong> right to Purchase Order.</td>
<td style="text-align: right;"><p>Goods Issue</p>
<p>Purchase Order</p>
<p>Order Number</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image83.png" style="width:5.16528in;height:1.29306in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <em>Movement type</em> <strong>351</strong>. You will find the box to fill in on the top right of the screen. Proceed with <em>Enter.</em></td>
<td style="text-align: right;">351</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image84.png" style="width:2.72859in;height:0.5322in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Your data from the stock transport order is copied to the line item section. Enter <strong>FG00</strong> as Storage Location and mark your line with the 10 Women’s Off Road Bikes as <strong>OK</strong>. If the <em>“Detail Data”</em> section is active you have to make your entries there or close the section with a click on <img src="media/image85.png" style="width:0.21654in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>FG00</p>
<p>Check - OK</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image86.png" style="width:5.16528in;height:1.62778in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image87.png" style="width:0.23622in;height:0.17717in" />. You will receive the following message:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image88.png" style="width:3.7078in;height:0.31851in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the <img src="media/image36.png" style="width:0.35433in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-7-display-inspection-lot">Step 7: Display Inspection Lot</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the Inspection Lot.</p>
<p><strong>Short Description</strong> In this task, you Display the Inspection Lot, which is created for the inspection.</p>
<p><strong>Name (Position)</strong> Juriko Hamada (Good Issue Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the created inspection lot, click in the <em>Quality Management</em> area in the role <em>Good Issue Clerk</em> on the app <em>Manage Inspection Lots</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image89.png" style="width:1.54724in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In <em>Manage Inspection Lots</em> enter the <strong>material number</strong> <strong>(ORWN1###)</strong> in the <em>material field</em>. Click on <img src="media/image90.png" style="width:0.2126in;height:0.17717in" />.</td>
<td style="text-align: right;">ORWN1###</td>
</tr>
<tr>
<td colspan="2"><img src="media/image91.png" style="width:5.16528in;height:1.55347in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see a row with the details of the inspection lot. Click on the row to maintain further details.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Origin</em> tab, you will find the source that created the inspection lot. In this case, you will find the previously created material document. You will also find information about the lot Quantity and the sample size.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image92.png" style="width:5.16528in;height:1.75417in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Also check the other tabs for further information about the inspection lot.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image36.png" style="width:0.35433in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-8-perform-inspection-and-record-results">Step 8: Perform Inspection and Record Results</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Perform the inspection and recording of the results</p>
<p><strong>Short Description</strong> In this task, you perform the inspection, you record the results, and you make the usage decision for the inspection lot.</p>
<p><strong>Name (Position)</strong> Juriko Hamada (Good Issue Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To perform the inspection, click in the <em>Quality Management</em> area in the role <em>Good Issue Clerk</em> on the app <em>Record Inspection Results</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image93.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Record Inspection Results</em> Screen enter the Number of your Inspection Lot. Click on <img src="media/image90.png" style="width:0.2126in;height:0.17717in" />.</td>
<td style="text-align: right;">Inspection Lot Number</td>
</tr>
<tr>
<td colspan="2"><img src="media/image94.png" style="width:5.02942in;height:1.46103in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Select your Inspection Lot and click on <img src="media/image95.png" style="width:0.99213in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image96.png" style="width:0.24803in;height:0.17717in" />. Select the <em>code group</em> <strong>COLOR</strong> with the <em>code</em> <strong>4</strong> (green) for both inspection objects using the value help symbol <img src="media/image97.png" style="width:0.17501in;height:0.17501in" />. Then enter <strong>10</strong> as <em>Inspected</em> and <strong>0</strong> as <em>Nonconforming</em> for both inspection objects.</td>
<td style="text-align: right;"><p>COLOR - 4</p>
<p>10</p>
<p>0</p></td>
</tr>
<tr>
<td colspan="2">The status should change to <em>Valuated</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image98.png" style="width:5.16964in;height:1.88385in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Now, save your progress by clicking on <img src="media/image75.png" style="width:0.31102in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-9-make-usage-decisions-of-inspection-lots">Step 9: Make Usage Decisions of Inspection Lots</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Make Usage Decisions on Inspection Lots</p>
<p><strong>Short Description</strong> In this task, you make usage decisions on the inspected lots that you performed in the previous step</p>
<p><strong>Name (Position)</strong> Juriko Hamada (Good Issue Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To perform the usage decision, click in the <em>Quality Management</em> area in the role <em>Good Issue Clerk</em> on the app <em>Manage Usage Decision</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image100.png" style="width:1.53543in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Manage Usage Decisions</em> screen, select <strong>your inspection lot</strong> and click on <img src="media/image101.png" style="width:0.22047in;height:0.17717in" />.</td>
<td style="text-align: right;">Inspection Lot</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image102.png" style="width:5.16528in;height:1.54861in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on your <em>inspection lot</em> to view detailed information.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image96.png" style="width:0.24803in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Usage Decision</em> tab, use the F4 help to find the usage decision code for <strong>Goods issue</strong> and <strong>Accept</strong> in plant 0001.</td>
<td style="text-align: right;">Goods issue<br />
Accept</td>
</tr>
<tr>
<td colspan="2"><img src="media/image103.png" style="width:5.16528in;height:2.69931in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The <em>usage decision</em> should now look like this.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image104.png" style="width:3.33213in;height:0.60075in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image75.png" style="width:0.31102in;height:0.17717in" /> to save your usage decision.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-10-create-goods-receipt">Step 10: Create Goods Receipt</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create Goods Receipts</p>
<p><strong>Short Description</strong> In this task, you receive the materials into San Diego.</p>
<p><strong>Name (Position)</strong> Yoshi Agawa (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a goods receipt, click in the <em>Quality Management</em> area in the role <em>Goods Receipt Clerk</em> on the app <em>Post Goods Movement</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image105.png" style="width:1.59449in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the follwoing screen change the Trans./Event to <strong>Goods Receipt</strong>. As Reference Document<em>,</em> choose <strong>Purchase Order</strong>. You find both drop down menu on the top right.</td>
<td style="text-align: right;"><p>Goods Receipt</p>
<p>Purchase Order</p></td>
</tr>
<tr>
<td colspan="2">Use the F4-Help or <img src="media/image97.png" style="width:0.17501in;height:0.17501in" /> to choose your Purchase Order.</td>
<td style="text-align: right;">Your Purchase Order</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image106.png" style="width:5.16528in;height:1.32222in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Press <em>Enter</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If the Details data is active, close it by clicking on <img src="media/image107.png" style="width:0.20866in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter the <em>movement Type</em> <strong>101</strong> and as <em>Storage Location</em> <strong>FG00</strong>. At last select the Item <strong>OK</strong> checkbox.</td>
<td style="text-align: right;"><p>101</p>
<p>FG00</p>
<p>Item OK</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image108.png" style="width:4.66531in;height:1.4152in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image87.png" style="width:0.23622in;height:0.17717in" />. You will receive the following message:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image109.png" style="width:2.99978in;height:0.35444in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-11-create-transfer-order">Step 11: Create Transfer Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a Transfer Order</p>
<p><strong>Short Description</strong> In this task, you create a transfer order for your materials.</p>
<p><strong>Name (Position)</strong> Sunil Gupta (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a transfer order, click in the <em>Quality Management</em> area in the role <em>Warehouse Employee</em> on the app <em>Display Transfer Requirement – List for Material</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> If the app is not displayed, search for it by using the search bar <img src="media/image110.png" style="width:0.19291in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image111.png" style="width:3.37782in;height:0.41172in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Transfer Requirement: List for Material</em> screen, enter the <em>Warehouse Number</em> <strong>100</strong>, the <em>Material</em> <strong>ORWN1###</strong>, the <em>Plant</em> <strong>SD00</strong> and the <em>Storage Location</em> <strong>FG00</strong>.</td>
<td style="text-align: right;"><p>100</p>
<p>ORWN1###</p>
<p>SD00</p>
<p>FG00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image112.png" style="width:5.16528in;height:2.50139in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Proceed with <em>enter</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Transfer Requirements for Material</em> screen, select the row with goods receipt for purchase order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image113.png" style="width:5.16528in;height:1.47639in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the <img src="media/image114.png" style="width:0.7126in;height:0.17717in" /> icon. In the <em>Create TO from TR: Prepare for Putaway</em> screen, press <em>enter</em> to copy the <em>Dest. Target quantity</em>. Also enter pallet storage <strong>002</strong> as <em>Type</em> and total section <strong>001</strong> as <em>Sec</em>.</td>
<td style="text-align: right;"><p>002</p>
<p>001</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image115.png" style="width:5.16528in;height:0.62778in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image116.png" style="width:0.35433in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Write down your Transfer Order Number you will need it in the next step.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image117.png" style="width:2.69914in;height:0.30823in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-12-confirm-transfer-order-i">Step 12: Confirm Transfer Order I</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Confirm Transfer Order I</p>
<p><strong>Short Description</strong> In this task, you create a transfer order for your materials.</p>
<p><strong>Name (Position)</strong> Sunil Gupta (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To confirm a transfer order, click in the <em>Quality Management</em> area in the role <em>Warehouse Employee</em> on the app <em>Confirm Transfer Order</em>.</td>
<td style="text-align: left;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image118.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If your Data is not filled in automatically in the screen <em>Confirm Transfer Order: Initial Screen</em>, enter for <em>TO Number</em> <strong>your Transfer Order Number</strong> for and the <em>Warehouse Number</em> <strong>100</strong>.</td>
<td style="text-align: right;"><p>Your Transfer Order Number</p>
<p>100</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image119.png" style="width:2.9153in;height:1.16095in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Proceed with <em>Enter</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Confirm Transfer Order: Overview of Transfer Order Items</em> screen, click on the <img src="media/image116.png" style="width:0.35433in;height:0.17717in" /> icon to post your transfer order. You will receive the following message:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image120.png" style="width:2.84203in;height:0.34992in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-13-create-sales-order">Step 13: Create Sales Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a sales order.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create a sales order.</p>
<p><strong>Name (Position)</strong> Karl Gruber (Sales Person 2 US West)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a sales order, click in the <em>Quality Management</em> area in the role <em>Sales Representative US West</em> on the app <em>Manage Sales Orders – Version 2</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image121.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Manage Sales Orders – Version 2</em> screen, click on <img src="media/image122.png" style="width:0.41339in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter the <em>Sales order type</em> <strong>OR</strong>. For organizational data, enter the <em>sales organization</em> <strong>UW00</strong>, the <em>distribution channel</em> <strong>WH</strong>, and the <em>division</em> <strong>BI</strong>.</td>
<td style="text-align: right;"><p>OR</p>
<p>UW00</p>
<p>WH</p>
<p>BI</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image123.png" style="width:1.81545in;height:2.22539in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then click on <img src="media/image124.png" style="width:0.37795in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Sales Order</em> screen, search for <strong>your customer</strong> using the F4 help as the <em>Sold-to party</em>. Also, enter <strong>your customer</strong> as the <em>Ship-to Party</em>. Enter <strong>PO-###</strong> as the <em>customer reference</em>. Enter <strong>today's date</strong> as the <em>Requested delivery date</em>.</td>
<td style="text-align: right;"><p>Your Customer Number</p>
<p>PO-###</p>
<p>today's date</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image125.png" style="width:5.16528in;height:2.66736in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Items</em> section enter the <em>Product</em> <strong>ORWN1###</strong> with an Requested Quantity of <strong>10</strong>.</td>
<td style="text-align: right;"><p>ORWN1###</p>
<p>10</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image126.png" style="width:5.16528in;height:0.86667in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Confirm your entries with with <img src="media/image127.png" style="width:0.37402in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image128.png" style="width:2.05382in;height:1.03285in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-14-create-outbound-delivery">Step 14: Create Outbound Delivery</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create an Outbound Delivery.</p>
<p><strong>Short Description</strong> In this task, you prepare the material for shipment by creating an outbound delivery, which contains the storage location from which the materials will be picked, and the shipping point to which the material will be delivered for shipment.</p>
<p><strong>Name (Position)</strong> Zarah Morello (Good Issue Clerk)</p></td>
<td style="text-align: right;"><blockquote>
<p><strong>Time</strong> 5 min</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a sales order, click in the <em>Quality Management</em> area in the role <em>Good Issue Clerk</em> on the app <em>Create Outbound Deliveries From Sales Orders</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image129.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the search mask, enter your <strong>business partner number</strong> in the <em>Ship-to party</em> field.</td>
<td style="text-align: right;">business partner number</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong>: Alternatively, if you have forgotten your BP number, click the value help icon <img src="media/image97.png" style="width:0.17501in;height:0.17501in" /> in the Ship-to Party field . A pop-up will open. In the Name 1 field, enter *### and San Diego as the City and press <img src="media/image130.png" style="width:0.22441in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>*###</p>
<p>San Diego</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select your customer and accept the entry with <img src="media/image131.png" style="width:0.22441in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In addition, enter <strong>SD00</strong> as the <em>shipping point</em> and remove the <em>Planned creation date</em>. Press <img src="media/image130.png" style="width:0.22441in;height:0.17717in" /> to execute the search. The prepared sales order is displayed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image132.png" style="width:5.16528in;height:1.45486in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select your sales order and choose the button <img src="media/image133.png" style="width:0.89764in;height:0.17717in" />. You will see that the sales order is no longer available. You will receive a confirmation that your outbound delivery has been created.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image134.png" style="width:1.79032in;height:0.44589in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-15-change-outbound-delivery">Step 15: Change Outbound Delivery</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Pick material.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to pick materials.</p>
<p><strong>Name (Position)</strong> Zarah Morello (Good Issue Clerk)</p></td>
<td style="text-align: right;"><blockquote>
<p><strong>Time</strong> 5 min</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To change the outbound delivery, click the <em>Change Outbound Delivery</em> app in the <em>Quality Management</em> area in the <em>Goods Issue Clerk</em> role.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image135.png" style="width:2.72955in;height:0.51049in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Outbound delivery</em> field, enter your <strong>outbound delivery number</strong>.</td>
<td style="text-align: right;">outbound delivery number</td>
</tr>
<tr>
<td colspan="2"><img src="media/image136.png" style="width:3.05592in;height:1.2757in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image137.png" style="width:0.43701in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the <em>picking</em> area and enter <strong>FG00</strong> as the <em>storage location</em>.</td>
<td style="text-align: right;">FG00</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image138.png" style="width:5.16528in;height:1.64514in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Save your delivery by clicking on <img src="media/image139.png" style="width:0.2874in;height:0.17717in" />. Write down your delivery number, you will need it in the following steps.</td>
<td style="text-align: right;"><p>outbound delivery number</p>
<p>………………….</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image140.png" style="width:2.84906in;height:0.26093in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-16-transfer-stock-from-warehouse-management">Step 16: Transfer Stock from Warehouse Management</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Transfer stock from Warehouse Management.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to transfer stock from warehouse management.</p>
<p><strong>Name (Position)</strong> Zarah Morello (Good Issue Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To transfer stock from WM, click in the <em>Quality Management</em> area in the role <em>Good Issue Clerk</em> on the app <em>Create Transfer Order – Outbound Delivery</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image141.png" style="width:1.59449in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create Transfer Order for Delivery Note: Initial Screen</em>, enter the <em>Warehouse Number</em> <strong>100</strong>, the <em>Plant</em> <strong>SD00</strong> and search for <strong>your Delivery Number</strong> if not filled in automatically. Select the Checkbox for <em>Activate Item</em>. Choose <strong>System-Guided</strong> as Foreground/Backgrnd Processing. Finally choose <strong>1</strong> (include picking quantities in delivery) for <em>Adopt Pick Quantity.</em></td>
<td style="text-align: right;"><p>100</p>
<p>SD00</p>
<p>Your Delivery Number</p>
<p>Activate Item -checked</p>
<p>System-Guided</p>
<p>1</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image142.png" style="width:3.39425in;height:3.27926in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Proceed with <em>Enter</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the next screen click on <img src="media/image143.png" style="width:0.40157in;height:0.17717in" /> to post your transfer order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Write down your Transfer Order Number you will need it in the next step.</td>
<td style="text-align: right;">Transfer order number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image144.png" style="width:2.99628in;height:0.31835in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-17-confirm-transfer-order-ii">Step 17: Confirm Transfer Order II</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Confirm the second Transfer Order.</p>
<p><strong>Short Description</strong> In this task, you will confirm the transfer order for your materials.</p>
<p><strong>Name (Position)</strong> Zarah Morello (Good Issue Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To confirm the transfer order, click in the <em>Quality Management</em> area in the role <em>Good Issue Clerk</em> on the app <em>Confirm Transfer Order</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image145.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Confirm Transfer Order: Initial Screen</em>, enter <strong>your TO Number</strong><em>,</em> which you received in step 15, and the <em>Warehouse Number</em> <strong>100</strong>. Make sure, <strong>Pick + Transfer</strong> is checked in the <em>Confirmation</em> section.</td>
<td style="text-align: right;"><p>TO Number</p>
<p>100</p>
<p>Pick + Transfer</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image146.png" style="width:2.4185in;height:3.85601in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Proceed with <em>Enter</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Review your confirmation Data:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image147.png" style="width:5.16528in;height:2.19583in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Confirm your transfer order with <img src="media/image143.png" style="width:0.40157in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image148.png" style="width:2.77637in;height:0.33778in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-18-ship-materials">Step 18: Ship Materials</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Ship the ordered materials to your customer.</p>
<p><strong>Short Description</strong> In this task, you ship the material to the customer by posting goods issue. Posting goods issue indicates a change in ownership in the goods and reduces the inventory quantities and value in the inventory quantities and value in the San Diego plant</p>
<p><strong>Name (Position)</strong> Zarah Morello (Good Issue Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To confirm the transfer order, click in the <em>Quality Management</em> area in the role <em>Good Issue Clerk</em> on the app <em>Manage Outbound Deliveries</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image149.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your <strong>customer number</strong> as the <em>Ship-to Party</em>. Click on <img src="media/image150.png" style="width:0.21654in;height:0.17717in" />.</td>
<td style="text-align: right;">customer number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image151.png" style="width:5.16528in;height:0.90208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <em>your delivery document</em> and click on <img src="media/image152.png" style="width:0.52362in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image153.png" style="width:2.59198in;height:1.1246in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the <em>goods issue date</em> as <strong>today's date</strong> and then click on <img src="media/image154.png" style="width:0.52362in;height:0.17717in" />.</td>
<td style="text-align: right;">today's date</td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-19-create-invoice">Step 19: Create Invoice</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create the invoice for your customer.</p>
<p><strong>Short Description</strong> In this task, you will prepare the invoice that you use to bill a customer.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">With the delivery complete, the customer can be invoiced. To create an invoice, click in the <em>Quality Management</em> area in the role <em>AR Accountant</em> on the app <em>Create Billing Documents</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image155.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note:</strong> The billing document serves several important functions:</p>
<ul>
<li><p>It is the sales and distribution document that helps you to generate invoices.</p></li>
<li><p>The billing document serves as a data source for financial accounting to help you to monitor and process customer payments.</p></li>
<li><p>When you create a billing document, the G/L accounts will normally be updated automatically.</p></li>
</ul></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Create Billing Document</em> screen, enter your <em>business partner</em> <strong>Quality Bikes ###</strong> in the <em>search field</em> and click <img src="media/image156.png" style="width:0.21654in;height:0.17717in" />. Select your sales document and then click <img src="media/image157.png" style="width:1.05512in;height:0.17717in" />.</td>
<td style="text-align: right;">Quality Bikes ###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image158.png" style="width:5.05535in;height:1.22544in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">On the following screen click on<img src="media/image159.png" style="width:0.29921in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">You will receive a message, that your Billing document has been saved.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-20-post-invoice">Step 20: Post Invoice</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Post the invoice you have just created.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to post the invoice.</p>
<p><strong>Name (Position)</strong> Catherine Dubios (AR Accountant)</p></td>
<td style="text-align: right;"><blockquote>
<p><strong>Time</strong> 5 min</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post your invoice, click in the <em>Quality Management</em> area in the role <em>AR Accountant</em> on the app <em>Manage Billing Documents</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image160.png" style="width:1.60236in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Manage Billing Document</em> screen, enter your <em>business partner</em> <strong>Quality Bikes ###*</strong> in the <em>search field</em> and click <img src="media/image156.png" style="width:0.21654in;height:0.17717in" />. Your billing document currently has the status "To Be Posted".</td>
<td style="text-align: right;">Quality Bikes ###*</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image161.png" style="width:5.16528in;height:1.45417in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Select your billing document. Click on <img src="media/image162.png" style="width:0.29921in;height:0.17717in" />. This changes the status of your invoice to "Completed".</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image163.png" style="width:5.16528in;height:0.47778in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-21-receive-payment-from-customer">Step 21: Receive Payment from Customer</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Receive the Payment for the previously processed order.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to receive payment from your customer.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post the incoming payment, click in the <em>Quality Management</em> area in the role <em>AR Accountant</em> on the app <em>Post Incoming Payments</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image164.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Post Customer Payments</em> enter <strong>US00</strong> for <em>Company Code.</em> Enter the <strong>current date</strong> for the <em>posting date</em> and for <em>Journal Entry Date.</em> Enter the <strong>current period</strong> as the <em>period</em> and make sure that <strong>DZ</strong> (customer payment) is selected as the <em>Journal Entry Type</em>.</td>
<td style="text-align: right;"><p>US00</p>
<p>Current date</p>
<p>Current period</p>
<p>DZ</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Amount fields</em> enter the <strong>amount from the Sales Order to be paid</strong> (Net Value = 25000) and <strong>USD</strong> for Currency/Rate, <strong>1810000</strong> (your bank GL Number) for G/L Account<em>.</em></td>
<td style="text-align: right;"><p>25000</p>
<p>USD</p>
<p>1810000</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image165.png" style="width:5.16528in;height:1.42292in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Under <em>Open item Selection</em>, choose <strong>Customer</strong> in the drop down and enter the <strong>customer number</strong> from the Sales Order in the Account Typ field.</td>
<td style="text-align: right;"><p>Customer</p>
<p>Your customer number</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image166.png" style="width:5.16528in;height:1.85208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Once the information hast been entered, proceed with click on <img src="media/image167.png" style="width:0.64173in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The Balance will change<img src="media/image168.png" style="width:1.30709in;height:0.17717in" />. In the section <em>Proposed Items,</em> the Payment appears. Click on <img src="media/image169.png" style="width:0.77953in;height:0.17717in" /> next to it.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The Clear status changes to <img src="media/image170.png" style="width:0.79134in;height:0.17717in" />. Once again the Balance is even <img src="media/image171.png" style="width:0.91732in;height:0.17717in" />. Click on <img src="media/image172.png" style="width:0.26772in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image173.png" style="width:2.77149in;height:1.08574in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-22-review-document-flow">Step 22: Review Document Flow</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Review the document flow.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to review the document flow.</p>
<p><strong>Name (Position)</strong> Catherine Dubios (Sales Representative US West)</p></td>
<td style="text-align: right;"><blockquote>
<p><strong>Time</strong> 5 min</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To review the document flow, click in the <em>Quality Management</em> area in the role <em>Sales Representative US West</em> on the app <em>Manage Sales Orders – Version 2</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image174.png" style="width:1.59449in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Manage Sales Orders – Version 2</em> screen, enter your <em>customer reference</em> <strong>PO-###</strong> and click on <img src="media/image175.png" style="width:0.22441in;height:0.17717in" />.</td>
<td style="text-align: right;">PO-###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image176.png" style="width:5.16528in;height:1.51111in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the line of your sales order that is now displayed to you.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Sales Order</em> screen, click on <em>Process Flow</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image177.png" style="width:5.16528in;height:2.21042in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on your <em>Standard order</em> and then click on <em>Display Document Flow – Sales Order</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image178.png" style="width:3.04905in;height:1.81598in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">This will generate the following screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image179.png" style="width:5.16528in;height:2.27153in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image99.png" style="width:0.38428in;height:0.17656in" /> to go to the Fiori Launchpad Overview.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>
