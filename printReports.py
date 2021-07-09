from XYcoordinates import *
import pyautogui as ag
import time
from datetime import date

today = date.today()
# mm_dd_yy
currDate = today.strftime("%m_%d_%y")
print(currDate)

def printInHouse():
    #   navigate menu
    ag.click(reportX,reportY)
    ag.click(occupencyX,occupencyY)
    ag.click(inHouseX,inHouseY)
    ag.click(IHbyRoomNumberX,IHbyRoomNumberY)
    
    #   save report
    ag.click(printerSetupX,printerSetupY)
    ag.click(printerNameX,printerNameY)
    ag.write(printToPDF)
    ag.press('enter')
    ag.press('enter')
    time.sleep(1)
    ag.write("InHouse Report " + currDate)
    ag.press('enter')

    return

def printArrivals():
    return

def printDepartures():
    return