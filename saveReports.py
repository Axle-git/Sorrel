from printReports import *

def navToPrinter():
    #   WARNING: save screen must be full screen
    ag.click(printerSetupX,printerSetupY)
    time.sleep(1)
    ag.click(printerNameX,printerNameY)
    time.sleep(.5)
    ag.write(printToPDF, interval = .1)
    ag.press('enter')
    time.sleep(.5)
    ag.press('enter')
    ag.click(printerX,printerY)
    time.sleep(2)

def navToFolder():
    ag.click(folderPathX,folderPathY)   #navigate to folder
    time.sleep(.5)
    ag.write('C:\\users\\ajacobs\\reports\\' + currDate, interval= .1)
    time.sleep(.5)
    return

def saveInHouse():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(occupencyX,occupencyY)
    time.sleep(.5)
    ag.click(inHouseX,inHouseY)
    time.sleep(.5)
    ag.click(IHbyRoomNumberX,IHbyRoomNumberY)
    time.sleep(10)

    #   save report
    navToPrinter()
    ag.write("InHouse Report " + currDate, interval = .1)
    navToFolder()
    ag.press('enter')
    time.sleep(2)
    ag.click(upperRightXX,upperRightXY)
    time.sleep(.5)

    return

def saveArrivals():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(occupencyX,occupencyY)
    time.sleep(.5)
    ag.click(arrivalsX,arrivalsY)
    time.sleep(.5)
    ag.click(arrivalsDateX,arrivalsDateY)
    time.sleep(.5)
    ag.click(dateOkX,dateOkY)
    time.sleep(10)

    #   save report
    navToPrinter()
    ag.write("Arrivals Report " + currDate, interval = .1)
    navToFolder()
    ag.press('enter')
    time.sleep(2)
    ag.click(upperRightXX,upperRightXY)
    time.sleep(.5)

    return
    
def saveDepartures():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(occupencyX,occupencyY)
    time.sleep(.5)
    ag.click(departuresX,departuresY)
    time.sleep(.5)
    ag.click(DbyRoomNumberX,DbyRoomNumberY)
    time.sleep(.5)
    ag.click(dateOkX,dateOkY)
    time.sleep(10)

    #   save report
    navToPrinter()
    ag.write("Departures Report " + currDate, interval = .1)
    navToFolder()
    ag.press('enter')
    time.sleep(2)
    ag.click(upperRightXX,upperRightXY)
    time.sleep(.5)

    return

def saveForecast():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(forecastX,forecastY)
    time.sleep(.5)
    ag.click(OccAndRevX,OccAndRevY)

    #   1 month ahead
    time.sleep(.5)
    ag.click(dateToDropX,dateToDropY)
    time.sleep(.5)
    ag.click(nextMonthArrowX,nextMonthArrowY)
    time.sleep(.5)
    ag.click(daysX,daysY)
    time.sleep(.5)
    ag.write(str(today.day), interval = .1)
    time.sleep(.5)
    ag.click(dateOkX,dateOkY)
    time.sleep(.5)
    ag.press('enter')
    time.sleep(10)

    #   save report
    navToPrinter()
    ag.write("Room Occupency and Revenue Forecast Report " + currDate, interval = .1)
    navToFolder()
    ag.press('enter')
    time.sleep(2)
    ag.click(upperRightXX,upperRightXY)
    time.sleep(.5)

    return

def saveGuestNotes():

    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(reservationsX,reservationsY)
    time.sleep(.5)
    ag.click(guestNotesX,guestNotesY)
    time.sleep(.5)
    ag.click(GNarrivalDateX,GNarrivalDateY)
    time.sleep(.5)
    ag.click(dateOkX,dateOkY)
    time.sleep(5)

    #   save report
    ag.click(ResPrintX,ResPrintY)
    time.sleep(.5)
    ag.click(ResPrintNameX,ResPrintNameY)
    time.sleep(.5)
    ag.write(printToPDF, interval = .1)
    ag.press('enter')
    time.sleep(.5)
    ag.press('enter')
    time.sleep(2)
    ag.write("Guest Notes " + currDate, interval = .1)
    navToFolder()
    ag.press('enter')
    time.sleep(2)
    ag.click(upperRightXX,upperRightXY)
    time.sleep(.5)

    return

def saveHousekeeping():
    #   navigate menu
    ag.press('f9')
    time.sleep(5)
    ag.click(housekeepingPrintX,housekeepingPrintY)
    time.sleep(5)

    #   save report
    navToPrinter()
    ag.write("Housekeeping Report " + currDate, interval = .1)
    navToFolder()
    ag.press('enter')
    time.sleep(2)
    ag.click(upperRightXX,upperRightXY)
    time.sleep(.5)
    ag.click(housekeepingCloseX,housekeepingCloseY)
    time.sleep(.5)

    return

def savePropertyStatus():
    
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(statisticsX,statisticsY)
    time.sleep(.5)
    ag.click(propertyStatusX,propertyStatusY)
    time.sleep(.5)
    ag.click(dateOkX,dateOkY)
    time.sleep(5)

    #   save report
    navToPrinter()
    ag.write("Property Status " + currDate, interval = .1)
    navToFolder()
    ag.press('enter')
    time.sleep(2)
    ag.click(upperRightXX,upperRightXY)
    time.sleep(.5)

    return