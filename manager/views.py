from django.shortcuts import render, redirect
from .forms import RegisterForm_Manager, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def registerManager(request):
    form = RegisterForm_Manager(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        newUser = User(username = username, email = email)
        newUser.set_password(password)
        newUser.save()

        login(request, newUser) 
        messages.success(request, message = 'You have successfully registered.')
        
        return redirect('index')
        
    context = {'form': form}
    return render(request, 'register.html', context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    
    context = {'form': form}
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request, message = 'Username or password is incorrect!')
            return render(request, 'login.html', context)
        
        messages.success(request, message = 'You have successfully logged in.')
        login(request, user)
        return redirect('index')
    
    return render(request, 'login.html', context) 

def logoutUser(request):
    pass
