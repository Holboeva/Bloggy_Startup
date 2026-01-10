from django.db import models
from django.conf import settings


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_groups"
    )

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="member_groups",
        blank=True
    )

    is_private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
