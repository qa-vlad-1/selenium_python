
import pytest

@pytest.mark.run(order=3)
def test_Case_1(prep, oneTimeSetup):
    print("---------- Test Case 1 ----------")
@pytest.mark.run(order=2)
def test_Case_2(prep, oneTimeSetup):
    print("---------- Test Case 2 ----------")
@pytest.mark.run(order=4)
def test_Case_3(prep, oneTimeSetup):
    print("---------- Test Case 3 ------------")
@pytest.mark.run(order=1)
def test_Case_4(prep, oneTimeSetup):
    print("---------- Test Case 4 ------------")

# 4, 2, 1, 3
















