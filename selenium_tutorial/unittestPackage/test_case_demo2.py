import unittest

class testCaseDemo_2(unittest.TestCase):

    def setUp(self):
        print("Running beginning of every TC -> Test Demo 2")

    def testCase_1(self):
        print("Test Case - Test Method 1")

    def testCase_2(self):
        print("Test Case - Test Method 2")

    def tearDown(self):
        print("End of Test Case - Test Demo 2")

if __name__=='__main__':
    unittest.main()