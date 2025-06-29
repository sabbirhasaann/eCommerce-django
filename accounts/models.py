"""Core models for app"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from .manager import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """Abstract Base User"""
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email