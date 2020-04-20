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


