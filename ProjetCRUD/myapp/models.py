# Dans models.py
from django.db import models

class APIObject(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
