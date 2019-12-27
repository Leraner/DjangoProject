from django.urls import path


from .views import HomeView, CategoryView, PostView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<slug:category_slug>/', CategoryView.as_view(), name='category'),
]
