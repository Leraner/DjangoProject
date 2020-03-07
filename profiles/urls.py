from django.urls import path

from .views import *

urlpatterns = [
    path('<slug:profile_slug>/', ProfileDetailView.as_view(), name='detail_profile'),
]
