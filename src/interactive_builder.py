"""This module houses the logic for building a word search grid"""
import re
from dupe_error import DupeError
from fit_error import FitError
from grid import Grid
from orientation import Orientation
from word import Word
from grid_builder import _add_word
from grid_builder import _get_dictionary_words
from grid_builder import _get_random_orientation
from grid_builder import _get_random_reverse
from grid_builder import _validate
from grid_builder import WORD_COUNT

def build():
    """Returns a word search grid"""
    # pylint: disable=line-too-long
    grids = []
    while True:
        generate_grid = _get_generate_choice()
        if not generate_grid:
            title = input('Title: ')
            grid = Grid(title)
            for i in range(WORD_COUNT):
                while True:
                    word = input(f'Word {i+1}: ')
                    word = re.sub(r'[^a-zA-Z]', '', word)
                    if not _validate(word):
                        continue
                    try:
                        grid.add(Word(word, _get_orientation(), _get_direction()))
                        break
                    except FitError:
                        print('Try another word or orientation')
                        continue
                    except DupeError:
                        print(f'Choose a different word since "{word}" is already in the grid')
                        continue
        else:
            grid = Grid('Random Adventure')
            word_choices = _get_dictionary_words(100)
            for word in word_choices:
                orientation = _get_random_orientation()
                reverse = _get_random_reverse()
                try:
                    _add_word(grid, Word(word, orientation, reverse))
                except FitError:
                    print('Trying a different word')
                if len(grid.words) >= WORD_COUNT:
                    break
        if len(grid.words) != WORD_COUNT:
            print(f'ERROR: Expected {WORD_COUNT} words in grid but actually have {len(grid.words)}')
            raise ValueError
        grid.fill()
        grids.append(grid)
        match input(f'You have made {len(grids)} word search{"es" if len(grids) > 1 else ""}. Do you want to make another? [Y]es, [N]o: ').lower():
            case 'n':
                break
        continue
    return grids

def _get_generate_choice():
    """Returns the user choice for grid building strategy"""
    while True:
        match input('Generate [r]andom grid or [e]nter custom words? ').lower()[:1]:
            case 'e':
                return False
            case 'r':
                return True
        continue

def _get_orientation():
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
                return _get_random_orientation()
        continue

def _get_direction():
    """Returns the user choice for word direction"""
    while True:
        match input('Reverse - [N]o, [Y]es:').lower()[:1]:
            case 'n':
                return False
            case 'y':
                return True
            case '':
                return _get_random_reverse()
        continue
