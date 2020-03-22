from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
import random


class Profile(models.Model):
    author = models.OneToOneField(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    status = models.CharField('Статус', max_length=100, null=True, blank=True)
    image = models.ImageField('Главная фотография', upload_to='users/', null=True, blank=True)
    published = models.BooleanField('Отображать?', default=True)
    slug = models.CharField(
        'url',
        max_length=10,
        unique=True,
        blank=False,
        null=False,
        default=str(random.randint(0, 10000000))
    )
    create_data = models.DateTimeField(
        'Дата редактирования',
        default=timezone.now,
        blank=True,
        null=True,
    )

    # def save(self, *args, **kwargs):
    #     """Метод чтобы правильно выставился url"""
    #     if not f'{self.slug}'.startswith('/'):
    #         self.slug = '/' + self.slug
    #         # Если в конце slug нет /, то мы его добавляем
    #     if not self.slug.endswith('/'):
    #         self.slug += '/'
    #     super().save(*args, **kwargs)

    def __str__(self):
        return str(self.author)

    # def get_absolute_url(self):
    #     return reverse("detail_profile", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        Profile.objects.create(author=instance)  # id=instance.id
        send_mail(
            # 'Subject here',           - title письма
            # 'Here is the message.',   - body письма
            'danilachuprin2004@gmail.com',
            [str(User.email)],
            fail_silently=False,
        )


@receiver
def save_user_profile(sender, instance, **kwargs):
    """Сохранение профиля пользователя"""
    instance.profile.save()
