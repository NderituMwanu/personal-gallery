# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.uploadedfile import SimpleUploadedFile

from django.test import TestCase
from .models import Editor, Image, Location, Category

# All view function tests

class EditorTestClass(TestCase):
    #Set Up Method
    def setUp(self):
        self.gerald= Editor(Username = 'Gerald', email = "samplemail@gmail.com")

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gerald,Editor))

class ImageTestClass(TestCase):

    # def setUp(self):
    #     self.newphoto= Image(image_name='test_image.jpg', image_description = "bob", pub_date = "12-3-2020") 

    def setUp(self):

        #Posting a new image and saving it
        self.newphoto = Image(image_name ="deafults.jpg", image_description = "sampleimage", pub_date = "12-3-2020")
        self.newphoto.save_image()


        #deletion of an image
        self.newphoto = Image(image_name ="defaults.jpg", image_description = "samplimage", pub_date = "12-3-2020")
        self.newphoto.delete_image()



    def tearDown(self):
        Image.objects.all().delete()
        Editor.objects.all().delete()
         