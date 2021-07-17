from quickstart import *

####    Download drive          ####
items = importDrive()

def downloadReservations():

    for item in items:
        print(item["name"])
        if item["name"] == "MASTER RESERVATION LIST":
            file_id = item["id"]
            request = drive_service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))
            break

downloadReservations()