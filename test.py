""" Testing framework for unit testing in Python"""
import unittest
from password_gen import generate_password
import string  # Provides a collection of useful string constants, including ASCII letters, digits, and


# punctuation characters


class TestGeneratePassword(unittest.TestCase):

    def test_generate_password(self):
        # Test with minimum length 10, including numbers and special characters
        password = generate_password(10, numbers=True, special_characters=True)
        self.assertTrue(len(password) >= 10)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

        # Test with minimum length 8, including only letters
        password = generate_password(8, numbers=False, special_characters=False)
        self.assertTrue(len(password) >= 8)
        self.assertTrue(password.isalpha())

        # Test with minimum length 12, excluding numbers and special characters
        password = generate_password(12, numbers=False, special_characters=False)
        self.assertTrue(len(password) >= 12)
        self.assertTrue(password.isalpha())


"""This conditional block ensures that the test script runs only when executed directly, not when imported as a 
module. """
if __name__ == '__main__':
    unittest.main()  # This line runs the test cases defined in the TestGeneratePassword class and displays
    # the test results on the screen.
