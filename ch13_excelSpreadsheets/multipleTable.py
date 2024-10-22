#!/usr/bin/env python3

import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.styles import Font

input = 6

wb = openpyxl.Workbook()
sheet = wb.active
current_col = 1
foont = Font(bold=True)

#set up loop
for i in range(1, input + 1):
    sheet[f'A{i+1}'] = i
    sheet[f'A{i+1}'].font = foont
    current_col += 1
    sheet[f'{get_column_letter(current_col)}1'] = i
    sheet[f'{get_column_letter(current_col)}1'].font = foont



wb.save('timesTable.xlsx')
