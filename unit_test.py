import unittest

from app import app

class AppTestCase(unittest.TestCase):
    def test_hello_with_string(self):
        # test hello
        res = app.hello("Group3")
        self.assertEqual(res, "Hello, Group3")

    def test_hello_with_number(self):
        # test hello
        res = app.hello(1)
        self.assertEqual(res, "Hello, 1")

if __name__ == "__main__":
    unittest.main()
