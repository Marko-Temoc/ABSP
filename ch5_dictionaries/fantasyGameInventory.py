#!/usr/bin/env python3

inv_warrior = {'battleaxe': 1, 'torch': 3, 'skulls': 4 ,'gold coin': 89}
inv_archer = {'bow': 2, 'arrow': 20, 'quiver': 2, 'gold coin': 233}
inv_mage = {'staff': 1, 'dagger': 3, 'scrolls': 11, 'gold coin': 28}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    totalNum = 0
    print("Inventory of :")
    for item, num in inventory.items():
        print(item, num)
        totalNum += num
    print("Total number of items: " + str(totalNum) + '\n')

def addToInventory(inventory, addedItems):
    #for every item in the loot list
    for item in addedItems:
        #check if in inventory, if not add it with a value of 0
        inventory.setdefault(item, 0)
        #whether its in inventory or not, add 1 to the value
        inventory[item] == inventory[item] + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

#displayInventory(inv_warrior)
#displayInventory(inv_archer)
#displayInventory(inv_mage)
