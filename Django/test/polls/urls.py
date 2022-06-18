from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('2', views.index2, name='index2'),
    path('3', views.index3, name='index3'),
    path('4', views.index4, name='index4')
]