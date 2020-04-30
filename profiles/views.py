from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib import messages

from .forms import ProfileForm
from .models import Profile


class ProfileUpdateView(View):
    """Редактирование профиля"""
    def get(self, request, profile_slug):
        profile = get_object_or_404(Profile, published=True, slug=profile_slug)
        form = ProfileForm(instance=profile)

        # Проверка пользователя, request.user == profile.author, супер юзер, персонал или нет
        if not request.user == profile.author:
            if not request.user.is_authenticated:
                raise Http404
            else:
                if not request.user.is_staff or not request.user.is_superuser:
                    raise Http404
                else:
                    return render(request, 'profile/update_profile_form.html', {'profile': profile, 'form': form})
        else:
            return render(request, 'profile/update_profile_form.html', {'profile': profile, 'form': form})

    def post(self, request, **kwargs):
        profile = get_object_or_404(Profile, published=True, slug=kwargs.get('profile_slug'))
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')
            # return redirect(reverse_lazy('detail_myprofile', form.slug))


class MyProfileDetailView(View):
    """Отображение страницы котору можно редактировать"""
    def get(self, request, profile_slug):
        profile = get_object_or_404(Profile, published=True, slug=profile_slug)

        return render(request, 'profile/my_profile.html', {'profile': profile})


class ProfileDetailView(View):
    """Отображение страницы котору нельзя редактировать"""
    def get(self, request, profile_slug):
        profile = get_object_or_404(Profile, published=True, slug=profile_slug)

        if not request.user == profile.author:
            if not request.user.is_staff or not request.user.is_superuser:
                return render(request, 'profile/profile_detail.html', {'profile': profile})
            else:
                return render(request, 'profile/my_profile.html', {'profile': profile})
        else:
            return render(request, 'profile/my_profile.html', {'profile': profile})


@receiver(user_logged_in)
def got_online(sender, user, request, **kwargs):
    request.user.profile.is_online = True
    print(request.user.profile)
    user.profile.save()


@receiver(user_logged_out)
def got_offline(sender, user, request, **kwargs):
    request.user.profile.is_online = False
    print(request.user.profile)
    user.profile.save()
