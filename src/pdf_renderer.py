"""This module houses the PdfRenderer class"""
from fpdf import FPDF
from grid import Grid

FONT = 'Roboto Mono'
FONT_PATH = '/workspaces/wordsearcher/fonts/roboto_mono/RobotoMono-VariableFont_wght.ttf'

def render(grids: list[Grid], path: str):
    """Renders the word search(es) as a PDF and writes to the given location"""
    pdf = FPDF()
    for grid in grids:
        pdf.add_page()
        pdf.add_font(FONT, '', FONT_PATH, uni = True)
        pdf.set_font(FONT, '', 20)
        pdf.cell(w = 0, h = 10, txt = grid.title, align = 'C')
        pdf.set_font(FONT, '', 16)
        top_gap = 31.5
        left_gap = 35
        row_height = 7.0
        cell_width = row_height

        for i, row in enumerate(grid.arry):
            pdf.set_xy(x = left_gap, y = (row_height * i) + top_gap)
            for char in row:
                pdf.cell(w = cell_width, h = row_height, txt = char.upper(), align = 'C')
        pdf.rect(x = left_gap, y = 30, w = 141, h = 142.5, style = 'D')

        pdf.set_font(FONT, '', 14)
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
    pdf.output(path, 'F')
