# OpenDrivesAssignment
This is a Test Automation Framework for OpenDrives

### Used
[![Python](https://img.shields.io/badge/python-blue.svg)]()
[![Selenium](https://img.shields.io/badge/selenium-blue.svg)]()
[![Pytest](https://img.shields.io/badge/pytest-blue.svg)]()

### How it works
clone project to your local 
install requirements via pip install -r requirements.txt

## Modes for running test cases:
### Simple run:
python -m pytest -v -s test_homepage.py

### Run only specified tests
python -m pytest -v -s -k 'name of test case'

### Run with reports
python -m pytest -v -s --html=report.html