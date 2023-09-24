"""Python Flask web application that can build a wordsearch"""
from flask import Flask, render_template, request, Response
from grid import Grid
from word import Word
import pdf_renderer

app = Flask(__name__)

@app.get("/")
def show_form():
    """Returns the page used to enter words for a wordsearch"""
    return render_template('create.html')

@app.post("/")
def create():
    """Creates and returns a PDF wordsearch using the given words"""
    grid = Grid('Fancy')
    for _, (_, value) in enumerate(request.form.items()):
        word = Word(value)
        grid.add(word)
    grid.fill()
    pdf = pdf_renderer.render_string(grid)
    return Response(pdf.encode("latin1"), status=200, mimetype='application/pdf')
