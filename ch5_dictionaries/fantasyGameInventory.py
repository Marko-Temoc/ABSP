#!/usr/bin/env python3

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    totalNum = 0
    print("Inventory of:")
    for item, num in inventory.items():
        print(item, num)
        totalNum += num
    print("Total number of items: " + str(totalNum) + '\n')

def addToInventory(inventory, addedItems):
    #for every item in the loot list
    for item in addedItems:
        #check if in inventory, if not add it with a value of 1
        inventory.setdefault(item, 1)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

#more inventory examples below

#nv_warrior = {'battleaxe': 1, 'torch': 3, 'skulls': 4 ,'gold coin': 89}
#nv_archer = {'bow': 2, 'arrow': 20, 'quiver': 2, 'gold coin': 233}
#nv_mage = {'staff': 1, 'dagger': 3, 'scrolls': 11, 'gold coin': 28}

#displayInventory(inv_warrior)
#displayInventory(inv_archer)
#displayInventory(inv_mage)
