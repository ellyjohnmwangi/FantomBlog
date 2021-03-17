from .models import *
from django import forms


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Enter your title here'}),
            'content': forms.Textarea(attrs={'class': 'single-input', 'placeholder': ' What do you have in mind?'}),
        }

        fields = [
            'title',
            'category',
            'content',
            'image'
        ]
