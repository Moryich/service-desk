from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from accounts.managers import UserManager
from accounts.choices import Role

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    role = models.CharField(choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        constraints = [
            models.CheckConstraint(
                condition=models.Q(role__in=Role.values),
                name="user_role_valid"
            )
        ]

class Invite(models.Model):
    inviter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="sent_invites"
    )
    email = models.EmailField()
    role = models.CharField(choices=Role.choices)
    token_hash = models.CharField(max_length=64, unique=True)
    expires_at = models.DateTimeField()
    used_at = models.DateTimeField(null=True, blank=True)
    revoked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(role__in=Role.values),
                name="invite_role_valid"
            )
        ]
