from django.urls import path
from . import views


app_name = "base"
urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("profile", views.profile, name="profile"),
    path("playlists", views.playlists, name="playlists"),
    path("location", views.location, name="location"),
    path("friends", views.friends, name="friends"),
    path("about", views.about, name="about"),
]
