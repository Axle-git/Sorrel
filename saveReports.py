from printReports import *

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

    return

