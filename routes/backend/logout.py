# --[[ logout.py ]]--
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

# --[[ Blueprint Setup ]]--
logoutBlueprint = Blueprint('logoutBlueprint', __name__)

# --[[ Route ]]--
@logoutBlueprint.route('/logout')
def logout():
    """
    Logs the current user out
    """

    response = make_response(redirect('/'))
    response.set_cookie('adAuthCookie', '', expires=0)
    return response