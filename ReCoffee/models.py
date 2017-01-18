from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class ShopProfile(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
#rating shouldn't be an attribute, should be a list
#displayed in tamplate as an average grade
    rating = models.DecimalField(
        default=0,
        max_digits=2,
        decimal_places=1)
	#avatar = models.ImageField(null=True, upload_to='images')

    def get_absolute_url(self):
        return reverse('shop_page', kwargs={'pk':self.pk})

class Review(models.Model):
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    shop = models.ForeignKey(ShopProfile)

class UserProfile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    #avatar = models.ImageField(null=True, upload_to='avatars')
    birthday = models.DateField(null=True)
    user = models.OneToOneField(
        User,
        primary_key=True,
        related_name='profile')

class Favorite(models.Model):
    f_id = models.IntegerField(default=0)
    username = models.CharField(max_length=20)
    shop_name = models.CharField(max_length=20)

#modified


