from calendar import c
from re import X
from tkinter import Image

from cv2 import resize
import coordinates
import champions
import comps
import controlMode

from PIL import ImageGrab
import time
import pyautogui
import os
import cv2 as cv
import mss
import numpy
import pytesseract

if(controlMode.tobi_pc):
    pytesseract.pytesseract.tesseract_cmd = r'C://Program Files//Tesseract-OCR//tesseract.exe'
if(controlMode.benni_pc):
    pytesseract.pytesseract.tesseract_cmd = r'C://Users//Bennitim//AppData//Local//Tesseract-OCR//tesseract.exe'

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('pictures/screen2.png')
    if(controlMode.tobi_pc):     
        file_name = os.path.join(os.path.dirname(__file__), 'C:/Users/tobia/git-projects/tft-bot/pictures/screen2.png')
    if(controlMode.benni_pc):
        file_name = os.path.join(os.path.dirname(__file__), 'C:/Users/Bennitim/tft-bot/pictures/screen2.png')
    assert os.path.exists(file_name)    
    img = cv.imread(file_name)
    # cv.imshow("thresholding", img)
    # cv.waitKey(0)
    return img

time.sleep(1)
#take_screenshot()

def lack_for_a_better_name(coord, img):
    tuple1 = coord[0]
    tuple2 = coord[1]
    row1 = tuple1[1]
    row2 = tuple2[1]
    col1 = tuple1[0]
    col2 = tuple2[0]

    crop_image = img[row1:row2, col1:col2]
    text = pytesseract.image_to_string(crop_image)
    text_str = str(text)
    return text_str

# possibility 2 to get text with ocr
# taking screenshot wit mss for function get_text_advanced
sct = mss.mss()
def change_coords_format(coords):
    topLeft = coords[0]
    bottomRight = coords[1]
    newFormat = {'left': topLeft[0], 'top': topLeft[1], 'width': bottomRight[0] - topLeft[0], 'height': bottomRight[1] - topLeft[1]}
    #newFormat = {'left': topLeft[0], 'top': topLeft[1], 'width': bottomRight[0], 'height': bottomRight[1]}
    return newFormat

def image_resize(scale, image):
    (width, height) = (image.width * scale, image.height * scale)
    return image.resize((width, height))

def image_array(image):
    image = numpy.array(image)
    image = image[..., :3]
    return image

def image_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def image_thresholding(image):
    return cv.threshold(image, 255, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]

def image_thresholding_champ_name(image):
    return cv.threshold(image, 200, 255, cv.THRESH_BINARY_INV)[1]

def get_num_advanced(coords) -> str:
    coordsWidLen = change_coords_format(coords)
    screenshot = sct.grab(coordsWidLen)
    array = image_array(screenshot)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    return pytesseract.image_to_string(thresholding, config='--psm 10 -c tessedit_char_whitelist=0123456789').strip()

def get_text_advanced(coords) -> str:
    coordsWidLen = change_coords_format(coords)
    screenshot = sct.grab(coordsWidLen)
    array = image_array(screenshot)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    return pytesseract.image_to_string(thresholding, config='--psm 10 -c tessedit_char_whitelist=').strip()

# taking screenshot with ImageGrab
def change_coords_ImageGrab(coords):
    coord1 = coords[0]
    coord2 = coords[1]
    newCoords = (coord1[0], coord1[1], coord2[0], coord2[1])
    return newCoords

def get_treasure_dragon_options_ImageGrab(scale):
    names = []
    for i in range(0, 9, 2):
        coordsdiffFormat = change_coords_ImageGrab((coordinates.option_names_treasure_dragon[i], coordinates.option_names_treasure_dragon[i + 1]))
        screenshot = ImageGrab.grab(coordsdiffFormat)
        resize = image_resize(scale, screenshot)
        array = image_array(resize)
        grayscale = image_grayscale(array)
        thresholding = image_thresholding(grayscale)
        # cv.imshow("thresholding", thresholding)
        # cv.waitKey(0)
        name = pytesseract.image_to_string(thresholding, config='--psm 6 -c tessedit_char_whitelist=').strip()
        print(name)

        # filter unwanted characters such as space and line breaks
        print(name)
        if(" " in name):
            name = name.replace(' ', '')
            print("replaced space")

        if("\n" in name):
            name = name.replace('\n', '')
            print("replaced line break")

        if("'" in name):
            name = name.replace("'", "")
            print("replaced '")

        names.append(name)
    return names

def get_text_ImageGrab(coords, scale, psm_num, whitelist) -> str:
    coordsdiffFormat = change_coords_ImageGrab(coords)
    screenshot = ImageGrab.grab(coordsdiffFormat)
    # cv.imshow("s", screenshot)
    # cv.waitKey(0)
    resize = image_resize(scale, screenshot)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding(grayscale)
    # cv.imshow("thresholding", thresholding)
    # cv.waitKey(0)
    return pytesseract.image_to_string(thresholding, config='--psm ' + psm_num + ' -c tessedit_char_whitelist=' + whitelist).strip()

def get_text_ImageGrab_champ_names(coords, scale):
    coordsdiffFormat = change_coords_ImageGrab(coords)
    screenshot = ImageGrab.grab(coordsdiffFormat)
    resize = image_resize(scale, screenshot)
    array = image_array(resize)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding_champ_name(grayscale)
    # cv.imshow("thresholding", thresholding)
    # cv.waitKey(0)
    return pytesseract.image_to_string(thresholding, config='--psm 8 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.').strip()

