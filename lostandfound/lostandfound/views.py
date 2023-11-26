from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def index(request):
    return render(request,"index.html")

def signin(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(username=name,password=password)
        
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

        myuser = User.objects.create_user(name,email,password)
        myuser.save()

        messages.success(request, f'Your account has been created ! You are now able to log in')
        return redirect('login')

    return render(request,"register.html")

def signout(request):
    logout(request)
    messages.error(request, f'logged out successfull !')
    return redirect('home')