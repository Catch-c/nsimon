from flask import Flask, render_template, request, redirect, url_for, session, flash
from Auth import getCookie
import Simon
from datetime import datetime, timezone
import json, pytz

app = Flask(__name__)
app.secret_key = 'TEMPKEY'


@app.route('/')
def index():
    if 'loggedIn' in session and session['loggedIn']:

        userCookie = session.get('simonCookie')
        now = datetime.now(timezone.utc)
        formattedDateTime = now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{int(now.microsecond / 1000):03d}Z"


        # Perform API Requests
        response, timetable = Simon.getTimetable(userCookie, formattedDateTime)
        timetable = json.loads(timetable)

        return render_template('base.html', timetable=timetable['d']['Periods'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            cookie = getCookie(username, password)
            if cookie:
                session['loggedIn'] = True
                session['simonCookie'] = cookie
                flash('Login successful!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Invalid username or password', 'error')
        except Exception as e:
            flash('Login failed. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)