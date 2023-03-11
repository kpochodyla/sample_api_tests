import random

import allure
import src.common_steps as step


@allure.title("Register user with POST Request")
@allure.description_html(
    """
  <h1>Test Scenario: Register user with POST Request</h1>
  <h2>Objective</h2>
  <p>To verify that the Reqres API can create a new user using a POST request, and that the response code and content are valid and accurate.</p>
  <h2>Preconditions</h2>
  <ul>
    <li>The Reqres API is available and accessible.</li>
  </ul>
  <h2>Test Steps</h2>
  <ol>
    <li>Send a POST request to the endpoint for registering a user using the Reqres API, including the test data in the request body.</li>
    <li>Verify that the response code returned is <code>200 OK</code>, indicating that the request was successful.</li>
    <li>Verify that the response content returned is in JSON format.</li>
    <li>Verify that the the response contains the expected properties, such as <code>id</code> and <code>token</code>,</li>
    <li>Verify that the values of the <code>id</code> property in the response is accurate and match the test data in the request.</li>
  </ol>
  <h2>Expected Result</h2>
  <ul>
    <li>The POST request to register a new user should return a response code of <code>200 OK</code>.</li>
    <li>The response content should be in JSON format and contain the expected data for the registered user.</li>
    <li>The data in the response should contain the expected properties and accurate values.</li>
  </ul>
"""
)
def test_register_user(settings):
    # Pick random user
    sample_user = random.choice(settings.base_users)
    # Prepare request data
    data = {
        "username": sample_user["email"],
        "email": sample_user["email"],
        "password": sample_user["first_name"] 
    }
    # Step 1: Send a POST request to register a users
    response = step.post_request(settings.base_url + "/register", data)
    # Step 2: Verify that the response code is 200 OK
    step.check_status(response, 200)
    # Step 3: Verify that the response content returned is in JSON format
    step.check_headers(response, "Content-type", "application/json; charset=utf-8")
    response_data = response.json()
    # Step 4: Verify that the data in the response contains expected properties
    expected_properties = ["id", "token"]
    step.check_properties_in_object(response_data, expected_properties)
    # Step 5: Verify that the values of the id property in the data object is accurate and match the test data in the Reqres API.
    step.check_values_are_equal(sample_user["id"], response_data["id"])
