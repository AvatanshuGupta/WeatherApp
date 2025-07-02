from django.shortcuts import render
from dotenv import load_dotenv
import os
import datetime
import requests


load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")




def home(request):
    weather_data={}
    try:
        if request.method=="POST":
            city=request.POST.get("city")
            url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
            data=requests.get(url).json()
            if data.get("cod") != 200:
                raise ValueError(data.get("message", "City not found."))
            date=datetime.date.today()
            coord = data.get('coord', {})
            main = data.get('main', {})
            wind = data.get('wind', {})
            rain = data.get('rain', {})
            clouds = data.get('clouds', {})
            weather = data.get('weather', [{}])[0]
            lon = coord.get('lon')
            lat = coord.get('lat')
            temp = main.get('temp')
            feels_like = main.get('feels_like')
            temp_min = main.get('temp_min')
            temp_max = main.get('temp_max')
            pressure = main.get('pressure')
            humidity = main.get('humidity')
            sea_level = main.get('sea_level', 'N/A')
            grnd_level = main.get('grnd_level', 'N/A')
            main_weather = weather.get('main')
            description = weather.get('description')
            icon = weather.get('icon')
            visibility = data.get('visibility', 'N/A')
            Wind_speed = wind.get('speed')
            Wind_deg = wind.get('deg')
            Wind_gust = wind.get('gust', 'N/A')
            rain = rain.get('1h', 0)
            clouds = clouds.get('all')

        
            weather_data = {
    "city":city,
    "date": date,
    "lon": lon,
    "lat": lat,
    "temp": temp,
    "feels_like": feels_like,
    "temp_min": temp_min,
    "temp_max": temp_max,
    "pressure": pressure,
    "humidity": humidity,
    "sea_level": sea_level,
    "grnd_level": grnd_level,
    "main_weather": main_weather,
    "description": description,
    "icon": icon,
    "visibility": visibility,
    "Wind_speed": Wind_speed,
    "Wind_deg": Wind_deg,
    "Wind_gust": Wind_gust,
    "rain": rain,
    "clouds": clouds,
            }
        return render(request,"home.html",weather_data)
    except Exception as e:
              return render(request, "home.html", {"error": "Unable to retrieve weather data. Please try again."})

   
