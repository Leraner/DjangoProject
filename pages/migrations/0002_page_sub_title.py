# Generated by Django 2.2.7 on 2020-02-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='sub_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Подзаголовок'),
        ),
    ]
