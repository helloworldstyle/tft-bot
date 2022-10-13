class Items:
    def __init__(self, name, coords, onBench):
        self.name = name
        self.coords = coords
        self.onBench = onBench # whether available

current_items = []
current_items_on_bench = [] # available items

def getItemIndexOnBench(coords):
    for index in range(len(current_items)):
        if(current_items_on_bench[index].coords == coords):
            return index
    else:
        return -1

def getItemIndex(coords):
    for index in range(len(current_items)):
        if(current_items[index].coords == coords):
            return index
    else:
        return -1

def addItem(name, coords, onBench):
    current_items.append(Items(name, coords, onBench))

def delItem(coords):
    del current_items[getItemIndex(coords)]


def printItemsHelperCurrentList(item_list):
    for l in range(len(item_list)):
        print(item_list[l].name)
        print(item_list[l].coords)
        print(item_list[l].onBench)
        pass
