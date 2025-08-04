# --[[ getLessonPlan.py ]]--
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
getLessonPlanBlueprint = Blueprint('getLessonPlanBlueprint', __name__)

# --[[ Route ]]--
@getLessonPlanBlueprint.route("/api/getLessonPlan", methods=["POST"])
def getLessonPlan():
    cookie = request.cookies.get("adAuthCookie")

    data = request.json
    classID = data["classID"]
    lessonID = data["lessonID"]

    return jsonify(Simon.getLessonPlan(cookie, classID, lessonID)), 200