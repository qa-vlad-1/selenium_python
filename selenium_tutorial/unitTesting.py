import unittest

class assertiondemo(unittest.TestCase):

    def test_assertTrue(self):
        a = True
        self.assertTrue(a, 'a is true')

    def test_assertFalse(self):
        b = False
        self.assertFalse(b, 'b is false')


if __name__ == '__main__':
    unittest.main()


