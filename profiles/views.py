from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.utils import timezone
from django.http import Http404
from django.contrib import messages

from .forms import ProfileUserEditForm
from .models import Profile


# class ProfileView(DetailView):
#     model = Profile
#     content_object_name = 'profile'
#     template_name = 'profile/profile_detail.html'


# def get_profile(request, profile_slug):
#     profile = get_object_or_404(Profile, published=True, slug="/" + profile_slug + "/")
#     return ProfileView(request, profile)

# class ProfileUpdateView(UpdateView):
#     model = Profile
#     fields = ['status']
#     template_name = 'profile/update_profile_form.html'


class ProfileUpdateView(View):
    def post(self, request, profile_slug):
        profile_form = ProfileUserEditForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid:
            profile_form.save()
            return redirect('/')

    def get(self, request, profile_slug):
        profile_form = ProfileUserEditForm(request.POST, instance=request.user.profile)
        return render(request, 'profile/update_profile_form.html', {'profile_form': profile_form})


class MyProfileDetailView(View):
    def get(self, request, profile_slug):
        profile = get_object_or_404(Profile, published=True, slug=profile_slug)
        return render(request, 'profile/my_profile.html', {'profile': profile})


class ProfileDetailView(View):
    def get(self, request, profile_slug):
        profile = get_object_or_404(Profile, published=True, slug=profile_slug)
        return render(request, 'profile/profile_detail.html', {'profile': profile})
