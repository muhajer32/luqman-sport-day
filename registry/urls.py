from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('success/', views.success, name='success'),
]
# This file defines the URL patterns for the registry app, mapping URLs to views.