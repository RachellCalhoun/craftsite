from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    location = forms.CharField(required=False)
    picture =  forms.ImageField(required=False)
    hobby = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "location", "picture","hobby")


    
        
        
    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user


