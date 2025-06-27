"""Core models for app"""
from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     BaseUserManager,
#     PermissionsMixin
# )

# Create your models here.


# class UserManager(BaseUserManager):
#     """User Manger"""
#     def create_user(self, email, password=None, **extra_fields):

#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     """Abstract Base User"""
#     email = models.EmailField(unique=True, max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'

class Item(models.Model):
    """Model for Item"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    """Model for Product"""
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sale = models.IntegerField()
    label = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    old_price = models.FloatField()
    new_price = models.FloatField()
    rating = models.IntegerField()