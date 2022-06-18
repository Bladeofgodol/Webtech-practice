from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.named),
    path('name/<str:name>/', views.great),
    path('index1/<str:name>/', views.index),
    path('index2/', views.courses),
    path('index3/', views.classes),
    path('index4/', views.press)
    ]