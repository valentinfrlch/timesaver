# load weather from openweathermap api
import requests


def open_weather_map():
    """
    Get weather from openweathermap.org
    """
    APIKEY = "4496197df33f1f9eaef47f0f0f1bec03"
    # call one call API
    x, y = 47.3992776, 8.7744840
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={x}&lon={y}&exclude=hourly,daily&appid={APIKEY}"
    response = requests.get(url)
    return response.json()

print(open_weather_map())