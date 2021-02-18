# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:43:31 2021

@author: martsc1
"""
#addToInventory.py
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))
    
def addToInventory(inventory, addedItems):
    # your code goes here
    for elem in addedItems:
        if inventory.get(elem,0) == 0:
            inventory.setdefault(elem,1)
        else:
            inventory[elem] += 1
            
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)