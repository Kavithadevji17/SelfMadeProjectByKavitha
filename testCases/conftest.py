import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("************Lanching Chrome Browser*********")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("************Lanching Firefox Browser*********")
    # else:
    #     driver = webdriver.Edge

    return driver

def pytest_addoption(parser):       # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the browser value to setup method
    return request.config.getoption("--browser")



##########################   PyTest HTML Report   ######################


# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop Commerce App'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Kavitha Devraj'
#
# #
# # # It is hook for delete/modify environment info to HTML report
# #
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)