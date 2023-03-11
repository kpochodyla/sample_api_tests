import requests

import allure
import src.common_steps as step


@allure.step("Register User")
def register_user(user: dict, data: dict()) -> None:
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
