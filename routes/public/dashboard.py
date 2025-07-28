# --[[ dashboard.py ]]--
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
dashboardBlueprint = Blueprint('dashboardBlueprint', __name__)

# --[[ Route ]]--
@dashboardBlueprint.route('/dashboard', methods=['GET'])
def dashboard():
    """
    Renders the dashboard page.
    """

    # Check if they are logged in
    cookie = request.cookies.get('adAuthCookie')
    if cookie:
        return render_template('/main/dashboard.html')
    else:
        return redirect('/')