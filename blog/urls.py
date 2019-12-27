from django.urls import path


from .views import HomeView, CategoryView, PostView


urlpatterns = [
    path('<slug:post_slug>/', PostView.as_view(), name='post'),
    path('<slug:category_slug>/', CategoryView.as_view(), name='category'),
    path('', HomeView.as_view(), name='home'),
]
