import unittest

from problem1 import multiplicative_persistence


class SolutionTest(unittest.TestCase):

    """Start Testing Results for 123 , 615 , 342"""

    def test_first_equal(self):
        """[ Check if 39 will return 3 ]"""
        self.assertEqual(multiplicative_persistence(123), 1)

    def test_second_equal(self):
        """[ Check if 999 will return 4 ]"""
        self.assertEqual(multiplicative_persistence(615), 2)

    def test_third_equal(self):
        """[ Check if 4 will return 0 ]"""
        self.assertEqual(multiplicative_persistence(342), 2)


if __name__ == '__main__':
    unittest.main()
