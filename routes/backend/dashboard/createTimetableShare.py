# --[[ createTimetableShare.py ]]--
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
import Database as Database

# --[[ Blueprint Setup ]]--
createTimetableShareBlueprint = Blueprint('createTimetableShareBlueprint', __name__)

# --[[ Route ]]--
@createTimetableShareBlueprint.route("/api/createTimetableShare", methods=["POST"])
def createTimetableShare():
    username = request.cookies.get("username")

    data = request.json
    date = data["date"]
    timetable = data["timetable"]

    return jsonify(Database.createTimetableShare(username, date, timetable)), 200