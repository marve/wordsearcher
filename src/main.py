"""Python module that implements a word search generator"""
import grid_builder
import pdf_renderer

print('Word Search Generator')
grid = grid_builder.build()
FILE = 'word-search.pdf'
print(f'Writing grid as {FILE}')
pdf_renderer.render(grid, FILE)
