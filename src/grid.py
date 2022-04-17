"""
This module houses the Grid class
"""
import random
import string
from typing import Final, Tuple
from fit_error import FitError
from orientation import Orientation
from word import Word

DEFAULT_SIZE: Final = 20

class Grid:
    """Class that represents a word search grid"""
    def __init__(self, title: str, size: int = DEFAULT_SIZE):
        self.title = title
        self.size = size
        self._arry: list[list[str]] = [[None for y in range(size)] for x in range(size)]
        self._words: list[Word] = []

    @property
    def words(self):
        """A copy of the words in the grid"""
        return self._words.copy()

    @property
    def arry(self):
        """A copy of the underlying grid representation"""
        return self._arry.copy()

    def add(self, word: Word):
        """Adds a word to an open location on the word search grid"""
        # pylint: disable=invalid-name
        # pylint: disable=line-too-long
        def rotate_grid():
            if word.orientation == Orientation.ACROSS:
                return [[(val, x, y) for y, val in enumerate(row)]
                        for x, row in enumerate(self._arry)]
            if word.orientation == Orientation.UP:
                return [[(self._arry[x][y], x, y) for x in range(self.size) for y in range(self.size)][i::self.size] for i in range(self.size)]
            # slice top left to bottom right
            reg = [[(self._arry[x+i][y+i], x+i, y+i) for i in range(self.size) if x+i < self.size and y+i < self.size] for x in range(self.size) for y in range(self.size)]
            # slice bottom left to top right
            rev = [[(self._arry[x+i][y-i], x+i, y-i) for i in range(self.size) if x+i < self.size and y-i >= 0] for x in range(self.size) for y in range(self.size-1, 0, -1)]
            return reg + rev
        def get_possible_positions(grid: list[list[Tuple[int,int,int]]]):
            for row in grid:
                for y in range(len(row)):
                    start = y
                    end = start + word.length
                    if end <= len(row):
                        vals = row[start:end]
                        if len([val for i, val in enumerate(vals) if not val[0] or word.rendered[i] == val[0]]) == word.length:
                            yield [(val[1], val[2]) for val in vals]
        if word.length > self.size:
            raise FitError
        possibilities = list(get_possible_positions(rotate_grid()))
        if not possibilities:
            raise FitError
        chosen = random.choice(list(possibilities))
        for i, coords in enumerate(chosen):
            x, y = coords
            self._arry[x][y] = word.rendered[i]
        self._words.append(word)

    def fill(self):
        """Fills empty spaces in the grid with random characters"""
        # pylint: disable=invalid-name
        for x in range(self.size):
            for y in range(self.size):
                if not self._arry[x][y]:
                    self._arry[x][y] = random.choice(string.ascii_lowercase)

    def __str__(self):
        return '\n'.join([str([i if i else ' ' for i in row]) for row in self._arry])
