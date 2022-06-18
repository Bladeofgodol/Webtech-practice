from unicodedata import name
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    # path('', views.hanna, name='ha'),
    # path('j/',views.jumua, name='ju'),
    # path('<str:name>/', name, name='name'),
    path('names/', names, name='names'),
    path('subjects/', subjects, name='subjects')
]