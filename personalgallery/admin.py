# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Editor, Image, Location, Category

# Register your models here.

admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
