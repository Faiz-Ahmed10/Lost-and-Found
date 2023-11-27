
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app.models import Users
# from django.db import models
import random
def index(request):
    return render(request,"index.html")

def signin(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(user=name,password=password)
        
        if user is not None:
            login(request,user)
            uname = user.username
            return render(request,"index.html",{'uname':uname})
        else:
            messages.error(request, f'please create a account to login !')
            return redirect('register')
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmPassword']
        id=random.randint(10**9, 10**10 - 1)
        myuser = Users.objects.create(user=name,email=email,password=password,id=id)
        myuser.save()

        messages.success(request, f'Your account has been created ! You are now able to log in')
        return redirect('login')

    return render(request,"register.html")

def signout(request):
    logout(request)
    messages.error(request, f'logged out successfull !')
    return redirect('home')