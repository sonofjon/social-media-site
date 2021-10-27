from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from . import forms
# from basic_app.forms import LoginForm,SignUpForm

# Create your views here.

def welcome(request):
    return render(request,"basic_app/welcome.html")
def logout(request):
    return redirect("basic_app/index")

def homepage(request):
    return render(request, "basic_app/homepage.html")

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
            return redirect("basic_app/myprofile")
    else:
        form = UserCreationForm()
    return render(request, "basic_app/signup.html", {'form': form})

def login(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect("basic_app/myprofile")
            else:
                message = 'Login User dont exist You your failed your login!'
    return render(request, "basic_app/login.html" , context={'form': form, 'message': message})
