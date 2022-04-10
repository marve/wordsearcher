"""
This module houses the GridGenerator
"""
import json
import os
from random import choices
from string import ascii_lowercase
from grid import Grid
from orientation import Orientation
from word import Word

MAX_WORD_LENGTH = 15

class GridBuilder:
    def get_grid(self):
        generate_grid = self.get_generate_choice()
        if not generate_grid:
            title = input('Title: ')
            grid = Grid(title)
            for i in range(20):
                while True:
                    word = input(f'Word {i+1}: ')
                    if not self.validate(word):
                        continue
                    break
                grid.add(Word(word, self.get_orientation(), self.get_direction()))
        else:
            word_dict = f'{os.path.dirname(__file__)}/../words_dictionary.json'
            with open(word_dict, 'r', encoding='utf8') as word_file:
                all_words = [k for k, v in json.load(word_file).items() if len(k) <= MAX_WORD_LENGTH]
            grid = Grid('Random Adventure')
            word_choices = choices(all_words, k=20)
            for word in word_choices:
                orientation = choices([Orientation.ACROSS, Orientation.DIAG, Orientation.UP], k=1)[0]
                reverse = choices([True, False], k=1)[0]
                grid.add(Word(word, orientation, reverse))
        grid.fill()
        return grid

    def validate(self, word):
        if [c for c in word.lower() if not ascii_lowercase.__contains__(c)]:
            print('Yikes, that does not seem like a word. Try again!')
            return False
        if len(word) < 2:
            print('Nah, that word is too short. Come up with a word that is at least 2 characters')
            return False
        if len(word) > MAX_WORD_LENGTH:
            print(f'Wow that word is a doozy. Pick one that is no more than {MAX_WORD_LENGTH}')
            return False
        return True

    def get_generate_choice(self):
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
        while True:
            match input('Orientation - [A]cross, [U]p, [D]iagonal: ').lower()[:1]:
                case 'a':
                    return Orientation.ACROSS
                case 'u':
                    return Orientation.UP
                case 'd':
                    return Orientation.DIAG
            continue

    def get_direction(self):
        while True:
            match input('Reverse - [N]o, [Y]es:').lower()[:1]:
                case 'n':
                    return False
                case '':
                    return False
                case 'y':
                    return True
            continue