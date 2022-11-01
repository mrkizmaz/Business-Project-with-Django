from django.contrib import admin
from django.urls import path
from . import views

app_name = "employer"

urlpatterns = [
    path('register/', views.registerEmployer, name = "registerEmployer"),
    path('login/', views.loginEmployer, name = "loginEmployer"),
    path('logout/', views.logoutEmployer, name = "logoutEmployer"),
    path('dashboard/', views.dashEmployer, name = "dashEmployer"),
    path('post-apply/<int:id>/', views.applyPost, name = "applyPost"),
    
    #path('addpost/', views.addPost, name = "addPost"),
    #path('post/<int:id>/', views.detailPost, name = "detailPost"),
    #path('post/update/<int:id>/', views.updatePost, name = "updatePost"),
    #path('post/delete/<int:id>/', views.deletePost, name = "deletePost"),
]