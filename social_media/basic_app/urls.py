from django.conf.urls import url
from basic_app import views
from django.contrib import admin
from django.urls import path
import basic_app.views


app_name = "basic_app"

urlpatterns = [
    url(r'^homepage/$', views.homepage, name = "homepage"),
    url(r'^about/$', views.about, name = "about"),
    url(r'^myprofile/$', views.myprofile, name = "myprofile"),
    url(r'^discussions/$', views.discussions, name = "discussions"),
    url(r'^message/$', views.message, name = "message"),
    url(r'^signup/$', views.signup, name = "signup"),
    url(r'^login/$', views.login, name = "login"),
    url(r'^logout/$',basic_app.views.logout, name='logout'),
    
]
