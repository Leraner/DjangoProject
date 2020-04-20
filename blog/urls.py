from django.urls import path

from .views import *

urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name='create_post'),
    path('tag/<slug:tag_slug>/', CategoryView.as_view(), name='tag'),
    path('<slug:category>/<slug:post_slug>/edit/', PostEditView.as_view(), name='edit_post'),
    path('<slug:category>/<slug:post_slug>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('<slug:category>/<slug:post_slug>/', PostDetailView.as_view(), name='detail_post'),
    path('<slug:category_slug>/', CategoryView.as_view(), name='category'),
    path('', HomeView.as_view(), name='home'),
]
