---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_SD_en_v4.3 (1)
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_SD_en_v4.3 (1).docx
---

Sales and Distribution (SD)

This case study explains an integrated sales and distribution process in detail and thus fosters a thorough understanding of each process step and underlying SAP functionality.

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
<p>Sales and Distribution</p>
<p>Authors</p>
<p>Bret Wagner</p>
<p>Stefan Weidner</p>
<p>Version</p>
<p>4.3</p>
<p>Last Update</p>
<p>July 2025</p></th>
<th style="text-align: left;"><p>MOTIVATION</p>
<p>The data entry of the exercises for sales was reduced because much of the data already existed in the SAP system. The stored data, known as master data, simplifies the handling of business processes.</p>
<p>In the sales order process, you used master data that already existed in the system, such as customers, material (products that Global Bike sells) and conditions, to shorten the sales process.</p>
<p>In this case study you will create your own master data, e.g. a new customer.</p></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"><p>PREREQUISITES</p>
<p>Before you use this case study, you should be familiar with navigation in the SAP system.</p>
<p>In order to successfully work through this case study, it is not necessary to have finished the SD exercises. However, it is recommended.</p>
<p>NOTES</p>
<p>This case study uses the model company Global Bike.</p>
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
<td colspan="2"><p><strong>Learning Objective</strong> Understand and perform an integrated order-to-cash cycle.</p>
<p><strong>Scenario</strong> In order to process a complete order-to-cash process you will take on different roles within the Global Bike company, e.g. sales agent, warehouse worker, accounting clerk. Overall, you will be working in the Sales and Distribution (SD), the Materials Management (MM) and the Financial Accounting (FI) departments.</p>
<p><strong>Employees involved</strong> David Lopez (Sales Representative US East)</p>
<p>Maria Diaz (Sales Person 1 US East)</p>
<p>Matthias Dosch (Sales Person 2 US East)</p>
<p>Sandeep Das (Warehouse Supervisor)</p>
<p>Sergey Petrov (Warehouse Employee)</p>
<p>Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 100 min</td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;">You start the sales order process by creating a new business partner (BP) – called the <em>The Bike Zone</em> – in Orlando with the role “Customer”. Then, you receive an inquiry which you will process into a quotation. Once the quotation is accepted by the customer you create a sales order referencing the quotation. As you will have enough bikes in stock, you deliver the products sold to your customer, create an invoice and receive the payment. The graphic below displays the complete process.</td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><img src="media/image2.png" style="width:5.85933in;height:4.19811in" /></td>
</tr>
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
<p><a href="#step-1-create-new-customer">Step 1: Create New Customer <span>4</span></a></p>
<p><a href="#step-2-create-customer-request">Step 2: Create Customer Request <span>6</span></a></p>
<p><a href="#step-3-create-customer-quotation">Step 3: Create Customer Quotation <span>11</span></a></p>
<p><a href="#step-4-create-sales-order-referencing-a-quotation">Step 4: Create Sales Order Referencing a Quotation <span>15</span></a></p>
<p><a href="#step-5-check-stock-status">Step 5: Check Stock Status <span>17</span></a></p>
<p><a href="#step-6-track-sales-order">Step 6: Track Sales Order <span>19</span></a></p>
<p><a href="#step-7-start-delivery-process">Step 7: Start Delivery Process <span>22</span></a></p>
<p><a href="#step-8-track-sales-order">Step 8: Track Sales Order <span>24</span></a></p>
<p><a href="#step-9-pick-materials-and-post-goods-issue">Step 9: Pick Materials and Post Goods Issue <span>26</span></a></p>
<p><a href="#step-10-check-stock-status">Step 10: Check Stock Status <span>28</span></a></p>
<p><a href="#step-11-create-billing-document-for-customer">Step 11: Create billing document for Customer <span>30</span></a></p>
<p><a href="#step-12-display-billing-document-and-post-customer-invoice">Step 12: Display Billing Document and Post Customer Invoice <span>32</span></a></p>
<p><a href="#step-13-post-receipt-of-customer-payment">Step 13: Post Receipt of Customer Payment <span>33</span></a></p>
<p><a href="#step-14-review-document-flow">Step 14: Review Document Flow <span>36</span></a></p>
<p><a href="#sd-challenge">SD Challenge <span>40</span></a></p></th>
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
<th colspan="2"><h1 id="step-1-create-new-customer">Step 1: Create New Customer</h1></th>
</tr>
<tr>
<th colspan="2"><p><strong>Task</strong> Create a new customer.</p>
<p><strong>Short Description</strong> Since the app for managing business partner master data is very complex and difficult to use, in this step, you will simply copy an existing customer and adjust individual data.</p>
<p><strong>Note</strong> Alternatively, you can create the business partner completely by yourself in the system. To do this, first use the BP case study. You can then continue with this case study from step 2 onwards.</p>
<p><strong>Name (Position)</strong> David Lopez (Sales Representative US East)</p></th>
<th style="text-align: right;"><strong>Time</strong> 5 min</th>
</tr>
<tr>
<th colspan="2"></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the space <em>Sales and Distribution</em> in the role of <em>Sales Representative</em> use the app <em>Manage Business Partner Master Data</em> to create a new customer.</th>
<th>Start</th>
</tr>
<tr>
<th colspan="2"><img src="media/image3.png" style="width:1.5748in;height:1.5748in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Before you can copy the business partner you need obviously to search for the corresponding copy template. In the <em>Manage Business Partner</em> screen, focus the field <em>Last Name/Name1</em> and enter <strong>The Bike Zone</strong>. Then press <img src="media/image4.png" style="width:0.24449in;height:0.17717in" />. You will see a list of all business partners named “The Bike Zone”. Please select the unique entry and click the <img src="media/image5.png" style="width:0.32707in;height:0.17717in" /> button. The following screenshot shows the proceeding.</th>
<th>The Bike Zone</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image6.png" style="width:5.71181in;height:1.63056in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Pressing the <img src="media/image5.png" style="width:0.32707in;height:0.17717in" /> button will lead you to the <em>Business Partner</em> screen. Please make sure you are in the <em>Basic Data</em> tab. In the <em>General Information</em> section, please add your three-digit number at the end of the <em>Name 1</em> field (The Bike Zone <strong>###</strong>). Enter ### also in the <em>Search Term 1</em> field.</th>
<th><p>Basic Data</p>
<p>The Bike Zone ###</p>
<p>###</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Keep in mind to replace ### with you three-digit number, e.g. 003 if your number is 003. The number is used to distinguish between different “The Bike Zone” master records, so that you can find your own business partner among all those created in the course.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><img src="media/image7.png" style="width:5.71181in;height:2.44792in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">After that, you can click on <img src="media/image8.png" style="width:0.3884in;height:0.17717in" />. The SAP system creates the master data record for the new BP and assigns a unique business partner number. Make a note of the BP number, which you will find in the header.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image9.png" style="width:3.0948in;height:1.753in" /></th>
<th><p>Business Partner Number</p>
<p>……………………..</p></th>
</tr>
<tr>
<th colspan="2">Click on <img src="media/image10.png" style="width:0.36458in;height:0.17708in" />to return to the SAP Fiori Launchpad.</th>
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
<th colspan="2"><h1 id="step-2-create-customer-request">Step 2: Create Customer Request</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a customer inquiry.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create a customer inquiry.</p>
<p><strong>Name (Position)</strong> Matthias Dosch (Sales Person 2 US East)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now, we will enter an inquiry from our new customer, <strong>The Bike Zone</strong>. An inquiry is a customer’s request to be provided with a quotation or sales information without obligation. An inquiry can relate to materials or services, conditions, and if necessary delivery dates.</td>
<td style="text-align: right;"><p>Scenario</p>
<p>Inquiry</p></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the space <em>Sales and Distribution</em> in the role of <em>Sales</em> <em>Person</em>, use the <em>Manage</em> <em>Sales Inquiries</em> app to create an inquiry.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image11.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> This dynamic Fiori app displays 1. This means that Global Bike currently has 1 customer request. The number you see depends on the number of requests that you and the other participants have created before. You will encounter this functionality in other apps as well.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If you want to display all existing sales inquiries, press <img src="media/image4.png" style="width:0.24449in;height:0.17717in" />. A list with all inquiries is displayed. If, on the other hand, you want to enter a new sale inquiry, click on <img src="media/image12.png" style="width:0.72638in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter the abbreviation <strong>IN</strong> (<em>Inquiry</em>) as the <em>Inquiry</em> <em>Type</em> and <strong>UE00</strong> (<em>US</em> <em>East</em>) as the <em>Sales</em> <em>Organization</em>. Also add <strong>100</strong> (<em>Wholesale</em>) to the <em>Distribution</em> <em>Channel</em> field and <strong>BI</strong> (<em>Bicycles</em>) to the <em>Division</em>.</td>
<td style="text-align: right;"><p>IN</p>
<p>UE00</p>
<p>WH</p>
<p>BI</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image13.png" style="width:1.92517in;height:1.73348in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Compare your entries with the screenshot above. Then select <img src="media/image14.png" style="width:0.46671in;height:0.17502in" />, in the lower screen area, to be able to enter further data for the request. This will take you to the following screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image15.png" style="width:4.84466in;height:2.25298in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Sold-to party</em> field, enter the <strong>Business Partner Number</strong> of your customer <strong>The Bike Zone</strong>.</td>
<td style="text-align: right;">Business Partner Number (Customer)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Alternatively, you can search for your GP number by selecting the input help icon <img src="media/image16.png" style="width:0.2126in;height:0.17717in" /> in the <em>Sold-To Party</em> field. As <em>Search Term</em> enter <strong>###</strong>, and as <em>City</em> enter <strong>Orlando</strong>. Confirm your entry with enter to run the search. Double click on the <em>The Bike Zone</em> line to add the GP to the request.</td>
<td style="text-align: right;"><p>###</p>
<p>Orlando</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter <strong>###</strong> as the <em>Customer Reference</em> and enter <strong>today's</strong> <strong>date</strong> in the fields <em>Customer reference date</em> and <em>Valid</em> <em>from</em> (F4, then Enter). For the <em>Valid</em> <em>To</em> and <em>Requested</em> <em>delivery</em> <em>date</em> fields, enter <strong>one month from today</strong>.</td>
<td style="text-align: right;"><p>###</p>
<p>today’s date</p>
<p>today’s date</p>
<p>one month from today</p>
<p>one month from today</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image17.png" style="width:4.73498in;height:2.34126in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The Bike Zone would like a quote for two products: The Deluxe Touring Bike (black) and the Professional Touring Bike (black). To find these products, use the search function. Click in the <em>Material</em> field and then click on the value help icon <img src="media/image16.png" style="width:0.2126in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Material</em> <em>by</em> <em>Description</em> Tab, enter <strong>*Bike*</strong> as the <em>Material</em> <em>Description</em> and <strong>*###</strong> (e.g. *003 if your number is 003) as the <em>Material</em>.</td>
<td style="text-align: right;"><p>*Bike*</p>
<p>*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:5.09209in;height:0.89184in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then click on <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to start the search process. You will get results whose material short text contains "Bike" and whose abbreviation ends in "###".</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image19.png" style="width:4.87675in;height:3.17406in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Double click on the <strong>Deluxe Touring Bike (Black)</strong> to select it. In the following screen, enter an <em>Order</em> <em>Quantity</em> of <strong>5</strong>.</td>
<td style="text-align: right;"><p>DXTR1###</p>
<p>5</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image20.png" style="width:4.90936in;height:0.56646in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat the process for the second item, searching for <strong>Professional</strong> <strong>Touring</strong> <strong>Bike</strong> (<strong>Black</strong>) as the <em>Material</em> and entering an <em>Order</em> <em>Quantity</em> of <strong>2</strong>. Select Enter to determine the price for this request. Confirm the message that appears.</td>
<td style="text-align: right;"><p>PRTR1###</p>
<p>2</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image21.png" style="width:4.91897in;height:2.52393in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The total price for these 7 bicycles for The Bike Zone is 21,400.00 USD (net value). The expected order value is a calculated value that multiplies the net value of the order quantity by the probability that a request from this customer will result in an actual order. Select both items and click on <img src="media/image22.png" style="width:0.20472in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image23.png" style="width:4.99816in;height:0.70559in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the lower area of the <em>General</em> <em>Sales</em> <em>Data</em> you will find the field <em>Order</em> <em>Probability</em>. This expresses the percentage probability that an enquiry or quotation item will result in a sales order. Assuming this order probability would be 30%, the expected order value would be 0.30 x 21,400.00 USD = 6,420.00 USD.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Changing the order probabilities may make sense because different requests from customers have different probabilities. Change the <em>Order</em> <em>Probability</em> for the material DXTR### to 70%. Then click on <img src="media/image24.png" style="width:0.2126in;height:0.17717in" /> (Next item) in the upper area to go to material PRTR1###.</td>
<td style="text-align: right;">70</td>
</tr>
<tr>
<td colspan="2"><img src="media/image25.png" style="width:4.73469in;height:4.03404in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Also enter an <em>Order</em> <em>Probability</em> of <strong>70%</strong> there. Confirm your change with Enter. In the tab <em>Shipping</em> enter the Storage Location <strong>FG00</strong> <em>(Finished Goods)</em> for the both types of Touring Bikes. Click on <img src="media/image26.png" style="width:0.17708in;height:0.17708in" /> (Back) to update the request and note the new expected order value of 14,980.00</td>
<td style="text-align: right;"><p>70</p>
<p>FG00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image27.png" style="width:3.97967in;height:2.92859in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image28.png" style="width:4.96057in;height:2.58022in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image29.png" style="width:0.30836in;height:0.17502in" /> to save the request. The SAP system will assign a unique number to the request. Make a note of it.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image30.png" style="width:2.33705in;height:0.26232in" /></td>
<td style="text-align: right;"><p>Inquiry Number</p>
<p>________</p></td>
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
<col style="width: 12%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-3-create-customer-quotation">Step 3: Create Customer Quotation</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a customer quotation.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create a customer quotation.</p>
<p><strong>Name (Position)</strong> David Lopez (Sales Representative US East)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">An inquiry presents the terms (price, delivery schedule) to a customer considering a purchase. A quotation is similar, except that it is a legally binding offer for delivering the requested product or services.</td>
<td style="text-align: right;">Quotation</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The Bike Zone would like a firm quote for the items in the inquiry created before. We can do this easily by copying the details from the inquiry into the new quotation. To do this, in the space <em>Sales and Distribution</em> and in the role of <em>Sales Representative</em>, use the <em>Manage Sales Quotations – Version 2</em> app.</td>
<td style="text-align: right;"><p>Scenario</p>
<p>Start</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image31.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If you want to display all sales quotations, click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" />. A list will be displayed accordingly. However, if you want to respond to the inquiry you have just entered, click on <img src="media/image32.png" style="width:1.09843in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create with Reference</em> pop-up that opens, please enter your <strong>inquiry number</strong> and the code <strong>QT</strong> (<em>Quotation</em>).</td>
<td style="text-align: right;"><p>Inquiry Number</p>
<p>QT</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Alternatively, if you have forgotten your inquiry number, in the <em>sales Inquiry</em> field click the input help icon <img src="media/image16.png" style="width:0.2126in;height:0.17717in" />. In the <em>Select: Sales Inquiry</em>, as <em>Customer Reference</em> enter your number (<strong>###</strong>).</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image33.png" style="width:4.93882in;height:1.00821in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> and double-click your order. Your inquiry number will be copied to the <em>Create with Reference</em> window accordingly.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image34.png" style="width:2.02517in;height:1.44179in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image35.png" style="width:1.09843in;height:0.17717in" /> to copy the information from the inquiry to the quote screen. This will produce the following screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image36.png" style="width:4.71561in;height:3.08125in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As <em>Cust. Reference</em> enter <strong>###</strong> and as <em>Document Date</em> type in <strong>today’s date</strong>. In the <em>Valid To</em> field, please add <strong>one month from today</strong>.</td>
<td style="text-align: right;"><p>###</p>
<p>today’s date</p>
<p>one month from today</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:4.72984in;height:1.75091in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To encourage The Bike Zone to become a loyal customer, you have been authorized to give a $50.00 discount on each Deluxe Touring bike, as well as a 5% discount on the entire order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To apply the $50.00 discount, go to the <em>Items</em> tab. Select the arrow icon in the line with the <strong>Deluxe Touring Bike</strong> <img src="media/image38.png" style="width:0.21875in;height:0.17708in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image39.png" style="width:5.13216in;height:0.90363in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Prices</em> tab, you will see a screen showing the conditions of the Deluxe Touring Bike.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> The condition master data includes prices, surcharges, and discounts, freights, and taxes. You can define condition master data (condition records) to be dependent on various data. You can, for example, maintain a material price customer-specifically. In SAP, pricing is done using conditions. The pricing procedure defines which condition types are to be used to calculate the final price. Condition type PR00 is a gross price condition.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To add a discount, click on <img src="media/image40.png" style="width:0.38337in;height:0.16668in" /> and enter the <em>condition type</em> <strong>Material (K004)</strong>.</td>
<td style="text-align: right;">Material (K004)</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:2.04184in;height:1.04176in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, please click on <img src="media/image42.png" style="width:0.38337in;height:0.17502in" />. A new price element line will be created.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In there, Enter an <em>amount</em> of <strong>50</strong> in the calculation scheme and after you have pressed Enter, a new price for the 5 Deluxe Touring Bikes will be calculated.</td>
<td style="text-align: right;">50</td>
</tr>
<tr>
<td colspan="2"><img src="media/image43.png" style="width:5.02449in;height:2.06337in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Note that the discount is now applied to the order. Choose <img src="media/image44.png" style="width:0.34752in;height:0.17717in" /> to move from the position price details back to the overall <em>Sales Quotation</em> screen. To apply the 5% discount to the entire document, click on the <em>Prices 🡪 Price Elements</em>:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image45.png" style="width:5.17841in;height:2.13248in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To apply the discount above 5%, click on <img src="media/image40.png" style="width:0.38337in;height:0.16668in" /> and enter the value <strong>% Discount from Net (RA00)</strong> in the <em>Condition type</em> field.</td>
<td style="text-align: right;">RA00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image46.png" style="width:2.13336in;height:1.06229in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, please click on <img src="media/image42.png" style="width:0.38337in;height:0.17502in" /> to generate a new line.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter an <em>amount</em> of <strong>5</strong> and click Enter.</td>
<td style="text-align: right;">5</td>
</tr>
<tr>
<td colspan="2"><img src="media/image47.png" style="width:4.91816in;height:1.99217in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image42.png" style="width:0.38337in;height:0.17502in" /> to save the new quotation.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image48.png" style="width:2.05851in;height:0.83341in" /></td>
<td style="text-align: right;"><p>Quotation Number</p>
<p>_____________</p></td>
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
<th colspan="2"><h1 id="step-4-create-sales-order-referencing-a-quotation">Step 4: Create Sales Order Referencing a Quotation</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a sales order with reference to a quotation.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create a sales order.</p>
<p><strong>Name (Position)</strong> David Lopez (Sales Representative US East)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The Bike Zone has agreed to the terms and conditions in the quotation, and wants to order the bikes in the quotation. As a result, we can simplify the order creation process by copying the quotation into a sales order.</td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the space <em>Sales and Distribution</em> and in the role of <em>Sales Representative</em>, you can use the <em>Manage Sales Orders –Version 2</em> app to create a sales order.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image49.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>If you want to display all sales orders, click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" />. A list will be displayed accordingly. If you want to create a customer order for the accepted offer, follow the following path:</p>
<p>Create with Reference ► Create from Quotation.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image50.png" style="width:5.19727in;height:1.68562in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the popup <em>Create from Quotation</em>, please enter your <strong>quotation number</strong> and in the <em>Sales order type</em> the code <strong>Standard Order (OR)</strong>.</td>
<td style="text-align: right;"><p>Quotation Number</p>
<p>OR</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Alternatively, if you have forgotten your quotation number, in the <em>Sales Quotation</em> field click the input help icon <img src="media/image16.png" style="width:0.2126in;height:0.17717in" />. In the <em>Select: Sales Quotation</em>, as <em>Customer Reference</em> enter your number (<strong>###</strong>).</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2"><img src="media/image51.png" style="width:5.439in;height:1.08273in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then click <img src="media/image52.png" style="width:0.23849in;height:0.17717in" /> and double-click your order. Your number will be copied to the <em>Create from Quotation</em> popup accordingly.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image53.png" style="width:1.82868in;height:1.31252in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image54.png" style="width:1.09843in;height:0.17717in" /> to copy the information from the quotation to the <em>Sales Order</em> screen. Due to the discounts granted in the offer, please note the <em>Net Value</em> has been reduced.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image55.png" style="width:4.67805in;height:2.91095in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As <em>Customer Reference</em> enter again your <strong>three-digit number ###</strong> and as <em>Document Date</em> please add <strong>today’s date</strong>. Note that the <em>Requested</em> <em>Delivery Date</em> has been copied from the quotation. Click <img src="media/image42.png" style="width:0.38337in;height:0.17502in" /> and write down the number of your sales order.</td>
<td style="text-align: right;"><p>###</p>
<p>today’s date</p>
<p>Standard Order Number</p>
<p>…………………</p></td>
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
<th colspan="2"><h1 id="step-5-check-stock-status">Step 5: Check Stock Status</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Check the inventory.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to check the stock status.</p>
<p><strong>Name (Position)</strong> David Lopez (Sales Representative US East)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">We can check on the inventory level of the bikes in the sales order for The Bike Zone. For this purpose, in the space <em>Sales and Distribution</em> and in the role of <em>Sales Representative</em>, you can use the <em>Stock – Multiple Materials</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image56.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see the default screen of the app. Due to the high amount of materials, it is not recommended to search without further restrictions. Therefore, in the <em>Material</em> field, please use the input help icon <img src="media/image16.png" style="width:0.2126in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image57.png" style="width:5.12536in;height:0.84202in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the pop-up that opens, as <em>Description</em> enter <strong>*TOURING*</strong> and as <em>Material</em> type in your number (*<strong>###</strong>).</td>
<td style="text-align: right;"><p>*TOURING*</p>
<p>*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image58.png" style="width:4.94141in;height:0.9197in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to run the search and to generate a result list of all “touring” bikes containing your number “###” in the material code. Select the <strong>Deluxe Touring Bike (black)</strong> and the <strong>Professional Touring Bike (black)</strong>. To copy your selection to the initial screen, click on the <img src="media/image59.png" style="width:0.3971in;height:0.17717in" /> button.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image60.png" style="width:4.58882in;height:1.9209in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Back in the <em>Stock – Multiple Materials</em> overview, as <em>Plant</em> enter <strong>MI00</strong> (<em>Miami</em>) and as <em>Storage Location</em> type in <strong>FG00</strong> (<em>Finished Goods</em>). Click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to display the corresponding stock levels.</td>
<td style="text-align: right;"><p>MI00</p>
<p>FG00</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image61.png" style="width:5.17135in;height:0.62453in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">This report shows the stock levels for the plant in Miami. Scroll to the right to see the unrestricted stock.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image62.png" style="width:1.71531in;height:1.12663in" /></td>
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
<th colspan="2"><h1 id="step-6-track-sales-order">Step 6: Track Sales Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Track the processing status of the sales order.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to track a sales order.</p>
<p><strong>Name (Position)</strong> David Lopez (Sales Representative US East)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">With relatively little user input, the sales order for The Bike Zone has been created. The <em>Track Sales Orders</em> app provides the opportunity to review the order in detail.</td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display and track a sales order, in the space <em>Sales and Distribution</em> and in the role of <em>Sales Representative</em>, please use the <em>Track Sales Orders</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image63.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see the standard view of the app. In the <em>Search</em> field, enter your number (<strong>###</strong>) and click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to run the search process.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Your order will be displayed in the result list. There you can already see first details like <em>the Overall Fulfillment</em> status or the <em>Net Value</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image64.png" style="width:5.13202in;height:1.65149in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please click on the line containing your sales order. You will be forwarded to the <em>Track Sales Order Details</em> screen, where you can see all the details of the order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image65.png" style="width:5.10009in;height:2.79382in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For example, you can see that the quotation processing has been fully processed (“fully referenced”), but that the processing of the standard order is currently still “open”. You can also see the requested delivery date of the order and the planned delivery in the overview.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Afterward, please click on the <em>Items</em> tab. There you will see a list of the ordered bikes and the quantity shipped or already invoiced.</td>
<td style="text-align: right;">Items</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If the system has not selected any columns by default, we recommend that you refresh the page.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image66.png" style="width:5.08158in;height:1.06549in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go back to the <em>Process Flow</em> tab and click on your Standard Order. The following context menu opens.</td>
<td style="text-align: right;">Process Flow</td>
</tr>
<tr>
<td colspan="2"><img src="media/image67.png" style="width:3.05537in;height:1.99418in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <em>Change Sales Order</em>. You will be forwarded to the corresponding app.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image68.png" style="width:5.3125in;height:2.20486in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Items</em> tab. There, you will see information about the respective customer order items. For example, you can check the availability of the products. You can see the status in the <em>Availability</em> column. Clicking on “Confirmed” opens a detailed pop-up window.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image69.png" style="width:4.97055in;height:1.63671in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Close the popup screen with a click anywhere on the screen. Open the <em>Prices</em> tab to view the conditions again. Note that the two discounts have been manually applied to this item.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image70.png" style="width:5.3125in;height:1.51528in" /></td>
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
<col style="width: 68%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-7-start-delivery-process">Step 7: Start Delivery Process</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Start the delivery process.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to start the delivery process.</p>
<p><strong>Name (Position)</strong> Sergey Petrov (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To start the process that will fulfill The Bike Zone’s order, we need to create a delivery document. To do this, in the space <em>Sales and Distribution</em> and in the role of <em>Warehouse employee</em>, use the <em>Create Outbound Deliveries – From Sales Orders</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image71.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> The app starts with a collapsed header area. Please expand it by clicking <img src="media/image72.png" style="width:0.17222in;height:0.17708in" /> (<em>Expand Header</em>).</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image73.png" style="width:4.84563in;height:1.71102in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You trigger shipping activities by creating deliveries. The responsible organizational unit for creating deliveries is the <strong>shipping point</strong>. The shipping point can be a loading ramp, a mail depot, or a rail depot. It can also be, for example, a group of employees responsible (only) for organizing urgent deliveries.</td>
<td style="text-align: right;">Shipping Point</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Create Outbound Deliveries</em> screen, in the <em>Ship-to party</em> field please enter your business partner number (The Bike Zone).</td>
<td style="text-align: right;">Business Partner Number (Customer)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Alternatively, you can search for your GP number by selecting the input help icon <img src="media/image16.png" style="width:0.2126in;height:0.17717in" /> in the <em>Ship-to party</em> field. A pop-up screen will open. As <em>Customer</em> <em>Name 1</em> enter <strong>*###</strong>, and as <em>City</em> enter <strong>Orlando</strong>. Click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to run the search.</td>
<td style="text-align: right;"><p>*###</p>
<p>Orlando</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image74.png" style="width:5.01158in;height:1.81994in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Select your customer and apply the entry to the initial screen by clicking <img src="media/image59.png" style="width:0.3971in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In addition, as <em>Shipping Point</em> please enter <strong>MI00</strong>, and remove the <em>Planned Creation Date</em>. Click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to run the search. The sales order will be displayed.</td>
<td style="text-align: right;">MI00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image75.png" style="width:4.88961in;height:1.65113in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the sales document and choose the button <img src="media/image76.png" style="width:0.99972in;height:0.17717in" />. You will see that the sales document is no longer available. Additionally, you will receive a confirmation that your outbound delivery has been created.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image77.png" style="width:1.69418in;height:0.41649in" /></td>
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
<th colspan="2"><h1 id="step-8-track-sales-order">Step 8: Track Sales Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Track the processing status of the sales order.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to track a sales order.</p>
<p><strong>Name (Position)</strong> David Lopez (Sales Representative US East)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display and track a sales order, in the space <em>Sales and Distribution</em> and in the role of <em>Sales Representative</em>, use the <em>Track Sales Orders</em> app again.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image63.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see the standard view of the app. In the <em>Search</em> field, enter your number (<strong>###</strong>) and click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to run the search process.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2"><img src="media/image78.png" style="width:5.01733in;height:1.125in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Your order will be displayed in the result list. You can now see changes from the previous state. The <em>Overall Fulfillment</em> is now set to <em>Partially processed</em> and the <em>Order Processing</em> is <em>completely processed</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image79.png" style="width:4.93091in;height:1.67886in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Please click on the line containing your sales order. You will be forwarded to the <em>Track Sales Order Details</em> screen, where you can see all the details of the order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image80.png" style="width:4.93924in;height:3.2013in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the overview that opens, you can see the completed standard order and the delivery that is still “open”. In addition, billing has already been planned automatically by the system. In the header area, the shipping status (<em>Not shipped</em>; previously: <em>Delivery Not Started</em>) and the billing status (<em>Not invoiced</em>, previously: <em>Not Relevant for Invoicing</em>) have also changed.</td>
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
<th colspan="2"><h1 id="step-9-pick-materials-and-post-goods-issue">Step 9: Pick Materials and Post Goods Issue</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Pick materials on delivery note.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to pick materials and to post a goods issue.</p>
<p><strong>Name (Position)</strong> Sandeep Das (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Picking a material changes the outbound delivery document, while goods issue subsequently changes the ownership of the material from Global Bike to The Bike Zone. To do this, in the space <em>Sales and Distribution</em> and in the role of <em>Warehouse employee</em> use the <em>Manage Outbound Deliveries</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image81.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The app starts with a collapsed header area. Please expand it by clicking <img src="media/image72.png" style="width:0.17222in;height:0.17708in" />. In the <em>Ship-to party</em> field, please enter your <strong>business partner number</strong>.</td>
<td style="text-align: right;">Business Partner Number (Customer)</td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> If you have forgotten your GP number, proceed as in the steps before.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In addition, as the <em>Shipping Point</em> enter <strong>MI00</strong> and as <em>Overall Status</em> select <strong>All Open Deliveries</strong>. To run the search, click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" />. Your outbound delivery is now displayed.</td>
<td style="text-align: right;"><p>MI00</p>
<p>All Open Deliveries</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image82.png" style="width:4.93171in;height:1.25335in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can see that neither picking nor goods issue has been processed yet. Then, select <img src="media/image83.png" style="width:0.28346in;height:0.17717in" /> to start the picking process. You will automatically be forwarded to the <em>Pick Outbound Delivery</em> app. Your outbound delivery is already preselected.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Delivery Items</em> area, enter the appropriate quantities in the <em>Picking Quantity</em> fields: For your DXTR1### <strong>5</strong> and for your PRTR1### <strong>2</strong>.</td>
<td style="text-align: right;"><p>5</p>
<p>2</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image84.png" style="width:4.78139in;height:0.87758in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Picking</strong> is the process of preparing or staging goods for delivery to the customer, with particular attention to dates, quantity and quality.</td>
<td style="text-align: right;">Picking</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Pick Outbound Delivery</em> screen, please choose <img src="media/image85.png" style="width:0.31768in;height:0.17717in" /> . You will receive a corresponding message from the system. In addition, the screen content changes. Picking is now complete and goods issue is ready.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image86.png" style="width:3.15027in;height:0.70839in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the lower screen area, you can now click <img src="media/image87.png" style="width:0.42153in;height:0.17717in" /> to post the goods issue. The screen content changes again. Both picking and goods issue are now complete.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image88.png" style="width:4.84243in;height:1.76804in" /></td>
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
<th colspan="2"><h1 id="step-10-check-stock-status">Step 10: Check Stock Status</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Check the inventory once again.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to check the stock status.</p>
<p><strong>Name (Position)</strong> David Lopez (Sales Representative US East)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The goods issue of the order has an impact of the inventory level of the bikes for Global Bike. To have a look at it, in the space <em>Sales and Distribution</em> and in the role of <em>Sales representative</em>, use the <em>Stock – Multiple Materials</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image56.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see the default screen of the app. Due to the high amount of materials, it is not recommended to search without further restrictions. Therefore, in the <em>Material Number</em> field, please use the input help icon <img src="media/image16.png" style="width:0.2126in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image57.png" style="width:5.03603in;height:0.82735in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the pop-up that opens, as <em>Description</em> enter <strong>*TOURING*</strong> and as <em>Material</em> type in your number (*<strong>###</strong>) again.</td>
<td style="text-align: right;"><p>*TOURING*</p>
<p>*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image89.png" style="width:4.82464in;height:0.91848in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to run the search and to generate a result list of all “touring” bikes containing your number “###” in the material code. Select the <strong>Deluxe Touring Bike (black)</strong> and the <strong>Professional Touring Bike (black)</strong>. To copy your selection to the initial screen, click on the <img src="media/image59.png" style="width:0.3971in;height:0.17717in" /> button.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image90.png" style="width:3.768in;height:2.08851in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Back in the <em>Stock – Multiple Materials</em> overview, as <em>Plant</em> enter <strong>MI00</strong> (<em>Miami</em>) and as <em>Storage Location</em> type in <strong>FG00</strong> (<em>Finished Goods</em>). Click <img src="media/image52.png" style="width:0.23849in;height:0.17717in" /> to display the corresponding stock levels again.</td>
<td style="text-align: right;"><p>MI00</p>
<p>FG00</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image61.png" style="width:3.71066in;height:0.92956in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">This report shows the stock levels for the plant in Miami. Scroll to the right to see the unrestricted stock. The inventory was reduced by the quantity for which the goods issue was posted.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image91.png" style="width:1.94184in;height:1.28344in" /></td>
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
<th colspan="2"><h1 id="step-11-create-billing-document-for-customer">Step 11: Create billing document for Customer</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a billing document for a customer.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create a customer billing document.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">With the delivery complete, the customer can be invoiced. To do this, in the space <em>Sales and Distribution</em> and in the role of <em>AR</em> <em>Accountant</em>, use the <em>Create Billing Documents</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image92.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Create Billing Documents</em> screen, all <em>Billing Due List Items</em> are automatically listed. For a better overview, the listing should be filtered. To do this, in the <em>Sold-to party</em> field, enter your <strong>business partner number</strong>.</td>
<td style="text-align: right;">Business Partner Number (Customer)</td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> If you have forgotten your GP number, proceed as in the steps before.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Apply the new filter. Therefore, click on <img src="media/image52.png" style="width:0.23849in;height:0.17717in" /> to restrict the result list. Your sales document will be the only one displayed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image93.png" style="width:4.94835in;height:1.59208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select your sales document and choose <img src="media/image94.png" style="width:1.18518in;height:0.17717in" />. The system prepares the customer invoice: The date and sold-to party are copied from the previous selection.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image95.png" style="width:4.9082in;height:2.06032in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Choose the <em>Process Flow</em> tab. There you can track the steps taken in advance that are relevant for the customer invoice.</td>
<td style="text-align: right;">Process Flow</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image96.png" style="width:3.65618in;height:1.97292in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Continue to the <em>Pricing Elements</em> tab. As a billing clerk, you can view the discounts granted in the quotation creation and how the total price is thus composed.</td>
<td style="text-align: right;">Pricing Elements</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image97.png" style="width:5.09947in;height:2.50487in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">To save the new customer invoice, select <img src="media/image29.png" style="width:0.30836in;height:0.17502in" />.</td>
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
<th colspan="2"><h1 id="step-12-display-billing-document-and-post-customer-invoice">Step 12: Display Billing Document and Post Customer Invoice</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display a billing document and a customer invoice.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to display a billing document/customer invoice.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now that the billing document has been created, it needs to be posted. Therefore, in the space <em>Sales and Distribution</em> and in the role of <em>AR</em> <em>Accountant</em>, use the <em>Manage Billing Documents</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image98.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Manage Billing Documents</em> screen, in the <em>Sold-to party</em> field, please enter your <strong>business partner number</strong>.</td>
<td style="text-align: right;">Business Partner Number (Customer)</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Alternatively, in the <em>Sold-to party</em> field, click the input help icon <img src="media/image16.png" style="width:0.2126in;height:0.17717in" /> and search for your business partner using your number (<strong>###</strong>) as in the previous step.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2">Select <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to display your invoice.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image99.png" style="width:4.75099in;height:1.57678in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select your entry and choose <img src="media/image100.png" style="width:0.29324in;height:0.17717in" />. This will send the invoice to the customer.</td>
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
<th colspan="2"><h1 id="step-13-post-receipt-of-customer-payment">Step 13: Post Receipt of Customer Payment</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Post a customer payment receipt.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to post a customer payment receipt.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">After The Bike Zone mails its payment, it needs to be recorded. To do this, in the space <em>Sales and Distribution</em> and in the role of <em>AR Accountant</em> use the <em>Post Incoming Payments</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image101.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">You will be directed to the following screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image102.png" style="width:4.98334in;height:2.0279in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>General Information</em> area, as <em>Company Code</em> enter <strong>US00</strong> (<em>Global Bike Inc.</em>). In the fields <em>Posting Date</em> and <em>Journal Entry Date</em>, use <img src="media/image103.png" style="width:0.16574in;height:0.17717in" /> (<em>Open Picker</em>) to enter the <strong>current date</strong>. Also, in the <em>Period</em> field, select the <strong>current period</strong> (for example, 09 for September). As the <em>Journal Entry Type</em> make sure that <strong>DZ</strong> (<em>Customer Payment</em>) is selected.</td>
<td style="text-align: right;"><p>US00</p>
<p>Current Date</p>
<p>Current Period</p>
<p>DZ</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image104.png" style="width:2.48766in;height:2.31742in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Bank Data</em> area, as G/L account select <strong>1810000</strong> (<em>Bank 1</em>). Please also add the amount <strong>20,092.50 USD</strong>. In the <em>Open Item Selection</em> area, as the <em>Account Type</em> select <strong>Customer</strong>, and add in the field directly next to it your <strong>business partner number</strong>. Compare your entries with the following screenshots.</td>
<td style="text-align: right;"><p>1810000</p>
<p>20,092.50 USD</p>
<p>Customer</p>
<p>Business Partner Number (Customer)</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image105.png" style="width:2.8717in;height:1.7366in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image106.png" style="width:2.83608in;height:1.78988in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image107.png" style="width:0.7937in;height:0.17717in" />. In the upper part of the screen, you can see that the balance has changed to <img src="media/image108.png" style="width:1.5059in;height:0.17717in" />. This is due to the open customer invoice. In the <em>Open AP/AR Items</em> area, the posting document from the previous steps will also be proposed to you.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image109.png" style="width:4.91803in;height:0.74891in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <img src="media/image110.png" style="width:0.87972in;height:0.17717in" /> in the line of the posting document. The open items are added to the <em>Items to be Cleared</em> with the recorded incoming payment.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image111.png" style="width:4.9384in;height:0.67532in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Since the incoming payment covers the full amount, the balance is cleared again (<img src="media/image112.png" style="width:1.07037in;height:0.17717in" />). Click <img src="media/image113.png" style="width:0.28937in;height:0.17717in" /> to save the incoming payment. The system will automatically assign a number to it.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image114.png" style="width:2.27157in;height:0.84086in" /></td>
<td style="text-align: right;"><p>Journal Entry</p>
<p>Incoming Payment:</p>
<p>___________________</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Choose <img src="media/image115.png" style="width:0.43986in;height:0.17717in" /> to additionally display the posting document. In the <em>Manage Journal Entries</em> screen, you can view individual posting items.</td>
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
<th colspan="2"><h1 id="step-14-review-document-flow">Step 14: Review Document Flow</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Review the document flow.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to review the document flow.</p>
<p><strong>Name (Position)</strong> David Lopez (Sales Representative US East)</p></td>
<td style="text-align: right;"><blockquote>
<p><strong>Time</strong> 5 min</p>
</blockquote></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The document flow tool links all documents that were used in The Bike Zone’s sales order. Again, there are many ways to access the document flow tool. One way is to start by displaying the sales order document.</td>
<td style="text-align: right;">Document Flow</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display and track a sales order, in the space <em>Sales and Distribution</em> and in the role of <em>Sales</em> <em>representative</em> use the <em>Track Sales Orders</em> app again.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image63.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see the standard view of the app. In the <em>Search</em> field, enter your number (<strong>###</strong>) and click <img src="media/image4.png" style="width:0.24449in;height:0.17717in" /> to run the search process.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image116.png" style="width:4.79104in;height:1.03905in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Your order will be displayed in the result list. Again, you can see changes from the previous state. The <em>Overall Fulfillment</em> is now set to <em>Completely Processed</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image117.png" style="width:4.91382in;height:1.61505in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please click on the line containing your sales order. You will be forwarded to the <em>Track Sales Order Details</em> screen, where you can see all the details of the order. For example, in the <em>Fulfillment</em> area the document flow for the sales order is displayed. All related documents are completely generated and recorded.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image118.png" style="width:4.79962in;height:1.57029in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Depending on which document is selected, the content of the right screen changes. Thus, information on the delivery or the invoice can be viewed directly. Choosing the <em>Fulfillment Standard Order</em>, the steps from the quotation to the journal entry are displayed as a process flow. The respective documents can also be called up from here.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image119.png" style="width:5.14284in;height:1.7015in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see, in the header area, both the shipping status (<em>Completely Shipped</em>) and the invoicing status (<em>Completely Invoiced</em>) have changed again. Finally, on the <em>Process Flow</em> tab, select the journal entry to open the context menu. Click <em>Manage Journal Entries</em> to access the corresponding app.</td>
<td style="text-align: right;">Manage Journal Entries</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image120.png" style="width:3.84588in;height:2.18557in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can see the line items in the header data of the journal entry. However, choose the <em>Related Documents</em> tab. Then expand the document flow completely.</td>
<td style="text-align: right;">Related Documents</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image121.png" style="width:3.13293in;height:3.93464in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Except for the incoming payment, you can see all documents generated for the sales order. This additionally includes the customer inquiry, as well as the material document including the accounting document of the delivery.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click the document number of the sales order to open the context menu and choose <img src="media/image122.png" style="width:0.63071in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image123.png" style="width:4.44024in;height:2.19392in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the pop-up that opens, select the <em>Display Document Flow – Sales Order</em> app.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the following screen you can see both the operational document flow and the G/L document flow.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image124.png" style="width:5.07215in;height:2.01626in" /></td>
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
<th colspan="2"><h1 id="sd-challenge">SD Challenge</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><strong>Learning Objective</strong> Understand and perform an integrated order-to-cash-process.</td>
<td style="text-align: right;"><strong>Time</strong> 75 min</td>
</tr>
<tr>
<td colspan="3"><p><strong>Motivation</strong> Having successfully completed the case study <em>Sales and Distribution</em>, you should be able to perform the following task independently.</p>
<p><strong>Scenario</strong> One of your existing customers has opened an independent offshoot called “Alster Adventures” in Hamburg. They would like to benefit from your new promotion, in which there is a free Off Road Helmet for each Off Road Bike ordered. In a standard order, individual items can be marked as a free item (TANN) in the item details. Be aware that Off Road Helmets belong to a different division.</p>
<p>Create a new customer Alster Adventures using Alster Cycling (customer 138000) as a template. (<strong>Note:</strong> If you are using the copy function, you have to change the grouping to internal number assignment in the header data of the BP.) Your new customer will be supplied from the plant in Hamburg (HH00) via the sales organization Germany North (DN00). Remember that the Euro is the common currency in Europe. Companies in Germany are subject to tax. You need to expand Alster Adventures that orders can be placed for the divisions Accessories and Cross Divisions.</p>
<p>Alster Adventures places an order for five Men’s Off Road Bikes and five Women’s Off Road Bikes. You can start the process directly with the order (without inquiry and quotation). As a long-term customer, Alster Adventures will receive a 50 Euro discount per bike and 3% of the net price on the entire order.</p>
<p><strong>Task Information</strong> Carry out the order-to-cash process including receiving payment from the customer. As this task is based on the sales case study, you can use it as a guide. However, it is recommended that you complete this continuative task without help, so that you can test your acquired knowledge.</p></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</tbody>
</table>
