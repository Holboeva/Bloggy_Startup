from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    # skills: ["Python", "Django", "Startup"]
    skills = models.JSONField(default=list, blank=True)

    # username.bloggy.uz
    portfolio_subdomain = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
