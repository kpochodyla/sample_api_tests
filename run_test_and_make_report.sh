#!/bin/bash
rm -r allure/allure-results/
pytest --alluredir=allure/allure-results
cp -r allure/allure-report/history allure/allure-results/history
cp allure/categories.json allure/allure-results/categories.json
cp allure/environment.properties allure/allure-results/environment.properties
allure generate allure/allure-results --clean -o allure/allure-report
cp -r allure/allure-report allure-report
