# --[[ index.py ]]--
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
indexBlueprint = Blueprint('indexBlueprint', __name__)

# --[[ Route ]]--
@indexBlueprint.route('/', methods=['GET'])
def index():
    """
    Renders the index page.
    """

    # Check if they are logged in
    cookie = request.cookies.get('adAuthCookie')
    if cookie:
        return redirect('/dashboard')
    else:
        return render_template('index.html')