def image_resize2(scale, img, width, height):
    (width, height) = (width * scale, height * scale)
    print(width)
    print(height)
    return img.resize((width, height))

def get_text_from_image(img, scale, width, height):
    array = image_array(img)
    grayscale = image_grayscale(array)
    thresholding = image_thresholding_champ_name(grayscale)
    # cv.imshow("thresholding", thresholding)
    # cv.waitKey(0)
    return pytesseract.image_to_string(thresholding, config='--psm 8 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.').strip()

# functions using templates
# source: https://stackoverflow.com/questions/7853628/how-do-i-find-an-image-contained-within-an-image
def find_lots_of_orbs(orb_type):
    screenshot = pyautogui.screenshot()
    screenshot.save('pictures/screen.png')

    screen = cv.imread('pictures/screen.png')
    if(orb_type == 'common'):
        template = cv.imread('pictures/commonOrb.png')
    if(orb_type == 'rare'):
        template = cv.imread('pictures/rareOrb.png')
    if(orb_type == 'legendary'):
        template = cv.imread('pictures/legendaryOrb.png')    

    res = cv.matchTemplate(screen, template, cv.TM_CCOEFF_NORMED)

    threshold = .7
    loc = numpy.where(res >= threshold)
    #print(loc)

    loc0 = loc[0]
    if(len(loc0) == 0):
        return (0, 0)
    else:
        loc00 = loc0[0]
        loc1 = loc[1]
        loc10 = loc1[0]
        location = (loc10, loc00)
        return location

def find_items_on_champs():
    # find more than one item from same type
    screenshot = pyautogui.screenshot()
    screenshot.save('pictures/screen.png')
    screenshot = cv.imread('pictures/screen.png')
    screen = screenshot[coordinates.crop_image_top_cut:1080, 0:1920]

    templates = ['pictures/negatron.png', 'pictures/bow.png', 'pictures/bf.png', 'pictures/chain.png', 'pictures/giants.png', 'pictures/rod.png', 'pictures/tear.png', 'pictures/gloves.png', 'pictures/spatula.png']
    item_names = ['NegatronCloak', 'RecurveBow', 'BFSword', 'ChainVest', 'GiantsBelt', 'NeedlesslyLargeRod', 'TearoftheGoddess', 'SparringGloves', 'Spatula']
    result = []
    for i in range(len(templates)):
        #print(i)
        template = cv.imread(templates[i])
        res = cv.matchTemplate(screen, template, cv.TM_CCOEFF_NORMED)

        threshold = .8
        loc = numpy.where(res >= threshold)
        #print(loc)

        loc0 = loc[0]
        if(len(loc0) == 0):
            location = (0, 0)
            continue
        else:
            loc00 = loc0[0]
            loc1 = loc[1]
            loc10 = loc1[0]
            location = (loc10, loc00)

            result.append(location)
            result.append(item_names[i])

    return result

def get_item_bench_layout():
    screenshot = pyautogui.screenshot()
    screenshot.save('pictures/screen.png')

    screen = cv.imread('pictures/screen.png')
    template1 = cv.imread('pictures/screen_item_bench1_cropped.png')
    template2 = cv.imread('pictures/screen_item_bench2_cropped.png')
    
    res1 = cv.matchTemplate(screen, template1, cv.TM_CCOEFF_NORMED)
    res2 = cv.matchTemplate(screen, template2, cv.TM_CCOEFF_NORMED)

    threshold = .95
    loc1 = numpy.where(res1 >= threshold)
    loc2 = numpy.where(res2 >= threshold)
    print(loc1)
    print(loc2)

    locUno0 = loc1[0]   
    locDos0 = loc2[0]
    if(len(locUno0) == 0 and len(locDos0) == 0):
        print("neither found")
        return 0
    if(not len(locUno0) == 0 and not len(locDos0) == 0):
        print("found both, change threshold")
        return -1
    if(not len(locUno0) == 0 and len(locDos0) == 0):
        print("found variant 1")
        return 1
    if(len(locUno0) == 0 and not len(locDos0) == 0):
        print("found variant 2")
        return 2

def set_champ_lvl():
    print("start func")
    screenshot = pyautogui.screenshot()
    screenshot.save('pictures/screen.png')

    screen = cv.imread('pictures/screen.png')
    template1 = cv.imread('pictures/sd.png')
    template2 = cv.imread('pictures/sd2.png')
    template3 = cv.imread('pictures/sd3.png')

    templates = [template1, template2, template3]

    for i in range(len(comps.lux_comp_star_coords)):
        window_coords = comps.lux_comp_star_coords[i]
        window_coords_min = window_coords[0]
        window_coords_max = window_coords[1]
        screen_window = screen[window_coords_min[1] : window_coords_max[1], window_coords_min[0] : window_coords_max[0]]
        # cv.imshow("screen_window", screen_window)
        # cv.waitKey(0)  
        for l in range(3):
            template = templates[l]
            res = cv.matchTemplate(screen_window, template, cv.TM_CCOEFF_NORMED)

            threshold = .83
            loc = numpy.where(res >= threshold)

            if(len(loc[0]) != 0):
                print(comps.lux_comp_champs_list[i])
                print(l + 1)

                # if intended star lvl is reached for this champ
                if(l + 1 >= comps.lux_comp_stars[comps.lux_comp_champs_list[i]]):
                    comps.lux_comp_champs_max_star_reached[comps.lux_comp_champs_list[i]] = True