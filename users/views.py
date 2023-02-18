from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
class login(View):
    def get(self, request):
        return render(request, '../templates/html/login.html')

class register(View):
    def get(self, request):
        return render(request, '../templates/html/register.html')