import pytest

#@pytest.fixture()
def setup():
    print("Runs only once")
    yield
    print("Run once only AFTER")

@pytest.mark.run(order=4)
def test_method_1(oneTimeSetup):
    print("----------- Test Method 1 ------------")

@pytest.mark.run(order=1)
def test_method_2(oneTimeSetup):
    print("----------- Test Method 2 ------------")

@pytest.mark.run(order=3)
def test_method_3(oneTimeSetup):
    print("----------- Test Method 3 ------------")

@pytest.mark.run(order=2)
def test_method_4(oneTimeSetup):
    print("----------- Test Method 4 ------------")
















