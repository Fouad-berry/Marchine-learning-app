from django.urls import path, include
from .views import index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
