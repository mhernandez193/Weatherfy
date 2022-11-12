import urllib.request
import json
import environ

env = environ.Env()
environ.Env.read_env()


def fetchWeather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city.replace(" ", "")}&appid={env("OPEN_WEATHER_API_KEY")}&units=imperial'
    response = urllib.request.urlopen(url).read()
    return json.loads(response)
