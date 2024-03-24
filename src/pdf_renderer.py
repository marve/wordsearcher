"""This module houses the PdfRenderer class"""
import pathlib
from fpdf import FPDF
from grid import Grid

FONT_NAME = 'Roboto Mono'
FONT_DIR = f'{pathlib.Path(__file__).parent.parent.resolve()}/fonts'
FONT_FILE = f'{FONT_DIR}/roboto_mono/RobotoMono-VariableFont_wght.ttf'

def render_string(grid: Grid):
    """Renders the word search as a PDF and returns the string representation"""
    pdf = FPDF()
    _add_page(grid, pdf)
    return str(pdf.output(dest = 'S'))

def render_file(grids: list[Grid], path: str):
    """Renders the word search(es) as a PDF and writes to the given file path"""
    pdf = FPDF()
    for grid in grids:
        _add_page(grid, pdf)
    pdf.output(name = path, dest = 'F')
    pdf.set_margins(0, 0, 0)

def _add_page(grid: Grid, pdf: FPDF):
    pdf.add_page()
    pdf.add_font(FONT_NAME, '', FONT_FILE, uni = True)
    pdf.set_font(FONT_NAME, '', 24)
    pdf.cell(w = 0, h = 0, txt = grid.title, align = 'C')
    pdf.set_font(FONT_NAME, '', 20)
    top_gap = 17.0
    left_gap = 5.0
    row_height = 10.0
    cell_width = row_height

    for i, row in enumerate(grid.arry):
        pdf.set_xy(x = left_gap, y = (row_height * i) + top_gap)
        for char in row:
            pdf.cell(w = cell_width, h = row_height, txt = char.upper(), align = 'C')
    pdf.rect(x = left_gap, y = 15.5, w = 200, h = 202.5, style = 'D')

    pdf.set_font(FONT_NAME, '', 21)
    num_cols = 3
    top_gap = 218.5
    left_gap = 5
    row_height = 8.35
    cell_width = 70
    word_table = [grid.words[i:i+num_cols] for i in range(0,len(grid.words),num_cols)]
    for i, row in enumerate(word_table):
        pdf.set_xy(x = left_gap, y = (row_height * i) + top_gap)
        for word in row:
            pdf.cell(w = cell_width, h = row_height, txt = word.text.capitalize(), align = 'L')
