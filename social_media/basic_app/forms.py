from django import forms
from django.forms import fields
from basic_app.models import User


class UserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

