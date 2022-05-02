"""Tests for grid builder module"""
from string import ascii_letters
import unittest
import grid_builder

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring

class GridTests(unittest.TestCase):
    def test_correct_number_of_words(self):
        words = [f'word{ascii_letters[i]}' for i in range(20)]
        grids = grid_builder.build(words)
        self.assertEqual(1, len(grids))

    def test_incorrect_number_of_words(self):
        with self.assertRaises(ValueError):
            grid_builder.build(["word"])

    def test_valid_num(self):
        grids = grid_builder.build(num = 4)
        self.assertEqual(4, len(grids))

    def test_invalid_num(self):
        with self.assertRaises(ValueError):
            grid_builder.build(num = 0)

if __name__ == '__main__':
    unittest.main()
