from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.views.generic.base import View
from django.utils import timezone
from django.http import Http404


from .forms import CommentForm
from .models import Category, Post, Comment, Tag


class HomeView(View):
    """Вывод полной домашней страницы"""
    def get(self, request):
        # __lte - меньше или равно
        post_list = Post.objects.filter(published_date__lte=timezone.now(), published=True)
        return render(request, 'blog/home.html', {'posts': post_list})


class CategoryView(View):
    """Вывод статей гатегории и тегов"""
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now(), published=True)

    def get(self, request, category_slug=None, tag_slug=None):
        if category_slug is not None:
            # __ - хотим обратиться в модель на которую завязаны
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        elif tag_slug is not None:
            posts = self.get_queryset().filter(tags__slug=tag_slug, tags__published=True)
        else:
            posts = self.get_queryset()
        # exists - спрашивает есть ли хоть одна статья в категории
        if posts.exists():
            template = posts.first().get_category_template()
        else:
            # template = 'blog/post_list.html'
            raise Http404()
        return render(request, template, {'posts': posts})


class PostDetailView(View):
    """Вывод поста"""
    def get(self, request, **kwargs):
        post = get_object_or_404(
            Post, slug=kwargs.get('post_slug'),
            published_date__lte=timezone.now(),
            published=True
        )
        post.viewed += 1    # инкрементируем счётчик просмотров и обновляем поле в базе данных
        post.save(update_fields=['viewed'])    # update_fields=['viewed']
        form = CommentForm()
        return render(
            request, post.template, {'post': post, 'form': form}
        )

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)
        print(request.POST.get('post'))
        if form.is_valid():
            form = form.save(commit=False)
            # form.post_id = request.POST.get('post')
            form.post_id = Post.objects.get(slug=kwargs.get('post_slug')).id
            form.author = request.user
            form.save()
        return redirect(request.path)

# class CreateCommentView(View):
#     def post(self, request, pk):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.post_id = pk
#             form.author = request.user
#             form.save()
#         return HttpResponse(status=201)
