from django import forms
from .models import CraftPost, Comment

class CraftForm(forms.ModelForm):

	class Meta:
		model = CraftPost
		fields = ('title', 'photo', 'text', 'link',)

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)
