from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель пользователя."""

    phone = PhoneNumberField(
        'Номер телефона',
        unique=True,
    )
    confirmation_code = models.PositiveSmallIntegerField(
        '4-х значный код подтверждения',
        blank=True,
        null=True
    )
    self_invite_code = models.CharField(
        'Инвайт-код пользователя',
        max_length=6,
        blank=True,
        null=True,
        unique=True
    )
    alien_invite_code = models.CharField(
        'Инвайт-код для добавления пользователя',
        max_length=6,
        blank=True,
        null=True,
        unique=True
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone
