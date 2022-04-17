""" This module houses the GridGenerator """
import json
import os
from random import choices
from string import ascii_lowercase
from dupe_error import DupeError
from fit_error import FitError
from grid import Grid
from orientation import Orientation
from word import Word

MAX_WORD_LENGTH = 15
WORD_COUNT = 20

class GridBuilder:
    """Class that can build a word search grid"""
    def get_grid(self):
        """Returns a word search grid"""
        # pylint: disable=line-too-long
        generate_grid = self.get_generate_choice()
        if not generate_grid:
            title = input('Title: ')
            grid = Grid(title)
            for i in range(WORD_COUNT):
                while True:
                    word = input(f'Word {i+1}: ')
                    if not self.validate(word):
                        continue
                    try:
                        grid.add(Word(word, self.get_orientation(), self.get_direction()))
                        break
                    except FitError:
                        print('Try another word or orientation')
                        continue
                    except DupeError:
                        print(f'Choose a different word since "{word}" is already in the grid')
                        continue
        else:
            word_dict = f'{os.path.dirname(__file__)}/../words_dictionary.json'
            with open(word_dict, 'r', encoding='utf8') as word_file:
                all_words = [k for k, _ in json.load(word_file).items() if len(k) <= MAX_WORD_LENGTH]
            grid = Grid('Random Adventure')
            word_choices = choices(all_words, k=100)
            for word in word_choices:
                orientation = self.get_random_orientation()
                reverse = self.get_random_reverse()
                try:
                    self.add_word(grid, Word(word, orientation, reverse))
                except FitError:
                    print('Trying a different word')
                if len(grid.words) >= WORD_COUNT:
                    break
        if len(grid.words) != WORD_COUNT:
            print(f'ERROR: Expected {WORD_COUNT} words in grid but actually have {len(grid.words)}')
            raise ValueError
        grid.fill()
        return grid

    def get_random_orientation(self):
        """Get a random orientation value"""
        return choices([Orientation.ACROSS, Orientation.DIAG, Orientation.UP], k=1)[0]

    def get_random_reverse(self):
        """Get a random reverse value"""
        return choices([True, False], k=1)[0]

    def validate(self, word):
        """Returns true if the word is valid, false otherwise"""
        if [c for c in word.lower() if not ascii_lowercase.__contains__(c)]:
            print('Yikes! That does not seem like a word. Try again!')
            return False
        if len(word) < 2:
            print('Nah. That word is too short. Choose a word at least 2 characters in length')
            return False
        if len(word) > MAX_WORD_LENGTH:
            print(f'What a doozy! Choose one less than {MAX_WORD_LENGTH + 1} characters')
            return False
        return True

    def get_generate_choice(self):
        """Returns the user choice for grid building strategy"""
        while True:
            match input('Generate [r]andom grid or [e]nter custom words? ').lower()[:1]:
                case 'e':
                    return False
                case 'r':
                    return True
                case _:
                    print('Hmm...that does not match. Try again')
                    continue

    def get_orientation(self):
        """Returns the user choice for word orientation"""
        while True:
            match input('Orientation - [A]cross, [U]p, [D]iagonal: ').lower()[:1]:
                case 'a':
                    return Orientation.ACROSS
                case 'u':
                    return Orientation.UP
                case 'd':
                    return Orientation.DIAG
                case '':
                    return self.get_random_orientation()
            continue

    def get_direction(self):
        """Returns the user choice for word direction"""
        while True:
            match input('Reverse - [N]o, [Y]es:').lower()[:1]:
                case 'n':
                    return False
                case 'y':
                    return True
                case '':
                    return self.get_random_reverse()
            continue

    def add_word(self, grid, word):
        """Adds the word to the grid if possible"""
        try:
            grid.add(word)
        except FitError:
            print(f'WARNING: Could not add {word}')
            print(grid)
            raise
