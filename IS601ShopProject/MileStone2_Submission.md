<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Kshitij Aji (ka598)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 6:09:36 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/ka598" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208302443-137d5cc2-c660-4140-b8db-a8cf15101a70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create Product Page from Admin Login<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208302461-26e6a226-059e-4802-b19d-6b9b0d9643c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid Data on the Create Product Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208302495-91dac51b-4ea2-4453-a320-182cf205a39a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Successfully Added Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208302512-55be4f68-c9b9-43f8-a566-47ee56e9965d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New Product created shows up on the Product List<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208302984-b0d01d58-b27e-4aa7-a698-bfdf0fb496ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop Products from Database (VSCode)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208302576-27327a2e-fd74-49e6-ad71-186c4434dc42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Products Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208302583-28318a36-b839-4ec2-85c5-914f9b2f1257.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products Page with View, Edit, Delete Option<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">To add items from the UI to the<br>database, a FlaskForm was first created that recorded details such as the item<br>id which was a hidden field, the name, stock, description, cost, image and<br>a submit form was included. A route was added to navigate to the<br>products page with the GET and POST Methods. A function was created for<br>this route called item which collected the data that was submitted to the<br>form. The validate_on_submit() function was used to record the values submitted by the<br>user and these values were used in the update query statements which directly<br>updated the product details to the database in the backend. Prior to creating<br>the FlaskForm a product table was created in SQL that is connected to<br>our database. For the layout of the product page, bootstrap CDN was used<br>and this was also added to the HTML page of our navbar.<span class="Apple-converted-space">&nbsp;</span></p><p<br>class="p2" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal;<br>font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><p class="p2" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch:<br>normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ka598-prod-fp.herokuapp.com">https://is601-ka598-prod-fp.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304311-b06ddb9d-e0a5-4ae7-98fa-c8240b1a8527.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logging In as a different user (Not Admin) <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304384-b6d7899d-e8c9-41c5-b0a7-2d81e9e2f2a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Page 1 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304406-035827df-c296-4216-8acd-00f6a97c190b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Page 2 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304420-57c088dd-88bc-4abc-b88a-e2db26030a05.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Page 3 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304427-4aed1415-d729-4ed9-82ff-9761263252f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Page 4 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304432-f1dbbd34-813e-4eaf-b0ba-126c28157f85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Page 5<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304447-c48aaf7f-567c-42af-b510-2425dfd9abee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Increase Quantity Filter (From Shop Page)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304468-2a077825-9350-4a84-b720-e79b6737e0af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product Decrease Quantity Filter (From Shop Page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">For a user to view the items in<br>the shop, a shop_list function was created where the selectAll query was used<br>to select all the items that are added to the Items table in<br>the database. An empty list named rows was first initialized and the selectAll<br>query was written in a try-except block. If the query was passed successfully,<br>the result was appended to the rows list. If there was an error<br>in selecting items a flash message was used to alert the user that<br>“There was an error in fetching the items”. A route was used to<br>access the shop items that used the GET and POST methods. In addition,<br>the @login_required was added before the function so that only logged-in users can<br>access the list of items in the shop. The user will be able<br>to increase and decrease the quantity from the shop page directly before adding<br>the product to the cart.<span class="Apple-converted-space">&nbsp;</span></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ka598-prod-fp.herokuapp.com">https://is601-ka598-prod-fp.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208305259-be3ca6d6-f33b-4082-a0fc-071c3ac5ad11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged In as Admin <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208305276-41d2d5d0-53c2-4494-a2d5-1d87cf5a4a6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products List Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208305324-60c1fbbe-976b-4e7a-83ae-9979d9b9319f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products List Page (More Sample Products)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208305296-fdbb9d85-401a-41a8-a79a-0d4d48ace584.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products List Page with View, Edit and Delete Filter <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208305344-e6cb40e4-f4ec-4453-9539-14fa1020ee5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Belt Item not visible in Shop Page (Stock set to 0)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208305369-47cfc5f9-c8f6-4789-974c-bf5d9fc1dc39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Belt Item visible in Products List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">For the admin to view, edit, create and<br>delete items from the Products page of the application, a function item was<br>created which referenced the FlaskForm ItemForm that was created in Forms.py. A route<br>was created to navigate through the shop/item page with the GET and POST<br>methods. The validation of admin login for this page was added by adding<br>the @admin_permission.require(http_exception=403) prior to the function. With this if the admin is not<br>logged in and the user tries to navigate to the products page, the<br>application will display the 403 page.<span class="Apple-converted-space">&nbsp; </span>The form.validate_on_submit() function was used collect<br>data from the admin/user when the form is submitted. To update the products<br>that already exist an update query was used to to update the the<br>items table in the database with the values entered in the form by<br>the admin. Similarly for adding new items to the database an insert query<br>was used to add the items based on the values submitted in the<br>form.<span class="Apple-converted-space">&nbsp;</span>For deleting items a separate function delete was created that used the<br>route with the GET and POST methods. The admin login was validated similar<br>to the item function described earlier. A delete query was used to delete<br>the item directly from the database based on the the item id collected<br>by the form. The function request.args.get("id") was used to collect the item id<br>from the user.<span class="Apple-converted-space">&nbsp;</span></p><p class="p2" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal;<br>font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ka598-prod-fp.herokuapp.com">https://is601-ka598-prod-fp.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306439-b965c8ea-727f-43a3-b04e-24ad3be0e9e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin Products List Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306450-d914a1f8-740e-44c4-b393-0ca43316a554.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products List Page with View, Edit, Delete options <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306463-db0e235d-8cac-4a35-a9b1-1fb9e7f650cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit Product Page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306626-f76ab448-e6c1-4043-9301-3a80a110f4f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Editing the Name of the Product (Wireless Gaming Headphones)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306644-ed2c49b5-137a-47cf-91ef-8d20fdd20a64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Changing the Name to Wireless Headphones<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306653-24e80b71-36e9-4995-bbf7-3a46fa8ea6a2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful Update Flash Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306690-17f750c4-6006-45fa-8a98-00554fafba8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product List Before Editing Name of the Product <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306666-c8e3b335-000b-454b-b174-a403a6847685.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product List showing new name Wireless Headphones<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208304384-b6d7899d-e8c9-41c5-b0a7-2d81e9e2f2a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop Page before changing Name of the product<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208306678-530df76f-c33c-4333-8398-81cb40e38b96.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop Page showing the New Name of the Product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">For the admin to edit products from the<br>product page, within the item function, the flask form ItemForm that was created<br>earlier is referenced in this function. This function uses the GET and POST<br>methods in its route. The admin permission is validated by adding @admin_permission.require(http_exception=403) before<br>the function. The form.validate_on_submit() function validates the data that is submitted by the<br>user/admin. To make edits to the product page, the DB.update function is used<br>and the<span class="Apple-converted-space">&nbsp; </span>update query is inserted in this function. The query uses<br>the user inputs from the form to update the products table in the<br>database. If the update is successful, the application displays a success flash message<br>and if there is an error in editing the products page, the application<br>displays an error message and a danger flash message.</p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ka598-prod-fp.herokuapp.com">https://is601-ka598-prod-fp.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ka598-prod-fp.herokuapp.com">https://is601-ka598-prod-fp.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307041-5523bdcd-884e-4f29-bf91-d11d69ed0cf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added Item to Cart with a successful flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307055-26fed79a-852e-4adc-a69e-f56f2d52824f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unable to access the Cart URL without logging in <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307081-4aeea476-dc21-463c-a58d-2e1ddff9a457.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Table from Database with Valid Records <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">A function was created to handle all the<br>processes related to the cart. A route with the GET and POST methods<br>was used to navigate to the cart tab in the application. User login<br>was validated by adding the @login_required prior to the cart function. This way<br>if a user that is not logged in will not be able to<br>access the cart by using the route for the cart tab of the<br>application. The request.form.get() function was used to collect information about the products from<br>the user such as the quantity and the item id of the product.<br>For the front-end perspective of the cart, a html page was created for<br>the cart which had the table heading tags of Product, Quantity, Subtotal, and<br>Actions. This page was then returned in the cart function using the return<br>render_template function.</p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">For Adding items to the cart, the cart<br>function created earlier is used. First, the user id of the logged-in user<br>is collected with the current_user.get_id() function. If the quantity selected is greater than<br>0, the cost and name of the chosen product is selected from the<br>items database with the SELECT query. The items in the cart are then<br>updated with the UPDATE query which uses the item id, quantity and cost<br>from the result of the earlier SELECT query. If the update query passes<br>successfully then a flash message is displayed otherwise the user is alerted that<br>there was an error updating the cart. If an item was not added<br>to the cart previously, then an INSERT query is used on the cart<br>table where the inputs of the query are id, quantity, cost ad user_id<br>are taken from the results of the earlier query.</p><p class="p2" style="text-align: justify; margin-bottom:<br>0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica<br>Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307323-2dc33766-1f47-4347-9245-5d6a3039d812.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart View with subtotal and cart total correctly calculated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307333-aacca116-efcd-4415-8aae-cacab07decab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart View with subtotal and cart total correctly calculated (Updated Watch Quantity to<br>2 and Subtotal updates to 80 correctly)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">The cart function has the @login_required<span class="Apple-converted-space">&nbsp; </span>prior<br>to the cart function which ensures that only logged in users can access<br>the cart. In the purchase function, the total cost, quantity, cart, and order<br>variables are first initialized.<span class="Apple-converted-space">&nbsp; </span>A Select query is used to get the<br>cart id, item id, name, quantity, stock, cost and (quantity * cost) is<br>used in the query to get the subtotal cost of the items. The<br>Cart table is joined with the Items table with the join condition being<br>Cart.Item_Id = Item.item_id. This select query is stored in a variable called result.<br>The result.rows method is used to display each cart item with their subtotals<br>as rows. A for loop is used to iterate through each item in<br>the cart, and the total and quantity variables are incremented for each item.<br>The total variable is the cart total cost for each subitem with their<br>updated quantities. If there are no errors in the query and there are<br>no exceptions, the logged in user will be able to view subtotal for<br>each line item and the total cost of all items.</p><p class="p2" style="text-align: justify;<br>margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family:<br>&quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ka598-prod-fp.herokuapp.com">https://is601-ka598-prod-fp.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307323-2dc33766-1f47-4347-9245-5d6a3039d812.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Before Updating Quantity<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307333-aacca116-efcd-4415-8aae-cacab07decab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart After Updating Quantity (Updated Watch Quantity to 2)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307875-54cc47ac-c129-478a-8a91-352bc3b7aa42.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page Before <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307884-9598a110-e04b-48ac-819e-66caeb4f50c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page After setting Phone Quantity to 0 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208307923-9fbf7057-d27e-400d-a625-595124201add.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page after updating Phone Quantity to 0 <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208308150-2952e885-0720-4aa4-a9f7-7284f4e353a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page Before setting Quantity to negative <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208308206-3d7f7b78-ddba-4990-b43e-e2b438fd1897.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page after setting Quantity to negative (for Wireless Headphones)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208308234-a56ea9d1-c3e2-4b1e-9faf-643ab6c5fbf2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page after updating the negative quantity  (for Wireless Headphones)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">For Adding/removing items to the cart, the cart<br>function created earlier is used. If the quantity selected is greater than 0,<br>the cost and name of the chosen product is selected from the items<br>database with the SELECT query. The items in the cart are then updated<br>with the UPDATE query which uses the item id, quantity and cost from<br>the result of the earlier SELECT query. Similarly, if the quantity selected is<br>less than 0 or negative which is the else condition in the function,<br>a DELETE query is used to delete the selected item from the cart<br>based on the item id and user id values. If the delete query<br>is passed successfully, the application passes a flash message saying that the item<br>is deleted from the cart.<span class="Apple-converted-space">&nbsp;</span></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208308486-258dde36-538e-4a76-9d9b-9551b8055d06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page Before deleting Items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208308501-379b44fa-3b42-4f91-a481-adee8f4b13c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page After Removing Pixel 7 Pro Smartphone<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208308486-258dde36-538e-4a76-9d9b-9551b8055d06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page Before Clearing Items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113541321/208308546-1f428f5b-e7dc-4df9-b559-5cc89ea1aedd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart Page After Clearing All Items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <div style="text-align: justify; "><span style="font-family: &quot;Helvetica Neue&quot;; font-size: 13px;">For deleting items from the<br>cart, we use the cart function. If the quantity selected by the user<br>is less than 0 or negative which is the else condition in the<br>function, a DELETE query is used to delete the selected item from the<br>cart based on the item id and user id values. If the delete<br>query is passed successfully, the application passes a flash message saying that the<br>item is deleted from the cart. If there is an error or an<br>exception, the application displays a warning message to the user.</span><span class="Apple-converted-space" style="font-family: &quot;Helvetica<br>Neue&quot;; font-size: 13px;">&nbsp;</span><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Kshitij2126/IS601-007/pull/24">https://github.com/Kshitij2126/IS601-007/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p class="p1" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">There were a few issues while trying to<br>deploy the application to Heroku. My project folder had a few test files<br>which were referencing an earlier part of the lesson which I had deleted/commented<br>so while deploying my tests were failing. I later removed these tests and<br>my application was able to deploy to heroku. From the heroku platform, I<br>tried to register/login to the shop application but I was not able to<br>login or register an account. This was because I had forgotten to add<br>the DB_URL string information to the config vars in the app for Heroku.<span<br>class="Apple-converted-space">&nbsp;</span></p><p class="p2" style="text-align: justify; margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size:<br>13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><p class="p1" style="text-align: justify; margin-bottom: 0px;<br>font-variant-numeric: normal; font-variant-east-asian: normal; font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;;">In<br>this Milestone we created an online shopping web based application where a user<br>is able to register and login to the account. The application has an<br>admin level superuser that can add/edit/delete products from the shop. The admin can<br>also update the stock and price of the items. The application let the<br>admin add pictures for each product which improved the layout and user experience<br>of this website. The user can add items to the cart and make<br>purchases. The application should be able to calculate the correct totals and subtotals<br>for the cost of the items and subitems based on their quantity. This<br>was a very useful application and I did get to learn a lot<br>from this lesson. This project integrated a lot of previous lessons from SQL,<br>Flask, Flask_login, WTForms, jinja templates and connecting forms in the front end of<br>the application to the database in the backend. I will try to work<br>on my own flask applications over the winter break but I still have<br>a lot more to learn.<span class="Apple-converted-space">&nbsp;</span></p><p class="p2" style="margin-bottom: 0px; font-variant-numeric: normal; font-variant-east-asian: normal;<br>font-stretch: normal; font-size: 13px; line-height: normal; font-family: &quot;Helvetica Neue&quot;; min-height: 15px;"><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ka598-prod-fp.herokuapp.com">https://is601-ka598-prod-fp.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/ka598" target="_blank">Grading</a></td></tr></table>
