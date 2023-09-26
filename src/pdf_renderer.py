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

def _add_page(grid: Grid, pdf: FPDF):
    pdf.add_page()
    pdf.add_font(FONT_NAME, '', FONT_FILE, uni = True)
    pdf.set_font(FONT_NAME, '', 20)
    pdf.cell(w = 0, h = 10, txt = grid.title, align = 'C')
    pdf.set_font(FONT_NAME, '', 16)
    top_gap = 31.5
    left_gap = 35
    row_height = 7.0
    cell_width = row_height

    for i, row in enumerate(grid.arry):
        pdf.set_xy(x = left_gap, y = (row_height * i) + top_gap)
        for char in row:
            pdf.cell(w = cell_width, h = row_height, txt = char.upper(), align = 'C')
    pdf.rect(x = left_gap, y = 30, w = 141, h = 142.5, style = 'D')

    pdf.set_font(FONT_NAME, '', 14)
    num_cols = 4
    top_gap = 182.5
    left_gap = 10
    row_height = 6
    cell_width = 50
    word_table = [grid.words[i:i+num_cols] for i in range(0,len(grid.words),num_cols)]
    for i, row in enumerate(word_table):
        pdf.set_xy(x = left_gap, y = (row_height * i) + top_gap)
        for word in row:
            pdf.cell(w = cell_width, h = row_height, txt = word.text.capitalize(), align = 'L')