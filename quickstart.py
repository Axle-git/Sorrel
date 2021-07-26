from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=1000, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    folderID = "14YblDFKymQeUFhDaciwy4BDPZmXDY9v5"

    query = f"parents = '{folderID}'"
    response = service.files().list(q=query).execute()
    files = response.get('files')
    for x in files:
        print(x)

    # if not items:
    #     print('No files found.')
    # else:
    #     open("driveFiles.txt","w").close()
    #     f = open("driveFiles.txt","w")
    #     for item in items:
    #         f.write(u'{0} ({1})'.format(item['name'], item['id']) + "\n")


if __name__ == '__main__':
    main()