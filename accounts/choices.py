from django.db import models

class Role(models.TextChoices):
        EMPLOYEE = 'employee'
        SUPPORT = 'support'
        ADMIN = 'admin'
