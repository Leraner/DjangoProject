# Generated by Django 2.2.7 on 2020-01-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200109_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Отображать?'),
        ),
    ]
