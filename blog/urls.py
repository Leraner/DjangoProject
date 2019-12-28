from django.urls import path


from .views import *


urlpatterns = [
    path('<slug:category>/<slug:post_slug>/', PostDetailView.as_view(), name='detail_post'),
    path('<slug:category_slug>/', CategoryView.as_view(), name='category'),
    path('', HomeView.as_view(), name='home'),
]
