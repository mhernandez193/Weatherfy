from django.test import TestCase
import geocoder
import folium
import ipinfo

# Create your tests here.

class URLTests(TestCase):
	def test_homepage(self):
		response = self.client.get('')
		self.assertEquals(response.status_code, 200)
	def test_homepage2(self):
		response = self.client.get('/home')
		self.assertEquals(response.status_code, 200)
	def test_location(self):
		response = self.client.get('/location')
		self.assertEquals(response.status_code, 200)
	def test_profile(self):
		response = self.client.get('/profile')
		self.assertEquals(response.status_code, 200)
	def test_friends(self):
		response = self.client.get('/friends')
		self.assertEquals(response.status_code, 200)
	def test_about(self):
		response = self.client.get('/about')
		self.assertEquals(response.status_code, 200)
	def test_register(self):
		response = self.client.get('/register')
		self.assertEquals(response.status_code, 200)
	def test_playlists(self):
		response = self.client.get('/playlists')
		self.assertEquals(response.status_code, 200)

class LocationTests(TestCase):
	def test_ip_location_state(self):
		loc = geocoder.ip('216.239.36.21')
		self.assertEquals(loc.state,"California")
	def test_ip_location_city(self):
		loc = geocoder.ip('216.239.36.21')
		self.assertEquals(loc.city,"Mountain View")
