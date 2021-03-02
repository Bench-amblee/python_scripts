Inventory = {'rope': 1, 'torches': 6, 'gold coins': 42, 'daggers': 1, 'arrows': 12}

def displayInventory(Inventory):
    print('Inventory:')
    item_total = 0
    for k, v in Inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: ' + str(item_total))

displayInventory(Inventory)

while True:
    print('Press F to defeat the Dragon')
    dragonFight = input()
    if dragonFight == 'F':
        print('DRAGON DEFEATED')
        break
    else:
        continue



print('Congrats! You just defeated a Dragon, here is your new Inventory: ')

dragonLoot = ['gold coins', 'daggers', 'gold coins', 'gold coins', 'ruby']

def addToInventory(Inventory, addedItems):
    for loot in addedItems:
        Inventory.setdefault(loot, 0)
        Inventory[loot] += 1
    return(Inventory)

Inventory = addToInventory(Inventory, dragonLoot)
displayInventory(Inventory)
