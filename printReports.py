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
    
    #   save report
    #   WARNING: save screen must be full screen
    ag.click(printerSetupX,printerSetupY)
    time.sleep(1)
    ag.click(printerNameX,printerNameY)
    time.sleep(.1)
    ag.write(printToPDF, interval = .1)
    ag.press('enter')
    time.sleep(.1)
    ag.press('enter')
    ag.click(printerX,printerY)
    time.sleep(2)
    ag.click(folderPathX,folderPathY)   #navigate to folder
    time.sleep(.1)
    ag.write('C:\\users\\ajacobs\\reports\\' + currDate, interval= .1)
    ag.press('enter')
    time.sleep(.1)
    ag.click(folderPathX,folderPathY)
    time.sleep(.1)
    for x in range(7):  #get to file name
        ag.press('tab')
        time.sleep(.1)
    ag.write("InHouse Report " + currDate, interval = .1)
    ag.press('enter')
    time.sleep(.1)

    #   print reports
    ag.click(printerSetupX,printerSetupY)
    time.sleep(1)
    ag.click(printerNameX,printerNameY)
    time.sleep(.1)
    ag.write(printerName, interval = .1)
    ag.press('enter')
    time.sleep(.1)
    for x in range(5):
        ag.press('tab')
        time.sleep(.1)
    ag.press('3')
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
