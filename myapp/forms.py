from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Write a Comment*'
    }))
    class Meta:
        model = CommentModel
        fields = ['content']