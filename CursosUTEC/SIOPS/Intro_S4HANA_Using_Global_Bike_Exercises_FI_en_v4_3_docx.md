---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Exercises_FI_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Exercises_FI_en_v4.3.docx
---

<img src="media/image1.png" style="width:1.3622in;height:0.73228in" alt="M:\Dokumente\UCC_Partner\Logos\SAP UA Logo\SAP_University_Alliances_Logo_2013_Februar\RGB\SAP_UniversityAlliances_scrn_R_pos_stac3.png" />

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 67%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="2"><h1 id="fi-1-display-chart-of-accounts-and-general-ledger-account">FI 1: Display Chart of Accounts and General Ledger Account</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Exercise</strong> Familiarize yourself with charts of accounts and G/L accounts.</p>
<p><strong>Task</strong> Use the SAP Fiori launchpad to list G/L accounts assigned to the Global Bike chart of accounts. For each G/L account, the chart of accounts records the account name, account number and additional technical information. Companies often have several bank accounts (e.g. for payroll, general payments and money market) listed in their balance sheet.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>A <em>Chart of Accounts</em> can be shared by different company codes. Each company code must be assigned to a chart of accounts. Once a chart of accounts has been assigned to a company code, it becomes the operational chart of accounts for that company code and contains all relevant information for Financial Accounting (FI) and Controlling (CO).</p>
<p>The following additional charts of accounts are possible if further information is to be entered for international business transactions:</p>
<ul>
<li><p><em>Country-specific chart of accounts</em> – This is structured according to the legal requirements of a specific country.</p></li>
<li><p><em>Group chart of accounts</em> – This is structured in accordance with the requirements for consolidated financial statements.</p></li>
</ul></td>
<td style="text-align: right;">Chart of Accounts</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display G/L accounts, please go to the <em>Financial Accounting</em> space and choose the page <em>Accounts Payable</em>. In <em>Head of Accounting</em> section, open the <em>Manage G/L Account Master Data</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image2.png" style="width:1.56693in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Manage G/L Account Master Data</em> screen, in the <em>Chart of Accounts</em> field click the input help icon <img src="media/image3.png" style="width:0.17717in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image4.png" style="width:4.99235in;height:0.66985in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the popup that opens, you get an overview of all existing charts of accounts. Here you can see various examples of country-specific charts of accounts structured for the respective country.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image5.png" style="width:3.70959in;height:3.05924in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the search box at the top left, enter <strong>GL00</strong> and press <img src="media/image6.png" style="width:0.24016in;height:0.17717in" /> to run the search.</td>
<td style="text-align: right;">GL00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image7.png" style="width:5.16528in;height:1.22153in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the chart of accounts <em>Global Bike Group</em> and confirm with <img src="media/image8.png" style="width:0.24803in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>View</em> field, make sure that <strong>Chart of Accounts View</strong> is selected. If this is not the case, select this entry in the dropdown. Press <img src="media/image6.png" style="width:0.24016in;height:0.17717in" /> to display all G/L accounts assigned to chart of accounts <em>GL00</em>.</td>
<td style="text-align: right;">Chart of Accounts View</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image9.png" style="width:5.10965in;height:2.3295in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will get an impression of how many different G/L accounts exist and what they are used for. Examples are <em>SW procurement</em>, <em>Passenger cars</em> as well as <em>Raw materials</em>. Due to the amount of accounts, you can filter the view as needed. To do this, in the header area in the <em>G/L Account</em> field click the input help icon<img src="media/image3.png" style="width:0.17501in;height:0.17501in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>G/L Account</em> pop-up, select the <em>Define Conditions</em> tab. For the first condition, as the criterion select <strong>contains</strong> and as the value enter <strong>1100000</strong>.</td>
<td style="text-align: right;"><p>Define Conditions contains</p>
<p>1100000</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image10.png" style="width:5.04245in;height:0.90775in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image11.png" /> to specify additional conditions. Repeat this process and record the following conditions:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><table style="width:71%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 45%" />
</colgroup>
<tbody>
<tr>
<td><strong>Criterion</strong></td>
<td><strong>Value</strong></td>
</tr>
<tr>
<td>contains</td>
<td>1800000</td>
</tr>
<tr>
<td>contains</td>
<td>4200000</td>
</tr>
<tr>
<td>contains</td>
<td>7510000</td>
</tr>
<tr>
<td>contains</td>
<td>8000000</td>
</tr>
<tr>
<td>contains</td>
<td>9100000</td>
</tr>
</tbody>
</table></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image8.png" style="width:0.24803in;height:0.17717in" /> to accept your entries and then <img src="media/image6.png" style="width:0.25439in;height:0.18898in" /> to run the search with the new search criteria.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter the short texts and the types of all selected G/L accounts in the table below.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><table style="width:71%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 28%" />
<col style="width: 23%" />
</colgroup>
<tbody>
<tr>
<td><strong>G/L Account</strong></td>
<td><strong>Short Text</strong></td>
<td><strong>G/L Account Type</strong></td>
</tr>
<tr>
<td>1100000</td>
<td> </td>
<td></td>
</tr>
<tr>
<td>1800000</td>
<td> </td>
<td></td>
</tr>
<tr>
<td>4200000</td>
<td> </td>
<td></td>
</tr>
<tr>
<td>7510000</td>
<td></td>
<td></td>
</tr>
<tr>
<td>8000000</td>
<td></td>
<td></td>
</tr>
<tr>
<td>9100000</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">At the end of the line of G/L account <em>1100000</em>, click the icon <img src="media/image12.png" style="width:0.23304in;height:0.18934in" /> for more details.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image13.png" style="width:4.63292in;height:2.17464in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p>Which G/L account type is the G/L account assigned to?</p>
<p>Which account group is this G/L account assigned to?</p>
<p>Which company codes is this G/L account assigned to?</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Note the differences between the German and American company codes!</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image14.png" style="width:0.20134in;height:0.2094in" /> to return to the list of G/L accounts. You are welcome to view other G/L account details if you wish.</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image15.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="fi-2-display-financial-statement">FI 2: Display Financial Statement</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Exercise</strong> Display a financial statement.</p>
<p><strong>Task</strong> Use the SAP Fiori launchpad to display a balance sheet/P&amp;L.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>In SAP, <em>Financial Statement versions</em> are a hierarchical arrangement of G/L accounts.</p>
<p>The structure can be in accordance with the legal requirements for preparing your balance sheet and profit and loss statement. However, it can also be an arbitrary arrangement.</p>
<p>You need a financial statement version for the following functions:</p>
<ul>
<li><p>To create and print financial statements</p></li>
<li><p>To run various reports, such as a structured list of account balances</p></li>
<li><p>As a basis for planning in General Ledger Accounting</p></li>
</ul>
<p>You can define several different financial statement versions. This may be necessary if you want to generate the financial statements using different formats.</p></td>
<td style="text-align: right;">Financial Statement version</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display financial statements, please go to the space <em>Financial Accounting</em> and choose the page <em>Accounts Payable</em>. In the <em>Head of Accounting</em> section, please open the <em>Balance Sheet/Income Statement</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image16.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Balance Sheet/Income Statement</em> screen, in the <em>Company Code</em> field enter <strong>US00</strong> and in the <em>Statement version</em> field <strong>G000</strong>. The currency is automatically selected based on the selected company code. Set the <em>End Period</em> to <strong>08/2023</strong> and the <em>Comparison End Period</em> to <strong>08/2022</strong>.</td>
<td style="text-align: right;"><p>US00</p>
<p>G000</p>
<p>08/2023</p>
<p>08/2022</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image17.png" style="width:5.27382in;height:1.36277in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Now press <img src="media/image6.png" style="width:0.25439in;height:0.18898in" /> to display the corresponding data.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:4.99159in;height:0.9704in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You see the aggregated period balances on top hierarchy level.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Your result/numbers may differ from the screenshot above. These are dependent on the number of tasks and case studies completed in your SAP S/4HANA client to date.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image19.png" style="width:0.2342in;height:0.19029in" /> to fully expand the view. You can now see all G/L accounts posted to and their respective period balances.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image20.png" style="width:5.16528in;height:1.22083in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> You will quickly realize that this balance sheet and income statement do not represent a typical picture of a medium-sized company. This is because this learning environment allows up to 1000 users to perform processes in SAP S/4HANA and because necessary learning situations are prepared many times.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image15.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
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
<th colspan="2"><h1 id="fi-3-check-reconciliation-account">FI 3: Check Reconciliation Account </h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Exercise</strong> Check how reconciliation accounts work.</p>
<p><strong>Task</strong> Use the SAP Fiori launchpad in order to display a posting done to an Account Receivables account. After checking the posting in this subsidiary ledger, review the corresponding posting in the General Ledger.</p>
<p><strong>Name (Position)</strong> Shuyuan Chen (Head of Accounting)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">When you post items to a subsidiary ledger, the SAP system automatically posts the same data to the corresponding G/L account. Each subsidiary ledger has one or more reconciliation accounts in the general ledger. This is necessary so that you can draw up financial statements at any time without having to transfer totals from the subledgers to the general ledger.</td>
<td style="text-align: right;"><p>Reconciliation</p>
<p>Accounts</p></td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Financial Accounting</em> space, choose the page <em>Accounts Receivable</em>. In the <em>Head of Accounting</em> section, open the <em>Display Customer Balances</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image21.png" style="width:1.53543in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Customer</em> field, enter <strong>129997</strong> (<em>Beantown Bikes</em>), as <em>Company Code</em> type in <strong>US00</strong> and as <em>Fiscal Year</em> <strong>2021</strong>. Compare with the screenshot shown below and click <img src="media/image6.png" style="width:0.25439in;height:0.18898in" />.</td>
<td style="text-align: right;"><p>129997</p>
<p>US00</p>
<p>2021</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image22.png" style="width:5.16528in;height:0.57708in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Customer Balances</em> screen, for August 2021 you find one entry in the <em>Debit</em> column and one entry in the <em>Credit</em> column.</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image23.png" style="width:5.16528in;height:1.91042in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the amount in the <em>Debit</em> column. This will take you to the <em>Manage Customer Line Items</em> app. There, all relevant selection criteria have already been entered automatically.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image24.png" style="width:5.16528in;height:1.2875in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will get more information about the posting such as the <em>Journal Entry Date</em>, the <em>Journal Entry</em> (number) and the <em>Journal Entry Type</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image25.png" style="width:5.16528in;height:0.62639in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In in the upper left corner, click <img src="media/image14.png" style="width:0.20134in;height:0.2094in" /> until you get back to the Display <em>Customer Balances</em> screen. Now, select the corresponding credit entry for August (<em>08</em>) by clicking on the amount in the second column.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image26.png" style="width:5.16528in;height:1.28542in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p>What is the journal entry number of this clearing journal entry?</p>
<p>________________________</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Fun Fact</strong> Here comes your extra-curricular German lesson: Using the search engine of your choice, try to find out what journal entry type <strong>DZ</strong> means in English and for which German business term it is an abbreviation?</p>
<p><u>English:</u> = <u>German:</u></p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image15.png" style="width:0.38583in;height:0.17717in" /> to return to the SAP Fiori launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: right;"></td>
<td style="text-align: right;"></td>
</tr>
</tbody>
</table>
