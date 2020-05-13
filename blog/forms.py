from django import forms
from django.core.exceptions import ValidationError

from .models import Comment, Post, Tag


class CommentForm(forms.ModelForm):
    """Класс формы комментариев"""

    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):
    """Класс формы постов"""

    class Meta:
        model = Post
        fields = (
            'title', 'text', 'slug', 'tags',
            'category', 'image',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'form-control',
                'id': 'Status',
            }),
            'text': forms.Textarea(attrs={
                'placholder': 'Text',
                'class': 'form-control',
                'id': 'text',
            }),
            'slug': forms.TextInput(attrs={
                'placeholder': 'Slug',
                'class': 'form-control',
                'id': 'slug',
            }),
            'tags': forms.SelectMultiple(attrs={
                'placeholder': 'Tags',
                'class': 'form-control',
                'id': 'tags',
            }),
            'category': forms.Select(attrs={
                'placeholder': 'Category',
                'class': 'form-control',
                'id': 'category',
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Title',
                'class': 'form-control',
                'id': 'image',
            }),

        }


