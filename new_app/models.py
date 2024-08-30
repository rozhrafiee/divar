from django.db import models
from django.contrib.auth.models import User


class Tracket(models.Model):
    title = models.CharField(max_length=225)
    price = models.PositiveBigIntegerField()
    description = models.TextField()