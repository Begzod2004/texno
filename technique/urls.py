from django.urls import *
from .views import *
from django.contrib import admin
from django.urls import path
from .views import profile



urlpatterns = [
    path('',indexListView.as_view(), name='index'),
    path('index.html', indexListView.as_view(), name='index'),
    path('brand.html', brand),
    path('contact.html', contact),
    path('products.html', products),
    path('about.html', about),
    path('main', main, name='main'),
    path('Brand/', BrandListView.as_view(), name='Brand'),
    path('Brand/add', BrandCreateView.as_view(), name='Brand-add'),
    path('Brand/change/<int:pk>', BrandUpdateView.as_view(), name='Brand-change'),
    path('Brand/delete/<int:pk>',
         BrandDeleteView.as_view(), name='Brand-delete'),
    path('Company/',  CompanyListView.as_view(), name='Company'),
    path('Company/add',  CompanyCreateView.as_view(), name='Company-add'),
    path('Company/change/<int:pk>',  CompanyUpdateView.as_view(), name='Company-change'),
    path('Company/delete/<int:pk>',
         CompanyDeleteView.as_view(), name='Company-delete'),
    path('Condition/',  ConditionListView.as_view(), name='Condition'),
    path('Condition/add',  ConditionCreateView.as_view(), name='Condition-add'),
    path('Condition/change/<int:pk>',  ConditionUpdateView.as_view(), name='Condition-change'),
    path('Condition/delete/<int:pk>',
         ConditionDeleteView.as_view(), name='Condition-delete'),
    path('Size/',  SizeListView.as_view(), name='Size'),
    path('Size/add',  SizeCreateView.as_view(), name='Size-add'),
    path('Size/change/<int:pk>',  SizeUpdateView.as_view(), name='Size-change'),
    path('Size/delete/<int:pk>',
         SizeDeleteView.as_view(), name='Size-delete'),


    path('Color/',  ColorListView.as_view(), name='Color'),
    path('Color/add',  ColorCreateView.as_view(), name='Color-add'),
    path('Color/change/<int:pk>',  ColorUpdateView.as_view(), name='Color-change'),
    path('Color/delete/<int:pk>',
          ColorDeleteView.as_view(), name='Color-delete') ,
    
 path('Aksiya/',  AksiyaListView.as_view(), name='Aksiya'),
    path('Aksiya/add',  AksiyaCreateView.as_view(), name='Aksiya-add'),
    path('Aksiya/change/<int:pk>',  AksiyaUpdateView.as_view(), name='Aksiya-change'),
    path('Aksiya/delete/<int:pk>',
          AksiyaDeleteView.as_view(), name='Aksiya-delete') ,
    

    path('Technique/', TechniqueListView.as_view(), name='Techniques'),
    path('Technique/add', TechniqueCreateView.as_view(), name='Technique-add'),
    path('Technique/change/<int:pk>',
         TechniqueUpdateView.as_view(), name='Technique-change'),
    path('Technique/delete/<int:pk>',
     TechniqueDeleteView.as_view(), name='Technique-delete'),
     
    path('register/', user_register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('Technique-order/<int:pk>', user_login_view, name='Technique-order'),
    path('profile/', profile, name='profile'),
    path('order/', main, name='main'),


    ] 
  

# path('', index),
