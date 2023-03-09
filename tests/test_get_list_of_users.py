import allure
import src.common_steps as step


@allure.title("Retrieve List of Users with GET Request")
@allure.description_html(
    """
<h1>Test Scenario: Retrieve List of Users with GET Request</h1>

<h2>Objective</h2>

<p>To verify that the Reqres API can retrieve a list of users using a GET request, and that the response code and content are valid and accurate.</p>

<h2>Preconditions</h2>

<ul>
    <li>The Reqres API is available and accessible.</li>
    <li>Test data is available in the Reqres API for retrieving a list of users.</li>
</ul>

<h2>Test Steps</h2>

<ol>
    <li>Send a GET request to the endpoint for retrieving a list of users using the Reqres API.</li>
    <li>Verify that the response code returned is <code>200 OK</code>, indicating that the request was successful.</li>
    <li>Verify that the response content returned is in JSON format</li>
    <li>Verify that the response content contains a list of user objects.</li>
    <li>Verify that each user object in the response contains the expected properties, such as <code>id</code>, <code>email</code>, and <code>first_name</code>.</li>
    <li>Verify that the values of the properties in each user object are accurate and match the test data in the Reqres API.</li>
    <li>Verify that the response content contains the expected number of user objects, based on the test data in the Reqres API.</li>
</ol>

<h2>Expected Result</h2>

<ul>
    <li>The GET request to retrieve a list of users should return a response code of <code>200 OK</code>.</li>
    <li>The response content should be in JSON format and contain a list of user objects.</li>
    <li>Each user object in the response should contain the expected properties and accurate values.</li>
    <li>The response content should contain the expected number of user objects.</li>
</ul>
"""
)
def test_retrieve_users(settings):
    # Step 1: Send a GET request to retrieve a list of users
    response = step.get_request(settings.base_url + "/users")
    # Step 2: Verify that the response code is 200 OK
    step.check_status(response, 200)
    # Step 3: Verify that the response content returned is in JSON format
    step.check_headers(response, "Content-type", "application/json; charset=utf-8")
    # Step 4: Verify that the response content contains a list of user objects
    response_data = response.json()
    step.check_field_in_data(response_data, "data")
    step.check_field_is_instance(response_data["data"], list)

    # Step 5: Verify that each user object in the response contains the expected properties
    expected_properties = ["id", "email", "first_name", "last_name", "avatar"]
    for field in response_data["data"]:
        step.check_properties_in_object(field, expected_properties)

    # Step 6: Verify that the values of the properties in each user object are accurate and match the test data in the Reqres API
    for user, expected_user in zip(response_data["data"], settings.base_users):
        step.check_user_data(user, expected_user)

    # Step 7: Verify that the response content contains the expected number of user objects
    expected_num_users = len(settings.base_users)
    step.check_values_are_equal(len(response_data), expected_num_users)
