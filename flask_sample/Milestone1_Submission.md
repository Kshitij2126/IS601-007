<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Kshitij Aji (ka598)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2022 5:33:05 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ka598" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206909836-073cea6e-e918-4a4f-98b3-2a28c91ba84e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Not Available Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206909862-3afae5a8-1e38-4fdc-af38-ec15f40cc29a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username Not available Flash Message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206909914-099fc1a7-551e-4f79-baad-803957684be6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Validation Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206909930-890ff67d-3c67-4d57-8305-70ec98393e80.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Validation Message 2 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206909955-cfaa12dd-fc85-43a6-a749-fea69ccaadcc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Validation Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206909977-ad8292cc-49b5-4d6e-9756-4627e2e54475.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Must Match Validation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206910000-ec670083-782c-4b98-8067-c88cf9719bc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form Details Before Submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206910020-2e5df51b-0901-4caf-b10c-f5cac40122db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Registration<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206910303-42aed1e9-c66c-4938-ae7f-674e34c3faf4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users Table Screenshot with marktwain user added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/22">https://github.com/Kshitij2126/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">To handle the login pages, Flask-login was used.<br>Flask-login can provide user session management for a flask web application. It has<br>the capability to handle common tasks of user logging in, logging out and<br>remembering each user’s sessions over extended periods of time. Flash messages were also<br>used to handle the validation logic for these forms. For example if the<br>user enters an email that was entered previously, the application will display a<br>Flash Message that the “Email is not available”. Similarly, if the user enters<br>a username that was saved previously, the flash message: “Username is not available”<br>is displayed. For the frontend part of the application, few html pages were<br>created to handle the login form of the user. The login.html page extends<br>from the layout.html The render_field function was used to access the email and<br>password from the user.<span class="Apple-converted-space">&nbsp;</span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206910697-42ebe0c3-8320-4362-bd67-24019ec9e14f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Mismatch Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206910708-bba73d70-d1a5-4273-94f6-acfe95ee74f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation Based on Non-Existing User<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206910766-ae0b0b92-b57e-419e-84e7-8a80c0e61304.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Login Message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/22">https://github.com/Kshitij2126/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">Similar to deliverable 1, flask-login was used to<br>handle the user login and registration pages. Flask-login stores the active user ids<br>in the flask session that lets us easily log them in and out<br>of the application. The form first collects the password from the user, and<br>Bcrypt from flask is used to create a hash of the password to<br>encrypt it. The email, username and password that the user enters in the<br>form pages is stored and inserted into the database. For the password only<br>a hash of the password is inserted, that way the password is only<br>known to the user.<span class="Apple-converted-space">&nbsp;</span></p><p class="p2" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian:<br>normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><p class="p1"<br>style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">To check for duplicate usernames and emails, a check duplicate<br>function was created, where the re.match function was used. If there is a<br>match, the application displays a flash message if there is a match on<br>the username or the email. If there is no match, and the user<br>can register, the application displays a flash message: “Successfully Registered”.<span class="Apple-converted-space">&nbsp;</span></p><p class="p2" style="text-align:<br>justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal;<br>font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian:<br>normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">While logging in, the<br>user types in a username and password. In the backend this is checked<br>with the username and the hash of the password in the database. If<br>there is a match with what the user typed and the database values,<br>the user will be able to login to the application.</p><p class="p2" style="text-align: justify;<br>margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family:<br>&quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206911284-1c5929dd-086d-4b82-8d91-16a6b1cd3700.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Logout Message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206911305-9da84d3e-fd82-46b7-830a-2c1434fd573a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Cannot Access other Pages without Logging In<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206911331-317d6f5c-53ad-4fa0-8929-598679c00437.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User has to Register/Login to Access other Pages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206924844-1338ce68-da4f-4512-8b67-aaa521f7cf24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cannot Access Roles Page without Logging In <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206924871-aa16dc56-d669-47f8-8877-640409afe815.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cannot Access Profile Page without Logging In <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206924887-5dfd5da8-be75-465c-8752-aa6e6c771762.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Profile Page After Logging In <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/22">https://github.com/Kshitij2126/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">For the logout pages, Flask-Principal was used. Flask-Principall<br>provides a framework to combine providers of two types of service, which are<br>often located in different parts of a web application. They are Authentication Providers<br>and User Information Providers.<span class="Apple-converted-space">&nbsp; </span>A logout function was used and the session<br>keys set by Flask-Principal were removed. After the user was logged out, the<br>application displayed a custom flash message: “Successfully Logged Out” and the web page<br>is redirected to the login page. The user is also not permitted to<br>visit any other pages prior to registering and logging in to the application.<span<br>class="Apple-converted-space">&nbsp;</span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206923925-f88832f6-278c-466f-922b-fc6f51c63f61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Cannot Access Login Protected Page (Roles)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206924065-66dbce69-27d2-4ed3-9a0e-b0e04a4058eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Cannot Access Roles Page if User is not an Admin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206924638-9fc3ee02-64d4-4ee2-ae8e-1539b66fe1f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles Tab Available After Logging In as Admin <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206924672-43f8fe9e-96b2-4759-a9ac-f78c5af2dd6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles Tab Not Available After Logging In as a Regular User <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206918698-ed655782-9e0b-4697-9fc5-0196c877c4c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles Table From Database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206918747-cea810de-5b43-4b87-9bb6-2ac214813454.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles List From Website<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206918718-6219afba-726e-4cce-b08c-3f236a525285.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles From Database <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206918758-5548ea40-c7f5-4b04-bc4b-ad31eba1f599.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin Role From Website (user: kshitij is the admin)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206918788-24839f0e-2b08-47f6-91f2-eb96a83e8e0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Assigned Roles 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206918801-e919f3dd-1110-4718-885d-36df27513aad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Assigned Roles 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/22">https://github.com/Kshitij2126/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">For the login pages, login_user, login_required, logout_user, current_user<br>were imported from flask-login. flask-login was used to handle the user login and<br>registration pages. Flask-login stores the active user ids in the flask session that<br>lets us easily log them in and out of the application. Flash messages<br>were also used to handle the validation logic for these forms. The form<br>first collects the password from the user, and Bcrypt from flask is used<br>to create a hash of the password to encrypt it. The email, username<br>and password that the user enters in the form pages is stored and<br>inserted into the database. For the password only a hash of the password<br>is inserted, that way the password is only known to the user. To<br>check for duplicate usernames and emails, a check duplicate function was created, where<br>the re.match function was used. If there is a match, the application displays<br>a flash message if there is a match on the username or the<br>email. If there is no match, and the user can register, the application<br>displays a flash message: “Successfully Registered”.<span class="Apple-converted-space">&nbsp;</span></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">For the roles pages, admin_permission was imported from<br>roles.permissions and RoleForm was imported from roles.forms. The roles section of the application<br>was created in a way such that only the user defined as an<br>admin was able to add, list and assign roles from the roles tab<br>of the application. A regular user will not be able to see the<br>roles tab in the application. Different methods for roles were defined such as<br>add, edit, list, delete, assign and apply. For the add function, a new<br>role is added directly into the database as an SQL query and if<br>the role can be created, the application displays a flash message, “Role Created<br>Successfully”.<span class="Apple-converted-space">&nbsp; </span>If an exception occurs, the application displays a flash message: “Error<br>creating role”.<span class="Apple-converted-space">&nbsp; </span>For the edit function, if the user that is predefined<br>as an admin, wants to edit a role, the form.validate_on_submit() checks that the<br>user is an admin.<span class="Apple-converted-space">&nbsp;</span>All the functions check if the user is an<br>admin prior to modifying/updating roles. This is done by adding the following route<br>prior to each function: @admin_permission.require(http_exception=403)</p><p class="p2" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian:<br>normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916412-742b5dfe-fc88-4369-9472-6ae2999e2199.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Home Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916453-d82308fd-8adc-4da4-a580-9fb351b5dbe0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916478-4993b1bc-8407-4618-a03f-8973cb0dde40.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Sample Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916489-eea941fe-7528-4d6a-bfea-3018a86537f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>List Samples Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916516-c621240c-0af7-4c11-a6e4-0016b63358e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Roles Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916521-18ac8b3b-6d5c-436c-b614-468183a94026.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>List Roles Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916541-18a48806-b5f4-4f92-978d-da39aa0b976c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Assign Roles Page 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916564-c729a8e1-cbf5-4cf9-a6c1-05dc57ee7bd3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Assign Roles Page 2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916585-0c8175ff-5262-4f9d-956e-465d4cf77820.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Assign Roles Page 3 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206916598-b45f011a-2f60-4f2a-8649-2db2494d241a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logout Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/22">https://github.com/Kshitij2126/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">To handle the basic styling of the web<br>pages, content delivery networks(cdn) from bootstrap were used. A CDN is a distributed<br>group of servers that can work together to provide fast delivery of internet<br>content. This allows for a<span class="Apple-converted-space">&nbsp;</span>quick transfer of assets needed for loading Internet<br>content including HTML pages, javascript files, stylesheets, images, and videos. The popularity of<br>CDN services continues to grow, and today the majority of web traffic is<br>served through CDNs, including traffic from major sites like Facebook, Netflix, and Amazon.<br>There are a lot of benefits to using CDNs: They improve website load<br>times, reduce bandwidth costs, increase content availability and redundancy. For designing most of<br>the frontend pages, Bootstrap was used. Bootstrap is a free open-source CSS framework<br>directed at responsive, mobile-first front-end web development. It contains HTML, CSS and JavaScript-based<br>design templates for typography, forms, buttons, navigation, and other interface components.</p><p class="p2" style="text-align:<br>justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal;<br>font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917271-59354b56-9be1-41e0-a84b-683e4d6c1e0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username Not Available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917281-a492b23c-8df1-47ad-a6f6-50a46bfa828b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Not Available  at Registration<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917295-7efd8474-bdf9-41d0-954e-4eb0a87e9d88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Must Match At Registration<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917303-52955a9f-e9fb-4805-b854-4d0170157819.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Password at Login <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917317-da36344d-e5e5-4d57-be61-7b6dc2baf623.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid User at Login <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917378-76e82e94-a35e-443b-b309-0c49d16928fe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email not Available at Profile Updation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917438-f8f43fdd-b63b-423a-983c-e9e09106cd4f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Validation Message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917460-db1dbab9-845e-42e6-b208-615285ee45a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Must Match Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917482-7c82e14e-d43e-4574-b8ca-1ba70e3a02bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Invalid Username Formate Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917522-18a692ac-fa4d-4988-9ec3-3316ef9e52d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile Saved Message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206917538-0e7f3b68-8d73-4e3a-83d1-36ad0b33c64a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Logout Message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/22">https://github.com/Kshitij2126/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">To handle technical messages and converting them to<br>being friendly to our users, flash messages were used.<span class="Apple-converted-space">&nbsp;</span>Feedback is very important<br>to make good applications and smooth user interfaces. If the user does not<br>get enough feedback they will probably not understand how to use the application.<br>Flask provides a really simple way to give feedback to a user with<br>the flashing system. The flashing system basically makes it possible to record a<br>message at the end of a request and access it next request and<br>only next request. This is usually combined with a layout template that does<br>this. Sometimes browsers and web servers enforce a limit on cookie sizes. This<br>means that flashing messages that are too large for session cookies causes message<br>flashing to fail silently.</p><p class="p2" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal;<br>font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206912076-f229b3ed-a4d3-4336-beee-c72a492fc715.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Can See Profile Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/22">https://github.com/Kshitij2126/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">To retrieve the data is retrieved about the<br>user and display the profile section in the form, the profile function is<br>added. The .get_id() function is used to get the userid from the user.<br>If the validate_on_submit() function is found to be true, the profile page pre<br>fills the data such as username, emailId and password. The user that is<br>logged in can change his/her profile information and update the username, email and<br>password in this page.<span class="Apple-converted-space">&nbsp;</span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206914048-429d48c7-c3ca-414e-b67c-50abe66309a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username Validation Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206914088-4ab6a4f0-0bfc-4818-a040-61c846b81141.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username Not Available Message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206914109-b67250c8-4ead-45f9-9d29-6f0440cf1200.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Not Available Message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206914128-543a1b01-5e38-45a0-8181-f877e9c12bb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Validation Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206914143-5a53315e-dcf1-46f1-b0a2-8a7768e6cc5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Must Match Message <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206914162-07c2a3c4-d53f-4cf9-88cf-a83612b1ad0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Updation Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206914190-2d9d8d47-4315-41ea-9434-cd2fec14ea37.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username Validation Message 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206912076-f229b3ed-a4d3-4336-beee-c72a492fc715.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Profile Updation <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/206914209-89625f59-47e5-42ff-b0c8-c3a32ba79727.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Profile Updation (Username)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/22">https://github.com/Kshitij2126/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">To retrieve the data is retrieved about the<br>user and display the profile section in the form, the profile function is<br>added. The .get_id() function is used to get the userid from the user.<br>If the validate_on_submit() function is found to be true, the profile page pre<br>fills the data such as username, emailId and password. The user that is<br>logged in can change his/her profile information and update the username, email and<br>password in this page. The profile function only handles the password change if<br>all three: current_password, password and confirm, are provided by the user. When the<br>password is successfully updated, the application displays a flash message: “Updated Password” and<br>if it cannot be updated the application displays a flash message “Invalid Password”.<span<br>class="Apple-converted-space">&nbsp; </span>The profile page also checks for duplicate email and username from the<br>database. If there is a duplicate, the application will not let the user<br>update their email or username to an already existing username or email in<br>the database.</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height:<br>normal; font-family: &quot;Helvetica Neue&quot;;">In this Milestone, we learnt about the basics of setting<br>up a simple web-based flask application. We learnt how to use flask-login and<br>WTForms to create pages that register, log in, and log out users. We<br>also learnt about creating and defining roles to create association tables between users<br>and roles. This application used MySQL to connect to a database and add<br>user data to the database. In addition to that, we used flash messages<br>to make the messages more user-friendly and to make<span class="Apple-converted-space">&nbsp;</span></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ka598-prod.herokuapp.com/login">https://is601-ka598-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ka598" target="_blank">Grading</a></td></tr></table>
