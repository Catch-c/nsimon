# Imports
import requests, os
from dotenv import load_dotenv

# Load env
load_dotenv()

def getStudentInformation(cookie):
    """
    Fetches the student information
    
    Args:
        None
        
    Returns:
        str: HTTPs status code
        str: Response text
    """
    
    # HEADERS
    url="https://simon.sfx.vic.edu.au/WebServices/Default.asmx/UserInformation"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # Make the request
    response = requests.post(url, headers=headers)

    # Return the status code and response text
    return response.status_code, response.text

def getStudentID(cookie, communityID):
    """
    Fetches the student ID
    
    Args:
        communityID (str): The community ID of the student
        
    Returns:
        str: HTTPs status code
        str: Response text
    """
    
    # HEADERS
    url="https://simon.sfx.vic.edu.au/WebServices/Profiles/Students.asmx/GetStudentIDByCommunityID"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "communityID": communityID,
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getStudentProfile(cookie, studentID):
    """
    Fetches the student profile profile
    
    Args:
        studentID (str): The student ID
        
    Returns:
        str: HTTPs status code
        str: Response text
    """
    
    # HEADERS
    url="https://simon.sfx.vic.edu.au/WebModules/Profiles/Student/StudentProfiles.asmx/StudentProfileDetails"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "studentID": studentID,
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getTimetable(cookie, date):
    """
    Fetches the timetable data for a specific date
    
    Args:
        date (str): The date in ISO format
    Returns:
        str: HTTPs status code
        str: Response text
    """
    
    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebServices/Default.asmx/GetTimetable"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "selectedDate": date,
        "selectedGroup": None
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getDailyMessage(cookie, date):
    """
    Fetches the daily messages
    
    Args:
        date (str): The date in ISO format
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebServices/SchoolMessagesAPI.asmx/GetWorkDeskDailyMessages"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "messageDate": date
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getFullTimetable(cookie, studentID, timetableGroup):
    """
    Fetches the students full timetable (day 1 -> day 10)
    
    Args:
        studentID (str): The student ID
        timetableGroup (str): The timetable group of the student (BEA, OFF, BER, SFX)
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebServices/Profiles/Students.asmx/GetTimetableForStudent"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "studentID": studentID,
        "timetableGroup": timetableGroup
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getClassResources(cookie, fileSequence=None, studentID=None):
    """
    Fetches the students class resources
    
    Args:
        fileSequence? (str): The semesters file sequence
        studentID? (str): The student ID
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebServices/Profiles/Students.asmx/GetTimetableForStudent"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "fileSequence": fileSequence if fileSequence is not None else '48',
        "studentID": studentID if studentID is not None else None,
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getUpcoming(cookie):
    """
    Fetches the students upcoming events
    
    Args:
        None
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebServices/Default.asmx/Upcoming"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # Make the request
    response = requests.post(url, headers=headers)

    # Return the status code and response text
    return response.status_code, response.text

def getLessonPlans(cookie, classID):
    """
    Fetches the classes lesson planms
    
    Args:
        classsID (str): The class ID
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebModules/LearningAreas/LearningAreas.asmx/GetAllStudentClassLessonPlans"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "classID": classID,
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getLessonPlan(cookie, classID, lessonPlanID):
    """
    Fetches the classes lesson planms
    
    Args:
        classsID (str): The class ID
        lessonPlanID (str): The lesson plan ID
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebModules/LearningAreas/LearningAreas.asmx/GetAllStudentClassLessonPlans"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "classLessonId": lessonPlanID,
        "classID": classID,
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getDashboardData(cookie, studentID, fileSequence=None):
    """
    Fetches the dashboard data for a student
    
    Args:
        studentID (str): The student ID
        fileSequence (str): The semesters file sequence
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebModules/Profiles/Student/GeneralInformation/StudentDashboard.aspx/GetDashboardDataByStudentID"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "studentId": studentID,
        "academicSemesterId": fileSequence if fileSequence is not None else '48',
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getReports(cookie, studentID):
    """
    Fetches the reports for a student
    
    Args:
        studentID (str): The student ID
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebServices/StudentAssessment/StudentAssessmentWS.asmx/GetReportArchives"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "studentId": studentID,
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text

def getLetters(cookie, studentID):
    """
    Fetches the letters for a student
    
    Args:
        studentID (str): The student ID
        
    Returns:
        str: HTTPs status code
        str: Response text
    """

    # URL and HEADERS
    url = "https://simon.sfx.vic.edu.au/WebModules/Profiles/Student/Letters/Letters.aspx/getProfileLettersByStudentID"
    headers = {
        "cookie": (
            f"adAuthCookie={cookie}"
        ),  
    }

    # BODY of REQUEST
    data = {
        "studentId": studentID,
    }

    # Make the request
    response = requests.post(url, headers=headers, json=data)

    # Return the status code and response text
    return response.status_code, response.text