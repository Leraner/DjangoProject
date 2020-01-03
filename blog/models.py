from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Tag(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100, unique=True)
    published = models.BooleanField('Отображать?', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(MPTTModel):
    """Модель категории"""
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)
    # default='' - позволяет не удалять миграции
    description = models.TextField('Описание', max_length=1000, default='', blank=True)
    # Подкатегории, => наследуется от MPTTModel
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    # default - уже адресс
    template = models.CharField('Шаблон', max_length=500, default='blog/post_list.html')
    published = models.BooleanField('Отображать?', default=True)
    paginated = models.PositiveIntegerField('Кол-во новостей на странице', default=5)
    sort = models.PositiveIntegerField('Порядок', default=0)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """Модель поста"""
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField('Заголовок', max_length=250)
    mini_text = models.TextField('Краткое содержание', max_length=5000)
    text = models.TextField('Текст', max_length=10000000)
    subtitle = models.TextField('Под заголовок', max_length=500, blank=True, null=True)
    slug = models.SlugField('url', max_length=100, unique=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэг', blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True,
    )
    image = models.ImageField('Главная фотография', upload_to='post/', null=True, blank=True)
    edit_date = models.DateTimeField(
        'Дата редактирования',
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
        blank=True,
        null=True
    )
    template = models.CharField('Шаблон', max_length=500, default='blog/post_detail.html')
    published = models.BooleanField('Отображать?', default=True)
    viewed = models.PositiveIntegerField('Просмотрено', default=0)
    status = models.BooleanField('Для зарегестрированных', default=False)
    sort = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        # Сортировака по дате публикации
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'post_slug': self.slug})

    def get_comments_count(self):
        return self.comments.count()

    def get_category_template(self):
        return self.category.template


class Comment(models.Model):
    """Модель комментария"""
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        verbose_name='Статья',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField('Текст')
    create_data = models.DateTimeField('Дата создания', auto_now_add=True)
    # slug = models.SlugField('url', max_length=100, unique=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        # Сортировака по дате публикации
        ordering = ['-create_data']
