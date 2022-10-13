from turtle import right
import pyautogui
import pydirectinput
import time
import ocrFunctions
import coordinates
#import ocrFunctions

def copy():
    pydirectinput.keyDown("ctrl")
    pydirectinput.press("c")
    pydirectinput.keyUp("ctrl")

def paste():
    pydirectinput.keyDown("ctrl")
    pydirectinput.press("v")
    pydirectinput.keyUp("ctrl")

def switch_windows():
    pydirectinput.keyDown("alt")
    pydirectinput.press("tab")
    pydirectinput.keyUp("alt")

# basic functions using the keyboard

def reroll():
    pydirectinput.press("d")

def level_up():
    pydirectinput.press("f")

def scout_downwards():
    pydirectinput.press("8")

def escape():
    pydirectinput.press("esc")

def left_click(coord_tuple):
    pydirectinput.moveTo(coord_tuple[0], coord_tuple[1])
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

def left_click_halt(coord_tuple):
    pydirectinput.moveTo(coord_tuple[0], coord_tuple[1])
    pydirectinput.mouseDown()

def right_click(coord_tuple):
    pydirectinput.moveTo(coord_tuple[0], coord_tuple[1])
    pydirectinput.mouseDown(button= 'right')
    pydirectinput.mouseUp(button= 'right')

def sell_champ(coord_tuple):
    pydirectinput.moveTo(coord_tuple[0], coord_tuple[1])
    pydirectinput.press("e")

def move_mouse_to(coord_tuple):
    pydirectinput.moveTo(coord_tuple[0], coord_tuple[1])


def go_to(coord_tuple):
    pydirectinput.moveTo(coord_tuple[0], coord_tuple[1])   
    pydirectinput.mouseDown(button= 'right')
    pydirectinput.mouseUp(button= 'right')

def current_position():
    return pydirectinput.position()

def halt_movement():
    pydirectinput.press("s")
# more advanced functions using the keyboard

def buy_champ(order):
    left_click(coordinates.shop_champs[order])

def accept_match():
    left_click(coordinates.accept_match_button_tuple)

def move_things(from_where_coord, to_there_coord):
    left_click_halt(from_where_coord)
    move_mouse_to(to_there_coord)
    pydirectinput.mouseUp()


# TODO: create find_match version for special event with tft_button_tuple and do settings to switch between mode
def find_match():
    # queue up with keyboard functions
    left_click(coordinates.play_button_tuple)
    time.sleep(1)
    left_click(coordinates.tft_button_tuple)
    #left_click(coordinates.ranked_button_tuple2) # currently just normals
    left_click(coordinates.confirm_button_tuple)
    time.sleep(4)
    left_click(coordinates.find_match_button_tuple)

    # check if game was found and game started
    inGame = False
    while(not inGame):
        img = ocrFunctions.take_screenshot()
        text_inGame_str = ocrFunctions.lack_for_a_better_name(coordinates.stage_one, img)
        text_inGame = text_inGame_str.split("-")[0]
        text_foundAgain_str = ocrFunctions.lack_for_a_better_name(coordinates.acceptButton, img)
        text_foundAgain = text_foundAgain_str.split("!")[0]

        if(text_foundAgain == "ACCEPT"):
            accept_match()
        if(text_inGame == "1"):
            inGame = True
        time.sleep(2)

def find_new_match():
    # queue up with keyboard functions
    time.sleep(4)
    left_click(coordinates.play_button_tuple)
    time.sleep(3)
    left_click(coordinates.find_match_button_tuple)

    # check if game was found and game started   
    inGame = False
    while(not inGame):
        img = ocrFunctions.take_screenshot()
        text_inGame_str = ocrFunctions.lack_for_a_better_name(coordinates.stage_one, img)
        text_inGame = text_inGame_str.split("-")[0]
        text_foundAgain_str = ocrFunctions.lack_for_a_better_name(coordinates.acceptButton, img)
        text_foundAgain = text_foundAgain_str.split("!")[0]

        if(text_foundAgain == "ACCEPT"):
            accept_match()
        if(text_inGame == "1"):
            inGame = True
        time.sleep(2)