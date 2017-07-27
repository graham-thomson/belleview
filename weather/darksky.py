import json
import time
import requests

def to_date(unixtime):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(unixtime)))

def get_apikey(config="../creds/darksky.json"):
    return json.load(open(config, "rb"))["apikey"]

def get_forecast(lat, long, apikey):
    request =  requests.get("https://api.darksky.net/forecast/{key}/{lat},{long}"
                            .format(key=apikey, lat=lat, long=long))
    try:
        return request.status_code, request.json()
    except ValueError:
        return request.status_code, request.text

def current_boston():
    forecast = get_forecast(lat=42.358153, long=-71.0647258, apikey=get_apikey())
    if forecast[0] == 200:
        current_temp = forecast[1]["currently"]["temperature"]
        current_condition = forecast[1]["currently"]["summary"]
        return "Current Boston Weather", "{summary} and {temp} degrees.".format(summary=current_condition, temp=current_temp)