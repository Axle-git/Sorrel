import pyautogui as ag
import time

t_end = time.time() + 10
while time.time() < t_end:
    print(ag.position())