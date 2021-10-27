from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request,"basic_app/welcome.html")

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
    return render(request, "basic_app/signup.html")

def login(request):
    return render(request, "basic_app/login.html")
