from django.db import models

class Post(models.Model):
    TEXT = "text"
    VIDEO = "video"

    POST_TYPES = [(TEXT, "Text"), (VIDEO, "Video")]

    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=POST_TYPES)
    content = models.TextField()
    tags = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
