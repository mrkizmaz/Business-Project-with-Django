from django.shortcuts import render, redirect, get_object_or_404
from business.models import Business
from .forms import RegisterForm_User, LoginForm_User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerEmployer(request):
    form = RegisterForm_User(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        newUser = User(username = username, email = email)
        newUser.set_password(password)
        newUser.save()

        login(request, newUser) 
        messages.success(request, message = 'You have successfully registered.')
        
        return redirect("employer:dashEmployer")
        
    context = {'form': form}
    return render(request, 'register_employer.html', context)

def loginEmployer(request):
    form = LoginForm_User(request.POST or None)
    
    context = {'form': form}
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.warning(request, message = 'Username or password is incorrect!')
            return render(request, 'login_employer.html', context)
        
        messages.success(request, message = 'You have successfully logged in.')
        login(request, user)
        return redirect("employer:dashEmployer")

    return render(request, "login_employer.html", context) 

def logoutEmployer(request):
    logout(request)
    messages.info(request, message = "You have successfully logged out.")
    return redirect("index")

@login_required(login_url = "index")
def dashEmployer(request):
    posts = Business.objects.filter(publisher = request.user)

    context = {
        "posts": posts
    }

    return render(request, "dash_employer.html", context)

def applyPost(request, id):
    # post = Business.objects.filter(id = id).first()
    post = get_object_or_404(Business, id = id)
    return render(request, "apply_post.html", {"post":post})

"""@login_required(login_url = "index")
def addPost(request):
    form = BusinessForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        business = form.save(commit = False)
        business.publisher = request.user
        business.save()

        messages.success(request, message = "Job posting created successfully.")
        return redirect("manager:dashManager")

    return render(request, "add_post.html", {"form": form})

def detailPost(request, id):
    # post = Business.objects.filter(id = id).first()
    post = get_object_or_404(Business, id = id)
    return render(request, "detail_post.html", {"post":post})

@login_required(login_url = "index")
def updatePost(request, id):
    post = get_object_or_404(Business, id = id)
    form = BusinessForm(request.POST or None, request.FILES or None, instance = post)
    
    if form.is_valid():
        business = form.save(commit = False)
        business.publisher = request.user
        business.save()

        messages.success(request, message = "The post updated successfully.")
        return redirect("manager:dashManager")

    return render(request, "update_post.html", {"form":form})

@login_required(login_url = "index")
def deletePost(request, id):
    post = get_object_or_404(Business, id = id)

    post.delete()
    messages.success(request, message = "The post deleted successfully.")
    return redirect("manager:dashManager")"""
