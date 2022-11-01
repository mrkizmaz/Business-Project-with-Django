from django.contrib import admin
from django.urls import path
from . import views

app_name = "business"

urlpatterns = [
    path('create/', views.index, name = "index"),
    path('post-<int:id>/', views.detailPost, name = "detailPost"),
]
