import Simon
import Auth

cookie = Auth.getCookie('sbcunningham26', 'cun001p315!!')

response, timetable = Simon.getStudentInformation(cookie)
print(response, timetable)