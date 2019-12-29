from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic.base import View
from django.utils import timezone


from .models import Category, Post, Comment, Tag


class HomeView(View):
    """Вывод полной домашней страницы"""
    def get(self, request):
        category_list = Category.objects.all()
        # __lte - меньше или равно
        post_list = Post.objects.filter(published_date__lte=timezone.now(), published=True)
        return render(request, 'blog/home.html', {'categories': category_list, 'posts': post_list})


class CategoryView(View):
    """Вывод статей гатегории"""
    def get(self, request, category_slug):
        current_category = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(
            # __ - хотим обратиться в модель на которую завязаны
            category__slug=category_slug, category__published=True, published=True
        )
        return render(request, posts.first().get_category_template(), {'posts': posts})


class PostDetailView(View):
    """Вывод поста"""
    def get(self, request, category, post_slug):
        categories = Category.objects.all()
        post = Post.objects.get(slug=post_slug, published_date__lte=timezone.now(), published=True)
        return render(request, post.template, {'post': post, 'categories': categories})


class TagView(View):
    """Вывод постов по тегам"""
    def get(self, request, tag_slug):
        posts = Post.objects.filter(tags__slug=tag_slug, published=True)
        return render(request, posts.first().get_category_template(), {'posts': posts})
