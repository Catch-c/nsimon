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
import re, bcrypt
import Database as Database
import Simon as Simon

# --[[ Blueprint Setup ]]--
loginBlueprint = Blueprint('loginBlueprint', __name__)

def cleanUsername(username):
    if '@' in username:
        username = username.split('@')[0]
    username = username.lower()
    username = re.sub(r'[^a-z0-9]', '', username)
    return username

def hashPassword(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def checkPassword(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# --[[ Route ]]--
@loginBlueprint.route('/login', methods=['POST'])
def login():
    """
    Handles user login.
    """
    
    username = request.form.get('username')
    password = request.form.get('password')

    username = cleanUsername(username)

    user = Database.getUser(username)
    if not user:
        cookie = Auth.getCookie(username, password)
        if cookie:
            Database.createUser(username, hashPassword(password), cookie)
            response = make_response(redirect('/dashboard'))
            response.set_cookie('adAuthCookie', cookie, max_age=60*60*24*120)
            response.set_cookie('username', username, max_age=60*60*24*120)
            return response
        else:
            flash('Login failed. Please check your credentials.', 'danger')
            return redirect('/')
    else:
        if checkPassword(password, user["password"]):
            if Simon.checkCookie(user["cookie"]):
                response = make_response(redirect('/dashboard'))
                response.set_cookie('adAuthCookie', user["cookie"], max_age=60*60*24*120)
                response.set_cookie('username', username, max_age=60*60*24*120)
                return response
            else:
                Database.deleteUser(username)
                cookie = Auth.getCookie(username, password)
                if cookie:
                    Database.createUser(username, hashPassword(password), cookie)
                    response = make_response(redirect('/dashboard'))
                    response.set_cookie('adAuthCookie', cookie, max_age=60*60*24*120)
                    response.set_cookie('username', username, max_age=60*60*24*120)
                    return response
                else:
                    flash('Login failed. Please check your credentials.', 'danger')
                    return redirect('/')
        else:
            flash('Login failed. Please check your credentials.', 'danger')
            return redirect('/')
            
        
    
    
