from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile
from django import forms



        
class SignUpForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class': 'form-control'
    }))
    
    email =  forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email address',
        'class': 'form-control'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class': 'form-control'
    }))
    
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' Reapeat Your password',
        'class': 'form-control'
    }))
    
    
    #login an existing user
class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ('username',  'password')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class': 'form-control'
    }))
    password =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':' Enter Your password',
        'class': 'form-control'
    }))