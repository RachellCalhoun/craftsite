from django import forms
from .models import CraftPost

class CraftForm(forms.ModelForm):

	class Meta:
		model = CraftPost
		fields = ('title', 'photo', 'text', 'link',)
