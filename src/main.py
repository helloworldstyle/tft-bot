import coordinates
import keyboardFunctions
import functions

import time
keyboardFunctions.switch_windows()

#time.sleep(3)

# infinite loop
while(True):
    # start searching for match
    keyboardFunctions.find_match()
    # game strategy 
    functions.game_strategy()

    # search for new matchs
    keyboardFunctions.find_new_match()