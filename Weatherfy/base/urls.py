from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import PasswordChange, EditProfile
app_name = "base"
urlpatterns = [
    path("", views.home, name="home"),
    path("admin", admin.site.urls),
    path("callback", views.callback, name="callback"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("home", views.home, name="home"),
    path("profile", views.profile, name="profile"),
    path("playlists", views.playlists, name="playlists"),
    path("location", views.location, name="location"),
    path("friends", views.friends, name="friends"),
    path("about", views.about, name="about"),
    path("userLogin", views.userLogin, name="userLogin"),
    path("userLogout", views.userLogout, name="userLogout"),
    path("register", views.register, name="register"),
    path("editprofile", EditProfile.as_view(), name="editprofile"),
    path("password/", PasswordChange.as_view(template_name='base/changepass.html')),
    path('togglePlayPause/', views.togglePlayPause, name='togglePlayPause'),
    path('skipForward/', views.skipForward, name='skipForward'),
    path('playSong/', views.playSong, name='playSong'),
    path('skipBackward/', views.skipBackward, name='skipBackward'),
    path('toggleFavorite/', views.toggleFavorite, name='toggleFavorite'),
]

