from django.urls import path
from . import views
from . view import view

urlpatterns = [
    path('', views.index, name='index'),
    path('class', views.page01, name='class01'),
    path('external', view.index, name='external-view'),
    path('html', view.render2, name='render'),
]
