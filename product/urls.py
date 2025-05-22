from django.contrib import admin
from django.urls import path
from .pages import product1

urlpatterns = [
    path('', product1.product, name="product1"),
]
