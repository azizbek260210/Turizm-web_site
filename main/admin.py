from django.contrib import admin
from . import models

"""Modellarni admin panelga registratsiya qilish"""
admin.site.register(models.Banner)
admin.site.register(models.AboutUs)
admin.site.register(models.Contact)
admin.site.register(models.Place)
admin.site.register(models.Service)
admin.site.register(models.Blog)
admin.site.register(models.Hotel)