from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from .models import Profile

from .models import Profile


class ProfileForm(forms.ModelForm):
    """Класс формы пользователя"""

    class Meta:
        model = Profile
        fields = ('author', 'status', 'image', 'slug',)


class ProfileUserEditForm(forms.ModelForm):
    """Класс формы изменение данных пользователя"""

    class Meta:
        model = Profile
        fields = (
            'status',
        )
