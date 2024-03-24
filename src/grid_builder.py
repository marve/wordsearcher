"""This module houses the logic for building a word search grid"""
import json
import os
from random import choices
from string import ascii_lowercase
from typing import Optional
from fit_error import FitError
from grid import Grid
from orientation import Orientation
from word import Word

MAX_WORD_LENGTH = 15
WORD_COUNT = 20

def build(num: Optional[int] = None, words: Optional[list[str]] = None):
    """Returns a word search grid"""
    # pylint: disable=line-too-long
    if words and num:
        raise ValueError('Both "words" and "num" arguments are set. Pick one!')
    if not words and not num:
        raise ValueError('Must specify either "words" or "num" argument. Pick one!')
    if words and len(words) % WORD_COUNT:
        raise ValueError(f'Supplied words need to be a multiple of {WORD_COUNT}.')
    if num is not None and num <= 0:
        raise ValueError('Desired number of word searches must be a positive integer.')
    if words and [w for w in words if not _validate(w, False)]:
        raise ValueError('At least one of the words is not valid')
    num = num if num else int(len(words) / WORD_COUNT) if words else 0
    words = words if words else _get_dictionary_words(WORD_COUNT * num)
    grids = []
    for i in range(num):
        grid = Grid('Random Adventure')
        start = i * WORD_COUNT
        for word in words[start:start+WORD_COUNT]:
            orientations_tried: set[Orientation] = set()
            while True:
                orientation = _get_random_orientation(orientations_tried)
                reverse = _get_random_reverse()
                try:
                    _add_word(grid, Word(word, orientation, reverse))
                    break
                except FitError:
                    print('WARNING: Trying the word in reverse')
                    try:
                        _add_word(grid, Word(word, orientation, not reverse))
                        break
                    except FitError:
                        orientations_tried.add(orientation)
                        print('WARNING: Trying a different orientation')
        if len(grid.words) != WORD_COUNT:
            raise ValueError(f'Expected {WORD_COUNT} words in grid but actually have {len(grid.words)}')
        grid.fill()
        grids.append(grid)
    return grids

def _validate(word, verbose = True):
    """Returns true if the word is valid, false otherwise"""
    # pylint: disable=line-too-long
    if [c for c in word.lower() if not ascii_lowercase.__contains__(c)]:
        _ = None if not verbose else print('Yikes! That does not seem like a word. Try again!')
        return False
    if len(word) < 2:
        _ = None if not verbose else print('Nah. That word is too short. Choose a word at least 2 characters in length')
        return False
    if len(word) > MAX_WORD_LENGTH:
        _ = None if not verbose else print(f'What a doozy! Choose one less than {MAX_WORD_LENGTH + 1} characters')
        return False
    return True

def _get_dictionary_words(num: int):
    word_dict = f'{os.path.dirname(__file__)}/../words_dictionary.json'
    with open(word_dict, 'r', encoding='utf8') as word_file:
        all_words = [w for w, _ in json.load(word_file).items() if _validate(w, False)]
    word_choices = choices(all_words, k=num)
    return word_choices

def _get_random_orientation(exclude: Optional[set[Orientation]] = None):
    """Get a random orientation value"""
    opts = {Orientation.ACROSS, Orientation.DIAG, Orientation.UP}
    if exclude:
        opts = opts.difference(exclude)
    if not opts:
        raise ValueError('No orientations left to try!')
    return choices(list(opts), k=1)[0]

def _get_random_reverse():
    """Get a random reverse value"""
    return choices([True, False], k=1)[0]

def _add_word(grid, word):
    """Adds the word to the grid if possible"""
    try:
        grid.add(word)
    except FitError:
        print(f'WARNING: Could not add {word}')
        print(grid)
        raise
