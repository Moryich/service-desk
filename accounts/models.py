from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.managers import UserManager

class User(AbstractUser):
    class Role(models.TextChoices):
        EMPLOYEE = 'employee'
        SUPPORT = 'support'
        ADMIN = 'admin'

    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()
