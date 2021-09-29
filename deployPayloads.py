import requests, os

URL = "http://192.168.1.1/upload"
DIRS = ["Linux", "MacOS", "Windows"]

for dir in DIRS:
    files = os.listdir(dir)
    toUpload = {}
    for fileName in files:
        if fileName != "empty.txt":
            toUpload[fileName] = open(os.path.join(dir, fileName), "r").read()
    if len(toUpload) > 0:
        r = requests.post(URL, files=toUpload)
        r.status_code