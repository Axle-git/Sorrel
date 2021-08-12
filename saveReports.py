from XYcoordinates import *
import pyautogui as ag
import time
from datetime import date
from quickstart import *

import os
import sys

today = date.today()
# mm_dd_yy
currDate = today.strftime("%m_%d_%y")

parentDir = 'C:/Users/%s/Reports/' % sys.argv[1]
path = os.path.join(parentDir, currDate)

def RKLogin():
    ####    open roomkey            ####
    ag.press('win')
    time.sleep(.5)
    ag.write('Roomkey',interval = .1)
    ag.press('enter')
    time.sleep(8)   #wait for roomkey to startup

    ####    login                   ####
    ag.write('*******', interval = .1)   #username
    ag.press('tab')
    ag.write('*******', interval = .1)   #password
    ag.press('enter')
    time.sleep(30)  #wait for roomkey

    return

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
    ag.write("C:\\users\\%s\\reports\\" % sys.argv[1] + currDate, interval= .1)
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

#   DO NOT USE ON LAST DAY OF MONTH
def saveArrivalsTomorrow():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(occupencyX,occupencyY)
    time.sleep(.5)
    ag.click(arrivalsX,arrivalsY)
    time.sleep(.5)
    ag.click(arrivalsDateX,arrivalsDateY)
    time.sleep(.5)
    ag.click(daysX,daysY)
    ag.write(str(today.day + 1), interval = .1) # tomorrow
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

#   DO NOT USE ON LAST DAY OF MONTH
def saveDeparturesTomorrow():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(occupencyX,occupencyY)
    time.sleep(.5)
    ag.click(departuresX,departuresY)
    time.sleep(.5)
    ag.click(DbyRoomNumberX,DbyRoomNumberY)
    time.sleep(.5)
    ag.click(daysX,daysY)
    ag.write(str(today.day + 1), interval = .1) # tomorrow
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

#   DO NOT USE ON LAST DAY OF MONTH
def saveForecastTomorrow():
    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(forecastX,forecastY)
    time.sleep(.5)
    ag.click(OccAndRevX,OccAndRevY)
    time.sleep(.5)
    ag.click(daysX,daysY)
    ag.write(str(today.day + 1), interval = .1) # tomorrow
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

#   DO NOT USE ON LAST DAY OF MONTH
def saveGuestNotesTomorrow():

    #   navigate menu
    ag.click(reportX,reportY)
    time.sleep(.5)
    ag.click(reservationsX,reservationsY)
    time.sleep(.5)
    ag.click(guestNotesX,guestNotesY)
    time.sleep(.5)
    ag.click(GNarrivalDateX,GNarrivalDateY)
    time.sleep(.5)
    ag.click(daysX,daysY)
    ag.write(str(today.day + 1), interval = .1) # tomorrow
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

def saveReportsRK():

    saveArrivals()
    saveDepartures()
    saveForecast()
    saveGuestNotes()
    saveHousekeeping()
    saveInHouse()
    savePropertyStatus()

    return

#   easiest, most intuitive way to print with python I could come up with
#   MUST BE DONE AFTER SAVE REPORTS
def printPackets():

    filePath = "C:\\users\\%s\\reports\\" % sys.argv[1] + currDate + "\\"
    
    #   IN ORDER
    reportNames = [ "Arrivals Report %s.pdf" % currDate,
                    "Departures Report %s.pdf" % currDate,
                    "InHouse Report %s.pdf" % currDate,
                    "Room Occupency and Revenue Forecast Report %s.pdf" % currDate,
                    "Guest Notes %s.pdf" % currDate,
                    "Property Status %s.pdf" % currDate,
                    "Housekeeping Report %s.pdf" % currDate]
                    # "Mindbody Schedule at a Glance %s.pdf" % currDate,
                    # "Master Reservations Sheet %s.pdf" % currDate,
                    # "Daily Scoop %s.pdf" % currDate]

    #   arrivals
    for currFile in reportNames:
        os.startfile(filePath + currFile)
        time.sleep(5)
        ag.hotkey("ctrl","p")
        time.sleep(5)
        for i in range(10): #   nav to "print" button
            ag.press("tab")
            time.sleep(.3)
        ag.press("enter")
        time.sleep(1)
        ag.hotkey("alt","f4")
        time.sleep(1)

    return

def saveEveningReports():

    RKLogin()

    saveInHouse()
    saveArrivalsTomorrow()
    saveGuestNotesTomorrow()
    saveDeparturesTomorrow()
    saveForecastTomorrow()
    saveHousekeeping()

    #   CREATE FOLDER FOR CURRENT DAY
    SCOPES = ['https://www.googleapis.com/auth/drive']
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('drive', 'v3', credentials=creds)

    currDay = date.today().day

    body = {
        'name': str(currDay),
        'mimeType': "application/vnd.google-apps.folder"
    }
    body['parents'] = ["1VwC-6je67uh5Fgu7KZD__UjANwMNR1QU"]
    root_folder = service.files().create(body = body).execute()
    #########

    reportNames = [ "Arrivals Report %s.pdf" % currDate,
                    "Departures Report %s.pdf" % currDate,
                    "InHouse Report %s.pdf" % currDate,
                    "Room Occupency and Revenue Forecast Report %s.pdf" % currDate,
                    "Guest Notes %s.pdf" % currDate,
                    "Housekeeping Report %s.pdf" % currDate]
    filePath = 'C:\\users\\%s\\reports\\' % sys.argv[1] + currDate + '\\'

    for report in reportNames:
        file_metadata = {
            'name': report,
            'mimeType': "application/pdf"
        }
        file_metadata['parents'] = [root_folder['id']]

        media = MediaFileUpload(filePath + report, mimetype='application/pdf')

        file = service.files().create(body=file_metadata, media_body=media).execute()
        print('File ID: %s' % file.get('id'))

    return
