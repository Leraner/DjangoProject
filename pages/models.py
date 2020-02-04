from django.db import models
from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri


class Page(models.Model):
    title = models.CharField('Название', max_length=225)
    text = models.TextField('Текст')
    active = models.BooleanField('вкл/выкл', default=True)
    slug = models.CharField('url', max_length=100, unique=True)
    edit_date = models.DateTimeField('Дата редактирования', auto_now=True, blank=True, null=True)
    published_date = models.DateTimeField('Дата публикация', blank=True, null=True)
    published = models.BooleanField('Опубликовать?', default=True)
    template = models.CharField('Шаблон', max_length=500, default='pages/home.html')
    registration_required = models.BooleanField(
        'Требуется регистрация',
        help_text='Если флажок установлен, только зарегестрированные пользователи могут просматривать страницу',
        default=False
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Метод чтобы правильно выставился url"""
        # Чтобы сделать гл.страницу
        if self.slug is None:
            self.slug = '/'
            # Если в начале slug нет /, то мы его добавляем
        if not f'{self.slug}'.startswith('/'):
            self.slug ='/' + self.slug
            # Если в конце slug нет /, то мы его добавляем
        if not self.slug.endswith('/'):
            self.slug += '/'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Построение правильного пути url
        Чтобы были учтены все /, то как url написан, нет ли каких-то определённых символов, соответствует ли utf-8 и т.д
        """
        return iri_to_uri(get_script_prefix().rstrip('/') + self.slug)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
