import pydirectinput
import time

def current_pos():
    return pydirectinput.position()
    time.sleep(1)
print(current_pos())