from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic.base import View
from datetime import datetime


from .models import Category, Post, Comment


class HomeView(View):
    """Вывод полной домашней страницы"""
    def get(self, request):
        category_list = Category.objects.all()
        # __lte - меньше или равно
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        print(category_list)
        print(post_list)
        return render(request, 'blog/home.html', {'categories': category_list, 'posts': post_list})


class CategoryView(View):
    """Вывод статей гатегории"""
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        return render(request, 'blog/post_list.html', {'category': category})


class PostDetailView(View):
    """Вывод поста"""
    def get(self, request, category, post_slug):
        categories = Category.objects.all()
        post = Post.objects.get(slug=post_slug)
        return render(request, 'blog/post_detail.html', {'post': post, 'categories': categories})

