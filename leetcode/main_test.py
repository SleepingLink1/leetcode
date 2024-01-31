import unittest
from main import is_palindrome, fibonacci


class TestLeetCode(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_is_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12345"))

    def test_is_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome("!@#$%$#@!"))
        self.assertFalse(is_palindrome("!@#$%^"))

    def test_is_palindrome_with_empty_string(self):
        self.assertTrue(is_palindrome(""))

    # Additional test cases for fibonacci
    def test_fibonacci_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_with_large_numbers(self):
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

if __name__ == '__main__':
    unittest.main()
