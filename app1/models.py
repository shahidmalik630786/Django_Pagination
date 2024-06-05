from django.db import models

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    disc = models.TextField(max_length=500)
    publish_date = models.DateTimeField(max_length=100)
