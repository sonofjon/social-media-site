from django.http import HttpResponseRedirect
from django.shortcuts import render
from basic_app import forms
from django.views import View
from django.views.generic import TemplateView


def index(request):
    return render(request, 'basic_app/index.html')



class UserProfile(View):
    form_class = forms.UserProfile
    initial = {'key': 'value'}
    template_name = 'user.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Bad Form! Bad!")  # devhelp debug
            
        return render(request, self.template_name, {'form': form})




