from django.urls import *
from .views import *
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('',index, name='index'),
    path('index', index, name='index2'),
    path('index_1', index1, name='index_1'),
    ] 
  

# path('', index),
