# -*- coding: UTF-8 -*-
import requests
import sys
import json

url = "http://127.0.0.1:8999/uploadImage"

for imageItem in sys.argv[1:]:

    payload={}
    files=[
      ('file',('head.jpg',open(imageItem,'rb'),'image/jpeg'))
    ]
    headers = {}
    # print(imageItem)
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print("Upload Success:")
    if json.loads(response.text)['code'] == 0:
        print(json.loads(response.text)['result'])


