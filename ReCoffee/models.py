from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=200)
	rating = models.DecimalField(default=0, max_digits=1, decimal_places=1)
	#avatar = models.ImageField(null=True, upload_to='images')

class UserProfile(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	#avatar = models.ImageField(null=True, upload_to='avatars')
	birthday = models.DateField(null=True)
	user = models.OneToOneField(User, primary_key=True, related_name='profile')




