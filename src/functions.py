from decimal import ROUND_UP
from email.errors import MissingHeaderBodySeparatorDefect
from tokenize import cookie_re
from cv2 import CAP_PROP_OPENNI_MAX_TIME_DURATION, COLORMAP_SPRING, fastNlMeansDenoising, repeat
from numpy import append

import pydirectinput
from pyparsing import java_style_comment
from torch import le
import coordinates
import ocrFunctions
import generalData
import keyboardFunctions
import controlMode
import comps
import champions
import items

import cv2 as cv
import mss
import time
from datetime import datetime


# functions using ImageGrab
def get_lvl():
    lvl = ocrFunctions.get_text_ImageGrab(coordinates.current_lvl, 3, '10', '0123456789')
    if(lvl == ""):
        print("empty lvl")
        return -2
    lvl = int(lvl)
    if(lvl > 0 and lvl < 11):
        return lvl
    else:
        return -1

def get_lvl_progress():
    lvl_progress = ocrFunctions.get_text_ImageGrab(coordinates.lvl_status, 3, '10', '0123456789/Max')
    print(lvl_progress)
    if(lvl_progress == ""):
        print("empty lvl progress")
        return [0, -2]
    #if()
    if(lvl_progress == "Max"):
        lvl_progress = "0/999"
    if(not "/" in lvl_progress):
        return [0, -2]
    lvl_progress_list = []
    lvl_progress_list = lvl_progress.split("/")
    if(lvl_progress_list[0] == "" or lvl_progress_list[1] == ""):
        print("empty lvl progress")
        return [0, -2] 
    #print(lvl_progress_list)
    if(generalData.level_progress.__contains__(int(lvl_progress_list[1]))):
        error = False
    else:
        error = True
    lvl_progress_list[0] = int(lvl_progress_list[0])
    lvl_progress_list[1] = int(lvl_progress_list[1])
    if(not error):
        return lvl_progress_list
    if(error):
        return [0, -1]

def get_hp():
    #hp = int(ocrFunctions.get_text_ImageGrab(coordinates.hp, 3, '10', '0123456789'))
    hp = ocrFunctions.get_text_ImageGrab(coordinates.hp, 3, '10', '0123456789')
    print(hp)
    if(hp == ""):
        print("empty hp")
        return -2
    hp = int(hp)
    if(hp > 0 and hp < 136):
        return hp
    else:
        return -1

def get_gold():
    gold = ocrFunctions.get_text_ImageGrab(coordinates.current_gold, 3, '10', '0123456789')
    if(gold == ""):
        return -1
    else:
        gold = int(gold)
    if(gold >= 0):
        return gold
    else:
        return -1

def get_stage():
    stage_one = ocrFunctions.get_text_ImageGrab(coordinates.stage_one, 3, '7', '0123456789-')
    #print(stage_one)
    stage_two_plus = ocrFunctions.get_text_ImageGrab(coordinates.stage_two_plus, 3, '7', '0123456789-')
    if(generalData.rounds.__contains__(stage_one)):
        return stage_one
    elif(generalData.rounds.__contains__(stage_two_plus)):
        return stage_two_plus
    else:
        return "Couldn't read stage number"

def get_stage2():
    stage_one = ocrFunctions.get_text_advanced(coordinates.stage_one)
    stage_two_plus = ocrFunctions.get_text_advanced(coordinates.stage_two_plus)
    if(generalData.rounds.__contains__(stage_one)):
        return stage_one
    elif(generalData.rounds.__contains__(stage_two_plus)):
        return stage_two_plus
    else:
        return "Couldn't read stage number"

def get_stage_type_without_screenshot(stage) -> str:
    if(generalData.pvp_round.__contains__(stage)):
        return "pvp"
    if(generalData.pve_round.__contains__(stage)):
        return "pve"
    if(generalData.carousel_round.__contains__(stage)):
        return "carousel"
    if(generalData.carousel_round_first.__contains__(stage)):
        return "first_carousel"
    if(generalData.augment_pvp_round.__contains__(stage)):
        return "augment_pvp"


