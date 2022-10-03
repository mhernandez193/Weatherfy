from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'base/home.html')
	
def profile(request):
	return render(request, 'base/profile.html')
	
def playlists(request):
	return render(request, 'base/playlists.html')
	
def location(request):
	return render(request, 'base/location.html')

def friends(request):
	return render(request, 'base/friends.html')

def about(request):
	return render(request, 'base/about.html')
