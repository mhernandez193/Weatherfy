from django.shortcuts import render

import ipinfo
import environ
from datetime import datetime
from random import randint
from django.http import HttpResponse
import folium
import geocoder
from .apis.Spotify import Spotify
from .apis.Weather import fetchWeather

env = environ.Env()
environ.Env.read_env()


def home(request):
    city = None

    # User searched weather for a different city
    if request.method == 'POST':
        city = request.POST['city']

    # Current city
    else:
        # Grab IP address from request
        if env("STAGE") == 'DEV':
            ipAddress = '216.239.36.21'  # Mountain View, CA
        else:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ipAddress = x_forwarded_for.split(',')[0]
            else:
                ipAddress = request.META.get('REMOTE_ADDR')

        # Fetch geolocation using IP
        handler = ipinfo.getHandler(env("IP_INFO_ACCESS_TOKEN"))
        details = handler.getDetails(ipAddress)
        city = details.city

    # Fetch weather for city
    weather = fetchWeather(city)

    # Fetch Spotify playlist using weather
    spotifyClient = Spotify()
    playlist = spotifyClient.fetchPlaylistByKeyword(
        weather['weather'][0]['description'])

    # Create data payload
    current_time = datetime.now()
    formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")

    data = {
        "city": str(city),
        "weather": {
            'city': city,
            'description': weather['weather'][0]['description'],
            'icon': weather['weather'][0]['icon'],
            'temperature': str(weather['main']['temp']) + ' °F',
            'country_code': weather['sys']['country'],
            'wind': 'Wind: ' + str(weather['wind']['speed']) + ' m/h',
            'humidity': 'Humidity: ' + str(weather['main']['humidity']) + '%',
            'time': formatted_time
        },
        "playlist": playlist[0].items[randint(0, playlist[0].total-1)]
    }

    return render(request, "base/home.html", data)


def profile(request):
    return render(request, "base/profile.html")


def playlists(request):
    return render(request, "base/playlists.html")


def location(request):
    #geolocation
	location = geocoder.ip('me')
	coords = location.latlng
	country = location.country
	city = location.city
	state = location.state
	
	#map object
	m = folium.Map(width = 1500, height = 750, location=[19,-12], zoom_start=3)
	folium.Marker(coords, tooltip='More Information', 
	popup=(country + ", " + city + ", " + state)).add_to(m)
	#html representation
	m = m._repr_html_()
	context={'m' : m,}
	return render(request, 'base/location.html', context)

def friends(request):
    data = {
        'friends': [],
        'users': [],
    }
    return render(request, "base/friends.html", data)


def about(request):
    return render(request, "base/about.html")
