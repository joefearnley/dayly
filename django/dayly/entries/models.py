from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Entry(models.Model):
    body = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, null=False, blank=False)
    date_created = models.DateTimeField("date created", default=now)
    date_published = models.DateTimeField("date published")
    date_updated = models.DateTimeField("date updated", default=now)
