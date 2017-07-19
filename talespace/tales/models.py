from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import django.utils.timezone as timezone


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    city = models.CharField(max_length=40)
    country = CountryField()

    def __str__(self):
        return self.user.get_full_name()


class Tale(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author)
    content = models.TextField()
    header_img = models.CharField(max_length=100, default="#")

    def __str__(self):
        return self.title
