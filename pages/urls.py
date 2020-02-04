from django.urls import path, include


from .views import get_page


urlpatterns = [
    path('<path:url>', get_page, name='page')
]