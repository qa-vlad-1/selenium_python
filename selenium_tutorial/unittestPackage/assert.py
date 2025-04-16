import unittest

class assertDemo(unittest.TestCase):

    def test_assertequal(self):
        a = False
        self.assertFalse(a, "Assert is NOT False")

    def test_assertTrue(self):
        a = 123
        b = 'yes'
        self.assertNotEqual(a, b, msg="Assert is False")


if __name__ == '__main__':
    assertDemo()





