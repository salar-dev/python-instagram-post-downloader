import requests
import json
from tkinter import filedialog

url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post.php"

postUrl = input("Enter Post Url >>> ")
getFileName = input('Enter File Name >>> ')
fileDec = filedialog.askdirectory()


querystring = {"url": postUrl}

headers = {
    'x-rapidapi-host': "instagram-media-downloader.p.rapidapi.com",
    'x-rapidapi-key': "**********" # Put Your API Key 
    }

response = requests.request("GET", url, headers=headers, params=querystring)

textToJson = json.loads(response.text)
print(textToJson)

postFileUrl = ''

if 'video' in textToJson:
    postFileUrl = textToJson["video"]
else: postFileUrl = textToJson["image"]

reqPostFileUrl = requests.get(postFileUrl)

fileEx = reqPostFileUrl.headers['Content-Type'].split('/')[-1].split('.')[0]

fileName = fileDec + '/' + getFileName + '.' + fileEx

with reqPostFileUrl as rq:
    with open(fileName, 'wb') as file:
        file.write(rq.content)

print(textToJson)