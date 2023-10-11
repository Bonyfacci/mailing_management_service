from django.contrib.auth.models import AbstractUser
from django.db import models

from app_send_mail.models import NULLABLE


class User(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='Страна', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)

    # Верификация почты пользователя
    code_verification = models.CharField(max_length=20, **NULLABLE, verbose_name='Ключ Активации')
    is_verified = models.BooleanField(default=False, verbose_name='Активирован')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-is_superuser', '-is_staff', )
