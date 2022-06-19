from django.test import TestCase

# Create your tests here.
from django.urls import *
from .views import *


urlpatterns = [
    path('test-api-view/', test_api_view),
    path('technique-api-view/', techniqueListAPIView.as_view()),
    path('technique-api-view/create', techniqueCreateAPIView.as_view()),
    path('technique-api-view/update/<int:pk>', techniqueUpdateAPIView.as_view()),
    path('technique-api-view/delete/<int:pk>', techniqueDestroyAPIView.as_view()),
    
    path('technique-api-view/<int:pk>/', technique_api_view),path('test-api-view/', test_api_view),
    
    path('Brand-api-view/', BrandListAPIView.as_view()),
    path('Brand-api-view/create', BrandCreateAPIView.as_view()),
    path('Brand-api-view/update/<int:pk>', BrandUpdateAPIView.as_view()),
    path('Brand-api-view/delete/<int:pk>', BrandDestroyAPIView.as_view()),
    path('Brand-api-view/<int:pk>/', Brand_api_view),
    
    
    path('size-api-view/', sizeListAPIView.as_view()),
    path('size-api-view/create', sizeCreateAPIView.as_view()),
    path('size-api-view/update/<int:pk>', sizeUpdateAPIView.as_view()),
    path('size-api-view/delete/<int:pk>', sizeDestroyAPIView.as_view()),
    
    path('size-api-view/<int:pk>/', size_api_view),
    

    path('Company-api-view/', CompanyListAPIView.as_view()),
    path('Company-api-view/create', CompanyCreateAPIView.as_view()),
    path('Company-api-view/update/<int:pk>', CompanyUpdateAPIView.as_view()),
    path('Company-api-view/delete/<int:pk>', CompanyDestroyAPIView.as_view()),
    
    path('Company-api-view/<int:pk>/', Company_api_view),

    

    path('auth/', include('rest_framework.urls')),
]
