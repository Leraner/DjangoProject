# Generated by Django 2.2.7 on 2020-01-03 10:52

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('is_auth', models.BooleanField(default=False, verbose_name='Для зарегистрированных или нет')),
                ('active', models.BooleanField(default=True, verbose_name='вкл/выкл')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='Название пункати меню на сайте')),
                ('title', models.CharField(max_length=225, verbose_name='Название латиницей')),
                ('status', models.BooleanField(default=False, verbose_name='вкл/выкл')),
                ('is_auth', models.BooleanField(default=False, verbose_name='Для зарегистрированных или нет')),
                ('anchor', models.CharField(blank=True, max_length=225, null=True, verbose_name='Якорь')),
                ('url', models.CharField(max_length=225, verbose_name='url на внешний ресурс')),
                ('active', models.BooleanField(default=True, verbose_name='вкл/выкл')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu', verbose_name='Меню')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.MenuItems', verbose_name='Родительский пункт')),
            ],
            options={
                'verbose_name': 'Пункты меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]
