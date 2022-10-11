from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, "base/location.html")


def friends(request):
    return render(request, "base/friends.html")


def about(request):
    return render(request, "base/about.html")
