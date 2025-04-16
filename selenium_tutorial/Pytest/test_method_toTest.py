
import pytest
from class_to_test import someClasstoTest

# fixture allows all methods in () to apply to methods below
@pytest.mark.usefixtures("oneTimeSetup", "setup_1")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.abc = someClasstoTest(10)

    def testMethod_A(self):
        print("--- Test Method-> testing Function 'sumNumbers' ---")
        result = self.abc.sumNumbers(5, 2)
        assert result == 17


    def testMethod_B(self):
        print("--- Test Method B-> voided ---")













