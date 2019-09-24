from django.shortcuts import render
import requests
from .models import City

def index(request):
    appid = '2a04a7f416f8792391a8b74c3a2a3d88'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        print(url)
        print(city_info)

        all_cities.append(city_info)

    context = {'all_info': all_cities}

    return render(request, 'weather/index.html', context)

# Create your views here.
