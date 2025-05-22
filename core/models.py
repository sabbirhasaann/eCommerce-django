"""Core models for app"""
from django.db import models

# Create your models here.

class Item(models.Model):
    """Model for Item"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
