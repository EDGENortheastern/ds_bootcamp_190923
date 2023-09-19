import unittest
from two_returns import fun_function

class TestFunFunction(unittest.TestCase):
    
    def test_vowel_count_and_reversed(self):
        # Test the given example
        self.assertEqual(fun_function("Hello, World!"), ("!dlroW ,olleH", 3))
        
        # Test an empty string
        self.assertEqual(fun_function(""), ("", 0))
        
        self.assertIsInstance(fun_function(''), tuple)

        self.assertIsInstance(fun_function(''), int)

if __name__ == "__main__":
    unittest.main()