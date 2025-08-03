# --[[ getUserInformation.py ]]--
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
getUserInformationBlueprint = Blueprint('getUserInformationBlueprint', __name__)

# --[[ Route ]]--
@getUserInformationBlueprint.route("/api/getUserInformation", methods=["POST"])
def getUserInformation():
    cookie = request.cookies.get("adAuthCookie")

    return jsonify(Simon.getUserInformation(cookie)), 200