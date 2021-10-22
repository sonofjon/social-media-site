from django.shortcuts import render
from django.http import HttpResponse
from basic_app import views

def homepage(request):
    my_dict={'insert me':""}
    return render (request,"homepage.html",context=my_dict)

# Create your views here.
