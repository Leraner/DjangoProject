from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.conf import settings


class Menu(models.Model):
    """Модель меню"""
    name = models.CharField('Название', max_length=100)
    is_auth = models.BooleanField('Для зарегистрированных или нет', default=False)
    active = models.BooleanField('вкл/выкл', default=True)
    published = models.BooleanField('Отображать?', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItems(MPTTModel):
    """Модель пунктов меню"""
    name = models.CharField('Название пункати меню на сайте', max_length=225)
    title = models.CharField('Название латиницей', max_length=225)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительский пункт',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(
        Menu,
        verbose_name='Меню',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    status = models.BooleanField('вкл/выкл', default=False)
    is_auth = models.BooleanField('Для зарегистрированных или нет', default=False)
    anchor = models.CharField('Якорь', max_length=225, null=True, blank=True)
    url = models.CharField('url на внешний ресурс', max_length=225, null=True, blank=True)
    active = models.BooleanField('вкл/выкл', default=True)
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Ссылка на',
        # Сколько будем отрображать из выпадающего списка
        limit_choices_to=settings.MENU_APPS,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(verbose_name='id записи', default=1, null=True)
    # Соединяет content_type и object_id, потому что при завязке ContentType надо указать id записи
    content_object = GenericForeignKey('content_type', 'object_id')
    sort = models.PositiveIntegerField('Порядок', default=0)
    published = models.BooleanField('Отображать?', default=True)

    def get_anchor(self):
        if self.anchor:
            # ставит текущий домен и прибавляет якорь через #
            return '{}/#{}'.format(Site.objects.get_current().domain, self.anchor)
        else:
            return False

    def __str__(self):
        return self.name

    content_object.short_description = 'ID'

    class Meta:
        verbose_name = 'Пункты меню'
        verbose_name_plural = 'Пункты меню'
