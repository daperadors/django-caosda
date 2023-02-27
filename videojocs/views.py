from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from videojocs.models import Platform,Videogame, platforms_users
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.contrib.auth.models import User
import random
from django.urls import resolve
from datetime import datetime
from django.core.paginator import Paginator
# Create your views here.
class home(View):
    def get(self, data):
        return render(data, 'html/index.html')

class videogames(LoginRequiredMixin, View):
    def get(self, data):
        videogames = Videogame.objects.select_related('platform')
        platforms = Platform.objects.all()
        context = {
            'videogames': videogames,
            'platforms': platforms
        }
        return render(data, 'html/videogames.html', context = context)
    def post(self, request, id):
        backUrl = request.META.get('HTTP_REFERER')
        name = request.POST['name']
        price = request.POST['price']
        isnew = 0
        if 'isnew' in request.POST:
            if request.POST['isnew'] == "on":
                isnew = 1
            else:
                isnew = 0
        else:
            isnew = 0
        platform = Platform.objects.get(id=id)
        videogame = Videogame(name=name, subscription_price=price, isNew=isnew, platform_id=platform.id)
        videogame.save()
        return redirect(backUrl)


class platforms(LoginRequiredMixin, View):
    def get(self, data):
        platforms = Platform.objects.all()
        users = User.objects.filter(is_staff=0)
        context = {
            'platforms':platforms,
            'users': users
        }
        return render(data, 'html/platform.html', context = context)
    def get(self, request, name):
        backUrl = request.META.get('HTTP_REFERER')
        print(backUrl)
        user = User.objects.filter(username=name)
        if user:
            platforms_inter = platforms_users.objects.filter(user_id=user[0])
            if platforms_inter:
                idList = []
                for p in platforms_inter:
                    idList.append(p.platform_id)

                platforms = Platform.objects.filter(id__in=idList).values()
                randomPlatform =  list(platforms)[random.randint(0, len(list(platforms))-1)]
                return JsonResponse(randomPlatform, safe=False)
        else:
            return redirect(backUrl)
    def post(self, request):
        backUrl = request.META.get('HTTP_REFERER')
        name = request.POST['name']
        datestr = request.POST['date']
        date = datetime.strptime(datestr, '%Y-%m-%d').date()

        platform = Platform(name=name, date=date)
        platform.save()

        return redirect(backUrl)
class usersPlatform(LoginRequiredMixin, View):
    def get(self, request, name):
        backUrl = request.META.get('HTTP_REFERER')
        print(backUrl)
        user = User.objects.filter(username=name)
        if user:
            platforms_inter = platforms_users.objects.filter(user_id = user[0])
            if platforms_inter:
                idList = []
                for p in platforms_inter:
                    idList.append(p.platform_id)

                platforms = Platform.objects.filter(id__in = idList).values()
                print(platforms)
                return JsonResponse(list(platforms), safe=False)
        else:
            return redirect(backUrl)
    def post(self, request, id1, id2):
        backUrl = request.META.get('HTTP_REFERER')

        platform = Platform.objects.get(id=id1)
        user = User.objects.get(id=id2)

        platform.users.add(user)
        platform.save()
        return redirect(backUrl)

class platformEdit(LoginRequiredMixin, View):
    def post(self, request, id):
        backUrl = request.META.get('HTTP_REFERER')
        platform = Platform.objects.get(id=id)

        platform.name = request.POST['name']
        datestr = request.POST['date']
        platform.date = datetime.strptime(datestr, '%Y-%m-%d').date()
        platform.save()
        return redirect(backUrl)

class platformDelete(LoginRequiredMixin, View):
    def post(self, request, id):
        backUrl = request.META.get('HTTP_REFERER')
        platform = Platform.objects.get(id=id).delete()
        return redirect(backUrl)

class platformRandom(LoginRequiredMixin, View):
    def get(self, data):
        platforms = Platform.objects.all()
        if(platforms):
            platform = random.choice(platforms)
            context={
                'platform':platform
            }
            return render(data, 'html/platformRandom.html', context=context)
        else:
            context={
                'platform':platforms
            }
            return render(data, 'html/platformRandom.html', context=context)

class platformRandomNewGames(LoginRequiredMixin, View):
    def get(self, data):
        newVideogames = Videogame.objects.filter(isNew=1)
        if(newVideogames):
            videogame = random.choice(newVideogames)
            platform = Platform.objects.get(id=videogame.platform_id)
            context={
                'platform':platform
            }
            return render(data, 'html/platformRandom.html', context=context)
        else:
            context={
                'platform':platforms
            }
            return render(data, 'html/platformRandom.html', context=context)

class remove_videojoc(LoginRequiredMixin, View):
    def get(self, request, videogame_id, user_id):
        user = User.objects.get(id = user_id)
        videogame = Videogame.objects.get(id = videogame_id)

        videogame.users.remove(user)
        return JsonResponse(videogame.name +" removed to " + user.username, safe=False)

class add_videojoc(LoginRequiredMixin, View):
    def get(self, request, videogame_id, user_id):
        user = User.objects.get(id = user_id)
        videogame = Videogame.objects.get(id = videogame_id)

        videogame.users.add(user)
        videogame.save()

        return JsonResponse(videogame.name +" added to "+user.username, safe=False)

