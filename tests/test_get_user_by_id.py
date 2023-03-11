import random

import allure
import src.common_steps as step


@allure.title("Retrieve Single User by ID with GET Request")
@allure.description_html(
    """
<h1>Test Scenario: Retrieve Single User by ID with GET Request</h1>

<h2>Objective</h2>

<p>To verify that the Reqres API can retrieve a single user by ID using a GET request, and that the response code and content are valid and accurate.</p>

<h2>Preconditions</h2>

<ul>
<li>The Reqres API is available and accessible.</li>
<li>Test data is available in the Reqres API for retrieving a single user by ID.</li>
</ul>

<h2>Test Steps</h2>

<ol>
<li>Send a GET request to the endpoint for retrieving a single user by ID using the Reqres API, specifying a valid user ID.</li>
<li>Verify that the response code returned is <code>200 OK</code>, indicating that the request was successful.</li>
<li>Verify that the response content returned is in JSON format.</li>
<li>Verify that the response content contains the expected user object.</li>
<li>Verify that the user object in the response contains the expected properties, such as <code>id</code>, <code>email</code>, <code>first_name</code>, <code>last_name</code> and <code>avatar</code>.</li>
<li>Verify that the values of the properties in the user object are accurate and match the test data in the Reqres API.</li>
</ol>

<h2>Expected Result</h2>

<ul>
<li>The GET request to retrieve a single user by ID should return a response code of <code>200 OK</code>.</li>
<li>The response content should be in JSON format and contain the expected user object.</li>
<li>The user object in the response should contain the expected properties and accurate values.</li>
</ul>
"""
)
def test_get_user_by_id(settings):
    # Pick random user
    sample_user = random.choice(settings.base_users)
    # Step 1: Send a GET request to retrieve a user data
    response = step.get_request(settings.base_url + f"/users/{sample_user['id']}")
    # Step 2: Verify that the response code is 200 OK
    step.check_status(response, 200)
    # Step 3: Verify that the response content returned is in JSON format
    step.check_headers(response, "Content-type", "application/json; charset=utf-8")
    # Step 4: Verify that the response content contains a user data objects
    response_data = response.json()
    step.check_field_in_data(response_data, "data")
    step.check_field_is_instance(response_data["data"], dict)

    # Step 5: Verify that the user object in the response contains the expected properties
    expected_properties = ["id", "email", "first_name", "last_name", "avatar"]
    step.check_properties_in_object(response_data["data"], expected_properties)

    # Step 6: Verify that the values of the properties in the user object are accurate and match the test data in the Reqres API.
    step.check_user_data(response_data["data"], sample_user)
