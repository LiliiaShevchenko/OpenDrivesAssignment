# OpenDrivesAssignment
This is a Test Automation Framework for OpenDrives

### Used
[![Python](https://img.shields.io/badge/python-green.svg)]()
[![Selenium](https://img.shields.io/badge/selenium-blue.svg)]()
[![Pytest](https://img.shields.io/badge/pytest-yellow.svg)]()

### How it works
clone project to your local 
install requirements via pip install -r requirements.txt

### To run the tests
python -m pytest -v -s test.py

### To run tests with a report 
python -m pytest -v -s --alluredir="path to project\report" test.py
cd path to local project folder
allure serve report