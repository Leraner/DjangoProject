from django.conf import settings
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin

from .views import get_page


class PageFallbackMiddleware(MiddlewareMixin):
    """При поступлении запроса проверяет его и если не
        находит страницу идёт логика ниже"""
    def process_response(self, request, response):
        if response.status_code != 404:
            return response
        try:
            return get_page(request, request.path_info)
        except Http404:
            return response
        except Exception:
            if settings.DEBUG:
                raise
            return response

