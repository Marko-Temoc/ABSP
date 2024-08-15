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

import pyinputplus as pyip

def sandwichMaker():
    breads = {'wheat':1.20, 'white':1.00, 'sourdough':1.15, 'moldy':0.10}
    proteins = {'chicken':2.00, 'turkey':1.99, 'ham':0.99, 'tofu':2.10, 'horse':3.00}
    cheese_types = {"cheddar":0.50, "Swiss":0.75, "mozzarella":0.56, "'that same horse'":0.99}
    cheese_choice = "no"
    price = 0.00

    print('Welcome to the Imaginary Sandwich Shop! Pretend to order a sandwich today!\n')
    bread_choice = pyip.inputMenu(list(breads.keys()))
    price += breads.get(bread_choice)
    protein_choice = pyip.inputMenu(list(proteins.keys()))
    price += proteins.get(protein_choice)
    answer = pyip.inputYesNo('Would you like cheese on your sandwich?\n')
    if answer == 'yes':
        cheese_choice = pyip.inputMenu(list(cheese_types.keys()))
        price += cheese_types.get(cheese_choice)
    how_many_sandwiches = pyip.inputInt("How many of that sandwich do you want?\n", greaterThan=0)
    price *= how_many_sandwiches
    price = f'{price:.2f}'
    print(f"All done! You want {how_many_sandwiches} sandwiches with {bread_choice} bread, {protein_choice} protein, and {cheese_choice} cheese!")
    print(f"\nYour total will be: ${price}")
sandwichMaker()
