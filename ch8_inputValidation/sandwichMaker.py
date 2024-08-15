#!/usr/bin/env python3

'''
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:
    Using inputMenu() for a bread type: wheat, white, or sourdough.
    Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
    Using inputYesNo() to ask if they want cheese.
    If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
    Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
    Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
'''

'''
pyip.inputMenu(breads)
pyip.inputMenu(proteins)
pyip.inputYesNo(cheese)
pyip.inputMenu(cheese_type)
pyip.inputInt(how_many_sandwiches)
'''
import pyinputplus as pyip

breads = ['wheat', 'white', 'sourdough', 'moldy']
proteins = ['chicken', 'turkey', 'ham', 'tofu', 'horse']
cheese_types = ["cheddar", "Swiss", "mozzarella", "'that same horse'"]
cheese_choice = "no"

def sandwichMaker():
    print('Welcome to the Imaginary Sandwich Shop! Pretend to order a sandwich today!\n')
    bread_choice = pyip.inputMenu(breads)
    protein_choice = pyip.inputMenu(proteins)
    answer = pyip.inputYesNo('Would you like cheese on your sandwich?\n')
    if answer == 'yes':
        global cheese_choice
        cheese_choice = pyip.inputMenu(cheese_types)
    how_many_sandwiches = pyip.inputInt("How many of that sandwich do you want?\n", greaterThan=0)
    print(f"All done! You want {how_many_sandwiches} sandwiches with {bread_choice} bread, {protein_choice} protein, and {cheese_choice} cheese!")
sandwichMaker()
