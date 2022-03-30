"""
This module houses the Grid class
"""
import random
import string
from typing import Final, Tuple
from orientation import Orientation
from word import Word

SIZE: Final = 20

class Grid:
    def __init__(self, title: str):
        self.title = title
        self._arry: list[list[str]] = [[None for y in range(SIZE)] for x in range(SIZE)]
        self._words: list[Word] = []

    @property
    def words(self):
        return self._words.copy()

    @property
    def arry(self):
        return self._arry.copy()

    def add(self, word: Word):
        def rotate_grid():
            if word.orientation == Orientation.ACROSS:
                return [[(val, x, y) for y, val in enumerate(row)] for x, row in enumerate(self._arry)]
            if word.orientation == Orientation.UP:
                return [[(self._arry[x][y], x, y) for x in range(SIZE) for y in range(SIZE)][i::SIZE] for i in range(SIZE)]
            return [[(self._arry[x+i][y+i], x+i, y+i) for i in range(SIZE) if x+i < SIZE and y+i < SIZE] for x in range(SIZE) for y in range(SIZE)]
        def get_possible_positions(grid: list[list[Tuple[int,int,int]]]):
            for row in grid:
                for y in range(len(row)):
                    start = y
                    end = start + word.length
                    if end < len(row):
                        vals = row[start:end]
                        if len([val for i, val in enumerate(vals) if not val[0] or word.rendered[i] == val[0]]) == word.length:
                            yield [(val[1], val[2]) for val in vals]
        if word.length > SIZE:
            raise ValueError
        possibilities = list(get_possible_positions(rotate_grid()))
        if not possibilities:
            raise ValueError
        chosen = random.choice(list(possibilities))
        for i, coords in enumerate(chosen):
            x, y = coords
            self._arry[x][y] = word.rendered[i]
        self._words.append(word)

    def fill(self):
        for x in range(SIZE):
            for y in range(SIZE):
                if not self._arry[x][y]:
                    self._arry[x][y] = random.choice(string.ascii_lowercase)

    def __str__(self):
        return '\n'.join([str([i if i else ' ' for i in row]) for row in self._arry])
