from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        'Username',
        max_length=150,
        # min_length=1,  # TODO implement via min_length validator
        # TODO pattern: ^[\w.@+-]+$
        unique=True,
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
        # TODO pattern: ^(?=.*[A-Z])(?=.*\d).{8,}$
        max_length=150,
        # min_length=1,  # TODO implement via min_length validator
        blank=False,
    )
    is_active = models.BooleanField(  # TODO how to inherit attributes from parent class?
        'Active',
        default=True,
        blank=False,
    )
    is_superuser = models.BooleanField(
        'Superuser status',
        default=False,
        blank=False,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.username
