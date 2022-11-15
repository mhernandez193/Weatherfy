from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from base.models import Profile
		

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		
class EditProfileForm(UserChangeForm):
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = User
		fields = {'username', 'first_name', 'last_name'}

