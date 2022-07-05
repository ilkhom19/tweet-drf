from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list),
    path('tweets/', views.author_list),
]
