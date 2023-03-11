import requests

import allure


@allure.step("Send GET request")
def get_request(url: str) -> requests.Response:
    response = requests.get(url=url)
    return response


@allure.step("Send POST request")
def post_request(url: str, data: dict) -> requests.Response:
    response = requests.post(url=url, data=data)
    return response


@allure.step("Check response status code")
def check_status(response: requests.Response, status_code: int) -> None:
    assert (
        response.status_code == status_code
    ), f"Expected status code {status_code}, but got {response.status_code}"


@allure.step("Check response headers")
def check_headers(response: requests.Response, headers_name: str, headers: str) -> None:
    assert (
        response.headers[headers_name] == headers
    ), f"Expected Content-Type header of {headers}, but got {response.headers[headers_name]}"


@allure.step("Check if field in response data")
def check_field_in_data(response_data: dict, field_name: str) -> None:
    assert (
        field_name in response_data
    ), f"Response data should contain a {field_name} field"


@allure.step("Check if field is a specific instance")
def check_field_is_instance(field, instance) -> None:
    assert isinstance(field, instance), f"Expected field to be a {instance}"


@allure.step("Check expected properties in object")
def check_properties_in_object(object: dict, expected_properties: list) -> None:
    for prop in expected_properties:
        assert (
            prop in expected_properties
        ), f"Expected property {prop} in object, but it is not present"


@allure.step("Check user data")
def check_user_data(user: dict, expected_user: dict) -> None:
    assert user["id"] == expected_user["id"]
    assert user["email"] == expected_user["email"]
    assert user["first_name"] == expected_user["first_name"]
    assert user["last_name"] == expected_user["last_name"]
    assert "avatar" in user


@allure.step("Check if values are equal")
def check_values_are_equal(first_value, second_value) -> None:
    assert (
        first_value == second_value
    ), f"Expected {first_value} to equal {second_value}"
