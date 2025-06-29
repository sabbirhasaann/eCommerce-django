from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

# Register your models here.

# class UserAdmin(BaseUserAdmin):
#     model = models.User
#     list_display = ('email', 'username', 'is_staff', 'is_active')
#     list_filter = ('is_staff', )
#     search_fields=('email','username')
#     ordering=('email',)



# admin.site.register(models.User, UserAdmin)