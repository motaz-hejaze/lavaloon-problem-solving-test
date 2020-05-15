import unittest

from problem3 import format_duration


class SolutionTest(unittest.TestCase):

    """Start Testing Results for some second numbers """

    def test_first_equal(self):
        """[ Check if (62) will return (1 minute and 2 seconds) ]"""
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")

    def test_second_equal(self):
        """[ Check if (3662) will return (1 hour, 1 minute and 2 seconds) ]"""
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")

    def test_third_equal(self):
        """[ Check if (123131233) will return (3 years, 330 days, 3 hours, 7 minutes and 13 seconds) ]"""
        self.assertEqual(format_duration(123131233), "3 years, 330 days, 3 hours, 7 minutes and 13 seconds")


if __name__ == '__main__':
    unittest.main()
