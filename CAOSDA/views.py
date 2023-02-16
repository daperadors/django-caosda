from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
class Saludos(View):
    def get(self,data):
        return HttpResponse(content='El troya es homo, se equivoca es el david')