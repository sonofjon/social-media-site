from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from . import forms

# Create your views here.

def homepage(request):
    return render(request,"basic_app/homepage.html")

def about(request):
    return render(request, "basic_app/about.html")

def myprofile(request):
    return render(request, "basic_app/myprofile.html")

def discussions(request):
    return render(request, "basic_app/discussionpage.html")

def message(request):
    return render(request, "basic_app/messagepage.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(firstname=firstname, lastname=lastname, username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "basic_app/signup.html", {'form': form})

def login(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, "basic_app/login.html", context={'form': form})