import os, requests, sys
from datetime import datetime as dt


def check_website(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print("Connected.")
        else:
            print(f"Status code: {response.status_code}, Can not connect.")
    except requests.exceptions.RequestException as e:
        print("")