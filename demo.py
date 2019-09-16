import unittest
import BSTestRunner

class DemoTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

if __name__ == '__main__':
    BSTestRunner.main()
