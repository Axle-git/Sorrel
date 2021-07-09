"""
WARNING:    This script will ONLY WORK ON THE CURRENT FRONT DESK COMPUTER AT SORREL RIVER RANCH (7/8/2021).
            In the event that we recieve new computers (god willing), there are instructions on how to change the pixel counts in the XYcoordinates.py file. 

This script does the following steps in order:
    1)  opens RoomKeyPMS and logs in
    2)  Prints the following reports:
        a)
"""


from printReports import *

import os
import sys
import time
import pyautogui as ag

####    Make Report Folder      ####

####    open roomkey            ####
ag.press('win')
ag.write('Roomkey',interval = .1)
ag.press('enter')
time.sleep(5)   #wait for roomkey to startup

####    login                   ####
ag.write('alexjacobs', interval = .1)   #username
ag.press('tab')
ag.write('LaceFace11', interval = .1)   #password
ag.press('enter')
time.sleep(20)  #wait for roomkey

printInHouse()
