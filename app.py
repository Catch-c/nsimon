# --[[ app.py ]]--
# --[[ Imports ]]--
from flask import (
    Flask,
    request, 
    jsonify, 
    redirect, 
    render_template, 
    url_for, 
    make_response, 
    flash
)
from dotenv import load_dotenv
import os

# --[[ Load Environment Variables ]]--
load_dotenv()

# --[[ Flask Initialisation ]]--
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET', 'FlaskSecret')

# --[[ Register Blueprints ]]--
from routes.public.index import indexBlueprint
app.register_blueprint(indexBlueprint)

from routes.backend.login import loginBlueprint
app.register_blueprint(loginBlueprint)

from routes.backend.logout import logoutBlueprint
app.register_blueprint(logoutBlueprint)

from routes.public.dashboard import dashboardBlueprint
app.register_blueprint(dashboardBlueprint)

from routes.backend.dashboard.getTimetable import getTimetableBlueprint
app.register_blueprint(getTimetableBlueprint)

from routes.backend.dashboard.getDailyMessages import getDailyMessagesBlueprint
app.register_blueprint(getDailyMessagesBlueprint)

from routes.backend.dashboard.getClasses import getClassesBlueprint
app.register_blueprint(getClassesBlueprint)

from routes.backend.dashboard.getWeather import getWeatherBlueprint
app.register_blueprint(getWeatherBlueprint)

from routes.backend.dashboard.getUserInformation import getUserInformationBlueprint
app.register_blueprint(getUserInformationBlueprint)

from routes.backend.dashboard.createTimetableShare import createTimetableShareBlueprint
app.register_blueprint(createTimetableShareBlueprint)

from routes.backend.dashboard.getTimetableShare import getTimetableShareBlueprint
app.register_blueprint(getTimetableShareBlueprint)

from routes.public.share import shareBlueprint
app.register_blueprint(shareBlueprint)


# --[[ Get SIMON Link & Version API ]]--
@app.route('/api/simon', methods=['GET'])
def getSimon():
    """
    Returns the SIMON link.
    """
    link = os.getenv('SIMON_LINK', 'https://simon.sfx.vic.edu.au')
    version = os.getenv('APP_VERSION', '1.0.0')
    return jsonify({'link': link, 'version': version})

# --[[ Start ]]--
# --[[ PRODUCTION ]]--
# if __name__ == '__main__':
#     from waitress import serve
#     serve(app, host='0.0.0.0', port=8080)

# --[[ DEVELOPMENT ]]--
if __name__ == '__main__':
    app.run(debug=True, port=8080)

