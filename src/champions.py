from torch import slogdet
import coordinates
import comps

class Champion:
    def __init__(self, name, coords, star, uncompletedItems, completedItems, finalItems, slot, finalCompBool, onBoardBool):
        self.name = name
        self.coords = coords
        self.star = star
        self.uncompletedItems = uncompletedItems
        self.completedItems = completedItems

        self.finalItems = finalItems
        self.slot = slot 
        self.finalCompBool = finalCompBool
        self.onBoardBool = onBoardBool

# talon_finalItems = ["IE", "OE", "RT"]
# boughtChamp = Champion("Talon", (100, 100), 2, [], [], talon_finalItems, 3, True, True)
# boughtChamp.completedItems.append("IE")
# print(boughtChamp.completedItems)
# print(boughtChamp.finalItems)

current_champions = []
current_champions_on_bench = []
def getChampionIndex(coords):
    for index in range(len(current_champions)):
        if(current_champions[index].coords == coords):
            return index
    else:
        return -1
def getChampionIndexOnBench(coords):
    for index in range(len(current_champions)):
        if(current_champions_on_bench[index].coords == coords):
            return index
    else:
        return -1
def getChampionName(coords):
    for index in range(len(current_champions)):
        if(current_champions[index].coords == coords):
            return current_champions[index].name
    return "error"
def getInfoCarouselChamp(coords):
    for index in range(len(current_champions)):
        if(current_champions[index].coords == coords):
            return [current_champions[index].name, current_champions[index].uncompletedItems, current_champions[index].completedItems]
    return "error"
def getNumberOfChampionsOnBoard():
    num_on_board = 0
    for i in range(len(current_champions)):
        if(current_champions[i].onBoardBool):
            num_on_board += 1
    return num_on_board

def findChampionOnBenchAndGetCoords():
    for i in range(len(current_champions)):
        if(not current_champions[i].onBoardBool):
            return current_champions[i].coords

def getChampionCoords(index):
    return current_champions[index].coords
def addChamp(name, coords, star, uncompletedItems, finalItems, slot, finalCompBool, onBoardBool):
    current_champions.append(Champion(name, coords, star, uncompletedItems, [], finalItems, slot, finalCompBool, onBoardBool))

def delChamp(coords):
    del current_champions[getChampionIndex(coords)]

def changePosChamp(coords_old, coords_new):
    championIndex = getChampionIndex(coords_old)
    if(coords_new in coordinates.champs_on_board):
        current_champions[championIndex].onBoardBool = True
    if(coords_new in coordinates.bench_champs):
        current_champions[championIndex].onBoardBool = False
    current_champions[championIndex].coords = coords_new

def changePosChampOnBench(coords_old, coords_new):
    current_champions_on_bench[getChampionIndexOnBench(coords_old)].coords = coords_new

def setStarChamp(coords, star_new):
    current_champions[getChampionIndex(coords)].star = star_new

def changeUncompletedItemsChamp(coords, uncompleted_items_new):
    current_champions[getChampionIndex(coords)].uncompletedItems = uncompleted_items_new

def changeCompletedItemsChamp(coords, completed_items_new):
    current_champions[getChampionIndex(coords)].completedItems = completed_items_new

def changeOnBoardBool(coords, onBoardBool):
    current_champions[getChampionIndex(coords)].onBoardBool = onBoardBool
    
def printChampsHelper(champ_list):
    for l in range(len(champ_list)):
        print(champ_list[l].name)
        print(champ_list[l].coords)
        print(champ_list[l].star)
        print(champ_list[l].uncompletedItems)
        print(champ_list[l].completedItems)

        print(champ_list[l].finalItems)
        print(champ_list[l].slot)
        print(champ_list[l].finalCompBool)
        print(champ_list[l].onBoardBool)

def printChampsHelperCurrentList(champ_list):
    for l in range(len(champ_list)):
        print(champ_list[l].name)
        print(champ_list[l].coords)
        print(champ_list[l].star)
        print(champ_list[l].uncompletedItems)

        print(champ_list[l].finalItems)
        print(champ_list[l].slot)
        print(champ_list[l].finalCompBool)
        print(champ_list[l].onBoardBool)

def print_champ_names(list):
    for l in range(len(list)):
        print(list[l].name)
        pass
        
def printChampsOnBoard():
    champions_on_board = []
    champions_on_bench = []
    for index in range(len(current_champions)):
        if(current_champions[index].onBoardBool == True):
            champions_on_board.append(current_champions[index])
        else:
            champions_on_bench.append(current_champions[index])
    print("Champs on board: \n")
    printChampsHelper(champions_on_board)
    print("\n \n")

    print("Champs on bench: \n")
    printChampsHelper(champions_on_bench)
    print("\n \n")

# TODO replace this function with smart data structure
def findHighestLvlOfThisChamp(name):
    lvl = 0
    for i in range(len(current_champions)):
        if(current_champions[i].name == name):
            if(current_champions[i].star > lvl):
                lvl = current_champions[i].star
    return lvl
def insertionSort(array):
    # start from 1 since element 0 is trivially sorted
    for i in range(1, len(array)):
        key = array[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key

def sortChampOnBoard():
    champs_on_board_coords_list = []
    champs_on_board_indexes = []
    for i in range(len(current_champions)):
        if(current_champions[i].onBoardBool):
            champs_on_board_coords_list.append(current_champions[i].coords)
    print(champs_on_board_coords_list)
    # TODO use "slot" in addChamp or ChangePos and supersede this part
    number_of_indexes_to_find = len(champs_on_board_coords_list)
    number_of_indexes_found = 0
    for l in range(len(coordinates.champs_on_board)):
        if(coordinates.champs_on_board[l] in champs_on_board_coords_list):
            champs_on_board_indexes.append(l)
            number_of_indexes_found += 1
            if(number_of_indexes_found == number_of_indexes_to_find):
                break
    insertionSort(champs_on_board_indexes)
    print(champs_on_board_indexes)
    return champs_on_board_indexes

# global variable, needed for board swap at krugs round
indexes_used = []

# addChamp("Illaoi", coordinates.champs_on_board[0], 1, [], [], 28, False, True)
# addChamp("ill", coordinates.champs_on_board[7], 1, [], [], 2, False, True)
# addChamp("ill", coordinates.champs_on_board[4], 1, [], [], 2, False, True)
# sortChampOnBoard()

# print(current_champions[0].slot)
# print(current_champions[1].slot)
# delChamp(coordinates.bench_champs[0])
# changePosChamp(coordinates.bench_champs[4], coordinates.bench_champs[1])
# print(current_champions[0].slot)
# print(current_champions[0].coords)
# lists = printChampsOnBoard()
