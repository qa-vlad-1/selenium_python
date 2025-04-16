import pytest

@pytest.fixture()
def setup_1():
    print("Log in")
    print("Sign in with User")
    print("Click Home")
    yield
    print("Sign out")
    print("Close Browser")
    print("Shut down Computer")

@pytest.fixture()
def teardown():
    print("------ Teardown -------")
    yield
    print("-------Teardown 2------")

@pytest.fixture(scope='module')
def oneTimeSetup():
    print("Method will run as SETUP - ONLY ONE TIME")
    yield
    print("Method will run as TEARDOWN - ONLY ONE TIME")

# def pytest_add_option(parser):
#     # browser type: Chrome, Firefox
#     parser.addoption("--browser")
#     # Operation Syster run on: Windows, Mac
#     parser.addoption("--OSType")

@pytest.fixture()
def prep():
    print("Run ONCE BEFORE every Test Case")
    yield
    print("Run ONCE AFTER every Test Case")












