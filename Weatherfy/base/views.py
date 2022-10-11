from django.shortcuts import render
from django.http import HttpResponse
import folium
import geocoder
from .apis.Spotify import Spotify




def home(request):
    spotifyClient = Spotify()
    playlist = spotifyClient.fetchPlaylistByKeyword('rainy')
    data = {
        "playlist": playlist[0].items[0].uri
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
    return render(request, "base/friends.html")


def about(request):
    return render(request, "base/about.html")
