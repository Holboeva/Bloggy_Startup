from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    skills = models.JSONField(default=list)
    location = models.CharField(max_length=100, blank=True)
    portfolio_subdomain = models.CharField(max_length=100, unique=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

