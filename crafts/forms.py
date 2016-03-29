from django import forms
from .models import CraftPost, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CraftForm(forms.ModelForm):

	class Meta:
		model = CraftPost
		fields = ('title', 'photo', 'text', 'link', 'postcategory',)

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ( 'author', 'text',)
