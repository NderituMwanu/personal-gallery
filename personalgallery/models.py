# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime as dt
from django.db import models

# Image editor model

class Editor(models.Model):
    Username = models.CharField(max_length =30)
    # location = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.Username

    class Meta:
        ordering = ['Username']


# Image Category Model

class Category(models.Model):
    image_category = models.CharField(max_length = 30)
    

    def __str__(self):
        return self.image_category

# Function for the Image location 
class Location(models.Model):
    image_location = models.CharField(max_length =30)
    

    def __str__(self):
        return self.image_location

    
    
# Image model

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length = 500)
    Username = models.ForeignKey(Editor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'images/', default='default.png')

    def __str__(self):
        return self.post_image


    @classmethod
    def post_of_today(cls):
        today = dat.date.today()
        image = cla.objects.filter(pub_date__date = today)
        return image
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()