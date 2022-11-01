from django.contrib import admin
from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path('register/', views.registerManager, name = "registerManager"),
    path('login/', views.loginManager, name = "loginManager"),
    path('logout/', views.logoutManager, name = "logoutManager"),
    path('dashboard/', views.dashManager, name = "dashManager"),
    path('addpost/', views.addPost, name = "addPost"),
    path('post/<int:id>/', views.detailPost, name = "detailPost"),
    path('post/update/<int:id>/', views.updatePost, name = "updatePost"),
    path('post/delete/<int:id>/', views.deletePost, name = "deletePost"),
]