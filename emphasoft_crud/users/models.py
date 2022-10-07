from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'Username',
        max_length=150,
        unique=True,
        db_index=True,
    )
    first_name = models.CharField(
        'First name',
        max_length=30,
    )
    last_name = models.CharField(
        'last name',
        max_length=150,
    )
    password = models.CharField(
        'Password',
        max_length=150,
        blank=False,
    )

    class Meta:
        ordering = ['-username']
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.username
