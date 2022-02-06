"""
Python module that implements a word search generator
"""
from grid import Grid
from orientation import Orientation
from word import Word
from pdf_renderer import PdfRenderer

words = [
    Word("fancy", Orientation.ACROSS),
    Word("solidary", Orientation.UP, True),
    Word("blinker", Orientation.DIAG),
    Word("missippi", Orientation.DIAG),
    Word("onomatopoeia", Orientation.ACROSS, False),
    Word("economical", Orientation.UP),
    Word("blighted", Orientation.ACROSS, False),
    Word("egotistical", Orientation.UP, True),
    Word("distopian", Orientation.ACROSS),
    Word("elliptical", Orientation.DIAG, True),
    Word("hypnotic", Orientation.DIAG),
    Word("couch", Orientation.ACROSS),
    Word("obtuse", Orientation.UP, True),
    Word("rectangular", Orientation.UP),
    Word("hangar", Orientation.ACROSS, True),
    Word("bleached", Orientation.UP),
    Word("familial", Orientation.DIAG),
    Word("recognition", Orientation.ACROSS),
    Word("fleeced", Orientation.DIAG, True),
    Word("earring", Orientation.UP)
]

grid = Grid()
for word in words:
    grid.add(word)
grid.fill()
renderer = PdfRenderer()
renderer.render(grid, 'word-search.pdf')