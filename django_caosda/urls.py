"""django_caosda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from videojocs.views import home
from videojocs.views import videogames
from users.views import login
from users.views import register

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('login/', login.as_view(), name="login"),
    path('register/', register.as_view(), name="register"),
    path('', home.as_view(), name="home"),
    path('videogames/', videogames.as_view(), name="videogames"),
]
