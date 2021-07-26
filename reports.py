"""
WARNING:    This script will ONLY WORK ON THE CURRENT FRONT DESK COMPUTER AT SORREL RIVER RANCH (7/8/2021).
            In the event that we recieve new computers (god willing), there are instructions on how to change the pixel counts in the XYcoordinates.py file. 
            All files are saved in Ajacobs account

WARNING:    RK save to PDF screen must be full screen

This script does the following steps in order:
    1)  opens RoomKeyPMS and logs in
    2)  Prints the following reports:
        a)
"""


from saveReports import *
from printReports import *
import psutil

if __name__ == '__main__':

    if psutil.virtual_memory().percent >= 85:   #   assures the sleep times will work properly
        exit()

    ####    Make Report Folder      ####
    # os.mkdir(path)
    # time.sleep(1)

    #   RKLogin()

    #   saveReportsRK()

    #   printPackets()