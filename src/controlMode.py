import coordinates

def get_index_of_items_on_bench(coords) -> int:
    for i in range(len(item_bench_layout)):
        if(item_bench_name_layout[i] == coords):
            return i 
    return -1

layout_recognized = False
item_bench_layout = coordinates.item_bench_layout2 # default
item_bench_name_layout = coordinates.item_name_bench_layout2 # default

play_ranked_game = False

ashe_comp_active = True
kayle_comp_active = False
comp_to_play_for = "Ashe"

tobi_pc = True
benni_pc = False
# if((talon_comp_active and ashe_comp_active) or (not talon_comp_active and not ashe_comp_active)):
#     print("error: check comp_active Button")