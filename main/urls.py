from django.urls import path, include
from .views import article_list
from .views import index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.article_list, name='article_list'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
