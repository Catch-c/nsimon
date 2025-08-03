import requests, time, re
import os
from dotenv import load_dotenv

# --[[ Load Environment Variables ]]--
load_dotenv()
SIMON_LINK = os.getenv('SIMON_LINK', 'https://simon.sfx.vic.edu.au')

def checkCookie(cookie):
    url = f"{SIMON_LINK}/WebServices/Default.asmx/UserInformation"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    response = requests.post(url, headers=headers)

    if response.status_code == 401:
        return False 
    else:
        return True


def getTimetable(cookie, time):
    url = f"{SIMON_LINK}/WebServices/Default.asmx/GetTimetable"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    data = {"selectedDate": time, "selectedGroup": "BEA"}

    response = requests.post(url, headers=headers, json=data)

    return response.json()

def getDailyMessages(cookie, time):
    url = f"{SIMON_LINK}/WebServices/SchoolMessagesAPI.asmx/GetWorkDeskDailyMessages"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    data = {"messageDate": time}

    response = requests.post(url, headers=headers, json=data)

    return response.json()

def getClassResources(cookie):
    url = f"{SIMON_LINK}/WebServices/Default.asmx/GetClassResources"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    data = {"FileSeq": 48, "UserID": None}
    response = requests.post(url, headers=headers, json=data)

    return response.json()


def getUserInformation(cookie):
    url = f"{SIMON_LINK}/WebServices/Default.asmx/UserInformation"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    response = requests.post(url, headers=headers)

    return response.json()
