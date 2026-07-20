---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Case_Study_WM_IV_en_v4.3
slides: 0
fuente: Intro_S4HANA_Using_Global_Bike_Case_Study_WM_IV_en_v4.3.docx
---

Warehouse Management (WM) IV

> This case study explains the integrated warehouse management process of the physical inventory. A storage bin is checked by means of a continuous physical inventory.

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
<p>Chris Bernhardt</p>
<p>Stefan Weidner</p>
<p>Version</p>
<p>4.3</p>
<p>Last Update</p>
<p>July 2025</p></th>
<th><p>MOTIVATION</p>
<p>Warehousing is of significant importance for logistics.</p>
<p>For a company, it is of central importance to know about the precise inventory quantities and inventory values of its warehouse complex. The warehouse management thus gathers all position outflows and inflows both quantitatively and qualitatively.<br />
Incorrect postings, shrinkage, and operational errors, however, might lead to stock differences.</p>
<p>In order to reveal missing quantities and differences and in order to gather physical stocks, the warehouse management draws on physical inventory.</p></th>
<th></th>
<th><p>PREREQUISITES</p>
<p>Before using this case study, you should be familiar with navigation in the SAP system.</p>
<p>In order to work through this case study successfully, it is not necessary to have finished the WM exercises although it is recommendable.</p>
<p>Notes</p>
<p>This case study uses the Global Bike (GB) data set, which was created exclusively for SAP UA global curricula.</p>
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
<th colspan="2"><p><strong>Learning Objective</strong> Conduct a physical inventory in the warehouse management.</p>
<p><strong>Scenario</strong> An internal security audit showed that, until now, there has been a mistake in the security concept. Through this mistake, unauthorized persons could have gained access to the pallet warehouse of the San Diego warehouse. For this reason, a continuous physical inventory will be conducted for all pallet warehouses that, according to the inventory control, contain materials and goods.</p>
<p><strong>Employees involved</strong> Carolin Bruzik (Warehouse Supervisor)<br />
Sunil Gupta (Warehouse Employee)</p></th>
<th style="text-align: right;"><strong>Time</strong> 60 min</th>
</tr>
<tr>
<th colspan="3"></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;"><p>The basis of a physical inventory in the SAP S/4HANA Warehouse Management is a system inventory record. In contrast to the sample-based physical inventory, documents are created directly when performing the continuous physical inventory because of the low number of storage bins that have to be checked. The affected storage bins are earmarked for counting and a status is set against the storage bin. In the next step, the activation of the physical inventory document causes the lock of all storage bins that are listed in the document but this can only be conducted if all outstanding transportation orders to the destinations have been completed beforehand. The lock can only be released after clearing the inventory - a manual release is not possible.</p>
<p>After the counting, the results have to be entered into the system. The same applies to any possible recounts. After the finalization of the physical inventory, the difference has to be cleared in the warehouse management system. Since the locked storage bins are released by clearing, this also applies if there are no differences.</p>
<p>Physical inventory is completed through the correction of the storage location stocks in MM inventory management. Thereby, not only the quantity difference is updated, but also the value difference.</p></th>
</tr>
<tr>
<th colspan="3" style="text-align: left;"><img src="media/image2.png" style="width:5.24842in;height:2.64908in" alt="ScreenShot00540" /></th>
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
<p><a href="#step-1-create-and-activate-a-physical-inventory-document">Step 1: Create and Activate a Physical Inventory Document <span>4</span></a></p>
<p><a href="#step-2-display-physical-inventory-document">Step 2: Display Physical Inventory Document <span>7</span></a></p>
<p><a href="#step-3-display-bin-status-report">Step 3: Display Bin Status Report <span>9</span></a></p>
<p><a href="#step-4-enter-count-results">Step 4: Enter Count Results <span>11</span></a></p>
<p><a href="#step-5-start-recount">Step 5: Start Recount <span>13</span></a></p>
<p><a href="#step-6-enter-recount">Step 6: Enter Recount <span>15</span></a></p>
<p><a href="#step-7-display-bin-status-report">Step 7: Display Bin Status Report <span>17</span></a></p>
<p><a href="#step-8-clear-differences-in-warehouse-management">Step 8: Clear Differences in Warehouse Management <span>19</span></a></p>
<p><a href="#step-9-display-bin-status-report">Step 9: Display Bin Status Report <span>20</span></a></p>
<p><a href="#step-10-display-warehouse-inventory-value">Step 10: Display Warehouse Inventory Value <span>22</span></a></p>
<p><a href="#step-11-clear-differences-in-mm-inventory-management">Step 11: Clear Differences in MM Inventory Management <span>24</span></a></p>
<p><a href="#step-12-display-warehouse-inventory-value">Step 12: Display Warehouse Inventory Value <span>26</span></a></p>
<p><a href="#wm-iv-challenge">WM IV Challenge <span>28</span></a></p></th>
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
<th colspan="2"><h1 id="step-1-create-and-activate-a-physical-inventory-document">Step 1: Create and Activate a Physical Inventory Document</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Create and activate a physical inventory document.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to create a physical inventory document</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To create a physical inventory document, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role use the app <em>Carry out Continuous Inventory.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image3.png" style="width:1.58346in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Carry out Continuous Inventory</em>, enter <strong>100</strong> as <em>Warehouse number</em>, <strong>002</strong> as <em>Storage type</em>, <strong>STBN-</strong>*-### (do not forget to replace ### with your number) as <em>Storage bin</em>.</td>
<td style="text-align: right;"><p>100</p>
<p>002</p>
<p>STBN-*-###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image4.png" style="width:4.44126in;height:1.34258in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Below you can find the <em>Program parameters</em> section. There, <strong>LEARN-###</strong> as Name of counter. Also make sure that the value <strong>Only bins not yet counted</strong> is <u>not</u> selected (this also displays storage bins from completed inventories). Compare with the screen below and confirm your entries with <img src="media/image5.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>LEARN-###</p>
<p>Deselect Only bins not yet counted</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image4.png" style="width:4.44126in;height:2.62362in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> The warehouse number is the highest level of organizational unit in warehouse management. In practice, the warehouse number usually corresponds to a physical building or distribution center. Each warehouse number has a substructure that maps the spatial relationship in the warehouse complex in detail.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image6.png" style="width:3.79167in;height:2.23958in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Storage bins are the lowest level of organizational structure. They are assigned to a storage type and a storage section (if one exists). Storage bins represent the physical location where the goods are stored in the warehouse.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the following screen, deselect all storage bins except for <strong>STBN-9-</strong>###.</td>
<td style="text-align: right;">STBN-9-###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image7.png" style="width:4.26562in;height:2.79806in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Now click on Activate button <img src="media/image8.png" style="width:0.17522in;height:0.17717in" /> and thus create a physical inventory document. Through this process, the selected storage bins are blocked against stock putaways and stock removals. Your will receive the following success message:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image9.png" style="width:1.8922in;height:0.20724in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> three times to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-2-display-physical-inventory-document">Step 2: Display Physical Inventory Document</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display your physical inventory document.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to watch your physical inventory document.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To watch your physical inventory document, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role use the app <em>Inventory Overview.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image11.png" style="width:1.59211in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Inventory Overview</em>, enter <strong>100</strong> as Warehouse number.</td>
<td style="text-align: right;">100</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image12.png" style="width:3.24402in;height:1.21819in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Make sure that all other screens are empty and click <img src="media/image5.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><img src="media/image13.png" style="width:5.16528in;height:0.66806in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Use the column Name of counter in order to find and to select your physical inventory document. Click on <img src="media/image14.png" style="width:0.71457in;height:0.17717in" />.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Check the inventory status text, the storage bin, and the count date. Press <img src="media/image15.png" style="width:0.40931in;height:0.17717in" /> in order to see additional key figures of the inventory.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><img src="media/image16.png" style="width:5.16528in;height:2.43542in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press on <img src="media/image17.png" style="width:0.21654in;height:0.17717in" /> to close the popup.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> three times to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-3-display-bin-status-report">Step 3: Display Bin Status Report</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Check the status of your bin status report.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad in order to display the bin status report, which displays a detailed report of each storage bin within the specific warehouse.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the bin status report, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role use the app <em>Run Bin Status Report.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:1.58355in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> (for the San Diego Warehouse) as Warehouse number and <strong>STBN*###</strong> as Storage bin (do not forget to replace ### with your number). Compare with below and press <img src="media/image5.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image19.png" style="width:3.72081in;height:1.73796in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In <em>Bin Status Report: Overview</em> you should see that the storage bin <strong>STBN-9-###</strong> is filled. The screenshot below may differ from your screen.</td>
<td style="text-align: right;">STBN-9-###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image20.png" style="width:4.47759in;height:2.77998in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on your storage bin (STBN-9-###) in order to receive more detailed information about the warehoused goods. Additionally, this screen also includes information about the current physical inventory status.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image21.png" style="width:5.22978in;height:0.78473in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2"><p>Please note the total stock for both goods of this storage bin:</p>
<p>________________________________________________________</p>
<p>________________________________________________________</p></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-4-enter-count-results">Step 4: Enter Count Results</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Enter your count results in the S/4HANA System.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad in order to enter your physical inventory document and the count information in the S/4HANA System in accounting terms.</p>
<p><strong>Name (Position)</strong> Sunil Gupta (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To enter your count results, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Employee</em> role use the app <em>Enter Inventory Count.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image22.png" style="width:1.58355in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Enter Inventory Count: Initial Screen</em>, enter <strong>100</strong> as Warehouse Number and <strong>today’s date</strong> as Count date. Enter <strong>your</strong> <strong>Inventory Record</strong> number if it is not entered automatically. If you cannot remember your inventory record, please re-simulate the transaction of the previous step in order to find it. Also, please enter <strong>LEARN-###</strong> as <em>name of counter</em>. Press Enter to confirm your entries.</td>
<td style="text-align: right;"><p>100</p>
<p>Your Inventory Record Number</p>
<p>Today’s day</p>
<p>LEARN-###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image23.png" style="width:3.5943in;height:2.51896in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In <em>Enter Inventory Count: Overview</em>, for the Material ORMN1###, <strong>add</strong> <strong>5 units to the value</strong> of the previous step and enter this new value as counted quantity. For the Material ORWN1###, enter <strong>the same value</strong> which you have listed in the previous step. Press Enter.</td>
<td style="text-align: right;"><p>ORMN1###</p>
<p>Actual value +5</p>
<p>ORWN1###</p>
<p>Actual value</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image24.png" style="width:5.16528in;height:1.22361in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The deviation of the count result should be more than 20%. For this reason, subsequently, a screen will open in which you will have to confirm the data by pressing Enter.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image25.png" style="width:3.31691in;height:0.25753in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image26.png" style="width:0.30836in;height:0.17502in" /> to update your physical inventory document with the count results.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-5-start-recount">Step 5: Start Recount</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Start the recount.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad in order to enter the data of the recount.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To order to enter the recount, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role use the app <em>Start recount.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image27.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Start Recount: Initial Screen</em>, the number of your <strong>Inventory record</strong> and <strong>100</strong> as Warehouse Number should already be listed. If they are not listed, please fill in the boxes.</td>
<td style="text-align: right;"><p>Inventory record</p>
<p>100</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> If you cannot remember the number of your inventory record, you can identify it once more as in the task <em>Display Physical Inventory Document</em>.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image28.png" style="width:3.49536in;height:2.10913in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press Enter. In the next screen make sure that your storage bin <strong>STBN-9-###</strong> is selected for the recount. Compare with the next screenshot and proceed by clicking on <img src="media/image29.png" style="width:0.72992in;height:0.17717in" /> .</td>
<td style="text-align: right;">STBN-9-###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image30.png" style="width:4.87871in;height:2.23274in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">You will receive following succes message:</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image31.png" style="width:2.36848in;height:0.26316in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-6-enter-recount">Step 6: Enter Recount</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Enter the count results of your recount into the S/4HANA System.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad to enter the count results into the S/4HANA System.</p>
<p><strong>Name (Position)</strong> Sunil Gupta (Warehouse Employee)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To enter the count result of the recount, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Employee</em> role use the app <em>Enter Inventory Count.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image22.png" style="width:1.58355in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Enter Inventory Count: Initial Screen</em>, enter <strong>100</strong> as Warehouse Number, <strong>1</strong> as Recount version, <strong>LEARN-###</strong> as Name of counter and <strong>today’s date</strong> as Count date. Please enter your <strong>Inventory Record Number</strong> if it is not listed automatically. Confirm your entries by pressing Enter.</td>
<td style="text-align: right;"><p>100</p>
<p>1</p>
<p>LEARN-###</p>
<p>Today’s date</p>
<p>Inventory Record Number</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image32.png" style="width:3.43651in;height:2.38076in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Enter Inventory Count: Overview</em>, enter <strong>the same data</strong> that was entered in the first count. Please enter <strong>LEARN-###</strong> as Name of counter for both positions. Press Enter.</td>
<td style="text-align: right;"><p>ORMN1###</p>
<p>Actual value +5</p>
<p>ORWN1###</p>
<p>Actual value</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image33.png" style="width:5.16528in;height:1.20278in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">The deviation of the count result is 20%. Therefore, in the new screen that will open subsequently, you have to confirm the data by pressing Enter.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image26.png" style="width:0.30836in;height:0.17502in" /> in order to update your physical inventory document with the recount results.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-7-display-bin-status-report">Step 7: Display Bin Status Report</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Check the status of your bin status report.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad in order to display the bin status report that displays a detailed report of every storage bin within the specific warehouse.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the bin status report, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role use the app <em>Run Bin Status Report.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:1.58355in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> (for your San Diego warehouse) as Warehouse number and <strong>STBN*###</strong> as Storage bin (replace ### with your number). Click <img src="media/image5.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image34.png" style="width:4.03387in;height:1.20127in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In <em>Bin Status Report: Initial Screen</em>, you should notice that the storage bin <strong>STBN-9-###</strong> is filled. The screenshot below could be look different from your view.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image35.png" style="width:3.55537in;height:2.18236in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click on your material ORMN1### in order to receive detailed information of this quant and check if the amounts have already changed.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> As you can see, the stock unchanged since the stock difference has not been booked into the warehouse management yet.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image36.png" style="width:5.16528in;height:3.80556in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-8-clear-differences-in-warehouse-management">Step 8: Clear Differences in Warehouse Management</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Clear the differences in the warehouse management.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad in order to clear the stock differences within the warehouse management.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To order to clear the differences, use in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role the app <em>Clear Differences in WM.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image37.png" style="width:1.56615in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Clear Differences in WM: Initial Screen</em>, the Warehouse Number <strong>100</strong> and the number of <strong>your Inventory record</strong> should already be entered. If this is not the case, please enter the corresponding figures. Press Enter.</td>
<td style="text-align: right;"><p>100</p>
<p>Inventory record</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image38.png" style="width:3.33944in;height:1.69033in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the list of differences, select your storage bin <strong>STBN-9-###</strong>. Afterwards, click on <img src="media/image39.png" style="width:0.41848in;height:0.17717in" />. You will receive the following success message:</td>
<td style="text-align: right;">STBN-9-###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image40.png" style="width:1.00957in;height:0.19846in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-9-display-bin-status-report">Step 9: Display Bin Status Report</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Recheck the bin status report.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad in order to watch the status of your bin status report. It will offer a detailed overview over each storage bin.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the bin status report, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role use the app <em>Run Bin Status Report.</em></td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image18.png" style="width:1.58355in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In <em>Bin Status Report: Initial Screen</em>, enter <strong>100</strong> as Warehouse number (for your San Diego warehouse) and <strong>STBN*###</strong> as Storage bin (replace ### with your number). Click <img src="media/image5.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>100</p>
<p>STBN*###</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image41.png" style="width:5.16528in;height:1.54931in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Bin Status Report: Overview</em>, click on your storage bin <strong>STBN-9-###</strong> in order to get detailed information. Make sure if the amount of your ORMN1### was adjusted.</td>
<td style="text-align: right;">STBN-9-###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image42.png" style="width:5.16528in;height:5.56319in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-10-display-warehouse-inventory-value">Step 10: Display Warehouse Inventory Value</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the warehouse stock.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad in order to watch the warehouse stock.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the warehouse stock, in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role use the app <em>Display Warehouse Stock</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image43.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Display Warehouse Stocks of Material</em>, enter <strong>ORMN1###</strong> as Material (replace ### with your number) and as <strong>SD00</strong> as Plant. Make sure that all checkboxes are empty and click <img src="media/image5.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: left;"><p>ORMN1###</p>
<p>SD00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image44.png" style="width:5.16528in;height:1.49097in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Pay attention to the fact that the stock difference, although booked for the warehouse management, is not cleared for the inventory management yet. This becomes noticeable as the values for the distribution center San Diego shows the old stock quantity.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image45.png" style="width:5.16528in;height:2.45903in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> twice to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-11-clear-differences-in-mm-inventory-management">Step 11: Clear Differences in MM Inventory Management </h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Clear the differences in MM inventory management.</p>
<p><strong>Short Description</strong> Use the SAP Fiori Launchpad in order to clear the stock differences in the inventory management.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To clear the differences in the inventory management, use in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role the app <em>Clear Differences in Inventory Management</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image46.png" style="width:1.5835in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Clearing of Differences in Inventory Management</em>, enter <strong>100</strong> as Warehouse number and <strong>999</strong> as Storage type.</td>
<td style="text-align: right;"><p>100</p>
<p>999</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image47.png" style="width:5.16528in;height:1.53819in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;"><strong>Note</strong> Storage types are represented as a group of warehouse bins with similar characteristics. Storage types are defined on the basis of their spatial or organizational features.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Press <img src="media/image5.png" style="width:0.41732in;height:0.17717in" />. In the screen <em>List of Quants for Difference Posting in Invent. Management</em>, select your Material <strong>ORMN1###</strong>. Make sure that no other elements are selected.</td>
<td style="text-align: right;">ORMN1###</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image48.png" style="width:5.16528in;height:1.98056in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">Click <img src="media/image39.png" style="width:0.41848in;height:0.17717in" />. On the next screen you will receive a message that your material document is now created.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image49.png" style="width:4.7385in;height:1.52068in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> twice to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="step-12-display-warehouse-inventory-value">Step 12: Display Warehouse Inventory Value</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><p><strong>Task</strong> Display the warehouse stock again.</p>
<p><strong>Short Description</strong> Use the SAP Easy Access Menu in order to see the warehouse stock.</p>
<p><strong>Name (Position)</strong> Carolin Bruzik (Warehouse Supervisor)</p></td>
<td style="text-align: right;"><strong>Time</strong> 5 min</td>
</tr>
<tr>
<td colspan="2"></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">To display the warehouse stock, use in the <em>Warehouse Management</em> area on the <em>Physical Inventory</em> page in the <em>Warehouse Supervisor</em> role the app <em>Display Warehouse Stock</em>.</td>
<td style="text-align: right;">Start</td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image43.png" style="width:1.5748in;height:1.5748in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">In the screen <em>Display Warehouse Stocks of Material</em>, enter <strong>ORMN1###</strong> as Material (replace ### with your number) and <strong>SD00</strong> as Plant. Make sure that all boxes are empty and click <img src="media/image5.png" style="width:0.41732in;height:0.17717in" />.</td>
<td style="text-align: right;"><p>ORMN1###</p>
<p>SD00</p></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image50.png" style="width:5.09563in;height:1.75038in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">As you can see, the amount of material and the associated data in San Diego has increased.</td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center;"><img src="media/image51.png" style="width:5.16528in;height:2.38611in" /></td>
<td style="text-align: right;"></td>
</tr>
<tr>
<td colspan="2">Click on <img src="media/image10.png" style="width:0.39862in;height:0.17717in" /> twice to return to the SAP Fiori Launchpad.</td>
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
<th colspan="2"><h1 id="wm-iv-challenge">WM IV Challenge</h1></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2"><strong>Learning Objective</strong> Conduct a physical inventory.</td>
<td style="text-align: right;"><strong>Time</strong> 45 min</td>
</tr>
<tr>
<td colspan="3" style="text-align: left;"><p>You have successfully gone through the Case Study <em>Warehouse Management IV.</em> Now you are able to demonstrate and to apply your knowledge. For this purpose, you should solve the following additional task on your own.</p>
<p><strong>Scenario</strong> As a warehouse manager, you are in control of the necessary physical inventories within your warehouse. The San Diego warehouse applies the method of continuous inventory. In the course of this inventory, your aim is to check all storage locations of the storage type <em>pallet storage</em>.</p>
<p>In the course of the physical inventory of the storage bin STBN-9-###, which is listed as empty, 120 units of your off-road helmets (<em>OHMT1###)</em> are found in storage location <em>TG00</em>. Strict investigations revealed that they were part of the last delivery and were not entered into the system at all. The goods were also put away into the wrong storage bin, as STBN-3-### would be the standard bin for them. Start this physical inventory within the system, add the count and clear it.</p>
<p>To reconcile the stocks, use a transportation order in order to restore the 120 units from the storage bin STBN-9-### to the storage bin STBN-3-###.</p>
<p><strong>Task Information</strong> You are free to use the Case Study <em>Warehouse Management IV</em> as an aid. It is recommended to accomplish this advanced task without any help in order to thus put your acquired knowledge to a test.</p></td>
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
