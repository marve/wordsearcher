"""
This module houses the PdfRenderer class
"""
from fpdf import FPDF
from grid import Grid

"""
Renders a word search grid in PDF format
"""
class PdfRenderer:
    def render(self, grid: Grid, path: str):
        pdf = FPDF()
        pdf.add_page()
        font_path = '/workspaces/wordsearcher/fonts/roboto_mono/RobotoMono-VariableFont_wght.ttf'
        pdf.add_font('Roboto Mono', '', font_path, uni = True)
        pdf.set_font('Roboto Mono', '', 20)
        pdf.cell(w = 0, h = 10, txt = grid.title, align = 'C')
        pdf.set_font('Roboto Mono', '', 16)
        top_gap = 31.5
        left_gap = 35
        row_height = 7.0
        cell_width = row_height

        for i, row in enumerate(grid.arry):
            pdf.set_xy(x = left_gap, y = (row_height * i) + top_gap)
            for char in row:
                pdf.cell(w = cell_width, h = row_height, txt = char.upper(), align = 'C')
        pdf.rect(x = left_gap, y = 30, w = 141, h = 142.5, style = 'D')

        pdf.set_font('Roboto Mono', '', 14)
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