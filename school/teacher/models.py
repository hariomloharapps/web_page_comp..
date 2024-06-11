from django.contrib.auth.models import AbstractUser
from django.db import models

class App2User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='app2user_set',  # Unique related_name for App2User
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='app2user_set',  # Unique related_name for App2User
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    # Add any extra fields for app2 users
    pass
