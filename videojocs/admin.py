from django.contrib import admin
from django import forms
from videojocs.models import Videogame, Platform
class VideogameAdmin(admin.ModelAdmin):
    fields = ['name', 'subscription_price', 'isNew', 'platform']
class PlatformAdmin(admin.ModelAdmin):
    fields = ['name', 'date']


admin.site.register(Videogame, VideogameAdmin)
admin.site.register(Platform, PlatformAdmin)
