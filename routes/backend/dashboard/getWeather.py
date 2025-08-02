# --[[ getWeather.py ]]--
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
import requests

# --[[ Blueprint Setup ]]--
getWeatherBlueprint = Blueprint('getWeatherBlueprint', __name__)

# --[[ Route ]]--
@getWeatherBlueprint.route("/api/getWeather", methods=["POST"])
def getWeather():

    requestURL = f"https://api.open-meteo.com/v1/forecast?latitude=-38.05169&longitude=145.37329&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max&current=temperature_2m,apparent_temperature,weather_code&timezone=Australia%2FSydney&forecast_days=1"
    response = requests.get(requestURL)
    data = response.json()
    print(data)

    if response.status_code == 200:
        currentTemperature = data["current"]["temperature_2m"]
        todayMin = data["daily"]["temperature_2m_min"][0]
        todayMax = data["daily"]["temperature_2m_max"][0]
        todayUV = data["daily"]["uv_index_max"][0]
        todaySunrise = data["daily"]["sunrise"][0]
        todaySunset = data["daily"]["sunset"][0]
        currentFeelsLike = data["current"]["apparent_temperature"]
        weatherCode = data["current"]["weather_code"]

        def wmo_interpretation(condition, icon):
            return {"condition": condition, "icon": icon}

        wmo_map = {
            0: wmo_interpretation("Clear", "clear"),
            1: wmo_interpretation("Mostly Clear", "mostly-clear"),
            2: wmo_interpretation("Partly Cloudy", "partly-cloudy"),
            3: wmo_interpretation("Overcast", "overcast"),

            45: wmo_interpretation("Fog", "fog"),
            48: wmo_interpretation("Icy Fog", "rime-fog"),

            51: wmo_interpretation("Light Drizzle", "light-drizzle"),
            53: wmo_interpretation("Drizzle", "moderate-drizzle"),
            55: wmo_interpretation("Heavy Drizzle", "dense-drizzle"),

            80: wmo_interpretation("Light Showers", "light-rain"),
            81: wmo_interpretation("Showers", "moderate-rain"),
            82: wmo_interpretation("Heavy Showers", "heavy-rain"),

            61: wmo_interpretation("Light Rain", "light-rain"),
            63: wmo_interpretation("Rain", "moderate-rain"),
            65: wmo_interpretation("Heavy Rain", "heavy-rain"),

            56: wmo_interpretation("Light Freezing Drizzle", "light-freezing-drizzle"),
            57: wmo_interpretation("Freezing Drizzle", "dense-freezing-drizzle"),

            66: wmo_interpretation("Light Freezing Rain", "light-freezing-rain"),
            67: wmo_interpretation("Freezing Rain", "heavy-freezing-rain"),

            71: wmo_interpretation("Light Snow", "slight-snowfall"),
            73: wmo_interpretation("Snow", "moderate-snowfall"),
            75: wmo_interpretation("Heavy Snow", "heavy-snowfall"),

            77: wmo_interpretation("Snow Grains", "snowflake"),

            85: wmo_interpretation("Light Snow Showers", "slight-snowfall"),
            86: wmo_interpretation("Snow Showers", "heavy-snowfall"),

            95: wmo_interpretation("Thunderstorm", "thunderstorm"),
            96: wmo_interpretation("Light T-storm w/ Hail", "thunderstorm-with-hail"),
            99: wmo_interpretation("T-storm w/ Hail", "thunderstorm-with-hail")
        }

        interpretation = wmo_map.get(weatherCode)

        currentDescription = "Unknown"
        currentIcon = "clear"

        if interpretation:
            currentDescription = interpretation["condition"]
            currentIcon = interpretation["icon"]

        return (
            jsonify(
                {
                    "currentTemperature": currentTemperature,
                    "currentDescription": currentDescription,
                    "currentIcon": currentIcon,
                    "currentFeelsLike": currentFeelsLike,
                    "todayMin": todayMin,
                    "todayMax": todayMax,
                    "todayUV": todayUV,
                    "todaySunrise": todaySunrise,
                    "todaySunset": todaySunset,
                }
            ),
            200,
        )
    else:
        jsonify(
            {
                "currentTemperature": "??",
                "currentDescription": "??",
                "currentIcon": "https://openweathermap.org/img/wn/01d.png",
            }
        ), 200