from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:profile_slug>/my_profile/edit/', ProfileUpdateView.as_view(), name='update_profile'),
    path('<slug:profile_slug>/my_profile/', MyProfileDetailView.as_view(), name='detail_myprofile'),
    path('<slug:profile_slug>/', ProfileDetailView.as_view(), name='detail_profile'),
]
