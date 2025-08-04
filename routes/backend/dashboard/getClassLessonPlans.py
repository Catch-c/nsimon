# --[[ getClassLessonPlans.py ]]--
# --[[ Imports ]]--
from flask import (
    Flask,
    request, 
    jsonify, 
    redirect, 
    render_template, 
    url_for, 
    make_response, 
    flash,
    Blueprint
)
import Auth as Auth
import Simon as Simon

# --[[ Blueprint Setup ]]--
getClassLessonPlansBlueprint = Blueprint('getClassLessonPlansBlueprint', __name__)

# --[[ Route ]]--
@getClassLessonPlansBlueprint.route("/api/getClassLessonPlans", methods=["POST"])
def getClassLessonPlans():
    cookie = request.cookies.get("adAuthCookie")

    data = request.json
    classID = data["classID"]

    return jsonify(Simon.getClassLessonPlans(cookie, classID)), 200