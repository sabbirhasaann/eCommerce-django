from django.contrib import admin
from django.urls import path
from .pages import product1
from . import views

urlpatterns = [
    path('', product1.product, name="product1"),
    path('products/', views.product_list, name="products"),
    path('product/add', views.add_product, name="add-product"),
    path('product/add/new', views.added_product, name="added_product")
]
