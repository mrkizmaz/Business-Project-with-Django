from django.shortcuts import render, get_object_or_404
from business.models import Business
from .forms import BusinessForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def detailPost(request, id):
    # post = Business.objects.filter(id = id).first()
    post = get_object_or_404(Business, id = id)
    return render(request, "detail_post.html", {"post":post})


