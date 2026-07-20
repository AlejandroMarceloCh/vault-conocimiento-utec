---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_FI-AP_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_FI-AP_en_v4.3.docx
---

Financial Accounting –

Accounts Payable (FI-AP)

This case study describes an integrated external accounting process and thus promotes an understanding of the individual process steps and the underlying SAP functionality.

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
<p>Accounts Payable</p>
<p>Authors</p>
<p>Michael Boldau</p>
<p>Stefan Weidner</p>
<p>Version</p>
<p>4.3</p>
<p>Last Update</p>
<p>July 2025</p></th>
<th><p>MOTIVATION</p>
<p>Data entry during the FI exercises was reduced because much of the data was already available in the SAP system. Static data, also referred to as master data, simplifies the handling of operational processes. Examples include vendor data and any type of G/L account.</p>
<p>In this case study, you create a vendor master record, enter the following vendor invoice, and initiate its payment.</p></th>
<th></th>
<th><p>PREREQUISITES</p>
<p>Before you work on the case study, you should familiarize yourself with navigation in the SAP system.</p>
<p>To carry out this FI case study successfully, it is not necessary to have worked through the FI exercises or other case studies. However, it is recommended.</p>
<p>NOTES</p>
<p>This case study uses the model company Global Bike, which was developed exclusively for SAP UA Curricula.</p>
<p><img src="media/image2.png" style="width:1.68893in;height:0.62765in" alt="M:\Curricula\Vorlagen\Logo_Global Bike\Global_Bike_Logo_neu_2018\Logo1.png" /></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<img src="media/image3.png" style="width:1.36042in;height:0.73264in" alt="M:\Dokumente\UCC_Partner\Logos\SAP UA Logo\SAP_University_Alliances_Logo_2013_Februar\RGB\SAP_UniversityAlliances_scrn_R_pos_stac3.png" />

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
<th colspan="2"><p><strong>Learning Objective</strong> Understand and execute an external accounting process in Accounts Payable (AP).</p>
<p><strong>Scenario</strong> To handle an external accounting process, you will take on various roles within Global Bike. Thereby you will work in the Financial Accounting (FI) department and there in the supplier accounting.</p>
<p><strong>Employees involved</strong> Silvia Cassano (AP Accountant)</p>
<p>Shuyuan Chen (Head of Accounting)</p></th>
<th style="text-align: right;"><strong>Time</strong> 100 Min.</th>
</tr>
<tr>
<th colspan="3"></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;">Before you post a vendor invoice, all necessary master data has to be maintained. Within this case study, you will first create the required G/L accounts as well as a new supplier (called vendor in Financial Accounting). Afterwards you will post the invoice and verify the changes on your G/L accounts. Since the posting affects the income statement, you will finally look at the effect on the balance sheet.</th>
</tr>
<tr>
<th colspan="3" style="text-align: center;"><img src="media/image4.png" style="width:6.54306in;height:3.75972in" /></th>
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
<p><a href="#step-1-create-bank-account-in-general-ledger">Step 1: Create Bank Account in General Ledger <span>4</span></a></p>
<p><a href="#step-2-create-reconciliation-account-in-general-ledger">Step 2: Create Reconciliation Account in General Ledger <span>7</span></a></p>
<p><a href="#step-3-create-expense-account-in-general-ledger">Step 3: Create Expense Account in General Ledger <span>9</span></a></p>
<p><a href="#step-4-create-vendor-master-record-for-landlord">Step 4: Create Vendor Master Record for Landlord <span>11</span></a></p>
<p><a href="#step-5-post-transfer-of-funds-to-alternate-bank-account">Step 5: Post Transfer of Funds to Alternate Bank Account <span>14</span></a></p>
<p><a href="#step-6-review-transfer-of-funds">Step 6: Review Transfer of Funds <span>16</span></a></p>
<p><a href="#step-7-create-invoice-receipt-for-rent-expense">Step 7: Create Invoice Receipt for Rent Expense <span>18</span></a></p>
<p><a href="#step-8-display-and-review-gl-account-balances-and-individual-line-items">Step 8: Display and Review G/L Account Balances and Individual Line Items <span>21</span></a></p>
<p><a href="#step-9-display-and-review-ap-balances-and-individual-line-items">Step 9: Display and Review AP Balances and Individual Line Items <span>23</span></a></p>
<p><a href="#step-10-post-payment-to-landlord">Step 10: Post Payment to Landlord <span>25</span></a></p>
<p><a href="#step-11-display-and-review-ap-balances-and-individual-line-items">Step 11: Display and Review AP Balances and Individual Line Items <span>27</span></a></p>
<p><a href="#step-12-run-financial-statement">Step 12: Run Financial Statement <span>30</span></a></p>
<p><a href="#fi-ap-challenge">FI-AP Challenge <span>32</span></a></p></th>
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
<th colspan="2"><h1 id="step-1-create-bank-account-in-general-ledger">Step 1: Create Bank Account in General Ledger</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a new G/L Account.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create a new Bank Account in the General Ledger.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In this case study, you create master data that will be used, for example, in accounts payable operational processes and to settle monthly rental expenses. The first thing to do is to create a bank account for outgoing payments to vendors.</td>
<td style="text-align: right;">Scenario</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please go to the <em>Financial Accounting</em> space and choose the <em>Accounts Payable</em> page. In the <em>Head of Accounting</em> section, you can use the <em>Manage G/L Account Master Data</em> app to create a new G/L account.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image5.png" style="width:1.59449in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image6.png" style="width:0.35419in;height:0.12501in" /> to add a new account.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image7.png" style="width:4.96234in;height:1.50212in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>G/L Account Master Data</em> screen, in the <em>G/L Account</em> field, enter <strong>180###5</strong>. Remember to insert for ### your three-digit number given to you by your instructor. For example, if your individual number is 013, enter 1800135.</td>
<td style="text-align: right;">180###5</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Chart of Accounts</em> field, select the value help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> and select from the list of results the <strong>GL00</strong> (<em>Global Bike Group</em>) entry. As <em>G/L Account Type</em>, select <strong>Balance Sheet Account</strong> from the drop-down.</td>
<td style="text-align: right;"><p>GL00</p>
<p>Balance Sheet Account</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Account Group</em> field, click the value help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> again. In the <em>Select: Account Group</em> window that now opens, the chart of accounts <em>GL00</em> should already have been automatically transferred. Then select the entry <strong>01</strong> (<em>Current Asset Accounts</em>) from the results list by clicking on it.</td>
<td style="text-align: right;">01</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image9.png" style="width:4.7842in;height:1.17921in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As <em>Short Text</em> enter <strong>Bank ###</strong>, and as <em>G/L Account Long Text</em>, please enter <strong>Bank Account ###</strong>. Replace ### again with your number. Compare your entries with the following screenshot. Afterward, go to the <img src="media/image10.png" style="width:1.05827in;height:0.18898in" /> area.</td>
<td style="text-align: right;"><p>Bank ###</p>
<p>Bank Account ###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image11.png" style="width:5.02548in;height:2.69133in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Next, you assign the new G/L account to a company code. Therefore, in the <em>Company Code Data</em> area, please select <img src="media/image6.png" style="width:0.35419in;height:0.12501in" />.</td>
<td style="text-align: right;">Company Code Data</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Company Code Assignment</em> window that opens, select the value help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> in the <em>New Company Code Assignment</em> field. The <em>Chart of Accounts</em> and <em>G/L Account</em> fields should already be filled with <strong>GL00</strong> and your new account <strong>180###5</strong>.</td>
<td style="text-align: right;"><p>GL00</p>
<p>180###5</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image12.png" style="width:5.02344in;height:1.58191in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">From the result list, choose the entry <strong>US00</strong>. Your selection will automatically add <strong>USD</strong> as the <em>Account Currency</em>. Now, select the checkbox <strong>Only Balance in Local Currency</strong>.</td>
<td style="text-align: right;"><p>US00</p>
<p>USD</p>
<p>Only Balance in Local Currency</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Account Management</em> area. In the Sort Key field, select <strong>001</strong> (<em>Posting date</em>).</td>
<td style="text-align: right;">001</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>CREATE/BANK/INTEREST</em> area, find and select the <em>Field Status Group</em> <strong>ZGBS</strong> (<em>General Balance Sheet Accounts</em>), and select the <strong>Relevant to Cash Flow</strong> checkbox.</td>
<td style="text-align: right;"><p>ZGBS</p>
<p>Relevant to Cash Flow</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image13.png" style="width:4.83186in;height:2.49033in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">First, confirm with <img src="media/image14.png" style="width:0.22047in;height:0.17717in" /> and then click on <img src="media/image15.png" style="width:0.29921in;height:0.17717in" />. You will receive the following message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image16.png" style="width:2.20806in;height:0.68741in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"></td>
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
<th colspan="2"><h1 id="step-2-create-reconciliation-account-in-general-ledger">Step 2: Create Reconciliation Account in General Ledger</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a new G/L account.</p>
<p><strong>Short Description</strong> Create a new Reconciliation Account in the General Ledger.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><em>Reconciliation Accounts</em> connect the General Ledger with sub ledgers, which are maintained for debtors (customers) and vendors (suppliers), for example. It should be noted that reconciliation accounts cannot be posted to directly. Later, you will create a new vendor master record and assign the new reconciliation account to it.</td>
<td style="text-align: right;">Reconciliation Account</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a new reconciliation account, please go to the space <em>Financial Accounting</em> and choose the page <em>Accounts Payable</em>. In the <em>Head of Accounting</em> section, open the app <em>Manage G/L Account Master Data</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:1.5315in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Again, click on <img src="media/image6.png" style="width:0.35419in;height:0.12501in" /> to add a new account. On the following screen, in the G/L Account field, enter <strong>330###5</strong> (replace ### with your number).</td>
<td style="text-align: right;">330###5</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Chart of Accounts</em> field, select the value help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> and select from the list of results the entry <strong>GL00</strong> (<em>Global Bike Group</em>). As <em>G/L Account Type</em>, select <strong>Balance Sheet Account</strong> from the drop-down.</td>
<td style="text-align: right;"><p>GL00</p>
<p>Balance Sheet Account</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Account Group</em> field, click the value help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> again. In the <em>Select: Account Group</em> window that opens, the chart of accounts <em>GL00</em> should already have been automatically transferred. Then select the entry <strong>03</strong> (<em>Outside Capital Accounts</em>) from the results list by clicking on it.</td>
<td style="text-align: right;">03</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As <em>Short Text</em> enter <strong>Payables-Misc ###</strong>, and as <em>G/L Account Long Text</em>, please enter <strong>Payables-Miscellaneous ###</strong>. Replace ### again with your number. Compare your entries with the following screenshot. Afterward, go to the <img src="media/image10.png" style="width:1.05827in;height:0.18898in" /> area.</td>
<td style="text-align: right;"><p>Payables-Misc ###</p>
<p>Payables-Miscellaneous ###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image19.png" style="width:4.90951in;height:2.43544in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Next, you assign the new G/L account to a company code. Therefore, in the <em>Company Code Data</em> area, please select <img src="media/image6.png" style="width:0.35419in;height:0.12501in" />.</td>
<td style="text-align: right;">Company Code Data</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the following screen, in the <em>New Company Code Assignment</em> field select the input help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" />. A pop up screen will open. The <em>Chart of Accounts</em> and <em>G/L Account</em> fields should already be filled with <strong>GL00</strong> and your new account <strong>330###5</strong>.</td>
<td style="text-align: right;"><p>GL00</p>
<p>330###5</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the results list, select the entry <strong>US00</strong>. You will automatically return to the main window. In the <em>Account Control</em> area, as <em>Account Currency</em> <strong>USD</strong> is already preselected. In the <em>Recon. Account for Account Type</em> dropdown, select <strong>K</strong> (<em>Vendors</em>).</td>
<td style="text-align: right;"><p>US00</p>
<p>USD</p>
<p>K (Vendors)</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Account Management</em> area, as the sort key please select <strong>001</strong> (<em>Posting date</em>). Afterward, please go the <em>CREATE/BANK/INTEREST</em> area. As <em>Field Status Group</em>, please choose <strong>ZRAA</strong> (<em>Reconciliation Accounts</em>).</td>
<td style="text-align: right;"><p>001</p>
<p>ZRAA</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image20.png" style="width:4.41607in;height:2.20352in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Confirm your entries by clicking <img src="media/image14.png" style="width:0.22047in;height:0.17717in" />. A draft will be saved. Afterward, click on <img src="media/image15.png" style="width:0.29921in;height:0.17717in" /> to create the account. You will receive a success message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 66%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="step-3-create-expense-account-in-general-ledger">Step 3: Create Expense Account in General Ledger</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create a new G/L Account.</p>
<p><strong>Short Description</strong> Create a new Expense Account in the General Ledger.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please go to the <em>Financial Accounting</em> space and choose the <em>Accounts Payable</em> page. In the <em>Head of Accounting</em> section, you can use the <em>Manage G/L Account Master Data</em> app to create a new G/L account.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:1.5315in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As in the previous steps, click on <img src="media/image6.png" style="width:0.35419in;height:0.12501in" /> to add a new account. On the following screen, in the <em>G/L Account</em> field, enter <strong>631###5</strong> (replace ### with your number).</td>
<td style="text-align: right;">631###5</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Chart of Accounts</em> field, enter <strong>GL00</strong> (<em>Global Bike Group</em>), and in the <em>G/L Account Type</em> drop-down menu, enter <strong>Primary Cost or Revenue</strong>. As <em>Account Group</em> choose <strong>56</strong> (<em>Operating Expenditure</em>).</td>
<td style="text-align: right;"><p>GL00</p>
<p>Primary Cost or Revenue</p>
<p>56</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For both fields <em>Short Text</em> and <em>G/L Account Long Text</em> please enter <strong>Rent Expenses ###</strong>. Again, remember to replace ### with your number. Compare your entries with the following screenshot. Afterward, go to the <img src="media/image10.png" style="width:1.05827in;height:0.18898in" /> area.</td>
<td style="text-align: right;"><p>Rent Expenses ###</p>
<p>Rent Expenses ###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image21.png" style="width:5.3447in;height:1.31165in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Next, you assign the new G/L account to a company code. Therefore, in the <em>Company Code Data</em> area, please select <img src="media/image6.png" style="width:0.35419in;height:0.12501in" />.</td>
<td style="text-align: right;">Company Code Data</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">A new screen will open. In the <em>New Company Code Assignment</em> field, please use the input help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> to choose <strong>US00</strong> (<em>Global Bike Inc.</em>). Back in the <em>New Company Code Assignment</em> screen, you can see that <strong>USD</strong> has been entered automatically. Please also select the <strong>Posting Without Tax Allowed</strong> checkbox. In the <em>Account Management</em> area, as the <em>Sort Key</em> please choose <strong>001</strong> (<em>Posting date</em>).</td>
<td style="text-align: right;"><p>US00</p>
<p>USD</p>
<p>Posting w/o Tax Allowed</p>
<p>001</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>CREATE/BANK/INTEREST</em> area, in the <em>Field Status Group</em> field find and select <strong>ZEXP</strong> (<em>Expense Accounts</em>). In the lower screen area, you can use the <img src="media/image14.png" style="width:0.22047in;height:0.17717in" /> button to save your entries as draft.</td>
<td style="text-align: right;">ZEXP</td>
</tr>
<tr>
<td colspan="2">Finally, go to the <img src="media/image22.png" style="width:0.93667in;height:0.18898in" />area. In the row containing controlling area <em>NA00</em>, in the <em>Cost Element Category</em> column, use the input help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> to select <strong>01</strong> (<em>Primary costs/cost-reducing revenues</em>).</td>
<td style="text-align: right;">01</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image23.png" style="width:5.04978in;height:1.61677in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please choose <img src="media/image15.png" style="width:0.29921in;height:0.17717in" /> to confirm your entries and to save you G/L account. You will receive a success message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"></td>
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
<th colspan="2"><h1 id="step-4-create-vendor-master-record-for-landlord">Step 4: Create Vendor Master Record for Landlord</h1></th>
</tr>
<tr>
<th colspan="2"><p><strong>Task</strong> Create a new vendor master record.</p>
<p><strong>Short Description</strong> The Chief Financial Officer has requested you create a new vendor account for <em>Cardinal Properties</em>.</p>
<p><strong>Name (Position)</strong> Silvia Cassano (AP Accountant)</p></th>
<th style="text-align: right;"><strong>Time</strong> 10 Min.</th>
</tr>
<tr>
<th colspan="2"></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">A business partner (BP) is an organization (firm, branch office), person, or a group of persons or organizations in which your company has a business interest. You can create and manage your business partners and their roles centrally in a company. For this purpose, you enter the general data of the BP once and assign business partner roles (BP roles) to them. The various roles are created at specific organizational levels, such as company code or sales area. There are exactly three business partner categories.</th>
<th>Business Partner</th>
</tr>
<tr>
<th colspan="2"><ul>
<li><p><em>(Natural) person</em> – is an individual, usually a private person.</p></li>
</ul></th>
<th>Business Partner Categories</th>
</tr>
<tr>
<th colspan="2"><ul>
<li><p><em>Organization</em> – represents units, such as a company (e.g., a legal person), parts of a legal entity (e.g., a department) or an association.</p></li>
</ul></th>
<th></th>
</tr>
<tr>
<th colspan="2"><ul>
<li><p><em>Group</em> – represents a shared living arrangement, a married couple, or an executive board.</p></li>
</ul></th>
<th></th>
</tr>
<tr>
<th colspan="2">A <em>vendor</em> is a business partner to whom liabilities exist for services received. For example, such a service can be a delivery of goods received, a service received, or the transfer of a right.</th>
<th>Vendor</th>
</tr>
<tr>
<th colspan="2"></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">To create a new business partner (vendor), please go to the space <em>Financial Accounting</em> and choose the <em>Accounts Payable</em> page. In the <em>AP Accountant</em> section, please use the app <em>Manage Business Partner</em> <em>Master Data</em>.</th>
<th>Start</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image24.png" style="width:1.51969in;height:1.5748in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">On the <em>Manage Business Partner</em> screen, select the button <img src="media/image6.png" style="width:0.35419in;height:0.12501in" />. A submenu will open. Click <img src="media/image25.png" style="width:0.62992in;height:0.17717in" /> here.</th>
<th>Organization</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image26.png" style="width:2.5401in;height:1.23981in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">On the <em>Create Organization</em> screen, in the field <em>BP Role</em> click on the input help icon <img src="media/image27.png" style="width:0.17706in;height:0.17706in" />. In the pop-up that opens, select the entry <strong>FLVN00 | FI Vendor</strong>.</th>
<th>FLVN00 | FI Vendor</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Back on the <em>Create Organization</em> window, please add the following information. As <em>Organization Title</em> choose <strong>Company</strong>, and as <em>Name 1</em> enter <strong>Cardinal Properties ###</strong>. Further, as <em>Street</em> enter <strong>Pioneer Trail</strong>, and as <em>City</em> enter <strong>Eden Prairie</strong> (with the <em>Postal Code</em> <strong>55347</strong>). In the field <em>Country</em>, please enter <strong>US</strong> (<em>USA</em>), and as <em>Region</em> choose <strong>MN</strong> (<em>Minnesota</em>). Finally, for <em>Language</em> select <strong>English</strong>.</th>
<th><p>Company</p>
<p>Cardinal Properties ###</p>
<p>Pioneer Trail</p>
<p>Eden Prairie, 55347</p>
<p>US, FL</p>
<p>EN</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image28.png" style="width:4.89743in;height:2.68598in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2">Confirm your entries with <img src="media/image14.png" style="width:0.22047in;height:0.17717in" />. The new <em>New Business Partner</em> screen will be generated. In the <em>General Information</em> area, in the field <em>Search Term 1</em> add your three-digit number <strong>###</strong>. You can use this term to easily find your business partner later.</th>
<th>###</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image29.png" style="width:2.51181in;height:1.0487in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Then, go to the <em>Roles</em> area. Auto-scroll will take you to the correct position. You will see a line with the details of the business partner role as well as the validity dates. At the end of the line, click <img src="media/image30.png" style="width:0.11806in;height:0.1389in" /> to maintain further details.</th>
<th>Roles</th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image31.png" style="width:5.05314in;height:0.50977in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Thereupon, a new screen will be generated. Go to the <em>Company Codes</em> area. Since there is no record for the company codes, please select <img src="media/image6.png" style="width:0.35419in;height:0.12501in" />.</th>
<th>Company Codes</th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">In the <em>Company Code</em> field, click the input help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> to find and choose <strong>US00</strong> (<em>Global Bike Inc.</em>). In the <em>Finance</em> area, as the <em>Reconciliation Account</em> enter <strong>330###5</strong> (<em>Payables-Miscellaneous ###</em>). Remember that you created this reconciliation account yourself.</th>
<th><p>US00</p>
<p>330###5</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image32.png" style="width:3.99738in;height:1.14348in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;">Afterward, go to the <em>Payment Data</em> subarea. In the field <em>Payment Terms</em>, please add <strong>0001</strong> (<em>Payable immediately Due net</em>). Additionally, please select the <strong>Check Double Invoice</strong> checkbox.</th>
<th><p>0001</p>
<p>Check Double Invoice</p></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image33.png" style="width:2.04629in;height:2.34973in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2">Select <img src="media/image34.png" style="width:0.33858in;height:0.17717in" /> to save the draft. You can save the customer role by clicking <img src="media/image35.png" style="width:0.34752in;height:0.17717in" /> once again afterwards. Use the <img src="media/image36.png" style="width:0.37008in;height:0.17717in" /> button in the lower screen area to finally save the business partner. The system acknowledges the creation of your business partner (vendor) with a success message.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: left;"><strong>Note</strong> Before you close the app, look at the top left of the window under the name of your new business partner. There you will see the number that the system has automatically assigned for your vendor.</th>
<th></th>
</tr>
<tr>
<th colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:2.14233in;height:0.72102in" /></th>
<th></th>
</tr>
<tr>
<th colspan="2">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</th>
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
<th colspan="2"><h1 id="step-5-post-transfer-of-funds-to-alternate-bank-account">Step 5: Post Transfer of Funds to Alternate Bank Account</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Transfer funds to Alternate Bank Account.</p>
<p><strong>Short Description</strong> Use the SAP SAP Fiori Launchpad to generate a journal entry for the Global Bike Inc. to transfer funds from your current bank account to your alternate bank account.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Please go to the space <em>Financial Accounting</em> and choose the page <em>Accounts Payable</em>. In the <em>Head of Accounting</em> section, use the <em>Post General Journal Entries</em> app to transfer these internal funds.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image38.png" style="width:1.58268in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Journal Entry Date</em> field, use the input help icon <img src="media/image39.png" style="width:0.19794in;height:0.21878in" /> and choose <strong>today’s date</strong>. Then, enter as <em>Company Code</em> <strong>US00</strong>, and as <em>Transaction Currency</em> <strong>USD</strong>. Please change the <em>Period</em> to the <strong>current month</strong>. In the <em>Reference</em> field, enter your three-digit number (###) and as <em>Header Text</em> <strong>Transfer of Funds</strong>.</td>
<td style="text-align: right;"><p>Today’s date</p>
<p>US00</p>
<p>USD</p>
<p>Current month</p>
<p>###</p>
<p>Transfer of Funds</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image40.png" style="width:5.05829in;height:1.08674in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Go to the <em>Line Items</em> area. In the first line, enter <em>Company Code</em> <strong>US00</strong> (<em>Global Bike Inc.</em>) and your <em>G/L Account</em> <strong>180###5</strong> (<em>Bank ###</em>). In the <em>Debit</em> field, enter an amount of <strong>5000</strong> USD.</td>
<td style="text-align: right;"><p>US00</p>
<p>180###5</p>
<p>Debit: 5000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Use the second line to enter <em>Company Code</em> <strong>US00</strong>, <em>G/L Account</em> <strong>1800000</strong> (<em>Bank</em>) and a <em>Credit</em> amount of <strong>5000</strong> USD.</td>
<td style="text-align: right;"><p>US00</p>
<p>1800000</p>
<p>Credit: 5000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:5.16528in;height:0.47431in" /></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Having placed the cursor in the <em>Credit</em> field of the second line, please confirm your entries by pressing Enter. The system will now recalculate the balance of this entry and display it in the upper right corner.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image42.png" style="width:1.80233in;height:0.73969in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">At the bottom right, use the <img src="media/image43.png" style="width:0.48614in;height:0.18751in" /> button to see if the postings are correct. If there is any error, an information window with the error description will appear. Otherwise, you will get a summary of your simulated posting.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> You can see an alphanumeric document number in the top left-hand corner. That means your entries have only been temporarily saved, up to this point. The final posting document is not generated in the system until you post.</td>
<td style="text-align: right;">Provisional posting document number</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image44.png" style="width:3.85808in;height:0.78946in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Finally, click on <img src="media/image45.png" style="width:0.26772in;height:0.17717in" />. The system will now create a unique posting document number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Look again at the top left and see the final number that the SAP system has automatically assigned for this G/L document.</td>
<td style="text-align: right;"><p>Final posting</p>
<p>document number</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image46.png" style="width:4.04918in;height:0.83455in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-6-review-transfer-of-funds">Step 6: Review Transfer of Funds</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display a G/L account document.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to display the G/L account document you have just created.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display a posting document in the SAP system, go to the <em>Financial Accounting</em> space and choose the <em>Accounts Payable</em> page. In the <em>Head of Accounting</em> section, open the <em>Manage Journal Entries – New Version</em> app</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image47.png" style="width:1.55118in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Manage Journal Entries</em> screen, select <em>Company Code</em> <strong>US00</strong>. In the <em>Journal Entry Date</em> field, select the input help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" />. If you performed the previous step (posting funds to alternate bank account) today, select <strong>Today</strong> in the dropdown menu. Otherwise, select another period that best narrows down the date of your posting. Remove the entry from the <em>Fiscal Year</em> field.</td>
<td style="text-align: right;"><p>US00</p>
<p>Today</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image48.png" style="width:5.08288in;height:1.07835in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Then click on <img src="media/image49.png" style="width:0.19685in;height:0.17717in" /> to run the search.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> As you work together with other users in company code <em>US00</em>, it makes sense to sort the results list of posting documents in ascending order by user name. To do this, click on the name of the <em>Journal Entry created by</em> column and select <img src="media/image50.png" style="width:1.13386in;height:0.19685in" />.</td>
<td style="text-align: right;">Sort Ascending</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image51.png" style="width:2.70638in;height:2.27979in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the Journal Entry Number (of your document) to open the context menu. Please choose the <strong>Manage Journal Entries</strong> app.</td>
<td style="text-align: right;"><p>Manage</p>
<p>Journal Entries</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image52.png" style="width:4.29443in;height:1.47805in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see the Journal Entry you created in the previous step. It shows the funds transfer from the main bank account to your new bank account. The document contains information such as the <em>posting date</em>, the <em>posting period</em> and the <em>creator</em> of the posting document.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image53.png" style="width:4.95236in;height:2.61334in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: left;"></td>
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
<th colspan="2"><h1 id="step-7-create-invoice-receipt-for-rent-expense">Step 7: Create Invoice Receipt for Rent Expense</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create an invoice receipt.</p>
<p><strong>Short Description</strong> Enter an invoice received from <em>Cardinal Properties</em> for this month’s rent of $1,500.00. This invoice will be posted to an existing G/L expense account in your chart of accounts and saved as an Accounts Payable to <em>Cardinal Properties</em>.</p>
<p><strong>Name (Position)</strong> Silvia Cassano (AP Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create an invoice receipt, go to the space <em>Financial Accounting</em> and choose the page <em>Accounts Payable</em>. In the <em>AP Accountant</em> section, use the app <em>Create Supplier Invoice</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image54.png" style="width:1.52105in;height:1.52105in" /></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the upcoming screen, enter <em>Company Code</em> <strong>US00</strong> (<em>Global Bike Inc.</em>). In the <em>Invoice Date</em> field, choose <strong>today’s date</strong>, and in the <em>Gross Invoice Amount</em> field, please enter <strong>1500</strong>. The <em>currency</em> <strong>USD</strong> should have already been derived from the company code. Last but not least, the <em>Reference</em> of this invoice should be <strong>### Cardinal 1</strong>. Replace ### again with your three-digit number.</td>
<td style="text-align: right;"><p>US00</p>
<p>Today’s date</p>
<p>1500 USD</p>
<p>### Cardinal 1</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image55.png" style="width:5.09834in;height:2.91787in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Invoicing Party</em> field, select the input help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" />. As <em>Search Term</em> you can use your three-digit number (###). In the large <em>Search</em> field at the top left, enter <strong>Cardinal</strong> and confirm your entries with Enter.</td>
<td style="text-align: right;"><p>###</p>
<p>Cardinal</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the result list, click on the single line to pick the landlord you created earlier. Your vendor number is now entered as <em>Invoicing Party</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image56.png" style="width:4.1985in;height:0.66676in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><blockquote>
<p><strong>Note</strong> All business transactions are posted to G/L accounts. A master record has to be created for each G/L account used. Additionally, a <em>vendor master record</em> has to be created for the vendor subledger account. This contains information that controls the entry of business transactions to the G/L account and the processing of the data.</p>
<p>The following information is used by the system in the master record</p>
</blockquote>
<ul>
<li><p>as default values when posting to the account. For example, the payment terms from the master record are suggested when posting.</p></li>
<li><p>for the processing of business transactions. For example, information on possible payment methods (check, bank transfer) and on the bank details for automatic payment is required.</p></li>
<li><p>for working with the master record. For example, you use authorization groups to restrict access to an account.</p></li>
</ul>
<p>In addition, both the line item display and the management of open items are automatically provided for each vendor account.</p></td>
<td style="text-align: right;">Vendor master record</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Afterward, go to the the <em>G/L Account Items</em> area. Once there, click on <img src="media/image57.png" style="width:0.27938in;height:0.17717in" />. A new line will appear.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Debit/Credit Indicator</em> field select <strong>Debit</strong>. For the <em>G/L Account</em>, enter the expense account you created earlier for rent (<strong>631###5</strong>), and as <em>Amount</em> enter <strong>1500</strong>. At the bottom of the screen choose the <img src="media/image58.png" style="width:0.35433in;height:0.17717in" /> button. As a result, the following error message appears at the bottom left.</td>
<td style="text-align: right;"><p>Debit</p>
<p>631###5</p>
<p>1500</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image59.png" style="width:3.68548in;height:0.6351in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">This means the following: For postings to this expense account, in parallel to external accounting (financial accounting) you need to specify an accounting object for internal accounting (controlling). For this purpose, you can use a cost center.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To do this, first open the detailed data of your G/L Account Item by clicking on the <img src="media/image60.png" style="width:0.80542in;height:0.21429in" /> icon below your new G/L Account line. There, in the <em>Account Assignment</em> area, please enter as <em>Cost Center</em> <strong>NAAD1000</strong> (<em>Admin Costs</em>).</td>
<td style="text-align: right;">NAAD1000</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image61.png" style="width:5.03532in;height:0.60006in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now click on <img src="media/image58.png" style="width:0.35433in;height:0.17717in" /> again. This time the following success message should appear.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image62.png" style="width:2.61495in;height:0.26045in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">By clicking on <img src="media/image43.png" style="width:0.46063in;height:0.17717in" /> you can check if your posting is correct.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image63.png" style="width:4.96853in;height:2.5994in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image45.png" style="width:0.26772in;height:0.17717in" /> to save the invoice receipt. The system confirms the creation with a success message while asking you if you want to create a new supplier invoice.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image64.png" style="width:2.25943in;height:1.41999in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Please choose <img src="media/image65.png" style="width:0.25001in;height:0.18751in" />. In case of not beeing redirected to the SAP Fiori launchpad click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"></td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-8-display-and-review-gl-account-balances-and-individual-line-items">Step 8: Display and Review G/L Account Balances and Individual Line Items</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Display and review general ledger account balances.</p>
<p><strong>Short Description</strong> Display, confirm the activity, and associated balance for the rent expense account used in the previous step.</p>
<p><strong>Name (Position)</strong> Silvia Cassano (AP Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 Min.</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Please go to the <em>Financial Accounting</em> space and choose the <em>Accounts Payable</em> page. In the <em>AP Accountant</em> section, use the <em>Display G/L Account Balances</em> app to display the expense balance.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image66.png" style="width:1.47786in;height:1.4864in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>G/L Account Balances</em> screen, enter as <em>Ledger</em> <strong>0L</strong> (<em>Leading Ledger</em>), as <em>Company Code</em> <strong>US00</strong>, and as <em>G/L Account</em> <strong>631###5</strong>. Furthermore, make sure that the <em>Ledger Fiscal Year</em> is the <strong>current year</strong> and that the <em>Controlling Area</em> is <strong>NA00</strong>. Compare your entries with the following screenshot and press <img src="media/image49.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: left;"><p>0L</p>
<p>US00</p>
<p>631###5</p>
<p>Current year</p>
<p>NA00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image67.png" style="width:5.26401in;height:0.79028in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will receive a total list of balances for all periods for the current fiscal year.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image68.png" style="width:5.16984in;height:1.45099in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the <em>Debit</em> amount in the current month to view the line items. You will see your previously created journal entry of the vendor invoice.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image69.png" style="width:5.19685in;height:0.65573in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-9-display-and-review-ap-balances-and-individual-line-items">Step 9: Display and Review AP Balances and Individual Line Items</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display and review Accounts Payable balances and individual line items.</p>
<p><strong>Short Description</strong> Display and confirm the activity and associated balance for the Accounts Payable for <em>Cardinal Properties</em>. Note that this transaction is considered to be “open” which means that payment has not been sent to <em>Cardinal Properties</em> as of this time.</p>
<p><strong>Name (Position)</strong> Silvia Cassano (AP Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To view the AP balances, go to the space <em>Financial Accounting</em> and choose the page <em>Accounts Payable</em>. In the <em>AP Accountant</em> section, use the <em>Display Supplier Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image70.png" style="width:1.56299in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Supplier</em> field, click the input help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> to find your vendor’s number. In the <em>Search Term</em> field, enter your three-digit number (<strong>###</strong>) and press <img src="media/image49.png" style="width:0.19685in;height:0.17717in" />.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As a result, you will get the list of all suppliers assigned to you in Germany and in the USA. Scroll down until you find <em>Cardinal Properties</em>. Select the entry by clicking the checkbox at the beginning of the line and confirm it by clicking on <img src="media/image14.png" style="width:0.22047in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image71.png" style="width:4.71299in;height:3.11369in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Back in the <em>Display Supplier Balances</em> screen, select the <em>Company Code</em> <strong>US00</strong> and choose as <em>Fiscal Year</em> the <strong>current year</strong>. Then press <img src="media/image72.png" style="width:0.45272in;height:0.21591in" /> to display the balances.</td>
<td style="text-align: right;"><p>US00</p>
<p>Current year</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image73.png" style="width:5.00395in;height:2.1555in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the <em>Credit</em> amount in the current month to generate a list with all items. As you can see, your journal entry has the clearing status (<em>Open</em>), which means that the invoice has not been paid yet.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image74.png" style="width:5.10475in;height:0.37061in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-10-post-payment-to-landlord">Step 10: Post Payment to Landlord</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Issue a payment to your landlord.</p>
<p><strong>Short Description</strong> Issue a payment to <em>Cardinal Properties</em> to settle the Accounts Payable for this month’s rent. A journal entry is made to Accounts Payable for <em>Cardinal Properties</em> and to the bank checking account in the G/L.</p>
<p><strong>Name (Position)</strong> Silvia Cassano (AP Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post a payment to a vendor, please go to the <em>Financial Accounting</em> space and choose the <em>Accounts Payable</em> page. In the <em>AP Accountant</em> section, use the <em>Post Outgoing Payments</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image75.png" style="width:1.60236in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Post Outgoing Payments</em> screen, enter <em>Company Code</em> <strong>US00</strong>, and select the <strong>current date</strong> as the <em>Posting Date</em> and as the <em>Journal Entry Date</em>. In the <em>Reference</em> field enter <strong>Inv Cardinal ###</strong>, and as <em>Period</em> the <strong>current month</strong>. For the <em>G/L account</em>, enter your created account <strong>180###5</strong>, and for the <em>Amount</em>, enter <strong>1500 USD</strong>. Make sure that <strong>KZ</strong> (<em>Vendor Payment</em>) is selected as the <em>Journal Entry Type</em>. Compare your entries with the following screenshot.</td>
<td style="text-align: right;"><p>US00</p>
<p>Current date</p>
<p>Current date</p>
<p>Inv Cardinal ###</p>
<p>Current month</p>
<p>180###5</p>
<p>1500 USD</p>
<p>KZ</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image76.png" style="width:5.00558in;height:1.39969in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Open Item Selection</em> area, check that as the <em>Account Type</em> <strong>Supplier</strong> is selected. As the <em>Account ID</em> enter your <strong>Vendor/Supplier Number</strong> for <em>Cardinal Properties</em>. If necessary, use the input help as before.</td>
<td style="text-align: right;"><p>Supplier</p>
<p>Vendor Number</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image77.png" style="width:4.61568in;height:0.87324in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image78.png" style="width:0.63371in;height:0.17717in" /> to generate the open items list. There should be only one result line.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image79.png" style="width:5.13479in;height:0.4621in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">At the end of the line, select <img src="media/image80.png" style="width:0.8722in;height:0.17717in" />. You will see the balance in the upper right corner <img src="media/image81.png" style="width:0.90709in;height:0.17717in" />. Compare your entries in the <em>Items to Be Cleared</em> area with the following screenshot.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image82.png" style="width:4.90251in;height:0.7979in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the lower screen area, click on <img src="media/image45.png" style="width:0.26772in;height:0.17717in" />. You will get a success message. On that pop-up message, select the <img src="media/image83.png" style="width:0.48in;height:0.20364in" /> button.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image84.png" style="width:4.99602in;height:2.67076in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38428in;height:0.17656in" /> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-11-display-and-review-ap-balances-and-individual-line-items">Step 11: Display and Review AP Balances and Individual Line Items</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display and review Accounts Payable balances and individual line items.</p>
<p><strong>Short Description</strong> Display the result of the creditor payment for the rental expense and check the balance of the liabilities affected by this payment to Cardinal Properties. Recheck the status of the transaction.</p>
<p><strong>Name (Position)</strong> Silvia Cassano (AP Accountant)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To view the AP balances again, go to the space <em>Financial Accounting</em> and choose the page <em>Accounts Payable</em>. In the <em>AP Accountant</em> section, open the <em>Display Supplier Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image70.png" style="width:1.56299in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Supplier</em> field, click the input help icon <img src="media/image8.png" style="width:0.17501in;height:0.17501in" /> to find your vendor’s number. In the <em>Search Term</em> field, enter your three-digit number (<strong>###</strong>) and press <img src="media/image85.png" style="width:0.39764in;height:0.17717in" />.</td>
<td style="text-align: right;">###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As a result, you will get the list of all suppliers assigned to you in Germany and in the USA. Scroll down until you have found <em>Cardinal Properties</em>. Select the entry by clicking the checkbox at the beginning of the line and confirm with <img src="media/image14.png" style="width:0.22047in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Back in the <em>Display Supplier Balances</em> screen, select the <em>Company Code</em> <strong>US00</strong> and choose as <em>Fiscal Year</em> the <strong>current year</strong>. Then press <img src="media/image49.png" style="width:0.19685in;height:0.17717in" /> to display the balances.</td>
<td style="text-align: right;"><p>US00</p>
<p>Current year</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image86.png" style="width:5.04209in;height:2.14367in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Compared to the situation before, what do you notice concerning the vendor payment? If necessary, look again at the screenshot of the same report two steps ago.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the current month line, click on the amount in the <em>Debit</em> column. You will now get a result list with the detail data of your journal entry, which you can recognize by the journaly entry type <em>KZ</em> (KZ = vendor payment).</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image87.png" style="width:5.39503in;height:0.25318in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">First, click on the number of your journal entry. In the context menu that opens use the <img src="media/image88.png" style="width:0.56557in;height:0.17717in" /> button to find and add the <em>Manage Journal Entry</em> app. Afterward, open the app.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image89.png" style="width:3.53041in;height:1.13754in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Now you will see the complete journal entry.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image90.png" style="width:4.84105in;height:2.53562in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">At the top left, click on <img src="media/image91.png" style="width:0.19685in;height:0.19685in" /> twice to close the detailed data of the journal entry and to leave debit entry as well. Back in the <em>Display Supplier Balances</em> screen, click on the amount in the current month’s <em>Credit</em> column.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image92.png" style="width:4.87988in;height:1.8883in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If you remember, you were looking at the exact credit entry before you post the vendor payment. What has changed? If necessary, look at the corresponding screenshot from a few steps ago.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="step-12-run-financial-statement">Step 12: Run Financial Statement</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Look at the financial statement.</p>
<p><strong>Short Description</strong> Run a trial financial statement.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">A <em>balance sheet</em> and a <em>profit &amp; loss statement</em> show all G/L accounts in a structure previously defined in the balance sheet/P&amp;L structure. With the help of filters, you can focus your analysis on specific segments or profit centers.</td>
<td style="text-align: right;"><p>Balance sheet</p>
<p>Profit and loss statement</p></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display a balance sheet/P&amp;L, go to the <em>Financial Accounting</em> space and choose the <em>Accounts Payable</em> page. In the <em>Head of Accounting</em> section, open the <em>Balance Sheet/Income Statement</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image93.png" style="width:1.58771in;height:1.60606in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Balance Sheet/Income Statement</em> view, enter as <em>Company Code</em> <strong>US00</strong> and as <em>Statement Version</em> <strong>G###</strong>. The currency is automatically determined based on the selected company code. Leave the other pre-filled fields as they are.</td>
<td style="text-align: right;"><p>US00</p>
<p>G###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image94.png" style="width:4.98987in;height:0.94425in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image49.png" style="width:0.19685in;height:0.17717in" />. You can see the period balances at the top hierarchy level.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image95.png" style="width:4.91595in;height:1.01729in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> Your screen or numbers may differ from the screenshot. These depend on the number of tasks and case studies completed in the client before.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In front of <em>Assets</em>, click <img src="media/image96.png" style="width:0.10418in;height:0.14585in" /> to expand the folder. Do the same with the folder <em>1 Current Assets</em>. You should now also see your G/L account <em>180###5</em> (<em>bank account ###</em>) in the Current Assets Category list.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image97.png" style="width:4.89751in;height:1.4253in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Can you explain the balance of $3,500?</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the <em>Period Balance</em> amount of your bank account. On the pop-up menu please choose the <strong>Display G/L Balances</strong> app.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image98.png" style="width:5.06294in;height:0.75001in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Analyze the posted line items of this G/L account.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image99.png" style="width:5.07181in;height:0.38642in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image17.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"></td>
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
<th colspan="2"><h1 id="fi-ap-challenge">FI-AP Challenge</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><strong>Learning Objective</strong> Perform an accounts payable process in Germany.</td>
<td style="text-align: right;"><strong>Time</strong> 60 Min.</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p><strong>Motivation</strong> After you have successfully completed the Financial Accounting - Accounts Payable case study, you should be able to solve the following task independently.</p>
<p><strong>Scenario</strong> Global Bike Germany GmbH has received an accounts payable invoice from its tool supplier Burgmeister Zubehör OHG. To do this, you must first create all the relevant master data. Then create the invoice for €3000 from Burgmeister Zubehör OHG and post the vendor payment. Take a look at the effects in the balance sheet and the income statement.</p>
<p>In company code DE00, use 180###6 as the number for the bank account, 330###6 for the reconciliation account and 631###6 for the expense account.</p>
<p><strong>Task Information</strong> As this task is based on the Financial Accounting - Accounts Payable case study, you can use it as a guide. However, it is recommended that you complete this advanced task without help in order to put your acquired knowledge to the test. Pay particular attention to creating all the necessary accounts.</p></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
<tr>
<td colspan="3"></td>
</tr>
</tbody>
</table>
