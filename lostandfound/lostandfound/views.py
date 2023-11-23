from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User


def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email,password=password)
        
        if user is not None:
            login(request,user)
        else:
            pass
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmPassword']

        myuser = User.objects.create_user(name,email,password)
        myuser.save()
        print("register success", email)
        return redirect('login')

    return render(request,"register.html")