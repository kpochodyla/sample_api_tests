import random

import allure
import src.common_steps as step
import src.preconditions_steps as precondition


@allure.title("Logout user with POST Request")
@allure.description_html(
    """
<h1>Test Scenario: Logout User with POST Request</h1>

<h2>Objective</h2>
<p>To verify that the Reqres API can logout a user using a POST request, and that the response code and content are valid and accurate.</p>

<h2>Preconditions</h2>
<ul>
  <li>The Reqres API is available and accessible.</li>
  <li>Test data is available for logging out a logged in and registered user.</li>
</ul>

<h2>Test Steps</h2>
<ol>
  <li>Send a POST request to the endpoint for logging out a user using the Reqres API, including valid test data in the request body.</li>
  <li>Verify that the response code returned is <code>200 OK</code>, indicating that the request was successful.</li>
  <li>Verify that the response content returned is in JSON format.</li>
</ol>

<h2>Expected Result</h2>
<ul>
  <li>The POST request to login a user should return a response code of <code>200 OK</code>.</li>
  <li>The response content should be in JSON format and contain the expected property.</li>
</ul>

"""
)
@allure.link("https://kpochodyla.github.io/sample_api_tests/test_scenarios/test_logout_user", name="Logout user with POST Request")
def test_logout_user(settings):
    # Pick random user
    sample_user = random.choice(settings.base_users)
    # Prepare request data
    data = {
        "username": sample_user["email"],
        "email": sample_user["email"],
        "password": sample_user["first_name"],
    }
    # Register User
    precondition.register_user(settings.base_url, sample_user, data)
    # Login User
    precondition.login_user(settings.base_url, sample_user, data)
    # Step 1: Send a POST request to logout a user
    response = step.post_request(settings.base_url + "/logout")
    # Step 2: Verify that the response code is 200 OK
    step.check_status(response, 200)
    # Step 3: Verify that the response content returned is in JSON format
    step.check_headers(response, "Content-type", "application/json; charset=utf-8")
