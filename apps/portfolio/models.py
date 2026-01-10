from django.db import models
from django.conf import settings


class Portfolio(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="portfolio"
    )

    template = models.CharField(max_length=50, default="default")
    content = models.JSONField(default=dict)

    custom_domain = models.CharField(max_length=255, null=True, blank=True)
    is_premium = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