def get_text_you_finished() -> str:
    return ocrFunctions.get_text_ImageGrab(coordinates.you_finished, 3, '7', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ')

def get_text_continue() -> str:
    return ocrFunctions.get_text_ImageGrab(coordinates.continue_after_victory, 3, '10', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ')

def get_text_augment(augment_pos):
    augment_coords = coordinates.getAugmentCoords()

    augment_name = ocrFunctions.get_text_ImageGrab(augment_coords[augment_pos], 3, '10', 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(augment_name)

    # augment name correction
    augment_name_list = []
    augment_name_list[:0] = augment_name

    if(augment_name_list[len(augment_name) - 3] == "I" and (augment_name_list[len(augment_name)- 2] == "l" or augment_name_list[len(augment_name)- 1] == "l")):
        augment_name_list[len(augment_name) - 1] = "I"
        augment_name_list[len(augment_name) - 2] = "I"

    elif(augment_name_list[len(augment_name)- 2] == "I" and augment_name_list[len(augment_name) - 1] == "l"):
        augment_name_list[len(augment_name) - 1] = "I"
    augment_name = "".join(augment_name_list)
    
    if(generalData.augments.__contains__(augment_name)):
        return augment_name

    else:
        return "Error in retrieving augment name"

def get_champ_name(coords):
    champ_name = ocrFunctions.get_text_ImageGrab_champ_names(coords, 3)
    print(champ_name)
    if(champ_name == "" or champ_name == "Be" or champ_name == "re" or champ_name == "ee"):
        return "-"
    if(champ_name == "Parie"):
        return "Taric"
    if(generalData.champions.__contains__(champ_name)):
        return champ_name
    else:
        return get_champ_with_longest_same_substring(find_champ_with_longest_same_substring(champ_name))

# game functions
# if false, leave game
def still_alive() -> bool:
    if(ocrFunctions.get_text_ImageGrab(coordinates.you_finished, 3, '10', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ') == "YOUFINISHED"):
        return False
    if(ocrFunctions.get_text_ImageGrab(coordinates.continue_after_victory, 3, '10', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') == "CONTINUE"):
        return False
    else:
        return True

def find_best_augment(augment1, augment2, augment3) -> int:
    print("     find best augment")
    if(controlMode.lux_comp_active):
        augments_ranked = comps.lux_augments_ranked
    positions = []
    if(augment1 == "Error in retrieving augment name"):
        positions.append(250)
    else:
        positions.append(augments_ranked.index(augment1))

    if(augment2 == "Error in retrieving augment name"):
        positions.append(250)
    else:
        positions.append(augments_ranked.index(augment2))

    if(augment3 == "Error in retrieving augment name"):
        positions.append(250)
    else:
        positions.append(augments_ranked.index(augment3))
    
    print(positions)
    # find smallest value and return position out of list
    min_value = positions[0]
    pos_min_value = 0
    for value in positions:
        if value < min_value:
            min_value = value
    for value in positions:
        if min_value == value:
            return pos_min_value
        pos_min_value += 1

def calculate_money_to_lvl_up(lvl_progress_list):
    xp_needed = lvl_progress_list[1] - lvl_progress_list[0]
    #TODO: adapt variables for augments
    xp_per_buy = 4
    cost_per_buy = 4
    number_buys_needed = int(xp_needed/xp_per_buy) + (xp_needed % xp_per_buy > 0)
    return number_buys_needed * cost_per_buy

def spend_money(gold, gold_needed_to_lvl_up, shop, lvl, missing_xp_to_lvl_up):
    added_xp = 0
    # buy champs
    if(gold >= 50):
        while(True):
            for i in range(len(shop)):
                if(shop[i] in comps.lux_comp_champs):
                    # check if champ reached his supposed lvl, if not buy champ
                    # TODO replace this function with smart data structure
                    star = champions.findHighestLvlOfThisChamp(shop[i])
                    if(star < comps.lux_comp_stars[shop[i]]):
                        keyboardFunctions.buy_champ(i)
                        gold -= comps.lux_comp_cost_dict[shop[i]]
                    
                    if(not comps.lux_comp_champs_max_star_reached[shop[i]]):
                        keyboardFunctions.buy_champ(i)
                        gold -= comps.lux_comp_cost_dict[shop[i]]                       
            # strategy lvl on 5, roll on 6, lvl on 7
            if(lvl == 4 or lvl == 5 or lvl == 6 and comps.lux_comp_champs_max_star_reached["Lux"] or lvl == 7):
                while(gold >= 54):
                    # lvl up
                    keyboardFunctions.level_up()
                    added_xp += 4
                    gold -= 4     

            if added_xp >= missing_xp_to_lvl_up: lvl += 1

            if gold < 54: break
            else: 
                keyboardFunctions.reroll()
                gold -= 2
                shop = get_champ_names_shop_smart()

    else:
        for i in range(len(shop)):
            if(shop[i] in comps.lux_comp_champs):
                # check if champ reached his supposed lvl
                # TODO replace this function with smart data structure
                star = champions.findHighestLvlOfThisChamp(shop[i])
                if(star < comps.lux_comp_stars[shop[i]]):
                    keyboardFunctions.buy_champ(i)
                    gold -= comps.lux_comp_cost_dict[shop[i]]
    return lvl
        

def pick_up_orbs():
    print("pick up orbs")
    tru = True
    while(tru):
        loc1 = ocrFunctions.find_lots_of_orbs('common')
        if(loc1 != (0,0)):
            keyboardFunctions.right_click((loc1))
        loc2 = ocrFunctions.find_lots_of_orbs('rare')
        if(loc2 != (0,0)):
            keyboardFunctions.right_click((loc2))
        loc3 = ocrFunctions.find_lots_of_orbs('legendary')
        if(loc3 != (0,0)):
            keyboardFunctions.right_click((loc3))
        if(loc1 == (0,0) and loc2 == (0,0) and loc3 == (0,0)):
            tru = False

def get_champ_names_shop_smart():
    image_bench = ocrFunctions.take_screenshot()
    names = []
    for i in range(0, 9 ,2):
        top_left = coordinates.champ_names_shop[i]
        bottom_right = coordinates.champ_names_shop[i + 1]
        current_focus = image_bench[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        name = ocrFunctions.get_text_from_image(current_focus, 3, bottom_right[1] - top_left[1], bottom_right[0] - top_left[0])
        #print(name)
        
        if(generalData.champions.__contains__(name)):
            names.append(name)
        elif(name == ""):
            names.append("-")
        else:
            most_similair_name = get_champ_with_longest_same_substring(find_champ_with_longest_same_substring(name))
            names.append(most_similair_name)
    return names

def find_champ_with_longest_same_substring(name_ocr):
    length_longest_substring = []
    for i in range(len(generalData.champions_list)):
        longest_substring_found = False
        for l in range(len(generalData.champions_list[i])):
            # if(longest_substring_found):
            #     print("break")
            #     break
            for m in range(l + 1):
                if(longest_substring_found):
                    break
                champ_name = generalData.champions_list[i][0 + m:len(generalData.champions_list[i]) - l + m]
                #print(champ_name)
                if(name_ocr.find(champ_name) != -1):
                    length_longest_substring.append(len(champ_name))
                    longest_substring_found = True
        if(not longest_substring_found):
            length_longest_substring.append(0)
    return length_longest_substring

def get_champ_with_longest_same_substring(substring_length_list):
    longest_sub = max(substring_length_list)
    return generalData.champions_list[substring_length_list.index(longest_sub)] # return index

def find_item_with_longest_same_substring(name_ocr):
    length_longest_substring = []
    for i in range(len(generalData.item_parts_list)):
        longest_substring_found = False
        for l in range(len(generalData.item_parts_list[i])):
            # if(longest_substring_found):
            #     print("break")
            #     break
            for m in range(l + 1):
                if(longest_substring_found):
                    break
                item_part_name = generalData.item_parts_list[i][0 + m:len(generalData.item_parts_list[i]) - l + m]
                #print(champ_name)
                if(name_ocr.find(item_part_name) != -1):
                    length_longest_substring.append(len(item_part_name))
                    longest_substring_found = True
        if(not longest_substring_found):
            length_longest_substring.append(0)
    return length_longest_substring
#print(get_champ_with_longest_same_substring(find_champ_with_longest_same_substring("")))

def get_item_with_longest_same_substring(substring_length_list):
    longest_sub = max(substring_length_list)
    return generalData.item_parts_list[substring_length_list.index(longest_sub)]
    
def search_for_new_champs_on_bench_stage_1_2():
    print("     search_for_new_champs_on_bench_stage_1_2")
    #TODO: recognize star lvl
    # we assume star lvl 1 at the moment

    # look for items
    result_item = ocrFunctions.find_items_on_champs()
    
    # look for champs
    keyboardFunctions.right_click(coordinates.bench_champs[0])
    champ_name = get_champ_name((coordinates.champ_name_bench[0], coordinates.champ_name_bench[1]))
    keyboardFunctions.move_things(coordinates.bench_champs[0], coordinates.champs_on_board[24])
    print(champ_name)
    print(result_item)
    if(champ_name == "-"):
        print("no champ detected")
        pass 
    else:
        finalCompBool = False
        if(champ_name in comps.lux_comp_champs):
            finalCompBool = True
        champions.addChamp(champ_name, coordinates.bench_champs[0], 1, result_item[1], [], 0, finalCompBool, False)
        champions.changePosChamp(coordinates.bench_champs[0], coordinates.champs_on_board[24])
    # print("champs on board:")
    # for i in range(len(champions.current_champions)):
    #     if(champions.current_champions[i].onBoardBool):
    #         print(champions.current_champions[i].name)
    # print("champs on bench:")
    # for i in range(len(champions.current_champions)):
    #     if(not champions.current_champions[i].onBoardBool):
    #         print(champions.current_champions[i].name)

def search_for_new_champs_on_bench_1_3():
    print("     search for new champs on bench 1 3")
    #TODO: recognize star lvl
    # we assume star lvl 1 at the moment
    
    # look for champs
    for i in range(3):
        j = i * 2
        new_item_name = None
        keyboardFunctions.right_click(coordinates.bench_champs[i])
        keyboardFunctions.halt_movement()
        champ_name = get_champ_name((coordinates.champ_name_bench[j], coordinates.champ_name_bench[j + 1]))
        print(champ_name)

        if(champ_name == "-"):
            print("no champ detected")
            pass
        else:
            # if(champions.getChampionIndex(coordinates.bench_champs[i]) == -1):
            #     for l in range(len(slot_name)):
            #         current_slot_name = slot_name[l]
            #         current_slot = current_slot_name[0]
            #         if(current_slot == 0):
            #             new_item_name = current_slot_name[1]
            #             print(new_item_name)
            #             continue
            finalCompBool = False
            if(champ_name in comps.lux_comp_champs):
                finalCompBool = True            
            champions.addChamp(champ_name, coordinates.bench_champs[i], 1, new_item_name, [], 0, finalCompBool, False)

    # print(champions.current_champions)
    # champions.printChampsHelperCurrentList(champions.current_champions)
    # champions.print_champ_names(champions.current_champions)
    print("champs on board:")
    for i in range(len(champions.current_champions)):
        if(champions.current_champions[i].onBoardBool):
            print(champions.current_champions[i].name)
            pass
    print("champs on bench:")
    for i in range(len(champions.current_champions)):
        if(not champions.current_champions[i].onBoardBool):
            print(champions.current_champions[i].name)
            pass
def search_for_new_champs_on_bench():
    print("     search for new champs on bench")
    #TODO: recognize star lvl
    # we assume star lvl 1 at the moment

    # look for items
    result = ocrFunctions.find_items_on_champs()
    result_coords = []
    result_name = []
    slot_name = []
    for i in range(len(result)):
        if(i % 2 == 0):
            result_coords.append(result[i])
        if(i % 2 == 1):
            result_name.append(result[i])
    print(result_coords)
    print(result_name)
    for i in range(len(result_coords)):
        comparable_coords = result_coords[i]
        for l in range(len(coordinates.items_on_bench_champs) - 1):
            if(comparable_coords[0] >= coordinates.items_on_bench_champs[l] and comparable_coords[0] <= coordinates.items_on_bench_champs[l + 1]):
                slot_name_tuple = (l, result_name[i])
                slot_name.append(slot_name_tuple)
                continue
    # look for champs
    for i in range(len(coordinates.bench_champs)):
    # for i in range(1): # for test purposes
    #     i = 4
        new_item_name = None
        #keyboardFunctions.right_click(coordinates.top_mid_screen)
        #print(i)
        j = i * 2
        keyboardFunctions.right_click(coordinates.bench_champs[i])
        keyboardFunctions.halt_movement()
        champ_name = get_champ_name((coordinates.champ_name_bench[j], coordinates.champ_name_bench[j + 1]))
        print(champ_name)

        if(champ_name == "-"):
            print("no champ detected")
            pass
        else:
            # if champ not yet registered
            if(champions.getChampionIndex(coordinates.bench_champs[i]) == -1):
                for l in range(len(slot_name)):
                    current_slot_name = slot_name[l]
                    current_slot = current_slot_name[0]
                    if(current_slot == i):
                        new_item_name = current_slot_name[1]
                        print(new_item_name)
                        continue
            finalCompBool = False
            if(champ_name in comps.lux_comp_champs):
                finalCompBool = True 
            champions.addChamp(champ_name, coordinates.bench_champs[i], 1, new_item_name, [], 0, finalCompBool, False)

    # print(champions.current_champions)
    # champions.printChampsHelperCurrentList(champions.current_champions)
    # champions.print_champ_names(champions.current_champions)
    print("champs on board:")
    for i in range(len(champions.current_champions)):
        if(champions.current_champions[i].onBoardBool):
            print(champions.current_champions[i].name)
            pass
    print("champs on bench:")
    for i in range(len(champions.current_champions)):
        if(not champions.current_champions[i].onBoardBool):
            print(champions.current_champions[i].name)
            pass

def sell_champs_on_bench():
    print("     sell champs on bench")
    champs_to_delete = []
    # sell champs which aren't in our comp and remember index
    for i in range(len(champions.current_champions)):
        if(not champions.current_champions[i].name in comps.lux_comp_champs and not champions.current_champions[i].onBoardBool):
            print(champions.current_champions[i].name)
            print("not comp champ on bench")
            keyboardFunctions.sell_champ(champions.getChampionCoords(i))
            champs_to_delete.append(i)
        elif(champions.current_champions[i].name in comps.lux_comp_champs and not champions.current_champions[i].onBoardBool):
            if(comps.lux_comp_champs_max_star_reached[champions.current_champions[i].name]):
                print(champions.current_champions[i].name)
                print("comp champ on bench and max star reached")
                keyboardFunctions.sell_champ(champions.getChampionCoords(i))
                champs_to_delete.append(i)
    # get rid of champs in current_champions/documentation
    print(champs_to_delete)
    for i in range(len(champs_to_delete) - 1, -1, -1):
        champions.delChamp(champions.getChampionCoords(champs_to_delete[i]))

def search_for_new_items_on_bench():
    print("     search for new items on bench")
    items.current_items = []
    items.current_items_on_bench = []
    for i in range(len(controlMode.item_bench_layout)):
        j = 2 * i
        # keyboardFunctions.right_click(coordinates.top_right_screen)
        keyboardFunctions.left_click(coordinates.top_right_screen)
        keyboardFunctions.right_click(controlMode.item_bench_layout[i])
        keyboardFunctions.halt_movement()
        item_name = ocrFunctions.get_text_ImageGrab_champ_names((controlMode.item_bench_name_layout[j], controlMode.item_bench_name_layout[j + 1]), 3)
        print(item_name)

        # check if retrieved item name is valid
        valid = False
        if(len(item_name) > 5):
            valid = True
            item_part_name = get_item_with_longest_same_substring(find_item_with_longest_same_substring(item_name))
            print(item_part_name)

        # for l in range(len(generalData.items_list)):
        #     if(item_name.find(generalData.items_list[l]) != -1):
        #         item_name = generalData.items_list[l]
        #         valid = True
        #         break
        print(valid)
        if(not valid):
            continue # TODO insert equal function

        else:
            if(items.getItemIndex(controlMode.item_bench_layout[i]) == -1): # if item doesnt exists yet as a digital copy
                print(controlMode.get_index_of_items_on_bench(controlMode.item_bench_layout[i]))
                items.addItem(item_part_name, controlMode.item_bench_layout[i], True)

    print(items.current_items)
    items.printItemsHelperCurrentList(items.current_items)

    if(not len(items.current_items) == 0):
        return True # item bench not empty
    else:
        return False

def equip_items():
    # check if champs (item carriers) are on board, if so check if both item parts are there and give them completed item
    for big_index in range(len(comps.champs_with_items)):
        champ = comps.champs_with_items[big_index]
        item_carrier_on_board = False
        # search champ and get pos (for easy version: just give item to pos where champ should be according to final comp)
        for champs in range(len(champions.current_champions)):
            if(champions.current_champions[champs].name == champ and champions.current_champions[champs].onBoardBool):
                print("champ ready:")
                print(champions.current_champions[champs].name)
                place_item_here = champions.current_champions[champs].coords
                item_carrier_on_board = True

        # look for matching items if the item carrier is on board
        #TODO: same item cant be given twice on same champ per game and loop/check for other items
        both_parts_available = False
        if(item_carrier_on_board):
            # looking for two matching item parts of this certain item carrier
            while(not both_parts_available):
                print("in loop")
                specific_item_list = comps.item_lists[big_index]
                print(specific_item_list)
                for i in range(len(specific_item_list)):
                    pair_one_available = False
                    pair_two_available = False
                    item_pair = generalData.dict_full_items_craftable[specific_item_list[i]]
                    print(item_pair)
                    for l in range(len(items.current_items)):
                        print("in inner for loop")
                        if(item_pair[0] == items.current_items[l].name and items.current_items[l].onBench):
                            print("found part one")
                            pair_one_available = True
                            item_one_index = l
                            for m in range(len(items.current_items)):
                                if(item_pair[1] == items.current_items[m].name and items.current_items[m].onBench and items.current_items[m].coords != items.current_items[item_one_index].coords):
                                    print("found part two")
                                    pair_two_available = True
                                    item_two_index = m
                    items_equipped = comps.equipped_items_boolean_lists[big_index]
                    item_already_on_champ = items_equipped[i]
                    if(pair_one_available and pair_two_available and not item_already_on_champ):
                        print("found both parts")
                        print(item_one_index)
                        print(item_two_index)

                        both_parts_available = True
                        keyboardFunctions.move_things(items.current_items[item_one_index].coords, place_item_here)
                        keyboardFunctions.move_things(items.current_items[item_two_index].coords, place_item_here)
                        if(item_one_index > item_two_index):
                            items.delItem(items.current_items[item_one_index].coords)
                            items.delItem(items.current_items[item_two_index].coords)
                        else:
                            items.delItem(items.current_items[item_two_index].coords)
                            items.delItem(items.current_items[item_one_index].coords)
                        
                        # set specific item is equipped by specific champ true
                        items_equipped[i] = True

                        print("moved items")

                if(not both_parts_available):
                    print("here")
                    break
    print("finished")

# TODO include augment +1 teamsize
def place_how_many_champs_on_board(lvl):
    num_champs_on_board = champions.getNumberOfChampionsOnBoard()
    print("so many champs are on board " + str(num_champs_on_board))
    print(lvl-num_champs_on_board)
    return lvl - num_champs_on_board

def get_how_many_unique_wanted_champs_registered():
    counter = 0
    for i in range(len(comps.lux_comp_champs_on_board)):
            if(comps.lux_comp_champs_on_board[comps.lux_comp_champs_list[i]]):
                counter += 1
    return counter

def get_empty_space_on_board():
    list_not_available_slots = []
    for i in range(len(champions.current_champions)):
        if(champions.current_champions[i].onBoardBool):
            list_not_available_slots.append(champions.getChampionIndex(champions.current_champions[i].coords))
    for i in range(len(coordinates.champs_on_board)):
        if(not i in list_not_available_slots and not i in comps.lux_comp_placement_on_board_list):
            print("empty slot on board:" + str(i))
            return i

def get_empty_space_on_bench():
    list_not_available_slots = []
    for i in range(len(champions.current_champions)):
        if(not champions.current_champions[i].onBoardBool):
            for l in range(len(coordinates.bench_champs)):
                if(coordinates.bench_champs[l] == champions.current_champions[i].coords):
                    list_not_available_slots.append(l)
    for i in range(len(coordinates.bench_champs)):
        if(not i in list_not_available_slots):
            print("empty slot on bench:" + str(i))
            return i

def get_team_in_order(lvl):
    print("GET TEAM IN ORDER")
    print("lvl: " + str(lvl))
    champsCoordsToDelete = []
    deletedChampsNumber = 0
    # iteration for every registered champion in current_champions
    for i in range(len(champions.current_champions)):
        print(get_how_many_unique_wanted_champs_registered())
        # access loop if champ is part of comp and there is no examplar of this comp champ on board yet
        if(champions.current_champions[i].name in comps.lux_comp_champs and not comps.lux_comp_champs_on_board[champions.current_champions[i].name]):
            # if a comp champ is needed on board, place this champ on board
            if(lvl - get_how_many_unique_wanted_champs_registered() > 0):
                place_champ_here_index = comps.lux_comp_placement_on_board[champions.current_champions[i].name]
                print(champions.current_champions[i].name)
                print(place_champ_here_index)
                keyboardFunctions.move_things(champions.current_champions[i].coords, coordinates.champs_on_board[place_champ_here_index])
                champions.changePosChamp(champions.current_champions[i].coords, coordinates.champs_on_board[place_champ_here_index])
                comps.lux_comp_champs_on_board[champions.current_champions[i].name] = True
            else:
                print("ssss")
                return True
        elif(champions.current_champions[i].name in comps.lux_comp_champs and champions.current_champions[i].onBoardBool and champions.current_champions[i].coords == coordinates.champs_on_board[comps.lux_comp_placement_on_board[champions.current_champions[i].name]]):
            print("s")
            pass
        # if champ is part of comp and on board but not on his allocated position, therefore place champ on bench
        elif(champions.current_champions[i].name in comps.lux_comp_champs and champions.current_champions[i].onBoardBool and not champions.current_champions[i].coords == coordinates.champs_on_board[comps.lux_comp_placement_on_board[champions.current_champions[i].name]]):
            # place from board on bench
            print("x")
            empty_space_on_bench = get_empty_space_on_bench()
            keyboardFunctions.move_things(champions.current_champions[i].coords, coordinates.bench_champs[empty_space_on_bench])
            champions.changePosChamp(champions.current_champions[i].coords, coordinates.bench_champs[empty_space_on_bench])
        # don't sell comp champs 
        elif(champions.current_champions[i].name in comps.lux_comp_champs):
            print("ss")
            pass
        # sell random champ that is not on board
        elif(not champions.current_champions[i].name in comps.lux_comp_champs and not champions.current_champions[i].onBoardBool):
            print("sss")
            keyboardFunctions.sell_champ(champions.current_champions[i].coords)
            champsCoordsToDelete.append(champions.current_champions[i].coords)
            deletedChampsNumber += 1
        # sell random champ
        else:
            print("xx")
            keyboardFunctions.sell_champ(champions.current_champions[i].coords)
            champsCoordsToDelete.append(champions.current_champions[i].coords)
            deletedChampsNumber += 1
    
    print(champsCoordsToDelete)
    for i in range(len(champsCoordsToDelete) - 1, -1, -1):
        champions.delChamp(champsCoordsToDelete[i])

# TODO: replace checking if champion name is in comps.lux_comp_champs, check if champ is finalCompBool
def add_random_champ_on_board_if_needed(lvl, shop):
    how_many_random_champs_need_to_be_placed_on_board = lvl - get_how_many_unique_wanted_champs_registered()
    print(how_many_random_champs_need_to_be_placed_on_board)
    bench_empty = False
    while(how_many_random_champs_need_to_be_placed_on_board > 0 and not bench_empty):
        # get random champ on board, either from bench
        for i in range(len(champions.current_champions)):
            if(not champions.current_champions[i].onBoardBool and not champions.current_champions[i].name in comps.lux_comp_champs):
                print("from bench")
                keyboardFunctions.move_things(champions.current_champions[i].coords, coordinates.champs_on_board[i])
                champions.changePosChamp(champions.current_champions[i].coords, coordinates.champs_on_board[i])
                how_many_random_champs_need_to_be_placed_on_board -= 1
                continue
        bench_empty = True
    # or shop
    if(how_many_random_champs_need_to_be_placed_on_board):  
        shop_counter = -1
        shop_useable_indizes = []
        for i in range(len(shop)):
            if(not shop[i] in comps.lux_comp_champs):
                shop_useable_indizes.append(i)
                shop_counter += 1

        if(shop_counter == -1):
            # TODO might implement to refresh store and look again for champs to buy
            pass
        else:
            print(shop_counter)
            # while champs are needed and champs are available in shop, buy and place em on the board 
            while(how_many_random_champs_need_to_be_placed_on_board > 0 and len(shop_useable_indizes) > 0):
                keyboardFunctions.buy_champ(shop_useable_indizes[0])
                # find out where on bench bought champ is
                bought_champ_is_here = get_empty_space_on_bench()
                free_slot_on_board = get_empty_space_on_board()
                keyboardFunctions.move_things(coordinates.bench_champs[bought_champ_is_here], coordinates.champs_on_board[free_slot_on_board])
                champions.addChamp(shop[shop_useable_indizes[0]], coordinates.champs_on_board[free_slot_on_board], 1, [], [], bought_champ_is_here, False, True)
                how_many_random_champs_need_to_be_placed_on_board -= 1
                del shop_useable_indizes[0]
                print("from shop")

def show_what_the_programm_thinks_how_board_looks_like():
    board = []
    bench = []
    for i in range(len(champions.current_champions)):
        for l in range(len(coordinates.champs_on_board)):
            if(champions.current_champions[i].coords == coordinates.champs_on_board[l]):
                board.append((champions.current_champions[i].name, l))
    for i in range(len(champions.current_champions)):
        for l in range(len(coordinates.bench_champs)):
            if(champions.current_champions[i].coords == coordinates.bench_champs[l]):
                bench.append((champions.current_champions[i].name, l))
    print(board)
    print(bench)

def show_what_the_programm_thinks_how_board_looks_like2():
    board = []
    bench = []
    for i in range(len(champions.current_champions)):
            if(champions.current_champions[i].onBoardBool):
                board.append((champions.current_champions[i].name))
    for i in range(len(champions.current_champions)):
            if(not champions.current_champions[i].onBoardBool):
                bench.append((champions.current_champions[i].name))
    print(board)
    print(bench)

# main function while game is running, calls functions for different stage types
def game_strategy():
    last_stage = "1-0"
    alive = True
    # while alive retrieve stages and compare to last one, in order to determine stage changes
    while(alive):
        alive = still_alive()
        print(alive)
        if(not alive):
            continue
        current_stage = get_stage()
        print(current_stage)
        print(last_stage)
        if(current_stage == "Couldn't read stage number"):
            continue
        if(last_stage != current_stage):
            if(get_stage_type_without_screenshot(current_stage) == "first_carousel"):
                carousel_round_first()
            if(get_stage_type_without_screenshot(current_stage) == "carousel"):
                carousel_round()
            if(get_stage_type_without_screenshot(current_stage) == "pve"):
                pve_round(current_stage)
            if(get_stage_type_without_screenshot(current_stage) == "pvp"):
                pvp_round()
            if(get_stage_type_without_screenshot(current_stage) == "augment_pvp"):
                time.sleep(1.5)
                augment_round()
                pvp_round()

        last_stage = current_stage
        time.sleep(1)
    print("leave game")
    time.sleep(10)

def carousel_round_first():
    # TODO: either while with global variable until we are in post carousel stage or we check if there is still the blue mascot standing
    for i in range(11):
        keyboardFunctions.right_click(coordinates.carousel_low_mid_pos)
        time.sleep(0.5)
    print("carousel")

def carousel_round():
    # TODO: either while with global variable until we are in post carousel stage or we check if there is still the blue mascot standing
    for i in range(28):
        keyboardFunctions.right_click(coordinates.carousel_low_mid_pos)
        time.sleep(0.5)
    print("carousel")

#TODO fix function for lvl-champsonboard > 1
def give_special_champs_right_pos(lvl):
    print("     give special champs right pos")
    onBoardcounter = 0
    dragonOnBoard = False
    noCompChampFound = True
    notAvailableSlotsOnBoard = []
    canMove = False

    for i in range(len(champions.current_champions)):
        if(champions.current_champions[i].onBoardBool):
            onBoardcounter += 1
            notAvailableSlotsOnBoard.append(champions.current_champions[i].coords)
        if("AurelionSol" == champions.current_champions[i].name and champions.current_champions[i].onBoardBool):
            dragonOnBoard = True
        if(not champions.current_champions[i].onBoardBool and noCompChampFound):
            if(champions.current_champions[i].name in comps.lux_comp_champs):
                champToMove = champions.current_champions[i]
                canMove = True
                noCompChampFound = False
            else:
                champToMove = champions.current_champions[i]
                canMove = True
    if(dragonOnBoard): #TODO: insert 
        pass
    else:
        if(lvl > onBoardcounter and canMove):
            # place champ that isn't on Board, on Board
            print("     slots on board that arent available")
            print(notAvailableSlotsOnBoard)
            # only for one champ to place yet, needs work
            for l in range(len(coordinates.champs_on_board)):
                if(not coordinates.champs_on_board[l] in notAvailableSlotsOnBoard):
                    champ_to_here_slot_on_board = coordinates.champs_on_board[l]
                    break
            keyboardFunctions.move_things(champToMove.coords, champ_to_here_slot_on_board)
            #champions.changeOnBoardBool(champToMove.coords, True)
            champions.changePosChamp(champToMove.coords, champ_to_here_slot_on_board)

def sell_first_champ_if_necessary():
    if(len(champions.current_champions) == 0):
        keyboardFunctions.sell_champ(coordinates.champs_on_board[24])
        return True

    elif(champions.current_champions[0].name in comps.lux_comp_champs):
        # keep champ if he has item he needs, sell him if he has different item
        if(champions.current_champions[0].name in comps.champs_with_items):
            for i in range(len(comps.champs_with_items)):
                item_needed = False
                items_searched_for = comps.item_lists[i]
                for i in range(len(items_searched_for)):
                    if(champions.current_champions[0].uncompletedItems in generalData.dict_full_items_craftable[items_searched_for[i]]):
                        item_needed = True
                if(not item_needed):
                    coords = champions.current_champions[0].coords
                    pydirectinput.moveTo(coords[0], coords[1])
                    time.sleep(0.5)
                    pydirectinput.press("e")
                    keyboardFunctions.sell_champ(coords)
                    champions.delChamp(champions.current_champions[0].coords)
                    # sold
                    return True
                else:
                    # not sold
                    return False

        # if champs (that are part of comp, but don't need items) have item that other champs need, sell em, if they have different item keep em
        else:
            item_found = False
            for i in range(len(comps.champs_with_items)):
                items_searched_for = comps.item_lists[i]
                for i in range(len(items_searched_for)):
                    if(champions.current_champions[0].uncompletedItems in generalData.dict_full_items_craftable[items_searched_for[i]]):
                        item_found = True
                        break
            if(item_found):
                coords = champions.current_champions[0].coords
                pydirectinput.moveTo(coords[0], coords[1])
                time.sleep(0.5)
                pydirectinput.press("e")   
                keyboardFunctions.sell_champ(coords)             
                champions.delChamp(champions.current_champions[0].coords)
                # sold
                return True
            else:
                # not sold
                return False
    else:
        # not future champ, sold
        coords = champions.current_champions[0].coords
        pydirectinput.moveTo(coords[0], coords[1])
        time.sleep(0.5)
        pydirectinput.press("e")   
        keyboardFunctions.sell_champ(coords)
        champions.delChamp(champions.current_champions[0].coords)
        return True

def get_index_of_final_comp_champ_in_shop(shop):
    for i in range(len(shop)):
        if(shop[i] in comps.lux_comp_champs):
            return i

def delete_elements_on_bench():
    to_delete = []
    for i in range(len(champions.current_champions)):
        if(not champions.current_champions[i].onBoardBool):
            to_delete.append(i)
    for i in range(len(to_delete) - 1, -1, -1):
        champions.delChamp(champions.current_champions[to_delete[i]].coords)

def pve_round(stage):

    if(stage == "1-2"):
        print("now in 1-2")
        search_for_new_champs_on_bench_stage_1_2()
        # time.sleep(5)
        # pick_up_orbs()

        show_what_the_programm_thinks_how_board_looks_like()
    elif(stage == "1-3"):
        print("now in 1-3")

        lvl = 2

        need_to_buy_second_champ = sell_first_champ_if_necessary()
        # spend money, buying champs, buying xp, sell champs
        test_gold = 10

        # version 2:
        shop = get_champ_names_shop_smart()
        if(need_to_buy_second_champ):
            if(len(set(shop).intersection(comps.lux_comp_champs)) > 1):
                # buy champion that fit in comp
                print(">1")
                spend_money(test_gold, 10, shop, lvl, 0)
            elif(len(set(shop).intersection(comps.lux_comp_champs)) > 0):
                # buy one champion that fits in comp and one random one
                print(">0")
                spend_money(test_gold, 10, shop, lvl, 0)
                for i in range(4):
                    if(i != get_index_of_final_comp_champ_in_shop(shop)):
                        buy_random_champ_index = i
                keyboardFunctions.buy_champ(buy_random_champ_index)
            else:
                # buy two random champions
                keyboardFunctions.buy_champ(0)
                keyboardFunctions.buy_champ(1)
        else:
            if(len(set(shop).intersection(comps.lux_comp_champs)) > 0):
                # buy champion that fit in comp
                spend_money(test_gold, 10, shop, lvl, 0)
            else:
                # buy one random champion
                keyboardFunctions.buy_champ(0)           

        # check for new champs on bench       
        search_for_new_champs_on_bench_1_3()

        # put champ on board if one space open
        give_special_champs_right_pos(lvl)

        if(need_to_buy_second_champ):
            give_special_champs_right_pos(lvl)

        sell_champs_on_bench()
        pick_up_orbs()

        # check for new champs on bench       
        search_for_new_champs_on_bench_1_3()
        sell_champs_on_bench()

        spend_money(test_gold, 10, shop, lvl, 0)
        show_what_the_programm_thinks_how_board_looks_like()

    elif(stage == "1-4"):
        # press button ones in game to see hp
        keyboardFunctions.left_click(coordinates.button_for_hp)

        lvl = 3
        # spend money, buying champs, buying xp, sell champs
        test_gold = 10
        shop = get_champ_names_shop_smart()
        if(len(set(shop).intersection(comps.lux_comp_champs)) > 0):
            # buy champions that fit in comp
            spend_money(test_gold, 10, shop, lvl, 0)
        else:
            # buy one random champion
            keyboardFunctions.buy_champ(0)

        # check for new champs on bench       
        search_for_new_champs_on_bench_1_3()

        # put champ on board if one space open
        give_special_champs_right_pos(lvl)
    
        sell_champs_on_bench()

        print("now in 1-4")
        pick_up_orbs()

        # check for new champs on bench       
        search_for_new_champs_on_bench_1_3()
        sell_champs_on_bench()

        spend_money(test_gold, 10, shop, lvl, 0)
        show_what_the_programm_thinks_how_board_looks_like()
    else:
        missing_xp_to_lvl_up = 1
        lvl_progress = get_lvl_progress()
        if(lvl_progress[1] == -1 or lvl_progress[1] == -2):
            print("Error in retrieving lvl progress")
            lvl = get_lvl()
        else:
            print(lvl_progress)
            lvl = 0
            for i in range(len(generalData.level_progress)):
                if(lvl_progress[1] == generalData.level_progress[i]):
                    lvl = i + 2
                    break
            missing_xp_to_lvl_up = lvl_progress[1] - lvl_progress[0]
            # lvl lvl still 0
            if(not lvl):
                print("this one")
                lvl = get_lvl()

        gold = get_gold()
        if(gold != -1):
            print(gold)
            pass
        else:
            print("Error in retrieving gold")
            pass
        
        # spend money, buying champs, buying xp, sell champs
        shop = get_champ_names_shop_smart()
        spend_money(gold, 10, shop, lvl, missing_xp_to_lvl_up)

        # search for loot
        pick_up_orbs()

        # delete champs out of current champ list that are on board
        delete_elements_on_bench()

        # check for new champs on bench
        search_for_new_champs_on_bench()

        # get champs on board in order
        get_team_in_order(lvl)

        # put champ on board if one space open
        give_special_champs_right_pos(lvl)
        
        # search items
        item_found = search_for_new_items_on_bench()
        if(not controlMode.layout_recognized):
            if(item_found):
                print(items.current_items)
                print(items.current_items_on_bench)
                keyboardFunctions.right_click(coordinates.top_right_screen)
                keyboardFunctions.left_click(items.current_items[0].coords)
                layout = ocrFunctions.get_item_bench_layout()
                print(layout)
                if(layout == 1):  #TODO: find layout variant
                    print("layout 1")
                    controlMode.item_bench_layout = coordinates.item_bench_layout1
                    controlMode.item_bench_name_layout = coordinates.item_name_bench_layout1
                    controlMode.layout_recognized = True
                if(layout == 2):
                    print("layout 2")
                    controlMode.layout_recognized = True
                if(layout == -1):
                    print("found both")
                    pass
                if(layout == 0):
                    print("found neither")
                    pass

                keyboardFunctions.left_click(items.current_items[0].coords)
    

def pvp_round():

    # look for loot bags
    pick_up_orbs()
    keyboardFunctions.go_to((597, 217))
   # check important stats, get info
    # hp = get_hp()
    # if(hp != -1):
    #     print(hp)
    #     pass
    # else:
    #     print("Error in retrieving hp")

    # lvl = get_lvl()
    # if(lvl != -1):
    #     print(lvl)
    #     pass
    # else:
    #     print("Error in retrieving lvl")
    missing_xp_to_lvl_up = 1
    lvl_progress = get_lvl_progress()
    if(lvl_progress[1] == -1 or lvl_progress[1] == -2):
        print("Error in retrieving lvl progress")
        lvl = get_lvl()
    else:
        print(lvl_progress)
        lvl = 0
        for i in range(len(generalData.level_progress)):
            if(lvl_progress[1] == generalData.level_progress[i]):
                lvl = i + 2
                break
        missing_xp_to_lvl_up = lvl_progress[1] - lvl_progress[0]
        # lvl lvl still 0
        if(not lvl):
            print("this one")
            lvl = get_lvl()



    #money_needed_to_lvl_up = calculate_money_to_lvl_up(lvl_progress)
    money_needed_to_lvl_up = 10 # for now to save time

    gold = get_gold()
    if(gold != -1):
        print(gold)
        pass
    else:
        print("Error in retrieving gold")
        pass

    ocrFunctions.set_champ_lvl()

    # spend money, buying champs, buying xp, sell champs
    shop = get_champ_names_shop_smart()
    lvl = spend_money(gold, money_needed_to_lvl_up, shop, lvl, missing_xp_to_lvl_up)

    # delete champs out of current champ list that are on board
    delete_elements_on_bench()

    # champ names, item names
    search_for_new_champs_on_bench()

    # show_what_the_programm_thinks_how_board_looks_like()
    # show_what_the_programm_thinks_how_board_looks_like2()
    
    # change board
    get_team_in_order(lvl)
    add_random_champ_on_board_if_needed(lvl, shop)
    # show_what_the_programm_thinks_how_board_looks_like()
    # show_what_the_programm_thinks_how_board_looks_like2()
    sell_champs_on_bench()

    # place items, change pos of items and champs
    # found_items = search_for_new_items_on_bench()
    # if(found_items):
    #     equip_items()



def augment_round():
    augment1 = get_text_augment(0)
    augment2 = get_text_augment(1)
    augment3 = get_text_augment(2)
    print(augment1)
    print(augment2)
    print(augment3)

    augment_to_choose = find_best_augment(augment1, augment2, augment3)
    print(augment_to_choose)
    if(augment_to_choose == 0):
        keyboardFunctions.left_click(coordinates.augment_name_left_click)
    if(augment_to_choose == 1):
        keyboardFunctions.left_click(coordinates.augment_name_middle_click)
    if(augment_to_choose == 2):
        keyboardFunctions.left_click(coordinates.augment_name_right_click)
