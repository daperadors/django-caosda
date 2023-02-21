from django.db import models
from django.contrib.auth.models import User

class Platform(models.Model):
    name = models.CharField(max_length=50, null= False)
    date = models.DateField(auto_now_add=True, null= True)
    users = models.ManyToManyField('auth.User')
    class Meta:
        ordering = ['name', 'date']
    def __str__(self):
        return "%s the user" % self.name

class Videogame(models.Model):
    name = models.CharField(max_length=10, null = False)
    subscription_price = models.IntegerField(null = False, default = 0)
    isNew = models.BooleanField(null = False, default = False)
    users = models.ManyToManyField('auth.User')
    plataform =  models.ForeignKey(Platform, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', 'subscription_price', 'isNew']
    def __str__(self):
        return "%s the videogame" % self.name