from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Уникальные поля пользователя, если они есть

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Уникальное имя для связи
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Уникальное имя для связи
        blank=True
    )


