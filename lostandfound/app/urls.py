from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import views as auth

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.signin, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", auth.LogoutView.as_view(template_name="index.html"), name="logout")
]