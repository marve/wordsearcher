"""Python module that implements a word search generator"""
import interactive_builder
import pdf_renderer

print('Word Search Generator')
grids = interactive_builder.build()
FILE = 'word-search.pdf'
print(f'Writing grid as {FILE}')
pdf_renderer.render_file(grids, FILE)
