---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_FI-AR_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_FI-AR_en_v4.3.docx
---

Financial Accounting –

Accounts Receivable (FI-AR)

This case study describes an integrated process of external accounting and provides the understanding of the individual process steps and the underlying SAP functionality.

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
<p>Undergraduate</p>
<p>Graduate</p>
<p>Beginner</p>
<p>Focus</p>
<p>Financial Accounting</p>
<p>Accounts Receivable</p>
<p>Authors</p>
<p>Babett Ruß</p>
<p>Stefan Weidner</p>
<p>Version</p>
<p>4.3</p>
<p>Last Update</p>
<p>July 2025</p></th>
<th><p>MOTIVATION</p>
<p>During this case study, you will create various customer invoices, and then post their incoming payments and reverse and reassign incorrectly posted payments.</p>
<p>A majority of the data already exists in the SAP system. The static data, known as master data, simplifies the processing of business processes. Examples include customer data and all types of G/L accounts.</p></th>
<th></th>
<th><p>PREREQUISITES</p>
<p>Before you work on the case study, you should familiarize yourself with navigation in the SAP system.</p>
<p>To carry out this FI case study successfully, it is not necessary to have worked through the FI exercises or other case studies. However, it is recommended.</p>
<p>NOTES</p>
<p>This case study uses the fictitious model company Global Bike.</p>
<p><img src="media/image1.png" style="width:1.68893in;height:0.62765in" alt="M:\Curricula\Vorlagen\Logo_Global Bike\Global_Bike_Logo_neu_2018\Logo1.png" /></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 69%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"><mark><br />
<br />
</mark></th>
<th colspan="2" style="text-align: left;"><h1 id="process-overview">Process Overview</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Learning Objective</strong> Understand and manage an external accounting process in the area of accounts receivable (AR).</p>
<p><strong>Scenario</strong> To handle an external accounting process, you will take on different roles within Global Bike. Thereby you will work in the Financial Accounting (FI) department and there in the customer accounting department.</p>
<p><strong>Beteiligte Mitarbeiter</strong> Stephanie Bernard (AR Accountant)</p>
<p>Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 135 Min.</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p>In this case study, you will generate and post various customer invoices in isolation in the SAP system. Preceding process steps of sales, purchasing or production are not considered in this scenario for simplification reasons.</p>
<p>First, you will look at the payment terms negotiated with Global Bike Inc. customers and update them as necessary. After creating the individual customer invoices, you will post the incoming payments in the SAP system for some of them. You will then check the effect of these postings on the G/L accounts involved in the process.</p>
<p>Unfortunately, as you proceed, you discover that some of these incoming payments, and sometimes even the receivables on which they are based, have been entered incorrectly into the system. The case study covers a total of three cases:</p></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><ul>
<li><p><em>Problem scenario 1</em> – Your customer Motown Bikes has informed you by telephone that the delivery of First Aid Kits with reference ### Motown 2 is no longer required. By mutual agreement, the posting document for the delivery and services receivable is reversed (cancel the billing document). Also, check the impact of this on your balance sheet.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><ul>
<li><p><em>Problem scenario 2</em> – Your customer Philly Bikes has two outstanding payments for the same amount. He settles the first one with an incorrect reference, which is why you mistakenly settle the last open invoice with this incoming payment. You therefore have to reset and reassign the payment.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><ul>
<li><p><em>Problem scenario 3</em> – In addition, you have mistakenly posted an incoming payment from your customer Windy City Bikes. Therefore, you have to cancel the payment completely.</p></li>
</ul></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p>The SAP system distinguishes between:</p>
<ul>
<li><p>Reversal of a delivery &amp; service receivable before receipt of payment (cancel billing document)</p></li>
<li><p>Document reversal after receipt of payment</p></li>
<li><p>Reversal of a customer payment that has already been made</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>Finally, since these postings are income statement effective, you will see an impact on the balance sheet and income statement.</p>
<p>Below you will first find an overview of all affected invoices/postings.</p>
<table style="width:97%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 38%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th><strong>Customer</strong></th>
<th><strong>Text</strong></th>
<th><strong>Reference</strong></th>
<th><strong>Amount</strong></th>
<th><strong>Cash<br />
discount</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Motown Bikes</td>
<td>Inv: Bicycle Accessories</td>
<td>### Motown 1</td>
<td>5.000</td>
<td>yes</td>
</tr>
<tr>
<td>Motown Bikes</td>
<td>Inv: First Aid Kits</td>
<td>### Motown 2</td>
<td>2.000</td>
<td>yes</td>
</tr>
<tr>
<td>Philly Bikes</td>
<td>Inv: Men´s Off Road Bikes</td>
<td>### Philly 1</td>
<td>3.500</td>
<td>no</td>
</tr>
<tr>
<td>Philly Bikes</td>
<td>Inv: Women´s Off Road Bikes</td>
<td>### Philly 2</td>
<td>3.500</td>
<td>no</td>
</tr>
<tr>
<td>Big Apple Bikes</td>
<td>Inv: Professional Touring Bikes Red</td>
<td>### Apple 1</td>
<td>6.000</td>
<td>no</td>
</tr>
<tr>
<td>Peachtree Bikes</td>
<td>Inv: Helmet</td>
<td>### Peachtree 1</td>
<td>10.000</td>
<td>no</td>
</tr>
<tr>
<td>Windy City Bikes</td>
<td>Inv: Bike &amp; Accessories</td>
<td>### Windy 1</td>
<td>4.000</td>
<td>no</td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><img src="media/image2.png" style="width:6.48056in;height:1.42358in" /></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><h1 id="table-of-contents" class="TOC-Heading">Table of Contents</h1>
<p><a href="#process-overview">Process Overview <span>2</span></a></p>
<p><a href="#step-1-change-terms-of-payment-for-a-customer">Step 1: Change Terms of Payment for a Customer <span>4</span></a></p>
<p><a href="#step-2-create-customer-invoice">Step 2: Create Customer Invoice <span>8</span></a></p>
<p><a href="#step-3-display-customer-balances">Step 3: Display Customer Balances <span>14</span></a></p>
<p><a href="#step-4-post-an-incoming-payment">Step 4: Post an Incoming Payment <span>17</span></a></p>
<p><a href="#step-5-display-customer-balances">Step 5: Display Customer Balances <span>22</span></a></p>
<p><a href="#step-6-scenario-1-cancel-receivablebill">Step 6: Scenario 1 – Cancel Receivable/Bill <span>24</span></a></p>
<p><a href="#step-7-scenario-2-change-invoice-assignment">Step 7: Scenario 2 – Change Invoice Assignment <span>29</span></a></p>
<p><a href="#step-8-scenario-3-reset-and-revers-incoming-payment">Step 8: Scenario 3 – Reset and Revers Incoming Payment <span>35</span></a></p></th>
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
<th colspan="2"><h1 id="step-1-change-terms-of-payment-for-a-customer">Step 1: Change Terms of Payment for a Customer</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Change the terms of payment of your customer.</p>
<p><strong>Short Description</strong> Change the terms of payment of your customer <em>Motown Bikes</em> to grant a discount.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The business partner <em>Motown Bikes</em> has negotiated new conditions with the finance department of Global Bike. If the customer settles his invoice within 14 days, he will automatically be granted a 2% discount. In order for this to happen automatically when the incoming payment is posted, you need to change the master data of this customer. By maintaining this information in the master data record, the system calculates discounts and rebates automatically.</td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please go to the <em>Financial Accounting</em> space and choose the <em>Accounts</em> Receivable page. In the <em>AR Accountant</em> section, use the <em>Manage Business Partner Master Data</em> app to change your customer's master record.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><blockquote>
<p><img src="media/image3.png" style="width:1.5748in;height:1.5748in" /></p>
</blockquote></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Manage Business Partner</em> window, in the <em>Search</em> field at the top left enter <strong>Motown</strong> and then click <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />. As a result, you will get a lot, more precisely 1000, customers with the name <em>Motown Bikes</em>.</td>
<td style="text-align: right;">Motown</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image5.png" style="width:3.71033in;height:2.46589in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> In the real company <em>Global Bike</em>, the business partner <em>Motown Bikes</em> would of course have only one and not 1000 master records. The SAP S/4HANA teaching and learning environment presented here, however, allows up to 1000 students to work on business processes in parallel. Each learner has his or her own copy of each master data record for this purpose.</td>
<td style="text-align: right;">1000 copies</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To ensure that each student uses the correct master record, the user's three-digit number has been stored for each of these in the <em>Search Term 1</em> field.</td>
<td style="text-align: right;">Search Term 1</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Since the <em>Search Term 1</em> field is not a default filter criterion of this app, you need to add it first. To do this, select the button <img src="media/image6.png" style="width:0.6042in;height:0.14584in" /> on the right.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Adapt Filters</em> window, scroll down to the <em>General Information - Name</em> section and open it by clicking on the icon <img src="media/image7.png" style="width:0.23259in;height:0.18898in" />. Select the <em>Search Term 1</em> checkbox there and confirm with <img src="media/image8.png" style="width:0.22047in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image9.png" style="width:5.3265in;height:0.25962in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the additional field that now appears, enter your three-digit number (###) and click again on <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The results list should now contain only one entry: Your customer <em>Motown Bikes</em> in Detroit. To see all the detailed information of the business partner, click on the icon <img src="media/image10.png" style="height:0.1354in" /> at the end of the line.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image11.png" style="width:5.09353in;height:0.54179in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Business Partner</em> window that opens, first check that your three-digit number (###) is actually in the <em>Search Term 1</em> field. After you have made sure of this, click in the upper right corner on <img src="media/image12.png" style="width:0.26378in;height:0.17717in" />. This will not only allow you to view the properties of these customers, but also to change them. You will see that the fields are now ready for input.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image13.png" style="width:5.15764in;height:2.00208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now scroll down to the <em>Roles</em> area. You will see that two business partner roles are assigned to this customer. Click the <img src="media/image14.png" style="width:0.11806in;height:0.1389in" /> icon at the end of the row of role <em>FLCU00</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image15.png" style="width:5.25984in;height:0.59844in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As a result, among other things, the <em>Company Codes</em> area has been added. Click on it.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image16.png" style="width:4.98896in;height:0.39578in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note</strong> The single line (<em>US00</em>) means that the customer Motown Bikes is only known to the subsidiary Global Bike Inc. in the USA and can currently only purchase goods there.</p>
<p>If he should want to purchase goods from <em>Global Bike Germany GmbH</em> at some point, the company code DE00 must be assigned to him here beforehand and certain basic settings must be made.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">At the end of the line of company code <em>US00</em>, click the icon <img src="media/image10.png" style="height:0.1354in" />. In the following window scroll down to the <em>Finance</em> area. In the <em>Payment Terms</em> field select the value help icon <img src="media/image17.png" style="width:0.17501in;height:0.17501in" />. From the list of payment terms select the entry <strong>0002</strong> (<em>within 14 days 2% cash discount, within 30 days Due net</em>).</td>
<td style="text-align: right;">0002</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:4.09762in;height:1.33571in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Automatic Payment Transactions</em> section, in the <em>Payment Methods</em> field, use the value help icon <img src="media/image17.png" style="width:0.17501in;height:0.17501in" />. In the popup <em>Select: Payment Methods</em>, select the entry <strong>I</strong> (<em>Incoming Payment</em>).</td>
<td style="text-align: right;">I</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image19.png" style="width:5.09943in;height:2.49513in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then click at the bottom right on <img src="media/image20.png" style="width:0.40974in;height:0.21529in" />. Back in the <em>Customer</em> screen, click on <img src="media/image21.png" style="width:0.37068in;height:0.18898in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">This will take you back to the initial screen of the <em>Motown Bikes</em> business partner. Here you click on the bottom right <img src="media/image22.png" style="width:0.29921in;height:0.17717in" />. You will receive the following message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image23.png" style="width:2.03838in;height:0.48075in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-2-create-customer-invoice">Step 2: Create Customer Invoice</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create multiple accounts receivable invoices.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to enter manually multiple customer invoices in the system.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In this step, you will create seven customer invoices in the SAP system. Debtors (lat. debere = to owe) are business partners against whom there are receivables for services rendered.</td>
<td style="text-align: right;">Debtor</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The <em>accounts receivable</em> summarizes the individual receivables of a customer and is usually maintained in the customer sub-ledger. In parallel, a collective account, also called a reconciliation account, is maintained in the general ledger. Normally, this account is called <em>trade receivables</em>.</td>
<td style="text-align: right;">Accounts Receivable</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a customer invoice, go to the <em>Financial Accounting</em> space and choose the <em>Accounts</em> Receivable page. In the <em>AR Accountant</em> section, open the <em>Create Outgoing Invoices</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><blockquote>
<p><img src="media/image25.png" style="width:1.5748in;height:1.5748in" /></p>
</blockquote></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If the following popup appears, in the <em>Company Code</em> field enter <strong>US00</strong> and confirm with <img src="media/image26.png" style="width:0.21872in;height:0.17706in" />. If it does not appear, click the button <img src="media/image27.png" style="width:0.91581in;height:0.18898in" />.</td>
<td style="text-align: right;">US00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image28.png" style="width:2.55386in;height:1.25622in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> You can change the company code at any time by using the <img src="media/image27.png" style="width:0.91581in;height:0.18898in" /> button.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Enter Customer Invoice: Company Code US00</em> screen, search for your customer number for Motown Bikes by clicking the value help icon <img src="media/image17.png" style="width:0.17501in;height:0.17501in" /> in the <em>Customer</em> field.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As <em>Search term</em> enter your three-digit number (<strong>###</strong>) and the <em>name</em> of your customer <strong>Motown Bikes</strong> and select <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>###</p>
<p>Motown Bikes</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image29.png" style="width:5.04962in;height:1.09668in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Double-click on your customer to select his number. As <em>Invoice Date</em> enter <strong>today's date</strong> and as <em>Amount</em> enter <strong>5000</strong>. For <em>Reference</em> enter <strong>### Motown 1</strong> and for text <strong>Inv: Bicycle Accessories</strong>.</td>
<td style="text-align: right;"><p>today’s date</p>
<p>5000</p>
<p>### Motown 1</p>
<p>Inv: Bicycle Accessories</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image30.png" style="width:5.08804in;height:2.55464in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now go to the <em>Items</em> area. In the first line, for <em>G/L account</em> enter <strong>4000000</strong> (<em>Sales</em>), for <em>D/C</em> select <strong>Credit</strong> and for <em>Amount in document currency</em> enter <strong>5000</strong>. Confirm your entries. Confirm any warning messages with Enter.</td>
<td style="text-align: right;"><p>4000000<br />
Credit</p>
<p>5000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Note that the SAP system automatically transfers the payment terms from the customer master data.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image31.png" style="width:3.75902in;height:2.21027in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image32.png" style="width:0.61054in;height:0.18898in" /> at the top. Again, please confirm any warning messages that may be displayed by pressing Enter.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image33.png" style="width:4.81536in;height:2.46701in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image34.png" style="width:0.26772in;height:0.17717in" />. Confirm warning messages with Enter one last time.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image35.png" style="width:4.1208in;height:0.27938in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat this step of creating customer invoices exactly six more times. Start with the second invoice to Motown Bikes. Use the tabular overview in the scenario at the beginning of this case study.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Invoice 2</strong> The second invoice for the sale of first aid kits to <em>Motown Bikes</em> is <em>2000 USD</em>.</td>
<td style="text-align: right;">Motown Bikes</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image36.png" style="width:4.14236in;height:2.3587in" /></td>
<td style="text-align: right;"><p>today’s date</p>
<p>### Motown 2</p>
<p>2000</p>
<p>Inv: First Aid Kits</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:5.15764in;height:0.71389in" /></td>
<td style="text-align: right;"><p>4000000</p>
<p>Credit</p>
<p>2000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Invoice 3</strong> The next accounts receivable invoice is for the sale of Men's Off Road Bikes to the customer <em>Philly Bikes</em> for <em>3500 USD</em>.</td>
<td style="text-align: right;">Philly Bikes</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image38.png" style="width:4.17527in;height:2.16774in" /></td>
<td style="text-align: right;"><p>today’s date</p>
<p>### Philly 1</p>
<p>3500</p>
<p>Inv: Men’s Off Road Bikes</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image39.png" style="width:4.44467in;height:0.59186in" /></td>
<td style="text-align: right;"><p>4000000</p>
<p>Credit</p>
<p>3500</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Invoice 4</strong> The fourth invoice to <em>Philly Bikes</em> is also for <em>3500 USD</em>, but for the sale of Women's Off Road Bikes.</td>
<td style="text-align: right;">Philly Bikes</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image40.png" style="width:4.28733in;height:2.24382in" /></td>
<td style="text-align: right;"><p>today’s date</p>
<p>### Philly 2</p>
<p>3500</p>
<p>Inv: Women’s Off Road Bikes</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image39.png" style="width:4.44467in;height:0.59186in" /></td>
<td style="text-align: right;"><p>4000000</p>
<p>Credit</p>
<p>3500</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Invoice 5</strong> You create the fifth accounts receivable invoice for <em>Big Apple Bikes</em> for <em>6000 USD</em> for the sale of Professional Touring Bikes Red.</td>
<td style="text-align: right;">Big Apple Bikes</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:4.38731in;height:2.28197in" /></td>
<td style="text-align: right;"><p>today’s date</p>
<p>### Apple 1</p>
<p>6000</p>
<p>Inv: Professional Touring Bikes Red</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image42.png" style="width:4.50936in;height:0.6108in" /></td>
<td style="text-align: right;"><p>4000000</p>
<p>Credit</p>
<p>6000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Invoice 6</strong> The next bill is for <em>Peachtree Bikes</em> over <em>10000 USD</em> for helmet sales.</td>
<td style="text-align: right;">Peachtree Bikes</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image43.png" style="width:4.0685in;height:2.44811in" /></td>
<td style="text-align: right;"><p>today’s date</p>
<p>### Peachtree 1</p>
<p>10000</p>
<p>Inv: Helmet</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image44.png" style="width:4.58314in;height:0.68003in" /></td>
<td style="text-align: right;"><p>4000000</p>
<p>Credit</p>
<p>10000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Invoice 7</strong> The last invoice is for <em>Windy City Bikes</em> for <em>4000 USD</em> for the sale of bikes and accessories.</td>
<td style="text-align: right;">Windy City Bikes</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Please note that this customer would like to pay <em>by check</em> and you indicate this accordingly.</td>
<td style="text-align: right;">Payment by check</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image45.png" style="width:4.31011in;height:2.71595in" /></td>
<td style="text-align: right;"><p>today’s date</p>
<p>### Windy 1</p>
<p>4000</p>
<p>Inv: Bike &amp; Accessories</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image46.png" style="width:4.47793in;height:0.63126in" /></td>
<td style="text-align: right;"><p>4000000</p>
<p>Credit</p>
<p>4000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To change the payment method, click on the <em>Payment</em> tab (to the right of <em>Basic data</em>) before posting. Confirm warning messages again with Enter.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Payment Method</em> field, click the value help icon <img src="media/image17.png" style="width:0.17501in;height:0.17501in" /> and double-click to select <strong>C</strong> (<em>Check</em>). Click on <img src="media/image34.png" style="width:0.30557in;height:0.2014in" />. Confirm warning messages with Enter.</td>
<td style="text-align: right;">C</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad. Confirm any warning messages of your browser with OK.</td>
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
<th colspan="2"><h1 id="step-3-display-customer-balances">Step 3: Display Customer Balances</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the balances of your customer accounts.</p>
<p><strong>Short Description</strong> Now that you have created numerous customer invoices, use the SAP Fiori Launchpad to create a balance overview of your customers.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In this step, you check the <em>customer balances</em>. The debit and credit amounts as well as the balances are displayed by company code, fiscal year and customer. You can also display all the associated line items.</td>
<td style="text-align: right;">Customer balances</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>AR Accountant</em> section, use the <em>Display Customer Balances</em> app to display customer balances.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image47.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">First, in the <em>Customer</em> field, click the value help icon <img src="media/image17.png" style="width:0.17501in;height:0.17501in" />. In the <em>Customer</em> window that opens, find and select <img src="media/image48.png" style="width:0.21805in;height:0.17717in" /> next to <em>Customers (General)</em> at the top left. There, select the second entry: <strong>Customers (by company code)</strong>.</td>
<td style="text-align: right;">Customer<br />
(by company code)</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image49.png" style="width:2.68039in;height:1.7938in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">This will cause the <em>Search Term</em> field to appear, among other things. Enter your three-digit number (<strong>###</strong>) in this field. In the search field at the top, enter <strong>Motown</strong>. Compare your entries with the screenshot below and click <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>###</p>
<p>Motown</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image50.png" style="width:5.15748in;height:1.1708in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the only result row with your customer <em>Motown Bikes</em> by selecting the checkbox at the beginning of the row. After that click on <img src="media/image8.png" style="width:0.22047in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image51.png" style="width:5.11811in;height:0.50237in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Back in the initial <em>Display Customer Balances</em> screen, the number of your business partner <em>Motown Bikes</em> has been copied into the <em>Customer</em> field. In the <em>Company Code</em> field, enter <strong>US00</strong> and as <em>Fiscal Year</em> enter the <strong>current year</strong>. Compare your entries with the screenshot below and then click <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image52.png" style="width:5.0031in;height:0.76458in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As a result, you will get a list of all balances of this customer account sorted by period (month) and debit/credit. Click on the amount in the <em>Debit</em> column in the row of the month in which you entered the customer invoices in the previous step.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image53.png" style="width:5.00582in;height:1.83733in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Manage Customer Line Items</em> screen that opens, you will see a list of all the line items in this customer account that match the selection criteria from the previous screen. The posting document numbers should match those of your first two generated customer invoices.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image54.png" style="width:4.97713in;height:0.51534in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">What does the red icon in the item's <em>Clearing Status</em> column mean?</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-4-post-an-incoming-payment">Step 4: Post an Incoming Payment</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Post incoming payments from your customers.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to post some incoming payments to the customer invoices you generate.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 25 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In this step, you post the incoming payment for the following customer invoices: ### Motown 1, ### Philly 1, ### Apple 1, ### Peachtree 1, ### Windy 1.</td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post customer invoices, go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>AR Accountant</em> section, open the <em>Post Incoming Payments</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image55.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Type in the <em>Company Code</em> field <strong>US00</strong>, in the <em>Posting Date</em> and <em>Journal Entry Date</em> fields enter <strong>today's date</strong>, the <strong>current period</strong> (for example, 07 for July), as <em>G/L Account</em> <strong>1810000</strong> (<em>Bank 1</em>), as <em>Amount</em> <strong>4900 USD</strong>, and as <em>Reference</em> <strong>### Motown 1</strong>. Press Enter.</td>
<td style="text-align: right;"><p>US00</p>
<p>today’s date (2x)<br />
current period</p>
<p>1810000</p>
<p>4900 USD</p>
<p>### Motown 1</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image56.png" style="width:5.05633in;height:2.1139in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Open Item</em> <em>Selection</em> area, make sure that <strong>Customer</strong> is selected in the <em>Account Type</em> dropdown. Then, in the <em>Account ID</em> field, click the value help icon <img src="media/image17.png" style="width:0.17501in;height:0.17501in" />.</td>
<td style="text-align: right;">Customer</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Select: Customer</em> popup, enter your three-digit number (<strong>###</strong>) as the <em>Search Term</em> and <strong>Motown</strong> in the search field at the top. Compare your entries with the screenshot below and then click <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>###</p>
<p>Motown</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image57.png" style="width:5.15764in;height:1.65486in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The only result you will get is your client <em>Motown Bikes</em>. Click on this line. In the <em>Post Incoming Payments screen</em> click on <img src="media/image58.png" style="width:0.68031in;height:0.18898in" /> now.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image59.png" style="width:4.84749in;height:2.20085in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Open Items</em> area, the system shows you exactly the two posting documents for the customer invoices you created earlier.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image60.png" style="width:5.15764in;height:0.90208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">At the end of the line with the item text <em>Inv: Bicycle Accessories</em>, click <img src="media/image61.png" style="width:0.93035in;height:0.18898in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image62.png" style="width:5.15764in;height:0.67222in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The system automatically calculates a <em>Discount Amount</em> of 100 USD because you had negotiated 2% cash discount with the customer as payment terms for payment within 14 days.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image63.png" style="width:5.15764in;height:0.92708in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Check the balance <img src="media/image64.png" style="width:1.24984in;height:0.11457in" /> in the upper right corner and then click <img src="media/image34.png" style="width:0.26772in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image65.png" style="width:3.14633in;height:1.19444in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Select <img src="media/image66.png" style="width:0.42651in;height:0.17717in" /> to view the complete journal entry.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image67.png" style="width:5.15764in;height:2.17708in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You have also received payments from your clients Big Apple Bikes, Peachtree Bikes, Windy City Bikes and the first invoice from Philly Bikes for the Men's Off Road Bike. Navigating back, you get an information popup. Confirm it with a click on <img src="media/image68.png" style="width:0.43307in;height:0.17717in" /> and post the additional payments.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p><strong>Incoming payment ### Apple 1</strong></p>
<p>Customer Big Apple Bikes over $6,000 for Inv: Professional Touring Bike-Red</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image69.png" style="width:5.15764in;height:2.24792in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image61.png" style="width:0.93035in;height:0.18898in" /> for item text <em>Inv: Professional Touring Bike-Red</em>. Check the balance <img src="media/image64.png" style="width:1.24984in;height:0.11457in" /> and click <img src="media/image34.png" style="width:0.26772in;height:0.17717in" />. Select the button <img src="media/image70.png" style="width:0.97395in;height:0.18898in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p><strong>Incoming payment ### Philly 1</strong></p>
<p>Customer Philly Bikes over $3.500 for Inv: Men´s Off Road Bikes</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image71.png" style="width:5.05106in;height:2.13958in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image61.png" style="width:0.93035in;height:0.18898in" /> for item text <em>Inv: Men´s Off Road Bike</em>s.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Check the balance <img src="media/image64.png" style="width:1.24984in;height:0.11457in" /> and click <img src="media/image34.png" style="width:0.30557in;height:0.2014in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image72.png" style="width:2.68613in;height:1.02208in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Important:</p>
<ul>
<li><p>Make a note of the journal entry number for future task:</p></li>
<li><p>Please also note the journal entry date:</p></li>
</ul></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the button <img src="media/image70.png" style="width:0.97395in;height:0.18898in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p><strong>Incoming payment ### Peachtree 1</strong></p>
<p>Customer Peachtree Bikes, $10,000 for Inv: Helmet</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image73.png" style="width:4.81574in;height:2.08529in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image61.png" style="width:0.93035in;height:0.18898in" /> for item text <em>Inv: Helmet</em>. Check the balance <img src="media/image64.png" style="width:1.24984in;height:0.11457in" /> and click <img src="media/image34.png" style="width:0.30557in;height:0.2014in" />. Select the button <img src="media/image70.png" style="width:0.97395in;height:0.18898in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p><strong>Incoming payment ### Windy 1</strong></p>
<p>Customer Windy City Bikes $4,000 for Inv: Bike &amp; Accessories</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image74.png" style="width:4.93191in;height:2.2757in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image61.png" style="width:0.93035in;height:0.18898in" /> for item text <em>Inv: Bike &amp; Accessories</em>. Check the balance <img src="media/image64.png" style="width:1.24984in;height:0.11457in" /> and click <img src="media/image34.png" style="width:0.30557in;height:0.2014in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Important:</p>
<ul>
<li><p>Make a note of the journal entry number for future task:</p></li>
<li><p>Please also note the journal entry date:</p></li>
</ul></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the button <img src="media/image70.png" style="width:0.97395in;height:0.18898in" /> and click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-5-display-customer-balances">Step 5: Display Customer Balances</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the balances of your accounts receivable.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to view the impact of the last step on customer balances.</p>
<p><strong>Name (Position)</strong> Stephanie Bernard (AR Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the balances of your accounts, go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>AR Accountant</em> section, open the <em>Display Customer Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image75.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">On the <em>Display Customer Balances</em> screen, click the value help icon <img src="media/image17.png" style="width:0.17501in;height:0.17501in" /> in the <em>Customer</em> field and select your customers <strong>Motown Bikes, Philly Bikes, Big Apple Bikes, Peachtree Bikes</strong>, and <strong>Windy City Bikes</strong>.</td>
<td style="text-align: right;"><p>Motown Bikes</p>
<p>Philly Bikes</p>
<p>Big Apple Bikes</p>
<p>Peachtree Bikes</p>
<p>Windy City Bikes</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image76.png" style="width:5.06063in;height:3.34218in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Confirm your choice by clicking <img src="media/image8.png" style="width:0.22047in;height:0.17717in" />. Back in the <em>Display Customer Balances</em> screen, enter your <em>Company Code</em> <strong>US00</strong> and as the <em>Fiscal Year</em> the <strong>current year</strong>.</td>
<td style="text-align: right;"><p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image77.png" style="width:5.15764in;height:0.88889in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image78.png" style="width:5.15764in;height:2.42361in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the previous step, you cleared all open customer invoices except ### Motown 2 and ### Philly 2 by posting an incoming payment. In the SAP system, you will see the open $5,500 from Motown Bikes and Philly Bikes as the balance and the posted $28,500 in the credit. The debit contains all the receivables from the debtors and the credit contains the payments (or credit memos).</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on the $28,500 in the <em>Credit</em> column of the current period.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image79.png" style="width:4.99991in;height:1.12493in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can see that 5 items have a balanced status. In the <em>Journal entry</em> column, you can find the list of the related accounting documents.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-6-scenario-1-cancel-receivablebill">Step 6: Scenario 1 – Cancel Receivable/Bill</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Cancel the invoice for the receivable from <em>Motown Bikes</em>.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to cancel the receivable.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Your customer <em>Motown Bikes</em> has informed you by telephone that the delivery of the First Aid Kit FAID with the reference ### Motown 2 is no longer needed. Therefore, you must cancel the invoice document for the trade accounts receivable. Also, check the influence of this on your balance sheet.</td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Substep 1 Go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, use the app <em>Balance Sheet/Income Statement</em> to view the effect of your open trade receivables.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image80.png" style="width:1.55906in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For <em>Company Code</em> enter <strong>US00</strong>, for <em>Ledger</em> choose <strong>0L</strong>, and as <em>Statement Version</em> enter <strong>G###</strong>. Make sure that you select the <strong>period</strong> in which you made the posting from the previous step as the end and comparison end period. The fiscal years correspond in each case to the current and the previous one.</td>
<td style="text-align: right;"><p>US00<br />
0L</p>
<p>G###<br />
period</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image81.png" style="width:4.9513in;height:0.60466in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> If you do not see any fields to fill in, click <img src="media/image82.png" style="width:0.18898in;height:0.18898in" /> to display the fields.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />. Make sure that the <em>All Accounts</em> tab is displayed. Use <img src="media/image83.png" style="width:0.23259in;height:0.18898in" /> to expand the tree path completely.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image84.png" style="width:5.15764in;height:3.09167in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Pay attention to the <em>Trade receivables</em> line.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image85.png" style="width:5.15764in;height:0.16736in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> The total is not user specific. All users post to the same company code. In addition, the SD case study may have an effect on this.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Substep 2 Go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, use the <em>Manage Journal Entries</em> app to view the open balances.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image86.png" style="width:1.55118in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Type in the <em>Company Code</em> field <strong>US00</strong> and for <em>Fiscal Year</em> the <strong>current year</strong>. Please add also your <strong>journal entry</strong> and the corresponding <strong>journal entry date</strong> from the previous step.</td>
<td style="text-align: right;"><p>US00</p>
<p>current year</p>
<p>Journal Entry</p>
<p>Journal Entry Date</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If you have not noted the data, you can find the journal entry by using the <em>Display Customer Balances</em> app. To do this, enter your <strong>customer</strong>, your <em>company code</em> <strong>US00</strong> and the <strong>current fiscal year</strong>. Confirm with Enter.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image87.png" style="width:5.04347in;height:3.52235in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on your debit entry in the current period <img src="media/image88.png" style="width:0.56693in;height:0.18898in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image89.png" style="width:5.15764in;height:0.70139in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image90.png" style="width:5.15764in;height:2.15764in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select your journal entry and click.<img src="media/image91.png" style="width:0.5125in;height:0.23819in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Reverse Journal Entries</em> pop-up, enter the original posting date.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image92.png" style="width:3.77164in;height:3.36741in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Press <img src="media/image93.png" style="width:0.50353in;height:0.22379in" />. You will receive a confirmation.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image94.png" style="width:1.86895in;height:0.58184in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Substep 3 To view the effect of the reversal, please go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, open again the <em>Balance Sheet/Income Statement</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image95.png" style="width:1.57478in;height:1.58334in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For <em>Company Code</em> enter <strong>US00</strong>, for <em>Ledger</em> choose <strong>0L</strong>, and as <em>Statement Version</em> enter <strong>G###</strong>. Make sure that you select the <strong>period</strong> in which you made the posting from the previous step as the end and comparison end period. The fiscal years correspond in each case to the current and the previous one.</td>
<td style="text-align: right;"><p>US00</p>
<p>0L</p>
<p>G###</p>
<p>period</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />. Make sure that the <em>All Accounts</em> tab is displayed. Use <img src="media/image83.png" style="width:0.23259in;height:0.18898in" /> to expand the tree path completely.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image96.png" style="width:5.15764in;height:2.17431in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Pay attention to the line <em>Trade receivables</em>. The period balance should now be lower. Note that the total is not user specific. All users post to the same company code. Also, the SD case study may have an effect on this.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-7-scenario-2-change-invoice-assignment">Step 7: Scenario 2 – Change Invoice Assignment</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Change the assignment of the customer invoice from <em>Philly Bikes</em>.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to change the assignment of the payment.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Unfortunately, an error has crept into your work. You had two bills over $3,500 each for your customer Philly Bikes.</p>
<ul>
<li><p>### Philly 1: Inv: Men´s Off Road Bike</p></li>
<li><p>### Philly 2: Inv: Women´s Off Road Bike</p></li>
</ul>
<p>The amount of money received from Philly Bikes over 3500 USD has been misclassified by your customer. That's why you have assigned the payment to the reference <em>### Philly 1</em>. Your customer has now informed you that the payment should balance the invoice with reference <em>### Philly 2</em>. You have to correct this now. Unlike Step 8, in which you later cancel the entire incoming payment, you simply have to change the assignment here. The money remains with us and only the compensation allocation and thus the still due documents are exchanged.</p></td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Substep 1 To display the open items, go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, open the <em>Display Customer Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image97.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Display Customer Balances</em> screen, search for your customer <strong>Philly Bikes</strong>. Also, enter your <em>Company Code</em> <strong>US00</strong> and as your <em>Fiscal Year</em> the <strong>current year</strong>. Click <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>Philly Bikes</p>
<p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image98.png" style="width:5.15764in;height:3.00347in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on your <em>credit</em> in the <em>current period</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image99.png" style="width:5.15764in;height:0.56875in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Note the number of the journal entry (<em>1400...</em>):</p>
<p>_____________________</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Substep 2</strong> Please go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, you can use the <em>Reset Cleared Items</em> app to undo the assignment of the payment to the open item.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image100.png" style="width:1.55906in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Reset Cleared Items</em> window, enter your <strong>Philly Bikes clearing entry</strong> (Step 4), as <em>Company Code</em> <strong>US00</strong> and as <em>Clearing Fiscal Year</em> the <strong>current year</strong>. Click on <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>Philly Bikes<br />
clearing entry</p>
<p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image101.png" style="width:5.15764in;height:1.16111in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">At the end of the line, click on <img src="media/image10.png" style="height:0.1354in" /> to open the details. You now have two options:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><ul>
<li><p><em>Reset</em> The assignment of the payment to the open item is reset.</p></li>
<li><p><em>Reset and Reverse</em> The assignment of the payment to the open item is reset and the incoming payment is cancelled.</p></li>
</ul></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image102.png" style="width:5.15764in;height:4.24375in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the lower screen area, click on <img src="media/image103.png" style="width:0.37068in;height:0.18898in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image104.png" style="width:3.00749in;height:1.18946in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Confirm by pressing the <img src="media/image68.png" style="width:0.43307in;height:0.17717in" /> button and click on <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Substep 3</strong> Previously you had incorrectly assigned the incoming payment of your customer Philly Bikes to the open receivable <em>### Philly 1</em>. You reversed this assignment in the previous substep.</p>
<p>In this substep, you need to assign this item to customer invoice <em>### Philly 2</em>. Therefore, go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, open the <em>Display Customer Balances</em> app to display the open balances.</p></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image105.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Display Customer Balances</em> screen, search for your <em>Customer</em> <strong>Philly Bikes</strong>. Also, enter your <em>Company Code</em> <strong>US00</strong> and as your <em>Fiscal Year</em> the <strong>current year</strong>. Choose <img src="media/image4.png" style="width:0.19685in;height:0.17717in" /> and then click on your <em>debit</em> in the <em>current period</em>. You can see that both invoices now are in the status <em>Open</em> again.</td>
<td style="text-align: right;"><p>Philly Bikes</p>
<p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image106.png" style="width:5.15764in;height:1.34514in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Substep 4</strong> Previously, you had incorrectly assigned the incoming payment from your customer <em>Philly Bikes</em> to the open receivable <em>### Philly 1</em>. You reversed this assignment in the previous substep. In this substep, you have to assign this item to customer invoice <em>### Philly 2</em>.</td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, open the <em>Assignment of Open Items</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image107.png" style="width:1.54331in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><img src="media/image108.png" style="width:5.15764in;height:1.70764in" /><br />
Click on <img src="media/image109.png" style="width:0.85827in;height:0.19685in" /></p>
<p>In the <em>Customer field</em>, enter <strong>Philly Bikes</strong> as your customer and <strong>US00</strong> as the <em>Company Code</em>. Click on <img src="media/image4.png" style="width:0.19685in;height:0.17717in" /></p></td>
<td style="text-align: right;"><p>###</p>
<p>Philly Bikes</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image110.png" style="width:4.77698in;height:1.23621in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select your customer via double-click.</td>
<td style="text-align: right;">US00</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image111.png" style="width:4.99953in;height:1.15446in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Debit</em> area you can see the two open receivables from your customer <em>Philly Bikes</em>. In the <em>Credit</em> area you can see the payment received for $3,500. Assign your second customer invoice to the payment. To do this, select the second row under <em>Debit</em> and the only row under <em>Credit</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image112.png" style="width:5.15764in;height:0.64931in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image113.png" style="width:1.03543in;height:0.19685in" />. In the <em>Assigned items</em> section, you can check the new assignment.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image114.png" style="width:5.15764in;height:0.65486in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>You can see that the new assignment is saved but unconfirmed. To confirm the assignment, click on <img src="media/image115.png" style="width:0.47225in;height:0.18751in" />.</p>
<p>You can see from the status that your new allocation has now been confirmed. You can now reconcile the two items. To do this, select your assigned items again and click on <img src="media/image116.png" style="width:0.31496in;height:0.17717in" />.</p>
<p><img src="media/image117.png" style="width:4.53092in;height:1.22561in" /></p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Use <img src="media/image24.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori Launchpad. Confirm any browser warning messages with <strong>Ok</strong>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Substep 5</strong> Go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, open the <em>Display Customer Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image118.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Display Customer Balances</em> screen, search for your customer <strong>Philly Bikes</strong>. Also, enter your <em>Company Code</em> <strong>US00</strong> and as your <em>Fiscal Year</em> the <strong>current year</strong>. Choose <img src="media/image4.png" style="width:0.19685in;height:0.17717in" /> and then click on your <em>debit</em> in the <em>current period</em>.</td>
<td style="text-align: right;"><p>Philly Bikes</p>
<p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image119.png" style="width:4.85694in;height:0.51401in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can see from the overview that the payment and the clearing document are now assigned to the correct invoice.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-8-scenario-3-reset-and-revers-incoming-payment">Step 8: Scenario 3 – Reset and Revers Incoming Payment</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Cancel and withdraw the payment.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to take back the incorrectly registered payment receipt as well as the assignment to your customer Windy City Bikes.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You have mistakenly assigned and posted an incoming payment to the wrong customer. You must therefore reverse the incoming payment completely.</td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Substep 1 To display customer balances, go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, open the <em>Display Customer Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image120.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Display Customer Balances</em> screen, search for your <em>customer</em> <strong>Windy City Bikes</strong>. Also, enter your <em>Company Code</em> <strong>US00</strong> and as your <em>Fiscal Year</em> the <strong>current year</strong>. Click <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>Windy City Bikes</p>
<p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image121.png" style="width:5.15764in;height:2.97917in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on your <em>Credit</em> in the <em>current period</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image122.png" style="width:5.03746in;height:0.50531in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p>Identify the incorrect journal entry and note its number:</p>
<p>_________________________</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Substep 2</strong> Please go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, open the <em>Balance Sheet/Income Statement</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image123.png" style="width:1.59449in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For <em>Company Code</em> enter <strong>US00</strong>, for <em>Ledger</em> choose <strong>0L</strong>, and as <em>Statement Version</em> enter <strong>G###</strong>. Make sure that you select the <strong>period</strong> in which you made the posting from the previous step as the <strong>end and</strong> <strong>comparison end</strong> <strong>period</strong>. Select <img src="media/image4.png" style="width:0.19685in;height:0.17717in" /> and use <img src="media/image83.png" style="width:0.23259in;height:0.18898in" /> to expand the tree path in the <em>All Accounts</em> tab.</td>
<td style="text-align: right;"><p>US00<br />
0L</p>
<p>G###<br />
period</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image124.png" style="width:5.15764in;height:1.62569in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Pay attention to the Trade receivables. After the cancellation, the period balance should increase due to the receivable then being open again.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Substep 3</strong> Go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, use the <em>Reset Cleared Items</em> app to undo the assignment of the payment.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image125.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Reset Cleared Items</em> screen, enter your <strong>Windy Bikes clearing entry</strong> (Step 4), as <em>Company Code</em> <strong>US00</strong> and as <em>Clearing Fiscal Year</em> the <strong>current year</strong>. Click on <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>Windy Bikes<br />
clearing entry</p>
<p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image126.png" style="width:5.15764in;height:1.82639in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">At the end of the line, click on <img src="media/image10.png" style="height:0.1354in" /> to open the details. You now have two options:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><ul>
<li><p><em>Reset</em> The assignment of the payment to the open item is reset.</p></li>
<li><p><em>Reset and Reverse</em> The assignment of the payment to the open item is reset and the incoming payment is cancelled.</p></li>
</ul></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image127.png" style="width:4.26185in;height:3.55546in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image128.png" style="width:0.95942in;height:0.18898in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the <em>Reverse Journal Entries</em> pop-up, check if the <em>Reversal Reason</em> is set to <strong>Reversal in current period.</strong> Also select the <strong>posting date</strong> and the <strong>period</strong> from step 4 and click <img src="media/image129.png" style="width:0.46517in;height:0.18898in" />.</td>
<td style="text-align: right;"><p>Reversal in current period</p>
<p>Posting Data</p>
<p>Period</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image130.png" style="width:3.91202in;height:1.17966in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image68.png" style="width:0.43307in;height:0.17717in" /> to confirm the message and click on <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Substep 4</strong> To view the impact of the reversal, please go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, open the <em>Display Customer Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image120.png" style="width:1.59055in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Display Customer Balances</em> screen, search for your customer <strong>Windy City Bikes</strong>. Also, enter your <em>Company Code</em> <strong>US00</strong> and as your <em>Fiscal Year</em> the <strong>current year</strong>. Click <img src="media/image4.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>Windy City Bikes</p>
<p>US00</p>
<p>current year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image131.png" style="width:5.15764in;height:3.00278in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on your <em>Debit</em> in the <em>current period</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image132.png" style="width:5.15764in;height:0.71528in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Substep 5</strong> Go to the <em>Financial Accounting</em> space and choose the <em>Accounts Receivable</em> page. In the <em>Head of Accounting</em> section, use the <em>Balance Sheet/Income Statement</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image133.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For <em>Company Code</em> enter <strong>US00</strong>, for <em>Ledger</em> choose <strong>0L</strong>, and as <em>Statement Version</em> enter <strong>G###</strong>. Make sure that you select the <strong>period</strong> in which you made the posting from the previous step as the <strong>end and</strong> <strong>comparison end</strong> <strong>period</strong>. Select <img src="media/image4.png" style="width:0.19685in;height:0.17717in" /> and use <img src="media/image83.png" style="width:0.23259in;height:0.18898in" /> to expand the tree path in the <em>All Accounts</em> tab.</td>
<td style="text-align: right;"><p>US00<br />
0L</p>
<p>G###<br />
period</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image134.png" style="width:5.15764in;height:1.14444in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Look at the period balance of trade receivables. You can see that the balance has increased because after the cancellation the receivable is open again.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image24.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>
