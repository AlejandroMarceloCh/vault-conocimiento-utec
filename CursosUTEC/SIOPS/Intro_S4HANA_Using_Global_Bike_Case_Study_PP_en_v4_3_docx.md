---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_PP_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_PP_en_v4.3.docx
---

Production Planning and Execution (PP)

This case study explains an integrated production planning and execution process in detail and thus fosters a thorough understanding of each process step and underlying SAP functionality.

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
<p>Production Planning and Execution</p>
<p><strong>Authors</strong></p>
<p>Michael Boldau</p>
<p>Bret Wagner</p>
<p>Stefan Weidner</p>
<p>Version</p>
<p>4.3</p>
<p>Last Update</p>
<p>July 2025</p></th>
<th style="text-align: left;"><p>MOTIVATION</p>
<p>The data entry requirements in the production planning exercises (PP 1 through PP 6) were minimized because much of the data already existed in the SAP system. This stored data, known as master data, simplifies the processing of business transactions. Examples for this, are material master data, bills of materials, and routings.</p>
<p>In this case study, we will create consumption values for a finished product to plan and process a complete manufacturing cycle.</p></th>
<th style="text-align: left;"></th>
<th style="text-align: left;"><p>PREREQUISITES</p>
<p>Before you use this case study, you should be familiar with navigation in the SAP system.</p>
<p>In order to successfully work through this case study, it is not necessary to have finished the PP exercises (PP 1 through PP 6). However, it is recommended.</p>
<p>NOTES</p>
<p>This case study uses the Global Bike data set.</p>
<p><img src="media/image1.png" style="width:1.68893in;height:0.62765in" alt="M:\Curricula\Vorlagen\Logo_Global Bike\Global_Bike_Logo_neu_2018\Logo1.png" /></p></th>
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
<col style="width: 0%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="3"><h1 id="process-overview">Process Overview</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Learning Objective</strong> Understand and perform a manufacturing process cycle.</p>
<p><strong>Scenario</strong> In order to experience a complete manufacturing process you will take on different roles within the Global Bike Group, e.g., production supervisor, shop floor worker and plant manager. Overall, you will be working in the Materials Management (MM) and the Production Planning and Execution (PP) departments.</p>
<p><strong>Employees involved</strong> Jun Lee (Production Manager)</p>
<p>Hiro Abe (Plant Manager)</p>
<p>Lars Iseler (Shop Floor Worker 2)</p>
<p>Susanne Castro (Goods Receipt Clerk)</p>
<p>Sanjay Datar (Warehous Employee)</p>
<p>Michael Brauer (Shop Floor Worker 4)</p>
<p>Jamie Shamblin (Controller)</p></td>
<td colspan="2" style="text-align: right;"><strong>Time</strong> 150 min</td>
</tr>
<tr>
<td colspan="3"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p>In the following process, you will plan the production for three products (namely, Deluxe Touring Bikes in black, silver, and red) and complete a production order for the red Deluxe Touring Bikes with the help of the system.</p>
<p>Before you can enter the product demands for your touring bike product group, changes in the material master record of the bikes need to be maintained. Afterwards, you will create planned independent requirements for the next 12 months for this product group and convert a selected planned order into a production order. To conclude the process, the production is confirmed as complete, the finished goods are received into the warehouse and costs assigned to the production order are analyzed.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="3" style="text-align: center;"><img src="media/image2.png" style="width:5.57547in;height:3.90457in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="3"><h1 id="table-of-contents" class="TOC-Heading">Table of Contents</h1>
<p><a href="#process-overview">Process Overview <span>2</span></a></p>
<p><a href="#step-1-change-product-master-record">Step 1: Change Product Master Record <span>4</span></a></p>
<p><a href="#step-2-change-routing">Step 2: Change Routing <span>7</span></a></p>
<p><a href="#step-3-display-product-group">Step 3: Display Product Group <span>10</span></a></p>
<p><a href="#step-4-maintain-planned-independent-requirement">Step 4: Maintain Planned Independent Requirement <span>12</span></a></p>
<p><a href="#step-5-schedule-mrp-runs">Step 5: Schedule MRP Runs <span>15</span></a></p>
<p><a href="#step-6-review-stockrequirements-list">Step 6: Review Stock/Requirements List <span>18</span></a></p>
<p><a href="#step-7-convert-planned-order-into-production-order">Step 7: Convert Planned Order into Production Order <span>21</span></a></p>
<p><a href="#step-8-receive-goods-in-inventory">Step 8: Receive Goods in Inventory <span>23</span></a></p>
<p><a href="#step-9-issue-goods-to-production-order">Step 9: Issue Goods to Production Order <span>26</span></a></p>
<p><a href="#step-10-review-production-order-status">Step 10: Review Production Order Status <span>29</span></a></p>
<p><a href="#step-11-confirm-production-completion">Step 11: Confirm Production Completion <span>33</span></a></p>
<p><a href="#step-12-review-production-order-status">Step 12: Review Production Order Status <span>36</span></a></p>
<p><a href="#step-13-receive-goods-from-production-order">Step 13: Receive Goods from Production Order <span>38</span></a></p>
<p><a href="#step-14-review-costs-assigned-to-production-order">Step 14: Review Costs Assigned to Production Order <span>40</span></a></p>
<p><a href="#step-15-settle-costs-of-production-order">Step 15: Settle Costs of Production Order <span>42</span></a></p>
<p><a href="#pp-challenge">PP Challenge <span>46</span></a></p></td>
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
<th colspan="2"><h1 id="step-1-change-product-master-record">Step 1: Change Product Master Record</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Prepare a product master record for Demand Planning.</p>
<p><strong>Short Description</strong> In order to plan Global Bike’s deluxe touring bikes (black, silver and red) prepare their product master records by adding planning-relevant data to these records.</p>
<p><strong>Name (Position)</strong> Jun Lee (Production Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 20 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To change the views of a material, in the space <em>Production Planning and Execution</em> space and the role of <em>Production Manager</em> use the <em>Manage Product Master Data</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image3.png" style="width:1.66998in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">In the search screen, enter <strong>DXTR*###</strong> (replace ### with your three-digit number) in the search field.</td>
<td style="text-align: right;">DXTR*###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image4.png" style="width:4.82885in;height:1.00318in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image5.png" style="width:0.23538in;height:0.17717in" />. Your various Deluxe Touring Bikes will be displayed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image6.png" style="width:4.91927in;height:1.14619in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click the line of <strong>Deluxe Touring Bike (red)</strong> (DXTR3##) to open the details of the product.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image7.png" style="width:5.01957in;height:1.54717in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image8.png" style="width:0.28701in;height:0.17717in" /> to switch to the edit mode.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Use the pull-down menu <img src="media/image9.png" style="width:0.20079in;height:0.17717in" /> to select the <em>Plants</em> section. The window automatically scrolls to the correct position.</td>
<td style="text-align: right;">Plants</td>
</tr>
<tr>
<td colspan="2"><p><img src="media/image10.png" style="width:1.75984in;height:1.12515in" /></p>
<p>…</p>
<p><img src="media/image11.png" style="width:1.75984in;height:1.06622in" /></p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see a list of all plants for which the product has been defined.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image12.png" style="width:5.09767in;height:2.13185in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image13.png" style="width:0.18398in;height:0.17717in" /> at the end of the line with the DL00 plant to open the plant-specific product master data.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image14.png" style="width:4.88196in;height:2.19065in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Select the <em>MRP Data</em> area. The window automatically scrolls to the correct position. Enter <strong>40</strong> in the <em>Strategy Group</em> field (Planning with final assembly).</td>
<td style="text-align: right;"><p>MRP Data</p>
<p>40</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image15.png" style="width:5.14761in;height:1.19755in" /></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <img src="media/image16.png" style="width:0.38268in;height:0.17717in" /> to save the plant-specific data for plant DL00. Click <img src="media/image17.png" style="width:0.35138in;height:0.17717in" /> to save your changes to the red Deluxe Touring Bike.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">The SAP system updates the master data record for material DXTR3### and displays a corresponding message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:2.17323in;height:0.54534in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <img src="media/image19.png" style="width:0.18898in;height:0.17717in" /> to return to the Manage Product Master Data screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Repeat the same procedure for the silver and black Deluxe Touring Bike. Start with the silver one (<strong>DXTR2###</strong>) and then change the black bike (<strong>DXTR1###</strong>).</td>
<td style="text-align: right;"><p>DXTR2###</p>
<p>DXTR1###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image20.png" style="width:0.35039in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-2-change-routing">Step 2: Change Routing</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Change a routing for a finished good.</p>
<p><strong>Short Description</strong> Change the routing for your red Deluxe Touring bike.</p>
<p><strong>Name (Position)</strong> Jun Lee (Production Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">After the operational steps are laid out, the components must be allocated to the individual operations. This is a progressive process where each operation builds off the materials that entered production in the previous operations.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To change the routing, in the space <em>Production Planning and Execution</em> space and the role of <em>Production Manager</em> use the <em>Manage Routing</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image21.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter the material number of your red Deluxe Touring bike (<strong>DXTR3###).</strong> In the <em>Plant</em> field, enter the Global Bike plant number in Dallas (<strong>DL00</strong>). Then press <img src="media/image22.png" style="width:0.20906in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>DXTR3###</p>
<p>DL00</p></td>
</tr>
<tr>
<td colspan="2">Select the displayed routing and then press<img src="media/image23.png" style="width:0.4252in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image24.png" style="width:4.92445in;height:1.2649in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The operation overview shows you the individual steps involved in manufacturing the product.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image25.png" style="width:5.02578in;height:1.88524in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note</strong> The routing group defines a routing and the routing group counter. Moreover, the routing contains a reference to the material whose production is described by the routing.</p>
<p>Besides the standard sequence, it can also have parallel or alternative sequences. Alongside the standard values, the routing also contains time elements that are relevant for scheduling operations. Each operation in the routing may contain its own base quantity, to which these time elements may refer.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select <img src="media/image26.png" style="width:0.35954in;height:0.17717in" /> to display a list of all components. If this is not displayed, you will find the entry in the pull-down menu under <strong>Menu</strong> <strong>►</strong> <strong>Goto ►</strong> <strong>Allocation</strong>. Select your material and then click <img src="media/image27.png" style="width:0.21335in;height:0.22188in" /> to display a list of all components.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You now want to assign two components (frame and seat) to the process “Attach seat to frame”. Select the rows Touring Frame-Red (<strong>TRFR3##</strong>) and Touring Seat Kit (<strong>TRSK1##</strong>).</td>
<td style="text-align: right;"><p>TRFR3###</p>
<p>TRSK1###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image28.png" style="width:5.18226in;height:1.20949in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image29.png" style="width:0.68898in;height:0.17717in" />. In the popup that appears, enter <strong>0020</strong> for <em>Activity</em> and confirm the entry with <img src="media/image30.png" style="width:0.17717in;height:0.17717in" />.</td>
<td style="text-align: right;">0020</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image31.png" style="width:3.56601in;height:1.61417in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Confirm the entry with <img src="media/image32.png" style="width:0.18898in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Back in the <em>Routing Change: Material Component Overview</em> you can see that both components have now been assigned to <em>Activity</em> <strong>0020</strong>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image33.png" style="width:4.82344in;height:1.41362in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Repeat this process for all other components and assign them to the operations below.</p>
<table style="width:72%;">
<colgroup>
<col style="width: 56%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Component</strong></th>
<th style="text-align: left;"><strong>Operation</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">TRHB1### (touring handlebar)</td>
<td style="text-align: left;">0030</td>
</tr>
<tr>
<td style="text-align: left;">TRWA1### (touring aluminum wheel assembly)</td>
<td style="text-align: left;">0040</td>
</tr>
<tr>
<td style="text-align: left;">DGAM1### (derailleur gear assembly)</td>
<td style="text-align: left;">0040</td>
</tr>
<tr>
<td style="text-align: left;">CHAN1### (chain)</td>
<td style="text-align: left;">0050</td>
</tr>
<tr>
<td style="text-align: left;">BRKT1### (brake kit)</td>
<td style="text-align: left;">0060</td>
</tr>
<tr>
<td style="text-align: left;">PEDL1### (pedal assembly)</td>
<td style="text-align: left;">0070</td>
</tr>
<tr>
<td style="text-align: left;">WDOC1### (warranty document)</td>
<td style="text-align: left;">0100</td>
</tr>
<tr>
<td style="text-align: left;">PCKG1### (packaging)</td>
<td style="text-align: left;">0100</td>
</tr>
</tbody>
</table></td>
<td style="text-align: right;"><p>TRHB1### 0030</p>
<p>TRWA1### 0040</p>
<p>DGAM1### 0040</p>
<p>CHAN1### 0050</p>
<p>BRKT1### 0060</p>
<p>PEDL1### 0070</p>
<p>WDOC1### 0100</p>
<p>PCKG1### 0100</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image34.png" style="width:5.10795in;height:2.12501in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Apply your changes with <img src="media/image17.png" style="width:0.34646in;height:0.19685in" />. The system issues a message that the routing has been saved. Click on <img src="media/image35.png" style="width:0.55856in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image36.png" style="width:0.33465in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-3-display-product-group">Step 3: Display Product Group</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Display a product group.</p>
<p><strong>Short Description</strong> Display the product group (product family) for all your Deluxe Touring bikes.</p>
<p><strong>Name (Position)</strong> Jun Lee (Production Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">A product group (product family) supports high-level planning. This way, it is not necessary to delve into the minutia of creating planning forecasts for every material in the company.</td>
<td style="text-align: right;">Product group</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To view the Deluxe Touring bike product group, in the space <em>Production Planning and Execution</em> space and the role of <em>Production Manager</em> use the <em>Display Product Group</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:1.56638in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Display Product Group: Initial Screen</em>, in the <em>Product group</em> field find and select your group for deluxe touring bikes. In order to do so, press the search icon <img src="media/image38.png" style="width:0.14581in;height:0.15623in" /> (or pressed F4), enter <strong>###*</strong> in the <em>Material description</em> field. Remember to replace ### with your three-digit number, e.g., enter 009* if your number is 009. Enter <strong>DL00</strong> as <em>Plant</em>.</td>
<td style="text-align: right;"><p>###*</p>
<p>DL00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image39.png" style="width:5.05935in;height:1.03534in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, press Enter or click on <img src="media/image40.png" style="width:0.2126in;height:0.19685in" /> to display the search results.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:4.83602in;height:1.90757in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see a list of all your product groups, e.g., for mountain bikes or touring bikes.Select the group of Deluxe Touring Bikes (<strong>PG-DXTR##</strong>). Then click <img src="media/image42.png" style="width:0.23849in;height:0.17717in" /> to apply the selection.</td>
<td style="text-align: right;">PG-DXTR###</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now that the correct <em>Product group</em> (<strong>PG-DXTR###</strong>) is filled in, make sure that <em>Plant</em> <strong>DL00</strong> is entered.</td>
<td style="text-align: right;">DL00</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image43.png" style="width:2.68879in;height:1.57392in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then, press Enter to display the product group details.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On this screen, you can see that this product group defines proportions for three different bikes: the black, silver and red deluxe touring bike. For the black bike, a share of 40% will be considered and 30% for the silver and the red bikes each.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image44.png" style="width:4.87489in;height:1.82335in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image20.png" style="width:0.35039in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<col style="width: 32%" />
<col style="width: 4%" />
<col style="width: 30%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th style="text-align: right;"></th>
<th colspan="4"><h1 id="step-4-maintain-planned-independent-requirement">Step 4: Maintain Planned Independent Requirement</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4"><p><strong>Task</strong> Create a Planned Independent Requirement for a product group.</p>
<p><strong>Short Description</strong> Create a 12<strong>-</strong>month Planned primary requirements for your Deluxe Touring Bike product group.</p>
<p><strong>Name (Position)</strong> Jun Lee (Production Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 min</td>
</tr>
<tr>
<td colspan="4"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">A <strong>planned independent requirement</strong> is a planned requirement notification for a material that is not yet covered by customer orders. It serves as the basis for demand planning in advance planning and consists of a planned quantity at a specific point in time or spread over several periods.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="4"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;"><em>Production Planning and Execution area, in the Production Manager role, use the Maintain Planned Independent Requirements</em> app to create PIRs.</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><img src="media/image45.png" style="width:1.5661in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">When you first open the app, you'll receive a welcome message asking you to select an area of responsibility. Confirm this with <img src="media/image46.png" style="width:0.23262in;height:0.17717in" />, another app, <em>My Area of Responsibility,</em> will appear.</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><img src="media/image47.png" style="width:4.18837in;height:2.42014in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">No plant is currently assigned to you. Select the <em>Dallas plant</em></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><img src="media/image48.png" style="width:4.19385in;height:2.43137in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">The values are saved automatically here. Go to SAP Fiori Launchpad <img src="media/image36.png" style="width:0.33125in;height:0.18194in" />and open the app <em>Maintain planned independent requirements</em> again.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><img src="media/image49.png" style="width:4.57325in;height:1.60212in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">Select all the material and click <img src="media/image50.png" style="width:0.3654in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><img src="media/image51.png" style="width:5.05275in;height:1.42312in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: left;">The screen shown is about maintaining Planned Independent Requirements for your materials (<em>DXTR1###, DXTR2###, DXTR3###</em>) in plant <em>DL00</em> The requirement values are entered in the table for each period (for the upcoming 12 months). Currently, all values are set to “0”. Using the function <img src="media/image52.png" style="width:0.8577in;height:0.19685in" />, you can enter the same requirement for multiple periods simultaneously. In the displayed mass maintenance dialog box, <strong>12 periods were</strong> selected (beginning with the current month) and a <strong>suggested requirement of 100 pieces</strong> was entered.</td>
<td style="text-align: right;"><p>12 periods</p>
<p>100 pieces</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image53.png" style="width:2.3468in;height:2.90931in" /></td>
<td style="text-align: center;">🡪</td>
<td style="text-align: center;"><img src="media/image54.png" style="width:1.91806in;height:1.52847in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4"><table style="width:81%;">
<colgroup>
<col style="width: 80%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Note</strong></p>
<p>Creation options in mass maintenance: In the Mass Maintenance function in SAP Fiori , you can maintain planned independent requirements in three ways:</p>
<ul>
<li><p>Copy from reference material:<br />
Adopts the planned independent requirements of another material as a template.</p></li>
<li><p>Enter quantities:<br />
You manually enter a fixed quantity that will be applied to the selected periods.</p></li>
<li><p>Forecast quantity:<br />
Uses automatically calculated forecast values from material requirements planning, if available.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">By confirming with <img src="media/image55.png" style="width:0.42247in;height:0.17717in" /> This value is applied to all selected periods at the same time.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><img src="media/image56.png" style="width:4.68779in;height:1.15603in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">Please click on <img src="media/image57.png" style="width:0.3045in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4">Click <img src="media/image20.png" style="width:0.35039in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"></td>
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
<th colspan="2"><h1 id="step-5-schedule-mrp-runs">Step 5: Schedule MRP Runs</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Schedule Material Requirements Planning (MRP).</p>
<p><strong>Short Description</strong> Process a MRP run to generate a series of planned orders that satisfy the requirements from demand management. Concurrently with MPS, the MRP materials will be processed leading to the generation of planned orders for dependent requirements that have been created by the BOM explosion process.</p>
<p><strong>Name (Position)</strong> Jun Lee (Production Manager)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To start MRP Scheduling, in the space <em>Production Planning and Execution</em> space and the role of <em>Plant Manager</em> use the <em>Schedule MRP Runs</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image58.png" style="width:1.59183in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the Application jobs screen, select <img src="media/image59.png" style="width:0.3884in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The system then displays the <em>New Job: Material Requirements Planning (MRP)</em> screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Select the <strong>Material Requirements Planning (MRP)</strong> <em>job template</em> and enter a <em>job name</em> <strong>Material Requirements Planning (MRP) ###</strong>.</td>
<td style="text-align: right;"><p>Material Requirements Planning (MRP)</p>
<p>Material Requirements Planning (MRP) ###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image60.png" style="width:5.15936in;height:1.51567in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image61.png" style="width:0.38159in;height:0.17717in" />. Define the scheduling options in the <em>Scheduling options</em> area. Click on <img src="media/image62.png" style="width:1.41732in;height:0.17717in" /> and Set <em>Recurrence pattern</em> to <strong>Single run</strong>.</td>
<td style="text-align: right;">Single Run</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image63.png" style="width:4.92632in;height:1.67756in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image42.png" style="width:0.23849in;height:0.17717in" /> and proceed with <img src="media/image64.png" style="width:0.38159in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Enter as <em>Plant</em> <strong>DL00</strong> and product group PG<strong>-DXTR###</strong>. Select the following options in the <em>Parameters screen area</em></p>
<p>Section <em>Also</em> <em>to be included in the planning</em></p>
<ul>
<li><p><em>All Order BOM Components</em>: <strong>Select</strong></p></li>
</ul></td>
<td style="text-align: right;"><p>DL00</p>
<p>DXTR3###</p>
<p>All Order BOM Components</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Section <em>Control Parameters</em></p>
<ul>
<li><p>Replanning: <strong>Select</strong></p></li>
<li><p>Scheduling: <strong>1</strong> (Determ. of Basic Dates for Pl. Orders)</p></li>
<li><p>Planning mode: <strong>1</strong> (Adjust Planning Data)</p></li>
<li><p>Output Material List (Job log): S<strong>elect</strong></p></li>
</ul></td>
<td style="text-align: right;"><p>1</p>
<p>1</p>
<p>Output</p>
<p>Material List</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image65.png" style="width:4.95841in;height:1.98189in" /></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2">Select <img src="media/image66.png" style="width:0.50424in;height:0.17717in" /> to complete the process.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> In material requirements planning, a net requirements calculation is carried out to determine whether there is a shortage situation for a material.In addition, the stock and the already existing firm receipts (e.g. purchase orders, production orders, fixed purchase requisitions, and planned orders) are compared with the safety stock and the requirements. This comparison results in the planning-available quantity.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As soon as the planning run is completed, a job is displayed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image67.png" style="width:5.05394in;height:1.11794in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Check the planning details of the <em>results</em> overview by.<img src="media/image68.png" style="width:0.22448in;height:0.17459in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image69.png" style="width:5.07345in;height:4.1126in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image36.png" style="width:0.33542in;height:0.17917in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-6-review-stockrequirements-list">Step 6: Review Stock/Requirements List</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Review the Stock/Requirements List.</p>
<p><strong>Short Description</strong> Review the Stock/Requirements List for your deluxe touring bike.</p>
<p><strong>Name (Position)</strong> Lars Iseler (Shop Floor Worker 2)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The Stock/Requirements List is a list which dynamically changes whenever a transaction occurs using the given material. Display and review the Stock/Requirements List for all materials of the red deluxe touring bike on hand and the demand that exists against these products. The report shows that there is no stock and therefore nothing is available for use at this time.</td>
<td style="text-align: right;">Stock/Requirements List</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">To display the stock/requirements list, in the space <em>Production Planning and Execution</em> space and the role of <em>Shop Floor Worker</em> use the M<em>onitor Stock/Requirements List</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image70.png" style="width:1.58874in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">On the <em>Individual access</em> tab, enter <em>Material</em> <strong>DXTR3###</strong> and <em>Plant</em> <strong>DL00</strong>.</td>
<td style="text-align: right;"><p>DXTR3###</p>
<p>DL00</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image71.png" style="width:3.55303in;height:2.64161in" /></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image72.png" style="width:0.5436in;height:0.18983in" /> to display the associated stock/requirements list.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image73.png" style="width:4.2047in;height:2.94926in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The system currently lists all entries as individual lines. Select <img src="media/image74.png" style="width:0.21389in;height:0.18472in" /> to summarize the entries into period totals. This allows you to see the planned independent requirements, planned receipts, and ATP quantities summarized by days, weeks, or months, depending on the selected tab.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image75.png" style="width:4.00589in;height:2.2754in" /></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2">Select <img src="media/image76.png" style="width:0.22532in;height:0.18898in" /> to go back to the individual rows.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">To view the details of the first planned order (PldOrd), select <img src="media/image77.png" style="width:0.19757in;height:0.18898in" /> (Element Details).</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image78.png" style="width:4.99372in;height:1.28569in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Select <img src="media/image79.png" style="width:0.19685in;height:0.17717in" /> to display the pegged requirements.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image80.png" style="width:5.08333in;height:1.29548in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">You can see that this planned order is to fulfill our Safety Stock and the first planned independent requirement that was created when we disaggregated our SOP.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image36.png" style="width:0.33465in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-7-convert-planned-order-into-production-order">Step 7: Convert Planned Order into Production Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Convert a planned order into a production order.</p>
<p><strong>Short Description</strong> Convert a planned order generated in the MPS/MRP run to a production order. The stock requirements list displays the suggested planned orders from the MPS run.</p>
<p><strong>Name (Position)</strong> Lars Iseler (Shop Floor Worker 2)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">To convert planned orders into production orders, in the space <em>Production Planning and Execution</em> space and the role of <em>Shop Floor Worker</em> use the SAP Fiori app <em>Convert Planned Orders</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image81.png" style="width:1.58327in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><strong>Note</strong> You may be asked to define your area of responsibility (cf. Step 4).</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Enter <em>Material</em> <strong>DXTR3###</strong> and click on <img src="media/image82.png" style="width:0.27559in;height:0.19685in" />.</td>
<td style="text-align: right;">DXTR3###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image83.png" style="width:5.16833in;height:1.98681in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will see your planned order. Select the third planned order. In the <em>Action</em> tab, you can convert your planned order into a production order using the corresponding button <img src="media/image84.png" style="width:1.6063in;height:0.19685in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image85.png" style="width:3.38106in;height:1.72001in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You will be redirected to the <em>Production Order Create: Header</em> screen. The order is release automatically.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image86.png" style="width:5.06184in;height:3.45169in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image87.png" style="width:0.30099in;height:0.1871in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> As soon as you save the production order, the system automatically calculates the planned production costs. This is also displayed accordingly in the status bar.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The system assigns a unique number to the production order. Please make a note of the production order number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image88.png" style="width:2.00535in;height:0.26738in" /></td>
<td style="text-align: right;"><p>Production order number</p>
<p>___________________</p></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image36.png" style="width:0.33194in;height:0.17847in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-8-receive-goods-in-inventory">Step 8: Receive Goods in Inventory</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Receive goods in the Dallas plant.</p>
<p><strong>Short Description</strong> Receive enough goods in the Dallas storage locations to start the production process.</p>
<p><strong>Name (Position)</strong> Susanne Castro (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Usually, at this point the purchasing department in Dallas would take over and procure enough raw materials from vendors to fill the inventory so that the production process can be initiated. In this case study, we are bypassing this procurement process (this process is explained in the MM unit in detail).</p>
<p>Because the inventory for all DXTR3### components is empty, we will assume that we find 500 pieces each in the storage location.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To receive goods in the inventory, in the space <em>Production Planning and Execution</em> space and the role of <em>Goods Receipt Clerk</em> use the app <em>Post Goods Receipt without Reference</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image89.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The document and posting date are already defaulted with the current date and can thus be transferred.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image90.png" style="width:5.06651in;height:1.21203in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Directly below you will find the <em>Item</em> section<em>.</em> The table there is ready for input and offers <strong>item 01</strong> in advance.</td>
<td style="text-align: right;">Items</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image91.png" style="width:5.23275in;height:0.76551in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the line of <strong>item 01</strong>, you will switch to a separate input window.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your <em>Material</em> <strong>TRWA1###</strong> and press Enter. Now you can enter the <em>Quantity</em> <strong>500</strong> with <em>Unit</em> <strong>EA</strong>. Next, choose <em>Plant</em> <strong>DL00</strong>. When choosing the <em>Storage Location</em> your storage for semi-finished goods (<strong>SF00</strong>) is will be proposed. You can check the status directly in the selection screen.</td>
<td style="text-align: right;"><p>TRWA1###</p>
<p>500 EA</p>
<p>DL00</p>
<p>SF00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image92.png" style="width:2.44408in;height:1.72076in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Choose the <em>Storage Location</em> <strong>SF00</strong>.The <em>Stock Type</em> is automatically set to <strong>Unrestricted-Use</strong>, and the <em>Special Stocks</em> is <strong>None</strong>.</td>
<td style="text-align: right;"><p>Unrestricted-Use</p>
<p>None</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image93.png" style="width:5.06132in;height:1.62307in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image94.png" style="width:0.70866in;height:0.17717in" /> to accept your entries and, at the same time, to be able to specify a new item. The system confirms the transfer of the item.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image95.png" style="width:1.51849in;height:0.38165in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now repeat the procedure for the other components of the bike DXTR3###.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><table style="width:79%;">
<colgroup>
<col style="width: 39%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th><strong>Material</strong></th>
<th style="text-align: center;"><strong>Quantity</strong></th>
<th style="text-align: center;"><strong>Unit</strong></th>
<th style="text-align: center;"><strong>Plant</strong></th>
<th style="text-align: center;"><strong>SLoc</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>TRFR3### (Touring Frame-Red)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
<tr>
<td>DGAM1### (Derailleur Gear Assembly)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
<tr>
<td>TRSK1### (Touring Seat Kit)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
<tr>
<td>TRHB1### (Touring Handle Bar)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
<tr>
<td>PEDL1### (Pedal Assembly)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
<tr>
<td>CHAN1### (Chain)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
<tr>
<td>BRKT1### (Brake Kit)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
<tr>
<td>WDOC1### (Warranty Document)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
<tr>
<td>PCKG1### (Packaging)</td>
<td style="text-align: center;">500</td>
<td style="text-align: center;">EA</td>
<td style="text-align: center;">DL00</td>
<td style="text-align: center;">RM00</td>
</tr>
</tbody>
</table></td>
<td style="text-align: right;"><p>TRFR3###</p>
<p>DGAM1###</p>
<p>TRSK1###</p>
<p>TRHB1###</p>
<p>PEDL1###</p>
<p>CHAN1###</p>
<p>BRKT1###</p>
<p>WDOC1###</p>
<p>PCKG1###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As soon as you create the last item, confirm it with <img src="media/image96.png" style="width:0.34752in;height:0.17717in" /> to automatically return to the goods receipt posting. There you will see all created items.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image97.png" style="width:5.11515in;height:2.0235in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If you have forgotten an item, you can add further items by clicking on <img src="media/image98.png" style="width:0.28256in;height:0.2246in" />Furthermore, you can also correct entries if necessary.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Save your goods receipt with <img src="media/image99.png" style="width:0.2688in;height:0.17717in" />.The SAP system will assign a unique number to the goods receipt and issue an associated message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image100.png" style="width:3.01059in;height:1.58602in" /></td>
<td style="text-align: right;"><p>Material Document Number</p>
<p>___________________</p></td>
</tr>
<tr>
<td colspan="2">Confirm the success message with <img src="media/image101.png" style="width:0.46517in;height:0.18898in" /> .</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image36.png" style="width:0.33465in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-9-issue-goods-to-production-order">Step 9: Issue Goods to Production Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Issue goods to a production order.</p>
<p><strong>Short Description</strong> Now that all necessary components are on stock issue them to your production order in precise quantity.</p>
<p><strong>Name (Position)</strong> Sanjay Datar (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The goods issue process is fully defined in the production order, BOM, and routing. The quantities and the materials are reserved for this specific production order, they will be withdrawn with reference to the order number and will be used to assign actual costs to the production order for managerial accounting purposes.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To issue goods to a production order, in the space <em>Production Planning, Execution space,</em> and the role of <em>Warehouse Employee</em> use the app <em>Post Goods Movement</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image102.png" style="width:1.54954in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Make sure that <strong>Goods Issue</strong> and <strong>Order</strong> are selected in the drop-down menus.</td>
<td style="text-align: right;"><p>Goods Issue</p>
<p>Order</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image103.png" style="width:4.91984in;height:0.996in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The <em>Document Date</em> as well as the <em>Posting Date</em> should be already set to the current date. The <em>Movement Type</em> should be set to <strong>261</strong> (GI for order).</td>
<td style="text-align: right;">261</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image104.png" style="width:5.45756in;height:1.20211in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your noted <strong>production order</strong> number.</td>
<td style="text-align: right;">production order</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Alternatively, click the value help icon <img src="media/image105.png" style="width:0.19685in;height:0.19685in" /> in the order field. In the <em>Order Number (1)</em> popup, use the icon on the far right <img src="media/image106.png" style="width:0.19488in;height:0.17717in" /> to display a list of all tabs. Select the tab <em>Production Orders using the Info System</em>. On this tab, enter your material <strong>DXTR3###</strong> in the <em>Material</em> field and click <img src="media/image107.png" style="width:0.47055in;height:0.20056in" />. Select your order and accept it with <img src="media/image108.png" style="width:0.19685in;height:0.19685in" />.</td>
<td style="text-align: right;"><p>Process Orders using the Info System</p>
<p>DXTR3###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Once you have found or entered your production order number, press <img src="media/image109.png" style="width:0.20472in;height:0.17717in" /> to load the order details.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image110.png" style="width:5.17372in;height:0.93611in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Note</strong> Goods issues posting for the required components is another milestone in the production order process. The following functions are performed when a GI for the components of the production order is posted:</p>
<ul>
<li><p>Storage-location-specific update of the stock and consumption fields</p></li>
<li><p>Reduction of the reservation (for planned withdrawal)</p></li>
<li><p>Update of costs for unplanned withdrawals</p></li>
<li><p>Determination of actual costs (valuation) and order update</p></li>
<li><p>Consumption update</p></li>
<li><p>Generation of material and accounting documents (FI and CO documents)</p></li>
<li><p>Creation of material document.</p></li>
<li><p>Creation of accounting document</p></li>
<li><p>Creation of controlling document</p></li>
<li><p>Printing of GI document</p></li>
</ul>
<p>The goods issues posting is controlled through a movement type (261), to which each posting refers. This can take place manually or automatically.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">An itemized list will appear. It lists all the materials and their respective quantities that need to be issued to your order. You need to tell the system what Storage Location the materials should be withdrawn from. For the Touring Aluminum Wheel Assembly (TRWA1###), enter <strong>SF00</strong> (Semi-finished goods) and for all other materials <strong>RM00</strong> (Raw materials) in the SLoc fields. Before pressing Enter, compare your screen with the one shown below. Notice that your quantity could be different.</td>
<td style="text-align: right;"><p>SF00</p>
<p>RM00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If you are unable to enter the storage location for a particular material, this is due to the open detail view in the lower part of the screen. Once you minimize this view, you can continue as usual.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Flag each item with <strong>OK.</strong> If you cannot flag the first item please close the detail view with a click on <img src="media/image111.png" style="width:0.22047in;height:0.19685in" /> unter the line item list.</td>
<td style="text-align: right;">OK</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image112.png" style="width:5.14788in;height:1.35479in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image113.png" style="width:0.24102in;height:0.15064in" /> and record the material document number.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image114.png" style="width:2.20887in;height:0.28299in" /></td>
<td style="text-align: right;"><p>Material Document Number</p>
<p>___________________</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image36.png" style="width:0.33194in;height:0.17847in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="step-10-review-production-order-status">Step 10: Review Production Order Status</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><p><strong>Task</strong> Review the production order status.</p>
<p><strong>Short Description</strong> Review the current production order with respect to the status of the order.</p>
<p><strong>Name (Position)</strong> Michael Brauer (Shop Floor Worker 4)</p></td>
<td style="text-align: right;"><strong>Time</strong> 10 min</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the production order, in the space <em>Production Planning and Execution</em> space and the role of <em>Shop Floor Worker</em> use the app <em>Manage Production Orders</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image115.png" style="width:1.60885in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">When you open the app for the first time, you will see a welcome message telling you to select an area of responsibility. Confirm this with <img src="media/image116.png" style="width:0.29134in;height:0.19685in" />, another popup will appear.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image117.png" style="width:4.56497in;height:3.23491in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Choose <em>Production Supervisor</em>. No Plant is currently assigned. Select the plant in Dallas.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image118.png" style="width:4.51616in;height:3.09843in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now select the tab Work Centers/Resources. Choose the <em>Work Center</em> <strong>DL Assembly (</strong>ASSY1000<strong>)</strong>, <strong>DL Inspection (</strong>INSP1000<strong>)</strong> and <strong>DL Packaging (</strong>PACK1000<strong>)</strong> from your Pland Dallas</td>
<td style="text-align: right;"><p>DLAssembly</p>
<p>DL Inspection</p>
<p>DL Packaging</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image119.png" style="width:4.4185in;height:3.12664in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The values are saved automatically here. Go to SAP Fiori Launchpad <img src="media/image36.png" style="width:0.33542in;height:0.17917in" />and open the app <em>Edit production orders</em> again. You will receive an overview of all existing orders. Depending on your course progress, there may be multiple production orders with different processing statuses.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image120.png" style="width:5.15319in;height:1.7655in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the field <em>Material</em> enter your material <strong>DXTR3###</strong> and choose <img src="media/image5.png" style="width:0.27165in;height:0.19685in" /> to display your order.</td>
<td style="text-align: right;">DXTR3###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image121.png" style="width:5.23107in;height:0.92071in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>The tabular overview already provides you with various information about your order, such as the current status and the current processing status.</p>
<p>For further information select the entry. You will be forwarded to the details of the production order.</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image122.png" style="width:5.20069in;height:2.66222in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on the status <img src="media/image123.png" style="width:0.43349in;height:0.19762in" /> for more information. You can see that your production order is precosted and a settlement rule has been created.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image124.png" style="width:3.51667in;height:1.29562in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now click on the <em>Components</em> tab. The screen scrolls to the corresponding position.</td>
<td style="text-align: right;">Components</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image125.png" style="width:5.12765in;height:2.63896in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the last task, you posted the goods issue for the production order. In the production order, you now see that there are no more open quantities for this order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image36.png" style="width:0.33333in;height:0.18056in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-11-confirm-production-completion">Step 11: Confirm Production Completion</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Confirm production order completion.</p>
<p><strong>Short Description</strong> Confirm completion for your production order.</p>
<p><strong>Name (Position)</strong> Michael Brauer (Shop Floor Worker 4)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">When the assembly has been completed for the current production order, we need to confirm that certain procedures and activities have been completed and record the quantity of the finished product that has been manufactured.</td>
<td style="text-align: right;">Production completion</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To confirm production completion, in the space <em>Production Planning and Execution</em> space and the role of <em>Shop Floor Worker</em> use the app <em>Enter Production order Confirmation.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image126.png" style="width:1.59413in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Enter your <strong>production order</strong> number and click on <img src="media/image127.png" style="width:0.32677in;height:0.19685in" />.</td>
<td style="text-align: right;">Production order number</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If you no longer know this, you can alternatively search for your order. To do so, use the value help symbol in the <em>order field.</em> <img src="media/image128.png" style="width:0.17717in;height:0.17717in" />. In the popup, go <img src="media/image129.png" style="width:0.20866in;height:0.17717in" />to the search <em>for production orders for the material and standard routing</em> and enter your material number <strong>DXTR3</strong> ###. Click on <img src="media/image130.png" style="width:0.33858in;height:0.17717in" />. Select your order and accept it with <img src="media/image131.png" style="width:0.20866in;height:0.17717in" />.</td>
<td style="text-align: right;">DXTR3 ###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image132.png" style="width:5.11184in;height:1.32847in" /></td>
<td style="text-align: right;"><p>Final Confirm.</p>
<p>Clear Reservation</p>
<p>Amount</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image133.png" style="width:4.41523in;height:1.54931in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Then click on <img src="media/image134.png" style="width:0.31266in;height:0.19896in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Check if <strong>Final Confirmation</strong> and <strong>Clear Open Reserv.</strong> is already checked in the <em>Confirmation Type</em> section.</td>
<td style="text-align: right;"><p>Final Confirmation</p>
<p>Clear Open Reserv</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image135.png" style="width:4.96238in;height:2.54724in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><p>Furthermore, in the <em>Actual Data</em> tab, the quantity of bicycles that you should produce for this order should already be entered in the <em>Yield Quantity</em> field<em>.</em></p>
<p>Change the <em>Start Execution</em> to <strong>1 hour earlier</strong> than the preset time.</p></td>
<td style="text-align: right;">1 hour earlier</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image136.png" style="width:4.9954in;height:2.94633in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Save your entries with <img src="media/image137.png" style="width:0.28214in;height:0.18339in" />. You will get a confirmation from the system.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image138.png" style="width:2.6in;height:0.35827in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> When the confirmation is saved, labor costs for the order are calculated automatically. The quantity yield also establishes the parameters for the goods receipt into Inventory.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click to <img src="media/image36.png" style="width:0.33542in;height:0.18333in" />go to SAP Fiori Return to Launchpad.</td>
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
<th></th>
<th colspan="2"><h1 id="step-12-review-production-order-status">Step 12: Review Production Order Status</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Review the production order status.</p>
<p><strong>Short Description</strong> Review the current production order with respect to the status of the order.</p>
<p><strong>Name (Position)</strong> Michael Brauer (Shop Floor Worker 4)</p></td>
<td style="text-align: right;"><strong>Zeit</strong> 5 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the production order, in the space <em>Production Planning and Execution</em> space and the role of <em>Shop Floor Worker</em> use the app <em>Manage Production Orders</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image139.png" style="width:1.55796in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the field <em>Material</em> enter your material <strong>DXTR3###</strong> and choose <img src="media/image5.png" style="width:0.27165in;height:0.19685in" /> to display your order.</td>
<td style="text-align: right;">DXTR3###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image140.png" style="width:5.26789in;height:1.51222in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see, the status of your production order has changed from <em>Released</em> to <em>Confirmed</em>. Furthermore, the processing status is now at <em>Move to storage</em>.</td>
<td style="text-align: right;">Confirmation</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">For more information, select the entry, you will be redirected to the details of the production order. Click on the <em>Confirmation</em> tab to go to the related area.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image141.png" style="width:5.23836in;height:1.10084in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">An order confirmation is now available. You can see that the complete quantity of your production order has been confirmed and that there is no scrap.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">After the confirmation, the goods receipt now needs to take place to complete the order.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image36.png" style="width:0.33465in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-13-receive-goods-from-production-order">Step 13: Receive Goods from Production Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Post a goods receipt from production order.</p>
<p><strong>Short Description</strong> Post a goods receipt from your production order.</p>
<p><strong>Name (Position)</strong> Susanne Castro (Goods Receipt Clerk)</p></td>
<td style="text-align: right;"><strong>Time</strong> 15 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Receive the completed products into finished goods inventory. Check the quantity proposed against the quantity specified in the production order and the quantity specified during confirmation. If there are any discrepancies, the system will decide if an error or warning message should be generated, depending upon the deviation identified.</td>
<td style="text-align: right;">Goods receipt</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To post the goods receipt, in the space <em>Production Planning and Execution</em> space and the role of <em>Goods Receipt Clerk</em> use the app <em>Post goods receipt for production order</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2"><img src="media/image142.png" style="width:1.62672in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your noted <strong>production order</strong>. Alternatively, click the input help icon and enter your product <img src="media/image143.png" style="width:0.1875in;height:0.18056in" /><strong>DXTR3###</strong> in the search. Press <img src="media/image144.png" style="width:0.29167in;height:0.17361in" />and then select your production order from the results list. After you have entered or found your number, press Enter. Your production order will be loaded and displayed</td>
<td style="text-align: right;"><p>Production order</p>
<p>DXTR3###</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image145.png" style="width:5.06415in;height:1.12563in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Add the storage location <strong>FG00</strong> for end products, all other settings can be accepted.</td>
<td style="text-align: right;">FG00</td>
</tr>
<tr>
<td colspan="2"><img src="media/image146.png" style="width:5.08167in;height:0.90839in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Save your goods receipt with <img src="media/image147.png" style="width:0.27617in;height:0.17717in" />. The SAP system will assign a unique number to the goods receipt and issue a corresponding message.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image148.png" style="width:2.31919in;height:1.18504in" /></td>
<td style="text-align: right;">Material Document Number</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Furthermore, this updates the current value of the material produced to the production order. Confirm the successmessage with <img src="media/image149.png" style="width:0.41339in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image36.png" style="width:0.33465in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-14-review-costs-assigned-to-production-order">Step 14: Review Costs Assigned to Production Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> View the corresponding costs assigned to your production order.</p>
<p><strong>Description</strong> Review all costs associated with your production order.</p>
<p><strong>Name (Position)</strong> Jamie Shamblin (Controller)</p></td>
<td style="text-align: right;"><strong>Zeit</strong> 5 Min.</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To view the cost of a manufacturing job, in the space <em>Production Planning and Execution</em> space and the role of <em>Controller</em> use the <em>Production Cost Analysis</em> app.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image150.png" style="width:1.70604in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the <em>Product</em> field enter <strong>DXTR3###</strong> and change the <em>Order Status</em> from <strong>Open</strong> to <strong>Closed</strong></td>
<td style="text-align: right;"><p>DXTR3###</p>
<p>Closed</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image151.png" style="width:5.0752in;height:1.02691in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image5.png" style="width:0.24449in;height:0.17717in" /> to start the search. Your recently completed production order will be displayed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image152.png" style="width:5.02663in;height:0.72108in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">This overview lists the summed target and actual costs and shows any variances. Click on <img src="media/image153.png" style="width:0.34016in;height:0.17717in" /> at the end of the entry to open the cost details.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image154.png" style="width:5.04698in;height:2.64291in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Pay only marginal attention to overhead costs. In this case, they are shown in the target costs but not in the actual costs.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now that the finished products have been received in the Inventory, the Manufacturing Output Settlement Variance has been added. How is this figure calculated by the system?</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image36.png" style="width:0.33125in;height:0.18194in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-15-settle-costs-of-production-order">Step 15: Settle Costs of Production Order</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Settle costs of your production order.</p>
<p><strong>Short Description</strong> Settle the costs of your production order. The costs are temporarily captured in the production order and they need to be assigned to an appropriate cost object. Compare the actual costs to the planned costs to identify any deviations or potential problems in this regard.</p>
<p><strong>Name (Position)</strong> Jamie Shamblin (Controller)</p></td>
<td style="text-align: right;"><strong>Time</strong> 20 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To settle costs of a production order, in the space <em>Production Planning and Execution</em> space and the role of use the app <em>Run Actual Settlement</em> - <em>Order - Single</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image155.png" style="width:1.54182in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">If you have to input the Controlling Area, enter <strong>NA00</strong>, and click on <img src="media/image156.png" style="width:0.54331in;height:0.19685in" />.</td>
<td style="text-align: right;">NA00</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Enter your <strong>production order number</strong>, alternatively search for it with your material DXTR3### in the Input-Help. In the <em>Parameters</em> section enter <em>Settlement- and posting period</em> as <strong>current month</strong> (e.g., 006 for June). Enter as <em>Fiscal Year</em> the <strong>current year</strong>. Make Sure that <strong>Test Run</strong> is checked in the <em>Processing Options</em> section.</td>
<td style="text-align: right;"><p>Order number</p>
<p>current month</p>
<p>current year</p>
<p>Test Run</p></td>
</tr>
<tr>
<td colspan="2"><img src="media/image157.png" style="width:5.02128in;height:2.93594in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image158.png" style="width:0.49636in;height:0.23358in" /> to proceed. Confirm any occurring pop-ups with enter. You enter the screen <em>Actual Settlement: Oder Basic list</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image159.png" style="width:5.09157in;height:2.2795in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image160.png" style="width:0.18194in;height:0.18194in" />in the upper part of the image to open the detailed lists.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image161.png" style="width:5.01334in;height:1.49295in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p>From the Menu bar choose:</p>
<blockquote>
<p><strong>Menu ► Environment ► Report</strong></p>
</blockquote></td>
<td style="text-align: right;">Menu Bar</td>
</tr>
<tr>
<td colspan="2">The <em>Select Report</em> pop-up will appear.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image162.png" style="width:3.17666in;height:1.50034in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <strong>Actual/Plan/Variance</strong> and confirm your selection with <img src="media/image163.png" style="width:0.19685in;height:0.19685in" />. A corresponding report group is generated and displayed.</td>
<td style="text-align: right;">Actual/Plan/Variance</td>
</tr>
<tr>
<td colspan="2"><img src="media/image164.png" style="width:4.89371in;height:3.91405in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The test run is now complete and the <em>actual settlement</em> should now be performed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on <img src="media/image165.png" style="width:0.19236in;height:0.17708in" /> to go back. Confirm the Message to leave the report <img src="media/image166.png" style="width:1.16682in;height:0.21608in" />.Afterwards press<img src="media/image165.png" style="width:0.19236in;height:0.17708in" /> two times to get back to the entry screen.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Deselect Test Run and again click on <img src="media/image167.png" style="width:0.45692in;height:0.20888in" />. In contrast to the previous run, you can now see in the <em>Processing Options</em> area that this was an update run that was <em>completed with no errors</em>.</td>
<td style="text-align: right;"><del>Test Run</del></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image168.png" style="width:5.04364in;height:1.11546in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Open the report <strong>Actual/Plan/Variance</strong> again by clicking on <img src="media/image160.png" style="width:0.18194in;height:0.18194in" /> first and then use the menu bar path <strong>Menu ► Environment ► Report</strong> and select the option <strong>Actual/Plan/Variance</strong>.</td>
<td style="text-align: right;">Actual/Plan/Variance</td>
</tr>
<tr>
<td colspan="2"><img src="media/image169.png" style="width:5.10338in;height:4.57026in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">You can see that the costs have now been settled.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click <img src="media/image36.png" style="width:0.33465in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2" style="text-align: left;"><h1 id="pp-challenge">PP Challenge</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: left;"><strong>Learning Objective</strong> Understand and perform an integrated manufacturing process.</td>
<td style="text-align: right;"><strong>Time</strong> 60 min</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p><strong>Motivation</strong> After you have successfully worked through the <em>Production Planning and Execution</em> case study you should be able to solve the following challenge on your own.</p>
<p><strong>Scenario</strong> In this challenge, you should plan the production for the product group Offroad Bicycles for the next months. Take into consideration that the materials of the product group have to be assigned to the strategy group (again “40”). You do not have to change the routing.</p>
<p>Therefore, enter manually the following planned independent requirements:</p>
<table style="width:68%;">
<colgroup>
<col style="width: 35%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th><strong>Period</strong></th>
<th><strong>PIRs</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Current month + 1</td>
<td>110</td>
</tr>
<tr>
<td>Current month + 2</td>
<td>150</td>
</tr>
<tr>
<td>Current month + 3</td>
<td>175</td>
</tr>
<tr>
<td>Current month + 4</td>
<td>200</td>
</tr>
<tr>
<td>Current month + 5</td>
<td>85</td>
</tr>
<tr>
<td>Remaining months</td>
<td>100</td>
</tr>
</tbody>
</table>
<p>The challenge focus will be on ORMN1###. For that product, please convert the first planned order into a production order. Then, carry out the production process. When posting goods receipts and issues, note the bill of materials for ORMN1###, which differs from the one in the case study. Once production is complete (including all goods movements), you settle costs afterwards.</p>
<p><strong>Task Information</strong> Since this task is based on the <em>Production Planning and Execution</em> case study you can use it as guidance. However, it is recommended that you solve it without any help in order to test your acquired knowledge.</p></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"></td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"></td>
</tr>
</tbody>
</table>
