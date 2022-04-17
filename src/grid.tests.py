"""Tests for grid module"""
import unittest
from fit_error import FitError

from grid import Grid
from orientation import Orientation
from word import Word

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name

class GridTests(unittest.TestCase):
    def setUp(self):
        self.grid = Grid('foo', 3)

    def test_across_word_too_long(self):
        with self.assertRaises(FitError):
            self.grid.add(Word('barf', Orientation.ACROSS))

    def test_up_word_too_long(self):
        with self.assertRaises(FitError):
            self.grid.add(Word('barf', Orientation.UP))

    def test_diag_word_too_long(self):
        with self.assertRaises(FitError):
            self.grid.add(Word('barf', Orientation.DIAG))

    def test_across_word_one_char_less_than_max(self):
        self.grid.add(Word('ba', Orientation.ACROSS))

    def test_across_max(self):
        self.grid.add(Word('bar', Orientation.ACROSS))

    def test_mixed_full_max(self):
        # pylint: disable=protected-access
        self.grid._words.append(Word('bar', Orientation.UP))
        self.grid._arry[0][1] = 'b'
        self.grid._arry[1][1] = 'a'
        self.grid._arry[2][1] = 'r'
        self.grid.add(Word('baz', Orientation.ACROSS))
        self.grid.add(Word('fab', Orientation.DIAG))
        self.grid.add(Word('rad', Orientation.DIAG))
        self.grid.fill()

    def test_diag_max(self):
        self.grid.add(Word('bar', Orientation.DIAG))

    def test_diag_full_max(self):
        self.grid.add(Word('bar', Orientation.DIAG))
        self.grid.add(Word('baz', Orientation.DIAG, reverse = True))
        self.grid.fill()

if __name__ == '__main__':
    unittest.main()
