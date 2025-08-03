# --[[ share.py ]]--
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
shareBlueprint = Blueprint('shareBlueprint', __name__)

# --[[ Route ]]--
@shareBlueprint.route('/s/<shareCode>', methods=['GET'])
def share(shareCode):
    """
    Renders the share page.
    """

    cookie = request.cookies.get('adAuthCookie')
    if cookie:
        return redirect('/dashboard?shareCode=' + shareCode)
    else:
        return redirect('/?shareCode=' + shareCode)