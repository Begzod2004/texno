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
    path('condition/',  conditionListView.as_view(), name='condition'),
    path('condition/add',  conditionCreateView.as_view(), name='condition-add'),
    path('condition/change/<int:pk>',  conditionUpdateView.as_view(), name='condition-change'),
    path('condition/delete/<int:pk>',
         conditionDeleteView.as_view(), name='condition-delete'),
    path('size/',  sizeListView.as_view(), name='size'),
    path('size/add',  sizeCreateView.as_view(), name='size-add'),
    path('size/change/<int:pk>',  sizeUpdateView.as_view(), name='size-change'),
    path('size/delete/<int:pk>',
         sizeDeleteView.as_view(), name='size-delete'),

    path('technique/', techniqueListView.as_view(), name='techniques'),
    path('technique/add', techniqueCreateView.as_view(), name='technique-add'),
    path('technique/change/<int:pk>',
         techniqueUpdateView.as_view(), name='technique-change'),
    path('technique/delete/<int:pk>',
     techniqueDeleteView.as_view(), name='technique-delete'),
     
    # path('register/', user_register_view, name='register'),
    # path('login/', user_login_view, name='login'),
    # path('technique-order/<int:pk>', user_login_view, name='technique-order'),
    path('admin/', admin.site.urls),
    path('profile/', profile, name='profile'),
    path('order/', main, name='main'),


    ] 
  

# path('', index),
