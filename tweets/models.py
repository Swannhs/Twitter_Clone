from django.db import models


# Create your models here.
class Tweet(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(unique='images/', blank=True, null=True)
