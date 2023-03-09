## Test Scenario: Retrieve Single User by ID with GET Request

### Objective

To verify that the Reqres API can retrieve a single user by ID using a GET request, and that the response code and content are valid and accurate.

### Preconditions

- The Reqres API is available and accessible.
- Test data is available in the Reqres API for retrieving a single user by ID.

### Test Steps

1. Send a GET request to the endpoint for retrieving a single user by ID using the Reqres API, specifying a valid user ID.
2. Verify that the response code returned is `200 OK`, indicating that the request was successful.
3. Verify that the response content returned is in JSON format.
4. Verify that the response content contains the expected user object.
5. Verify that the user object in the response contains the expected properties, such as `id`, `email`, `first_name`, `last_name` and `avatar`.
6. Verify that the values of the properties in the user object are accurate and match the test data in the Reqres API.

### Expected Result

- The GET request to retrieve a single user by ID should return a response code of `200 OK`.
- The response content should be in JSON format and contain the expected user object.
- The user object in the response should contain the expected properties and accurate values.
