"""
WARNING:    This script will ONLY WORK ON THE CURRENT FRONT DESK COMPUTER AT SORREL RIVER RANCH (7/8/2021).
            In the event that we recieve new computers (god willing), there are instructions on how to change the pixel counts in the XYcoordinates.py file. 
            All files are saved in Ajacobs account

WARNING:    RK save to PDF screen must be full screen
"""


from saveReports import *
from printReports import *
import psutil

def main():
    if psutil.virtual_memory().percent >= 85:   #   assures the sleep times will work properly
        exit()

    ####    Make Report Folder      ####
    if not os.path.exists('C:/Users/%s/Reports/' % sys.argv[1]):
        os.mkdir('C:/Users/%s/Reports/' % sys.argv[1])
        time.sleep(1)

    if not os.path.exists(path):
        os.mkdir(path)
        time.sleep(1)

    RKLogin()

    saveReportsRK()

    for i in range(3):
        printPackets()

if __name__ == '__main__':
    main()
