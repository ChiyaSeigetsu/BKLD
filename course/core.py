import requests
import os
from datetime import datetime

def getfile(url):
    response_head = requests.head(url)
    response = requests.get(url)

    if "Last-Modified" in response_head.headers:
        date_string = response_head.headers["Last-Modified"]
        date_object = datetime.strptime(date_string, "%a, %d %b %Y %H:%M:%S GMT")
        formatted_date = date_object.strftime("%d %b %Y")
        print("Last Modified:", formatted_date)
    else:
        print("Not found Last Modified in file")

    if response.status_code == 200:
        original_filename = "cautrucmonhoc.json"
        new_filename = "cautrucmonhoc_raw.json"
        with open(original_filename, "wb") as f:
            f.write(response.content)

        if os.path.exists(new_filename):
            os.remove(new_filename)
        os.rename(original_filename, new_filename)
        print(f"File downloaded")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

getfile("http://aao.hcmut.edu.vn/catalog/view/theme/default/ctdt_upload/cautrucmonhoc.json")