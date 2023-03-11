# Test Scenario: Login User with POST Request

## Objective
To verify that the Reqres API can login a user using a POST request, and that the response code and content are valid and accurate.

## Preconditions
- The Reqres API is available and accessible.
- Test data is available for logging in a registered user.

## Test Steps
1. Send a POST request to the endpoint for logging in a user using the Reqres API, including valid test data in the request body.
2. Verify that the response code returned is `200 OK`, indicating that the request was successful.
3. Verify that the response content returned is in JSON format.
4. Verify that the response content contains the expected `token` property.

## Expected Result
- The POST request to login a user should return a response code of `200 OK`.
- The response content should be in JSON format and contain the expected property.
