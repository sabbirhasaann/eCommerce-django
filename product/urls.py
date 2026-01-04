from django.contrib import admin
from django.urls import path
from .pages import product1
from . import views
from . import category_view

urlpatterns = [
    path("", product1.product, name="product1"),
    path("products/", views.product_list, name="products"),
    path("product/add", views.add_product, name="add-product"),
    path("product/add/new", views.added_product, name="added_product"),
    path("product/category/", category_view.category, name="category"),
    path("product/categories/", category_view.categories, name="categories"),
]
