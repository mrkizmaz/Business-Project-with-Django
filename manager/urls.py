from django.contrib import admin
from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path('register/', views.registerManager, name = "registerManager"),
    path('login/', views.loginUser, name = "loginUser"),
    path('logout/', views.logoutUser, name = "logoutUser"),
]