import requests, time, re

def checkCookie(cookie):
    url = "https://simon.sfx.vic.edu.au/WebServices/Default.asmx/UserInformation"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    response = requests.post(url, headers=headers)

    if response.status_code == 401:
        return False 
    else:
        return True


def getTimetable(cookie, time):
    url = "https://simon.sfx.vic.edu.au/WebServices/Default.asmx/GetTimetable"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    data = {"selectedDate": time, "selectedGroup": "BEA"}

    response = requests.post(url, headers=headers, json=data)

    return response.json()

def getDailyMessages(cookie, time):
    url = "https://simon.sfx.vic.edu.au/WebServices/SchoolMessagesAPI.asmx/GetWorkDeskDailyMessages"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    data = {"messageDate": time}

    response = requests.post(url, headers=headers, json=data)

    return response.json()

def getClassResources(cookie):
    url = "https://simon.sfx.vic.edu.au/WebServices/Default.asmx/GetClassResources"
    headers = {"Content-Type": "application/json", "Cookie": f"adAuthCookie={cookie}"}

    data = {"FileSeq": 48, "UserID": None}
    response = requests.post(url, headers=headers, json=data)

    return response.json()
