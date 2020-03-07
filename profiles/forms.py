from django import forms


from .models import Profile


class ProfileForm(forms.ModelForm):
    """Класс формы пользователя"""
    class Meta:
        model = Profile
        fields = ('author', 'status', 'image', 'slug',)