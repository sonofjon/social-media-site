from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


# class SignUpForm(forms.Form):
#     firstname =forms.CharField(max_length=63)
#     lastname =forms.CharField(max_length=63)
#     email=forms.EmailField(email, required=False)
#     username = forms.CharField(max_length==15)
#     password=forms.CharField(max_length=63, widget=forms.PasswordInput)
            
            
