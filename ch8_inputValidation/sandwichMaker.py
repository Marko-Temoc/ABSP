#!/usr/bin/env python3

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
    answer1 = pyip.inputYesNo('Would you like cheese on your sandwich?\n')
    if answer1 == 'yes':
        cheese_choice = pyip.inputMenu(list(cheese_types.keys()))
        price += cheese_types.get(cheese_choice)
    answer2 = pyip.inputYesNo('Would you like mayo, mustard, lettuce, or tomato?\n')
    if answer2 == 'yes':
        multiple = []
        mayo_choice = pyip.inputYesNo('Mayo?\n')
        if mayo_choice == 'yes':
            multiple.append(' mayo')
        mustard_choice = pyip.inputYesNo('Mustard?\n')
        if mustard_choice == 'yes':
            multiple.append(' mustard')
        lettuce_choice = pyip.inputYesNo('Lettuce?\n')
        if lettuce_choice == 'yes':
            multiple.append(' lettuce')
        tomato_choice = pyip.inputYesNo('Tomato?\n')
        if tomato_choice == 'yes':
            multiple.append(' tomato')
        multiple = ','.join(multiple) + ','
    if answer2 == 'no':
        multiple = ''
    how_many_sandwiches = pyip.inputInt("How many of that sandwich do you want?\n", greaterThan=0)
    price *= how_many_sandwiches
    price = f'{price:.2f}'
    print(f"All done! You want {how_many_sandwiches} sandwiches with {bread_choice} bread, {protein_choice} protein,{multiple} and {cheese_choice} cheese!")
    print(f"\nYour total will be: ${price}")
sandwichMaker()
