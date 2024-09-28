#!/usr/bin/env python3
#updateProduce.py - Corrects costs in produce sales spreadsheet
import openpyxl
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']
#the produce types and their updates prices
PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}
#TODO loop through the rows and update the prices
