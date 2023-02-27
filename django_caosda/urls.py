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

from videojocs.views import home, videogames, platforms, platformRandom, platformEdit, platformDelete, platformRandomNewGames, usersPlatform, remove_videojoc, add_videojoc
from users.views import LoginView, LogoutView
from users.views import register

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', register.as_view(), name="register"),
    path('', home.as_view(), name="home"),
    path('videogames/', videogames.as_view(), name="videogames"),
    path('platforms/addVideogames/<int:id>', videogames.as_view()),
    path('platforms/', platforms.as_view(), name="platforms"),
    path('platforms/edit/<int:id>', platformEdit.as_view(), name="edit_platform"),
    path('platforms/add/', platforms.as_view(), name="add_platform"),
    path('randomPlatform/', platformRandom.as_view(), name="random_platform"),
    path('randomPlatformNewGames/', platformRandomNewGames.as_view(), name="random_platform_newgames"),
    path('platforms/delete/<int:id>', platformDelete.as_view(), name="delete_platform"),
    path('platforms/add/<int:id1>/<int:id2>', usersPlatform.as_view(), name="associate_user_into_platform"),
    path('plataformesde/<str:name>', usersPlatform.as_view(), name="user_platform_search"),
    path('removeVideojoc/<int:videogame_id>/<int:user_id>', remove_videojoc.as_view()),
    path('videojoc/<int:videogame_id>/<int:user_id>', add_videojoc.as_view()),
    path('plataformade/<str:name>', platforms.as_view())
]
