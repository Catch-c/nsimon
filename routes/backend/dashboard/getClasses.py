# --[[ getClasses.py ]]--
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
getClassesBlueprint = Blueprint('getClassesBlueprint', __name__)

# --[[ Route ]]--
@getClassesBlueprint.route("/api/getClasses", methods=["POST"])
def getClasses():
    cookie = request.cookies.get("adAuthCookie")

    return jsonify(Simon.getClassResources(cookie)), 200