from django.db import models
from django.conf import settings

from tickets.choices import Status

class Ticket(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_tickets"
    )
    support = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="supported_tickets",
        null=True,
        blank=True
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(choices=Status.choices, default=Status.NEW)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(status__in=Status.values),
                name="ticket_status_valid"
            )
        ]

class Message(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="ticket_messages"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="user_messages",
        null=True,
        blank=True
    )
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
