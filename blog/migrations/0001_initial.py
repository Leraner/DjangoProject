# Generated by Django 2.2.7 on 2020-01-03 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=100, verbose_name='url')),
                ('description', models.TextField(blank=True, default='', max_length=1000, verbose_name='Описание')),
                ('template', models.CharField(default='blog/post_list.html', max_length=500, verbose_name='Шаблон')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
                ('paginated', models.PositiveIntegerField(default=5, verbose_name='Кол-во новостей на странице')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.Category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='url')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('mini_text', models.TextField(max_length=5000, verbose_name='Краткое содержание')),
                ('text', models.TextField(max_length=10000000, verbose_name='Текст')),
                ('subtitle', models.TextField(blank=True, max_length=500, null=True, verbose_name='Под заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='url')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/', verbose_name='Главная фотография')),
                ('edit_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата редактирования')),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата публикации')),
                ('template', models.CharField(default='blog/post_detail.html', max_length=500, verbose_name='Шаблон')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
                ('viewed', models.PositiveIntegerField(default=0, verbose_name='Просмотрено')),
                ('status', models.BooleanField(default=False, verbose_name='Для зарегестрированных')),
                ('sort', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-published_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('create_data', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('moderation', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-create_data'],
            },
        ),
    ]
