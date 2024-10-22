1. Workbook object
2. list of every sheet's name
3. `sheet = wb['Sheet1']`
4. `sheet = wb.active`
5. `sheet['C5'].value`
6. `sheet['C5'] = "Hello"`
7. `cell.row` and `openpyxl.utils.get_index_from_string(cell.column)`
8. integer of maximum number of columns/rows of sheet
9. `openpyxl.utils.get_index_from_string('M')`
10. `openpyxl.utils.get_column_letter(14)`
11. `cellTuple = sheet['A1':'F1']`
12. `wb.save('example.xlsx')`
13. `cell = '=SUM(B1:B4)'`
14. `cell.value`
15. `sheet.row_dimensions[1].height=100`
16. `sheet.column_dimensions['C'].width=0`
17. A group of one or more rows and/or columns that are frozen whilst scrolling
18. openpyxl.chart.Reference(), openpyxl.chart.Series(), Series.append(), openpyxl.chart.BarChart(), sheet.add_chart()
