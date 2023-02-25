from django.db import models
from django.contrib.auth.models import User

class Platform(models.Model):
    name = models.CharField(max_length=50, null= False)
    date = models.DateField(null= True)
    users = models.ManyToManyField('auth.User', through='platforms_users')
    class Meta:
        ordering = ['name', 'date']
    def __str__(self):
        return str(self.__dict__)

class Videogame(models.Model):
    name = models.CharField(max_length=30, null = False)
    subscription_price = models.IntegerField(null = False, default = 0)
    isNew = models.BooleanField(null = False, default = False)
    users = models.ManyToManyField('auth.User', through='videogames_users')
    platform =  models.ForeignKey(Platform, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', 'subscription_price', 'isNew']
    def __str__(self):
        return str(self.__dict__)
class platforms_users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

class videogames_users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    videogame = models.ForeignKey(Videogame, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)