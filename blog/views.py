from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic.base import View


from .models import Category, Post, Comment


class HomeView(View):
    """Вывод полной домашней страницы"""
    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.all()
        print(category_list)
        print(post_list)
        return render(request, 'blog/home.html', {'categories': category_list, 'posts': post_list})


class CategoryView(View):
    """Вывод статей гатегории"""
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        return render(request, 'blog/category_list.html', {'category': category})


class PostView(View):
    """Вывод поста"""
    def get(self, request, post_slug):
        post = Post.objects.get(slug=post_slug)
        return render(request, 'blog/post_list.html', {'post': post})
