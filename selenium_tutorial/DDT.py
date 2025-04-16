from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import pytest, unittest
from ddt import ddt, unpack, data

@pytest.mark.usefixtures("oneTimeSetup", "setup")
@ddt
class RegisterMultipleCourses(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetup):
        self.courses = RegisterCoursesPage(self.driver)
        self.TS = TestStatus(self.driver)

    def testInvalidEnrollment(self, courseName, ccNum, ccExpDate, ccCVV):












