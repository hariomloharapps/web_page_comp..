from django.contrib.auth.models import AbstractUser
from django.db import models

class PrincipalUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='principal_set',  # Unique related_name for App1User
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='principal_set',  # Unique related_name for App1User
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    # Add any extra fields for app1 users
    pass



class Principal(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    

class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    admission_date = models.DateField()
    grade = models.CharField(max_length=10)
    performance = models.TextField()
    attendance_records = models.TextField()
    disciplinary_actions = models.TextField()
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_fee = models.DecimalField(max_digits=10, decimal_places=2)
    attendance_percentage = models.FloatField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



