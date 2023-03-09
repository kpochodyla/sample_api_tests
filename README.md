# API Test Project with Allure Report Generation

This project is an example of API testing with the Reqres API using Python's `requests` library, Pytest and Allure for report generation.
More focus has been put on creating detailed Allure reports that use as much of the Allure functionalities as possible. Therefore, the test scenarios implemented in this project may not cover all the possible use cases of the Reqres API but this project is still WIP.

## Requirements

To run this project, you need to have the following installed on your machine:

- Python 3.x
- Poetry
- Allure Command Line Interface

## Setup

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using Poetry: `poetry install`.

## Running Tests

1. Activate the virtual environment created by Poetry: `poetry shell`.
2. Run the script that executes test and generates allure report: `./run_test_and_make_report.sh`
This will run all the test, generate new report with trend graph and the configured properties of the report in `categories.json` and `environment.properties` files. The open the report you need to open `allure/allure-report/index.html` file. 
If you encounter a issue with the field not loading up, please take a look at this [known issue](https://github.com/allure-framework/allure2/issues/968) and the possible solutions for it. 

Alternatively for step 2 you can do:
2. Run Pytest to execute the tests: `pytest --alluredir=allure/allure-results`.
3. Generate an Allure report using the CLI: `allure serve allure/allure-results`.
