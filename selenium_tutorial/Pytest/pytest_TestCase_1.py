import pytest

@pytest.yield_fixture()
def setup():
    print("Run ONCE --Before-- Test Case")
    yield
    print("Run ONCE --After-- Test Case ")
def test_case_1(setup):
    print("------------Run Test Case 1 -----------")

def test_case_2():
    print("------------Run Test Case 2 -----------")

