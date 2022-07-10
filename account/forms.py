from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = form.CharField(widget=forms.PasswordInput)