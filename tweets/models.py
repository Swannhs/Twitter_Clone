from django.db import models


# Create your models here.
class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(unique='images/', blank=True, null=True)

