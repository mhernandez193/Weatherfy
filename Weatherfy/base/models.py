from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	spotifyLink = models.TextField()
	profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
	playlist = models.CharField(max_length=255, null=True, blank=True)
	def __str__(self):
		return str(self.user)
