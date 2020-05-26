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
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
 

    
    
# Image model

class Image(models.Model):
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length = 500)
    # image_category = models.CharField(max_length = 30, default="none")
    username = models.ForeignKey(Editor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'images/', default='default.png')

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__name__icontains=search_term)
        return gallery

    @classmethod
    def gallery_images(cls):
        gallery = cls.objects.all()
        return gallery

    @classmethod
    def get_by_location(cls,search_term):
        gallery = cls.objects.filter(location__name__icontains=search_term)
        return gallery
