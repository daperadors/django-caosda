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
        context = {
            'videogames': videogames
        }
        return render(data, 'html/videogames.html', context=context)
    #def post(self, data, platform_id):


class platforms(View):
    def get(self, data):
        return render(data, 'html/platform.html')

    def post(self, request):
        name = request.POST['name']
        date = request.POST['date']
        users_id = request.POST.getlist['users']
        users = User.objects.filter(id__in=users_id)
        platform = Platform(name = name, date = date)
        platform.save()


