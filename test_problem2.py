import unittest

from problem2 import heaviest_word


class SolutionTest(unittest.TestCase):
    """Start Testing Results for some sentences"""
    def test_first_equal(self):
        """[ Check if (man i need a taxi up to ubud) will return (taxi) ]"""
        self.assertEqual(heaviest_word("man i need a taxi up to ubud"), "taxi")

    def test_second_equal(self):
        """[ Check if (what time are we climbing up to the volcano) will return (volcano) ]"""
        self.assertEqual(heaviest_word("what time are we climbing up to the volcano"), "volcano")

    def test_third_equal(self):
        """[ Check if (take me to semynak) will return (semynak) ]"""
        self.assertEqual(heaviest_word("take me to semynak"), "semynak")


if __name__ == '__main__':
    unittest.main()
