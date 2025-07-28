# --[[ login.py ]]--
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

# --[[ Blueprint Setup ]]--
loginBlueprint = Blueprint('loginBlueprint', __name__)

# --[[ Route ]]--
@loginBlueprint.route('/login', methods=['POST'])
def login():
    """
    Handles user login.
    """
    
    username = request.form.get('username')
    password = request.form.get('password')

    cookie = Auth.getCookie(username, password)
    if cookie:
        response = make_response(redirect('/dashboard'))
        response.set_cookie('adAuthCookie', cookie, max_age=60*60*24*120)  # Cookie valid for 120 days
        return response
    else:
        flash('Login failed. Please check your credentials.', 'danger')
        return redirect('/')
