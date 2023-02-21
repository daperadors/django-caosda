from django.http import HttpResponse
from django.shortcuts import render
from videojocs.models import Platform,Videogame
from django.views.generic.base import View
# Create your views here.
class home(View):
    def get(self, data):
        return render(data, 'html/index.html')

class videogames(View):
    def get(self, data):
        videogames = Videogame.objects.all()
        return render(data, 'html/videogames.html', context = {videogames})
    #def add_videojoc(self, data, platform_id):

class platforms(View):
    def get(self, data):
        return render(data, 'html/platform.html')

    def add_platform(self, request):
        Platform.objects.create(request, name = request.POST.get("name"), date = request.POST.get("date"), users = request.POST.get("users"))


