"""
Python module that implements a word search generator
"""
import json, os
from random import choices
from grid import Grid
from orientation import Orientation
from word import Word
from pdf_renderer import PdfRenderer

def get_generate_choice():
    if input('Generate [r]andom grid or [e]nter custom words? ').lower()[:1] == 'e':
        return False
    return True

def get_orientation():
    while True:
        match input('Orientation - [A]cross, [U]p, [D]iagonal: ').lower()[:1]:
            case 'a':
                return Orientation.ACROSS
            case 'u':
                return Orientation.UP
            case 'd':
                return Orientation.DIAG
        continue

def get_direction():
    while True:
        match input('Reverse - [N]o, [Y]es:').lower()[:1]:
            case 'n':
                return False
            case '':
                return False
            case 'y':
                return True
        continue

MAX_WORD_LENGTH = 15

print('Word Search Generator')
generate_grid = get_generate_choice()
if not generate_grid:
    title = input('Title: ')
    grid = Grid(title)
    for i in range(20):
        word = input(f'Word {i+1}: ')
        grid.add(Word(word, get_orientation(), get_direction()))
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
renderer = PdfRenderer()
renderer.render(grid, 'word-search.pdf')