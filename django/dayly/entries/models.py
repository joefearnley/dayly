from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField("date created")
    date_published = models.DateTimeField("date published")
    date_updated = models.DateTimeField("date updated")
