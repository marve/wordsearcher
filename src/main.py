"""Python module that implements a word search generator"""
import grid_builder
import pdf_renderer

print('Word Search Generator')
grids = grid_builder.build()
FILE = 'word-search.pdf'
print(f'Writing grid as {FILE}')
pdf_renderer.render(grids, FILE)
