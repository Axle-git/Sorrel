from XYcoordinates import *
import pyautogui as ag
import time
from datetime import date

import os
import sys

today = date.today()
# mm_dd_yy
currDate = today.strftime("%m_%d_%y")
parentDir = 'C:/Users/Ajacobs/Reports/'
path = os.path.join(parentDir, currDate)

def printInHouse():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.1)
    ag.click(occupencyX,occupencyY)
    time.sleep(.1)
    ag.click(inHouseX,inHouseY)
    time.sleep(.1)
    ag.click(IHbyRoomNumberX,IHbyRoomNumberY)
    time.sleep(5)

    #   print reports
    ag.click(printerSetupX,printerSetupY)
    time.sleep(1)
    ag.click(printerNameX,printerNameY)
    time.sleep(.1)
    ag.write(printerName, interval = .1)
    ag.press('enter')
    time.sleep(.1)
    ag.press('enter')
    time.sleep(1)
    ag.click(printerX,printerY)
    time.sleep(2)
    ag.click(printerCloseX,printerCloseY)

    return

def printArrivals():
    return

def printDepartures():
    return
