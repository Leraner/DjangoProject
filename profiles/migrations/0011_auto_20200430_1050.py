# Generated by Django 3.0.5 on 2020-04-30 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20200430_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.CharField(default='9836286', max_length=10, unique=True, verbose_name='url'),
        ),
    ]
