""" Python module that implements a word search generator """
from grid_builder import GridBuilder
from pdf_renderer import PdfRenderer

print('Word Search Generator')
builder = GridBuilder()
grid = builder.get_grid()
renderer = PdfRenderer()
renderer.render(grid, 'word-search.pdf')
