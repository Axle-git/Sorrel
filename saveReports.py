from printReports import *

def navToSaveName():
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
    return

def saveInHouse():
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
    navToSaveName()
    ag.write("InHouse Report " + currDate, interval = .1)
    ag.press('enter')
    time.sleep(.1)
    ag.hotkey('alt','f4')   #   close print window
    time.sleep(.1)

    return

def saveArrivals():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.1)
    ag.click(occupencyX,occupencyY)
    time.sleep(.1)
    ag.click(arrivalsX,arrivalsY)
    time.sleep(.1)
    ag.click(arrivalsDateX,arrivalsDateY)
    time.sleep(5)

    #   save report
    navToSaveName()
    ag.write("Arrivals Report " + currDate, interval = .1)
    ag.press('enter')
    time.sleep(.1)
    ag.hotkey('alt','f4')   #   close print window
    time.sleep(.1)

    return
    
def saveDepartures():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.1)
    ag.click(occupencyX,occupencyY)
    time.sleep(.1)
    ag.click(departuresX,departuresY)
    time.sleep(.1)
    ag.click(DbyRoomNumberX,DbyRoomNumberY)
    time.sleep(5)

    #   save report
    navToSaveName()
    ag.write("Departures Report " + currDate, interval = .1)
    ag.press('enter')
    time.sleep(.1)
    ag.hotkey('alt','f4')   #   close print window
    time.sleep(.1)

    return

def saveHousekeeping():
    #   navigate menu
    ag.press('f9')
    time.sleep(5)
    ag.click(housekeepingPrintX,housekeepingPrintY)
    time.sleep(1)

    #   save report
    navToSaveName()
    ag.write("Housekeeping Report " + currDate, interval = .1)
    ag.press('enter')
    time.sleep(.1)
    ag.hotkey('alt','f4')   #   close print window
    time.sleep(.1)
    ag.hotkey('alt','f4')
    time.sleep(.1)

    return

def saveForecast():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.1)
    ag.click(forecastX,forecastY)
    time.sleep(.1)
    ag.click(OccAndRevX,OccAndRevY)

    #   1 month ahead
    time.sleep(.1)
    ag.click(dateToDropX,dateToDropY)
    time.sleep(.1)
    ag.click(nextMonthArrowX,nextMonthArrowY)
    time.sleep(.1)
    ag.click(daysX,daysY)
    time.sleep(.1)
    ag.write(str(today.day), interval = .1)
    time.sleep(.1)
    ag.click(dateOkX,dateOkY)
    time.sleep(.1)
    ag.press('enter')
    time.sleep(5)

    #   save report
    navToSaveName()
    ag.write("Room Occupency and Revenue Forecast Report " + currDate, interval = .1)
    ag.press('enter')
    time.sleep(2)
    ag.hotkey('alt','f4')   #   close print window
    time.sleep(.1)

    return