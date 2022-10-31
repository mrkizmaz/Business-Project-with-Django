from django.shortcuts import render
from .forms import BusinessForm

# Create your views here.

def index(request):
    return render(request, "index.html")



