import pytest
# contains common methods that can be executed within TC

@pytest.fixture()
def check():
    print("this will print once")
    yield
    print("will do the Clean Up")

@pytest.fixture()
def runOneTime():
    print("Will RUN ONLY ONCE")
    yield
    print("Will CLEAN UP only ONCE")