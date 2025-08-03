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



# --[[ Get Version API ]]--
@app.route('/api/version', methods=['GET'])
def getVersion():
    """
    Returns the version of the application.
    """
    version = os.getenv('APP_VERSION', '1.0.0')
    return jsonify({'version': version})

# --[[ Start ]]--
# --[[ PRODUCTION ]]--
# if __name__ == '__main__':
#     from waitress import serve
#     serve(app, host='0.0.0.0', port=8080)

# --[[ DEVELOPMENT ]]--
if __name__ == '__main__':
    app.run(debug=True, port=8080)

