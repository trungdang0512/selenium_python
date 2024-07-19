# Selenium Boilerplate
This is a boilerplate for running selenium tests with python. It supports to run the test on Chrome, Firefox, MS Edge. 
# Getting started
This boilerplate requires both selenium, python, allure
- Python 3.9+
- Selenium 4+
- Allure
# Run test via command line

```
pytest tests/test_example.py --browser=chrome
```

Headless mode
```
pytest tests/test_example.py --browser=chrome --headless
```