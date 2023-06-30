from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse
from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                # register user
                user = User.objects.create(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'User alredy exist'
                })
                
            
        return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'Password do no match'
        })
    
def tasks(request):
    return render(request, 'tasks.html') 

def info(request):
    return render(request, 'info.html')
