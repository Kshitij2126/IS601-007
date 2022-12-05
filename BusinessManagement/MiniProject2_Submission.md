<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Kshitij Aji (ka598)</td></tr>
<tr><td> <em>Generated: </em> 12/4/2022 7:38:02 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/ka598" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205509880-59b37d2f-fc1d-4995-bf5c-4e2a2af8d9ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index Page displayed from Heroku Dev with DIAR-ka598 (Student ID), heroku dev URL,<br>Index Page&#39;s Message with student&#39;s first name, ucid, and IS601 section<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205510125-35ffefad-6ab3-49ad-9896-9445d39e8b16.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changes Made to Layout.html<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205510176-6913cfda-f732-45db-a234-39156141e0f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changes Made to Index.html<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205510424-bcf1ab31-0e7d-4899-9610-4694ad38a8d8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP2_Companies table with UCID (ka598) / DB name (IS601_MP2_Companies) is visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205510459-0055be85-33dd-426c-8f68-41b7587a6f32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>IS601_MP2_Employees table with UCID (ka598) / DB name (IS601_MP2_Employees) is visible<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205512232-70bafd38-d445-4873-8649-2b7c1184d07b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import/Upload CSV Code 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205512241-9df55d50-fbb9-4dc0-9132-4cb441261e24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import/Upload CSV Code 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205512255-dee7ef38-1fae-4773-9cf3-9691bac6bdcf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import/Upload CSV Code 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205512267-176fa20f-81c5-4207-80f9-2e45a814a294.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import/Upload CSV Code 4<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205513335-e9a2a314-ecb3-4d1e-bebd-ff41839802f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>No Selected File Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205513361-6f8265be-f05d-4183-a18d-ad4ad7a4a910.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>File Not a .CSV Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205514166-73a19ff7-80b2-41e2-a279-408a00299e37.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows proper success and Count Message for Companies and Employees inserted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205514302-08de9ab9-60e4-4c8f-9dbd-9d418b9533cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Data Uploaded 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205514307-399aeb54-e4d2-469b-a3d1-739dfef38d75.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Data Uploaded 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205514657-14876b9e-d704-40f3-bb9a-cc72831d03f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee Data Uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205515277-42d4487f-ad4b-4e05-9c2d-69aba80cc375.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Employee Code Changes 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205515284-8bac3121-2af9-45ad-a681-6eb17a44ca92.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Employee Code Changes 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205516404-16e3017f-56d1-4647-9807-f3d2803158ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding New Employee Prior to Form Submission <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205516414-a5fc9b4a-8ded-48fb-8b7b-faad34119455.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New Employee Record Created <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205516431-feb14f8a-91a2-4935-a6e6-f0a68bf2b62e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Name Required Flash Message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205516450-d156fc39-6f1f-4962-8d2d-987167e5c0b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last Name Required Flash Message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205516470-d07defa5-e083-4c07-8717-f23969ae49ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Required Flash Message <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205516487-5d7cff66-d956-4c2f-815c-54139efaca68.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New Employee Record (Mark Twain) shown in VS Code/ IDE <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517175-d2e3f8ed-dd52-431b-86a1-ef2a99bf9b73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Employee Code Changes 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517188-efc25de7-e353-4900-b0cb-8af916c75fc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Employee Code 2 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517196-4d5898bb-c4bc-4274-a0bd-dcc4c0774afc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Employee Code 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517369-702ce3f3-c617-4533-9adf-4c23daccbdc9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Name Filter (Shawna)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517381-148763c4-33c7-4cee-86d2-0b77f9373eeb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First Name Filter Results (Shawna)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517642-fac96921-3b62-4d4a-a74d-6e6860a06296.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last Name Filter (Tarbor)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517669-461f155f-eb3d-4023-a659-3d7bd37121b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last Name Filter Results (Tarbor)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517690-b31b6011-8389-4429-b9bc-5e3bdebdacc0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Filter  (<a href="mailto:&#109;&#97;&#x72;&#x69;&#x63;&#97;&#x2e;&#116;&#97;&#114;&#x62;&#x6f;&#114;&#x40;&#x68;&#x6f;&#116;&#x6d;&#x61;&#105;&#108;&#x2e;&#99;&#111;&#x6d;">&#109;&#97;&#x72;&#x69;&#x63;&#97;&#x2e;&#116;&#97;&#114;&#x62;&#x6f;&#114;&#x40;&#x68;&#x6f;&#116;&#x6d;&#x61;&#105;&#108;&#x2e;&#99;&#111;&#x6d;</a>)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517706-2c4b9c73-95f0-426f-962a-471da8964ed6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Filter Results (<a href="mailto:&#x6d;&#97;&#114;&#x69;&#99;&#x61;&#46;&#116;&#x61;&#114;&#98;&#111;&#114;&#x40;&#x68;&#x6f;&#116;&#x6d;&#97;&#105;&#108;&#x2e;&#99;&#111;&#109;">&#x6d;&#97;&#114;&#x69;&#99;&#x61;&#46;&#116;&#x61;&#114;&#98;&#111;&#114;&#x40;&#x68;&#x6f;&#116;&#x6d;&#97;&#105;&#108;&#x2e;&#99;&#111;&#109;</a>)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517719-f751f6d3-7f4f-4f4e-bd8f-5e19ec22b7c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Filter (20 20 Printing Inc)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205517961-63dc918b-7bc4-46c1-9353-3da538ff570e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Filter Results (20 20 Printing Inc)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205518010-78ecc6db-1bc9-40ca-9070-19ef9948b325.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Asc Filter with Last Name <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205518017-adb11069-5d08-4def-b188-b547fc0ddd85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Asc Filter with Last Name Results <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205518044-07e55a11-79b7-49c5-86c0-37c18ba77d5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Desc Filter with First Name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205518053-f8bc346a-f1cc-4bee-af4c-0252fec2e0ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Desc Filter with First Name Results<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205518672-3bc109f0-598e-428e-ab67-fdc2f67288ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Employee Code Changes 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205518690-9431e401-7bb1-46ea-b1d3-03cde80a752e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Edit Employee Code Changes 2 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205518700-93b49b4c-ed5d-4595-b1ed-18eb901d5453.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Employee Code Changes 3 <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205519272-f4744c41-1a0b-4891-87aa-6aab03b5c682.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee Before Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205519279-e5fb0cff-c558-4ed1-a63c-033bb47fdc94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Results Before editing Employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205519306-58e9ac10-da77-417a-872b-5b3eafad8506.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee After Edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205519315-0cae0225-9455-4142-ad12-69285404cad0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edited Employee in Search Results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205519348-664db5b8-0902-4e3b-a98b-ce57cfd3c9d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB Before editing Employee from  VS Code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205519362-c06ecc1f-5a88-47fb-87ec-398746cccf88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB After Editing Employee  from  VS Code <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205519917-29b7f931-798b-4f45-84ee-d42582472e2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Company Code 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205519931-fe1be2a1-877c-42db-bf24-3588a79d0781.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Company Code 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521069-96483881-e3b6-46e3-9287-458495d7622e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New Company Values before Adding<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521089-58dd321a-35a7-4223-ba38-f1c7c9259a14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New Company Values before Adding 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521160-2efc4782-60e5-4238-b57e-67ff60d8f738.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New Company in search Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521284-82cc3883-b7dc-4d16-8ed8-112cc051d0bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name Required Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521312-35151509-1491-4481-8baf-75e9f991d37f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country Required Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521320-b0003b97-aa6a-4e30-9306-1eeff8ad4f61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Address Required Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521339-72a8c865-f4b6-4461-82d5-4b03d5b45ba8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>City Required Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521351-13517e6b-814b-4d78-b264-ac903db70f00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State Required Flash Message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205521385-628611de-f0cd-48b8-a043-99ca024e0abb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Added to the DB (ID 545)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522026-07f087e6-00bc-4985-aabd-0f97cae754f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Company Code Changes 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522043-da31ba32-3dad-4ed0-a244-d50110d33926.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Company Code Changes 2 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522054-8ed69078-36da-4559-9662-663c288f92fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Company Code Changes 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522914-a8b066e0-77fc-4e60-bada-7e1dc894dca0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Name Filter (Rangoni)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522918-ba59be41-7589-4966-b568-d2fe44a1d09d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Name FIlter (Rangoni) Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522922-cff34310-3b77-46fe-ba98-a5fcada48836.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country Filter Uruguay<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522931-54d421b5-8ee8-47f9-a942-1439f9223835.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country Filter Uruguay Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522939-cf760ed8-b048-430a-8703-c7cf56c40cbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State Filter CA<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522943-856df8b3-ebe5-4d32-8ba4-19a41688ff78.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State Filter CA Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522954-453bec0d-9a0b-4b04-9026-8e103d3b1e6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name Filter Asc<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522960-eab1197a-1203-48c3-9d4d-bedeec661f86.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name Filter Asc Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522967-335a3c29-5713-48dd-8c78-2d697e7f6db4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>City Filter Desc<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205522973-2b6970d2-49ac-4636-9064-ec8c7eb6f726.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>City Filter Desc Results<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205523359-1a9519ce-10ac-46f7-8328-f3d146ef5b3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Company Code Changes 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205523387-be56aba7-5106-4fb5-b2c0-94672a05d7f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Company Code Changes 2 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205523420-c241f5e7-2f3a-45af-b789-d558fa8c1b0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Company Code Changes 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205523959-f5c893cd-283b-415a-9993-15aad83cb7f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit Company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205523971-b9e14c4c-b077-4aa3-ab88-c11cd5653ac1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit Company Search Results<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524005-af85a070-8962-4beb-aa04-424e6f1af5c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit Company Search Results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524026-21395fe8-e947-416b-83df-17fb70487d95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Edit Company DB in VS code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524033-056e1ec1-fb77-48cc-bd0c-edc003eddbc4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Edit Company DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524409-eb1b2371-45b5-4744-86b7-c85df2828a73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Employee Code Changes <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524711-780bc434-8dec-43c1-80a3-f7106fe6ac17.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deleting employee with ID = 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524730-bbef7735-96c4-42c9-8fc2-36d6d5160087.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deleting Employee with ID = 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524755-15691a11-ab13-4410-863e-e7e43dee3697.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash Message for deleting employee successfully<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524424-051c2031-7e0d-421d-811c-080afa97878a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Company Code Changes <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524804-1048747a-4d60-4f49-b3ee-93046579ce6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Deleting Company with ID = 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524814-323e45e8-e9f9-4fae-a214-dfda53357e5e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deleting Company with ID = 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205524741-cd85a2ca-ed59-4702-a3b7-8905ff3ea8da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash Message for deleting company successfully<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/205514800-c4b337b9-2b0d-4994-ae3f-266eda2f135a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>29/29 Test Cases Passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">Mini Project-2 was by far the most challenging<br>assignment in the course. It required a knowledge of various applications such as<br>flask, HTML, Python and SQL. While working on this project I learnt the<br>basics of developing a simple web application through Flask. The Mini Project 2<br>was based on a Business Management Database, where the user can add, edit,<br>search for companies and their employees. This was a useful application and it<br>will definitely help me in my future courses.</p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/ka598" target="_blank">Grading</a></td></tr></table>
