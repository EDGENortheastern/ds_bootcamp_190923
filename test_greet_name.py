import unittest

# to test the output of the print function capture the standard output (stdout)
# For this purpose, the io.StringIO class is used as an in-memory text stream
import io
import sys
from greet_name import greet

class TestGreetFunction(unittest.TestCase):

    def setUp(self):
        # Capture the standard output
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Release the standard output capture
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_greet_walter(self):
        greet("Walter")
        self.assertEqual(self.held_output.getvalue(), "Hello, Walter!\n")
        self.assertNotEqual(self.held_output.getvalue(), "Hi, Walter!\n")

    def test_greet_alice(self):
        greet("Alice")
        self.assertEqual(self.held_output.getvalue(), "Hello, Alice!\n")
        self.assertNotEqual(self.held_output.getvalue(), "Hello, Bob!\n")

    def test_greet_return_value(self):
        result = greet("Walter")
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
