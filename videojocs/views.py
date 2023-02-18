from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
class home(View):
    def get(self,data):
        return render(data, 'html/index.html')

class videogames(View):
    def get(self,data):
        return render(data, 'html/videogames.html')