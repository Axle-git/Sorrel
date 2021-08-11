from saveReports import *

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

    #   print report
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
    ag.hotkey('alt','f4')
    time.sleep(.1)

    return

def printArrivals():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.1)
    ag.click(occupencyX,occupencyY)
    time.sleep(.1)
    ag.click(arrivalsX,arrivalsY)
    time.sleep(.1)
    ag.click(arrivalsDateX,arrivalsDateY)
    time.sleep(5)

    #   print report
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
    ag.hotkey('alt','f4')
    time.sleep(.1)

    return

def printDepartures():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.1)
    ag.click(occupencyX,occupencyY)
    time.sleep(.1)
    ag.click(departuresX,departuresY)
    time.sleep(.1)
    ag.click(DbyRoomNumberX,DbyRoomNumberY)
    time.sleep(5)

    #   print report
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
    ag.hotkey('alt','f4')
    time.sleep(.1)

    return

def printHousekeeping():
    #   navigate menu
    ag.press('f9')
    time.sleep(5)
    ag.click(housekeepingPrintX,housekeepingPrintY)
    time.sleep(1)

    #   print report
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
    time.sleep(1)
    ag.hotkey('alt','f4')
    time.sleep(.1)
    ag.hotkey('alt','f4')
    time.sleep(.1)

    return
    
def printForecast():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.1)

    return