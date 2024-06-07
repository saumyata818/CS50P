import unittest
from twttr import shorten

class TestTwttr(unittest.TestCase):
    def test_shorten(self):
        self.assertEqual(shorten('Hello'), 'Hll')
        self.assertEqual(shorten('world'), 'wrld')
        self.assertEqual(shorten('AEIOU'), '')
        self.assertEqual(shorten('aeiou'), '')
        self.assertEqual(shorten(''), '')
        self.assertEqual(shorten('Hello, world!'), 'Hll, wrld!')  # Test case for punctuation
        self.assertEqual(shorten('Hello123'), 'Hll123')  # Test case for numbers

if __name__ == '__main__':
    unittest.main()

