from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponsePermanentRedirect, Http404
from django.views.decorators.csrf import csrf_protect


from .models import Page


def get_page(request, url):
    """
    Получение страницы по url
    Нужно если при написании пути пользователь забыл поставить '/'
    """
    if not url.startswith('/'):
        url = '/' + url
    try:
        page = get_object_or_404(Page, slug=url, published=True)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            page = get_object_or_404(Page, slug=url, published=True)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    return render_page(request, page)


@csrf_protect
def render_page(request, page):
    """Рендер страницы"""
    if page.registration_required and not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        # request.path - если человек авторизуется то его отправляют на страницу где он был
        return redirect_to_login(request.path)
    return render(request, page.template, {'page': page})
