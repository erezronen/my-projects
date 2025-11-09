import pygsheets
import os
import cv2
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google_drive_downloader import GoogleDriveDownloader as gdd
def seperate(whole):
    a=[]
    for i in range(len(whole)):
        a.append(whole[i])
    return(a)
def find(strin,find,replace):
    strin=seperate(strin)
    for i in range(len(strin)):
        if strin[i-1]==find:
            strin[i-1]=replace
    e=strin[0]
    for i in range(len(strin)-1):
        e=e+strin[i++1]
    return(e)
def download_file_from_google_drive(id, destination):
    gdd.download_file_from_google_drive(file_id=id,
                                        dest_path=destination,
                                        unzip=False)
def click_at_other_computer(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hac.sheet1.update_value(((1,1)),str(x)+"p"+str(y))
try:
    os.remove("/content/settings.yaml")
except:
    yyyyyy=1
download_file_from_google_drive("1POpfRM_IUZpiHJ5tX7fSLZJ8uXDwwzf8","C:/Users/User/Downloads/directory/settings.yaml")
try:
    os.remove("/content/credentials.json")
except:
    yyyyyy=1
if True:
    download_file_from_google_drive("1uTZGKA3gRF2MreiwIxUA6pfPZPTxjadQ","C:/Users/User/Downloads/directory/credentials.json")
try:
    os.remove("/content/client_secrets.json")
except:
    yyyyyy=1
download_file_from_google_drive("1VjnFZ36XMm3HEBzjuaeE8JJe0fT5yHRv","C:/Users/User/Downloads/directory/client_secrets.json")
try:
    os.remove("/content/sheets.googleapis.com-python.json")
except:
    yyyyyy=1
download_file_from_google_drive("1v5T1s2HmYzkwOJ3J_Lgu1hmP0Rz3FE4l","C:/Users/User/Downloads/directory/sheets.googleapis.com-python.json")
gauth = GoogleAuth()
drive = GoogleDrive(gauth)
gc=pygsheets.authorize()
hac=gc.open_by_url("https://docs.google.com/spreadsheets/d/1VZvauV21uSYUeZ03B3POycgu2XR2Ql4oMSOy9kFs_sI/edit#gid=0")
while True:
    fileList = drive.ListFile({'q': "'1v8pKPKqvKkv8UjJyTELbrnNaygHtETiT' in parents and trashed=false"}).GetList()
    for file in fileList:
        if (file['title'] == "image.png"):
            fileID = file['id']
    try:
        os.remove("image.png")
    except:
        yyyyyy=1
    try:
        download_file_from_google_drive(fileID, "C:/Users/User/Downloads/directory/image.png")
        image = cv2.imread("image.png")
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', click_at_other_computer)
        cv2.imshow('image', image)
        cv2.waitKey(1)
    except:
        yyyyyy=1

