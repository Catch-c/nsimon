# --[[ getTimetableShare.py ]]--
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
getTimetableShareBlueprint = Blueprint('getTimetableShareBlueprint', __name__)

# --[[ Route ]]--
@getTimetableShareBlueprint.route("/api/getTimetableShare", methods=["POST"])
def getTimetableShare():

    data = request.json
    shareCode = data["shareCode"]

    shareTimetable = Database.getTimetableShare(shareCode)

    sharedTimetable = {
        "username": shareTimetable["username"],
        "date": shareTimetable["date"],
        "timetable": shareTimetable["timetable"],
    }

    return jsonify(sharedTimetable), 200