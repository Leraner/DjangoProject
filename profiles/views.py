from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic.base import View
from django.views.generic import DetailView
from django.utils import timezone
from django.http import Http404


from .models import Profile


# class ProfileView(DetailView):
#     model = Profile
#     content_object_name = 'profile'
#     template_name = 'profile/profile_detail.html'


# def get_profile(request, profile_slug):
#     profile = get_object_or_404(Profile, published=True, slug="/" + profile_slug + "/")
#     return ProfileView(request, profile)


class ProfileDetailView(View):
    def get(self, request, profile_slug):
        profile = get_object_or_404(Profile, published=True, slug=profile_slug)
        return render(request, 'profile/profile_detail.html', {'profile': profile})

