from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

# Register your models here.

class UserAdmin(BaseUserAdmin):
    model = models.User


admin.site.register(models.User)