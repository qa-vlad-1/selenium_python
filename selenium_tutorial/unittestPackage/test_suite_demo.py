import unittest

# import all Test Case files to create Test Suite
from selenium_tutorial.unittestPackage.test_case_demo1 import testCaseDemo_1
from selenium_tutorial.unittestPackage.test_case_demo2 import testCaseDemo_2

# will load ALL Tests from 'testCaseDemo_1 and 2'
TC1 = unittest.TestLoader().loadTestsFromTestCase(testCaseDemo_1)
TC2 = unittest.TestLoader().loadTestsFromTestCase(testCaseDemo_2)

# Create Test Suite combining testCaseDemo_1 and 2
#   - Place Test Suite into Variable
SmokeTest = unittest.TestSuite([TC1, TC2])

# Trigger Test Runner or Test Suite
unittest.TextTestRunner(verbosity=1).run(SmokeTest)



