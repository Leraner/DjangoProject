from django.db import models


class Tag(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Comment(models.Model):
    """Модель комментария"""
    text = models.TextField('Текст')
    create_data = models.DateTimeField('Дата создания', auto_now_add=True)
    slug = models.SlugField('url', max_length=100, unique=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Post(models.Model):
    """Модель поста"""
    title = models.CharField('Заголовок', max_length=250)
    mini_text = models.TextField('Описание')
    text = models.TextField('Текст')
    create_data = models.DateTimeField('Дата создания', auto_now_add=True)
    slug = models.SlugField('url', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(models.Model):
    """Модель категории"""
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
