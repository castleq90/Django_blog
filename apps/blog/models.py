from django.db import models
from config.settings  import settings

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()