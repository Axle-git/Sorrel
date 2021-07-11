import pyautogui as ag
import time

t_end = time.time() + 10    #gives 10 seconds to leave cursor on desired location
while time.time() < t_end:
    print(ag.position())