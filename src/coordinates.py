# coordinates in league client
# will be clicked and needs format (x,y) respectively (col, row)
play_button_tuple = (438, 226)
tft_button_tuple = (944, 471)
tft_button_tuple2 = (1070, 476)
ranked_button_tuple = (904, 728)
ranked_button_tuple2 = (1004, 720)
confirm_button_tuple = (855, 868)
find_match_button_tuple = (855, 868)
accept_match_button_tuple = (950, 742)
acceptButton = [(913, 727), (1013, 749)]

acceptButtonBenniPC= [(907, 702), (1013, 724)]
play_button_tuple_Benni_PC = (439, 203)
tft_button_tuple2_Benni_PC = (944, 445)
ranked_button_tuple2_Benni_PC = (888, 736)
confirm_button_tuple_Benni_PC = (854, 849)
find_match_button_tuple_Benni_PC = (854, 849)
# accept_match_button_tuple_Benni_PC = (955, 722) # not in use
acceptButtonBenniPC = [(907, 702), (1013, 724)]

exit_now_tuple = (827, 555)
exit_now = [(772, 537), (886, 565)]
you_finished = [(889, 378), (1039, 401)]
continue_after_victory_tuple = (960, 641)
continue_after_victory = [(913, 630), (1002, 649)]

# coordinates ingame
carousel_low_mid_pos = (960, 620)
# left to right
shop_champs = [(583, 991), (782, 992), (982, 994), (1177, 994), (1378, 994)]
bench_champs_old = [(421, 769), (559, 768), (658, 772), (773, 774), (896, 771), (1008, 785), (1131, 786), (1247, 785), (1356, 780)]
bench_champs = [(425, 784), (535, 782), (656, 786), (776, 786), (892, 786), (1011, 783), (1123, 786), (1249, 786), (1359, 787)]
# item_slot 36x36
# champions_on_bench_champs = []
# for i in range(9):
#     helper= bench_champs[i]
#     one = helper[0] + 15
#     items_on_bench_champs.append(one)
# print(items_on_bench_champs)

items_on_bench_champs = [0, 436, 574, 673, 788, 911, 1023, 1146, 1262, 1371, 1980]
crop_image_top_cut = 650

champs_on_board = [(555, 424), (671, 433), (793, 440), (908, 421), (1030, 420), (1142, 415), (1259, 419),
                    (607, 489), (725, 490), (849, 492), (964, 504), (1086, 490), (1205, 496), (1326, 488),
                (518, 556), (652, 562), (773, 555), (901, 555), (1023, 568), (1154, 568), (1269, 572),
                    (560, 650), (690, 651), (834, 656), (961, 670), (1090, 652), (1226, 647), (1355, 640)]
item_bench_layout1= [(298, 759), (334, 727), (303, 685), (353, 671), (394, 590), (385, 634), (404, 666), (440, 639)]
item_bench_layout2= [(298, 759), (334, 727), (303, 685), (353, 671), (324, 632), (349, 602), (394, 590), (385, 634), (404, 666), (440, 639)] # until 8th place, 7th index fine


# will be scanned and needs format (x,y,x+width,y+heigth)
# works
stage_one = [(817,7), (864, 32)] 
stage_two_plus = [(760, 10), (815, 30)]
augment_name_left = [(454, 580), (658, 611)]
augment_name_left_click = (550, 570)
augment_name_middle = [(853, 580), (1059, 610)]
augment_name_middle_click = (950, 580)
augment_name_right = [(1250, 579), (1475, 609)]
augment_name_right_click = (1300, 580)

# tome of traits
emblem_one = []
emblem_two = []
emblem_three = []
emblem_four = []
emblem_one_click = ()
emblem_two_click = ()
emblem_three_click = ()
emblem_four_click = ()

hp = [(1782, 212), (1824, 238)]
tome_of_traits_on_bench = [(435, 805)]
item_name_bench_layout1 = [(391, 200), (616, 234), (425, 176), (658, 205), (448, 117), (683, 154), (425, 81), (709, 108), (442, 42), (671, 73), (492, 41), (725, 72), (475, 80), (719, 128), (505, 119), (738, 149), (542, 90), (772, 121)] # without index 4, 5 of layout 2
item_name_bench_layout2 = [(391, 200), (616, 234), (425, 176), (658, 205), (402, 117), (636, 183), (448, 117), (683, 154), (425, 81), (709, 108), (442, 42), (671, 73), (492, 41), (725, 72), (475, 80), (719, 128), (505, 119), (738, 149), (542, 90), (772, 121)] # until 5/6th index fine but sparring gloves still p                      roblem   
#item_name_bench = [(391, 200), (616, 234), (425, 176), (658, 205), (405, 136), (647, 163), (448, 117), (683, 154), (425, 81), (709, 108), (442, 42), (671, 73), (492, 41), (725, 72), (499, 126), (724, 153)]
champ_name_bench_old = [(612, 691), (742, 714), (737, 689), (867, 715), (864, 692), (994, 715), (980, 691), (1110, 711), (1101, 692), (1231, 712), (1226, 693), (1356, 712), (1342, 691), (1473, 711), (1476, 692), (1599, 715), (1590, 689), (1720, 713)]
champ_name_bench = [(612, 691), (742, 714), (726, 690), (847, 715), (864, 692), (994, 715), (980, 691), (1110, 711), (1101, 694), (1231, 712), (1226, 693), (1356, 712), (1342, 694), (1473, 712), (1476, 692), (1599, 715), (1590, 689), (1720, 713)]
# champ_name_bench needed for nunu willump: (564, 691), (742, 714)

first_item_name_on_bench_champ = []
# for i in range(9):
#     first_item_name_on_bench_champ.append((670 + i * 118, 816))
#     first_item_name_on_bench_champ.append((910 + i * 118, 849))
# print(first_item_name_on_bench_champ)
first_item_name_on_bench_champ = [(670, 816), (910, 849), (788, 816), (1028, 849), (906, 816), (1146, 849), (1024, 816), (1264, 849), (1142, 816), (1382, 849), (1260, 816), (1500, 849), (1378, 816), (1618, 849), (1496, 816), (1736, 849), (1614, 816), (1854, 849)]
champ_names_shop = [(483, 1043), (598, 1065), (686, 1045), (802, 1066), (886, 1044), (1001, 1066),(1089, 1043), (1193, 1067), (1290, 1043), (1407, 1067)]

current_gold = [(870, 880), (920, 910)]
current_lvl= [(313, 882), (346, 910)]
# current_lvl2 = [(265, 878), (425, 908)]
# current_lvl3 = [(268, 877), (336, 903)]
lvl_status = [(402, 886), (444, 906)]

top_mid_screen = (900, 200)
top_right_screen = (1266, 192)

button_for_hp = (1891, 126)
# functions
def getAugmentCoords():
    return [augment_name_left, augment_name_middle, augment_name_right]


# star_lvl
#TODO: adapt coords
lux_star_coords = [(1322, 518), (1353, 600)] # with item, second calculated
skarner_star_coords = [(855, 359), (887, 422)] # with item finished
sylas_star_coords = [(1091, 302), (1119, 369)] # with item finished
varus_star_coords = [(1046, 530), (1080, 609)] # with item, first missing
nidalee_star_coords = [(525, 567), (557, 618)] # finished
vladimir_star_coords = [(1226, 452), (1256, 511)] # finished    

aurelion_star_coords = [(), ()] # with items
# 4 higher, 2 lower values, vlad and skarner