# Generated by Django 2.2.7 on 2020-03-05 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100, null=True, verbose_name='Статус')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Главная фотография')),
                ('published', models.BooleanField(default=True, verbose_name='Отображать?')),
                ('slug', models.CharField(default='912959', max_length=10, unique=True, verbose_name='url')),
                ('create_data', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата редактирования')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
