import pytest

@pytest.fixture()
def setUp():
    print("this is Sample TC")

def testSample1(setUp):
    print("this is Sample TC 1")

def testSample2(setUp):
    print("this is Sample TC 2")









