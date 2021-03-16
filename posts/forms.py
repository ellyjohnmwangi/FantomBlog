from .models import *
from django import forms


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
            'title',
            'category',
            'content',
            'image',
            'tag'
        ]
