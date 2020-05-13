from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Profile

from .models import Profile


class ProfileForm(forms.ModelForm):
    """Класс формы пользователя"""

    class Meta:
        model = Profile
        fields = ('status', 'image', 'slug',)
        widgets = {
            'status': forms.TextInput(attrs={
                'placeholder': 'Status',
                'class': 'form-control',
                'id': 'status',
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Title',
                'class': 'form-control',
                'id': 'image',
            }),
            'slug': forms.TextInput(attrs={
                'placeholder': 'Slug',
                'class': 'form-control',
                'id': 'slug',
            }),
        }

