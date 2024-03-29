from django.urls import *
from .views import *
from django.contrib import admin
from django.urls import path
from .views import profile



urlpatterns = [
    path('',index, name='index'),
    path('index', index, name='index'),
    path('brand', brand, name='brand'),
    path('product/', product, name='product'),
    path('contact', contact, name='contact'),
    path('events', events, name='events'),
    path('services', services, name='services'),
    path('products', products, name='products'),
    path('checkout', checkout, name='checkout'),
    path('about', about, name='about'),
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



    path('Country/',  CountryListView.as_view(), name='Country'),
    path('Country/add',  CountryCreateView.as_view(), name='Country-add'),
    path('Country/change/<int:pk>',  CountryUpdateView.as_view(), name='Country-change'),
    path('Country/delete/<int:pk>',
          CountryDeleteView.as_view(), name='Country-delete') ,

          

    path('Aksiya_Code/',  Aksiya_CodeListView.as_view(), name='Aksiya_Code'),
    path('Aksiya_Code/add',  Aksiya_CodeCreateView.as_view(), name='Aksiya_Code-add'),
    path('Aksiya_Code/change/<int:pk>',  Aksiya_CodeUpdateView.as_view(), name='Aksiya_Code-change'),
    path('Aksiya_Code/delete/<int:pk>',
          Aksiya_CodeDeleteView.as_view(), name='Aksiya_Code-delete') ,
          

    path('Features/',  FeaturesListView.as_view(), name='Features'),
    path('Features/add',  FeaturesCreateView.as_view(), name='Features-add'),
    path('Features/change/<int:pk>',  FeaturesUpdateView.as_view(), name='Features-change'),
    path('Features/delete/<int:pk>',
          FeaturesDeleteView.as_view(), name='Features-delete') ,

          
    
    path('Aksiya/',  AksiyaListView.as_view(), name='Aksiya'),
    path('Aksiya/add',  AksiyaCreateView.as_view(), name='Aksiya-add'),
    path('Aksiya/change/<int:pk>',  AksiyaUpdateView.as_view(), name='Aksiya-change'),
    path('Aksiya/delete/<int:pk>',
          AksiyaDeleteView.as_view(), name='Aksiya-delete') ,
    

    path('Technique/', TechniqueListView.as_view(), name='Technique'),
    path('Technique/<int:pk>', TechniqueDetailView.as_view(), name='TechniqueDetailView'),
    path('Technique/add', TechniqueCreateView.as_view(), name='Technique-add'),
    path('Technique/change/<int:pk>',
         TechniqueUpdateView.as_view(), name='Technique-change'),
    path('Technique/delete/<int:pk>',
     TechniqueDeleteView.as_view(), name='Technique-delete'),
     
    path('register/', user_register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('Technique-order/<int:pk>', user_login_view, name='Technique-order'),
    path('profile/', profile, name='profile'),
    path('registeratsiya/', profile, name='registeratsiya'),
    


    ] 
  

# path('', index),
