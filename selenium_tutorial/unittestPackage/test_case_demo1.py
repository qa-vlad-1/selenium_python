import unittest

class testCaseDemo_1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Run only ONCE at BEGINNING of ALL Test Cases -> Data Prep")
    def setUp(self):
        print("Run at beginning of every Test Case -> Test Demo 1")

    def testCase_1(self):
        print("Test Case 1")

    def testCase_2(self):
        print("Test Case 2")

    def tearDown(self):
        print("Run at END of Test Case -> Test Demo 1")

    @classmethod
    def tearDownClass(cls):
        print("Run only ONCE at END of ALL Test Cases -> Clean Up")


if __name__=='__main__':
    unittest.main()

