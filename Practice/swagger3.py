import pytest
from classToTest import testDemoToClass
# Section 163

class TestDemoMethod():


    def test_Method_A(self):
        print("---- Method A -----")
        abc = testDemoToClass(10)
        result = abc.sumNumbers(8, 2)
        assert result == 20

    def test_Method_B(self):
        print("---- Method B -----")
























