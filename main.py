import os
import io 
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

#authentication
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com.auth.drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


file_ids = ['', '', '']

for file_id in file_ids:
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False 
    while not done:
        status, done = downloader.next_chunk() #returns a tuple
        print(f"Download Progress {status.progress()*100}")

    fh.seek(0)

    #save to your destination
    """
    with open(os.path.join('./'DriveDownloads'), file_name+'idx') as f:
        f.write(fh.read())
        f.close()
    """
