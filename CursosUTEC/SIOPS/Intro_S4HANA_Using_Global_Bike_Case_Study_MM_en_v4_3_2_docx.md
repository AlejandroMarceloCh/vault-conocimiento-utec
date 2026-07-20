---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_MM_en_v4.3 (2)
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_MM_en_v4.3 (2).docx
---

Materials Management (MM)

This case study explains an integrated materials management process in detail. This promotes a thorough understanding of each process step and the underlying SAP functions.

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
<p>Bachelor's degree</p>
<p>Masters</p>
<p>Beginner</p>
<p>Focus</p>
<p>Materials Management</p>
<p>Authors</p>
<p>Bret Wagner</p>
<p>Stefan Weidner</p>
<p>Version</p>
<p>4.3</p>
<p>Last Change</p>
<p>July 2025</p></th>
<th><p>MOTIVATION</p>
<p>In the exercises for Materials Management, a procurement process was tracked with master and transaction data that had already been created.</p>
<p>This case study explains and executes a complete material procurement process from the creation of master data, through purchasing to payment for the delivered goods.</p></th>
<th></th>
<th><p>PREREQUISITES</p>
<p>Before you process the case study, you should familiarize yourself with the navigation in the SAP system.</p>
<p>To successfully perform this MM case study, it is not necessary to have completed all MM exercises. However, it is recommended.</p>
<p>NOTES</p>
<p>This case study uses the model company Global Bike, which was developed exclusively for SAP UA Curricula.</p>
<p><img src="media/image2.png" style="width:1.68893in;height:0.62765in" alt="M:\Curricula\Vorlagen\Logo_Global Bike\Global_Bike_Logo_neu_2018\Logo1.png" /></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="media/image3.png" style="width:1.36042in;height:0.73264in" alt="SAP_UniversityAlliances_scrn_R_pos_stac3" />

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="process-overview" class="P68B1DB1-berschrift16">Process Overview</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Learning objective</strong> Understand and execute an integrated procurement process.</p>
<p><strong>Scenario</strong> To process a complete procurement process, you will assume various roles within Global Bike, for example: Purchaser, Warehouse Worker, Accounting Clerk. In general, you will work in the Materials Management (MM) and Financial Accounting (FI) departments.</p>
<p><strong>Employees involved</strong> Joyce Hausman (Contract Manager)</p>
<p>Sandeep Das (Warehouse Supervisor)</p>
<p>Sergey Petrov (Warehouse Employee)</p>
<p>Wilton Saban (Inventory Supervisor)</p>
<p>Alberto Conti (Inventory Assistant)</p>
<p>Aura Maxwell (Purchasing Agent 2)</p>
<p>Tatiana Karsova (Goods Receipt Clerk)</p>
<p>Silvia Cassano (AP Accountant)</p>
<p>Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 170 min</td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">Before you start the procurement process, you must create a new supplier (Mid-West Supply from Lincoln). You then create the new master record for a trading good (chain closing) in the system. After the stock is checked (empty), you initiate the procurement by creating a purchase requisition. You then generate a request for quotation and maintain the quotations for three different vendors (including your new vendor). After evaluating and accepting the bid from Mid-West Supply, you create a purchase order with reference to the original purchase quotation. You will then post the goods receipt document and confirm the physical receipt into warehouse stock. After creating two partial invoices, you will post the payment to the supplier and finally check all involved G/L accounts in financial accounting. The following graphic shows the entire process.</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><img src="media/image4.png" style="width:6.41732in;height:3.46603in" /></td>
</tr>
<tr>
<td colspan="3"><h1 id="table-of-contents" class="P68B1DB1-Inhaltsverzeichnisberschrift9">Table of Contents</h1>
<p><a href="#process-overview">Process Overview <span>2</span></a></p>
<p><a href="#step-1-create-vendor">Step 1: Create Vendor <span>4</span></a></p>
<p><a href="#step-2-create-material">Step 2: Create Material <span>8</span></a></p>
<p><a href="#step-3-change-material">Step 3: Change Material <span>13</span></a></p>
<p><a href="#step-4-display-stock">Step 4: Display Stock <span>15</span></a></p>
<p><a href="#step-5-create-purchase-requisition">Step 5: Create Purchase Requisition <span>18</span></a></p>
<p><a href="#step-6-manage-stock">Step 6: Manage Stock <span>20</span></a></p>
<p><a href="#step-7-create-rfq">Step 7: Create RFQ <span>22</span></a></p>
<p><a href="#step-8-create-quotation-from-vendor">Step 8: Create Quotation from Vendor <span>24</span></a></p>
<p><a href="#step-9-price-based-bid-evaluation">Step 9: Price Based Bid Evaluation <span>26</span></a></p>
<p><a href="#step-10-create-purchase-order-referencing-an-rfq">Step 10: Create Purchase Order Referencing an RFQ <span>28</span></a></p>
<p><a href="#step-11-display-purchase-order">Step 11: Display Purchase Order <span>32</span></a></p>
<p><a href="#step-12-post-goods-receipt-for-purchase-order">Step 12: Post Goods Receipt for Purchase Order <span>33</span></a></p>
<p><a href="#step-13-check-received-goods">Step 13: Check Received Goods <span>37</span></a></p>
<p><a href="#step-14-check-physical-goods-receipt">Step 14: Check Physical Goods Receipt <span>40</span></a></p>
<p><a href="#step-15-create-and-post-the-first-supplier-invoice">Step 15: Create and Post the First Supplier Invoice <span>42</span></a></p>
<p><a href="#step-16-display-purchase-order-history">Step 16: Display Purchase Order History <span>45</span></a></p>
<p><a href="#step-17-display-document-flow">Step 17: Display Document Flow <span>47</span></a></p>
<p><a href="#step-18-post-goods-receipt-for-purchase-order">Step 18: Post Goods Receipt for Purchase Order <span>49</span></a></p>
<p><a href="#step-19-check-physical-goods-receipt">Step 19: Check Physical Goods Receipt <span>51</span></a></p>
<p><a href="#step-20-create-and-post-the-second-supplier-invoice">Step 20: Create and Post the Second Supplier Invoice <span>53</span></a></p>
<p><a href="#step-21-post-outgoing-payment">Step 21: Post Outgoing Payment <span>56</span></a></p>
<p><a href="#step-22-display-supplier-balance">Step 22: Display Supplier Balance <span>58</span></a></p>
<p><a href="#step-23-display-purchase-order-history">Step 23: Display Purchase Order History <span>60</span></a></p>
<p><a href="#step-24-display-account-balances">Step 24: Display account balances <span>62</span></a></p>
<p><a href="#mm-challenge">MM Challenge <span>64</span></a></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-1-create-vendor" class="P68B1DB1-berschrift16">Step 1: Create Vendor </h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a new supplier.</p>
<p><strong>Description</strong> Use the SAP Fiori launchpad to create a new supplier (Mid-West Supply).</p>
<p><strong>Name (position)</strong> Joyce Hausman (Contract Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 20 min</td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Suppliers are used in both financials and procurement. The master record of a vendor includes 3 categories – General Data, Finance, and Procurement. Vendors can be created centrally or with shared responsibilities. During central creation, all views are generated in one step and by one person. In the case of shared responsibility, finance and procurement create the views that are relevant for them. In this case study, the vendor is created centrally. As a result, the vendor master record contains all the information required to perform business transactions.</td>
<td style="text-align: right;">Vendor Master</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a new supplier, go to the <em>Materials Management</em> space. In the role of <em>Contract Manager</em>, you can use the <em>Manage Business Partner Master Data</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image5.png" style="width:1.56299in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">The following screen appears:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image6.png" style="width:5.20619in;height:1.76865in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Manage Business Partners</em> screen, choose <img src="media/image7.png" style="width:0.37008in;height:0.17717in" /> and <strong>Organization</strong>.</td>
<td style="text-align: left;">Organization</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create Organization</em> popup window, leave the Business Partner field blank. The system will generate a unique number later. In the <em>BP Role</em> field, click <img src="media/image8.png" style="width:0.16142in;height:0.17717in" /> and in the <em>Select: BP Role</em> window, select <strong>FI Vendor (FLVN00)</strong>.</td>
<td style="text-align: right;">FLVN00</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For the <em>Organization Title</em> field, select <strong>Company (0003)</strong> and enter <strong>Mid-West Supply ###</strong> as the <em>Name 1</em>. Compare your entries with the following screenshot.</td>
<td style="text-align: right;"><p>Company (0003)</p>
<p>Mid-West Supply ###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image9.png" style="width:4.95621in;height:2.50454in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image10.png" style="width:0.22835in;height:0.17717in" />. In the <em>Business Partner</em> view, in the <em>Basic Data</em> area, enter your three-digit number (<strong>###</strong>) as <em>Search Term 1</em>.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Address</em> area and in the <em>Street</em> field, enter <strong>335 W Industrial Lake Dr</strong>, for <em>Postal Code</em> <strong>68528</strong>, for <em>City</em>, enter <strong>Lincoln</strong>, for <em>Country</em> <strong>US</strong> and <em>Region</em> <strong>NE</strong>. Under <em>Standard Communication</em>, select <strong>English (EN)</strong> as the <em>language</em>. Compare your entries with the following screenshot.</td>
<td style="text-align: right;"><p>335 W Industrial Lake</p>
<p>Dr</p>
<p>68528 Lincoln</p>
<p>US</p>
<p>NE</p>
<p>English</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image11.png" style="width:4.9919in;height:3.89275in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Identification</em> tab and click <img src="media/image12.png" style="width:0.38337in;height:0.16668in" /> in the <em>Tax Numbers</em> section. In the line that appears, enter <strong>US1</strong> <em>as the Tax Category</em> and <strong>12-3456###</strong> as the <em>Tax Number</em> – replace ### with your number.</td>
<td style="text-align: right;"><p>US1</p>
<p>12-3456###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image13.png" style="width:5.08234in;height:1.39284in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now go back to the <em>Roles</em> area and click <img src="media/image12.png" style="width:0.38337in;height:0.16668in" />. Choose <strong>Vendor (FLVN01)</strong> as the <em>Business Partner Role</em>.</td>
<td style="text-align: right;">FLVN01</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now click <img src="media/image14.png" style="width:0.20836in;height:0.23962in" /> in the row of the newly created business partner role.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image15.png" style="width:5.20963in;height:0.88653in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can now maintain company code-specific data for your business partner in the role of the vendor. Go to the <em>Company Codes</em> area and click <img src="media/image12.png" style="width:0.38337in;height:0.16668in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>New Company Code</em> screen, enter <strong>US00</strong> in the <em>Company Code</em> field. Select the value in the selection help that appears automatically. Confirm with Enter.</td>
<td style="text-align: right;">US00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image16.png" style="width:5.01514in;height:1.93437in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Switch to the <em>Finance</em> tab and enter <strong>3300000 (Trade payables)</strong> for <em>the Reconciliation Account</em>. In the Payment Data section, enter <strong>0001 (Payable immediately Due net)</strong> as the <em>Payment Terms</em> and select <strong>Check</strong> <strong>Double Invoice</strong>. Compare your entries with the following screenshot.</td>
<td style="text-align: right;"><p>3300000</p>
<p>0001</p>
<p>Check Duplicate Invoice</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image17.png" style="width:5.04179in;height:1.40993in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now switch to the <em>Correspondence</em> area. Enter <strong>your user</strong> (LEARN-###) as the <em>Clerk ID at Supplier</em>. Now click <img src="media/image18.png" style="width:0.36319in;height:0.17717in" /> in the lower screen area.</td>
<td style="text-align: right;">Your User</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Back on the <em>New Business Partner</em> screen, go to the Purchasing Organizations area to enhance your Mid-West Supply business partner with purchasing-specific data.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image19.png" style="width:5.18838in;height:0.95277in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image7.png" style="width:0.37008in;height:0.17717in" /> in the <em>Purchasing Organization</em> window. In the <em>Purchasing Organization</em> field, enter <strong>US00</strong>.</td>
<td style="text-align: right;">US00</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Purchasing Organizations</em> tab, enter <strong>USD</strong> as the <em>Order Currency</em> and use the <strong>F4 help</strong> to search for the <em>Payment Terms</em> <strong>Payable immediately Due net (0001)</strong>.</td>
<td style="text-align: right;"><p>USD</p>
<p>Payable immediately Due net (0001)</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Navigate to the <em>Partner Functions</em> tab<em>.</em> Click on <img src="media/image7.png" style="width:0.37008in;height:0.17717in" /> and enter the partner function <strong>VN</strong> for vendor and press Enter.</td>
<td style="text-align: right;">VN</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image20.png" style="width:5.08655in;height:0.69173in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image18.png" style="width:0.36319in;height:0.17717in" /> to transfer your purchasing-specific data for your business partner. Then click <img src="media/image21.png" style="width:0.40644in;height:0.17717in" /> and then <img src="media/image22.png" style="width:0.38337in;height:0.17502in" />. The system automatically assigns a unique number to your supplier.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image23.png" style="width:2.2052in;height:1.32662in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image24.png" style="width:0.34252in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 68%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-2-create-material" class="P68B1DB1-berschrift16">Step 2: Create Material</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create the material master record for a trading good.</p>
<p><strong>Description</strong> Use the SAP Fiori launchpad to create the wholesale chain lock master data.</p>
<p><strong>Name (position)</strong> Sandeep Die (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 20 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create materials, go to the <em>Materials Management</em> space. In the role of <em>Warehouse Supervisor</em>, you can use the <em>Manage Product Master Data</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image25.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image26.png" style="width:5.14652in;height:1.74624in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">On the Manage <em>Product Master Data</em> screen, click <img src="media/image12.png" style="width:0.38337in;height:0.16668in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create Master Data Record</em> dialog box that appears, enter <strong>CHLK1###</strong> as the <em>Product Number</em> and <strong>HAWA (Trading Goods)</strong> as the <em>Product Type</em>. Enter <strong>EA (Each)</strong> as the base unit of measure for the <em>Product Group</em> <strong>UTIL (Utilities)</strong>. Furthermore, enter <strong>Chain Lock ###</strong> as the description.</td>
<td style="text-align: right;"><p>CHLK1###</p>
<p>HAWA</p>
<p>UTIL</p>
<p>EA</p>
<p>Chain Lock ###</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image27.png" style="width:4.41463in;height:2.19403in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image10.png" style="width:0.22835in;height:0.17717in" />. On the <em>General Information</em> tab page in the <em>Basic Data</em> section, enter <strong>Accessories (AS)</strong> for the <em>Division</em>.</td>
<td style="text-align: right;">Accessories (AS)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Descriptions</em> section, click <img src="media/image7.png" style="width:0.37008in;height:0.17717in" />. Enter the <em>Product</em> <strong>Kettenschloss ###</strong> for language <em>DE</em> (German), replace ### with your number. Confirm your entries with Enter.</td>
<td style="text-align: right;">Kettenschloss ###</td>
</tr>
<tr>
<td colspan="2"><img src="media/image28.png" style="width:2.73256in;height:1.11595in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Scroll down to the <em>Units of Measure</em> section. At the end of the line in which the unit of measure EA is already entered, click <img src="media/image29.png" style="width:0.13123in;height:0.19685in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Unit of Measure</em> screen, on the <em>Dimensions</em> tab page, enter <strong>65</strong> for the <em>Gross Weight</em> and <strong>OZ (ounce)</strong> as the <em>Unit</em>.</td>
<td style="text-align: right;"><p>65</p>
<p>OZ</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image30.png" style="width:5.01255in;height:1.18837in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image18.png" style="width:0.36319in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now go to the <em>Sales</em> area and enter <strong>0001 (On pallets)</strong> as the <em>Transportation Group</em>. Afterwards, navigate to the <em>Distribution Chains</em> area and choose <img src="media/image12.png" style="width:0.38337in;height:0.16668in" />.</td>
<td style="text-align: right;">0001</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Distribution Chain</em> screen, enter <em>Sales Organization</em> <strong>UE00 (US East)</strong>, <em>Distribution Channel</em> <strong>WH (Wholesale)</strong>, and <em>Delivery Plant</em> <strong>MI00 (DC Miami)</strong>.</td>
<td style="text-align: right;"><p>UE00</p>
<p>WH</p>
<p>MI00</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image31.png" style="width:4.27486in;height:2.59812in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Grouping Terms</em> area, choose <strong>NORM (Standard item)</strong> for the <em>Item Category Group</em>.</td>
<td style="text-align: right;">NORM</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Sales Tax</em> area and choose <em>Tax Classification</em> <strong>0 (Exempt)</strong> for all three tax categories.</td>
<td style="text-align: right;">0 (Exempt)</td>
</tr>
<tr>
<td colspan="2"><img src="media/image32.png" style="width:3.70517in;height:1.61984in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image18.png" style="width:0.36319in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Back on the <em>Product</em> screen, navigate to the <em>Plants</em> area and click <img src="media/image12.png" style="width:0.38337in;height:0.16668in" />. On the <em>Plant</em> screen, in the <em>General Data</em> section, enter <strong>MI00 (DC Miami)</strong> for <em>Plant</em> and in the Sales Section, enter <strong>Hand lift</strong> for <em>Loading Group</em>.</td>
<td style="text-align: right;"><p>MI00</p>
<p>Hand lift</p></td>
</tr>
<tr>
<td colspan="2"><p><img src="media/image33.png" style="width:2.88467in;height:0.74427in" /></p>
<p><img src="media/image34.png" style="width:2.79979in;height:0.77283in" /></p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now go to the <em>Purchasing</em> area and enter <strong>N00 (North America)</strong> as the <em>Purchasing Group</em>.</td>
<td style="text-align: right;">N00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image35.png" style="width:5.12199in;height:1.10344in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>MRP Data</em> area and enter the <em>MRP Type</em> <strong>PD (MRP)</strong>, <em>the MRP Controller</em> <strong>000</strong> <strong>(MI MRP Controller)</strong>, and the <em>Availability Check</em> <strong>02 (Individual Requirement)</strong>.</td>
<td style="text-align: right;"><p>PD</p>
<p>000</p>
<p>02</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image36.png" style="width:2.79161in;height:1.69924in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Lot-Size Data</em> section, enter <strong>EX (Lot-for-lot order quantity)</strong> as the <em>Lot-Sizing Procedure</em> and <strong>10</strong> as the <em>Minimum Lot Size</em>.</td>
<td style="text-align: right;"><p>EX</p>
<p>10</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:3.02328in;height:1.62104in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the <em>Procurement</em> section, for <em>Planned Delivery Time</em>, enter <strong>6</strong> (days).</td>
<td style="text-align: right;">6</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image38.png" style="width:5.10309in;height:1.4424in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Switch to the <em>Storage Locations</em> tab page and choose <img src="media/image12.png" style="width:0.38337in;height:0.16668in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <strong>TG00</strong> <strong>(Trading Goods)</strong> for the <em>Storage Location</em> field.</td>
<td style="text-align: right;">TG00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image39.png" style="width:3.27642in;height:1.21351in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image18.png" style="width:0.36319in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Product</em> screen, please navigate to the <em>Valuation Areas</em> area and click <img src="media/image12.png" style="width:0.38337in;height:0.16668in" />. On the <em>Valuation Area</em> screen, enter <em>Valuation Area</em> <strong>MI00</strong> and <em>Valuation Class</em> <strong>3100 (Trading goods)</strong>.</td>
<td style="text-align: right;"><p>MI00</p>
<p>3100</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image40.png" style="width:5.18969in;height:2.41451in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Valuation</em> area and enter <strong>32.00</strong> USD as the <em>Inventory Price</em> and ensure that <strong>Moving Average Price/Periodic Unit Price (V)</strong> is selected for <em>Price Control</em>.</td>
<td style="text-align: right;">32.00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:5.20713in;height:0.70651in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image18.png" style="width:0.36319in;height:0.17717in" /> and then click <img src="media/image22.png" style="width:0.38337in;height:0.17502in" />. Your material has now been created.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the home icon <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the Fiori Launchpad Overview.</td>
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
<th colspan="2"><h1 id="step-3-change-material" class="P68B1DB1-berschrift16">Step 3: Change Material</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Extend a material master record.</p>
<p><strong>Description</strong> Extend the distribution chain of the new trading goods (chain closure) to enable the San Diego plant to maintain another condition.</p>
<p><strong>Name (position)</strong> Sergey Petrov (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create new views for a trading good, please go to the <em>Materials Management</em> space. In the role of <em>Warehouse Employee</em>, you can use the <em>Manage Product Master Data</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image43.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your material number <strong>CHLK1###</strong> (replace ### with your number) in the <em>Product</em> field and click <img src="media/image44.png" style="width:0.20079in;height:0.17717in" />.</td>
<td style="text-align: right;">CHLK1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image45.png" style="width:5.08284in;height:1.76728in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the line with your material.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Product</em> screen, click <img src="media/image46.png" style="width:0.24803in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Navigate to the <em>Distribution Chains</em> area and click <img src="media/image12.png" style="width:0.38337in;height:0.16668in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Distribution Chain</em> screen, in the <em>General Information</em> section, enter <em>Sales Organization</em> <strong>UW00 (US West)</strong>, <em>Distribution Channel</em> <strong>WH (Wholesale)</strong>, and <em>Delivery Plant</em> <strong>SD00 (San Diego</strong>).</td>
<td style="text-align: right;"><p>UW00</p>
<p>WH</p>
<p>SD00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image47.png" style="width:5.18135in;height:1.06632in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Grouping Terms</em> area, choose <strong>0001 (Make-to-order)</strong> for the <em>Item Category Group</em>.</td>
<td style="text-align: right;">0001</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Sales Tax</em> area, ensure that <em>Tax Classification</em> <strong>0 (Exempt)</strong> is entered for all three tax categories.</td>
<td style="text-align: right;">0 (Exempt)</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image48.png" style="width:3.10962in;height:1.36849in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image18.png" style="width:0.36319in;height:0.17717in" /> and then click <img src="media/image49.png" style="width:0.30836in;height:0.17502in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Finally, press <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to get to the Fiori Launchpad Overview.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-4-display-stock" class="P68B1DB1-berschrift16">Step 4: Display Stock</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Display the current stock.</p>
<p><strong>Description</strong> View the current stock for your chain lock and the demand for this product. The report should show that there is no provision for this and therefore no lock is currently available.</p>
<p><strong>Name (position)</strong> Wilton Saban (Inventory Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The stock is dynamic. As a result, it always changes when the affected material is used in a transaction.</td>
<td style="text-align: right;">Stock</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the stock, go to the <em>Materials Management</em> space. In the role of <em>Inventory Supervisor</em>, you can use the <em>Stock - Single Material</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image50.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will be directed to the following screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image51.png" style="width:5.11381in;height:0.7876in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To find the material number of your bike lock, click in the <em>Material</em> field and then click <img src="media/image52.png" style="width:0.18504in;height:0.17717in" />. In the <em>Material</em> field, enter your number in the format <strong>*###</strong>.</td>
<td style="text-align: right;">*###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image53.png" style="width:5.10268in;height:1.11144in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image54.png" style="width:0.20079in;height:0.17717in" /> to search. Double-click your material CHLK1###. Your stock should look like this:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image55.png" style="width:5.059in;height:2.031in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If you do not see the <em>Stock history</em> column, click on <img src="media/image56.png" style="width:0.22441in;height:0.17717in" /> and then on <img src="media/image57.png" style="width:0.20866in;height:0.17717in" />and select <em>Stock history.</em></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image58.png" style="width:1.80199in;height:2.45341in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then click on <img src="media/image59.png" style="width:0.4252in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the DC Miami row, in the <em>Stock History</em> column, click the<img src="media/image60.png" style="width:0.75197in;height:0.19685in" />icon. The system will now display the stock history of your material CHLK1### in DC MI00.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image61.png" style="width:5.0309in;height:2.61784in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Since the material has just been created and no stocks have been posted yet, the stock history in all key figures is 0.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Close the window and click the Home button <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-5-create-purchase-requisition" class="P68B1DB1-berschrift16">Step 5: Create Purchase Requisition</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Create a purchase requisition.</p>
<p><strong>Description</strong> The sales management has informed the purchasing department that an advertising campaign is starting in 3 months to introduce the new chain key. Create a demand (purchase requisition) for 200 of your locks so that you can choose the supplier that best meets your needs from any quotations.</p>
<p><strong>Name (position)</strong> Wilton Saban (Inventory Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a purchase requisition, please go to the <em>Materials Management</em> space. In the role of <em>Inventory Supervisor</em>, you can use the <em>My Purchase Requisition -</em> <em>New</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image62.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You should now see the following screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image63.png" style="width:5.17709in;height:2.34698in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image64.png" style="width:0.58661in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <em>Material</em> <strong>CHLK1###</strong> (## - replace with your number), press Enter. The Short Tex, Material Group, Valuation Price und Price Unit will be added automatically.</td>
<td style="text-align: right;">CHLK1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <strong>200</strong> as the <em>Quantity Requested</em>. For the <em>Delivery Date</em>, you choose <strong>today in</strong> <strong>3 months</strong>.</td>
<td style="text-align: right;"><p>200</p>
<p>Today in 3 months</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> The requested quantity is displayed with three decimal places. Therefore, your 200 is displayed as 200.000.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image65.png" style="width:5.22688in;height:1.19858in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>At the very end, enter the following message under the Notes heading and on the <em>Item text</em> tab page:</p>
<p>“Global Bike formally requests quotations for the following material. Quotations will be accepted until [01.day of next month].“</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image66.png" style="width:4.46949in;height:1.0499in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image67.png" style="width:0.32283in;height:0.17717in" /> and then to <img src="media/image68.png" style="width:0.3622in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image69.png" style="width:2.73626in;height:0.89713in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Close the notification and then click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-6-manage-stock" class="P68B1DB1-berschrift16">Step 6: Manage Stock</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Manage the stock.</p>
<p><strong>Description</strong> Display the stock/requirements list of your existing chain key and check which requirements exist for this product.</p>
<p><strong>Name (position)</strong> Alberto Conti (Inventory Assistant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please go to the <em>Materials Management</em> space. In the role of <em>Inventory Assistant</em>, you can use the <em>Stock (Single Material)</em> app to display the stock/requirements list.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image50.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Stock – Single Material</em> screen, in the <em>Material</em> field, enter your chain lock <strong>CHLK1###</strong>. Your warehouse/demand list should look similar to the screenshot below.</td>
<td style="text-align: right;">CHLK1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image70.png" style="width:5.16415in;height:1.50405in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the DC Miami row, in the Stock History column, click the icon <img src="media/image71.png" style="width:0.55118in;height:0.19685in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The system will now display the stock history of your material CHLK1### in DC MI00.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image72.png" style="width:5.20863in;height:2.70439in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> As you can see, the creation of the purchase requisition has not influenced the stock development.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad</td>
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
<th colspan="2"><h1 id="step-7-create-rfq" class="P68B1DB1-berschrift16">Step 7: Create RFQ</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a request for quotation for your purchase requisition.</p>
<p><strong>Description</strong> Create one request for each supplier. This is used to collect all relevant information (such as pricing, delivery, and so on) that is needed to select the supplier that best meets your requirements.</p>
<p><strong>Name (position)</strong> Aura Maxwell (Purchasing Agent 2)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a request for quotation for your purchase requisition, go to the <em>Materials Management</em> space. In the role of <em>Purchasing Agent</em>, you can use the <em>Process Purchase Requisitions</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image73.png" style="width:1.55512in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the <em>Search</em> field enter you material <strong>CHLK1###</strong> and click <img src="media/image74.png" style="width:0.24409in;height:0.17717in" /> .</td>
<td style="text-align: right;">CHLK1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image75.png" style="width:5.14717in;height:1.07848in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Select the row with your Purchase Requisition and click <img src="media/image76.png" style="width:0.51575in;height:0.17717in" /> .</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Process Purchase Requisitions</em> window enter <strong>Request for Quote</strong> as <em>RFQ Type</em>, <strong>RFQ1###</strong> as <em>RFQ Description,</em> <strong>one month from today</strong> as the <em>Quotation Deadline,</em> <strong>US00</strong> for the <em>Purchasing Organization</em> and <em>Company Code.</em></td>
<td style="text-align: right;"><p>Request for Quote</p>
<p>RFQ1###</p>
<p>One month from today</p>
<p>US00</p>
<p>US00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image77.png" style="width:5.14582in;height:1.36973in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bidders</em> area click on <img src="media/image78.png" style="width:0.19685in;height:0.17717in" /> to add a new bidder.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Search for your supplier <strong>Mid-West Supply ###</strong>. Please make sure selecting your supplier from the proposal list and click <img src="media/image79.png" style="width:0.42126in;height:0.17717in" /> to add them as bidder.</td>
<td style="text-align: right;">Mid-West Supply ###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image80.png" style="width:5.1854in;height:0.72827in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat this procedure to add the suppliers <strong>Dallas Bike Basics</strong> and <strong>Spy Gear</strong> as bidders.</td>
<td style="text-align: right;"><p>Dallas Bike Basic</p>
<p>Spy Gear</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> You recognize your supplier by the last three digits of the supplier number. For example, supplier number 103<strong>105</strong> represents supplier Dallas Bike Basics for user LEARN-<strong>105</strong>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image81.png" style="width:5.11535in;height:1.54653in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Note that in the <em>Items</em> section your purchase requisition was added.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image82.png" style="width:5.21115in;height:0.77506in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image83.png" style="width:0.42126in;height:0.17717in" /> and confirm the pop up with <img src="media/image83.png" style="width:0.42126in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will get a success message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image84.png" style="width:2.85018in;height:1.09851in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Close the pop up and click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-8-create-quotation-from-vendor" class="P68B1DB1-berschrift16">Step 8: Create Quotation from Vendor</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Maintain the quotation from a supplier.</p>
<p><strong>Description</strong> After we receiving responses to our purchase requisition from our suppliers, it is necessary to maintain the respective information in our procurement system in order to create comparability with which we can support the choice of supplier.</p>
<p><strong>Name (position)</strong> Alberto Conti (Inventory Assistant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Materials Management</em> space. In the role of <em>Inventory Assistant</em>, you can use the <em>Manage RFQs</em> app to create a request for quotation for your purchase requisition.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image85.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Search</em> field enter <strong>RFQ1###</strong> and click <img src="media/image86.png" style="width:0.22441in;height:0.17717in" />.</td>
<td style="text-align: right;">RFQ1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image87.png" style="width:4.80354in;height:1.89057in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the row with your Request for Quote. Go to the <em>Bidders</em> area. Select your bidder Mid-West Supply ### and click <img src="media/image88.png" style="width:0.82677in;height:0.17717in" /> to create a quotation.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image89.png" style="width:5.17142in;height:1.15373in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Supplier Quotation</em> window enter <strong>three weeks from today</strong> as <em>Quotation Submission Date</em> and <strong>NB</strong> as <em>Follow-On Document Type.</em></td>
<td style="text-align: right;"><p>Three weeks from today</p>
<p>NB</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image90.png" style="width:4.94981in;height:2.01376in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> The submission date must not be after the end of the bid period. You can find the quotation deadline unter <em>general Information.</em></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Items</em> are enter <strong>32.00</strong> USD as <em>Net Order Price.</em></td>
<td style="text-align: right;">32.00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image91.png" style="width:5.19879in;height:1.26914in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image92.png" style="width:0.33858in;height:0.17717in" /> to create the Quotation. Click <img src="media/image93.png" style="width:0.38583in;height:0.17717in" /> to submit the Quotation. If you don't see the Submit button, enlarge your browser window.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image94.png" style="width:1.72913in;height:0.5657in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image95.png" style="width:0.16929in;height:0.17717in" /> to return to the <em>Request for Quotation</em> window. The quotation from your supplier Mid-West Supply ### can now be found in the <em>Quotations</em> area.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Repeat this process for the other two bidders. Enter the following prices:</p>
<p>Dallas Bike Basics <strong>36.50</strong> USD</p>
<p>Spy Gear <strong>35.00</strong> USD</p>
<p>Make sure you save both requests and take note of the success messages.</p></td>
<td style="text-align: right;"><p>Dallas Bike Basics</p>
<p>36.50</p>
<p>Spy Gear</p>
<p>35.00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image96.png" style="width:5.08661in;height:0.97886in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad. Confirm any notes by choosing OK.</td>
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
<col style="width: 12%" />
<col style="width: 68%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-9-price-based-bid-evaluation" class="P68B1DB1-berschrift16">Step 9: Price Based Bid Evaluation</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Evaluate the quotes based on the price. Reject two of the three offers.</p>
<p><strong>Description</strong> Generate a quotation price comparison list from the quotations from the individual vendors. The quotation price comparison list sorts the quotations from lowest to highest.</p>
<p>The successful vendor (Mid-West Supply) was selected using the criterion of the most favorable quotation. It is now necessary to inform the subordinate providers of the rejection of their offers.</p>
<p><strong>Name (position)</strong> Wilton Saban (Inventory Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Materials Management</em> space. In the role of <em>Inventory Supervisor</em> section, you can use the C<em>ompare Supplier Quotations</em> app to reject a quotation.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image97.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Search for your Request for Quotation by using the <strong>F4 help</strong>. Enter the <strong>RFQ1###</strong> as <em>RFQ Description</em> and click <img src="media/image98.png" style="width:0.21654in;height:0.17717in" />.</td>
<td style="text-align: right;">RFQ1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image99.png" style="width:5.31205in;height:1.73254in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select your RFQ.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image100.png" style="width:5.23798in;height:1.86842in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Compare the quotes and select the best one, in this case the quotation from Mid-West Supply ###. Choose the beste Quote and click <img src="media/image101.png" style="width:0.33071in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> For the best offer the <em>Total Quotation Net Value</em> is highlighted in green.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Reject the other two offers. To do this click on the Supplier <em>Qutation number</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image102.png" style="width:2.90693in;height:1.56803in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Then click on the <em>Qutation number</em> again.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the <em>Supplier Quotation</em> window click on <img src="media/image103.png" style="width:0.48031in;height:0.17717in" />(top right).</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If your browser window is to small, the <em>Complete</em> button will be hidden under <img src="media/image104.png" style="width:0.2768in;height:0.1692in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image105.png" style="width:0.12992in;height:0.17717in" /> to return to the <em>Compare Supplier Quotations</em> window.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Repeat this procedure to also reject the second quotation.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad. Confirm any notes by choosing OK.</td>
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
<th colspan="2"><h1 id="step-10-create-purchase-order-referencing-an-rfq" class="P68B1DB1-berschrift16">Step 10: Create Purchase Order Referencing an RFQ</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a purchase order with reference to a request for quotation.</p>
<p><strong>Description</strong> Create a purchase order that refers to the successful supplier's quote. The details are then imported into the new purchase order.</p>
<p><strong>Name (position)</strong> Alberto Conti (Inventory Assistant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Materials Management</em> space. In the role of <em>Inventory Assistant</em>, you can use the <em>Manage RFQs</em> app to create a request for quotation for your purchase requisition.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image106.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the <em>search field</em> enter <strong>RFQ1###*</strong> and click <img src="media/image107.png" style="width:0.24449in;height:0.17717in" />.</td>
<td style="text-align: right;">RFQ1###*</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image108.png" style="width:5.14611in;height:1.82126in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Open your RFQ and go to the <em>Process Flow</em> area.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image109.png" style="width:5.06282in;height:4.84468in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You see your purchase requisition followed by the associated RFQ and the three supplier quotations. Two of the three offers have already been rejected, as indicated by the comment completed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the Supplier Quotation with the comment <img src="media/image110.png" style="width:0.75757in;height:0.19685in" /> and then on <em>Quotation number</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image111.png" style="width:3.51209in;height:1.24005in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a purchase order from the quotation click in the <em>Supplier Quotation</em> window on <img src="media/image112.png" style="width:1.18504in;height:0.17717in" /> and then on <img src="media/image113.png" style="width:1.52786in;height:0.15279in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image114.png" style="width:1.59333in;height:0.83333in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Purchase Order</em> go to the <em>Items</em> area you see one entry with your CHLK1### material.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">We want to split the delivery in two partial deliverys. Change the <em>Order Quantity</em> from 200 to <strong>100</strong>. Select the entry and click <img src="media/image115.png" style="width:0.32283in;height:0.17717in" />.</td>
<td style="text-align: right;">200🡪 100</td>
</tr>
<tr>
<td colspan="2">In the <em>Purchase Order Item</em> screen go to the <em>Schedule Lines</em> area and change the <em>Delivery Date</em> to <strong>Today's date</strong> .</td>
<td style="text-align: right;">Today's date</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image116.png" style="width:3.23997in;height:1.03943in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image18.png" style="width:0.36319in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image117.png" style="width:5.14595in;height:2.10955in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image118.png" style="width:0.31496in;height:0.17717in" /> to save the purchase order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image119.png" style="width:2.1364in;height:0.69613in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note</strong> A purchase order is a formal request to a vendor to deliver goods or services according to the conditions of the purchase order. Several objects can trigger a purchase order (see graphic).</p>
<p><img src="media/image120.png" style="width:3.82077in;height:2.48958in" /></p>
<p>Goods receipt and invoice verification are usually based on the purchase order.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image121.png" style="width:0.19291in;height:0.17717in" /> until you have returned to the <em>Request for Quotation</em> screen. Take another look at the <em>Process Flow</em>. The Quotation is now followed by a purchase order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image122.png" style="width:5.19525in;height:3.79353in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad. Confirm any notes by choosing OK.</td>
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
<th colspan="2"><h1 id="step-11-display-purchase-order" class="P68B1DB1-berschrift16">Step 11: Display Purchase Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display your purchase order.</p>
<p><strong>Description</strong> You now want to look in the system at what you have sent to the vendor.</p>
<p><strong>Name (position)</strong> Aura Maxwell (Purchasing Agent 2)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the purchase order, please go to the <em>Materials Management</em> space. In the role of <em>Purchasing Agent</em>, you can use <em>My Purchasing Document Items (Professional)</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image123.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The app provides you with an overview of all purchase requisitions, purchase orders, goods receipts, and supplier invoices. In the <em>Supplier</em> field, enter <strong>Mid-West Supply ###</strong> and choose <img src="media/image124.png" style="width:0.2126in;height:0.17717in" />. Afterwards, go to the <img src="media/image125.png" style="width:0.79528in;height:0.17717in" /> tab.</td>
<td style="text-align: right;">Mid-West Supply ###</td>
</tr>
<tr>
<td colspan="2">You may need to scroll down to see your supplier and purchase order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image126.png" style="width:4.73358in;height:1.63898in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-12-post-goods-receipt-for-purchase-order" class="P68B1DB1-berschrift16">Step 12: Post Goods Receipt for Purchase Order </h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a goods receipt posting for your purchase order.</p>
<p><strong>Description</strong> You receive the goods that you ordered in the previous step from Mid-West Supply into your inventory. A goods receipt posting is created that refers to your purchase order. The stock is increased and a financial document is created that posts the value of the goods correctly.</p>
<p><strong>Name (position)</strong> Tatiana Karsova (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post the goods receipt, please go to the <em>Materials Management</em> space. In the role of <em>Goods Receipt Clerk</em>, you can use the <em>Post Goods Receipt for Purchasing Document</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image127.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <strong>your purchasing document number</strong> in the <em>Purchasing Document</em> field. If you want to search for your purchasing document number, use the <strong>F4 help</strong>. In the search field, enter <strong>CHLK1###</strong> and then click <img src="media/image128.png" style="width:0.22441in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>Your purchase order number</p>
<p>CHLK1###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image129.png" style="width:5.21431in;height:1.43063in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then select the <strong>first of your</strong> <strong>purchase orders</strong> by double-clicking it. You can now see your splitted purchase order.</td>
<td style="text-align: right;">First of your orders</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note</strong> If goods are delivered for a purchase order, document a goods receipt with reference to the purchase order. The system checks the purchase order and copies only the open purchase order items to the goods receipt transaction.</p>
<p><img src="media/image130.png" style="width:4.2555in;height:2.16808in" /></p>
<p>For goods receipt with reference to a purchase order, the system checks the following:</p>
<ul>
<li><p>Whether the correct material was delivered.</p></li>
<li><p>Whether the correct quantity was delivered. (If there is no surplus or underdelivery)</p></li>
<li><p>Whether perishable goods are within their minimum shelf life. (In this case, the shelf life expiration date check must be activated.)</p></li>
</ul></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image131.png" style="width:4.97477in;height:2.51031in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For <em>Printing</em>, select <strong>Individual slip</strong>. If it is not filled automatically, select <strong>TG00 (Trading Goods)</strong> in the individual items for <em>storage location</em>.</td>
<td style="text-align: right;"><p>Individual slip</p>
<p>TG00</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image132.png" style="width:5.04469in;height:2.52365in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Since you have split your purchase order, you should see two lines with 100 pieces. In this step, we only process the first delivery. Therefore, click on the first row to check all entries.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the <strong>Delivery</strong> <strong>Completed</strong> checkbox.</td>
<td style="text-align: right;">X</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Check that <strong>Tradings Goods</strong> is entered as the <em>storage location</em> and change the <em>stock type</em> to <strong>Quality Inspection</strong>.</td>
<td style="text-align: right;"><p>Trading goods</p>
<p>Quality Inspection</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image133.png" style="width:4.95503in;height:2.05078in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now click <img src="media/image134.png" style="width:0.29134in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Note Inventory Management recognizes various stock types that indicate the usability of the material:</p>
<ul>
<li><p>unrestricted-use stock</p></li>
<li><p>Stock in quality inspection</p></li>
<li><p>blocked stock</p></li>
</ul>
<p><img src="media/image135.png" style="width:3.42533in;height:2.08862in" /></p>
<p>For goods receipts, you decide to which stock type a quantity is posted. The stock type is relevant for determining the available stock in material requirements planning (MRP) and for withdrawals in inventory management (see also Availability Check).</p>
<p>You can only post withdrawals for consumption from unrestricted-use stock. From quality inspection stock and blocked stock, you can only withdraw a sample, scrap a quantity, or post an inventory difference.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Leave the first line selected.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image136.png" style="width:5.12623in;height:0.97109in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image137.png" style="width:0.29528in;height:0.17717in" /> to post the goods receipt of your material. You receive the following success message with your material document number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image138.png" style="width:2.40261in;height:1.28936in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note</strong> When you post a goods receipt into one of the warehouses, the system generates a material document. This document contains information about the delivered material and the corresponding quantity. For stock items, the plant storage location is documented.</p>
<p><img src="media/image130.png" style="width:4.2555in;height:2.16808in" /></p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Close the message and click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<col style="width: 12%" />
<col style="width: 68%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-13-check-received-goods" class="P68B1DB1-berschrift16">Step 13: Check Received Goods</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Check the quality of the goods.</p>
<p><strong>Description</strong> You must ensure that the goods have been delivered in the required quality. The goods are released for consumption.</p>
<p><strong>Name (position)</strong> Sandeep Die (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please go to the <em>Materials Management</em> space. In the role of <em>Warehouse Supervisor</em> section, you can use the <em>Stock (Single Material)</em> app to perform a quality inspection of the goods.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image139.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If it is not already selected, enter your material <strong>CHLK1###</strong>.</td>
<td style="text-align: right;">CHLK1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image140.png" style="width:5.19242in;height:0.46339in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the previous step, you posted the received goods for quality inspection. Here you can see the 100 units of quality inspection stock.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image141.png" style="width:5.17363in;height:0.65773in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the icon <img src="media/image71.png" style="width:0.55118in;height:0.19685in" /> in the <em>Stock History</em> column in the Trading Goods row.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image142.png" style="width:5.1733in;height:2.70044in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can only remove goods from unrestricted-use stock for consumption. Therefore, you have to transfer post the goods.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> In reality, you would check whether the correct goods and quantity were delivered before posting them to unrestricted-use stock.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the row for storage location Trading Goods in the plant in Miami and click <img src="media/image143.png" style="width:1.1063in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image144.png" style="width:5.20479in;height:1.43732in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Stock in Quality Inspection</em> column, click <img src="media/image145.png" style="width:0.22146in;height:0.17717in" />, next to the 100 units. The icon under <em>Unrestricted use stock</em> is now clickable. Click <img src="media/image146.png" style="width:0.22146in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Transfer Stock – In-Plant</em> window, increase the quantity to <strong>100</strong>.</td>
<td style="text-align: right;">100</td>
</tr>
<tr>
<td colspan="2"><img src="media/image147.png" style="width:3.60783in;height:3.6906in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image148.png" style="width:0.29921in;height:0.17717in" />. You receive a success message. The material has been transferred.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image149.png" style="width:2.84634in;height:1.09872in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Close the message and click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-14-check-physical-goods-receipt" class="P68B1DB1-berschrift16">Step 14: Check Physical Goods Receipt</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Confirm the physical receipt of the goods.</p>
<p><strong>Description</strong> View the inventory of chain locks again. The stock overview gives you an overview of the stocks of a material across all organizational levels.</p>
<p><strong>Name (position)</strong> Tatiana Karsova (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To check the stock level of a material, go to the <em>Materials Management</em> space. In the role of <em>Goods Receipt Clerk</em>, you can use the <em>Manage Stock</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image150.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">From the drop down menu, choose the <strong>DC Miami (MI00</strong>). To find the material number from your chain lock, click in the Material field and then click the value help icon<img src="media/image151.png" style="width:0.17717in;height:0.17717in" />.</td>
<td style="text-align: right;">MI00</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the Search field, enter <strong>*###</strong> (for example, if your number is 002, enter *105).</td>
<td style="text-align: right;">*###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image107.png" style="width:0.24449in;height:0.17717in" /> to display the list of materials. Extend the Material Short Text field. Scroll down until you find your material <strong>CHLK1###</strong>.</td>
<td style="text-align: right;">CHLK1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image152.png" style="width:4.59577in;height:0.45458in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Double click on it. The report shows you the storage level for the DC in Miami.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image153.png" style="width:5.0711in;height:1.49442in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can find out more details about the stock of the chain lock. To do so, click <img src="media/image154.png" style="width:0.98425in;height:0.17717in" />. This will give you detailed information about the stock of the chain lock in the different plants.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image155.png" style="width:5.12609in;height:1.61614in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the icon <img src="media/image156.png" style="width:0.30315in;height:0.19685in" /> at the DC Miami (MI00) plant to see detailed information about the stock of the chain lock in Miami. On the following screen, you can see a graphical overview.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image157.png" style="width:4.98173in;height:2.60206in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-15-create-and-post-the-first-supplier-invoice" class="P68B1DB1-berschrift16">Step 15: Create and Post the First Supplier Invoice</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a supplier invoice.</p>
<p><strong>Description</strong> Create a supplier invoice from Mid-West Supply for 3,200.00 USD for the current purchase order and the received goods.</p>
<p>This invoice is assigned to an existing expense account in the general ledger of your chart of accounts and saved as a payable to Mid-West Supply.</p>
<p>To facilitate data entry in the general ledger, the invoice is shown below.</p>
<p><img src="media/image158.jpeg" style="width:4.68152in;height:6.07968in" alt="lieferantenrechnung mm en-page-002" /></p>
<p><strong>Name (position)</strong> Silvia Cassano (AP Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a supplier invoice, please go to the <em>Materials Management</em> space. In the role of <em>AP Accountant</em>, you can use the <em>Create Supplier Invoice</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image159.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the Create Supplier Invoice screen, enter <strong>today’s date</strong> as the <em>Invoice Date</em>. Check your <em>company code</em> <strong>US00</strong>. Enter the amount of the above invoice (<strong>3,200.00</strong>) in the <em>Gross Invoice Amount</em> field. Now enter <strong>INVOICE00504-###</strong> as <em>Reference</em>.</td>
<td style="text-align: right;"><p>Today's date</p>
<p>US00</p>
<p>3,200.00</p>
<p>INVOICE00504-###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image160.png" style="width:5.20077in;height:0.90603in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the tab <em>Purchasing Document References</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now enter (or search for) the <strong>number of your purchase order</strong> in the <em>Purchase Order/Scheduling Agreement</em> field. Then press Enter. The Invoicing Party field has now been automatically filled with the number of your vendor.</td>
<td style="text-align: right;">Your purchase order number</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image161.png" style="width:5.13927in;height:1.57186in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For the first invoice item, enter <strong>XI</strong> as the <em>Tax Code</em> and <strong>TX0000000</strong> as the <em>Tax Jurisdiction</em>.</td>
<td style="text-align: right;"><p>XI</p>
<p>TX0000000</p></td>
</tr>
<tr>
<td colspan="2">Scroll back to the top of the page. As you can see, the balance is 0.00 USD.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image162.png" style="width:3.39978in;height:0.96724in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Then press <img src="media/image163.png" style="width:0.40157in;height:0.17717in" /> to verify that your postings are correct.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image164.png" style="width:5.12316in;height:2.18882in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Finally, press <img src="media/image165.png" style="width:0.28346in;height:0.17717in" />. The system will generate a unique supplier invoice number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image166.png" style="width:2.22591in;height:1.29113in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Close the message with <strong>No</strong> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-16-display-purchase-order-history" class="P68B1DB1-berschrift16">Step 16: Display Purchase Order History</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the purchase order history.</p>
<p><strong>Description</strong> Review the status of your order of the chain locks. Due to the first transaction that was carried out for your purchase order number, the Purchase Order Processing tab page is now available in the purchase order.</p>
<p><strong>Name (position)</strong> Wilton Saban (Inventory Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the purchase order history, go to the <em>Materials Management</em> space. In the role of <em>Inventory Supervisor</em>, you can use <em>My Purchasing Document Items (Professional)</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image123.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The app provides you with an overview of all purchase requisitions, purchase orders, goods receipts, and supplier invoices. In the Supplier field, enter your vendor <strong>Mid-West Supply ###</strong>.</td>
<td style="text-align: right;">Mid-West Supply ###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image167.png" style="width:5.2061in;height:0.89725in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Choose <img src="media/image168.png" style="width:0.21654in;height:0.17717in" /> and then choose the tab page <img src="media/image169.png" style="width:0.79528in;height:0.17717in" />. You may need to scroll down to see your supplier and purchase order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the Purchase Order Items area, click <img src="media/image170.png" style="width:0.19685in;height:0.17717in" /> and select the <em>Delivered Quantity</em> and <em>Delivered Amount</em> columns in the <em>View Settings</em> dialog box<em>.</em></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image171.png" style="width:3.43018in;height:1.58985in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image172.png" style="width:0.22835in;height:0.17717in" />. As you can see, the first item of the purchase order has been delivered for a delivery value of 3,200.00 USD.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image173.png" style="width:4.45848in;height:2.0218in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now choose the tab page<img src="media/image174.png" style="width:0.74409in;height:0.17717in" />. You can see the 100 delivered chain locks. You see the material document that was created in the system when you confirmed the goods receipt.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image175.png" style="width:4.9399in;height:0.91215in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <img src="media/image176.png" style="width:0.84646in;height:0.17717in" /> tab, you can see further activities that have been carried out with reference to your purchase order. Click <img src="media/image177.png" style="width:0.79134in;height:0.19685in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image178.png" style="width:4.8839in;height:0.79232in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The invoice has been created. Click on the invoice line of your chain lock. This will take you to the financial document that was created when you created the supplier invoice.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image179.png" style="width:5.21345in;height:1.77708in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-17-display-document-flow" class="P68B1DB1-berschrift16">Step 17: Display Document Flow </h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the document flow.</p>
<p><strong>Description</strong> Check the goods receipt document and the document flow of your material.</p>
<p><strong>Name (position)</strong> Wilton Saban (Inventory Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the history of documents, please go to the <em>Materials Management</em> space. In the role of <em>Inventory Supervisor</em>, you can use the <em>Material Documents Overview</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image180.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The app provides an overview of material documents. You can find your purchase order by using the assigned number. To do this, enter your material number <strong>CHLK1###</strong> in the <em>Material</em> field. If the search fields are not displayed in your system, first click to<img src="media/image181.png" style="width:0.75632in;height:0.19685in" /> expand the search fields.</td>
<td style="text-align: right;">CHLK1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image182.png" style="width:5.11816in;height:0.86513in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">After entering the search term, click <img src="media/image107.png" style="width:0.24449in;height:0.17717in" />. Then click Settings <img src="media/image183.png" style="width:0.23228in;height:0.17717in" />. In the <em>view settings</em>, activate the <strong>Stock Type (Transfer)</strong> column. Confirm with<img src="media/image10.png" style="width:0.22835in;height:0.17717in" />.</td>
<td style="text-align: right;">Stock Type (Stock Transfer)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">A new material document is created for each material movement. You see two material documents with your material CHLK###. One is the document for the goods receipt into inspection stock. You also see a document that was generated by the transfer posting of the material to unrestricted-use stock.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Identify the line with the Stock Type (Transfer): Unrestricted-Use Stock (01).</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image184.png" style="width:5.1663in;height:0.93373in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on this line. You can now see the general information for the document from the step in which you confirmed the goods receipt.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image185.png" style="width:5.14626in;height:1.8954in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click the <em>Process Flow</em> tab. In the process flow, you can see the transfer posting of the material from stock to quality inspection to unrestricted-use stock.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image186.png" style="width:3.5733in;height:3.75724in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-18-post-goods-receipt-for-purchase-order" class="P68B1DB1-berschrift16">Step 18: Post Goods Receipt for Purchase Order </h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Post a Goods Receipt for a Purchase Order.</p>
<p><strong>Description</strong> You receive the missing goods that you ordered from Mid-West Supply into your warehouse. A goods receipt posting is created that refers to your purchase order. This ensures that you have received the ordered goods within the expected time and in the required quality. The stock is increased and a financial document is created that posts the value of the goods correctly.</p>
<p><strong>Name (position)</strong> Tatiana Karsova (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post the goods receipt, please go to the <em>Materials Management</em> space. In the role of <em>Goods Receipt Clerk</em>, you can use <em>Post Goods Receipt for Purchasing Document</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image187.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">The <em>Post Goods Receipt for Purchasing Document</em> window appears.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image188.png" style="width:4.2216in;height:0.42544in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Choose the <strong>F4 help</strong> in the <em>Purchasing Document</em> field.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your number *### and click <img src="media/image107.png" style="width:0.24449in;height:0.17717in" />. Search for your material <strong>CHLK1###</strong>. You can see that you no longer see two purchase orders but only one open purchase order for your material.</td>
<td style="text-align: right;">*###</td>
</tr>
<tr>
<td colspan="2"><img src="media/image189.png" style="width:5.08161in;height:1.21422in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Double-click the purchase order. The following screen appears. On the <em>Items</em> tab page, you should see only one row.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Make sure that for <em>Storage Location</em> <strong>TG00 (Trading Goods)</strong> and for <em>Stock Type</em> <strong>Unrestricted use</strong> is selected.</td>
<td style="text-align: right;"><p>TG00</p>
<p>Unrestricted Use</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image190.png" style="width:5.24328in;height:0.74997in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> In step 12, you first posted the goods in quality inspection and then inspected them later. In this scenario, you inspect the goods directly at goods receipt so that you can use them directly.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the item line of your chain lock to check all entries. Select the <strong>Delivery</strong> <strong>Completed</strong> checkbox.</td>
<td style="text-align: right;">Delivery Completed</td>
</tr>
<tr>
<td colspan="2"><img src="media/image191.png" style="width:5.19525in;height:2.20024in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now click<img src="media/image192.png" style="width:0.3622in;height:0.17717in" />. Select the line and click <img src="media/image193.png" style="width:0.25984in;height:0.17717in" />. You receive the following success message with your material document number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image194.png" style="width:2.19195in;height:1.12497in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Close the messafe and click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<col style="width: 68%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-19-check-physical-goods-receipt" class="P68B1DB1-berschrift16">Step 19: Check Physical Goods Receipt</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Confirm the physical receipt of the goods.</p>
<p><strong>Description</strong> View the inventory of chain locks again. The stock overview gives you an overview of the stocks of a material across all organizational levels.</p>
<p><strong>Name (position)</strong> Tatiana Karsova (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To check the stock level of a material, go to the <em>Materials Management</em> space. In the role of <em>Goods Receipt Clerk</em> section, you can use the <em>Manage Stock</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image195.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">From the drop down menu, choose the Miami <em>plant</em> <strong>DC Miami</strong> (<strong>MI00</strong>). To find the material number from your chain lock, click in the Material field and then click the value help icon<img src="media/image196.png" style="width:0.20866in;height:0.17717in" />.</td>
<td style="text-align: right;">MI00</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the Search field, enter <strong>*###</strong> (for example, if your number is 105, enter *105). Click <img src="media/image107.png" style="width:0.24449in;height:0.17717in" /> to display the list of materials.</td>
<td style="text-align: right;">*###</td>
</tr>
<tr>
<td colspan="2">Scroll down until you find your material <strong>CHLK1###</strong>. Double click on it.</td>
<td style="text-align: right;">CHLK1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image197.png" style="width:5.0997in;height:1.87297in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Since in the previous step the goods receipt was posted directly to unrestricted stock, you can see that the stock in this category has increased from 100 to 200.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can find out more details about the stock of the chain lock. To do so, click<img src="media/image198.png" style="width:1.09843in;height:0.17717in" />. This will give you detailed information about the stock of the chain lock in the different plants.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image199.png" style="width:5.14825in;height:2.30245in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image200.png" style="width:0.2874in;height:0.19685in" /> to display the stock history for plant DC Miami (MI00) graphically. You can now see a graphical overview.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image201.png" style="width:5.20314in;height:3.52984in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Since you currently only have unrestricted-use stocks, the key figures are set to 0.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Close and then click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<col style="width: 12%" />
<col style="width: 67%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-20-create-and-post-the-second-supplier-invoice" class="P68B1DB1-berschrift16">Step 20: Create and Post the Second Supplier Invoice</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a supplier invoice.</p>
<p><strong>Description</strong> Create a supplier invoice from Mid-West Supply for USD 3,200.00 for the second partial delivery and the received goods. This invoice is also assigned to an existing expense account in the general ledger of your chart of accounts and saved as a payable to Mid-West Supply. Later, a check is issued for Mid-West Supply. To facilitate data entry in the general ledger, the invoice is shown below.</p>
<p><strong>Name (position)</strong> Silvia Cassano (AP Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a supplier invoice, please go to the <em>Materials Management</em> space. In the role of <em>AP Accountant</em>, you can use the <em>Create Supplier Invoice</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image203.png" style="width:1.56299in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Create Supplier Invoice</em> screen, enter <strong>today’s date</strong> as the <em>Invoice Date</em>. Verify that <em>company code</em> <strong>US00</strong> is selected. In the <em>Gross Amount</em> field, enter the amount of the invoice above (<strong>3,200.00</strong>). Enter <strong>INVOICE00515-###</strong> as the <em>reference</em>.</td>
<td style="text-align: right;"><p>Today's date</p>
<p>US00</p>
<p>3,200.00</p>
<p>INVOICE00515-###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image204.png" style="width:5.28564in;height:1.74005in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Choose the <em>Purchasing Document References</em> tab.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now enter (or search for) the <strong>number of your purchase order in the Purchase Order</strong>/Scheduling Agreement field. Then press Enter. The Invoicing Party field has now been automatically filled with the number of your vendor.</td>
<td style="text-align: right;">Your purchase order number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image205.png" style="width:5.22204in;height:1.58111in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For the second item, enter <strong>XI</strong> as <em>the tax code</em> and <strong>TX0000000</strong> as the <em>tax jurisdiction</em>.</td>
<td style="text-align: right;"><p>XI</p>
<p>TX0000000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image206.png" style="width:5.29412in;height:0.69135in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the document header, you can see that the balance is 0.00.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image207.png" style="width:2.90664in;height:1.344in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Then press <img src="media/image208.png" style="width:0.41339in;height:0.17717in" /> to verify that your postings are correct.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image209.png" style="width:5.24627in;height:2.27625in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Finally, press <img src="media/image210.png" style="width:0.30709in;height:0.17717in" />. The system will generate a unique supplier invoice number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image211.png" style="width:2.40443in;height:1.56947in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image212.png" style="width:0.39764in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-21-post-outgoing-payment" class="P68B1DB1-berschrift16">Step 21: Post Outgoing Payment</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Post the payments to a supplier.</p>
<p><strong>Description</strong> Issue a payment to your supplier Mid-West Supply to pay your payables. Note that the total amount is for both of your invoices. The created posting will clear the liability from your bank account.</p>
<p><strong>Name (position)</strong> Silvia Cassano (AP Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post the payment to a supplier, go to the <em>Materials Management</em> space. In the role of <em>AP Accountant</em>, you can use the <em>Post Outgoing Payments</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image213.png" style="width:1.56299in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Post Outgoing Payments</em> screen, choose Global Bike as the <em>company code</em> (<strong>US00</strong>). For <em>Posting Date</em> and <em>Journal Entry Date</em> enter <strong>today’s date</strong>, for Reference <strong>INVOICES ###</strong>, and the <strong>current period</strong>. For <em>G/L account</em>, enter <strong>1810000</strong> (Bank 1) and the <em>Amount</em> <strong>6,400.00</strong> <strong>USD</strong>.</td>
<td style="text-align: right;"><p>US00</p>
<p>Current Date</p>
<p>INVOICES ###</p>
<p>Current Period</p>
<p>1810000</p>
<p>6,400.00 USD</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Ensure that the journal entry type <strong>KZ (Vendor Payment)</strong> is selected. Use the following screenshot to check your entries.</td>
<td style="text-align: right;">KZ (Vendor Payment)</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image214.png" style="width:5.12169in;height:1.38559in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Under <em>Open Item Selection</em>, enter your supplier number for <strong>Mid-West Supply</strong> as the account (if necessary, use the F4 help).</td>
<td style="text-align: right;">Mid-West Supply</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image215.png" style="width:4.0917in;height:0.66705in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image216.png" style="width:0.59055in;height:0.17717in" />. On the upper right, you can see that the open balance is USD 6,400.00.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image217.png" style="width:1.45854in;height:0.23962in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">On the <em>Open Items</em> tab page, you see the two split deliveries.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image218.png" style="width:5.17135in;height:0.82699in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Since you want to pay both bills together, choose the button <img src="media/image219.png" style="width:0.76378in;height:0.17717in" /> in both lines. Note that both items have been cleared.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image220.png" style="width:1.15632in;height:0.80053in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">The open balance is now USD 0.00. <img src="media/image221.png" style="width:1.3231in;height:0.20836in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image222.png" style="width:0.28937in;height:0.17717in" /> to post your payments to Mid-West Supply. The system will assign a unique document number to your supplier payment.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image223.png" style="width:2.82856in;height:1.0796in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Press <img src="media/image224.png" style="width:0.44094in;height:0.17717in" /> and click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad. Confirm any error messages.</td>
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
<th colspan="2"><h1 id="step-22-display-supplier-balance" class="P68B1DB1-berschrift16">Step 22: Display Supplier Balance</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the balances of a vendor.</p>
<p><strong>Description</strong> View and confirm the activities and related balances related to your Mid-West Supply vendor. You should see a debit posting and a credit posting that were generated by the two invoices and the output of a single payment to settle the payables to Mid-West Supply.</p>
<p><strong>Name (position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the balances of a vendor, please go to the <em>Materials Management</em> space. In the role of <em>Head of Accounting</em>, you can use the <em>Display Supplier Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image225.png" style="width:1.53937in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Use the <img src="media/image226.png" style="width:0.17717in;height:0.17717in" /> in the Supplier field to find the number of your supplier. In the Search Term field, enter your number <strong>###*</strong> and press <img src="media/image107.png" style="width:0.24449in;height:0.17717in" />.</td>
<td style="text-align: right;">###*</td>
</tr>
<tr>
<td colspan="2">Scroll until you find your Supplier <strong>Mid-West</strong> <strong>Supply</strong>. Select the entry.</td>
<td style="text-align: right;">Mid-West Supply</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image227.png" style="width:5.09642in;height:3.42735in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Confirm with <img src="media/image228.png" style="width:0.5315in;height:0.17717in" />. Back on the Display <em>Supplier Balances screen,</em> choose <strong>US00</strong> as the company code and <strong>the current year</strong> as the fiscal year.</td>
<td style="text-align: right;"><p>US00</p>
<p>Current Year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image229.png" style="width:5.1053in;height:0.96042in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Then choose <img src="media/image230.png" style="width:0.24016in;height:0.17717in" /> to display the balances. You get a similar overview.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image231.png" style="width:5.18093in;height:2.55747in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<col style="width: 17%" />
<col style="width: 67%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-23-display-purchase-order-history" class="P68B1DB1-berschrift16">Step 23: Display Purchase Order History</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the purchase order history.</p>
<p><strong>Description</strong> Review the status of your order of the chain locks. The Purchase Order History tab page has been updated as a result of further postings.</p>
<p><strong>Name (position)</strong> Wilton Saban (Inventory Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the purchase order history, go to the <em>Materials Management</em> space. In the role of <em>Inventory Supervisor</em> section, you can use <em>My Purchasing Document Items (Professional)</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image232.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The app provides you with an overview of all purchase requisitions, purchase orders, goods receipts, and supplier invoices.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Supplier</em> field, enter the number of your supplier <strong>Mid-West Supply ###</strong> and choose <img src="media/image230.png" style="width:0.24016in;height:0.17717in" />.</td>
<td style="text-align: right;">Mid-West Supply ###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image233.png" style="width:5.49929in;height:1.06056in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image234.png" style="width:0.8189in;height:0.17717in" />. You may need to scroll down to see your supplier and purchase order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Purchase Order Items</em> section, click on <img src="media/image235.png" style="width:0.18504in;height:0.17717in" /> and select the column <em>Next Delivery Quantity</em> in the pop-up <em>View Settings</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image236.png" style="width:5.54802in;height:0.84872in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see, no more open quantities are displayed under Next Delivery Quantity.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image237.png" style="width:0.70079in;height:0.17717in" />. You see the other 100 delivered chain locks. You also see the material document that was created in the system when you confirmed the goods receipt.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image238.png" style="width:5.6056in;height:0.87379in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the Supplier Invoice Overview, you can see further activities that have been performed with reference to your purchase order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image239.png" style="width:0.77559in;height:0.17717in" />. Both invoices have been created and have the status Posted.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image240.png" style="width:5.46373in;height:1.10859in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display more information about the documents, you can click on the relevant row. This will take you to the financial document that was created when you created the supplier invoice.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<col style="width: 18%" />
<col style="width: 65%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-24-display-account-balances" class="P68B1DB1-berschrift16">Step 24: Display account balances</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the balance of the general ledger.</p>
<p><strong>Description</strong> Use G/L account numbers to display the activities and related balances for some accounts in your general ledger.</p>
<p><strong>Name (position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the account balances, please go to the <em>Materials Management</em> space. In the role of <em>Head of Accounting</em>, you can use the <em>Balance Sheet/Income Statement</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image241.png" style="width:1.54724in;height:1.5748in" /></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Financial Statement</em> screen, enter <strong>US00</strong> (Global Bike) for Company Code, <strong>0L</strong> for Ledger, and <strong>G000</strong> for Financial Statement Version. Make sure that the Balance Sheet Type is <strong>Normal (Actual - Actual)</strong> and End Period is <strong>current period/year</strong> and Comparison Period is <strong>1/2016</strong>. Compare your screen with the following screenshot.</td>
<td style="text-align: right;"><p>US00</p>
<p>0L</p>
<p>G000</p>
<p>Normal (Actual – Actual)</p>
<p>Current Period/Year</p>
<p>1/2016</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image242.png" style="width:5.36718in;height:0.92724in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Choose <img src="media/image107.png" style="width:0.24449in;height:0.17717in" />. In the view, you can see all items of the accounts of Global Bike in the United States.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image243.png" style="width:5.32324in;height:1.21075in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Since all participants in your course are posting to the same US bank account, the number you see next to the bank account 1810000 used is different.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image244.png" style="width:5.35in;height:1.37476in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image42.png" style="width:0.3189in;height:0.17717in" /> to go to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="mm-challenge" class="P68B1DB1-berschrift16">MM Challenge</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><strong>Learning objective</strong> Understand and execute a Materials Management process.</td>
<td style="text-align: right;"><strong>Time</strong> 80min</td>
</tr>
<tr>
<td colspan="3"><p><strong>Motivation</strong> After you have successfully completed the Materials Management case study, you should be able to solve the following task independently.</p>
<p><strong>Scenario</strong> A new chain closure<em>, Chain Lock Security Pro ###</em> (ger.: Kettenschloss Security Pro ###), is available on the market and we would like to include it in our inventory. The new chain closure with material number CHSP1### consists of a higher quality steel than the previous chain lock (CHLK1###), but the old one can still be used as a template because it has the same properties. The new material is intended for plant MI00, sales organization UE00, and distribution channel WH. With modern production techniques, the new material CHSP1### is also offered more cheaply by the suppliers. Global Bike passes the savings on to its customers. Maintain the chain lock and set the inventory price to 30.00 USD per chain lock. Request offers for 300 chain locks of security pro with a valuation price of 30.00 USD. Based on your request of 300 pieces, <em>Boomtown Tire &amp; Wheel</em> <em>(102###)</em> is offering 26.00 USD per piece and <em>Space Bike Composites (105###)</em> of 25.50 USD per piece. Enter both quotations and accept the best quotation and order the requested 300 chain locks. Process the inbound delivery and enter the incoming invoice. You then pay for the delivery.</p>
<p><strong>Note</strong> Since this task is based on the Materials Management case study, you can use this as a guide. However, we recommend that you carry out this continuing task without assistance in order to test your acquired knowledge.</p></td>
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
