from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
# Create your views here.
from django.views.generic.base import View

class LoginView(View):
    def get(self, request):
        return render(request, '../templates/html/login.html')
    def post(self, request):
        print(request.POST.get("username"), request.POST.get('password'))
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        return self.get(request)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')

class register(View):
    def get(self, request):
        return render(request, '../templates/html/register.html')
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        return redirect('home')
