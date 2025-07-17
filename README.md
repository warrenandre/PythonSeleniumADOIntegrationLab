
# Page Object Model (POM) in Selenium Python

Page-object-model (POM) is a pattern that we can apply it to develop efficient automation framework. Basically in page-object we create base class which includes basic functionalities for every pages .create page class file for each web page. This class file consists of different web elements present on the web page. Moreover, the test scripts then use these elements to perform different actions. Since each page's web elements are in a separate class file, the code becomes easy to maintain and reduces code duplicity


## Installation

•	**Selenium** : Selenium 4.12.0 (for auto dowanload webdriver use SeleniumManager)

•	**Pytest** : Python UnitTest framework


## Running Tests

#### If you want to run tests, you should type:

```bash
  pytest TestCases/test_loginpage.py
```
#### If you want to run tests on desired browser, you should type:
```bash
  pytest TestCases/test_loginpage.py --browsername chrome

  pytest TestCases/test_loginpage.py --browsername firefox
