# # import activities from activities.json
import data_sources as ds
import time
import json

activities = json.load(open('activities.json'))

def decide():
    outdoor = False
    day = False
    """
    Decide what to do with the activities
    """
    # get the weather
    weather = ds.open_weather_map()

    if weather["temp"] > 20 and weather["conditions"] != "Rain":
        outdoor = True
    
    # get the current time
    time = time.localtime()
    
    # get if it's between 8 and 18
    if time.tm_hour >= 8 and time.tm_hour <= 18:
        day = True
    
    # decide what to do based on the weather and the time
    if outdoor and day:
        return activities["outdoor"]
    elif not outdoor and day:
        return activities["indoor"]
    