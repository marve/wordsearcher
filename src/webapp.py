"""Python Flask web application that can build a wordsearch"""
import re
from flask import Flask, render_template, request, Response
from fit_error import FitError
from grid import Grid
from word import Word
from grid_builder import _add_word
from grid_builder import _get_dictionary_words
from grid_builder import _get_random_orientation
from grid_builder import _get_random_reverse
from grid_builder import WORD_COUNT
import pdf_renderer

app = Flask(__name__)

@app.get("/")
def index():
    """Returns the default page for the application"""
    return render_template('index.html')

@app.get("/custom")
def custom_form():
    """Returns the page used to enter words for a wordsearch"""
    return render_template('custom.html')

@app.post("/custom")
def custom_create():
    """Creates and returns a PDF wordsearch using the given words"""
    grid = Grid('Custom Adventure')
    for _, (_, word) in enumerate(request.form.items()):
        word = re.sub(r'[^a-zA-Z]', '', word)
        orientation = _get_random_orientation()
        reverse = _get_random_reverse()
        _add_word(grid, Word(word, orientation, reverse))
    return _pdf_response(grid)

@app.post("/generate")
def generate():
    """Creates and returns a PDF wordsearch with random words"""
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
    return _pdf_response(grid)

def _pdf_response(grid: Grid):
    grid.fill()
    pdf = pdf_renderer.render_string(grid).encode("latin1")
    return Response(pdf, status=200, mimetype='application/pdf')
